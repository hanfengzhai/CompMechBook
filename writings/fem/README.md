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

## FEA reading map (template for Part IV)

| Chapter | FEA Notes object | Wire beat | Hands off to |
|---------|------------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure | Mesh the wire; Acts II–III share one connectivity | 01 |
| 01 Weighted residuals | Trial/test spaces, residual orthogonality | Heat and elasticity residuals in the same Galerkin choice | 02 |
| 02 Galerkin assembly | Local scatter into \(\mathbf{K}\); block preview | Element loops build \(\mathbf{K}_{TT}\) and \(\mathbf{K}_{uu}\) | 03 |
| 03 Elements / quadrature | Isoparametric maps, Gauss rules, patch test | P1 bars on the wire; shared quadrature for \(T\) and \(\mathbf{u}\) | 04 |
| 04 Poisson → elasticity | \(\mathbf{B}^T\mathbb{C}\mathbf{B}\); thermoelastic blocks | Staggered or monolithic pass with \(\varepsilon_{\text{th}}\) loading | 05 |
| 05 Convergence | Céa's lemma, \(h\)-rates, a posteriori estimators | Halve \(h\) at the grip corner; export \(T_w\) for CHT | [Part V](../fvm/chapters/00-opening.md) (Door A) · [Part VI](../continuum/chapters/00-opening.md) (Door B) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part IV sits between weak PDEs and fluids/continuum forks.

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
