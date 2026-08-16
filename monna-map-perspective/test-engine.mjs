// test-engine.mjs — golden-value assertions for the Monna Map Perspective Renderer (UMP.010 C5).
// Run: node test-engine.mjs   (exit 0 = all pass, 1 = any fail)
// Identities from the paper: Non-Archimedean Projective Perspective, 10.5281/zenodo.21969784 (§3-§4).

function pAdicDigits(x, p, K) {
  // x >= 0: repeated division. x < 0: borrow-based complement
  // (no huge-mod arithmetic — x + p^K loses small x beyond 2^53).
  const d = [];
  if (x >= 0) {
    let t = x;
    for (let k = 0; k < K; k++) { d.push(t % p); t = Math.floor(t / p); }
  } else {
    let a = -x, carry = 0;
    for (let k = 0; k < K; k++) {
      const ak = a % p;
      a = Math.floor(a / p);
      d.push((p - ak - carry + p) % p);
      carry = (ak + carry > 0) ? 1 : 0;
    }
  }
  return d;
}
function monnaRational(x, p, K = 24) {
  const d = pAdicDigits(x, p, K);
  let num = 0, den = 1;
  for (let k = 0; k < K; k++) {
    const pk = Math.pow(p, k);
    num = num * pk + d[k] * den;
    den = den * pk;
  }
  return { num, den, value: num / den };
}
function naiveSize(k, p, n) { return { raw: Math.pow(p, k), norm: Math.pow(p, k - n) }; }
function renderedSize(k, p) {
  const r = monnaRational(Math.pow(p, k), p).value;
  return { r, size: 1 / (1 + r) };
}
function verifyMath(p, n) {
  // Tolerance 1e-6 covers the K=24 truncation bound p^{1-K} (worst p=2: ~1.2e-7).
  const T = 1e-6;
  const tests = [
    ["M(1) = 1", 1, monnaRational(1, p).value],
    ["M(p) = 1/p", 1 / p, monnaRational(p, p).value],
    ["M(p^2) = 1/p^2", 1 / (p * p), monnaRational(p * p, p).value],
    ["M(-1) = p", p, monnaRational(-1, p).value],
    ["M(-p^2) = 1/p", 1 / p, monnaRational(-p * p, p).value],
    ["M(1+p) = 1 + 1/p", 1 + 1 / p, monnaRational(1 + p, p).value],
    ["naive ratio p^{k+1}/p^k = p", p, naiveSize(2, p, 8).raw / naiveSize(1, p, 8).raw],
  ];
  const res = tests.map(([name, exp, got]) => ({
    name, exp, got, pass: Math.abs(got - exp) <= T * Math.max(1, Math.abs(exp)),
  }));
  let smooth = true;
  for (let k = 0; k < n; k++) {
    const a = renderedSize(k, p).size, b = renderedSize(k + 1, p).size;
    if (a > 0 && b / a > p - 1e-9) smooth = false;
  }
  res.push({ name: "rendered smooth (no p-fold jumps)", exp: true, got: smooth, pass: smooth });
  return res;
}

// ===== run over the full parameter space (invariant sweep) =====
let allPass = true, total = 0;
for (const p of [2, 3, 5]) {
  for (const n of [1, 3, 5, 8]) {
    const res = verifyMath(p, n);
    total += res.length;
    for (const r of res) {
      if (!r.pass) { allPass = false; console.log(`FAIL p=${p} n=${n}: ${r.name} exp=${r.exp} got=${r.got}`); }
    }
  }
}
console.log(`golden-value sweep: ${total} assertions, ${allPass ? "ALL PASS" : "FAILURES"}`);
process.exit(allPass ? 0 : 1);
