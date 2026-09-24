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
| CHT export clear but Part VI virtual work feels separate from Part IV \(\mathbf{K}\) | [Twin-ladder → virtual work reunion (row 31)](../appendix/chapters/sources.md#twin-ladder-virtual-work-reunion-index-row-31) · [V.4 Bridge → Part VI](../chapters/04-navier-stokes-cfd.md#bridge-to-part-vi) |
| Virtual work clear but return-mapping at yield feels separate from \(\delta\Pi = 0\) | [Virtual work → plasticity preview reunion (row 32)](../appendix/chapters/sources.md#virtual-work-plasticity-preview-reunion-index-row-32) · [VI.3 opening hinge → VI.4](../../src/part06-continuum/03-variational-elasticity.md#opening-hinge-vi3-to-vi4) |
| Part IV heat/mechanics never shared one mesh before Picard | [Thermoelastic assembly reunion (row 29)](../appendix/chapters/sources.md#thermoelastic-assembly-reunion-index-row-29) · [IV.5 thermoelastic \(h\)-study](../../src/part04-fem/05-convergence.md#lab-act-extension-thermoelastic-h-refinement-on-one-mesh-acts-iiiii) |
| Picard converged but descent still uses 300 K default | [Scale-boundary reunion (row 28)](../appendix/chapters/sources.md#scale-boundary-reunion-index-row-28) · [V.4 CHT Bridge](../chapters/04-navier-stokes-cfd.md#bridge-to-part-vi) |

Upstream: [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) · [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf). Book part: [Part V in `src/part05-fvm/`](../../src/part05-fvm/).
