# Ensembles, Integrators, and Practical Molecular Dynamics

MD is not merely integrating Newton's laws — it is **controlled sampling** of statistical mechanics. The integrator and thermostat determine what physical state the simulation represents. A copper wire held at room temperature in the lab corresponds to an **NVT** or **NPT** ensemble at 300 K and ambient pressure — not an isolated **NVE** cluster drifting with whatever energy the initial velocity draw happened to assign.

Getting the ensemble wrong is not a small error. It is simulating the wrong experiment.

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

### Worked example: equilibration length for a copper nanowire

How long must an NPT run run before stress–strain data from the Lab act below are trustworthy? The answer is not "50 ps because the input deck says so" — it is tied to **autocorrelation time** \(\tau\) of the observable you will average.

For a 50 nm fcc Cu segment (\(\sim 10^5\) atoms) at 300 K:

1. **Thermalize** with Langevin or Berendsen for 10–20 ps — fast relaxation of kinetic temperature toward 300 K.
2. **Equilibrate** with Nosé–Hoover NPT until the **pressure tensor** \(\langle P_{ij} \rangle\) and **box dimensions** fluctuate around stable means. For metals, 50–100 ps is often sufficient; for polymers or nanostructures with slow rearrangement, multiply by 10.
3. **Estimate \(\tau\)** for the stress component you will report (e.g. \(\sigma_{zz}\) during tension). Compute the autocorrelation function \(C(t) = \langle \sigma_{zz}(0)\sigma_{zz}(t)\rangle - \langle\sigma_{zz}\rangle^2\) and find the first zero crossing or exponential decay time. Block averages with block length \(\gg \tau\) are approximately independent.
4. **Production** length: at least \(10\tau\) per block, with \(\ge 5\) blocks for error bars on modulus.

| Observable | Typical \(\tau\) (Cu, 300 K, \(\sim 10^5\) atoms) | Minimum production |
|------------|--------------------------------------------------|--------------------|
| Kinetic temperature | 0.1–0.5 ps | 5 ps after thermostat settles |
| Hydrostatic pressure | 0.5–2 ps | 20 ps NPT equilibration |
| \(\sigma_{zz}\) under tension | 1–5 ps (depends on strain rate) | 50–100 ps ramp + blocks |
| Mean-square displacement (diffusion) | 10–100 ps | nanoseconds |

If you export Young's modulus from a 5 ps tension ramp without checking \(\tau\), you are reporting **noise dressed as mechanics** — the MD analogue of reporting FEM stress before mesh convergence. Part IV's refinement study and Part IX's k-mesh convergence ask the same question: *has the discretization (here, time sampling) converged for the quantity I need?*

### Elastic constants

Two routes:

1. **Fluctuation formulas** (requires NVT or NPT with correct statistics): relate stress fluctuations to compliance tensor.
2. **Small-strain deformation**: apply \(\varepsilon_{ij}\), measure \(\sigma_{ij}\) in NPT — simpler, widely used for validating potentials against DFT elastic constants of copper (\(C_{11}, C_{12}, C_{44}\)).

### Dislocation mobility for DDD

Constrained MD applies shear stress \(\tau\) on a simulation cell containing a dislocation. Steady-state velocity \(v(\tau, T)\) is extracted and tabulated for **OpenDiS** mobility laws. This closes the loop between Part VIII and Part VII: atoms inform lines.

## Einstein relation and vacancy diffusion on the wire

Room-temperature copper wire does not creep on laboratory time scales — but **electromigration** and **high-temperature annealing** make vacancy diffusion a first-class export from atomistics. The continuum picture is Fick's law \(J = -D \nabla c\); MD supplies \(D(T)\) from trajectories without fitting a phenomenological prefactor.

### Mean-square displacement

Track a tagged atom (or all atoms in a dilute vacancy supercell) in **NVT** at temperature \(T\). The **mean-square displacement** (MSD) is

\[
\text{MSD}(t) = \left\langle \|\mathbf{r}_i(t) - \mathbf{r}_i(0)\|^2 \right\rangle,
\]

