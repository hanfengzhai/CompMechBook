# Interatomic Potentials and Phase Space

Molecular dynamics (MD) treats atoms as classical particles interacting through potentials fitted to quantum data or experiments. It is the workhorse of atomistic materials mechanics — the scale where the copper wire's lattice resolves into distinct nuclei, each carrying kinetic energy, each feeling forces from neighbors across bonds that may stretch, buckle, or break.

When continuum fields smear atoms into density, MD puts them back. When DFT tracks electrons explicitly, MD assumes nuclei move on a **potential energy surface** those electrons define. Part VIII lives in that middle ground: classical mechanics with quantum-informed forces.

## Closing the arc from Part VII {#opening-hinge-vii3-to-viii1}

If you have read linearly since the prologue, [VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md) closed the mesoscale chapter with OpenDiS → DAMASK → polycrystal FEM export discipline — hardening laws, rate extrapolation, and the `mobility.yaml` row that cites `MD_NVT_shear_PartVIII` without yet showing where that file came from. Part VIII.1 does not repeat that pipeline; it **grounds** the parameters the pipeline borrowed on trust:

| Part VII export (VII.3) | Part VIII.1 vocabulary |
|-------------------------|------------------------|
| Mobility \(M(\tau, T)\) in OpenDiS segment laws | Forces \(\mathbf{F}_i = -\nabla_{\mathbf{r}_i} V\) on a screw-core RVE |
| Peierls threshold and core cutoff \(r_c\) | Core width \(w\) from relaxed atomic positions |
| Stacking-fault energy \(\gamma_{\text{sf}}\) as input | Generalized stacking-fault surface from slab configuration |
| Burgers vector \(b = a_0/\sqrt{2}\) in DDD yaml | EAM-minimized lattice parameter \(a_0\) |
| Taylor \(\tau \propto \sqrt{\rho}\) hardening fit | Cohesive energy and elastic constants from bulk minimization |
| `rate_handoff.txt` citing mobility at \(T_w\) | Hamiltonian \(H\) and phase space \((\{\mathbf{r}_i\}, \{\mathbf{p}_i\})\) at the same \(T_w\) |

