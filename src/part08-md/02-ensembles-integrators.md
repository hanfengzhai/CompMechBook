# Ensembles, Integrators, and Practical Molecular Dynamics

MD is not merely integrating Newton's laws — it is **controlled sampling** of statistical mechanics. The integrator and thermostat determine what physical state the simulation represents. A copper wire held at room temperature in the lab corresponds to an **NVT** or **NPT** ensemble at 300 K and ambient pressure — not an isolated **NVE** cluster drifting with whatever energy the initial velocity draw happened to assign.

Getting the ensemble wrong is not a small error. It is simulating the wrong experiment.

## Story so far (Parts I–VII & VIII.1)

| Stage | What the wire became | Key object |
|-------|----------------------|------------|
| Parts I–VI | Continuum PDEs, FEM, FVM, stress, balance | Engineering-scale fields and laws |
| Part VII | Dislocation lines; strain hardening | Mesoscale defects on a lattice |
| [VIII.1](01-potentials-phase-space.md) | EAM potential; phase space \((\mathbf{r},\mathbf{p})\) | Interatomic forces from fitted surfaces |
| **VIII.2 (here)** | Verlet; NVT/NPT at 300–600 K | Controlled sampling of statistical mechanics |

Part VII's dislocations move on atomistic substrates; this chapter asks whether the MD trajectory represents the **same temperature and pressure** as the laboratory wire. The [prologue](../../prologue/00-many-scales.md) **Act IV — Hardening** bent the load cell curve at laboratory temperature — NVT and NPT ensembles are how that temperature enters simulation, not as a comment line in an input deck.

## Scene: thermometers in a nanoscale lab

A nanowire segment in MD cannot feel the laboratory thermostat on the wall — only the algorithm enforcing 300 K at the boundaries. NVE, NVT, NPT: each name is a contract about what is held fixed while the atoms move. Verlet integration advances positions; a Nosé–Hoover chain adds noise and drag in calibrated amounts. Get the ensemble wrong and you tensile-test frozen Cu at 0 K while believing it is room temperature.

### A copper nanowire tension test (MD setup)

Return to the copper wire from the prologue, now at nanometer scale. A cylindrical segment of fcc Cu — perhaps 10 nm diameter, 50 nm gauge length — carries uniaxial tension in a **NPT** ensemble at 300 K and 0 GPa hydrostatic pressure until equilibrated, then switches to **NVT** or **NPT with fixed lateral stress** for the load ramp. The state is positions and velocities of \(\sim 10^5\)–\(10^6\) atoms; the governing principle is Newton's laws with an EAM potential fit from Part IX's DFT outputs; the discretization is Verlet with \(\Delta t \approx 1\) fs and a neighbor cutoff beyond the potential range.

What passes upward to Part VII or Part IV is not the raw trajectory but **effective moduli**, **stacking-fault energies**, and **fracture stress at this strain rate** — numbers that explain why the engineering wire's yield point differs from bulk DFT elasticity. If you heat the segment to mimic annealing, watch **vacancy diffusion** and **dislocation annihilation** in the trajectory; those are the atomistic events Part VII's dislocation density must summarize.

## The symplectic baseline: Verlet integration

The **Verlet** algorithm advances positions from the previous two timesteps:

\[
\mathbf{r}^{n+1} = 2\mathbf{r}^n - \mathbf{r}^{n-1} + \mathbf{a}^n \Delta t^2,
\]

where \(\mathbf{a}^n = \mathbf{F}^n / m\) is acceleration at step \(n\). **Velocity Verlet** (leapfrog) splits the update for better bookkeeping:

\[
\mathbf{v}^{n+\tfrac{1}{2}} = \mathbf{v}^n + \tfrac{1}{2}\mathbf{a}^n \Delta t, \qquad
\mathbf{r}^{n+1} = \mathbf{r}^n + \mathbf{v}^{n+\tfrac{1}{2}} \Delta t, \qquad
\mathbf{v}^{n+1} = \mathbf{v}^{n+\tfrac{1}{2}} + \tfrac{1}{2}\mathbf{a}^{n+1} \Delta t.
\]

