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

The copper wire began as a chain of coupled springs in Part I. At the mesoscale it is a **forest of line defects** whose collective motion reproduces the same load-cell curve that phenomenological plasticity fit in Part VI:

| Part I (springs on the wire) | Part VII (dislocations on the wire) |
|------------------------------|-------------------------------------|
| State vector \(\mathbf{u}\) | Dislocation network (positions, \(\mathbf{b}\), \(\rho\)) |
| Stiffness matrix \(\mathbf{K}\) | Elastic superposition + Peach–Köhler driving forces |
| Eigenmodes decouple vibration | Slip systems decouple on {111}\(\langle 110 \rangle\) families |
| Mesh refinement sends \(N\to\infty\) | DDD link statistics → crystal plasticity internal variables |
| Energy \(\mathbf{u}^T \mathbf{K}\mathbf{u}\) | Line energy + forest hardening \(\Delta\tau \propto \sqrt{\rho}\) |

Part II taught that infinite-dimensional limits live in function spaces; Part VI named the stress tensors those limits carry. Part VII is the first descent that **generates** constitutive history rather than fitting parameters to a curve. When the load cell slope rises after cold drawing, the mechanism is not a larger \(\mathbf{K}\) — it is dislocation density stored by manufacturing and multiplied under load.

## Bridge

Part VI closed with the load cell curve bending upward — yield and work hardening that no elastic modulus alone explains. Look at the wire under the microscope: slip lines appear on the surface; inside the grains, dislocation lines tangle and multiply. That is the scene Part VII opens on. The next chapter names the defect structures (vacancies, grain boundaries, dislocations); the one after simulates their motion with Peach–Köhler forces and mobility laws; the last exports hardening laws to crystal plasticity FEM on the same mesh Part IV taught us to assemble.
