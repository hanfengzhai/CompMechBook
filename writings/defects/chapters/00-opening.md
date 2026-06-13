# Part VII — Defects and Dislocations

Parts I–VI described the copper wire as a smooth continuum: displacement fields, stress tensors, finite elements and finite volumes that approximate elliptic and hyperbolic PDEs. That picture is correct at the engineering scale and incomplete at the mesoscale, where the wire is a polycrystal full of vacancies, grain boundaries, and dislocation lines that carry plasticity.

Return to the cold-drawn copper wire from the prologue. A tensile test reports a smooth stress–strain curve; Part VI's J₂ plasticity can fit that curve with a yield stress and hardening modulus. Those numbers are not fundamental. They summarize **collective motion** of line defects frozen into the material by drawing dies and partial annealing. Zoom to a transmission electron micrograph and the smooth curve dissolves into tangled dislocation forests, pile-ups at grain boundaries, and occasional voids — structures that continuum fields cannot resolve without regularization, yet whose statistics control every macroscopic property we care about.

This part steps down one rung on the ladder. We classify defects, then follow **dislocation dynamics (DDD)** — Peach–Köhler forces, mobility laws, junction formation, and the forest hardening that makes cold-drawn copper stronger than annealed copper. The continuum moduli and yield surfaces used in Part VI are **homogenized summaries** of motion at this scale. Parts VIII and IX descend further, to atoms and electrons, to explain where even dislocation theory must borrow its parameters.

## What this part covers

| Chapter | Focus | Copper wire connection |
|---------|-------|------------------------|
| 01 — Defect taxonomy | Point, line, surface defects; Burgers vector | Why drawing increases strength; grain boundaries in polycrystal wire |
| 02 — Dislocation dynamics | Peach–Köhler, mobility, Taylor hardening | Work-hardening curve from evolving dislocation density |
| 03 — Polycrystal handoff | Crystal plasticity, FEM export | From DDD statistics to constitutive laws in structural models |

The layout follows the **Defects Notes** in [`writings/defects/`](../../writings/defects/): numbered chapters, mechanics examples tied to the wire, and **Bridge** sections at each handoff — the same pattern as the [Functional Analysis Notes](../functional-analysis/).

## The mesoscale question

At every scale we ask four questions (prologue, Part I). At the mesoscale the answers are:

- **State**: dislocation network (segment positions, Burgers vectors, connectivity).
- **Equations**: elastic field + Peach–Köhler driving forces + mobility laws + topological rules.
- **Discretization**: line segments, fast multipole or influence matrices, adaptive remeshing at junctions.
- **Upward export**: hardening laws \(\tau(\gamma)\), dislocation density \(\rho\), link statistics, back stress.

When Part IV's FEM mesh is fine enough but the stress–strain curve is still wrong, the signal is not "refine more" — it is "descend to Part VII."

## Bridge

Part VI closed with variational elasticity: energy minimization and virtual work for smooth fields. The drawn copper wire violates that smoothness at the mesoscale — dislocation lines, grain boundaries, and vacancy clusters are the mechanisms behind yield and work hardening. The next chapter names those structures; the one after simulates their motion.
