# Defects & Dislocations Notes

Canonical markdown for **Part VII — Defects and Dislocations**, aligned with [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) and [OpenDiS](https://github.com/OpenDiS/OpenDiS).

## Layout (Functional Analysis Notes style)

```
defects/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-defect-taxonomy.md
│   ├── 02-dislocation-dynamics.md
│   └── 03-polycrystal-and-fem-handoff.md
```

Chapter numbering `00`–`03` matches `src/part07-defects/` in CompMechBook. Bridge sections connect continuum elasticity to mesoscale plasticity; Chapter 03 hands off to Part VIII (molecular dynamics).

## Build standalone

```bash
cd writings/defects && mdbook build
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
| Part VII feels like taxonomy slides separate from OpenDiS | [Bridge reunion — Part VII (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-vii) |
| DDD and polycrystal FEM handoff feel disconnected | [VII.3 → Handshake 4a reunion](../appendix/chapters/sources.md#vii3-handshake4a-reunion-index-row-41) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part descent VI–IX](../appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
| DDD \(\tau(\gamma)\) imported at lab rate without extrapolation | [Scale-boundary reunion (row 28)](../appendix/chapters/sources.md#scale-boundary-reunion-index-row-28) · [VII.3 rate handshake](chapters/03-polycrystal-and-fem-handoff.md#scale-boundary-handshake-ddd-strain-rate-to-quasi-static-fem) |
