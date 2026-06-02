# Molecular Dynamics Notes

Canonical markdown for **Part VIII — Atomistic Simulation**, aligned with [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf).

## Layout (Functional Analysis Notes style)

```
md/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-potentials-phase-space.md
│   └── 02-ensembles-integrators.md
```

Chapter numbering `01`–`02` matches `src/part08-md/`.

## Build standalone

```bash
cd writings/md && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