where the average is over time origins and, for self-diffusion in a periodic bulk cell, over equivalent atoms. In three dimensions, Fickian diffusion gives

\[
\text{MSD}(t) = 6 D t \quad \text{(long-time limit)}.
\]

The **Einstein relation** extracts \(D\) from the slope:

\[
D = \lim_{t \to \infty} \frac{\text{MSD}(t)}{6t}.
\]

In practice, fit MSD versus \(t\) over a window where the slope is linear — after ballistic short-time motion (\(t < 1\) ps) and before sublinear caging at very long times in small cells.

| Stage | MSD behavior | Physical meaning |
|-------|--------------|------------------|
| \(t < 0.5\) ps | \(\sim t^2\) (ballistic) | Not diffusive — exclude from fit |
| 1–50 ps | \(\sim t\) (linear) | Diffusive regime; fit \(D\) here |
| \(t > 100\) ps (small cell) | sublinear | Periodic image correlation; enlarge cell |

### Worked example: Cu self-diffusion at 900 K

Annealing cold-drawn wire at \(900\,\text{K}\) activates vacancy hops MD can resolve. A minimal LAMMPS workflow on a 256-atom fcc supercell with one vacancy:

```lammps
# in.diffusion — Cu vacancy diffusion, NVT 900 K
units           metal
atom_style      atomic
read_data       cu_vac_256.data
pair_style      eam/alloy
pair_coeff      * * Cu.eam.alloy Cu
group           vac type 1
compute         msd all msd com yes
fix             1 all nvt temp 900 900 0.1
timestep        0.001
thermo          100
run             500000    # 500 ps
```

Post-process `msd.txt`: plot \(\text{MSD}(t)\) versus \(t\); linear regression on \(t \in [10, 200]\,\text{ps}\) yields \(D \approx 10^{-12}\)–\(10^{-11}\,\text{m}^2/\text{s}\) (order of magnitude — potential and \(T\) dependent). Compare to experimental Cu self-diffusion \(\sim 10^{-13}\,\text{m}^2/\text{s}\) at 900 K: EAM often overestimates \(D\) by factors of 2–10 unless vacancy formation and migration barriers were in the fit set.

**Scale-boundary handshake (MD → continuum creep models).**

| MD export | Continuum consumer | Pass criterion |
|-----------|-------------------|----------------|
| \(D(T)\) from MSD slope | Arrhenius fit \(D = D_0 e^{-Q/RT}\) in creep law | Activation energy \(Q\) within 20% of experiment |
| Vacancy hop rate | Kinetic Monte Carlo (Part VIII.3) | Same \(D\) at long times |
| MSD at 300 K (negligible) | "No creep on lab times" in Part VI | Slope \(\approx 0\) over accessible MD window |

**What breaks without the handshake.** Exporting a 5 ps MSD slope from ballistic motion inflates \(D\) by orders of magnitude — the atomistic analogue of reporting FEM stress before mesh convergence. Using NVE during a heating ramp (instead of NVT) changes the effective temperature and corrupts \(D(T)\) tables fed to mesoscale kinetics.

### Green–Kubo alternative for diffusion

The **velocity autocorrelation function** (VACF) integrates to \(D\) via

\[
D = \frac{1}{3N} \int_0^\infty \sum_i \langle \mathbf{v}_i(0) \cdot \mathbf{v}_i(t) \rangle \, dt.
\]

MSD and Green–Kubo must agree within statistical error when both are converged — cross-checking them is standard practice before archiving `D_cu_900K.txt` for the foundation folder.

## Phonon density of states from velocity autocorrelation

Thermal expansion, heat capacity, and thermal conductivity all depend on how atoms vibrate. DFT phonons (Part IX) compute harmonic modes on a grid in **k**-space; MD can estimate the **phonon density of states** (DOS) from equilibrium **NVT** trajectories without a separate phonon code — a downward-friendly audit when DFT `ph.x` is unavailable.

