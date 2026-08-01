# Part VIII — Atomistic Simulation

Parts I–VII treated the copper wire as a continuum or a network of line defects. Part VIII descends to the scale where matter resolves into **individual atoms** — nuclei moving on a potential energy surface, thermal vibrations exchanging energy with a heat bath, bonds stretching and breaking at crack tips where no elliptic PDE can remain valid without regularization.

Molecular dynamics is the workhorse of atomistic materials mechanics. It supplies the interatomic potentials that empirical models require, the mobility laws that dislocation dynamics calibrates, and the fracture trajectories that explain how notches become cracks. Classical MD assumes nuclei follow Born–Oppenheimer surfaces; Part IX derives those surfaces from electron density.

Three chapters cover potentials and phase space, ensembles and integrators, then ab initio MD, coarse-graining, and potential fitting. The layout follows the **MD Notes** in [`writings/md/`](../../writings/md/): numbered chapters with **Bridge** sections and explicit upward links to DDD (Part VII) and DFT (Part IX).

## Chapter guide

| Chapter | Wire story beat | Core object | Handoff |
|---------|-----------------|-------------|---------|
| [VIII.1](01-potentials-phase-space.md) | Copper lattice as \(N\) interacting particles | Lennard-Jones, EAM, periodic boundaries, cutoff | Thermostats and timestep → integrators in VIII.2 |
| [VIII.2](02-ensembles-integrators.md) | NVT equilibration; NPT elastic response | Verlet, Nose–Hoover, stress–strain from MD | Potential fitting and AIMD → coarse-graining in VIII.3 |
| [VIII.3](03-ab-initio-and-coarse-graining.md) | EAM fit exports \(\gamma_{\text{sf}}\), \(E_{\text{coh}}\) | LAMMPS workflows, DeepMD, handoff tables | [Bridge to Part IX](03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) |

Read in order. Each chapter ends with a **Bridge** that states why the next chapter must exist; running MD without understanding ensembles is energy drift disguised as physics; fitting EAM without DFT anchors is multiscale folklore.

## Scene

Part VII ended with dislocation lines gliding through a polycrystal, exporting hardening laws and link statistics to crystal plasticity FEM. That picture is still **coarse-grained**: the dislocation core is a line singularity regularized by a cutoff radius; mobility tables are fit from experiments or atomistic snapshots, not derived from first principles.

The copper wire at the atomistic scale is a face-centered cubic lattice of copper nuclei — roughly \(10^{23}\) atoms per centimeter of wire. No laptop integrates Newton's equations for all of them. Molecular dynamics therefore chooses a **representative volume**: a notch tip, a grain boundary segment, a dislocation core, or a slab under uniaxial strain. Periodic boundaries mimic bulk crystal; thermostats exchange heat with a reservoir; a finite timestep and cutoff radius make the simulation tractable.

What MD returns upward: cohesive energy, elastic constants, stacking-fault energies, and mobility parameters that DDD and continuum models consume. What MD demands downward: a potential energy surface — empirical (EAM, MEAM) or learned from DFT (Part IX). The wire's story continues here as vibrating nuclei on that surface.

## Two clocks: reading order vs foundation pedigree

This book and the laboratory use **two different orderings** for the same afternoon — and both are intentional.

| Clock | Order | What it optimizes |
|-------|-------|-------------------|
| **Mathematical (chapter order)** | VII mesoscale → VIII atoms → IX electrons | Descend to finer physics after continuum and DDD show where parameters hide their history |
| **Workflow (Act VI foundation)** | IX DFT → VIII MD fit → VII mobility/hardening → IV FEM deck | Trace where input-file numbers actually come from before the operator mounts the wire |

You are reading **mathematical order**: Part VII explained why hardening curves bend; Part VIII resolves cores and fits potentials; Part IX audits those potentials against electron density. In **workflow order** — the invisible afternoon before Act I — someone already ran Quantum ESPRESSO on fcc Cu, fitted an EAM in LAMMPS, calibrated mobility for OpenDiS, and typed Young's modulus into the mesh script. That prequel is documented in [Act VI of the sources appendix](../appendix/sources.md#six-acts--parts-laboratory-time).

If the descent feels backward relative to how codes are built, treat Part IX as the **pedigree chapter** for every potential Part VIII already assumed — the same role Part II played for Part I's stiffness matrices. You may also read Part IX before Part VIII using the [scale-first path](../prologue/00-many-scales.md#the-experiment-as-plot) in the prologue; linear readers should arrive here correctly after atomistics and read IX as the audit, not a bolt-on.

