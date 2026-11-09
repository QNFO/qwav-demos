# BT-Tree QEC: Staircase Redundancy Demo

**Interactive computational proof of concept** for: *Ultrametric Code Spaces: The Bruhat--Tits Tree as a Geometry for Quantum Error Correction* — DOI: [10.5281/zenodo.21817596](https://doi.org/10.5281/zenodo.21817596).

Live: [https://qnfo.github.io/qwav-demo-bt-qec/](https://qnfo.github.io/qwav-demo-bt-qec/)

## What this demonstrates

| Paper claim | Computed in demo | Verify by |
|:------------|:-----------------|:----------|
| Ultrametric redundancy is a staircase, not smooth | `engine.getStaircase(d)` → `[1, p, p^2, ...]` | Redundancy curve tab; count horizontal steps |
| Error confinement is ultrametric | `engine.getErrorSubtree(id)` → subtree only | Error mode; click a node |
| QEC-Darwinism coexistence windows | Flat segments between staircase steps | Compare Archimedean: smooth line has none |

## How to use

| Control | What it does |
|:--------|:-------------|
| Prime 2/3/5 | Rebuild the Bruhat-Tits tree for that p |
| Depth slider | Change number of tree levels (1-6) |
| Tree geometry tab | Hover/click nodes; selection shows root path |
| Redundancy curve tab | The staircase; toggle Compare for Archimedean |
| Inject error | Click a node: only its subtree is affected |
| Reset | Clear selections and restore default |

## Verification (all passing, 2026-08-06)

| Layer | Check | Result |
|:------|:------|:-------|
| Syntax | `node --check` on engine | PASS |
| Unit | Golden values (p^d nodes, staircase, error subtree) | PASS |
| Chrome suite | 15/15 checks (every control clicked, state asserted, 0 console errors, desktop+mobile) | PASS |
| Live | HTTP 200 + engine marker on deployed URL | PASS |

Golden values from the paper's math: p-ary tree depth d has p^d nodes at max depth (e.g. p=2,d=3 → 8); error subtree of node at depth k with r levels below = 1+p+...+p^r.

## Run locally

```bash
git clone https://github.com/QNFO/qwav-demo-bt-qec.git
cd qwav-demo-bt-qec
python -m http.server 8765   # or just open index.html
```

Test in DevTools:
```js
window._demo.tree.getRedundancy(3)         // 8 (p=2)
window._demo.tree.getErrorSubtree(2).size  // 7
```


## Screenshots (from the Chrome automated test suite)

| Tree geometry | Redundancy curve | Mobile |
|:--------------|:-----------------|:-------|
| ![tree](screenshots/view-tree.png) | ![curve](screenshots/view-curve.png) | ![mobile](screenshots/view-mobile.png) |

## Deployment

Native GitHub Pages (gh-pages branch). Update: `git checkout gh-pages && git add index.html && git commit -m "update" && git push origin gh-pages`. No CI config.

License: QNFO Unified License Agreement (QNFO-ULA). Companion demo to DOI 10.5281/zenodo.21817596.
