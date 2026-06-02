# Finite Element Analysis Notes

Canonical markdown for **Part IV — The Finite Element Method**, aligned with [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf).

## Layout (Functional Analysis Notes style)

```
fem/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-weighted-residuals.md
│   ├── 02-galerkin-assembly.md
│   ├── 03-elements-quadrature.md
│   ├── 04-poisson-to-elasticity.md
│   └── 05-convergence.md
```

Chapter numbering `01`–`05` matches `src/part04-fem/`.

## Build standalone

```bash
cd writings/fem && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
