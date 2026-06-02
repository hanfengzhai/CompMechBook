# Defects and Dislocations Notes

Canonical markdown for **Part VII — Defects and Dislocations**, aligned with [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf).

## Layout (Functional Analysis Notes style)

```
defects/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-defect-taxonomy.md
│   └── 02-dislocation-dynamics.md
```

Chapter numbering `01`–`02` matches `src/part07-defects/`.

## Build standalone

```bash
cd writings/defects && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
