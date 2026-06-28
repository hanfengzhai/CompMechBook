# Finite Element Method Notes

Canonical markdown for **Part IV — The Finite Element Method**, aligned with [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html).

## Layout (Functional Analysis Notes style)

```
fem/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-weighted-residuals.md
│   ├── 02-galerkin-assembly.md
│   ├── 03-elements-quadrature.md
│   ├── 04-poisson-to-elasticity.md
│   └── 05-convergence.md
```

Chapter numbering `00`–`05` matches `src/part04-fem/` in CompMechBook. Bridge sections connect weighted residuals to Galerkin assembly, elements, elasticity, and convergence; Chapter 05 hands off to Part V (finite volumes and conservation laws).

## Build standalone

```bash
cd writings/fem && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
