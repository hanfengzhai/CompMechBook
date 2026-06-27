# Part VII — Defects and Dislocations

Parts I–VI described the copper wire as a smooth continuum: displacement fields, stress tensors, finite elements and finite volumes that approximate elliptic and hyperbolic PDEs. That picture is correct at the engineering scale and wrong at the mesoscale, where the wire is a polycrystal full of vacancies, grain boundaries, and dislocation lines that carry plasticity.

This part steps down one rung on the ladder. We classify defects, then follow dislocation dynamics — Peach–Köhler forces, mobility laws, and the forest hardening that makes cold-drawn copper stronger than annealed copper. The continuum moduli and yield surfaces used in Part VI are not fundamental constants; they are **homogenized summaries** of motion at this scale. Parts VIII and IX descend further, to atoms and electrons, to explain where even dislocation theory must borrow its parameters.

## The concept map

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Dislocation lines, Burgers vector \(\mathbf{b}\), dislocation density \(\rho\) |
| What **structure** does it add? | Peach–Köhler forces, mobility laws, link statistics |
| What **theorem** becomes possible? | Taylor hardening, DDD time integration, homogenization to crystal plasticity |
| What **breaks** if structure is missing? | Core singularity, wrong hardening law, non-physical yield without forest structure |

```mermaid
flowchart LR
  T[Defect taxonomy] --> DDD[Dislocation dynamics]
  DDD --> TH[Taylor hardening]
  TH --> CP[Crystal plasticity FEM]
  CP --> OD[OpenDiS to DAMASK handoff]
```

**Baby picture:** name the line defects that carry plasticity, simulate their motion with elastic superposition and mobility tables, extract hardening laws and link statistics, then export internal variables to polycrystal FEM. The drawn copper wire is stronger because of this forest, not because \(\mathbf{K}\) changed.

## Bridge

Part VI closed with variational elasticity: energy minimization and virtual work for smooth fields. The drawn copper wire violates that smoothness at the mesoscale — dislocation lines, grain boundaries, and vacancy clusters are the mechanisms behind yield and work hardening. The next chapter names those structures; the one after simulates their motion.