### VACF → spectral density

In NVT at 300 K, record atomic velocities every \(\Delta t_{\text{sample}}\). The VACF is

\[
C_v(t) = \frac{1}{N} \sum_i \langle \mathbf{v}_i(0) \cdot \mathbf{v}_i(t) \rangle.
\]

Its Fourier transform (discrete cosine transform on a long trajectory) gives a spectral density \(g(\omega)\) proportional to the phonon DOS up to normalization:

\[
g(\omega) \propto \int_0^\infty C_v(t) \cos(\omega t) \, dt.
\]

Peaks in \(g(\omega)\) at \(\omega \sim 10^{13}\,\text{rad/s}\) match the highest frequencies that set the Verlet timestep limit from [VIII.1](01-potentials-phase-space.md).

| Peak location | Mode type | Link to Part I / IX |
|---------------|-----------|---------------------|
| Low \(\omega\) | Acoustic branches | Long-wavelength sound speed; bulk modulus check |
| Mid \(\omega\) | Optical-like | Timestep stability; heat capacity |
| High \(\omega\) | Short-wavelength | \(\omega_{\max}\) sets \(\Delta t \lesssim 2\pi/(10\,\omega_{\max})\) |

### Scale-boundary handshake (MD phonons → Part IX → Part VI \(\alpha\))

Part IX.3 computes quasi-harmonic thermal expansion \(\alpha(T)\) from DFT phonon free energy. MD phonon DOS from VACF is a **cross-check**, not a replacement:

1. Run 100 ps NVT on 256-atom bulk Cu at 300 K; dump velocities every 10 fs.
2. Compute VACF; FFT to \(g(\omega)\).
3. Compare peak positions to DFT `ph.x` dispersion along high-symmetry lines — shifts \(> 5\%\) flag a bad EAM fit before exporting \(\alpha\) to Part VI thermoelasticity.
4. Archive `phonon_dos_md.dat` beside `cu.phonon/` in the foundation folder.

**What breaks without the handshake.** A potential that reproduces bulk modulus but shifts optical peaks by 15% will predict wrong heat capacity and, through quasi-harmonic coupling, wrong thermal expansion — the same \(\alpha\) that enters Part I.3's thermal eigenstrain and Part VI's coupled thermomechanical block system. Phonon DOS is the vibration spectrum the wire's eigenmodes from [I.3](../part01-linear-algebra/03-eigenvalues.md) approach as \(N \to \infty\); MD and DFT are two ways to name that spectrum at atomic scale.

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

### Scale-boundary handshake: phonons from DFT to MD validation

Part IX will compute phonon dispersions from density-functional perturbation theory (DFPT) or finite differences of forces. Part VIII can **validate** the EAM potential before any notch or dislocation run by comparing those frequencies to MD spectra — the atomistic analogue of mesh convergence in Part IV.

**Downward export (DFT).** Relax a 2×2×2 fcc Cu supercell in Quantum ESPRESSO; run `ph.x` (or equivalent) on the converged geometry. Archive the \(\Gamma\)-point optical and acoustic branches at low \(|q|\):

| Mode (illustrative, PBE Cu) | DFT frequency (THz) | Physical meaning |
|-----------------------------|---------------------|------------------|
| TA (transverse acoustic) | ~0 at \(\Gamma\) | Goldstone; slope sets sound speed |
| LA (longitudinal acoustic) | ~0 at \(\Gamma\) | Bulk modulus check via \(c = \omega/k\) |
| TO (transverse optical) | ~7–8 | Zone-boundary character at finite \(q\) |
| LO (longitudinal optical) | ~8–9 | Optical branch; EAM often softens here first |

**Upward test (MD).** Minimize the same supercell in LAMMPS with the EAM file intended for production runs. Run a short **NVE** trajectory (\(\Delta t = 1\,\text{fs}\), 20 ps) and compute the **velocity autocorrelation function** (VACF) or take the Fourier transform of the mass-weighted velocity spectrum. Peaks in the VACF spectrum should align with DFT phonon frequencies at the same \(q\)-points within 5–10% for a well-fit EAM; larger shifts at optical branches signal the potential is wrong for core structures even if bulk modulus matches.

