# Density Functional Theory Notes

Canonical markdown for **Part IX — Electronic Structure**, aligned with [MSE5720 coursework](https://github.com/hanfengzhai/MSE5720-HW).

## Layout (Functional Analysis Notes style)

```
dft/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-born-oppenheimer.md
│   └── 02-kohn-sham.md
```

Chapter numbering `01`–`02` matches `src/part09-dft/`.

## Build standalone

```bash
cd writings/dft && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
