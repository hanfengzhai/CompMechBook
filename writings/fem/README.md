# Finite Element Method Notes

Canonical markdown for **Part IV — The Finite Element Method**, aligned with [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html).

## Layout (Functional Analysis Notes style)

```
fem/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-weighted-residuals.md
│   ├── 02-galerkin-assembly.md
│   ├── 03-elements-quadrature.md
│   ├── 04-poisson-to-elasticity.md
│   └── 05-convergence.md
```

Chapter numbering `00`–`05` matches `src/part04-fem/` in CompMechBook. Bridge sections connect weighted residuals to Galerkin assembly, elements, elasticity, and convergence. Chapter 05 offers **two doors**: Door A continues to Part V (finite volumes and conservation laws); Door B skips ahead to Part VI (continuum mechanics and stress–balance language). Both paths reconverge before Part VII.

## Build standalone

```bash
cd writings/fem && mdbook build
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
| Part IV feels like five unrelated FEA assignments | [Bridge reunion — Part IV (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-iv) |
| Act II + III on one mesh | [Thermoelastic assembly reunion (row 29)](../appendix/chapters/sources.md#thermoelastic-assembly-reunion-index-row-29) |
| Door A vs Door B after IV.5 | [IV.5 two doors](../chapters/05-convergence.md#bridge-two-doors-from-here) |

Upstream: [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf). Book part: [Part IV in `src/part04-fem/`](../../src/part04-fem/).