Both are **symplectic** (for conservative \(V\)): they preserve a modified Hamiltonian to \(O(\Delta t^2)\), keeping energy drift bounded over long trajectories rather than accumulating secular error like generic Runge–Kutta on Hamiltonian systems.

### Timestep choice for copper

Timestep \(\Delta t\) must resolve the highest vibrational frequency \(\omega_{\max}\). For Cu with nearest-neighbor spring scale \(k \sim 50\) N/m and mass \(m \sim 10^{-25}\) kg, \(\omega_{\max} \sim 10^{13}\) rad/s, suggesting \(\Delta t \lesssim 1\)–\(2\) fs in metal units.

Too large \(\Delta t\): energy blows up, bonds over-extend. Too small: wasted compute with negligible accuracy gain. Adaptive timestep schemes appear in some codes but fixed \(\Delta t\) with stability margin remains standard in LAMMPS metal workflows.

### Constraint algorithms

Flexible molecules (or explicit hydrogen in biomolecules) contain stiff bonds requiring sub-femtosecond steps. **SHAKE** and **RATTLE** constrain bond lengths, allowing larger \(\Delta t\) on slow degrees of freedom. For monatomic copper EAM, constraints are usually unnecessary — every atom is free.

## Thermostats: sampling NVT

The **microcanonical (NVE)** ensemble fixes total energy — appropriate for checking integrator stability or short-time dynamics, not for comparing to a wire at constant laboratory temperature.

**NVT** (canonical) fixes temperature \(T\). Common algorithms:

| Thermostat | Idea | Caveat |
|------------|------|--------|
| **Berendsen** | Weak coupling to heat bath | Wrong fluctuation spectrum; not true canonical |
| **Nosé–Hoover** | Extended system with fictitious variable | Can become non-ergodic for small systems |
| **Langevin** | Friction + random force | Stochastic; damps dynamics, good for equilibration |
| **Bussi (CSVR)** | Stochastic velocity rescaling | Popular in modern MD; correct average \(T\) |

For copper property calculation (diffusion, thermal expansion), **Nosé–Hoover chains** or **Langevin** with careful friction choice are common. Equilibration often begins with Langevin (fast thermalization), then production with Nosé–Hoover.

Target temperature 300 K for "room-temperature copper wire" must be maintained during **mechanical loading** as well — deforming in NVE heats the sample adiabatically, mimicking high strain rates, not quasi-static lab tests.

## Barostats: sampling NPT

**NPT** (isothermal–isobaric) fixes \(T\) and pressure \(P\) — the ensemble closest to a wire segment under ambient conditions with free thermal expansion.

**Berendsen barostat** scales cell volume toward target pressure — fast but incorrect fluctuation statistics.

**Parrinello–Rahman** treats the cell matrix as a dynamical variable with kinetic energy, allowing **anisotropic** stress control — essential when simulating uniaxial tension of a copper nanowire with Poisson contraction.

Stress control couples to **elastic constants**: NPT equilibration at zero stress validates lattice parameter against the EAM/DFT value before production runs.

## Ensemble selection for copper wire problems

| Physical question | Ensemble | Notes |
|-------------------|----------|-------|
| Bulk modulus from small strain | NPT | Ramp pressure, measure volume |
| Thermal expansion | NPT | \(\alpha = \frac{1}{L}\frac{dL}{dT}\) |
| Uniaxial tension at fixed \(T\) | NPT with stress control | Fix \(\sigma_{zz}\), measure strain |
| Crack propagation (adiabatic limit) | NVE or NVT with caution | Heating at tip is physical at high rate |
| Diffusion coefficient | NVT | Einstein relation on MSD |
| Dislocation mobility | NVT + applied shear stress | Fit \(v\)–\(\tau\) for DDD |

Choosing the wrong ensemble misrepresents the experiment you compare against — the MD analogue of using Dirichlet data where the lab imposed traction.

## Extracting continuum quantities

### Stress: Irving–Kirkwood and Hardy

**Cauchy stress** in MD is not read from a constitutive law; it is computed from the atomistic configuration. The Irving–Kirkwood formula combines kinetic and virial contributions:

\[
\sigma_{\alpha\beta} = \frac{1}{V}\left[\sum_i m_i v_i^\alpha v_i^\beta + \sum_{i<j} r_{ij}^\alpha F_{ij}^\beta\right],
\]

