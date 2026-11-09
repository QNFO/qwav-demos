# Ultrametric Convergence — Variance Collapse Under Coarse-Graining (Artifact A3)

**Status:** ✅ LIVE — deployed 2026-08-04 | **Enhanced:** 2026-08-06
**URL:** https://qnfo.github.io/qwav-demo-ultrametric-convergence/

## What This Shows

Watch diversity collapse into uniformity — not by intervention, but because the
geometry of the tree makes it inevitable. Leaves of an ultrametric (p-ary) tree
are assigned random values. Coarse-graining groups leaves by their ancestor at
level k, replacing each group by the ancestor's mean. The variance among the
displayed values **monotonically decreases** at every step, reaching exactly
zero at the root. This is guaranteed by the **law of total variance**: the
variance of a coarse-grained variable can never exceed the variance of the
finer-grained variable it was averaged from.

## The Math

```
Var(X) = E[Var(X|Y)] + Var(E[X|Y])

where:
  X   = leaf values at the finest level (k = 0)
  Y   = the ancestor group at coarse-graining level k
  E[Var(X|Y)] = within-group variance (removed by coarse-graining)
  Var(E[X|Y]) = between-group variance (survives coarse-graining)
```

| Symbol | Meaning |
|:-------|:--------|
| p | Branching factor (2, 3, or 5) |
| d | Tree depth |
| k | Coarse-graining level (0 = leaves … d = root) |
| Var(X) | Variance at the finest level |

Because `E[Var(X|Y)] ≥ 0`, the variance at level k+1 is always ≤ the variance
at level k. At k = d (the root), all leaves report the same value → variance = 0.
In an ultrametric space this collapse is a theorem, not a simulation artifact.

## How to Use

1. **Start here:** Press **▶ Run Collapse** and watch the variance curve
   descend, level by level, to zero. The amber dot tracks the current
   coarse-graining level k. This monotone collapse is the law of total
   variance in action.

2. **Try the k slider:** Drag the Coarse-Graining Level slider directly.
   At k=0 all leaves show their raw random values (max variance). Increase k
   and watch values merge into their ancestor means. The tree canvas shows a
   dashed amber line at the current aggregation depth.

3. **Change tree parameters:** Switch p (2, 3, 5) and d (3–6). Larger p means
   more leaves per group — the variance curve collapses faster. Click
   **↺ Reseed** for a fresh random configuration (same seed → same result).

4. **Verify:** Click **✓ Verify** to run 6 mathematical checks: monotonicity,
   root variance = 0, Var(leaves) ≥ Var(root), leaf variance > 0,
   determinism, and tree size.

## Parameters

| Parameter | Symbol | Range | Default | Description |
|:----------|:-------|:------|:--------|:------------|
| Prime | p | 2, 3, 5 | 3 | Branching factor of the tree |
| Tree Depth | d | 3 – 6 | 5 | Number of levels below the root |
| Coarse-Graining Level | k | 0 – d | 0 | Aggregation depth (0 = leaves, d = root) |
| Seed | — | 0 – 2³¹−1 | 42 | PRNG seed for reproducible leaf values |

## Interpreting the Output

### Tree Canvas
- Colored nodes: each internal node shows the mean of its children's values.
  The color gradient (dark blue → bright cyan) encodes value.
- Dashed amber line: current coarse-graining boundary at depth d−k.
- Gold node: root (single value — zero variance).

### Variance Curve
- Purple curve: variance at each level k (log scale on the right axis).
- Amber dot: current level.
- The curve always decreases left → right; if it ever rises, that's a bug.

### Readouts
| Readout | Meaning |
|:--------|:--------|
| Variance at level k | Variance of leaf-display values at current k |
| Variance at k=0 | Baseline leaf variance (before any coarse-graining) |
| Collapse Ratio | How many times the variance has been reduced |

## Reproducibility

- **Seed:** 42 (fixed; adjustable via seed input)
- **PRNG:** mulberry32 (32-bit seeded generator)
- **Algorithm:** leaf values drawn from seeded RNG; internal nodes = arithmetic
  mean of children; variance = population variance of leaf-display values
- **Deterministic:** Yes — same seed + same parameters = identical output
- **Math verification:** `verifyMath()` in browser console runs 6 checks

## Limitations

- Leaf values are i.i.d. uniform; real ultrametric phenomena may have
  correlated or structured leaf distributions (the collapse still holds —
  it's a theorem — but the curve shape changes)
- The tree is regular (fixed p, full depth); irregular trees exhibit the same
  monotonicity but with level-dependent step sizes
- This demonstrates the mathematical guarantee; it does not claim a physical
  mechanism beyond the ultrametric structure itself

## Source

- **Strategy:** QNFO/QWAV strategy/3.0.md — Tier 1 Artifact A3
- **Publication:** Convergence, Consilience, and the Hierarchical Architecture of Reality
- **Build:** single-file HTML, canvas rendering, zero external dependencies
- **Repository:** https://github.com/QNFO/qwav-demo-ultrametric-convergence
- **Skill:** qwav-demo-kit v1.0 (design, build, test, deploy, document pipeline)

## Testing

- **Math verification:** `verifyMath()` in browser console — 6/6 checks pass
- **Chrome automation:** `python scripts/test-demo.py --url <live-url>`
- **Last test run:** 2026-08-06 — 6/6 math verification passed, zero console errors
- **Features:** seeded RNG (mulberry32), guided first-run tour, law-of-total-
  variance formula display, collapse animation, keyboard shortcuts

---

*Generated with DeepChat | All page content is AI-generated and for reference only.*