Part VII left dislocation **cores** as line singularities regularized by a cutoff radius. MD is where that cutoff becomes physical: a cylindrical or spherical volume enclosing the core, periodic or fixed boundaries, and forces from an EAM potential fit to copper's lattice parameter and cohesive energy. The representative volume is not arbitrary — it must be large enough that bulk elastic response dominates the boundary, yet small enough that a workstation or cluster can integrate millions of timesteps. That tension between fidelity and cost repeats at every scale in this book; MD is its first atomistic instance.

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

## Representative schematics (Atomistic Modeling Notes)

The [Atomistic Modeling Notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf) follow the same ME 412 habit: each schematic is a baby picture of the atomistic pipeline. Use them as a visual index while reading:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Interatomic potentials, phase space, periodic boundaries on a Cu representative volume | [VIII.1](01-potentials-phase-space.md) |
| 2 | Ensembles (NVT, NPT), symplectic integrators, LAMMPS workflows | [VIII.2](02-ensembles-integrators.md) |
| 3 | Ab initio MD, coarse-graining, DeepMD; fitting EAM upward to DDD and FEM | [VIII.3](03-ab-initio-and-coarse-graining.md) |

Each schematic answers the four concept-map questions for one atomistic layer. When a cutoff radius or timestep choice feels arbitrary, return to the matching row: *what object, what structure, what theorem, what breaks?* Part VII regularized dislocation cores with a cutoff; Part VIII resolves those cores as vibrating nuclei on a potential surface.

## Story so far (Parts I–VII)

The wire has been a spring network, a meshed solid, a stress field, a dislocation forest, and now becomes a **lattice of nuclei**:

| Part | Representation | What history was missing |
|------|----------------|--------------------------|
| IV–VI | Smooth \(\mathbf{u}(\mathbf{x})\), \(\boldsymbol{\sigma}\) | Cold work, texture, core singularities |
| VII | Line defects with cutoff cores | Atomic structure inside the core; bond breaking at cracks |

MD closes the gap at **cores, grain boundaries, and fracture surfaces** — regions where Part VII's line singularities and Part VI's continuum fields need atomic resolution. The representative volume is the narrative device: we cannot simulate \(10^{23}\) atoms, so we simulate the smallest patch that still answers the upstream question (stacking-fault energy for DDD mobility, cohesive law for a notch). Part IX will derive the potential surface MD assumes; Part VIII shows how timesteps, thermostats, and LAMMPS workflows make that assumption computable.

## Closing the arc from Part VII

If you have read linearly since the prologue, Part VII's closing checkpoint exported hardening laws and link statistics from dislocation dynamics to crystal plasticity FEM. Part VIII is the next **descent** — where line singularities become vibrating nuclei:

| Part VII (dislocations on the wire) | Part VIII (atoms on the wire) |
|-------------------------------------|-------------------------------|
| Line defects with cutoff cores | Representative volume of fcc Cu nuclei |
| Mobility tables from experiments or fits | Mobility from MD shear tests on cores |
| Stacking-fault energy as input parameter | \(\gamma_{\text{sf}}\) from relaxed faulted configurations |
| Taylor \(\sqrt{\rho}\) hardening law | Cohesive energy and elastic constants from fluctuations |
| [VII.3 Bridge](03-polycrystal-and-fem-handoff.md) exports to FEM | [VIII.3](03-ab-initio-and-coarse-graining.md) fits EAM upward |

Part VII regularized dislocation cores with a cutoff radius and mobility law; Part VIII **resolves** those cores as atoms on an interatomic potential — still finite-dimensional in any simulation box, but now with bond breaking, thermal statistics, and phonon drag that no line model captures alone. The copper wire's notch tip (prologue Act V) and grain boundaries (VII.3 polycrystal handoff) are where continuum and DDD models need atomic witnesses. Part IX will derive the potential \(V(\{\mathbf{r}_i\})\) MD assumes; Part VIII shows how LAMMPS workflows, thermostats, and coarse-graining make that assumption computable and exportable.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** reappear here with atomistic vocabulary — and how the **same mathematical moves** from Part I return on phase space:

