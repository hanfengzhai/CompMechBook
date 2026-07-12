# Interatomic Potentials and Phase Space

Molecular dynamics (MD) treats atoms as classical particles interacting through potentials fitted to quantum data or experiments. It is the workhorse of atomistic materials mechanics — the scale where the copper wire's lattice resolves into distinct nuclei, each carrying kinetic energy, each feeling forces from neighbors across bonds that may stretch, buckle, or break.

When continuum fields smear atoms into density, MD puts them back. When DFT tracks electrons explicitly, MD assumes nuclei move on a **potential energy surface** those electrons define. Part VIII lives in that middle ground: classical mechanics with quantum-informed forces.

## Story so far (Parts I–VII)

| Stage | Scale | Wire instance |
|-------|-------|---------------|
| Parts I–VI | Continuum fields and meshes | Tensile + thermal FEM/FVM |
| Part VII | Dislocation lines; forest density \(\rho\) | Hardening curve from cold draw |
| **VIII.1 (here)** | Atomic positions \(\{\mathbf{r}_i\}\); potential \(V\) | Notch root under the microscope |
| [VIII.2](02-ensembles-integrators.md) (next) | Verlet; NVT/NPT ensembles | Laboratory temperature in the box |
| [VIII.3](03-ab-initio-and-coarse-graining.md) | EAM fits; export tables | Parameters climb back to FEM and DDD |

Part VII's [Bridge](03-polycrystal-and-fem-handoff.md#bridge) named the **ink** behind dislocation lines — atomic bonding. This chapter is the first atomistic page: phase space, Hamiltonian structure, EAM potentials, and the LAMMPS mindset. The [two clocks note](00-opening.md#two-clocks-reading-order-vs-foundation-pedigree) at the Part VIII opening explains why workflow order may have already fit EAM parameters from Part IX; linear readers arrive correctly after DDD and should treat this chapter as **resolving the core** the mesoscale model regularized with a cutoff.

## Scene: the notch under the microscope

Part VII explained that a stress concentration at a notch root is where continuum elasticity hands off to dislocation nucleation. Zoom one more step. A molecular dynamics simulation boxes a few nanometers of copper around the notch tip: tens of thousands of fcc lattice sites, periodic or fixed boundaries on the sides, atoms pulled on the top layer to mimic the far-field tension from the tensile frame.

There is no \(\boldsymbol{\sigma}(\mathbf{x})\) field in the data — only positions \(\mathbf{r}_i(t)\) and forces \(\mathbf{F}_i = -\nabla_{\mathbf{r}_i} V\). The potential \(V\) might be an EAM fit to DFT energies from Part IX; the integrator might be velocity Verlet with a femtosecond timestep. Bonds at the tip stretch; a dislocation loop nucleates; the student watches plasticity begin as coordinated atomic motion, not as a yield surface parameter.

This scene is why MD exists in the ladder. FEM on the wire tells us where stress concentrates; DDD tells us how lines move in response; MD tells us what happens when the smeared continuum finally resolves into neighbors swapping across a disturbed lattice. The rest of Part VIII supplies the Hamiltonian structure, potential forms, and LAMMPS workflows that make such a box simulation reproducible rather than anecdotal.

## Phase space and the Hamiltonian

For \(N\) atoms with positions \(\mathbf{r}_i\) and momenta \(\mathbf{p}_i\), the **Hamiltonian** is

\[
H(\{\mathbf{r}_i\}, \{\mathbf{p}_i\}) = \sum_{i=1}^{N} \frac{\|\mathbf{p}_i\|^2}{2m_i} + V(\{\mathbf{r}_i\}),
\]

where \(V\) is the **potential energy** — the object every MD simulation must specify. Hamilton's equations,

\[
\dot{\mathbf{r}}_i = \frac{\partial H}{\partial \mathbf{p}_i} = \frac{\mathbf{p}_i}{m_i}, \qquad
\dot{\mathbf{p}}_i = -\frac{\partial H}{\partial \mathbf{r}_i} = -\nabla_{\mathbf{r}_i} V,
\]