(with appropriate conventions for pairwise potentials). **Hardy** formulations localize stress to atoms for crack-tip analysis.

Stress from MD feeds **continuum boundary conditions** in sequential multiscale schemes: MD at an interface provides traction for FEM in the surrounding bulk.

### Temperature

**Kinetic temperature** from equipartition:

\[
T = \frac{1}{3N k_B} \sum_i m_i \|\mathbf{v}_i\|^2
\]

(excluding constrained or frozen degrees of freedom). In NVT, \(T\) fluctuates around the target; block averages report meaningful values only after autocorrelation time of kinetic energy.

### Elastic constants

Two routes:

1. **Fluctuation formulas** (requires NVT or NPT with correct statistics): relate stress fluctuations to compliance tensor.
2. **Small-strain deformation**: apply \(\varepsilon_{ij}\), measure \(\sigma_{ij}\) in NPT — simpler, widely used for validating potentials against DFT elastic constants of copper (\(C_{11}, C_{12}, C_{44}\)).

### Dislocation mobility for DDD

Constrained MD applies shear stress \(\tau\) on a simulation cell containing a dislocation. Steady-state velocity \(v(\tau, T)\) is extracted and tabulated for **OpenDiS** mobility laws. This closes the loop between Part VIII and Part VII: atoms inform lines.

## LAMMPS workflow in practice

