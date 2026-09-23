# Molecular Dynamics Notes

Canonical markdown for **Part VIII — Atomistic Simulation**, aligned with [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) and [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf).

## Layout (Functional Analysis Notes style)

```
md/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-potentials-phase-space.md
│   ├── 02-ensembles-integrators.md
│   └── 03-ab-initio-and-coarse-graining.md
```

Chapter numbering `00`–`03` matches `src/part08-md/` in CompMechBook. Bridge sections connect dislocation-scale physics to interatomic potentials and LAMMPS workflows; Chapter 03 hands off to Part IX (density functional theory).

## Build standalone

```bash
cd writings/md && mdbook build
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
| Part VIII feels like a LAMMPS manual separate from DFT audit | [Bridge reunion — Part VIII (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-viii) |
| 0 K EAM vs NVT at \(T_w\) still feel like separate subjects | [Potentials → ensembles reunion](../appendix/chapters/sources.md#potentials-ensembles-reunion-index-row-34) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part descent VI–IX](../appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
