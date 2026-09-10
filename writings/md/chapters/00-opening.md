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

Part VII ended with dislocation lines gliding through a polycrystal, exporting hardening laws and link statistics to crystal plasticity FEM. That picture is still **coarse-grained**: the dislocation core is a line singularity regularized by a cutoff radius; mobility tables are fit from experiments or atomistic snapshots, not derived from first principles. If **Act II — Warming** ran the conjugate heat transfer loop from [V.4](../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid), the wall temperature \(T_w \approx 379\,\text{K}\) softens phonon drag before the first MD timestep — NVT shear tests and mobility fits in this part must read \(M(\tau, T_w)\), not \(M(\tau, 300\,\text{K})\).

The copper wire at the atomistic scale is a face-centered cubic lattice of copper nuclei — roughly \(10^{23}\) atoms per centimeter of wire. No laptop integrates Newton's equations for all of them. Molecular dynamics therefore chooses a **representative volume**: a notch tip, a grain boundary segment, a dislocation core, or a slab under uniaxial strain. Periodic boundaries mimic bulk crystal; thermostats exchange heat with a reservoir; a finite timestep and cutoff radius make the simulation tractable.

What MD returns upward: cohesive energy, elastic constants, stacking-fault energies, and mobility parameters that DDD and continuum models consume. What MD demands downward: a potential energy surface — empirical (EAM, MEAM) or learned from DFT (Part IX). The wire's story continues here as vibrating nuclei on that surface.

## Descent hinge: cores, mobility, and the \(T_w\) pedigree {#descent-hinge-cores-mobility-and-tw-pedigree}

[Part VII's ascent hinge](../part07-defects/00-opening.md#ascent-hinge-midpoint-and-twin-ladders) closed the **ascent** with the [twin ladders reunion](../part06-continuum/00-opening.md#the-twin-ladders-reunite-galerkin-and-conservation) — Galerkin energy (Part IV) and conservation flux (Part V) on one specimen before descent began. Part VII inherited \(T_w \approx 379\,\text{K}\) from conjugate heat transfer and demanded DDD mobility \(M(\tau, T_w)\), not a room-temperature default. Part VIII inherits that **temperature pedigree** at the atomistic layer: every NVT shear test that calibrates drag, every parallel-tempering ladder in [VIII.3](03-ab-initio-and-coarse-graining.md#wham-part-vii-mobility-hinge-act-ii-temperature-pedigree), and every phonon-lifetime interpolation for rate sensitivity must match the converged \(T_w\) from [V.4's Picard loop](../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) — archive `cht_export.yaml` beside `mobility_cu_screw_{T_w}K.yaml` so OpenDiS, MD, and the epilogue share one wall temperature.

