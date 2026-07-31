# Finite Volume Method Notes

Canonical markdown for **Part V — Conservation on Cells**, aligned with [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) and [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf).

## Layout (Functional Analysis Notes style)

```
fvm/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-conservation-integral.md
│   ├── 02-fvm-1d.md
│   ├── 03-fluxes-riemann.md
│   └── 04-navier-stokes-cfd.md
```

Chapter numbering `00`–`04` matches `src/part05-fvm/` in CompMechBook. Topics include conservation form, cell averages, eigenstructure, shock-tube verification, and Navier–Stokes CFD. Bridge sections connect Part IV (FEM for elliptic solids) to integral flux balance on the copper wire's cooling flow.

## Build standalone

```bash
cd writings/fvm && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
