# Molecular Dynamics Notes

Canonical markdown for **Part VIII — Atomistic Simulation**, aligned with [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) and [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf).

## Layout (Functional Analysis Notes style)

```
md/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-potentials-phase-space.md
│   └── 02-ensembles-integrators.md
```

Chapter numbering `01`–`02` matches `src/part08-md/` in CompMechBook. Bridge sections connect dislocation-scale physics to interatomic potentials and LAMMPS workflows; Chapter 02 hands off to Part IX (density functional theory).

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
