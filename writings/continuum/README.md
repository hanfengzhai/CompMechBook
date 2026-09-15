# Continuum Mechanics Notes

Canonical markdown for **Part VI — Continuum Mechanics**, aligned with [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf).

## Layout (Functional Analysis Notes style)

```
continuum/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-kinematics.md
│   ├── 02-stress-balance.md
│   ├── 03-variational-elasticity.md
│   └── 04-nonlinear-plasticity-preview.md
```

Chapter numbering `01`–`04` matches `src/part06-continuum/` in CompMechBook. Bridge sections connect FEM discretization to the virtual work principle; Chapter 03 hands off to nonlinear plasticity; Chapter 04 hands off to Part VII (defects and dislocations).

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
