# Part VIII — Atomistic Simulation

Parts I–VII treated the copper wire as a continuum or a network of line defects. Part VIII descends to the scale where matter resolves into **individual atoms** — nuclei moving on a potential energy surface, thermal vibrations exchanging energy with a heat bath, bonds stretching and breaking at crack tips where no elliptic PDE can remain valid without regularization.

Molecular dynamics is the workhorse of atomistic materials mechanics. It supplies the interatomic potentials that empirical models require, the mobility laws that dislocation dynamics calibrates, and the fracture trajectories that explain how notches become cracks. Classical MD assumes nuclei follow Born–Oppenheimer surfaces; Part IX derives those surfaces from electron density.

Three chapters cover potentials and phase space, ensembles and integrators, then ab initio MD, coarse-graining, and potential fitting. The layout follows the **MD Notes** in [`writings/md/`](../../writings/md/): numbered chapters with **Bridge** sections and explicit upward links to DDD (Part VII) and DFT (Part IX).

## Where we left the wire

Part VII ended with dislocation lines gliding through a polycrystal, exporting hardening laws and link statistics to crystal plasticity FEM. That picture is still **coarse-grained**: the dislocation core is a line singularity regularized by a cutoff radius; mobility tables are fit from experiments or atomistic snapshots, not derived from first principles.

The copper wire at the atomistic scale is a face-centered cubic lattice of copper nuclei — roughly \(10^{23}\) atoms per centimeter of wire. No laptop integrates Newton's equations for all of them. Molecular dynamics therefore chooses a **representative volume**: a notch tip, a grain boundary segment, a dislocation core, or a slab under uniaxial strain. Periodic boundaries mimic bulk crystal; thermostats exchange heat with a reservoir; a finite timestep and cutoff radius make the simulation tractable.

What MD returns upward: cohesive energy, elastic constants, stacking-fault energies, and mobility parameters that DDD and continuum models consume. What MD demands downward: a potential energy surface — empirical (EAM, MEAM) or learned from DFT (Part IX). The wire's story continues here as vibrating nuclei on that surface.

Part VII left dislocation **cores** as line singularities regularized by a cutoff radius. MD is where that cutoff becomes physical: a cylindrical or spherical volume enclosing the core, periodic or fixed boundaries, and forces from an EAM potential fit to copper's lattice parameter and cohesive energy. The representative volume is not arbitrary — it must be large enough that bulk elastic response dominates the boundary, yet small enough that a workstation or cluster can integrate millions of timesteps. That tension between fidelity and cost repeats at every scale in this book; MD is its first atomistic instance.

## Scene: the scratch at the corner

Optional in the lab, decisive at scale breaks: a sharp grip corner or a scratched surface concentrates stress where elliptic PDEs predict singular gradients. An atomistic supercell at the tip — nuclei, velocities, an EAM potential — resolves bond stretching and dislocation nucleation that no continuum mesh should claim to see. Part VIII is the descent when **fields** fail but **trajectories** still carry the physics.

## Lab act (Notch and calibration — Act V)

Optional in the experiment, mandatory in the book: a scratched surface or sharp grip corner concentrates stress where elliptic PDEs fail. **Act V** resolves bond stretching and dislocation nucleation with atomistic resolution — and calibrates the EAM potentials that **Act VI** will trace to electrons.

## The concept map

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Positions \(\{\mathbf{r}_i\}\), momenta, interatomic potential \(V\) |
| What **structure** does it add? | Hamiltonian mechanics, thermostats, periodic boundaries |
| What **theorem** becomes possible? | Energy conservation (symplectic integrators), ergodic sampling |
| What **breaks** if structure is missing? | Drift in energy, wrong ensemble, cutoff artifacts in EAM fits |

```mermaid
flowchart LR
  PS[Phase space / potentials] --> EN[Ensembles / integrators]
  EN --> LA[LAMMPS workflows]
  LA --> CG[Coarse-graining upward]
  CG --> DFT[DFT Part IX]
```

**Baby picture:** write Newton's equations for nuclei on a potential surface, choose an ensemble (NVT, NPT), integrate with a stable timestep, then fit EAM parameters and export moduli to continuum models. The copper lattice vibrates here; DDD mobility and FEM stiffness inherit the averages.

## Representative schematics (atomistic notes)

The [Atomistic Modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf) collect the phase-space and integrator figures this part implements:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Interatomic potentials; phase space and Hamiltonian | [VIII.1](01-potentials-phase-space.md) |
| 2 | Thermostats, barostats, Verlet integrators | [VIII.2](02-ensembles-integrators.md) |
| 3 | LAMMPS workflows; ab initio MD; coarse-graining upward | [VIII.3](03-ab-initio-and-coarse-graining.md) |

When a representative volume feels arbitrary, return to these schematics: they show what question each patch must answer before its averages export upward.

## Story so far (Parts I–VII)

The wire has been a spring network, a meshed solid, a stress field, a dislocation forest, and now becomes a **lattice of nuclei**:

| Part | Representation | What history was missing |
|------|----------------|--------------------------|
| IV–VI | Smooth \(\mathbf{u}(\mathbf{x})\), \(\boldsymbol{\sigma}\) | Cold work, texture, core singularities |
| VII | Line defects with cutoff cores | Atomic structure inside the core; bond breaking at cracks |

MD closes the gap at **cores, grain boundaries, and fracture surfaces** — regions where Part VII's line singularities and Part VI's continuum fields need atomic resolution. The representative volume is the narrative device: we cannot simulate \(10^{23}\) atoms, so we simulate the smallest patch that still answers the upstream question (stacking-fault energy for DDD mobility, cohesive law for a notch). Part IX will derive the potential surface MD assumes; Part VIII shows how timesteps, thermostats, and LAMMPS workflows make that assumption computable.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** from the opening table reappear here with atomistic vocabulary — and how the **same mathematical moves** from Part I return at the finest classical scale:

| Part I (springs on the wire) | Part VIII (atoms in the wire) |
|------------------------------|-------------------------------|
| State vector \(\mathbf{u}\in\mathbb{R}^N\) | Positions \(\{\mathbf{r}_i\}\in\mathbb{R}^{3N}\) |
| Stiffness matrix \(\mathbf{K}\) | Hessian of interatomic potential \(\nabla^2 U\) |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) at equilibrium | \(\mathbf{F}_i=-\nabla_i U=0\) at minimum energy |
| Timestep evolution (preview in dynamics) | Verlet/leapfrog integration of Newton's equations |
| Limit \(N\to\infty\) sent us to Part II | Representative volume keeps \(N\) finite but meaningful |

Part I's bar elements were a crude two-body spring network; Part VIII's EAM potential is a **refined** two- and many-body model whose parameters must be fit or derived. Every MD timestep still reduces to force evaluation and linear algebra inside the integrator — but the state now tracks nuclei, not continuum nodes. Part IX will derive the potential surface MD assumes; the epilogue will ask how to climb back up with moduli and cohesive energies computed here.

## Bridge

Part VII ended with dislocation lines and the admission that atoms matter at cores and crack tips. The first chapter below puts those atoms back: phase space, Hamiltonian mechanics, and the interatomic potentials that define forces in every MD simulation of copper.
