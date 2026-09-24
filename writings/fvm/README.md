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

## Reading map (continuous book)

| When the plot stutters | Open |
|------------------------|------|
| Part V feels like 1D FVM homework separate from CFD | [Bridge reunion — Part V (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-v) |
| Solid FEM vs fluid FVM | [CHT outer-loop reunion (row 30)](../appendix/chapters/sources.md#cht-outer-loop-reunion-index-row-30) |
| Part V feels like a separate CFD course after Part IV | [IV.5 → V.0 FEM–FVM reunion (row 49)](../appendix/chapters/sources.md#rows17-48-iv5-v0-fem-fvm-reunion-index-row-49) |
| Part VI feels like elasticity after Navier–Stokes | [V.4 → VI.0 FVM–continuum reunion (row 50)](../appendix/chapters/sources.md#rows17-49-v4-vi0-fvm-continuum-reunion-index-row-50) · [V.4 Writings canonical hinge](chapters/04-navier-stokes-cfd.md#writings-canonical-hinge-v4-to-vi0) |

Upstream: [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) · [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf). Book part: [Part V in `src/part05-fvm/`](../../src/part05-fvm/).
