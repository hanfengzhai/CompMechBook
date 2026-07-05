# Part VII — Defects and Dislocations

Parts I–VI described the copper wire as a smooth continuum: displacement fields, stress tensors, finite elements and finite volumes that approximate elliptic and hyperbolic PDEs. That picture is correct at the engineering scale and wrong at the mesoscale, where the wire is a polycrystal full of vacancies, grain boundaries, and dislocation lines that carry plasticity.

This part steps down one rung on the ladder. We classify defects, then follow dislocation dynamics — Peach–Köhler forces, mobility laws, and the forest hardening that makes cold-drawn copper stronger than annealed copper. The continuum moduli and yield surfaces used in Part VI are not fundamental constants; they are **homogenized summaries** of motion at this scale. Parts VIII and IX descend further, to atoms and electrons, to explain where even dislocation theory must borrow its parameters.

Three chapters cover defect taxonomy, dislocation dynamics, and the handoff to crystal plasticity and FEM. The layout follows the **Defects Notes** in [`writings/defects/`](../../writings/defects/): numbered chapters with **Bridge** sections, worked examples tied to the copper wire, and explicit upward links to Part VI (continuum) and downward requests to Part VIII (MD).

## Where we left the wire

Part VI closed with nonlinear elasticity and the admission that cold-drawn copper work-hardens — its yield surface rises, its texture evolves, and notch roots concentrate stress until smooth fields lie. None of that history lives in the elastic modulus \(\mathbb{C}\) alone; it lives in **defects**: dislocation lines tangled by drawing, grain boundaries from polycrystal structure, vacancies left by processing.

At the engineering scale the wire still satisfies balance laws and virtual work; at the mesoscale it is a forest of line defects whose collective motion we can simulate rather than postulate. Part VII is the first rung where the copper wire stops pretending to be a smooth continuum everywhere.

Recall the prologue's processing history: **drawing** through dies increases dislocation density and aligns grains; **annealing** lets vacancies diffuse and lines rearrange. Part VI's nonlinear plasticity preview fit phenomenological hardening parameters \(H\) and \(\sigma_{y0}\) without naming the forest that produces them. Part VII names the forest — and shows how dislocation dynamics turns cold-work history into exportable internal variables for crystal plasticity FEM.

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

## Story so far (Parts I–VI)

The climb upward is complete for the **continuum floor**. Every rung below Part VII exported numbers upward; Part VII is the first descent that explains where those numbers hid their history:

| Part | Scale | Wire story beat |
|------|-------|-----------------|
| I–III | Mathematics | Springs → fields → weak PDEs |
| IV–V | Discretization | FEM solid mesh; FVM cooling air (optional) |
| VI | Continuum physics | \(\mathbf{F}\), \(\boldsymbol{\sigma}\), virtual work; J₂ plasticity **preview** with fitted \(H\), \(\sigma_y\) |

Part VI admitted that cold-drawn copper work-hardens and that notch roots break smooth-field assumptions — but it could not **simulate** the dislocation forest that drawing created. Phenomenological plasticity fits curves; dislocation dynamics **generates** the curves from line motion. The prologue's processing history (draw, anneal, load) now gets a mesoscale narrator: Burgers vectors, Peach–Köhler forces, Taylor \(\sqrt{\rho}\) hardening. Parts VIII–IX will ask where mobility and stacking-fault energy come from; Part VII asks how plasticity **moves** before we shrink to atoms and electrons.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** from the opening table reappear here with defect vocabulary — and how the **same mathematical moves** from Part I return at the mesoscale:

| Part I (springs on the wire) | Part VII (dislocations in the wire) |
|------------------------------|-------------------------------------|
| State vector \(\mathbf{u}\) | Dislocation segment positions and link topology |
| Stiffness matrix \(\mathbf{K}\) | Elastic influence matrix between line segments |
| Eigenmodes decouple vibration | Normal modes of the elastic medium superpose on line motion |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) from energy minimization | Peach–Köhler force balance on each segment |
| Fitted parameters in a phenomenological law | **Generated** hardening from forest density \(\rho\) |

Part VI's J₂ plasticity preview fit \(H\) and \(\sigma_y\) without naming the forest; Part VII is where cold-drawn strength stops being a magic constant and becomes **motion of line defects** we can time-integrate. The copper wire that began as a spring network still ends in sparse linear algebra whenever DDD solves elastic superposition — but the state is no longer nodal displacement alone. Parts VIII–IX will ask where mobility tables and stacking-fault energy originate; Part VII exports the hardening history FEM needs.

## Bridge

Part VI closed with variational elasticity: energy minimization and virtual work for smooth fields. The drawn copper wire violates that smoothness at the mesoscale — dislocation lines, grain boundaries, and vacancy clusters are the mechanisms behind yield and work hardening. The next chapter names those structures; the one after simulates their motion.