are equivalent to Newton's second law:

\[
m_i \ddot{\mathbf{r}}_i = -\nabla_{\mathbf{r}_i} V.
\]

The **phase space** \((\{\mathbf{r}_i\}, \{\mathbf{p}_i\})\) has dimension \(6N\). For a nanoscale cube of copper with \(10^5\) atoms, that is \(6 \times 10^5\) coupled ODEs — tractable on modern GPUs for picoseconds to nanoseconds of physical time, insufficient for wire-scale processes without coarse-graining.

## Newton's equations as Part I linear algebra at every timestep

Part I taught \(\mathbf{K}\mathbf{u}=\mathbf{f}\) for static equilibrium. MD is the **dynamic** analogue: at each timestep, forces \(\mathbf{F}_i = -\nabla_{\mathbf{r}_i} V\) play the role of loads, and the integrator advances positions and velocities as if solving a sparse time-stepping system millions of times.

| Part I (static) | Part VIII (dynamic) |
|-----------------|---------------------|
| State \(\mathbf{u}\) | Phase \((\{\mathbf{r}_i\}, \{\mathbf{p}_i\})\) |
| Stiffness \(\mathbf{K}\) from energy Hessian | Force field \(-\nabla V\) from potential |
| Solve once for equilibrium | Integrate \(10^5\)–\(10^7\) steps |
| Eigenmodes decouple vibration | Phonon spectrum = Hessian eigenvalues at equilibrium |

Near a perfect lattice minimum, expand \(V\) to second order in displacements \(\mathbf{u}_i\). The Hessian matrix \(\mathbf{H}\) (block-sparse, local neighbors only) has eigenvalues \(\omega^2\) — phonon modes that Part I would have called normal modes of a spring network, now with \(N \sim 10^5\) degrees of freedom. MD does not diagonalize \(\mathbf{H}\) each step; it propagates the full nonlinear dynamics. But the **same linear-algebraic structure** — local coupling, sparse assembly, eigenmodes as decoupled coordinates — reappears whenever we linearize, compute elastic constants from fluctuations, or validate an EAM potential against DFT phonons.

Velocity Verlet, the workhorse integrator, is a three-line recurrence:

\[
\mathbf{p}_i^{n+\frac{1}{2}} = \mathbf{p}_i^n + \frac{\Delta t}{2}\mathbf{F}_i^n, \quad
\mathbf{r}_i^{n+1} = \mathbf{r}_i^n + \frac{\Delta t}{m_i}\mathbf{p}_i^{n+\frac{1}{2}}, \quad
\mathbf{p}_i^{n+1} = \mathbf{p}_i^{n+\frac{1}{2}} + \frac{\Delta t}{2}\mathbf{F}_i^{n+1}.
\]

Each step is \(O(N)\) with a neighbor list — the atomistic version of sparse matrix–vector multiply. When LAMMPS reports `thermo` output every thousand steps, it is printing the trajectory of a gigantic dynamical system whose stable static limit (if one exists) would be found by Part IV's Newton–Raphson on a continuum mesh. MD and FEM are not rival philosophies; they are static and dynamic faces of the same balance laws, at different scales and state dimensions.

## Why classical MD works for copper

Born–Oppenheimer separation (Part IX) justifies treating nuclei as classical point masses when electronic excitations are frozen out. At room temperature, thermal energy \(k_B T \approx 0.025\) eV is small compared to bond energies (~few eV) and much smaller than electronic band gaps. Copper's valence electrons adiabatically follow nuclear motion; the **potential surface** \(V\) encodes their quantum average.

MD fails when chemistry changes — oxidation, dissociation, charge transfer — or when quantum nuclear effects matter (light atoms, very low \(T\)). For ductile fracture and thermal vibration of copper, classical MD with a good potential is the standard tool.

