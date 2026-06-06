# Density Functional Theory Notes

Canonical markdown for **Part IX — Electronic Structure**, aligned with [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) coursework and Martin, *Electronic Structure*.

## Layout (Functional Analysis Notes style)

```
dft/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-born-oppenheimer.md
│   └── 02-kohn-sham.md
```

Chapter numbering `01`–`02` matches `src/part09-dft/` in CompMechBook. Bridge sections connect atomistic potentials to Born–Oppenheimer separation and the Kohn–Sham equations; Chapter 02 hands off to the epilogue on multiscale coupling.

## Build standalone

```bash
cd writings/dft && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
