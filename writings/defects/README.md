# Defects & Dislocations Notes

Canonical markdown for **Part VII — Defects and Dislocations**, aligned with [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) and [OpenDiS](https://github.com/OpenDiS/OpenDiS).

## Layout (Functional Analysis Notes style)

```
defects/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-defect-taxonomy.md
│   └── 02-dislocation-dynamics.md
```

Chapter numbering `01`–`02` matches `src/part07-defects/` in CompMechBook. Bridge sections connect continuum elasticity to mesoscale plasticity; Chapter 02 hands off to Part VIII (molecular dynamics).

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