## Interatomic potentials: a taxonomy

| Class | Form | Use case | Copper? |
|-------|------|----------|---------|
| Lennard-Jones | Pairwise \(4\epsilon[(\sigma/r)^{12} - (\sigma/r)^6]\) | Noble gases, benchmarks | Poor (no fcc stability) |
| Embedded Atom Method (EAM) | Pairwise + embedding \(F(\bar{\rho}_i)\) | Metals, alloys | **Standard for Cu** |
| MEAM | Angular-dependent EAM | Metals, covalent–metallic | Used for Cu alloys |
| Tersoff / Stillinger–Weber | Bond order | Covalent solids (Si, C) | Not primary for Cu |
| ReaxFF | Reactive bond order | Chemistry, fracture with bonds breaking | Cu–O systems |
| ML potentials (GAP, NequIP, etc.) | Neural network on local environment | DFT accuracy at MD cost | Emerging for Cu |

### EAM for copper

The **EAM** potential writes

\[
V = \sum_{i<j} \phi(r_{ij}) + \sum_i F\!\left(\sum_{j \neq i} \rho_j(r_{ij})\right),
\]

where \(\phi\) is a pairwise repulsion, \(\rho_j\) is an electron-density contribution from atom \(j\), and \(F\) is the embedding energy of atom \(i\) in that local density. Many-body effects — the volume dependence of cohesion in metals — emerge without explicit angle terms.

Potentials such as **Mishin et al.** EAM for Cu are fitted to DFT energies, lattice constants, elastic constants, and vacancy formation energies. A wire simulation's credibility begins with which potential file sits in the input deck.

### Machine-learned potentials

**ML interatomic potentials** train on DFT datasets of energies and forces for diverse configurations (bulk, surfaces, defects, liquids). They aim for near-DFT accuracy at MD cost. For copper fracture — where bond breaking at crack tips matters — ML potentials increasingly replace fixed functional forms, at the price of careful validation outside the training manifold.

The author's [atomistic modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf) and graphene fracture studies illustrate MD for crack propagation and thermal effects — where continuum fields cannot resolve bond breaking.

## Computing forces and the neighbor list

Each timestep requires forces \(-\nabla_{\mathbf{r}_i} V\). Pairwise sums scale as \(O(N^2)\); practical codes use **neighbor lists** rebuilt every few steps: only atoms within cutoff \(r_c\) contribute. Cutoff choice balances accuracy (EAM often needs \(r_c \sim 5\)–\(6\) Å for Cu) against list rebuild cost.

