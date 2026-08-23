# Dislocation Dynamics and Strain Hardening

When metal yields, dislocations multiply and tangle. **Dislocation dynamics (DDD)** tracks their motion and interactions — the mesoscale engine of strain hardening. Pull a copper wire beyond its elastic limit and the stress–strain curve bends upward not because the lattice stiffens, but because an evolving **forest** of dislocation lines impedes further slip. DDD is how we simulate that forest without resolving every atom.

## Scene: the forest grows

Resume the tensile test where Part VI left it — load increasing, stress beyond yield. Inside the copper crystal, dislocation lines **glide** on {111} planes, **multiply** at Frank–Read sources, and **tangle** into a forest whose density rises with plastic strain. The load cell registers hardening: more stress needed for the next increment of stretch. No phenomenological law was typed in by hand; the curve bends because moving lines must push through a thickening forest.

A DDD simulation represents that forest as a network of segments, each feeling Peach–Köhler forces from external load and from every other segment. Timestep by timestep, the network evolves; the accumulated obstacle strength passes upward as a **hardening law** for crystal plasticity and, eventually, for continuum FEM. This scene is why Part VII exists: the wire's cold-drawn strength and its post-yield curve are **histories written in line defects**, not numbers we may choose arbitrarily at the continuum scale.

## Closing the arc from Part VII.1 {#opening-hinge-vii1-to-vii2}

If you have read linearly since the prologue, [VII.1](01-defect-taxonomy.md) named the defect inventory cold drawing wrote into the wire — point, line, and surface defects with Burgers vectors and stacking faults. This chapter is where that inventory becomes **moving geometry**: segments under Peach–Köhler forces, not labels on an input deck.

