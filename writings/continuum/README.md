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
│   └── 03-variational-elasticity.md
```

Chapter numbering `01`–`03` matches `src/part06-continuum/`.

## Build standalone

```bash
cd writings/continuum && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