When line cores feel like cutoffs rather than vibrating nuclei, return to [continuity hinge row 7](../appendix/sources.md#continuity-hinges-index-when-the-plot-stutters) (mesoscale → atomistic) and [rows 5–6](../appendix/sources.md#continuity-hinges-index-when-the-plot-stutters) (ascent → descent via [VII.0 ascent hinge](../part07-defects/00-opening.md#ascent-hinge-midpoint-and-twin-ladders)). The [epilogue Handshake 4a](../epilogue/multiscale.md#4a--ddd-strain-rate-to-quasi-static-load-cell-act-iv--hardening) is the workflow-order export of the same rate–temperature contract Part VII opened — Act IV's hardening knee reads power-law \(m\) and \(\tau_{\text{lab}}\) only after mobility at \(T_w\) is archived; the [VII.3 rate handshake](../part07-defects/03-polycrystal-and-fem-handoff.md#scale-boundary-handshake-ddd-strain-rate-to-quasi-static-fem) is the upstream half, Handshake 4a the downstream half. The [Part IX electronic audit hinge](../part09-dft/00-opening.md#electronic-audit-hinge-descent-pedigree-and-tw-phonon) is where phonon lifetimes and quasiharmonic \(\alpha(T)\) receive DFT pedigree at the same \(T_w\) — the audit beneath every mobility table Part VIII measured.

## The atomistic descent in one paragraph

Read this once if you paused after Part VII and wonder why the book now resolves line cores as atoms — every chapter below unpacks one atomistic beat of the same copper wire.

Dislocation dynamics regularized cores with a cutoff radius and borrowed mobility from tables. Part VIII replaces that fiction with vibrating nuclei on an interatomic potential — a representative volume at the notch tip, grain boundary, or screw core where bonds stretch, rebond, and thermal statistics answer questions DDD cannot ask. NVT and NPT ensembles equilibrate the patch; velocity-Verlet integration marches Newton's equations in femtoseconds; LAMMPS workflows fit EAM parameters that export cohesive energy, elastic constants, and stacking-fault energy upward to DDD and continuum models. Part IX audits those potentials from electron density; the [epilogue](../epilogue/multiscale.md) wires the exports into handshakes no single code runs alone. Mesoscale descent taught forest statistics; atomistic descent teaches **trajectories**.

## Two clocks: reading order vs foundation pedigree

This book and the laboratory use **two different orderings** for the same afternoon — and both are intentional.

| Clock | Order | What it optimizes |
|-------|-------|-------------------|
| **Mathematical (chapter order)** | VII mesoscale → VIII atoms → IX electrons | Descend to finer physics after continuum and DDD show where parameters hide their history |
| **Workflow (Act VI foundation)** | IX DFT → VIII MD fit → VII mobility/hardening → IV FEM deck | Trace where input-file numbers actually come from before the operator mounts the wire |

You are reading **mathematical order**: Part VII explained why hardening curves bend; Part VIII resolves cores and fits potentials; Part IX audits those potentials against electron density. In **workflow order** — the invisible afternoon before Act I — someone already ran Quantum ESPRESSO on fcc Cu, fitted an EAM in LAMMPS, calibrated mobility for OpenDiS, and typed Young's modulus into the mesh script. That prequel is documented in [Act VI of the sources appendix](../appendix/sources.md#six-acts-parts-laboratory-time).

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

## How Part VIII connects to Parts II–IX

Part VIII is the **finest discrete scale** before electrons enter explicitly. Like Part II's contract for FEM, each export upward must name its consumer and its audit downward:

| Part VIII chapter | Structure or theorem | Where it reappears |
|-------------------|---------------------|-------------------|
| VIII.1 Potentials | Hamiltonian on BO surface; EAM cutoff | Part VII core width; Part IX \(E_{\text{coh}}\) audit |
| VIII.2 Ensembles | Symplectic Verlet; NVT/NPT sampling | Part VI thermal expansion; Part V boundary \(T\) |
| VIII.3 Coarse-graining | Handoff tables; EAM-fit acceptance | Part IV \(\mathbb{C}\); Part VII \(M(\tau,T)\), \(\gamma_{\text{sf}}\) |

**Mathematical lineage (Part I → Part VIII).** Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) becomes dynamic Newton's laws: forces from \(\nabla V\), equilibrium from \(\nabla V = 0\), normal modes from the Hessian eigensystem. Part II's completeness instinct reappears as **RVE convergence** — halving the simulation cell and checking \(a_0\), \(\kappa\), or \(\gamma_{\text{sf}}\) is the atomistic mesh-refinement study. Part IV's scatter loop is the static limit; velocity Verlet is the same sparsity pattern executed \(10^7\) times per nanosecond of physical time.

