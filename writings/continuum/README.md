# Continuum Mechanics Notes

Canonical markdown for **Part VI — Continuum Mechanics**, aligned with [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf).

## Layout (Functional Analysis Notes style)

```
continuum/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-kinematics.md
│   ├── 02-stress-balance.md
│   ├── 03-variational-elasticity.md
│   └── 04-nonlinear-plasticity-preview.md
```

Chapter numbering `00`–`04` matches `src/part06-continuum/` in CompMechBook. Bridge sections connect FEM discretization to the virtual work principle; Chapter 03 hands off to nonlinear plasticity; Chapter 04 hands off to Part VII (defects and dislocations).

## Continuum mechanics reading map (template for Part VI)

| Chapter | Elasticity Notes object | Wire beat | Hands off to |
|---------|-------------------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure; midpoint (ascent complete) | FEM + FVM reunite on Cauchy stress; Joule heat + grip strain | 01 |
| 01 Kinematics | \(\mathbf{F}\), strain measures, objectivity | Grip displacement ramps; lateral contraction vs \(\nu\) | 02 |
| 02 Stress & balance | Cauchy stress, momentum/energy balance, constitutive closure | Load cell force; thermocouple + Joule heating coupled to \(\boldsymbol{\sigma}\) | 03 |
| 03 Variational elasticity | Virtual work, hyperelastic energy, FEM reunion | \(\delta\Pi=0\) explains \(\mathbf{K}\mathbf{U}=\mathbf{F}\); thermal strain from CHT | 04 |
| 04 Nonlinear / plasticity preview | \(J_2\), hardening, return mapping; ascent ends | Load cell knee; fitted \(H\) as placeholder for a forest | [Part VII](../defects/chapters/00-opening.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part VI closes the ascent before descent to defects and atoms.

## Build standalone

```bash
cd writings/continuum && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
