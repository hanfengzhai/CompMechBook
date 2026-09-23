# Partial Differential Equations Notes

Canonical markdown for **Part III — Fields on Domains**, aligned with [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf).

## Layout (Functional Analysis Notes style)

```
pde/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-strong-form.md
│   ├── 02-weak-form.md
│   ├── 03-sobolev-spaces.md
│   └── 04-energy-methods.md
```

Chapter numbering `00`–`04` matches `src/part03-pdes/` in CompMechBook. Bridge sections connect Part II function spaces to Part IV discretization; Chapter 04 hands off to the finite element method.

## ME 300B reading map (template for Part III)

| Chapter | ME 300B object | Wire beat | Hands off to |
|---------|----------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure | Domain + BCs; thermoelastic stack on one bar | 01 |
| 01 Strong form | Pointwise PDEs, classification, where \(C^2\) fails | Heat + elasticity + coupled \(\sigma(T)\) at three lab points | 02 |
| 02 Weak form | Test functions, bilinear forms, natural BCs | Grip corner; integration by parts on the heated wire | 03 |
| 03 Sobolev spaces | \(H^1\), traces, Poincaré, conforming FE preview | \(H^1\) displacement, \(L^2\) temperature on the mesh | 04 |
| 04 Energy methods | Dirichlet principle, Lax–Milgram, Rayleigh–Ritz | Minimize thermal then elastic energy before assembly | [Part IV](../fem/chapters/00-opening.md) (FEM) · [Part V](../fvm/chapters/00-opening.md) (fluids fork) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part III sits between function spaces and discretization.

## Build standalone

```bash
cd writings/pde && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
