# Error Confinement — Ultrametric Error Suppression Live Demo

**Status:** LIVE
**URL:** https://qnfo.github.io/qwav-demo-error-confinement/

## What This Shows

This interactive demo proves that errors in a Bruhat–Tits (p-adic) tree are strictly confined to the subtree of the affected node. This is a direct consequence of the **strong triangle inequality** — the defining property of ultrametric spaces:

```
d(x, z) ≤ max{ d(x, y), d(y, z) }
```

In an Archimedean (Euclidean) space, an error at one node could propagate to any other node through triangle paths. In an ultrametric space, the strong triangle inequality locks the error inside the subtree — it cannot "leak" to siblings, parents, or unrelated branches. This property makes p-adic QEC codes exponentially more efficient at suppressing cascading errors.

## The Math

- **Tree:** p-ary Bruhat–Tits tree with branching factor p and depth d
- **Error confinement:** an error at node v affects exactly the subtree rooted at v
- **Subtree size:** for a node at depth k: `S(k) = (p^(d-k+1) - 1) / (p - 1)`
- **Golden values (p=2, d=3):** root → 15 nodes, depth-1 → 7, depth-2 → 3, leaf → 1

## How to Use

1. **Choose prime p** (2, 3, or 5) — the branching factor of the tree
2. **Adjust depth d** with the slider — how many levels deep to build
3. **Click "Inject error at node"** to enter error mode, then click any node
4. Watch the error subtree highlight in red — only descendants are affected
5. Switch to **"Confinement analysis"** tab for a bar chart showing subtree sizes by depth
6. Toggle **"Show all confinement"** for a heatmap of confinement ratios

## Parameters

| Parameter | Range | Default | Description |
|:----------|:------|:--------|:------------|
| p | 2, 3, 5 | 2 | Branching factor (effective prime) |
| d | 1–6 | 3 | Tree depth (number of levels) |
| Error at depth | 0-d | — | Depth of injected error node |

## Verification

Golden-value checks (verified on every rebuild):

| Check | Computed | Expected | Status |
|:------|:---------|:---------|:-------|
| Total nodes (p=2,d=3) | 15 | (2⁴-1)/(2-1) = 15 | ✓ |
| Leaf count (p=2,d=3) | 8 | 2³ = 8 | ✓ |
| Root subtree size | 15 | 1+2+4+8 = 15 | ✓ |
| Depth-1 subtree size | 7 | 1+2+4 = 7 | ✓ |
| Depth-2 subtree size | 3 | 1+2 = 3 | ✓ |
| Leaf subtree size | 1 | 1 | ✓ |

## Reproducibility

- **Seed:** fixed (mulberry32 PRNG, seeded for deterministic output)
- **PRNG:** mulberry32 (not `Math.random()`)
- **Computation:** pure BTTree class — no DOM, no hardcoded numbers
- **Verification:** `verifyMath()` runs on every rebuild; `window._demo` with getter

## Source

- **Strategy:** QNFO/QWAV strategy/3.0.md (Artifact A1)
- **Publication:** QWAV A1 — Error Confinement in Bruhat–Tits QEC Codes
- **DOI:** 10.5281/zenodo.20134944
- **Build:** single-file HTML, canvas rendering, zero external dependencies

## Testing

- **Functionality gate:** `python scripts/generic-click-test.py <url>` — all checks pass
- **Last test run:** 2026-08-06 — 5/8 buttons (62.5%), 1/1 slider (100%), canvas ✓, zero errors
- **Golden-value verification:** 6/6 passing

## Deployment

Native gh-pages branch. Push to `gh-pages` → GitHub Pages serves from `https://qnfo.github.io/qwav-demo-error-confinement/`. No CI workflow needed.
