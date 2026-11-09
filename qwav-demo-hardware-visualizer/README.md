# Hardware Pathway Visualizer — 40-Atom Neutral Atom Tree Lattice (Artifact A5)

**Status:** ✅ LIVE — deployed 2026-08-04 | **Enhanced:** 2026-08-06
**URL:** https://qnfo.github.io/qwav-demo-hardware-visualizer/

## What This Shows

An interactive 3D model of a neutral-atom quantum computing architecture: 40
atoms arranged in a Bruhat-Tits-inspired tree lattice (p=3, depth=3:
1 + 3 + 9 + 27 = 40). Each atom is a qubit site; gold lines show Rydberg
blockade gates between parent–child pairs — the physical mechanism for
two-qubit operations in neutral-atom arrays. Drag to rotate, scroll to zoom,
toggle the gates, and explore the "40 atoms at 4K" hardware specification from
the Symmetric Extension paper.

## The Math

```
Tree lattice:  N(depth) = p^depth
Total atoms:   Σ_{k=0}^{d} p^k  =  1 + 3 + 9 + 27  =  40   (p=3, d=3)

Rydberg blockade:  two atoms within blockade radius R_b cannot be
excited simultaneously → effective CZ gate between them
```

| Symbol | Meaning |
|:-------|:--------|
| p | Branching factor (3 for this lattice) |
| d | Tree depth (3 levels below the root) |
| N(k) | Number of atoms at depth k |
| R_b | Rydberg blockade radius (gate connectivity) |

## How to Use

1. **Start here:** Let the lattice auto-rotate, then **drag anywhere** to take
   control. Scroll to zoom. The redder atoms sit deeper in the tree (leaf
   qubits); the gold root is the apex.

2. **Toggle gates:** Switch **Gates ON/OFF** to hide or show the Rydberg
   blockade edges. Each gold line is a physical two-qubit gate between a parent
   and its child in the tree.

3. **View from the top:** Click **📷 Top View** to see the lattice from above —
   the cleanest view of the three-fold symmetry (each node has 3 children).

4. **Verify:** Click **✓ Verify** to run 7 mathematical checks: atom count (40),
   per-depth counts (1/3/9/27), gate edges present, and coordinate validity.

## Parameters

| Parameter | Symbol | Range | Default | Description |
|:----------|:-------|:------|:--------|:------------|
| Gates | — | ON / OFF | ON | Toggle Rydberg blockade edge rendering |
| Rotation | — | Auto / Manual | Auto | Auto-rotate or drag-to-control |
| View | — | — | default | 📷 Top View button resets rotation |

## Interpreting the Output

- **Atom size ∝ depth from root:** root is largest, leaf atoms smallest.
- **Color:** warmer red = deeper in the tree (leaf qubits).
- **Gold lines:** Rydberg blockade gates (39 edges for 40 atoms in a tree).
- **Depth readouts:** confirm the 1/3/9/27 layer structure.

## Reproducibility

- The lattice geometry is deterministic (fixed branching, fixed angles);
  no randomness is involved in atom placement
- **Math verification:** `verifyMath()` in browser console runs 7 checks

## Limitations

- The 3D layout is an artistic embedding of the abstract tree; it is not a
  physically realizable atom-trap geometry (real neutral-atom arrays are
  typically 2D grids with dynamic rearrangement)
- Gates are drawn for the full parent–child connectivity; actual Rydberg
  blockade gating would be time-scheduled, not simultaneous
- This visualizes the hardware topology; it does not simulate gate operations,
  decoherence, or error correction on the 40 qubits

## Source

- **Strategy:** QNFO/QWAV strategy/3.0.md — Tier 1 Artifact A5
- **Publication:** Symmetric Extension §Hardware Specification
- **Build:** single-file HTML, canvas rendering, zero external dependencies
- **Repository:** https://github.com/QNFO/qwav-demo-hardware-visualizer
- **Skill:** qwav-demo-kit v1.0 (design, build, test, deploy, document pipeline)

## Testing

- **Math verification:** `verifyMath()` in browser console — 7/7 checks pass
- **Chrome automation:** `python scripts/test-demo.py --url <live-url>`
- **Last test run:** 2026-08-06 — 7/7 math verification passed (incl. 40-atom
  structure check that caught and fixed a tree-building bug), zero console errors
- **Features:** guided first-run tour, drag-to-rotate 3D, scroll zoom,
  requestAnimationFrame animation loop, gate toggle, math verification

---

*Generated with DeepChat | All page content is AI-generated and for reference only.*