| Part I (springs on the wire) | Part VIII (atoms on the wire) |
|------------------------------|-------------------------------|
| State vector \(\mathbf{u}\) | Positions \(\{\mathbf{r}_i\}\) and momenta \(\{\mathbf{p}_i\}\) |
| Stiffness matrix \(\mathbf{K}\) | Hessian \(\nabla^2 V\) of the interatomic potential |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) at equilibrium | \(\nabla V = 0\) at energy minimum (static limit) |
| Eigenmodes decouple vibration | Normal modes from mass-weighted Hessian (phonons) |
| Timestep stability (implicit/explicit) | Verlet / velocity-Verlet with \(\Delta t\) constraint |

Part I's coupled springs become Part VIII's coupled nuclei on a potential surface — still finite-dimensional on any simulation box, still governed by linear algebra at each force evaluation, but now with **thermal statistics** and **bond breaking** that no elliptic FEM mesh resolves without regularization. Part VII exported mobility and stacking-fault energy as tables; Part VIII shows how those tables are measured or computed from trajectories. The copper wire's core is no longer a line singularity with a cutoff; it is a patch of vibrating atoms whose averages feed the mesoscale. Part IX will derive the potential \(V\) itself from electron density.

## Lab act: V–VI — Notch and offline foundation

**Act V** is the optional scratch or grip corner where continuum fields predict *where* stress concentrates but cannot resolve bond breaking — MD's representative volume lives here. **Act VI** is the prequel every practitioner runs offline: EAM parameters, mobility tables, and elastic constants that Part VII and Part IV consume without re-deriving them each run. Part VIII connects both acts: atomistic trajectories at the notch tip and potential fitting that feeds the whole ladder upward.

### What you should be able to do after Part VIII

Each chapter adds one move to the atomistic workflow that supplies numbers the mesoscale and continuum codes trust:

| After chapter | Skill on the copper wire | Minimal artifact |
|---------------|--------------------------|------------------|
| VIII.1 | Write Hamiltonian for N atoms; state phase-space dimension | \(H = \sum_i \|\mathbf{p}_i\|^2/(2m_i) + V(\{\mathbf{r}_i\})\); \(6N\) DOFs |
| VIII.2 | Choose NVT ensemble; implement velocity-Verlet; estimate \(\Delta t\) | Energy drift \(< 10^{-4}\) over 10 ps; \(\Delta t \sim 1\,\text{fs}\) for Cu |
| VIII.3 | Fit EAM to bulk properties; coarse-grain to export moduli upward | \(a_0\), \(E\), \(\gamma_{\text{sf}}\) from a 500-atom fcc box |

None of these require a full ab initio MD production run — but each one is the atomistic audit Part IX will derive from first principles. If you can integrate Newton's equations with a thermostat, read a LAMMPS log for temperature and pressure, and explain what an EAM potential assumes about electron density, you have the finest discrete scale before Kohn–Sham replaces the potential with orbitals.

## Bridge

Part VII ended with dislocation forests, Taylor hardening, and the admission that **cores and crack tips need atoms**. [VII.3](03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the quantities MD must supply — stacking-fault energy, core width, mobility tables — and deferred their microscopic origin to this part. Part VIII puts the atoms back on stage.

| What Part VII homogenized | What Part VIII resolves |
|---------------------------|-------------------------|
| Line defects with Burgers vector \(\mathbf{b}\) | Atomic positions \(\{\mathbf{r}_i\}\) in a periodic box |
| Cutoff-regularized core singularity | Bond breaking and thermal vibrations at the notch tip |
| Mobility law \(M(\tau, T)\) as a fitted table | NVT shear tests that measure drag from phonon scattering |
| Taylor \(\tau \propto \sqrt{\rho}\) hardening | Trajectories whose statistics export \(\tau(\gamma)\) upward |

Part I's coupled springs reappear here as coupled nuclei on an interatomic potential — still \(\mathbf{F} = -\nabla V\) at each timestep, still eigenmodes (now phonons) that decouple small oscillations, still stability constraints on \(\Delta t\) that mirror explicit Euler's CFL limit. Part VII exported mesoscale numbers; Part VIII shows how LAMMPS workflows, thermostats, and coarse-graining make those numbers **measurable and traceable** before Part IX derives the potential surface \(V(\{\mathbf{r}_i\})\) from electron density.

The first chapter below opens **phase space** — positions, momenta, Hamiltonian mechanics — and the interatomic potentials every MD run of copper assumes on trust until the audit in Part IX. Turn the page when the mesh is fine enough but the core is still wrong: that is the hinge between line defects and atoms.