For \(N\) atoms with fixed density, neighbor list algorithms achieve \(O(N)\) per step — enabling billion-atom simulations on GPU codes like [GPUMD](https://github.com/brucefan1983/GPUMD).

## Periodic boundary conditions

Bulk copper wire interior is modeled as **periodic**: atom leaving one face of the simulation cell re-enters from the opposite face. Periodic boundaries eliminate surface effects and mimic an infinite crystal — appropriate for bulk modulus, dislocation glide in the interior, or thermal conductivity of the lattice.

They are **inappropriate** for surfaces, cracks, or wire diameters where free surfaces dominate. Those simulations use **free boundaries** or **fixed** atoms at the outer shell, sometimes coupled to continuum elasticity (flexible boundary methods) to mimic a larger elastic surrounding.

## Defects in MD: how to introduce them

| Defect | MD construction |
|--------|-----------------|
| Vacancy | Remove one atom |
| Interstitial | Insert atom at interstitial site |
| Dislocation | Insert half-plane (Volterra construction) or quench from melt |
| Grain boundary | Rotate two blocks and join |
| Crack | Delete a plane of atoms or strain until failure |
| Notch | Geometric removal at free surface |

After insertion, **energy minimization** (conjugate gradient, fire algorithm) relaxes the configuration before dynamics. A poorly relaxed dislocation core spews phonons and drifts spuriously — the MD analogue of an unconverged FEM mesh.

For the copper wire notch problem — stress concentration leading to fracture — MD resolves bond breaking at the tip in ways linear elasticity cannot, feeding **fracture toughness** estimates and **crack-tip dislocation nucleation** mechanisms upstream of DDD.

## Initial conditions and equilibration

A raw crystal at \(T = 0\) K is not a physical state at finite temperature. Standard workflow:

1. **Minimize** energy to remove bad contacts.
2. **Assign velocities** from Maxwell–Boltzmann distribution at target \(T\).
3. **Equilibrate** in NVT ensemble until temperature and pressure stabilize.
4. **Production run** in the ensemble matching the experiment (NVE, NVT, NPT).

Skipping equilibration produces transient artifacts in stress and diffusion coefficients — the atomistic counterpart of starting a transient FEM solve from incompatible initial data.

## Observables linking MD to coarser scales

From trajectories \(\{\mathbf{r}_i(t)\}\), MD extracts:

- **Radial distribution function** \(g(r)\): validates liquid vs. solid, melting.
- **Mean square displacement**: diffusion coefficients via Einstein relation.
- **Stress tensor** (Irving–Kirkwood or Hardy): continuum stress for coupling to FEM.
- **Dislocation identification** (DXA, CNA): extract lines for DDD comparison.
- **Phonon density of states**: thermal properties, compare to DFT.

A single MD run of a copper nanowire under tension yields a stress–strain curve that **includes** thermal noise, nucleation events, and size effects — richer than continuum elasticity, narrower than a real wire with millions of grains.

## Thermal conductivity and phonons

Beyond mechanics, MD of copper computes **thermal transport** via Green–Kubo relations from heat current autocorrelation functions, or nonequilibrium MD with imposed temperature gradients. Phonon lifetimes from MD validate **DFT phonon** calculations (Part IX) and explain why ultra-pure copper wire conducts heat and current efficiently — defect scattering reduces both.

Anharmonicity at high temperature (approaching melt) pushes MD beyond quasi-harmonic DFT; the wire's operating temperature stays well below melt, but **Joule heating** locally raises \(T\) and softens response — coupling MD-derived thermal properties to continuum electro-thermal FEM.

## Alloyed and impure wire

Commercial copper wire is not 99.999% pure. **Solutes** (oxygen, silver trace) pin dislocations and alter resistivity. **EAM alloy** potentials (Cu–Ag, Cu–O with ReaxFF for oxidation) extend MD beyond pure element studies. Solute–dislocation interaction energies from DFT inform both MD and DDD obstacle strengths.

The pure-copper narrative in this book is pedagogical; production wire adds **chemistry** at surfaces and grain boundaries — another descent toward DFT when oxidation or electromigration matters.

## Limitations of scale and time

| Challenge | Typical copper MD | Wire experiment |
|-----------|-------------------|-----------------|
| System size | \(10^4\)–\(10^9\) atoms (~nm–µm) | mm–cm diameter |
| Time | ps–ns (µs with rare events) | seconds to years |
| Strain rate | \(10^7\)–\(10^{10}\) s\(^{-1}\) | \(10^{-4}\)–\(10^{-1}\) s\(^{-1}\) |

**Strain-rate gap** and **time-scale gap** are fundamental. MD informs **mechanisms** (how dislocations nucleate at a notch) and **parameters** (mobility, stacking-fault energy), not direct prediction of wire lifetime without extrapolation or multiscale coupling (epilogue).

## Software and file formats

[LAMMPS](https://www.lammps.org/) dominates metal MD: input scripts specify units (metal: Å, ps, eV), potential style (`eam/alloy`), ensemble, and output dumps. Typical artifacts:

```
# Conceptual LAMMPS workflow for Cu bulk modulus
units           metal
atom_style      atomic
read_data       cu_fcc.data
pair_style      eam/alloy
pair_coeff      * * Cu.eam.alloy Cu
fix             1 all npt temp 300 300 0.1 iso 0 0 1
run             50000
```

Potentials define forces; integrators and statistical ensembles define how trajectories sample the correct thermodynamic state — the subject of the next chapter.

## Bridge

Potentials define forces; integrators and statistical ensembles define how trajectories sample the correct thermodynamic state. A copper wire at 300 K is not a zero-Kelvin energy minimum — it is a canonical or isothermal–isobaric sample of phase space.

| What Part VII exported | What this chapter supplies | What [VIII.2](02-ensembles-integrators.md) must sample |
|------------------------|----------------------------|--------------------------------------------------------|
| Mobility \(M(\tau,T)\) fit from atomistic snapshots | EAM cohesive energy, lattice parameter \(a_0\) | NVT/NPT trajectories at the lab temperature (300 K) |
| Stacking-fault energy for partial dislocations | Generalized stacking-fault surface from slab pulls | Ensemble averages that define the stress–strain curve |
| Core cutoff radius in OpenDiS | Physical core structure in a cylindrical RVE | Stable timesteps and thermostat transients |
| Taylor hardening from link statistics | Nucleation barriers and cross-slip rates | Converged runs before exporting to DDD yaml tables |

Part VII's [Bridge](../../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the **ink** behind dislocation lines — atomic bonding. The copper lattice here is that ink: nuclei on a Born–Oppenheimer surface whose parameters were trusted in LAMMPS before Part IX derived them from \(\rho(\mathbf{r})\). The [two clocks note](00-opening.md#two-clocks-reading-order-vs-foundation-pedigree) at the Part VIII opening explains why you may already have run EAM fits in workflow order; linear readers arrive correctly after DDD and should treat this chapter as **resolving the core** the mesoscale model regularized with a cutoff.

Return to the prologue's **Act IV — Hardening**: the load cell curve bent because lines moved; MD shows **how bonds stretch** at the core where Peach–Köhler forces are largest. Part I's pattern returns — state vector \(\{\mathbf{r}_i\}\), force vector from \(\nabla V\), timestep loop as repeated matrix–vector work — now with \(10^5\)–\(10^9\) atoms instead of \(N\) springs.

**Act V — Notch** is the scene this chapter opened: FEM on the wire names where stress concentrates; DDD names how lines respond; MD names what happens when the smeared continuum finally resolves into neighbors swapping across a disturbed lattice. The epilogue's multiscale workflows wire those three answers together when no single code spans the ladder.

| Scale on the wire | State variable | Force law | Book chapter |
|-------------------|----------------|-----------|--------------|
| Continuum FEM | \(\mathbf{u}(\mathbf{x})\), \(\boldsymbol{\sigma}\) | Virtual work / \(\mathbb{C}:\boldsymbol{\varepsilon}\) | Parts IV, VI |
| DDD | Segment network \(\{\mathbf{r}_s,\boldsymbol{\xi},\mathbf{b}\}\) | Peach–Köhler + mobility | Part VII |
| MD (this chapter) | Atomic positions \(\{\mathbf{r}_i\}\) | \(\mathbf{F}_i=-\nabla_i V\) | Part VIII |
| DFT (preview) | \(\rho(\mathbf{r})\), orbitals | Kohn–Sham + SCF | Part IX |

Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) is the finite-\(N\) shadow of all four rows: MD replaces springs with atoms, DFT replaces the empirical \(V\) with a self-consistent electronic energy, and the epilogue asks which row to trust at each interface.

[VIII.2](02-ensembles-integrators.md) makes sampling precise: Verlet integration, NVT and NPT control, and LAMMPS workflows that connect atomistic simulation to dislocation dynamics and beyond. Turn the page when the potential is specified but the wire's laboratory temperature has not yet entered the simulation — that is the signal that phase space, not just energy minimization, is the correct stage.
