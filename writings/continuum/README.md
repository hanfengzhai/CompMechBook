# Continuum Mechanics Notes

Canonical markdown for **Part VI — Continuum Mechanics**, aligned with [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf).

## Layout (Functional Analysis Notes style)

```
continuum/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-kinematics.md
│   ├── 02-stress-balance.md
│   ├── 03-variational-elasticity.md
│   └── 04-nonlinear-plasticity-preview.md
```

Chapter numbering `00`–`04` matches `src/part06-continuum/` in CompMechBook. Bridge sections connect FEM discretization to the virtual work principle; Chapter 03 hands off to nonlinear plasticity; Chapter 04 hands off to Part VII (defects and dislocations).

## Build standalone

```bash
cd writings/continuum && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.

## Reading map (continuous book)

| When the plot stutters | Open |
|------------------------|------|
| Part VI feels like kinematics homework separate from virtual work | [Bridge reunion — Part VI (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-vi) |
| Twin ladders and \(\mathbf{K}\) still feel disconnected | [Twin-ladder → virtual work reunion](../appendix/chapters/sources.md#twin-ladder-virtual-work-reunion-index-row-31) |
| Virtual work clear but return-mapping at the knee feels arbitrary | [Virtual work → plasticity preview reunion (row 32)](../appendix/chapters/sources.md#virtual-work-plasticity-preview-reunion-index-row-32) · [VI.3 opening hinge → VI.4](chapters/03-variational-elasticity.md#opening-hinge-vi3-to-vi4) · [VI.4 intermission](chapters/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) |
| Part VII forest clear but OpenDiS mobility lacks MD pedigree at \(T_w\) | [Part VII → VIII descent hinge reunion (row 33)](../appendix/chapters/sources.md#part-vii-viii-descent-hinge-reunion-index-row-33) · [Part VII descent hinge](../../src/part07-defects/00-opening.md#descent-hinge-from-vi4-energy-break-forest-begins) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part descent VI–IX](../appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
| Handbook \(\alpha\) or DFT moduli in FEM cards feel arbitrary | [Scale-boundary reunion (row 28)](../appendix/chapters/sources.md#scale-boundary-reunion-index-row-28) · [VI.2 \(\alpha\) handshake](chapters/02-stress-balance.md#scale-boundary-handshake-thermal-expansion-alpha) · [VI.2 \(\mathbb{C}\) handshake](chapters/02-stress-balance.md#scale-boundary-handshake-dft-elastic-tensor-to-fem-material-card) |
