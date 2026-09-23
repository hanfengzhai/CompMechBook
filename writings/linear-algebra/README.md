# Linear Algebra Notes

Canonical markdown for **Part I — The Grammar of Computation**, aligned with [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf).

## Layout (Functional Analysis Notes style)

```
linear-algebra/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-vectors-matrices.md
│   ├── 02-linear-maps.md
│   ├── 03-eigenvalues.md
│   └── 04-toward-infinity.md
```

Chapter numbering `00`–`04` matches `src/part01-linear-algebra/` in CompMechBook. Each chapter ends with a **Bridge** section that connects the narrative to the next topic; Chapter 04 introduces function spaces and motivates Part II.

## ME 300A reading map (template for Part I)

| Chapter | ME 300A object | Wire beat | Hands off to |
|---------|----------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure | Mount wire; name nodal DOFs and the load cell | 01 |
| 01 Vectors & matrices | \(\mathbb{R}^n\), norms, conditioning | Spring network; first \(\mathbf{K}\mathbf{u}=\mathbf{f}\) assembly | 02 |
| 02 Linear maps | Range, null space, rank | Stiffness as a map from displacements to forces | 03 |
| 03 Eigenvalues | Modes, spectra, Rayleigh quotients | Vibration modes foreshadow continuum and FEM | 04 |
| 04 Toward infinity | From \(\mathbb{R}^n\) to function spaces | Mesh refines; dot products need a limit | [Part II](../functional-analysis/chapters/00-opening.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part I sits in the ascent.

## Build standalone

```bash
cd writings/linear-algebra && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