The [preface descent continuity hinges](../preface.md#descent-continuity-hinges) name [VI.4 → VII](../part06-continuum/04-nonlinear-plasticity-preview.md#bridge-to-part-vii) as the **phenomenology → pedigree** turn; read this opening hinge when the taxonomy table feels like metallurgy notes rather than simulation input — the next sections integrate the lines VII.1 catalogued.

| Part VII.1 (taxonomy on the wire) | Part VII.2 (DDD on the wire) |
|-----------------------------------|------------------------------|
| Point defects (vacancies, interstitials) | Climb and recovery kinetics feeding \(\rho(\gamma)\) |
| Line defects (edge, screw, mixed) | Peach–Köhler motion, Frank–Read multiplication |
| Surface defects (GBs, stacking faults) | Slip barriers; partial separation from \(\gamma_{\text{sf}}\) |
| Scalar \(\rho\) as internal variable | Taylor \(\tau \propto \sqrt{\rho}\) from link statistics |
| Part VI \(H\), \(\sigma_{y0}\) borrowed without derivation | Mesoscale origin of hardening from forest density |
| [VII.1 Bridge](01-defect-taxonomy.md#bridge) previews line motion | OpenDiS export yaml for one crystal orientation |

Turn back to the mounted wire when \(\rho\) is still a fitted constant on a crystal plasticity deck — that is the signal dislocation dynamics is the next move, not another Voce fit.

## From elasticity to line defects

In Part VI, equilibrium satisfied a virtual work equation with smooth displacement fields. Dislocations introduce **topological** content: the displacement field is multi-valued, and the Burgers vector \(\mathbf{b}\) quantifies the jump. DDD replaces the singular continuum field with a **discrete network** of line segments, each carrying \(\mathbf{b}\) and a line direction \(\boldsymbol{\xi}\).

The long-range elastic stress from a segment is computed via **isotropic or anisotropic elasticity** (often precomputed Green's functions). Short-range **core** interactions — when segments pass within ~1–5 nm — require empirical rules or tables from molecular dynamics. The mesoscale model lives in the gap: elastic everywhere else, phenomenological at the core.

### Partial dislocations and the GSF handshake (Part IX → VII)

In fcc copper, a perfect dislocation with Burgers vector \(\mathbf{b} = a_0/2\langle 110\rangle\) is energetically unfavorable as a single line on {111}. It **dissociates** into two Shockley partials:

\[
\mathbf{b} = \mathbf{b}_1 + \mathbf{b}_2, \qquad |\mathbf{b}_p| = \frac{a_0}{\sqrt{6}} \approx 0.147\,\text{nm},
\]

separated by a **stacking-fault ribbon** whose energy per unit area \(\gamma_{\text{sf}}\) is exactly the quantity [Part IX.3](../part09-dft/03-dft-workflows.md) computes from a faulted DFT supercell — not a literature constant pasted into OpenDiS without pedigree.

Isotropic elasticity gives an equilibrium separation (order of magnitude)

\[
d \;\sim\; \frac{2-\nu}{1-\nu}\,\frac{\mu\,|\mathbf{b}_p|}{4\pi\,\gamma_{\text{sf}}},
\]

where \(\mu\) is shear modulus and \(\nu\) is Poisson's ratio. For copper at room temperature:

| Input | Source | Typical value |
|-------|--------|---------------|
| \(\mu\) | Voigt average of Part IX \(C_{ij}\) | \(\sim 48\,\text{GPa}\) |
| \(\gamma_{\text{sf}}\) | DFT stable fault (IX.3 GSF workflow) | \(\sim 40\)–\(50\,\text{mJ/m}^2\) (experiment \(\sim 45\)) |
| \(|\mathbf{b}_p|\) | Lattice constant \(a_0 \approx 3.61\,\text{Å}\) | \(0.147\,\text{nm}\) |
| \(d\) | Formula above | \(\sim 5\)–\(8\,\text{nm}\) |

The ribbon width sets three DDD parameters that mobility tables alone cannot supply:

| GSF export | DDD consumer | Wire-scale consequence |
|------------|--------------|------------------------|
| \(\gamma_{\text{sf}}\) at stable fault | Partial separation \(d\) | Core cutoff radius in segment rules |
| \(\gamma_{\text{USF}}\) at unstable fault | Cross-slip barrier scale | Recovery during annealing (Act IV) |
| \(\mathrm{d}^2\gamma/\mathrm{d}u^2\) at minimum | Peierls stress estimate | Initial yield in cold-drawn wire |

**Sensitivity check.** Because \(d \propto 1/\gamma_{\text{sf}}\), a DFT functional that overestimates \(\gamma_{\text{sf}}\) by 10% **underestimates** separation by 10% — segments interact as if partials were closer, cross-slip activates earlier, and the hardening curve from OpenDiS shifts even when mobility tables are unchanged. This is the mesoscale analogue of the epilogue's Handshake 1 sensitivity: elastic constants matter in the linear regime, but **\(\gamma_{\text{sf}}\) pedigree** matters the moment Act IV's load cell bends.

If your `cu.gsf/` folder from Part IX converges but OpenDiS still cites "literature 45 mJ/m²" without a path, the downward derivation stopped one rung above where it should have — the same audit the [IX.3 GSF bridge table](../part09-dft/03-dft-workflows.md#bridge-table-dft-gsf--part-vii-ddd) flags for Act VI.

## Peach–Köhler forces and mobility

Each dislocation segment experiences a **Peach–Köhler** force per unit length:

\[
\mathbf{f} = (\boldsymbol{\sigma} \cdot \mathbf{b}) \times \boldsymbol{\xi},
\]

where \(\boldsymbol{\sigma}\) is the local stress tensor (external load plus stress from all other segments). The segment velocity \(\mathbf{v}\) follows a **mobility law**:

\[
\mathbf{v} = M(\boldsymbol{\sigma}, \mathbf{b}, \boldsymbol{\xi}, T)\, \mathbf{f},
\]

where \(M\) may be anisotropic and thermally activated. In fcc crystals, screw dislocations on {111} planes glide under resolved shear stress; **cross-slip** onto other {111} planes enables recovery and affects hardening at elevated temperature.

Mobility parameters for copper are fit to MD simulations or experiments. A DDD simulation is only as credible as its mobility table — another instance of the ladder: fine scale informs coarse scale.

### NEB/KMC cross-links: climb, recovery, and the time-scale gap (Part VIII → VII)

Glide-dominated DDD timesteps advance microseconds of physical time — long enough for forest hardening in Act IV, but not for **dislocation climb** during annealing or **void growth** during electromigration. Those processes require vacancy diffusion at rates MD cannot reach directly at room temperature. Part VIII.2 and VIII.3 supply the barriers and rate tables; Part VII consumes them as **kinetic boundary conditions** on the DDD clock.

| Process | DDD limitation | Part VIII source | Part VII consumer |
|---------|----------------|------------------|-------------------|
| Screw cross-slip at 400–500 K | Rare event; zero counts in short runs | [VIII.3 parallel tempering Lab act](../../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-parallel-tempering-for-screw-cross-slip-at-joule-heated-temperature-act-ii--iv-bridge) | Recovery rate in hardening law |
| Vacancy-assisted climb | Requires point-defect flux to jogs | [VIII.2 NEB vacancy hop](../../part08-md/02-ensembles-integrators.md#neb-workflow-vacancy-hop-in-copper) → Arrhenius \(D(T)\) | Climb velocity \(v_c \propto D(T)\) on edge segments |
| Grain-boundary void nucleation | No atomistic resolution in DDD | [VIII.2 KMC grain boundary](../../part08-md/02-ensembles-integrators.md#kmc-workflow-grain-boundary-vacancy-exchange) | Reduced cross-section → stress concentration handoff to Part IV |
| Stacking-fault energy at elevated \(T\) | Static \(\gamma_{\text{sf}}\) at 0 K | [VIII.3 metadynamics GSF Lab act](../../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-gsf-free-energy-surface-via-well-tempered-metadynamics-act-vi-scout--foundation) | Temperature-dependent partial separation |

**Cross-slip barrier from GSF surface.** The unstable stacking fault energy \(\gamma_{\text{USF}}\) from Part IX.3 (or the metadynamics scout in Part VIII.3) sets the activation scale for screw cross-slip:

\[
\tau_{\text{cross-slip}} \;\sim\; \frac{2\gamma_{\text{USF}}}{b_p},
\]

where \(b_p = a_0/\sqrt{6}\) is the Shockley partial magnitude. When \(\tau_{\text{resolved}} > \tau_{\text{cross-slip}}\), screw segments leave their glide plane — forest density drops, and the hardening curve **recovers** during annealing (Act II heating). OpenDiS mobility tables that omit cross-slip rules at elevated \(T\) will over-predict hardening after the wire is heated.

**Climb rate from NEB barriers.** Vacancy migration barrier \(\Delta E_m\) from [VIII.2 NEB Lab act](../../part08-md/02-ensembles-integrators.md#lab-act-neb-barrier-for-cu-vacancy-migration-act-ii-anneal-preview) gives diffusivity:

\[
D(T) = a^2 \nu_0 \exp(-\Delta E_m / k_B T),
\]

and climb velocity on an edge dislocation with jog spacing \(h\):

\[
v_c \;\approx\; \frac{D(T)\, c_v^{\text{eq}}}{h},
\]

where \(c_v^{\text{eq}}\) is equilibrium vacancy concentration (from Part IX formation energy \(E_f^v\)). At 300 K, \(D \sim 10^{-30}\,\text{m}^2/\text{s}\) — DDD cannot resolve this; but at 900 K anneal, \(D\) rises enough that climb competes with glide on the same Act IV timescale. Export `cu_vac_migration_rates.yaml` from VIII.2 beside the mobility table so OpenDiS climb rules inherit the same pedigree.

**KMC void growth → continuum damage.** When electromigration drives vacancy flux to grain boundaries, [VIII.2 KMC](../../part08-md/02-ensembles-integrators.md#kmc-workflow-grain-boundary-vacancy-exchange) reaches milliseconds where DDD stops at microseconds. The time-averaged void area fraction \(\phi(t)\) feeds Part VI damage mechanics as an effective diffusivity — not a number chosen by hand. The [VII.3 handoff Lab act](03-polycrystal-and-fem-handoff.md#lab-act-archive-the-opendis--damask--fem-handoff-act-ivv) expects `kmc_void_growth.dat` in the same folder as DDD outputs when the wire's service-life story requires void nucleation.

**What breaks without these cross-links.** Running OpenDiS with 300 K mobility at 400 K wire temperature (Joule heating from Act II) misses thermally activated cross-slip. Using literature \(D(T)\) without the VIII.2 NEB pedigree shifts climb rates by orders of magnitude. Pasting \(\gamma_{\text{sf}}\) from IX.3 while ignoring \(\gamma_{\text{USF}}\) leaves recovery kinetics unconstrained — the hardening curve after annealing has no barrier scale. Each failure is the mesoscale analogue of exporting FEM stress before mesh convergence: the code runs, but the story is wrong.

### Lab act: calibrate screw mobility from MD shear (Act IV — mobility prelude)

**Act IV** bends the load cell curve because lines move under Peach–Köhler forces. Before OpenDiS can reproduce that bend, the mobility law \(M(\tau, T)\) must be calibrated — not copied from a literature table without pedigree. This Lab act extracts \(M\) from a Part VIII MD shear test on a dislocation-containing supercell, then exports a yaml table OpenDiS consumes.

**Step 1 — build the MD cell.** Use the same EAM potential and \(a_0\) from [Part VIII.1 Lab act](../../part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude). Insert a straight screw dislocation on one {111}\(\langle 110\rangle\) system (Volterra construction or `dislocate` in LAMMPS). Cylindrical geometry: radius \(\geq 10\,b\), glide length \(\geq 20\,b\), flexible outer shell or fixed bottom layers to suppress spurious drift.

**Step 2 — NVT shear protocol at 300 K.** Equilibrate in NVT, then apply constant resolved shear stress \(\tau\) via `fix addforce` on a top layer (or `fix deform` with stress control). Log dislocation position \(x(t)\) and average glide velocity \(v = \dot{x}\) over 50–200 ps once transients decay.

| Applied \(\tau\) (MPa) | Expected regime (Cu screw, 300 K) | Observable |
|------------------------|-----------------------------------|------------|
| 5–15 | Thermally activated, low stress | \(v \approx 0\) or sporadic bursts |
| 20–40 | Glide-dominated | Steady \(v \propto \tau\) (mobility linear) |
| 60+ | High-stress; watch cross-slip | \(v\) saturates or oscillates |

**Step 3 — fit mobility.** In the linear regime, \(v = M\,\tau\,b\) (units: m/(Pa·s) when \(b\) is Burgers magnitude). Fit \(M\) from the slope of \(v\) vs \(\tau\). Repeat at \(T = 400\,\text{K}\) and \(500\,\text{K}\) to capture thermal activation:

\[
M(T) = M_0 \exp\!\left(-\frac{Q}{k_B T}\right)
\]

Archive fitted \(M_0\), \(Q\), and the raw \((\tau, v)\) pairs in `mobility_cu_screw_300K.yaml`.

**Step 4 — export to OpenDiS.** Map the yaml into OpenDiS material input:

```yaml
# mobility_cu_screw_300K.yaml (illustrative)
material: Cu
temperature_K: 300
potential: Mishin_EAM_2001
burgers_m: 2.556e-10
mobility_law: linear
M_m_per_Pa_s: 4.5e-11   # fit from Step 3
activation_eV: 0.15     # optional Arrhenius tail
source_md: shear_supercell_256atoms.lammps
```

**Step 5 — cross-check against Part VII hardening Lab act.** Run OpenDiS with the calibrated table (not literature defaults) on the Frank–Read source setup from [below](#lab-act-read-the-hardening-bend-from-forest-density-act-iv). Compare \(\tau(\gamma)\) at fixed \(\gamma\): if mobility is wrong by a factor of two, the hardening slope shifts even when \(\gamma_{\text{sf}}\) from Part IX is correct — the same sensitivity the [GSF handshake](#partial-dislocations-and-the-gsf-handshake-part-ix--vii) flags for partial separation.

| Quantity | Literature paste | MD-calibrated (this Lab act) |
|----------|------------------|------------------------------|
| \(M(300\,\text{K})\) | Tabulated in OpenDiS examples | Fit from shear supercell |
| \(\tau(\gamma)\) at \(\gamma = 0.01\) | May match by accident | Reproducible with archived yaml |
| Hardening slope | Wrong if \(M\) wrong | Traces to Part VIII potential |

**What breaks without calibration.** OpenDiS examples ship default copper mobility from papers whose EAM potential, temperature, and strain rate differ from yours. A DDD run that reproduces forest density but not flow stress is usually a **mobility pedigree error**, not a segment-mesh bug — the mesoscale mirror of Part VIII's phonon handshake: two discretizations of the same copper lattice must agree on the same observable before coarser models inherit the numbers.

### Worked example: OpenDiS single-slip run with MD mobility (Act IV)

This walkthrough ties Steps 1–5 above to a **minimal OpenDiS-style deck** — not a vendor manual, but the same audit discipline as the LAMMPS checklist in Part VIII. The goal is a \(\tau\)–\(\gamma\) curve whose slope traces to `mobility_cu_screw_300K.yaml`, not to literature defaults.

**Setup summary.**

| Input | Value | Provenance |
|-------|-------|------------|
| Crystal | fcc Cu, \([001]\) loading, one active \(\{111\}\langle 110\rangle\) system | Single-slip RVE |
| Box | \(2\,\mu\text{m}\) cube, periodic | OpenDiS / ParaDiS style |
| \(C_{ij}\) | Voigt from Part IX DFT or handbook | Same table as [VII.1 handshake](../part07-defects/00-opening.md#handshake-0-fem-stress-at-an-rve-centroid) |
| Initial network | Two Frank–Read sources, segment length \(L_0 = 500\,b\) | Seeds forest without random loops |
| Mobility | `mobility_cu_screw_300K.yaml` from MD shear Lab act | **Not** built-in Cu table |
| Load | \(\dot\gamma = 10^{-2}\,\text{s}^{-1}\), \(T = 300\,\text{K}\) | Matches prologue tensile frame order-of-magnitude |
| Stop | \(\gamma = 0.02\) or \(\rho > 10^{14}\,\text{m}^{-2}\) | Export before saturation noise |

**Control file skeleton (illustrative).**

```yaml
# opendis_cu_single_slip.yaml
simulation:
  crystal: fcc
  lattice_a: 3.615e-10
  load_type: constant_strain_rate
  strain_rate: 1.0e-2
  temperature_K: 300
  max_strain: 0.02

material:
  elastic: file://Cij_cu_dft.yaml
  burgers_m: 2.556e-10
  mobility: file://mobility_cu_screw_300K.yaml   # MD-calibrated

network:
  type: frank_read_sources
  n_sources: 2
  segment_length_b: 500
  slip_system: [111, 110]

output:
  every_strain: 0.001
  fields: [rho, tau, link_length_histogram]
  archive: ddd_cu_fr300K/
```

**Reading the log (expected columns).**

| Strain \(\gamma\) | \(\rho\) [m\(^{-2}\)] | \(\tau\) [MPa] | \(\bar\ell\) [nm] | Interpretation |
|-------------------|------------------------|----------------|-------------------|----------------|
| 0.000 | \(5\times 10^{11}\) | 12 | 450 | Elastic + source bow-out |
| 0.005 | \(2\times 10^{13}\) | 28 | 180 | Forest building; \(\tau \propto \sqrt{\rho}\) onset |
| 0.010 | \(8\times 10^{13}\) | 41 | 95 | Taylor line steepens |
| 0.015 | \(1.5\times 10^{14}\) | 52 | 70 | Link shortening on active system |
| 0.020 | \(2.2\times 10^{14}\) | 58 | 58 | Export point for VII.3 |

Plot \(\tau\) versus \(\sqrt{\rho}\): a straight segment from \(\gamma \approx 0.005\)–\(0.015\) confirms Taylor hardening with MD mobility. **Sensitivity:** rerun with literature mobility at the same \(\rho\); if \(\tau\) at \(\gamma = 0.01\) shifts by \(> 15\%\), the hardening mismatch in Act IV is a mobility pedigree error — fix Part VIII shear before refining segment mesh.

**Export bundle for VII.3.**

```text
ddd_cu_fr300K/
  opendis_cu_single_slip.yaml
  mobility_cu_screw_300K.yaml
  Cij_cu_dft.yaml
  tau_vs_gamma.csv
  rho_vs_gamma.csv
  link_hist_gamma0.020.dat
```

Fit \(\tau = \tau_0 + \alpha \mu b \sqrt{\rho}\) on the linear segment; store \(\alpha\) beside the yaml. [VII.3](03-polycrystal-and-fem-handoff.md) imports \(\tau(\gamma)\) into DAMASK — this directory is the **mesoscale evidence** that \(H\) in Part VI is not arbitrary.

## Discrete dislocation dynamics algorithms

Each dislocation is a curve (or network of segments) in an elastic medium. Time integration proceeds:

1. Compute stress field at each segment from superposition (direct summation, **fast multipole**, or precomputed influence matrices).
2. Evaluate Peach–Köhler forces.
3. Update segment positions via mobility laws.
4. Handle **topology changes**: annihilation when opposite segments meet, junction formation when segments intersect, Frank–Read source multiplication when pinned segments bow out.

Open-source frameworks such as [OpenDiS](https://github.com/OpenDiS/OpenDiS) and ParaDiS implement these algorithms at scale — enabling simulations of work hardening in single crystals and polycrystals. Typical simulations track \(10^3\)–\(10^6\) segments over strain intervals that would take years in full MD, at computational cost orders of magnitude lower than atomistic resolution of the same volume.

For the copper wire, a representative **single-crystal slip** simulation might impose shear at constant strain rate and record how dislocation density and flow stress co-evolve — output that feeds crystal plasticity constitutive laws used in polycrystal FEM.

## Taylor hardening and dislocation density

Classical models relate flow stress to total dislocation density \(\rho\):

\[
\tau = \alpha \mu b \sqrt{\rho},
\]

known as **Taylor hardening**. Here \(\mu\) is shear modulus, \(b\) is Burgers vector magnitude, and \(\alpha \approx 0.3\) is an empirical constant. The square-root scaling arises from treating other dislocations as random obstacles whose stress fields superpose incoherently.

During deformation, **storage** (multiplication at sources, junction formation) competes with **recovery** (annihilation, cross-slip, dynamic recovery at high temperature). The net evolution

\[
\frac{d\rho}{d\gamma} = k_1 \sqrt{\rho} - k_2 \rho
\]

(with strain \(\gamma\)) produces the familiar hardening then saturation shape. Parameters \(k_1, k_2\) depend on temperature, strain rate, and crystal structure — DDD extracts them from first-principles mesoscale physics rather than curve fitting alone.

For copper at room temperature, initial yield corresponds to \(\rho \sim 10^{10}\) m\(^{-2}\) (as-received); cold work can push \(\rho\) toward \(10^{15}\) m\(^{-2}\) before saturation effects dominate.

## Link statistics: beyond scalar density

Taylor's \(\sqrt{\rho}\) law uses a **scalar** measure of defect content. Large-scale DDD campaigns show that **topology** — how line length is distributed across the network — carries information the square root alone does not.

A **link** is a continuous segment between two nodes (junctions or endpoints). Its length distribution \(P(\ell)\), mean link length \(\bar{\ell}\), and network connectivity affect hardening in ways \(\rho\) alone cannot capture. Long links glide freely; short links in dense tangles contribute disproportionately to obstacle strength.

Recent work on fcc metals under monotonic loading tracks **link length distributions** on each slip system: segments between junctions, classified as active or inactive under the current stress state. Two patterns emerge across more than a hundred DDD simulations:

- **Inactive slip systems** maintain link lengths that follow a **single exponential** distribution — a memoryless Poisson-like picture of random forest structure left behind when slip ceases on that system.
- **Active slip systems** evolve toward **double-exponential** distributions whose shape responds to resolved shear stress — consistent with a generalized Poisson process in which stress accelerates creation and annihilation of links on the active system.

For the copper wire, this distinction matters when cold work activates only a subset of slip systems while others remain latent. Exporting a single \(\rho\) to crystal plasticity collapses that structure. Exporting **link statistics** — mean link length \(\bar\ell\), active-system fractions, distribution shape parameters — gives constitutive models internal variables with clearer physical meaning than a fitted Voce law alone.

The author's research on [link statistics during strain hardening](https://doi.org/10.1016/j.jmps.2026.106533) sits at this interface: using large-scale DDD to extract statistical laws that continuum models can adopt as **internal state variables** beyond scalar dislocation density. For copper wire, where conductivity depends on defect scattering, link-length statistics may correlate with both mechanical strength and electrical resistivity — a reminder that mesoscale structure carries multiple property footprints.

The mesoscale lesson matches the book's ladder theme: DDD does not only produce \(\tau(\gamma)\); it produces **distributional** outputs that homogenization must decide whether to keep or discard.

## Frank–Read sources and multiplication

When a pinned dislocation segment bows under stress, it may spontaneously double: each bowed half-loop expands and closes, leaving two loops and regenerating the pinned segment — a **Frank–Read source**. Multiplication is the exponential engine of work hardening: a few initial dislocations become a forest.

The critical condition for bow-out balances line tension \(T \sim \mu b^2\) against applied stress. DDD captures this geometry explicitly; continuum models approximate it through a **source density** term in the \(\rho\) evolution equation.

In drawn copper wire, pre-existing dislocation sources from prior processing determine the initial hardening rate. DDD sensitivity to initial microstructure mirrors experimental batch-to-batch variability — another reason mesoscale simulation complements macroscale testing.

## Boundary conditions and finite domains

Infinite-medium Green's functions simplify bulk single-crystal studies. Real wires have **surfaces** where dislocations can **escape** (reducing \(\rho\) and softening) or **pile up** (raising local stress and potentially nucleating cracks). Image stress methods or finite-domain elastic solvers enforce traction-free or periodic boundary conditions on bounded volumes.

Coupling DDD to continuum FEM — passing dislocation density or back stress as internal variables — is an active research area. The wire's surface is not merely a geometric constraint; it is a **sink and source** for line defects.

## Coupling scales

| Scale | Method | State variable | Output to next scale |
|-------|--------|----------------|----------------------|
| DFT / MD | Core structure, \(\gamma_{\text{sf}}\), mobility | Atomic positions | Segment rules, \(M(\boldsymbol{\sigma})\) |
| DDD | Line network | Segment coordinates, \(\rho\), link stats | Hardening law, texture drivers |
| Crystal plasticity FEM | Slip systems | Slip rates, \(\rho\) (internal) | Polycrystal texture, anisotropic flow |
| Continuum FEM | Homogenized \(\mathbb{C}\), J2 | Stress, strain | Engineering design, wire sag |
| CFD (if heated) | Navier–Stokes | Velocity, temperature | Thermal softening input |

Machine learning accelerates the FEM step: graph neural networks on polycrystal meshes learn stress fields from microstructure — but still need DDD or experiments for training data at the mesoscale. Surrogates do not remove the ladder; they climb it faster.

## Strain-rate and temperature effects

Copper wire experiments run at strain rates \(\dot\varepsilon \sim 10^{-3}\)–\(10^{-1}\) s\(^{-1}\); DDD can access similar rates in stress-controlled tests. MD often exceeds \(10^7\) s\(^{-1}\), requiring extrapolation or **strain-rate sensitivity** parameters in mobility:

\[
v \propto \exp\!\left(-\frac{\Delta G(\tau)}{k_B T}\right),
\]

with activation free energy \(\Delta G\) decreasing under stress — thermally activated glide.

Temperature raises recovery rates (cross-slip, climb via vacancies). Annealing simulations couple DDD to vacancy diffusion models: dislocations climb when vacancies arrive at jogs. Wire conductivity recovery during anneal is partly **dislocation annihilation** — mesoscale structure relaxing toward lower \(\rho\).

## Comparison to continuum hardening models

| Model | Captures | Omits |
|-------|----------|-------|
| Isotropic J2 + Voce hardening | Macro \(\sigma\)–\(\varepsilon\) curve | Texture, anisotropy, Bauschinger |
| Crystal plasticity | Slip system activity, texture | Individual dislocation topology |
| DDD | Line geometry, junctions, link-length statistics | Fast core reactions, chemistry |
| MD | Core, nucleation | Time/length scale of wire |

Calibration path: DDD → extract \( \tau(\gamma), \dot\rho(\gamma), \bar\ell(\gamma) \) → fit crystal plasticity or simplified J2 internal variables → FEM of wire. Each hop loses detail but gains domain size.

## Validation and limitations

DDD validates against:

- **TEM measurements** of dislocation structures post-mortem
- **In situ diffraction** during loading (pattern evolution)
- **MD** on small volumes with matching boundary conditions
- **Macroscopic stress–strain curves** when homogenized

Limitations include:

- **Core physics** approximated, not resolved
- **Short-range reactions** (junction types, cross-slip rates) empirically parameterized
- **Phonon drag** and **solute pinning** require extensions for alloyed or high-temperature copper
- **Polycrystal** DDD with full grain-boundary physics remains expensive

Unvalidated DDD is animated elasticity with pretty lines. Convergence studies on segment length and time step — analogous to FEM mesh refinement — are mandatory.

## Worked example: Taylor hardening on drawn copper

Cold-drawn copper wire carries a dislocation forest frozen by manufacturing. A scalar Taylor estimate links that forest to the extra shear stress needed for further slip — the upward bend the load cell records after yield.

Take representative values for fcc Cu at room temperature:

| Quantity | Symbol | Value | Source rung |
|----------|--------|-------|-------------|
| Shear modulus | \(\mu\) | \(\approx 48\,\mathrm{GPa}\) | Experiment / DFT (Part IX) |
| Burgers vector magnitude | \(b\) | \(2.56\,\mathrm{\AA}\) | Crystal geometry |
| Taylor factor | \(\alpha\) | \(\approx 0.3\) | Literature / DDD calibration |
| Dislocation density (cold-drawn) | \(\rho\) | \(\sim 10^{14}\,\mathrm{m}^{-2}\) | TEM / DDD post-mortem |

Taylor hardening gives

\[
\Delta\tau = \alpha\,\mu\,b\,\sqrt{\rho}
\approx 0.3 \times 48\times10^9 \times 2.56\times10^{-10} \times \sqrt{10^{14}}
\approx 37\,\mathrm{MPa}.
\]

Converting to uniaxial stress with Taylor factor \(M \approx 3.06\) for fcc polycrystal texture gives \(\Delta\sigma \approx 110\,\mathrm{MPa}\) — order-of-magnitude consistent with the gap between annealed and half-hard copper yield strengths. Part VI's Voce law can fit the macroscopic curve; this calculation shows **where the fitted hardening modulus hides its physics**: in \(\sqrt{\rho}\), not in an arbitrary slope typed into the input deck.

A DDD run should reproduce \(\rho(\gamma)\) and \(\tau(\gamma)\) from which \(\alpha\) and the \(k_1, k_2\) evolution law are extracted — not merely match one stress–strain point.

## OpenDiS workflow

A reproducible OpenDiS-style workflow for copper single-crystal shear, modeled on the LAMMPS checklist in Part VIII:

1. **Initialize** a dislocation network — Frank–Read sources on one active {111}\(\langle 110\rangle\) system, or an imported post-mortem structure from TEM.
2. **Material table** — anisotropic elastic constants \(C_{ij}\) from DFT (Part IX) or experiment; Burgers vector and slip systems for fcc Cu; mobility law \(M(\tau, T)\) from MD (Part VIII) or literature tables.
3. **Load protocol** — constant strain rate \(\dot\gamma\) matched to the prologue tensile frame (\(\dot\varepsilon \sim 10^{-3}\)–\(10^{-1}\,\mathrm{s}^{-1}\)); temperature \(T\) fixed or coupled to Joule heating later.
4. **Integrate** — segment timestep constrained by mobility and remeshing when curvature exceeds threshold; log \(\rho\), \(\tau\), and link-length histograms each strain increment.
5. **Convergence** — refine segment length and timestep until \(\tau(\gamma)\) at fixed \(\gamma\) changes by less than 5%; compare inactive slip systems for single-exponential link statistics.
6. **Export** — write \(\tau(\gamma)\), \(d\rho/d\gamma\), \(\bar\ell(\gamma)\), and calibrated \(\alpha\) to a yaml or table for crystal plasticity (foreshadow Part VII.3 DAMASK handoff).

The copper wire's cold-worked strength is, in part, a snapshot of step 4 frozen by manufacturing — DDD explains what that snapshot contains.

### Scale-boundary handshake: DDD exports to FEM crystal plasticity

OpenDiS produces **dislocation density evolution** \(\rho(\gamma, t)\) and **resolved shear stress** \(\tau(\gamma)\) on a single-crystal RVE. FEM crystal plasticity (Part VI, Part IV user subroutines) consumes **hardening moduli** and **yield surface parameters** — not raw segment coordinates.

| DDD export | Transformation | FEM / continuum input |
|------------|----------------|----------------------|
| \(\rho(t)\) at several strains | Fit Taylor \(\Delta\tau = \alpha\mu b\sqrt{\rho}\) | Voce hardening modulus \(k_1\) |
| \(v(\tau, T)\) from MD-informed mobility | Tabulate \(\dot\gamma(\tau, T)\) | Flow rule in crystal plasticity |
| Line-length distribution | Average obstacle spacing \(L \sim 1/\sqrt{\rho}\) | Internal length in gradient plasticity (optional) |
| Stress–strain curve on RVE | Homogenize \(\bar\sigma\), \(\bar\varepsilon\) | Validate against Part IV tensile run |

**Downward import (FEM → DDD).** The far-field strain rate \(\dot\varepsilon\) from a Part IV tensile simulation sets the loading column in OpenDiS — DDD is a **local RVE calculator** for a material point on the wire mesh.

**What breaks without the handshake.** Pasting literature \(\alpha = 0.3\) while DDD predicts \(\rho\) a factor of three too low doubles Taylor hardening and shifts the load cell curve in Act IV — the mesoscale analogue of mixing handbook \(E\) with DFT \(\gamma_{\text{sf}}\). Archive `ddd_rho_vs_strain.csv` beside `mobility_cu_300K.yaml` and the Part IV `.inp` that supplied boundary strain rate; the epilogue's multiscale afternoon treats missing files as failed audits.

## Reproducibility checklist

Before exporting DDD hardening laws to crystal plasticity or FEM:

1. Cite mobility table provenance (MD potential, temperature, strain rate).
2. Converge segment length and timestep on \(\tau(\gamma)\) at fixed plastic strain.
3. Document initial network topology (random loops vs. Frank–Read sources).
4. Compare \(\rho\) and link-length distributions to TEM or in situ diffraction when available.
5. Cross-check \(\alpha\) and \(C_{ij}\) against independent MD volumes on matching boundary conditions.
6. Archive input decks, material tables, and random seeds for network initialization.

Unvalidated DDD is animated elasticity with pretty lines — the same warning Part VIII repeats for unconverged MD and Part IX repeats for unconverged plane-wave cutoff.

## Lab act: read the hardening bend from forest density (Act IV)

**Act IV** is the upward bend on the force–displacement trace after yield. Part VI fitted it with a scalar hardening modulus \(H\); this Lab act estimates the same bend from **dislocation forest density** — the mesoscale object DDD simulates.

**Step 1 — Taylor hardening on paper.** For fcc copper, Taylor's relation gives critical resolved shear stress \(\tau = \tau_0 + \alpha \mu b \sqrt{\rho}\), with shear modulus \(\mu \approx 48\,\text{GPa}\), Burgers magnitude \(b \approx 2.5\times 10^{-10}\,\text{m}\), and \(\alpha \approx 0.3\). Cold-drawn wire often carries \(\rho \sim 10^{14}\)–\(10^{15}\,\text{m}^{-2}\); annealed copper starts near \(\rho \sim 10^{12}\,\text{m}^{-2}\).

**Step 2 — convert to uniaxial stress.** With Taylor factor \(M \approx 3.06\) for typical polycrystal texture, uniaxial yield rise is \(\Delta\sigma \approx M \Delta\tau \approx M \alpha \mu b (\sqrt{\rho_{\text{drawn}}} - \sqrt{\rho_{\text{annealed}}})\). Using \(\rho_{\text{drawn}} = 5\times 10^{14}\,\text{m}^{-2}\) and \(\rho_{\text{annealed}} = 10^{12}\,\text{m}^{-2}\):

\[
\Delta\sigma \approx 3.06 \times 0.3 \times 48\times 10^9 \times 2.5\times 10^{-10} \times (7.1\times 10^7 - 3.2\times 10^6) \approx 80\,\text{MPa}.
\]

That order-of-magnitude matches the gap between annealed (\(\sim 70\,\text{MPa}\)) and half-hard (\(\sim 150\)–\(200\,\text{MPa}\)) copper — the same bend the load cell showed in the prologue.

**Step 3 — OpenDiS-style simulation checklist.** On a single crystal with one active slip system:

1. Initialize Frank–Read sources or a relaxed random loop network.
2. Load elastic constants from Part IX DFT (or handbook \(C_{ij}\)).
3. Apply constant strain rate \(\dot\gamma\) matched to the tensile frame.
4. Log \(\rho(\gamma)\) and resolved stress \(\tau(\gamma)\) each increment.
5. Refine segment length until \(\tau\) at fixed \(\gamma\) changes by \(< 5\%\).

Plot \(\tau\) versus \(\sqrt{\rho}\): a straight line confirms Taylor hardening; curvature signals link-length effects or inactive slip systems waking up.

**Step 4 — connect to Part VI.** Export \(\tau(\gamma)\) and \(d\rho/d\gamma\) to replace fitted \(H\) in the return-mapping loop. The load cell bend is no longer a magic constant — it is forest statistics you can simulate, archive, and trace to mobility tables from Part VIII MD.

| Quantity | Phenomenological (Part VI) | DDD (this Lab act) |
|----------|---------------------------|---------------------|
| Hardening | \(\sigma_y = \sigma_{y0} + H\alpha\) | \(\tau(\rho)\) from line motion |
| History | Internal variable \(\alpha\) | Link-length histograms, \(\rho(\gamma)\) |
| Calibration | One tensile test | Mobility + \(C_{ij}\) + network topology |

Turn back to the mounted wire when the FEM curve matches experiment in bulk but the hardening slope changes with mesh refinement — that is the signal Part VII exists to answer.

## Concept map checkpoint (dislocation dynamics)

This chapter's four questions — scoped to **segment-network simulation**, not the full Part VII arc:

| Question | DDD answer (copper wire) |
|----------|--------------------------|
| What **object**? | Segment network with Burgers vector \(\mathbf{b}\) and line direction \(\boldsymbol{\xi}\) |
| What **structure**? | Peach–Köhler forces; mobility law \(M\); elastic superposition |
| What **theorem**? | Taylor \(\tau \propto \sqrt{\rho}\); link-statistics evolution on active slip systems |
| What **breaks**? | Core cutoff artifacts; wrong mobility; scalar \(\rho\) collapsing texture |

The load cell's post-yield bend is not a fitted Voce slope alone — it is a forest whose density and link statistics DDD can measure. The **full Part VII** checkpoint — taxonomy through crystal plasticity handoff — closes in [VII.3](03-polycrystal-and-fem-handoff.md). Parts VIII–IX supply the mobility and elastic constants this chapter consumes.

## Bridge to Part VII.3 {#bridge-to-vii3}

Single-crystal DDD explains how lines move, multiply, and harden a crystal — but the copper wire is polycrystalline and structural models speak crystal plasticity and FEM, not segment networks alone. [VII.3](03-polycrystal-and-fem-handoff.md) follows how DDD statistics export upward to constitutive laws and where Peierls barriers and grain boundaries still demand finer-scale input from Parts VIII–IX.

| What VII.2 simulated | What [VII.3](03-polycrystal-and-fem-handoff.md) must homogenize |
|------------------------|----------------------------------------------------------------|
| Segment network on one slip system | Texture and grain orientation across thousands of crystals |
| \(\tau(\gamma)\), \(\rho(\gamma)\), link-length histograms | Internal state variables on a crystal plasticity mesh |
| Mobility \(M(\tau,T)\) from MD tables | Peierls thresholds and grain-boundary barriers |
| OpenDiS export yaml for one crystal | DAMASK / FEM handoff for the full wire spool |

**Scale-boundary handshake (VII.2 → VII.3 → Part IV/VI).**

| DDD export (this chapter) | Homogenization (next chapter) | Continuum consumer | Failure mode |
|---------------------------|-------------------------------|--------------------|--------------|
| \(\tau(\gamma)\), \(\rho(\gamma)\) from OpenDiS | Taylor fit → Voce hardening \(k_1\) | Part VI return-mapping \(H\) | Literature \(\alpha=0.3\) with wrong \(\rho\) |
| Link-length histograms | Obstacle spacing \(L \sim 1/\sqrt{\rho}\) | Gradient plasticity (optional) | Scalar \(\rho\) collapsing texture |
| \(M(\tau,T)\) from [VIII.2](../part08-md/02-ensembles-integrators.md) | Flow-rule tabulation \(\dot\gamma(\tau,T)\) | Crystal plasticity UMAT | Rate-independent J₂ at high strain rate |
| \(C_{ij}\), \(\gamma_{\text{sf}}\) from [Part IX](../part09-dft/03-dft-workflows.md) | Peierls threshold calibration | Partial separation in segment rules | Linear elasticity at \(r < 1\) nm |
| Single-crystal RVE stress curve | Texture average over grain orientations | Part IV tensile run on wire spool | One orientation vs cold-drawn polycrystal |

Return to the [prologue](../../prologue/00-many-scales.md): **Act IV — Hardening** is when the load cell curve bent upward after yield because lines multiplied and tangled — DDD made that forest visible as moving segments. Part VI's J₂ plasticity fitted the bend with a scalar hardening modulus \(H\); this chapter showed where \(H\) hides its physics in \(\rho\) and link statistics. [VII.3](03-polycrystal-and-fem-handoff.md) closes the mesoscale arc by asking how those statistics survive **drawing dies and grain boundaries** — the organizational scale the cold-drawn wire on the bench actually has.

Parts VIII–IX supply the mobility and elastic constants this chapter consumed; VII.3 is where DDD stops being a single-crystal movie and becomes **input for the same FEM mesh Part IV taught us to assemble**. The epilogue's **Handshake 4** formalizes the rate-sensitivity export this chapter's mobility tables feed into [VI.4 Perzyna](../part06-continuum/04-nonlinear-plasticity-preview.md#bridge-to-part-vii) — DDD power-law \(m\) at \(10^3\,\text{s}^{-1}\) extrapolated to lab \(10^{-3}\,\text{s}^{-1}\) is the same unit-mismatch hazard Part V warned about at CHT interfaces.

| Verification gate (this chapter) | What must pass before VII.3 | Epilogue handshake |
|----------------------------------|----------------------------|-------------------|
| Segment length convergence on \(\tau(\gamma)\) | Taylor fit stable to \(\pm 5\%\) | Handshake 3: \(\rho\) → \(H\) |
| Mobility \(M(\tau,T)\) tabulated | Matches MD shear at same \(T\) | Handshake 4a: rate extrapolation |
| \(C_{ij}\) from DFT or handbook | Peierls threshold calibrated | Handshake 2: elastic constants |
| Single-crystal RVE stress curve | Texture average planned | Handshake 5: polycrystal FEM |

Turn the page when OpenDiS converges on one orientation but the wire's macroscopic hardening still disagrees with experiment — that is the signal that polycrystal texture, not segment timestep, is the missing physics. If the forest-density Lab act above matches the load cell bend on paper but the spool test does not, the cold-drawn wire's grain structure — not another OpenDiS increment — is what [VII.3](03-polycrystal-and-fem-handoff.md) must homogenize.
