# Molecular Dynamics Notes

Canonical markdown for **Part VIII — Atomistic Simulation**, aligned with [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) and [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf).

## Layout (Functional Analysis Notes style)

```
md/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-potentials-phase-space.md
│   ├── 02-ensembles-integrators.md
│   └── 03-ab-initio-and-coarse-graining.md
```

Chapter numbering `00`–`03` matches `src/part08-md/` in CompMechBook. Bridge sections connect dislocation-scale physics to interatomic potentials and LAMMPS workflows; Chapter 03 hands off to Part IX (density functional theory).

## MD & atomistics reading map (template for Part VIII)

| Chapter | AtomModel / StatMech object | Wire beat | Hands off to |
|---------|----------------------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure; descent rung 2 | VII.3 exported mobility; cores need nuclei at \(T_w\) from CHT | 01 |
| 01 Potentials & phase space | EAM, cutoffs, periodic RVE; Newton on BO surface | EAM minimization sets \(a_0\); Burgers vector links to VII | 02 |
| 02 Ensembles & integrators | NVT/NPT, Verlet, stress from MD | NVT shear at \(T_w\); NPT moduli before export | 03 |
| 03 Coarse-graining & workflows | LAMMPS fit, WHAM, yaml handoff tables | `mobility_cu_screw_{T_w}K.yaml`; pedigree gate before DFT | [Part IX](../dft/chapters/00-opening.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part VIII sits in the descent after Part VII.

## Build standalone

```bash
cd writings/md && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
