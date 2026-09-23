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

## FVM / CFD reading map (template for Part V)

| Chapter | FVM / CFD Notes object | Wire beat | Hands off to |
|---------|------------------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure | Door A from FEM; air outside the wire needs flux balance | 01 |
| 01 Conservation integral | Divergence theorem on control volumes; discrete balance | Natural convection off the hot surface; no weak form yet | 02 |
| 02 FVM 1D | Cell averages, upwind flux, CFL, ghost cells | Boundary-layer slice normal to wire; flux handshake with solid | 03 |
| 03 Fluxes / Riemann | Exact and approximate Riemann solvers; TVD limiters | Shock tube beside the lab; steep gradients at hot wall | 04 |
| 04 Navier–Stokes CFD | SIMPLE/PISO, staggered grids, conjugate heat transfer | \(T_w\) and Robin \(h\) → resolved convection; export for CHT | [Part VI](../continuum/chapters/00-opening.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part V sits between FEM solids and continuum stress language.

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
