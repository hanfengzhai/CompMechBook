# Finite Volume Method Notes

Canonical markdown for **Part V — Conservation on Cells**, aligned with [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) and [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf).

## Layout (Functional Analysis Notes style)

```
fvm/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-conservation-integral.md
│   ├── 02-fvm-1d.md
│   ├── 03-fluxes-riemann.md
│   └── 04-navier-stokes-cfd.md
```

Chapter numbering `01`–`04` matches `src/part05-fvm/`.

## Build standalone

```bash
cd writings/fvm && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