**Handshake checklist** (archive beside `README_DFT.md` and the LAMMPS input deck):

| Check | DFT artifact | MD artifact | Pass criterion |
|-------|--------------|-------------|----------------|
| Equilibrium \(a_0\) | `vc-relax.out` | `minimize` log | \(\|a_{\text{DFT}} - a_{\text{EAM}}\| < 0.02\,\text{Å}\) |
| Cohesive energy | SCF total energy per atom | `pe/atom` after minimize | Same sign, within 10% |
| LA sound speed along [100] | Phonon slope from DFPT | Long-wavelength VACF peak | Within 10% |
| Optical branch at zone boundary | `ph.x` output | VACF peak assignment | Same order; note EAM softness |

**What breaks without the handshake.** A potential tuned only to bulk modulus and lattice constant can reproduce NPT elastic constants ([Lab act below](#lab-act-npt-tension-on-a-copper-nanowire-segment)) yet fail at dislocation cores — where optical-mode character matters for stacking-fault energy. Part VII's mobility tables inherit that error silently. The phonon handshake is cheap (256-atom supercell, minutes of MD) compared to a million-atom notch run; it is the **scale boundary** where electronic-structure exports first meet classical trajectories.

When DFT phonons and MD spectra disagree, fix the potential before exporting \(b = a_0/\sqrt{2}\) to OpenDiS. Part IX's [phonon workflow](../part09-dft/03-dft-workflows.md) supplies the reference; this section supplies the acceptance test on the MD side.

## Lab act: NPT tension on a copper nanowire segment

This Lab act runs the nanowire tension test described in the opening scene — the atomistic counterpart to Part IV's elastic step and Part VII's mobility calibration.

**Step 1 — build and equilibrate.** Create an fcc Cu lattice (\(a_0 \approx 3.615\,\text{Å}\)), carve a cylindrical segment (\(\sim 10\,\text{nm}\) diameter, \(\sim 50\,\text{nm}\) length), assign Mishin EAM (`pair_style eam/alloy`), minimize, then equilibrate in **NPT** at 300 K and 0 GPa for at least 50 ps (\(\Delta t = 1\,\text{fs}\)):

```
units           metal
atom_style      atomic
pair_style      eam/alloy
pair_coeff      * * Cu_mishin.eam.alloy Cu
minimize        1e-12 1e-12 1000 10000
velocity        all create 300.0 12345 dist gaussian
fix             1 all npt temp 300 300 0.1 iso 0 0 1
run             50000
```

Verify: potential energy per atom stable; pressure tensor relaxes to \(\sim 0\); lattice parameter within 1% of DFT/experiment.

**Step 2 — uniaxial tension at fixed temperature.** Switch to **NPT with fixed lateral stress** (or `fix deform` with NVT thermostat on lateral faces). Ramp engineering strain at \(\dot\varepsilon \sim 10^8\,\text{s}^{-1}\) (MD time scales — not the lab frame's \(10^{-3}\,\text{s}^{-1}\), but comparable to high-rate impact):

```
unfix           1
fix             2 all npt temp 300 300 0.1 y 0 0 1 z 0 0 1
fix             3 all deform 1 z erate 1.0e-4 units box
compute         s all stress/atom NULL
run             100000
```

**Step 3 — read stress–strain and compare scales.** Extract engineering stress from the pressure tensor; compare Young's modulus to Part VI (\(E \approx 110\)–\(130\,\text{GPa}\) polycrystal) and Part IX DFT \(C_{11}\). Yield and fracture stress at this strain rate explain why the engineering wire's strength differs from bulk elasticity — dislocation nucleation at the surface, not a fitted yield surface.

**Step 4 — export upward.** Archive: (i) \(E\), \(\nu\) from small-strain NPT; (ii) stress at first plastic event; (iii) dislocation density from OVITO DXA if available. These feed Part VII mobility tables and Part IV constitutive sanity checks. Document potential version, cutoff, \(\Delta t\), and random seed — the reproducibility checklist below is not optional.

| Check | Pass criterion | Failure mode |
|-------|----------------|--------------|
| NVE drift test | \(|H(t)-H(0)|/H(0) < 10^{-4}\) over 10 ps | \(\Delta t\) too large or bad neighbor skin |
| Temperature | \(\langle T \rangle = 300 \pm 10\,\text{K}\) in production | Wrong ensemble (NVE during loading) |
| Modulus | Within 10% of DFT/experiment | Bad EAM or unconverged equilibration |

When bulk modulus matches but yield stress is half the experimental wire value, suspect **surface nucleation and strain rate**, not the integrator — the same scale-separation warning Part VII repeats for DDD.

## Reproducibility checklist

Before publishing MD results on copper (or any metal):

1. Cite potential source and version; report cutoff and neighbor skin.
2. Converge \(\Delta t\) and system size for the observable of interest.
3. Document ensemble, thermostat/barostat parameters, equilibration length.
4. Report energy drift in NVE sanity checks.
5. Compare lattice parameter, cohesive energy, and elastic constants to DFT/experiment.
6. Archive input decks and random seeds.

Unconverged MD is structured noise — the same warning we will repeat for DFT cutoff energy.

## Concept map checkpoint (ensembles and integrators)

This chapter is where the copper wire's laboratory temperature enters simulation. Before coarse-graining exports parameters upward, summarize what MD integration established:

| Question | Part VIII answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Phase-space trajectory \(\{\mathbf{r}_i(t), \mathbf{p}_i(t)\}\); state vector in \(\mathbb{R}^{6N}\) |
| What **structure**? | Symplectic Verlet; thermostats (NVT) and barostats (NPT) |
| What **theorem**? | NVE energy drift as timestep audit; ergodic sampling in equilibrium ensembles |
| What **breaks**? | \(\Delta t\) too large; wrong ensemble during loading; strain-rate gap vs lab frame |

The NVE drift and NPT modulus checks in the Lab act mirror Part IV's mesh refinement and Part IX's cutoff convergence — do not export \(E\), \(\nu\), or yield stress until the integrator and ensemble are audited. Part I's pattern returns: state plus update rule, now at \(10^5\)–\(10^9\) atoms.

## Bridge

Verlet integrators and NVT/NPT ensembles make classical MD a controlled experiment on the potential energy surface — but that surface is usually **empirical**. The next chapter asks when **ab initio** forces replace EAM, how DFT data are compressed into potentials and mobility tables, and how atomistic simulations hand parameters upward before we descend to electrons in Part IX.

| What VIII.2 established | What VIII.3 supplies |
|-------------------------|----------------------|
| Symplectic Verlet; NVE as sanity check | When EAM is not enough: AIMD and QM/MM |
| NVT/NPT thermostats and barostats for Cu at 300–600 K | EAM-fit workflow from DFT bulk properties |
| Reproducibility checklist (cutoff, \(\Delta t\), drift) | Coarse-graining: export \(C_{ij}\), \(\gamma_{\text{sf}}\), mobility to Part VII |
| Time-scale gap (creep, rare events) | Handoff table linking Part VIII exports to Part IV/VII consumers |

Return to the [prologue](../../prologue/00-many-scales.md): the wire's strength at the engineering scale still depends on a potential someone fit from quantum data. Part VII's dislocations move on surfaces MD integrates; Part IV's elastic step uses moduli MD or DFT averaged over a polycrystal. [VIII.3](03-ab-initio-and-coarse-graining.md) is the **export chapter** — the rung where atomistics stops being a standalone movie and becomes input for coarser models, while naming what only Part IX can re-derive from \(\rho(\mathbf{r})\).

Turn the page when the EAM curve matches experiment in bulk but fails at the notch root — that is the signal to audit the potential against electronic structure.