[LAMMPS](https://www.lammps.org/) organizes simulation into **styles**: units, atom_style, pair_style, fix, compute, dump. A reproducible copper wire fragment study might follow:

### 1. Build structure

Create fcc lattice, define simulation box, optionally carve cylindrical nanowire geometry with `region` and `delete_atoms`.

### 2. Specify potential

```
pair_style      eam/alloy
pair_coeff      * * Cu_mishin.eam.alloy Cu
```

Verify energy per atom near \(-3.5\) eV/atom (potential-dependent) and lattice parameter \(a \approx 3.615\) Å.

### 3. Minimize and equilibrate

```
minimize        1e-12 1e-12 1000 10000
velocity        all create 300.0 12345 dist gaussian
fix             1 all npt temp 300 300 0.1 iso 0 0 1
run             50000
unfix           1
```

### 4. Production deformation

```
fix             2 all npt temp 300 300 0.1 y 0 0 1 z 0 0 1
variable        srate equal 1.0e8
fix             3 all deform 1 erate ${srate} units box remap x
compute         stress all stress/atom NULL
run             100000
```

### 5. Post-process

Dump trajectories to OVITO for dislocation extraction; compute stress–strain from box dimensions and pressure tensor.

### 6. Chain upward

Export elastic constants, mobility curves, or fracture energies to DDD/FEM inputs.

GPU packages (`package gpu`, Kokkos) accelerate pair force evaluation — essential for million-atom fracture runs.

## Energy conservation as diagnostic

In NVE, total energy \(H\) should drift slowly (symplectic) rather than explode. Plot \(H(t)\) and temperature \(T(t)\) during method development:

- Sudden energy jump: neighbor list error, bad potential cutoff, or too large \(\Delta t\).
- Linear drift: subtle thermostat coupling left on during NVE test.
- Stable oscillation: normal for small systems; average over many vibrational periods.

Verification culture from Part IV–V applies here: **manufactured** checks (harmonic oscillator), conservation checks, and convergence in \(\Delta t\) before trusting production data.

## Rare events and the time-scale gap

Wire creep over years involves vacancy diffusion and dislocation climb at strain rates MD cannot reach directly. **Accelerated MD** (hyperdynamics, parallel replica, metadynamics) and **kinetic Monte Carlo** extrapolate from MD-derived barriers — topics beyond this chapter but essential for connecting atomistics to service life.

For crack nucleation, **transition path sampling** finds rare barrier-crossing trajectories. The copper wire epilogue will return to these coupling strategies; here we note MD supplies **barriers and mechanisms**, not always **timescales**.

## Reproducibility checklist

Before publishing MD results on copper (or any metal):

1. Cite potential source and version; report cutoff and neighbor skin.
2. Converge \(\Delta t\) and system size for the observable of interest.
3. Document ensemble, thermostat/barostat parameters, equilibration length.
4. Report energy drift in NVE sanity checks.
5. Compare lattice parameter, cohesive energy, and elastic constants to DFT/experiment.
6. Archive input decks and random seeds.

Unconverged MD is structured noise — the same warning we will repeat for DFT cutoff energy.

## Bridge

Verlet integrators and NVT/NPT ensembles make classical MD a controlled experiment on the potential energy surface — but that surface is usually **empirical**. The next chapter asks when **ab initio** forces replace EAM, how DFT data are compressed into potentials and mobility tables, and how atomistic simulations hand parameters upward before we descend to electrons in Part IX.

| What VIII.2 established | What VIII.3 supplies |
|-------------------------|----------------------|
| Symplectic Verlet; NVE as sanity check | When EAM is not enough: AIMD and QM/MM |
| NVT/NPT thermostats and barostats for Cu at 300–600 K | EAM-fit workflow from DFT bulk properties |
| Reproducibility checklist (cutoff, \(\Delta t\), drift) | Coarse-graining: export \(C_{ij}\), \(\gamma_{\text{sf}}\), mobility to Part VII |
| Time-scale gap (creep, rare events) | Handoff table linking Part VIII exports to Part IV/VII consumers |

Return to the [prologue](../../prologue/00-many-scales.md): **Act IV — Hardening** bent the load cell curve because dislocation lines moved on a potential surface whose parameters were fit at laboratory temperature — the NVT and NPT ensembles named in this chapter are how that temperature enters the simulation, not as a comment line in an input deck. **Act V — Notch** concentrates stress where continuum meshes regularize singularities; MD's representative volume at the notch root is the atomistic witness those regularized fields cannot supply alone.

**Act VI — Foundation** runs offline before any grip closes: DFT bulk energies, EAM fits, mobility tables. Part VII's dislocations move on surfaces MD integrates; Part IV's elastic step uses moduli MD or DFT averaged over a polycrystal. [VIII.3](03-ab-initio-and-coarse-graining.md) is the **export chapter** — the rung where atomistics stops being a standalone movie and becomes input for coarser models, while naming what only Part IX can re-derive from \(\rho(\mathbf{r})\).

| Prologue act | What VIII.2 makes computable | What VIII.3 exports upward |
|--------------|------------------------------|----------------------------|
| IV — Hardening | NVT shear at 300–600 K for drag and cross-slip statistics | Mobility \(M(\tau,T)\) tables for OpenDiS |
| V — Notch | Stable Verlet trajectories at the stress concentrator | Nucleation barriers and cohesive response |
| VI — Foundation | Reproducible LAMMPS decks with documented drift | \(C_{ij}\), \(\gamma_{\text{sf}}\), EAM parameters for FEM and DDD |

**Act VI — Foundation** in workflow order runs before **Act I — Mounting**: the NVT shear tests and bulk-modulus checks in this chapter are the audit trail behind every Young's modulus and mobility table the later acts spend. Reading order places Part IX after this chapter; both orders converge when export tables carry convergence logs, not folklore.

Reading order places Part IX after this chapter; workflow order runs DFT **before** the LAMMPS deck exists. Both are valid — the [two clocks note](00-opening.md#two-clocks-reading-order-vs-foundation-pedigree) at the Part VIII opening explains why EAM parameters may already be on disk when you arrive here linearly. [VIII.3](03-ab-initio-and-coarse-graining.md) names what only Part IX can re-derive from \(\rho(\mathbf{r})\); this chapter names what MD must sample correctly before any export table is trustworthy.

| Integrator/ensemble choice | What it certifies on the wire | What breaks if wrong |
|---------------------------|------------------------------|----------------------|
| Verlet (NVE) | Symplectic stability; phonon spectrum | Energy drift masks creep at wrong temperature |
| Nosé–Hoover (NVT) | 300 K laboratory comparison | Simulating 0 K while believing room temperature |
| Parrinello–Rahman (NPT) | Gauge-length tension at ambient pressure | Spurious stress from wrong box dynamics |

Turn the page when the EAM curve matches experiment in bulk but fails at the notch root — that is the signal to audit the potential against electronic structure in Part IX.
