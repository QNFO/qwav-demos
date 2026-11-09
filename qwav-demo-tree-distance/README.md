# Tree Distance Sandbox — Cophenetic, Euclidean & Ultrametric Distances (Artifact A4)

**Status:** ✅ LIVE — deployed 2026-08-04 | **Enhanced:** 2026-08-06
**URL:** https://qnfo.github.io/qwav-demo-tree-distance/

## What This Shows

Three ways to measure distance between leaves of a weighted tree — and why the
ultrametric one behaves so differently. Cophenetic distance counts edges to the
lowest common ancestor (LCA). Euclidean distance uses coordinates in the
embedding. Ultrametric distance is p^(−depth of LCA) and satisfies the **strong
triangle inequality**: for any three points, the two largest distances are
equal. This "triadic rigidity" is a theorem of ultrametric spaces — and it makes
hierarchical clustering well-defined in a way Euclidean geometry is not.

## The Math

```
d_coph(a,b) = depth(LCA(a,b))
d_ultra(a,b) = p^(−depth(LCA(a,b)))
d_eucl(a,b) = √(Σᵢ (aᵢ − bᵢ)²)

Triadic rigidity:  among any three points a,b,c,
  the two largest of {d(a,b), d(b,c), d(a,c)} are EQUAL
```

| Symbol | Meaning |
|:-------|:--------|
| p | Branching factor (prime) |
| d | Tree depth |
| LCA(a,b) | Lowest common ancestor of leaves a and b |
| d_coph | Cophenetic distance (0 = same node, d = leaves diverge at root) |
| d_ultra | Ultrametric distance (1 = same node, p^(−d) = root divergence) |
| d_eucl | Euclidean distance in the 2D embedding |

## How to Use

1. **Start here:** Click **🎲 Random Pair** to select two leaves (cyan A, amber
   B). Their three distances appear in the readout panel. The green ring marks
   their lowest common ancestor.

2. **Click leaves directly:** Click any leaf on the tree canvas to select it.
   First click = leaf A, second = leaf B, third restarts.

3. **Watch triadic rigidity:** Click **✓ Verify**. The check selects three
   spread-out leaves and confirms the two largest ultrametric distances are
   equal — a property that fails for Euclidean distance in general.

4. **Change the tree:** Switch p (2, 3, 5) and d (3–6) to see how distances
   scale. Higher p → leaves spread wider → larger cophenetic depth values.

## Parameters

| Parameter | Symbol | Range | Default | Description |
|:----------|:-------|:------|:--------|:------------|
| Prime | p | 2, 3, 5 | 3 | Branching factor of the tree |
| Tree Depth | d | 3 – 6 | 4 | Number of levels below the root |
| Seed | — | 0 – 2³¹−1 | 42 | PRNG seed for edge weights |

## Interpreting the Output

### Tree Canvas
- Purple nodes: internal tree nodes (leaf labels on the bottom row).
- Cyan A / amber B: the two selected leaves.
- Green ring: the lowest common ancestor — the distance reference point.

### Distance Bars
- Three bars: Cophenetic (cyan), Euclidean (violet), Ultrametric (amber).
- Cophenetic is measured in levels (0–d), ultrametric in probability-like
  values (p^(−depth), so 1 at identity down to p^(−d)).

### Readouts
| Readout | Meaning |
|:--------|:--------|
| Cophenetic Distance | Number of levels to the LCA |
| Euclidean Distance | Straight-line distance in the 2D embedding |
| Ultrametric Distance | p^(−depth of LCA) |
| Triadic Rigidity | Status note (run ✓ Verify for the proof check) |

## Reproducibility

- **Seed:** 42 (fixed; adjustable via seed input)
- **PRNG:** mulberry32 (32-bit seeded generator)
- **Algorithm:** p-ary tree; weights assigned from seeded RNG; distances
  computed from LCA depth (cophenetic, ultrametric) and embedding coords
  (Euclidean)
- **Deterministic:** Yes — same seed + same parameters = identical distances
- **Math verification:** `verifyMath()` in browser console runs 7 checks
  including triadic rigidity

## Limitations

- The Euclidean distance is computed in the synthetic 2D embedding, not in a
  learned or biological feature space; absolute values are only meaningful
  relative to each other
- The tree is regular and symmetric; real phylogenies / hierarchies are
  irregular and weighted differently per edge
- Triadic rigidity is verified on three fixed sample leaves; it holds for all
  triples by construction of the ultrametric metric

## Source

- **Strategy:** QNFO/QWAV strategy/3.0.md — Tier 1 Artifact A4
- **Publication:** Tree Distance Cophenetic (QNFO)
- **Build:** single-file HTML, canvas rendering, zero external dependencies
- **Repository:** https://github.com/QNFO/qwav-demo-tree-distance
- **Skill:** qwav-demo-kit v1.0 (design, build, test, deploy, document pipeline)

## Testing

- **Math verification:** `verifyMath()` in browser console — 7/7 checks pass
  (includes triadic rigidity)
- **Chrome automation:** `python scripts/test-demo.py --url <live-url>`
- **Last test run:** 2026-08-06 — 7/7 math verification passed, zero console errors
- **Features:** seeded RNG (mulberry32), guided first-run tour, click-to-select
  leaves, formula display, math verification

---

*Generated with DeepChat | All page content is AI-generated and for reference only.*