**Scale-boundary discipline.** Every quantity MD exports must carry a pedigree row in the foundation folder (see [Act VI in the sources appendix](../appendix/sources.md#six-acts-parts-laboratory-time)):

| Export | Minimum MD evidence | Downstream consumer |
|--------|---------------------|---------------------|
| \(a_0\), \(E_{\text{coh}}\) | Minimized bulk cell; pressure \(\approx 0\) | EAM sanity; Burgers \(b = a_0/\sqrt{2}\) for DDD |
| \(\mathbb{C}_{ij}\) or \(E, \nu\) | NPT small-strain response | Part IV elastic step; Part VI.3 handshake |
| \(\gamma_{\text{sf}}\) | Generalized stacking-fault slab | Part VII partial separation; Peierls stress |
| \(\kappa(T)\) | Green–Kubo or NEMD | Part III/V thermal fields on heated wire |
| \(M(\tau, T)\) | NVT shear on dislocation core | OpenDiS mobility tables |

If a row lists only "Mishin EAM, 2001" with no phonon or DFT cross-check, Part IX is the audit chapter — the same role Part II played when Part I's stiffness matrix needed an \(H^1\) limit. Linear readers arrive here after DDD; workflow readers may have run EAM fits before OpenDiS — both paths converge when the handoff table is populated before the epilogue's multiscale afternoon.

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
| [VII.3 Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md) exports to FEM | [VIII.3](03-ab-initio-and-coarse-graining.md) fits EAM upward |

Part VII regularized dislocation cores with a cutoff radius and mobility law; Part VIII **resolves** those cores as atoms on an interatomic potential — still finite-dimensional in any simulation box, but now with bond breaking, thermal statistics, and phonon drag that no line model captures alone. The copper wire's notch tip (prologue Act V) and grain boundaries (VII.3 polycrystal handoff) are where continuum and DDD models need atomic witnesses. Part IX will derive the potential \(V(\{\mathbf{r}_i\})\) MD assumes; Part VIII shows how LAMMPS workflows, thermostats, and coarse-graining make that assumption computable and exportable.

## Closing the arc from Part VI

If you have read linearly since the prologue, Part VI named the continuum fields that FEM and FVM approximate — Cauchy stress, virtual work, thermal strain — and admitted that cold-drawn strength and notch singularities hide history smooth elasticity cannot explain. Part VIII is the **finest discrete scale** where those fields still make engineering sense before electrons enter explicitly:

| Part VI (continuum on the wire) | Part VIII (atoms on the wire) |
|---------------------------------|-------------------------------|
| Cauchy stress \(\boldsymbol{\sigma}\); virtual work | Virial stress from atomic trajectories in an RVE |
| Hyperelastic energy \(W(\mathbf{F})\); elastic tensor \(\mathbb{C}\) | NPT fluctuations export \(E\), \(\nu\), bulk modulus upward |
| Thermal strain \(\varepsilon_{\text{th}} = \alpha\Delta T\) in balance laws | NVT/NPT equilibration at \(T_w\) from conjugate heat transfer |
| \(J_2\) yield and phenomenological hardening preview | Cohesive energy, \(\gamma_{\text{sf}}\), core width for DDD mobility |
| Smooth fields fail at notches (VI.4 intermission) | Representative volume resolves bond breaking at the notch tip |

Part VI's virtual work principle is the **same statement** Newton's equations satisfy in an atomistic box — forces from \(\nabla V\), equilibrium from \(\nabla V = 0\), thermal averages replacing pointwise fields. Part VII homogenized dislocation motion into forest statistics; Part VIII resolves the **cores and interfaces** those statistics regularized. When the load cell curve bends in Act IV, Part VI named the phenomenon with a fitted yield surface; Part VII named the forest; Part VIII shows how stacking-fault energy and mobility emerge from trajectories on a potential surface Part IX will derive from \(\rho(\mathbf{r})\).

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

### What you should be able to do after Part VIII {#what-you-should-be-able-to-do-after-part-viii}

Each chapter adds one move to the atomistic workflow that supplies numbers the mesoscale and continuum codes trust:

| After chapter | Skill on the copper wire | Minimal artifact |
|---------------|--------------------------|------------------|
| VIII.1 | Write Hamiltonian for N atoms; state phase-space dimension | \(H = \sum_i \|\mathbf{p}_i\|^2/(2m_i) + V(\{\mathbf{r}_i\})\); \(6N\) DOFs |
| VIII.2 | Choose NVT ensemble; implement velocity-Verlet; estimate \(\Delta t\) | Energy drift \(< 10^{-4}\) over 10 ps; \(\Delta t \sim 1\,\text{fs}\) for Cu |
| VIII.3 | Fit EAM to bulk properties; coarse-grain to export moduli upward | \(a_0\), \(E\), \(\gamma_{\text{sf}}\) from a 500-atom fcc box |

None of these require a full ab initio MD production run — but each one is the atomistic audit Part IX will derive from first principles. If you can integrate Newton's equations with a thermostat, read a LAMMPS log for temperature and pressure, and explain what an EAM potential assumes about electron density, you have the finest discrete scale before Kohn–Sham replaces the potential with orbitals.

When Act II warmed the wire but mobility folders still cite 300 K, pause at the [preface row 8 skill checkpoint](../preface.md#skill-navigation-row-8) before trusting any NVT shear or WHAM export — [`parse_cht.sh`](../../scripts/parse_cht.sh) must emit `cht_export.yaml` with converged \(T_w\) first; the [descent hinge](#descent-hinge-cores-mobility-and-tw-pedigree) above and [memory sheet rows 8–9 baby picture](../appendix/memory-sheet.md#rows-8-9-baby-picture-tw-temperature-pedigree) draw the same chain from CHT through MD mobility to DFT phonon audits in Part IX.

## Bridge

Part VII ended with dislocation forests, Taylor hardening, and the admission that **cores and crack tips need atoms**. [VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the quantities MD must supply — stacking-fault energy, core width, mobility tables — and deferred their microscopic origin to this part. Part VIII puts the atoms back on stage.

| What Part VII homogenized | What Part VIII resolves |
|---------------------------|-------------------------|
| Line defects with Burgers vector \(\mathbf{b}\) | Atomic positions \(\{\mathbf{r}_i\}\) in a periodic box |
| Cutoff-regularized core singularity | Bond breaking and thermal vibrations at the notch tip |
| Mobility law \(M(\tau, T)\) as a fitted table | NVT shear tests that measure drag from phonon scattering |
| Taylor \(\tau \propto \sqrt{\rho}\) hardening | Trajectories whose statistics export \(\tau(\gamma)\) upward |

Part I's coupled springs reappear here as coupled nuclei on an interatomic potential — still \(\mathbf{F} = -\nabla V\) at each timestep, still eigenmodes (now phonons) that decouple small oscillations, still stability constraints on \(\Delta t\) that mirror explicit Euler's CFL limit. Part VII exported mesoscale numbers; Part VIII shows how LAMMPS workflows, thermostats, and coarse-graining make those numbers **measurable and traceable** before Part IX derives the potential surface \(V(\{\mathbf{r}_i\})\) from electron density.

**Scale-boundary handshake (Part VII → Part VIII → Part IX).**

| DDD export ([Part VII](../part07-defects/00-opening.md)) | MD contract (this part) | DFT audit (Part IX) | Failure mode |
|-----------------------------------------------------------|-------------------------|---------------------|--------------|
| Cutoff-regularized core; mobility \(M(\tau,T)\) | RVE of fcc Cu nuclei; NVT shear on core | AIMD forces replace empirical \(M\) | Core box too small → spurious image forces |
| \(\gamma_{\text{sf}}\) as input parameter | Relaxed faulted slab in LAMMPS | SCF generalized stacking-fault surface | EAM fit without phonon cross-check |
| Taylor \(\tau \propto \sqrt{\rho}\) hardening | Trajectory statistics export \(\tau(\gamma)\) | Not re-derived at electronic scale | Mobility table with no temperature sweep |
| Polycrystal texture handoff to FEM | \(a_0\), \(E\), \(\nu\) from NPT fluctuations | Bulk modulus from small-strain DFT | Mishin EAM, 2001 — no pedigree row |

The [preface descent continuity hinge](../preface.md#descent-continuity-hinges) names [VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) as the **mesoscale → atomistic** turn — where line cores and mobility tables need atomic bonding before Part IX audits the potential from \(\rho(\mathbf{r})\). Return to the [prologue](../prologue/00-many-scales.md): **Act V** is the notch where continuum fields predict stress concentration but cannot resolve bond breaking; **Act VI** is the offline foundation folder where EAM parameters and mobility tables are fitted before the operator mounts the wire.

The first chapter below opens **phase space** — positions, momenta, Hamiltonian mechanics — and the interatomic potentials every MD run of copper assumes on trust until the audit in Part IX. When the mesh is fine enough but the core is still wrong — that is the hinge between line defects and atoms. Turn the page.