[VII.3's Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the **ink** behind dislocation lines — atomic bonding. The [Part VIII opening descent hinge](00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree) closed the **temperature pedigree**: if Act II warmed the wire to \(T_w \approx 379\,\text{K}\) via [V.4 conjugate heat transfer](../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid), every NVT shear that calibrates drag must read that temperature, not 300 K — archive `cht_export.yaml` beside `mobility_cu_screw_{T_w}K.yaml` before OpenDiS inherits the table. This chapter is where both contracts land in one place: **coordinates and forces** replace line singularities; **\(T_w\)** replaces handbook defaults before any trajectory is integrated.

The wire's strength is a story written in dislocation lines; the lines borrow their mobility from phonons and cores the mesoscale cannot resolve. Part VIII.1 is the first page where those cores become **atoms on a potential surface** — still finite-dimensional in any simulation box, but now with the Born–Oppenheimer contract Part IX will derive from \(\rho(\mathbf{r})\). When Peierls stress or mobility tables feel like magic numbers, pause here — not at the integrator in [VIII.2](02-ensembles-integrators.md), not at the EAM fit in [VIII.3](03-ab-initio-and-coarse-graining.md) — because every later atomistic export inherits the potential and lattice parameter this chapter establishes.

## Scene: the notch under the microscope

[VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md) explained that a stress concentration at a notch root is where offline crystal plasticity may fail and FE² embeds a DDD RVE — but even that RVE regularizes the core with a cutoff. Zoom one more step. A molecular dynamics simulation boxes a few nanometers of copper around the notch tip: tens of thousands of fcc lattice sites, periodic or fixed boundaries on the sides, atoms pulled on the top layer to mimic the far-field tension from the tensile frame.

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

### RVE size selection: when periodic bulk is honest

The representative volume element (RVE) is the atomistic analogue of Part IV's mesh: too small and boundary artifacts dominate; too large and cost explodes. For bulk property extraction (moduli, \(\gamma_{\text{sf}}\), cohesive energy), a standard audit on fcc Cu:

| Property | Minimum cell (rule of thumb) | Convergence test |
|----------|------------------------------|------------------|
| Lattice parameter \(a_0\) | 256 atoms (4×4×4 conventional) | \(\|a(N) - a(2N)\| < 0.001\,\text{Å}\) |
| Bulk modulus \(B\) | 500–2000 atoms | \(B(N)\) within 2% of \(B(2N)\) |
| Stacking-fault energy \(\gamma_{\text{sf}}\) | Slab with \(\geq 15\,\text{Å}\) vacuum between periodic images | \(\gamma_{\text{sf}}\) stable when slab thickness doubled |
| Dislocation core structure | Cylinder \(\geq 10\,b\) radius, \(\geq 20\,b\) glide length | Core width and Peierls stress stable vs box size |

**Scale-boundary handshake (RVE → continuum/FEM).** Part VI's variational elasticity and Part IV's \(\mathbf{B}^T \mathbb{C} \mathbf{B}\) consume **homogenized** moduli. MD on a 256-atom periodic cell returns **single-crystal** values; the drawn wire is polycrystalline. Document the reduction:

\[
E_{\text{poly}} \approx \text{Voigt/Reuss average of } C_{ij} \text{ from MD or DFT},
\]

and compare to the tensile-test secant modulus from Act III. A 15% gap between single-crystal MD and wire test is **expected** (texture, cold work); a 15% gap between two MD cells of different size on the **same** geometry is **unconverged RVE** — the atomistic mirror of Part IV's mesh refinement study.

**Flexible boundary methods** (displacement imposed on an outer shell from linear elasticity) reduce image stress when a dislocation or crack cannot be periodized. The outer shell stiffness should match Part VI's \(E\) and \(\nu\) from the handshake table in [VI.3](../part06-continuum/03-variational-elasticity.md#scale-boundary-handshake-mathbbc-from-dftmd-to-variational-elasticity) — otherwise the MD box fights the continuum it is supposed to represent.

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

Beyond mechanics, MD of copper computes **thermal transport** — the property that lets Joule-heated electrons deposit energy the wire must conduct to ambient air (Part VI, Act II). Continuum FEM imports a scalar **thermal conductivity** \(k \approx 400\,\text{W/(m·K)}\) for OFHC copper at room temperature; MD can **derive** that number from atomic vibrations rather than a handbook, and flag when defects or grain boundaries reduce it.

### Green–Kubo: conductivity from equilibrium fluctuations

In the **NVE** ensemble, energy diffuses even without an imposed temperature gradient. The **heat current operator** (microscopic definition, Irving–Kirkwood form) fluctuates around zero; its autocorrelation integrates to thermal conductivity via the **Green–Kubo relation**:

\[
\kappa = \frac{V}{k_B T^2} \int_0^\infty \langle J(0)\, J(t) \rangle \, dt,
\]

where \(V\) is system volume, \(T\) is temperature, and \(J(t)\) is the instantaneous heat flux. Intuitively: fast-decaying correlations mean efficient transport (high \(\kappa\)); long-lived correlations or frequent scattering events lower \(\kappa\). The integral is estimated from a long NVE trajectory by averaging over time origins — the atomistic analogue of estimating a diffusion coefficient from mean-square displacement.

### Green–Kubo in the Part II vocabulary

Part II taught that honest discretization needs a **complete space** and a **norm that measures what physics cares about**. Green–Kubo is the same contract at atomistic scale: the heat flux \(J(t)\) is a random process on a trajectory; its autocorrelation is an inner product in time, and conductivity is a linear functional of that correlation. Read the four concept-map questions from [Part II.2](../part02-functional-analysis/02-normed-spaces.md) again — they apply without modification:

| Question | Green–Kubo answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Heat current \(J(t)\) along the wire axis (scalar component of Irving–Kirkwood flux) |
| What **structure**? | Stationarity in NVE; time-translation invariance of \(\langle J(0)J(t)\rangle\) |
| What **theorem**? | Fluctuation–dissipation: \(\kappa\) from equilibrium correlations (Onsager reciprocity in linear response) |
| What **breaks**? | Too-short trajectories (incomplete time average); finite-size \(V\); anharmonicity at high \(T\) |

**Correlation as an \(L^2\) inner product.** For a stationary process, define the autocorrelation at lag \(\tau\):

\[
C(\tau) = \langle J(0)\, J(\tau) \rangle = \lim_{T_{\text{run}} \to \infty} \frac{1}{T_{\text{run}}} \int_0^{T_{\text{run}}} J(t)\, J(t+\tau)\, dt.
\]

The time average is the ergodic substitute for an ensemble average — the same move Part II made when replacing nodal values with fields: a **limit** must exist and stay in the admissible class. Here the admissible class is "long enough NVE after NVT equilibration," and the limit is \(C(\tau)\) itself. Green–Kubo then writes

\[
\kappa = \frac{V}{k_B T^2} \int_0^\infty C(\tau)\, d\tau,
\]

which is a **Riesz-style pairing**: the transport coefficient is a linear functional of the correlation function, exactly as Part II.3 paired loads with test functions through \(\ell(v) = \int f v\).

**Connection to Part I eigenmodes.** Near equilibrium, expand the potential to second order — the Hessian \(\mathbf{H}\) from [above](#newtons-equations-as-part-i-linear-algebra-at-every-timestep). Phonon modes diagonalize \(\mathbf{H}\); each mode contributes to \(J(t)\) with a characteristic decay time (phonon lifetime). In the harmonic limit, \(C(\tau)\) is a sum of exponentials \(\sum_n A_n e^{-|\tau|/\tau_n}\); the integral \(\int C(\tau)\, d\tau\) is dominated by long-lived acoustic modes — the same normal modes Part I.3 decoupled on the spring network, now with \(N \sim 10^5\) degrees of freedom. Anharmonicity broadens peaks and shortens lifetimes; defect scattering (vacancies from cold drawing) adds faster-decaying channels — lowering \(\kappa\) exactly as the handbook warns for impure wire.

**Completeness analogue.** Part II.2's Cauchy sequences needed Banach completeness so FEM limits stayed in \(H^1\). Green–Kubo needs **statistical completeness**: the time integral of \(C(\tau)\) must converge before the trajectory ends. Diagnostic: plot \(C(\tau)\) and the running integral \(\kappa(T_{\text{cut}}) = \int_0^{T_{\text{cut}}} C(\tau)\, d\tau\) versus \(T_{\text{cut}}\). If \(\kappa(T_{\text{cut}})\) still drifts at the end of the run, the simulation is the thermal analogue of an unconverged mesh — extend \(T_{\text{run}}\) or increase cell size until the plateau stabilizes within 10%.

**Downward link to Part III.** Part III wrote steady conduction \(-k T'' = \dot{q}\) in strong form; Part II placed \(T \in H^1\). Green–Kubo derives the scalar \(k\) that Part III assumed — closing the loop from fluctuation at atomistic scale to the coefficient in the weak thermal form Part IV and Part V discretize. When Joule heating raises local temperature near the grip (Part VI, Act II), the FEM thermal step needs \(k(T)\) with this pedigree, not a handbook paste.

**Nonequilibrium MD (NEMD)** offers an alternative: impose \(\Delta T\) across a slab with fixed hot and cold regions (`fix heat`), measure steady heat flux \(J\), and apply Fourier's law \(\kappa = -J / (\nabla T)\). NEMD is easier to visualize; Green–Kubo is often preferred for bulk properties because it avoids artificial thermostat boundaries in the flux path.

| Method | Ensemble | Observable | Typical Cu supercell |
|--------|----------|------------|---------------------|
| Green–Kubo | NVE after NVT equilibration | \(\langle J(0)J(t)\rangle\) integral | 256–2048 atoms, 100 ps–1 ns |
| NEMD | Steady \(\Delta T\) across slab | \(J\) vs \(\nabla T\) | Same; watch finite-size effects |
| Phonon lifetime (BTE) | Harmonic + anharmonic MD | Mode relaxation times | Links to DFT phonons (Part IX) |

### Scale-boundary handshake: \(\kappa\) from MD to continuum heat equation

Part III wrote steady conduction as \(-k T''(x) = \dot{q}(x)\); Part VI couples that field to Joule heating when current flows through the wire. The FEM thermal step needs \(k(T)\) with the same audit trail as Young's modulus — not a handbook value pasted without pedigree.

**Downward export (MD).** Equilibrate bulk fcc Cu (same 256-atom cell as the EAM Lab act) in **NVT** at 300 K, then switch to **NVE** for 500 ps. Compute heat current autocorrelation with LAMMPS `compute heat/flux` (or post-process from atomic velocities and pairwise energies). Integrate to obtain \(\kappa_{\text{MD}}\):

| Quantity | MD artifact | Pass criterion vs experiment |
|----------|-------------|------------------------------|
| \(\kappa\) at 300 K | `heatflux.dat` + Kubo integral | Within 20% of \(\sim 400\,\text{W/(m·K)}\) for pure Cu |
| Phonon lifetime at LA mode | VACF peak width or spectral decomposition | Same order as DFT `ph.x` (Part VIII.2 handshake) |
| Defected \(\kappa\) | Vacancy or grain-boundary supercell | \(\kappa_{\text{defect}} < \kappa_{\text{bulk}}\) — explains hot spots |

**Upward import (FEM / FVM).** Map \(\kappa_{\text{MD}}\) into the thermal conductivity field in the continuum model:

\[
k(x) = \kappa_{\text{MD}} \quad \text{(bulk)}, \qquad k(x) = \kappa_{\text{GB}} \quad \text{(grain boundary regions from polycrystal mesh)}.
\]

Part V's finite-volume diffusion schemes and Part IV's coupled thermoelastic steps consume the same scalar — the discretization philosophy changes, not the physical number. Archive `kappa_md_300K.txt` beside `cu.elastic/` and `cu.phonon/` in the foundation folder; the epilogue's electro-thermal sensitivity analysis assumes this file exists when Joule heating raises local \(T\) near the grip.

**What breaks without the handshake.** Importing handbook \(k = 400\,\text{W/(m·K)}\) while using DFT-derived elastic moduli and MD-derived stacking-fault energies mixes pedigree levels. A wire whose thermal run predicts grip temperatures 15% too high may have correct mechanics but wrong \(\kappa(T)\) — especially after cold drawing introduces vacancy clusters that scatter phonons. Green–Kubo on a defected supercell quantifies that reduction; skipping it leaves hot-spot predictions un-audited.

Phonon lifetimes from MD validate **DFT phonon** calculations (Part IX) and explain why ultra-pure copper wire conducts heat and current efficiently — defect scattering reduces both. Anharmonicity at high temperature (approaching melt) pushes MD beyond quasi-harmonic DFT; the wire's operating temperature stays well below melt, but **Joule heating** locally raises \(T\) and softens response — coupling MD-derived thermal properties to continuum electro-thermal FEM is the upward path this handshake names.

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

## Lab act: EAM lattice constant from energy minimization (Act V — Notch prelude)

**Act V** in the lab is the notch — stress concentration at a geometric defect. MD resolves the atomic distortion that continuum \(\mathbf{F}\) smooths over. Before running dynamics, **calibrate the ink**: the EAM lattice parameter \(a_0\) and cohesive energy must match bulk copper at 300 K.

Build a minimal FCC copper supercell (4×4×4 conventional cells, 256 atoms) in LAMMPS with `pair_style eam/alloy` and a published `Cu.eam.alloy` file:

| Step | LAMMPS command / action | Expected outcome |
|------|-------------------------|------------------|
| 1 | `units metal`; `atom_style atomic` | Å, ps, eV consistent |
| 2 | `lattice fcc 3.615` (initial guess); `create_box` | Starting geometry |
| 3 | `minimize 1e-12 1e-12 1000 10000` at 0 K | Relaxed \(a_0 \approx 3.615\,\text{Å}\) (potential-dependent) |
| 4 | Read `pe` per atom; multiply by atoms/mol | Cohesive energy \(\approx 3.5\,\text{eV/atom}\) (literature ballpark) |
| 5 | `compute pe/atom`; dump core region at future notch site | Baseline before any defect is introduced |

Sanity checks before exporting to Part VII or Part IX:

- **Pressure** after minimization: \(\langle p \rangle \approx 0\) in NPT-ready cell (use `fix npt` in [VIII.2](02-ensembles-integrators.md) for finite-T).
- **Bulk modulus**: small volumetric strain \(\pm 0.5\%\), fit \(dP/dV\) — compare to experimental \(\sim 140\,\text{GPa}\) order-of-magnitude.
- **Units**: eV/Å³ vs GPa conversion documented in the run log (see [IX.3](../part09-dft/03-dft-workflows.md) unit table).

This 256-atom minimization runs in seconds on a laptop — it is the **foundation archive** Part IX's DFT run will supersede when ab initio parameters are available. Part VII's OpenDiS simulation does not need the full supercell, but its Burgers vector magnitude \(b = a_0/\sqrt{2}\) for FCC must match the \(a_0\) trusted here. When the notch MD run in Act V nucleates dislocations, the core structure is this potential's responsibility — not the Peach–Köhler law alone.

## Concept map checkpoint (interatomic potentials)

This chapter is where Part VII's dislocation lines receive their **ink** — atomic bonding on a Born–Oppenheimer surface. Before integrators sample phase space at lab temperature, summarize what potentials established:

| Question | Part VIII answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Potential energy \(V(\{\mathbf{r}_i\})\); forces \(\mathbf{F}_i = -\nabla_i V\) |
| What **structure**? | EAM decomposition into pair + embedding terms; cutoff radius |
| What **theorem**? | Newton's equations on BO surface; energy conserved in NVE |
| What **breaks**? | Empirical fit away from training data; core structure wrong → bad mobility |

The EAM minimization Lab act calibrated \(a_0\) and cohesive energy before any dynamics — the same foundation archive Part IX's DFT will supersede. Burgers vector \(b = a_0/\sqrt{2}\) links this chapter to Part VII's line geometry.

## Bridge

Potentials define forces; integrators and statistical ensembles define how trajectories sample the correct thermodynamic state. A copper wire at 300 K is not a zero-Kelvin energy minimum — it is a canonical or isothermal–isobaric sample of phase space.

| What Part VII exported | What this chapter supplies | What [VIII.2](02-ensembles-integrators.md) must sample |
|------------------------|----------------------------|--------------------------------------------------------|
| Mobility \(M(\tau,T)\) fit from atomistic snapshots | EAM cohesive energy, lattice parameter \(a_0\) | NVT/NPT trajectories at the lab temperature (300 K) |
| Stacking-fault energy for partial dislocations | Generalized stacking-fault surface from slab pulls | Ensemble averages that define the stress–strain curve |
| Core cutoff radius in OpenDiS | Physical core structure in a cylindrical RVE | Stable timesteps and thermostat transients |
| Taylor hardening from link statistics | Nucleation barriers and cross-slip rates | Converged runs before exporting to DDD yaml tables |

**Scale-boundary handshake (VII.3 → VIII.1 → VIII.2).**

| Mesoscale request (Part VII) | Atomistic foundation (this chapter) | Dynamics audit (next chapter) | Failure mode |
|------------------------------|-------------------------------------|-------------------------------|--------------|
| Burgers vector \(b = a_0/\sqrt{2}\) | EAM-minimized \(a_0\) on fcc lattice | NPT equilibration at 300 K | Wrong lattice constant in DDD yaml |
| Core cutoff \(r_c\) in OpenDiS | Physical core width from cylindrical RVE | Stable \(\Delta t\) under NVE check | Linear elasticity inside core |
| \(\gamma_{\text{sf}}\) for partial dislocations | Generalized stacking-fault surface | Slab pull under NVT ensemble | Wrong stacking sequence in EAM fit |
| Peierls threshold in segment law | Core structure at 0 K minimization | Finite-\(T\) phonon drag from NVT shear | 0 K barrier exported to 300 K DDD |

Part VII's [Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the **ink** behind dislocation lines — atomic bonding. The copper lattice here is that ink: nuclei on a Born–Oppenheimer surface whose parameters were trusted in LAMMPS before Part IX derived them from \(\rho(\mathbf{r})\). The [two clocks note](00-opening.md#two-clocks-reading-order-vs-foundation-pedigree) at the Part VIII opening explains why you may already have run EAM fits in workflow order; linear readers arrive correctly after DDD and should treat this chapter as **resolving the core** the mesoscale model regularized with a cutoff.

Return to the prologue's **Act IV — Hardening**: the load cell curve bent because lines moved; MD shows **how bonds stretch** at the core where Peach–Köhler forces are largest. Part I's pattern returns — state vector \(\{\mathbf{r}_i\}\), force vector from \(\nabla V\), timestep loop as repeated matrix–vector work — now with \(10^5\)–\(10^9\) atoms instead of \(N\) springs. The EAM minimization Lab act above is the **foundation archive** Part IX's DFT run will supersede — but only after [IX.3](../part09-dft/03-dft-workflows.md) documents cutoff and k-mesh convergence.

The [preface descent continuity hinges](../preface.md#descent-continuity-hinges) name [VII.3 → VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) as the **mesoscale → atomistic** turn — the first hinge in the scale descent. The [opening hinge above](#opening-hinge-vii3-to-viii1) is where that turn lands in chapter order: mobility tables and core cutoffs from Part VII receive atomic coordinates and EAM forces before [VIII.2](02-ensembles-integrators.md) samples phase space at lab temperature. [Part VIII opening](../part08-md/00-opening.md#what-you-should-be-able-to-do-after-part-viii) lists the EAM minimization Lab act as the VIII.1 skill checkpoint before ensembles and integrators in VIII.2.

**Foundation pedigree row (VIII.1 archive).**

| Export | File | Upstream consumer | Failure mode |
|--------|------|-------------------|--------------|
| Lattice parameter \(a_0\) | `cu_eam_a0.txt` | Burgers vector \(b = a_0/\sqrt{2}\) in DDD yaml | Wrong Peierls threshold |
| Cohesive energy | `cu_eam_ecoh.txt` | Part IX DFT audit target | EAM fit without DFT cross-check |
| Bulk modulus from volumetric strain | `cu_eam_B.txt` | Part VI \(E,\nu\) handshake | Unconverged RVE size |
| Thermal conductivity \(\kappa\) (Green–Kubo) | `kappa_md_300K.txt` | Part IV/V thermal blocks | Handbook \(k\) mixed with DFT moduli |

[VIII.2](02-ensembles-integrators.md) makes sampling precise: Verlet integration, NVT and NPT control, and LAMMPS workflows that connect atomistic simulation to dislocation dynamics and beyond. Turn the page when the potential is specified and the EAM minimization archive is on disk, but the wire's laboratory temperature has not yet entered the simulation — that is the signal that phase space, not just energy minimization, is the correct stage.
