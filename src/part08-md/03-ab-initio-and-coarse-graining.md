# Ab Initio MD, Coarse-Graining, and the Ladder Upward

Classical molecular dynamics of Part VIII assumes nuclei move on a **potential energy surface** — usually empirical (EAM) or fitted to quantum data. This chapter closes the atomistic part by making that assumption explicit: **Born–Oppenheimer ab initio MD** computes forces from DFT each timestep; **coarse-graining** and **potential fitting** translate DFT landscapes into EAM tables DDD and production MD can afford.

The copper wire at laboratory scale will never be a full DFT supercell. The wire at atomic scale **must** be described quantum mechanically when bonds rearrange, chemistry appears, or empirical potentials have never been validated. The art is knowing when ab initio MD is mandatory, when classical MD suffices, and how to compress atomistic trajectories into numbers the mesoscale accepts.

## Scene: when EAM is not enough

Most MD of copper uses an EAM potential fit once to DFT data and then trusted for millions of timesteps. At a crack tip where bonds stretch until rupture, or at a surface where oxidation nucleates, that trust may fail. Born–Oppenheimer MD recomputes forces from DFT each step; coarse-graining distills those trajectories into tables the mesoscale can afford. The wire's fracture strain is either validated at this scale or assumed.

## Born–Oppenheimer molecular dynamics

In **Born–Oppenheimer MD (BOMD)**, nuclear positions \(\{\mathbf{R}_I\}\) evolve classically while electrons stay in the instantaneous ground state:

\[
M_I \ddot{\mathbf{R}}_I = -\nabla_{\mathbf{R}_I} E_{\text{DFT}}(\{\mathbf{R}_I\}).
\]

Each timestep requires a **self-consistent Kohn–Sham solve** (Part IX) to obtain energy and forces. Cost is orders of magnitude above EAM — thousands of atoms for picoseconds, not millions for nanoseconds.

| Method | Force source | Typical scale (Cu) |
|--------|--------------|-------------------|
| Classical MD (EAM) | Tabulated potential | \(10^6\)–\(10^9\) atoms, ns |
| BOMD | DFT each step | \(10^2\)–\(10^3\) atoms, ps |
| Car–Parrinello MD | Extended Lagrangian for electrons | Similar to BOMD; different dynamics |

Use BOMD when:

- **Bond breaking** or **phase transformations** invalidate fixed functional forms,
- **Defect core structures** set mobility laws DDD will use,
- **New alloys or interfaces** lack trusted EAM libraries.

For bulk modulus and lattice parameter of perfect fcc Cu, BOMD cross-checks EAM; for a **crack tip** in the wire where bonds stretch until failure, BOMD (or QM/MM) is often the only trustworthy path.

## QM/MM and partitioned domains

**Quantum mechanics / molecular mechanics (QM/MM)** partitions the system: a **QM region** (DFT) handles reactive or electronic detail; an **MM region** (EAM) handles elastic far-field. Link atoms or boundary potentials prevent gaps at the interface.

Typical copper wire scenarios:

- **Surface oxidation**: DFT on Cu–O bonds at the surface; EAM bulk below.
- **Notch root fracture**: DFT on the bond-breaking zone; EAM on the surrounding crystal.
- **Dislocation core**: DFT on the core; elastic continuum or EAM outside (core studies).

QM/MM is the practical bridge between Parts VIII and IX when the whole wire cannot be quantum mechanical but **part of it must be**.

## Fitting potentials from DFT

Production MD and DDD rely on **fitted potentials**. A standard workflow for copper:

1. **DFT reference data**: Equation of state (lattice constant, cohesive energy), elastic constants, vacancy and interstitial formation energies, generalized stacking-fault (GSF) surfaces along slip paths, perhaps surface energies.
2. **Functional form**: EAM (embedded atom method) or MEAM with chosen cutoff and neighbor criteria.
3. **Optimization**: Minimize weighted error between potential predictions and DFT sets (force matching on diverse configurations is increasingly used).
4. **Validation**: Phonon dispersion, melting point (approximate), mobility trends vs. DFT core structures.

```text
DFT (Part IX)  →  energies, forces, GSF landscapes
       ↓
Fit EAM / SNAP / ML potential
       ↓
Classical MD (Part VIII)  →  diffusion, dislocation cores, fracture trajectories
       ↓
Mobility tables, τ_P, junction rules  →  DDD (Part VII)
```

A potential fit only to perfect-lattice bulk properties **fails** at dislocation cores and surfaces — exactly where the wire's processing history matters. Multiscale credibility requires **diverse** training configurations, not a single equation-of-state curve.

## Coarse-graining atomistic data

Not every DDD or FEM parameter needs a full trajectory. Common **coarse-graining** exports:

| Observable | MD procedure | Consumer |
|------------|--------------|----------|
| Diffusion coefficient \(D\) | NVT, mean-square displacement | Creep models, vacancy kinetics |
| Stacking-fault energy \(\gamma_{\text{sf}}\) | Rigid shift of half-crystals | DDD mobility, Peierls estimates |
| Dislocation core structure | Relax core in periodic cell | Image stress corrections, \(\tau_P\) |
| Uniaxial stress–strain (nanowire) | NPT tension | Validation of continuum \(E\), yield |
| Friction stress vs. temperature | Shear with thermostat | Mobility \(M(T)\) |

**Coarse-grained models** (e.g., dissipative particle dynamics, phase-field crystal) sit between MD and DDD; they average atoms into fields on larger grids. When dislocation density is high and atomistic detail is secondary, such models accelerate mesoscale statistics — at the cost of new calibration to MD.

For the wire, coarse-graining is the **discipline of reporting**: which averages over which time windows, with which uncertainty, at which temperature — so Part VII does not inherit a mobility value from a 50 ps simulation at the wrong strain rate.

## Machine-learned potentials

**Neural network potentials** (Behler–Parrinello, DeepMD, etc.) interpolate DFT data with near-DFT accuracy at MD cost after training. Workflow:

1. Generate DFT snapshots (active learning expands the set where uncertainty is high).
2. Train network on energies and forces.
3. Deploy in LAMMPS for large-scale MD.

For multiscale copper studies, ML potentials increasingly replace hand-tuned EAM when **reactive** or **complex** configurations matter. The ladder logic is unchanged: electronic structure defines the surface; atomistics explores it; mesoscale inherits statistics.

## Limits of classical MD for the wire

Classical MD omits:

- **Electronic excitations** (metallic heat capacity is OK; photochemistry is not),
- **Nuclear quantum effects** (minor for Cu, major for H in steels),
- **Long-time rare events** without acceleration (creep, slow diffusion at room temperature).

Recognizing limits prevents **category errors**: MD cannot predict decade-long wire creep without kinetic Monte Carlo or accelerated methods (mentioned in the previous chapter). It **can** supply stacking-fault energies and core structures that make DDD and crystal plasticity credible.

## Reproducibility at the MD–DFT boundary

When publishing parameters that cross scales:

1. Report DFT functional, pseudopotential, k-mesh, and convergence (Part IX checklist).
2. Report potential fitting database and weights.
3. Archive both **DFT inputs** and **LAMMPS decks** with versions.
4. Document whether forces used in MD match finite-difference DFT forces on the same configs.

Silent mismatch — PBE DFT training, LDA used in a later study — corrupts the ladder worse than a 5% force error.

## Scene return: why this checklist matters for the wire

Return to the prologue's **Act V (notch)** and **Act VI (foundation)** for a moment. The operator has not yet trusted the fracture strain at the grip corner or the multiscale story printed in the final report — but those numbers will stand or fall on what happens in this chapter. A single EOS curve or a hand-waved EAM file cannot certify the wire: **\(\gamma_{\text{sf}}\)** sets whether DDD sees the right stacking-fault energy, core forces set whether dislocations move at the right stress, and archived DFT inputs set whether a colleague can reproduce the ladder five years later. Read the worked example below as the audit the wire earns before Part IX names the electrons that supply every entry in the handoff table.

## Worked example: Cu EAM fit from DFT to LAMMPS

This section ties Part IX outputs to Part VIII inputs for fcc copper — the same material as the wire, at the scale where potentials are built rather than assumed.

### DFT reference dataset (Part IX checklist)

Before fitting, converge bulk properties on fcc Cu (GGA-PBE, PAW pseudopotential — document versions):

| Configuration | DFT property | Typical PBE target | Weight in fit |
|---------------|--------------|-------------------|---------------|
| Equilibrium fcc | \(a_0\), \(E_{\text{coh}}\) | \(a_0 \approx 3.63\) Å, \(E_{\text{coh}} \approx -3.7\) eV/atom | High |
| Elastic strain ±0.5% | \(C_{11}, C_{12}, C_{44}\) | 170, 124, 76 GPa (order of magnitude) | High |
| Vacancy | \(E_f^{\text{vac}}\) | \(\sim 1.2\) eV | Medium |
| (111) stacking fault | \(\gamma_{\text{sf}}\) | \(\sim 45\) mJ/m\(^2\) | **Critical for DDD** |
| Surface (111) | \(\gamma_{\text{surf}}\) | \(\sim 1.2\) J/m\(^2\) | Medium |
| Core structure | Forces on atoms near dissociated core | Force-matching | High if mobility is goal |

Archive Quantum ESPRESSO inputs (`pw.x`, `vc-relax`, strained cells) with k-mesh and cutoff documented — Part IX Chapter 3 ritual.

### EAM fitting checklist

1. **Choose functional form:** Finnis–Sinclair or DYNAMO-style EAM for monatomic Cu; cutoff radius \(r_c \approx 5\)–\(6\) Å (include 2nd-neighbor shell in fcc).
2. **Optimization target:** weighted least squares on equation of state + elastic constants + \(\gamma_{\text{sf}}\) + optional force matching on NVT snapshots from short BOMD runs.
3. **Reject overfit:** potential must reproduce **phonon** dispersion at \(\Gamma\) (optional ph.x check) and not blow up at high coordination defects.
4. **Validate outside training set:**
   - Melting point (approximate — often 10–15% low for EAM),
   - Uniaxial tension of nanowire: Young's modulus vs Part VI,
   - Dislocation core width and \(\gamma_{\text{sf}}\) from rigid shift vs DFT GSF curve.
5. **Export for DDD:** fit \(M(\tau, T)\) from NVT shear simulations at several temperatures; tabulate for OpenDiS mobility input (cross-ref Part VII worked example).

```text
DFT (QE)  →  Cu_fit_data/  (EOS, GSF, vacancy, forces)
       ↓
optimize_eam.py  →  Cu.eam.alloy
       ↓
validate_lammps/  (phonon, tension, core)
       ↓
mobility_tables/  →  Part VII OpenDiS
```

### Minimal LAMMPS deck (metal units, NVT equilibration)

After fitting `Cu.eam.alloy`, a standard sanity run before production:

```lammps
# in.lammps — 500-atom fcc Cu, NVT 300 K, sanity equilibration
units           metal
atom_style      atomic
boundary        p p p

lattice         fcc 3.615
region          box block 0 5 0 5 0 5
create_box      1 box
create_atoms    1 box

pair_style      eam/alloy
pair_coeff      * * Cu.eam.alloy Cu

mass            1 63.546

velocity        all create 300.0 12345
fix             1 all nvt temp 300.0 300.0 0.1

timestep        0.001        # ps
thermo          100
run             10000        # 10 ps equilibration

# Production: uniaxial tension along z (NPT stress control)
unfix           1
fix             2 all npt temp 300.0 300.0 0.1 iso 0.0 0.0 1.0
variable        s equal step
fix             3 all deform 1 z erate 1.0e-4 units box
run             50000
```

**Reading the output:**

- `thermo` pressure should relax to \(\sim 0\) GPa in NPT before deformation,
- Potential energy per atom stable after equilibration (no drift → timestep OK),
- Stress–strain from `fix deform` exports Young's modulus; compare to DFT \(C_{11}\) and Part VI \(E \approx 110\)–\(130\) GPa for polycrystalline wire.

### DeepMD / ML potential workflow (when EAM is insufficient)

When dislocation cores, surfaces, or crack tips dominate (notch root in the wire), extend the ladder:

| Stage | Tool | Input | Output |
|-------|------|-------|--------|
| Active learning | DFT snapshots | Uncertain configs from short MD | Expanded training set |
| Train | DeepMD-kit | `type.raw`, `box.raw`, forces | `graph.pb` |
| Deploy | LAMMPS `pair deepmd` | Same `in.lammps` with `pair_style deepmd` | Large-scale trajectories |
| Export | Coarse-grain | Core structures, \(\gamma_{\text{sf}}\), \(M(\tau)\) | Part VII mobility |

The intellectual contract is unchanged: **electronic structure defines the surface; MD explores it; mesoscale inherits statistics.** ML potentials reduce the cost of exploration, not the need for DFT anchors.

## Accelerated methods: when MD time runs out

Classical MD integrates femtosecond timesteps for nanoseconds of physical time. The copper wire's **creep**, **slow vacancy diffusion at room temperature**, and **rare cross-slip events** live at seconds to years — scales no direct MD trajectory can span. Accelerated methods do not remove the time-scale gap; they **concentrate sampling** on the events that matter and export rates or barriers the mesoscale can use.

### Nudged elastic band (NEB) for migration barriers

Vacancy diffusion and dislocation glide require **activated hops** over energy barriers. **Nudged elastic band** methods find minimum-energy paths between two relaxed configurations (initial and final states) and estimate the barrier height \(\Delta E\):

\[
D \approx a^2 \nu_0 \exp(-\Delta E / k_B T),
\]

where \(a\) is hop distance and \(\nu_0\) is an attempt frequency (\(\sim 10^{12}\)–\(10^{13}\,\text{s}^{-1}\) for metals). NEB on a vacancy hop in Cu with EAM or a DeepMD potential replaces guessing \(\Delta E\) from a misfit MSD slope at 300 K.

| Method | Input | Output | Consumer |
|--------|-------|--------|----------|
| NEB / CI-NEB | Relaxed initial/final configs | \(\Delta E\), MEP | Arrhenius \(D(T)\); KMC rates |
| Metadynamics | Collective variables (CVs) | Free-energy surface | Phase transitions, stacking faults |
| Parallel tempering | Replica exchange at multiple \(T\) | Enhanced sampling at low \(T\) | Complex energy landscapes |

For the wire's **annealing** story (Act II heating), NEB barriers for vacancy formation (\(E_f^v\)) and migration (\(\Delta E_m\)) connect Part IX DFT totals to Part VII dislocation climb rates without simulating every hop explicitly.

### Metadynamics: free-energy surfaces the wire inherits

**Metadynamics** adds a history-dependent bias potential \(V(\mathbf{s}, t)\) to the Hamiltonian, where \(\mathbf{s}\) is a small set of **collective variables** (CVs) that summarize the configuration. Gaussian hills deposited along the trajectory gradually fill metastable wells; the biased dynamics eventually escape local minima and explore the full free-energy landscape \(F(\mathbf{s}) = -k_B T \ln Z(\mathbf{s})\).

For copper, the CVs that matter for multiscale handoffs are not abstract — they are the same coordinates Part IX and Part VII already name:

| CV | Physical meaning | Wire-scale consumer |
|----|------------------|---------------------|
| Shear displacement \(u\) along a {111} slip direction | Position on the generalized stacking-fault (GSF) surface | \(\gamma_{\text{sf}}\), partial separation \(d\) (Part VII) |
| Coordination number of surface atoms | Nucleation of oxide or adsorbate | Surface chemistry at notch (Act V) |
| Dislocation core radius or partial separation | Core structure under stress | Mobility \(M(\tau)\) calibration (Part VII.2) |

**Worked sketch: GSF metadynamics on Cu (111).** Build a bicrystal with one {111} plane shifted rigidly by coordinate \(u\) (same geometry as the DFT GSF workflow in [IX.3](../../part09-dft/03-dft-workflows.md)). Choose CV \(s = u / b_p\) where \(b_p = a_0/\sqrt{6}\) is the Shockley partial magnitude. Run well-tempered metadynamics in LAMMPS (`fix plumed`) or PLUMED coupled to an audited EAM:

1. **Equilibrate** the slab at 300 K with fixed lateral box; verify zero net stress at \(u = 0\).
2. **Deposit hills** with initial height \(\omega \sim k_B T\) and width \(\sigma \sim 0.05\)–\(0.1\,b_p\); well-tempered factor \(\Delta T \sim 300\)–\(500\,\text{K}\) prevents over-filling.
3. **Monitor** \(F(u)\): a minimum at the stable fault gives \(\gamma_{\text{sf}} = F(u_{\min}) / A_{\text{fault}}\); a maximum at the unstable fault gives \(\gamma_{\text{USF}}\) for cross-slip barriers.
4. **Cross-check** against Part IX DFT on the same \(u\) grid — metadynamics on EAM is a **fast scout**; DFT is the audit before OpenDiS imports the numbers.

```text
Metadynamics F(u) on EAM  →  locate u_min, u_max
       ↓
DFT single-point at u_min, u_max (IX.3)  →  γ_sf, γ_USF with pedigree
       ↓
Partial separation d ∝ 1/γ_sf  →  Part VII segment rules
```

**What breaks without metadynamics discipline.** A single constrained MD snapshot at one \(u\) reports an energy, not a **free energy** — entropic contributions at finite \(T\) shift \(\gamma_{\text{sf}}\) by several mJ/m\(^2\) for some metals. Depositing hills too aggressively fills the well before the system visits the unstable fault; the resulting \(\gamma_{\text{USF}}\) is a numerical artifact, not a barrier Part VII can use for recovery during annealing.

### Lab act: GSF free-energy surface via well-tempered metadynamics (Act VI scout — Foundation)

**Act VI** runs in parallel with the wire-scale afternoon — someone must supply \(\gamma_{\text{sf}}\) and \(\gamma_{\text{USF}}\) before OpenDiS imports stacking-fault numbers. DFT (Part IX) is the audit; **metadynamics on an audited EAM** is the fast scout that tells you where to place DFT single points on the \(\gamma(\mathbf{u})\) grid. This Lab act builds the full GSF curve in hours, not days.

**Step 1 — bicrystal geometry.** Build a {111} slab with 24–32 atomic layers and in-plane dimensions \(\geq 8\,a_0\) (same slab template as [IX.3 GSF workflow](../../part09-dft/03-dft-workflows.md)). Fix the bottom four layers; allow the top half to relax in-plane. Define CV \(s = u / b_p\) where \(u\) is rigid shear displacement along \(\langle 112\rangle\) in the fault plane and \(b_p = a_0/\sqrt{6}\).

**Step 2 — PLUMED / LAMMPS setup.** Use the same EAM potential from [VIII.1 Lab act](../part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude). Well-tempered metadynamics parameters (Cu, illustrative):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Hill height \(\omega\) | \(1.2\,k_B T\) | Fills wells without overwhelming barriers |
| Hill width \(\sigma\) | \(0.08\,b_p\) | Resolves USF peak without over-smoothing |
| Well-tempered \(\Delta T\) | 400 K | Prevents over-filling of stable fault well |
| Bias factor | 10–15 | Standard for metal surfaces |
| Deposition pace | Every 500 fs | Balance exploration vs wall time |

**Step 3 — run and monitor.** Equilibrate 50 ps at 300 K with `fix nvt`, then enable metadynamics for 2–5 ns until \(F(s)\) plateaus. Plot \(F(s)\) versus \(s\); identify:

| Feature | CV location \(s\) | Export |
|---------|-------------------|--------|
| Stable fault minimum | \(s \approx 1.0\) | \(\gamma_{\text{sf}} = F(s_{\min}) / A_{\text{fault}}\) |
| Unstable fault maximum | \(s \approx 0.5\) | \(\gamma_{\text{USF}} = F(s_{\max}) / A_{\text{fault}}\) |
| Perfect crystal reference | \(s = 0\) | Set \(F(0) = 0\) by subtracting reference |

**Step 4 — cross-check against DFT.** Run Quantum ESPRESSO single-point energies at \(s \in \{0, 0.5, 1.0\}\) using the IX.3 slab template. Pass criterion: EAM metadynamics and DFT agree on \(\gamma_{\text{sf}}\) within 15% before exporting to Part VII. If disagreement exceeds 15%, the EAM fit is wrong for faulted configurations — refit with GSF points in the training set ([EAM-fit audit below](#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch)).

**Step 5 — archive and export.** Write `gsf_metadynamics_cu111.dat` with columns \((s, F(s)\,\text{eV}, \gamma(s)\,\text{mJ/m}^2)\) and `README_GSF.md` documenting potential version, hill parameters, and DFT cross-check status. Run `./scripts/parse_gsf.sh gsf_metadynamics_cu111.dat` to extract tabulated values for OpenDiS input. The script converts units and flags non-monotonic segments that indicate incomplete sampling.

```text
Metadynamics F(s)  →  parse_gsf.sh  →  gsf_export.yaml
       ↓                                      ↓
DFT audit at s_min, s_max (IX.3)      Part VII partial separation d
```

When `gsf_export.yaml` sits beside `mobility_cu_screw_300K.yaml` in the project folder, Act VI's foundation deck is **complete at the atomistic scout level** — DFT audit remains mandatory before production DDD, but the metadynamics curve tells you which DFT points matter and catches EAM failures before expensive slab calculations.

### Parallel tempering: replica exchange across temperature

**Parallel tempering** (replica exchange MD) runs \(N_{\text{rep}}\) copies of the same system at temperatures \(T_1 < T_2 < \cdots < T_{N_{\text{rep}}}\). Periodically, adjacent replicas attempt to swap configurations with Metropolis acceptance

\[
P_{\text{accept}} = \min\!\left(1,\; \exp\!\left[\(\beta_i - \beta_j\)\(U_j - U_i\)\right]\right),
\]

where \(\beta = 1/k_B T\) and \(U\) is the potential energy of the configuration being offered for swap. Hot replicas explore barrier crossings; cold replicas sample low-\(T\) equilibrium without becoming trapped — the same logic as simulated annealing, but with parallel trajectories and detailed balance.

For the copper wire's **annealing** and **cross-slip** stories, parallel tempering addresses events NEB and plain NVT miss:

| Target process | Why plain MD fails | Parallel tempering role |
|----------------|-------------------|-------------------------|
| Screw dislocation cross-slip at 400–500 K | Rare activated reorientation; ns MD sees zero events | Hot replicas visit cross-slipped cores; cold replica inherits sampled structures |
| Stacking-fault energy at elevated \(T\) | \(F(u)\) shifts with thermal expansion | \(T\)-dependent \(\gamma_{\text{sf}}(T)\) for Part V conjugate heat → Part VII mobility |
| Vacancy cluster formation near notch | Nucleation barrier \(\gg k_B T\) at 300 K | High-\(T\) replicas nucleate; resize and quench to study stability |

**Replica ladder design (Cu, EAM, illustrative).** Choose geometric spacing so swap acceptance stays 20–40%:

| Replica index | \(T\) [K] | Purpose |
|---------------|-----------|---------|
| 1 | 300 | Production mobility calibration |
| 2 | 400 | Wire operating temperature under Joule heat |
| 3 | 600 | Annealing onset |
| 4 | 900 | Accelerated cross-slip sampling |
| 5 | 1200 | Rare core reconstructions |

Attempt swaps every 1000 MD steps; run 5–20 ns per replica before expecting converged swap rates. Export **reweighted** observables at \(T = 300\,\text{K}\) using the multicanonical weights — raw cold-replica time series alone under-samples barriers.

**Handshake to Part VII.** Parallel tempering at \(T_w\) from Part V conjugate heat transfer supplies **temperature-matched** core structures and cross-slip counts for mobility tables — not extrapolated from 300 K MD alone. Document the replica ladder beside `mobility_cu_screw_300K.yaml`; OpenDiS at 400 K needs \(M(\tau, 400\,\text{K})\), not an Arrhenius guess from one cold run. The [Lab act below](#lab-act-parallel-tempering-for-screw-cross-slip-at-joule-heated-temperature-act-ii--iv-bridge) walks through a minimal LAMMPS replica-exchange run that exports those temperature-matched counts.

### Lab act: parallel tempering for screw cross-slip at Joule-heated temperature (Act II–IV bridge)

**Act II** raises wall temperature toward 380 K ([V.4 conjugate heat transfer](../../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid)); **Act IV** hardening depends on whether screw dislocations **cross-slip** and annihilate forest segments during recovery. Plain NVT MD at 400 K rarely observes cross-slip in nanoseconds — the event is activated. **Parallel tempering** lets hot replicas visit cross-slipped cores while a cold replica at \(T_w\) inherits sampled structures with correct Boltzmann weights. This Lab act is the atomistic counterpart of Part VII's [mobility calibration](../part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude), but targets **rare reorientation** rather than glide on a straight line.

**Step 1 — system and potential.** Use the audited EAM from [VIII.1 Lab act](../part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude). Build a periodic cell (\(\geq 10\,000\) atoms) containing one straight screw dislocation on {111}\(\langle 110\rangle\) — the same Volterra geometry as the mobility Lab act, but **without** applied shear: the goal is spontaneous cross-slip, not driven glide.

| Parameter | Value | Role |
|-----------|-------|------|
| Box | \(20\,b \times 20\,b \times 10\,b\) | Suppress spurious image interactions |
| Dislocation line | Along \(z\), screw character | Cross-slip reorients line direction |
| Bottom 4 layers | Fixed | Anchor the crystal |
| Thermostat | Nose–Hoover per replica | Independent \(T_i\) on each replica |

**Step 2 — replica ladder.** Match temperatures to the wire's operating range, not an arbitrary MD default:

| Replica | \(T\) [K] | Wire story link |
|---------|-----------|-----------------|
| 1 | 300 | Room-temperature reference mobility |
| 2 | 380 | \(T_w\) from Part V Picard loop (Joule-heated wall) |
| 3 | 450 | Recovery onset for cold-drawn copper |
| 4 | 600 | Accelerated cross-slip sampling |
| 5 | 900 | Rare core reconstructions |

In LAMMPS, use `fix nvt` on each replica group and `fix atom/swap` or the `temper` fix for Metropolis exchange attempts every 1000 steps. Target swap acceptance 20–40% between adjacent replicas; if acceptance is below 10%, tighten the geometric spacing (e.g., use ratio \(T_{i+1}/T_i \approx 1.15\) instead of 1.25).

**Step 3 — run and monitor.** Equilibrate all replicas 100 ps at their respective \(T_i\), then enable exchanges for 10–20 ns wall time per replica.

| Observable | How to measure | Pass criterion |
|------------|----------------|----------------|
| Swap acceptance | Log `temper` output | 20–40% between neighbors |
| Cross-slip events | Track line direction (CNA or DXA) | \(\geq 1\) event per replica 4–5 trajectory |
| Core energy drift | Potential energy per atom at \(T_2\) | Stable within 2 meV/atom after 5 ns |
| Reweighted \(T = 380\,\text{K}\) density | WHAM or LAMMPS `fix wham`; verify with [`parse_wham.sh`](../../scripts/parse_wham.sh) | Converged within 5% between 10 and 20 ns |

**Step 4 — export to Part VII.** Count cross-slip events on replica 2 (\(T = 380\,\text{K}\)) using dislocation extraction (OVITO DXA or LAMMPS `compute dislocation/atom`). Before exporting rates, reweight the replica-exchange histogram at the Part V wall temperature:

```bash
# Histogram columns: T_K  E_eV_per_atom  count  (from LAMMPS fix wham or post-processed logs)
./scripts/parse_wham.sh replica_10ns.hist --target 380 --compare replica_20ns.hist
```

The script reports `wham_converged_5pct=yes` when the reweighted mean energy at 380 K is stable within 5% between 10 and 20 ns wall time — the same pass criterion in the table above. Define recovery rate

\[
\dot{n}_{\text{cs}} = \frac{N_{\text{cross-slip}}}{t_{\text{eff}} \cdot \rho_{\text{line}}},
\]

where \(t_{\text{eff}}\) is the reweighted simulation time at 380 K and \(\rho_{\text{line}}\) is dislocation line length per volume. Export to `cross_slip_380K.yaml`:

```yaml
# parallel_tempering_handoff (archive beside mobility tables)
temperature_K: 380
source: "Part V T_w from Picard loop"
replica_ladder_K: [300, 380, 450, 600, 900]
cross_slip_events: 3          # illustrative — replace with run data
effective_time_ns: 12.5
recovery_rate_m-2s-1: 1.2e14  # illustrative
potential: "EAM Cu — commit hash"
wham_converged: true
```

**Step 5 — handshake checks.**

| Check | Criterion | Failure action |
|-------|-----------|----------------|
| Temperature pedigree | Replica 2 matches Part V \(T_w \pm 5\,\text{K}\) | Re-run Picard loop; do not use 300 K tables |
| vs plain NVT | Cross-slip count at 380 K ≥ 10× plain NVT at same wall time | Increase highest replica or extend run |
| vs Part VII | Recovery rate enters forest evolution, not glide mobility alone | Split yaml: `mobility_*.yaml` vs `recovery_*.yaml` |
| vs metadynamics GSF | \(\gamma_{\text{sf}}(380\,\text{K})\) within 10% of 300 K value or refit | Run metadynamics Lab act at elevated \(T\) |

When `cross_slip_380K.yaml` sits beside `mobility_cu_screw_300K.yaml`, Part VII's hardening Lab act can distinguish **forest generation** (glide) from **forest annihilation** (cross-slip recovery) at the temperature the wire actually reaches during Act II — not an Arrhenius extrapolation from a cold shear cell.

#### WHAM → Part VII mobility hinge (Act II temperature pedigree)

The parallel tempering Lab act above is not complete until **WHAM reweighting** certifies the \(380\,\text{K}\) statistics — the same discipline as the Picard loop in [V.4 CHT](../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid): raw cold-replica time series are a **partitioned** estimate; [`parse_wham.sh`](../../scripts/parse_wham.sh) is the monolithic correction that enforces detailed balance across the replica ladder before any number crosses to OpenDiS.

| Export from WHAM (`wham_export.yaml`) | Part VII consumer | Failure if skipped |
|---------------------------------------|-------------------|---------------------|
| Reweighted mean energy at \(T_w\) | Sanity check on core structure before mobility fit | Spurious thermal expansion of the dislocation core |
| `wham_converged_5pct=yes` | Gate before archiving `cross_slip_380K.yaml` | Recovery rate from under-sampled cold replica |
| Target \(T\) matching Part V \(T_w \pm 5\,\text{K}\) | [VII.2 mobility calibration](../part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) at \(T = T_w\), not 300 K | OpenDiS runs at room temperature while the wire is at 380 K |
| Cross-slip event count at \(T_w\) | Forest **sink** term beside glide mobility in hardening yaml | Over-predicted hardening after Act II heating |

**Workflow order on the copper wire:**

```text
V.4 Picard loop  →  T_w ≈ 379 K  →  cht_export.yaml
       ↓
Replica ladder with T = T_w node  →  parallel tempering (this Lab act)
       ↓
parse_wham.sh --target T_w  →  wham_export.yaml (converged?)
       ↓
MD shear at T_w  →  mobility_cu_screw_{T_w}K.yaml  →  Part VII OpenDiS
       ↓
cross_slip_{T_w}K.yaml  →  recovery sink in forest evolution (Act IV knee)
```

Part VII's [glide mobility Lab act](../part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) supplies \(M(\tau, T)\) from NVT shear; this parallel-tempering + WHAM chain supplies **temperature-matched recovery** at the same \(T_w\) the CHT loop converged — two yaml files (`mobility_*.yaml` and `cross_slip_*.yaml`), one temperature pedigree. When [`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) runs Handshakes 1–4b, it reads `cht_export.yaml` before phonon lifetime interpolation at \(T_w\); archive `wham_export.yaml` beside `cht_export.yaml` so Handshake 4a's drag and recovery share the same wall temperature the epilogue names in Handshake 2.

```text
Part V T_w (379 K)  →  replica 2 in parallel tempering
       ↓
parse_wham.sh at T_w  →  wham_export.yaml
       ↓
Cross-slip counts at T_w  →  recovery rate in OpenDiS
       ↓
Act IV hardening knee  ←  forest ρ evolution with source + sink terms
```

### Kinetic Monte Carlo (KMC)

**Kinetic Monte Carlo** replaces continuous Newtonian integration with discrete events drawn from a rate table:

\[
P_i = \nu_i \exp(-\Delta E_i / k_B T), \qquad \text{select event } i \text{ with probability } P_i / \sum_j P_j.
\]

MD supplies the rates; KMC advances **clock time** by orders of magnitude. A copper grain boundary with vacancy exchange events can reach milliseconds where MD stops at nanoseconds — the upward path for **electromigration void growth** models that Part VI continuum damage mechanics cannot resolve atomistically.

**Scale-boundary handshake (MD → KMC → continuum).**

| Rung | Delivers | Requires |
|------|----------|----------|
| DFT (IX) | \(\Delta E_i\) for hop events | Converged SCF on initial/final states |
| MD (VIII) | Validation of \(\nu_0\), local barrier from NEB | Audited EAM or ML potential |
| KMC | Time-averaged \(\rho_{\text{vac}}(t)\), void growth | Rate table + consistent \(T\) |
| Continuum (VI) | Effective diffusivity in damage law | \(D(T)\) from Arrhenius fit to KMC/MD |

**What breaks without the handshake.** KMC with barriers from a different functional than the MD that validated \(\nu_0\) produces void growth rates wrong by exponentials — worse than any linear elasticity error. Room-temperature \(D\) from a 5 ps MSD fit plugged into a year-long creep model is the same category error at the other extreme.

### Parallel MD and domain decomposition

Production copper simulations (millions of atoms, notch root boxes) use **domain decomposition**: each MPI rank owns a spatial subdomain; ghost atoms replicate neighbor layers across rank boundaries. Force computation remains \(O(N)\) per rank with balanced load; communication cost scales with surface area of subdomain partitions.

| Concern | Practice on LAMMPS/GPUMD | Wire-scale implication |
|---------|--------------------------|------------------------|
| Load balance | `processors * * *` grid matches geometry | Long thin nanowires need aspect-aware decomposition |
| Neighbor skin | Rebuild list when any atom crosses skin | Too small → missed pairs; too large → slow rebuild |
| GPU offload | `package gpu` or native GPU codes | 10–100× speedup for EAM on large cells |
| I/O bottleneck | Dump every 1000 steps, not every step | Trajectory size dominates wall time for long NVT |

Parallel scaling does not change the **physics exports** — only how quickly you reach converged MSD, stress–strain, or Green–Kubo integrals. The reproducibility checklist still applies: same potential, same \(\Delta t\), same ensemble, documented seed, whether the run used 1 or 1024 ranks.

### Handoff summary for the copper wire

| Quantity | Source chapter | Consumer |
|----------|----------------|----------|
| \(a_0\), \(E_{\text{coh}}\) | Part IX DFT | EAM fit, sanity checks |
| \(\gamma_{\text{sf}}\), core width | Part VIII MD (this chapter) | Part VII Peierls, mobility |
| \(M(\tau, T)\) | Part VIII NVT shear | OpenDiS |
| \(E\), \(\nu\) polycrystal average | Part VIII NPT + Part VI | Part IV elastic step |

Document every conversion at the boundary: Ry → eV, Bohr → Å, metal units → SI when feeding DAMASK or Abaqus.

## Lab act: EAM-fit audit before the notch MD run (Act V — Notch)

**Act V** concentrates stress at the notch root where dislocation nucleation begins. Before launching a million-atom LAMMPS run, this Lab act **audits** the EAM potential against the DFT pedigree checklist — the same contract Part IX will enforce from first principles.

For fcc Cu, minimum acceptance tests on a 500-atom NPT cell at 300 K:

| Test | EAM target | Pass criterion | Failure action |
|------|------------|----------------|----------------|
| Lattice constant \(a_0\) | DFT Murnaghan minimum (IX.1) | \(|a_{\text{EAM}} - a_{\text{DFT}}| < 0.01\,\text{Å}\) | Refit embedding/density functions |
| Cohesive energy | DFT \(E_{\text{coh}}\) per atom | Within 5% | Check cutoff radius and fitting set |
| \(C_{11}\) | DFT elastic constant | Within 10% via small-strain NPT | Add compressed/stretched configs to fit set |
| Stacking fault \(\gamma_{\text{sf}}\) | DFT generalized SF surface | Same order of magnitude at intrinsic fault | Part VII partial separation wrong if this fails |
| Melting point (optional) | Experiment ~1358 K | EAM within ~100 K | Note if high-\(T\) creep studies are planned |

Run a **short** NVT shear cell (\(\dot\gamma \sim 10^8\,\text{s}^{-1}\)) to extract a trial \(M(\tau)\) curve for OpenDiS. Document metal units → SI conversion in `units.txt` beside the handoff bundle from [VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md).

If any row fails, do **not** proceed to notch nucleation MD — fix the potential or train a DeepMD model on DFT snapshots (table in this chapter). The notch root is where EAM cutoff artifacts and wrong \(\gamma_{\text{sf}}\) first appear as spurious dislocation loops; Act V is too expensive to run on an un-audited surface.

## Concept map checkpoint (Part VIII)

Part VIII followed the MD Notes from phase space through coarse-graining. The four questions summarize the atomistic arc:

| Question | Part VIII answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Positions \(\{\mathbf{r}_i\}\), momenta, interatomic potential \(V\) |
| What **structure**? | Hamiltonian mechanics, thermostats, periodic boundaries, cutoff radius |
| What **theorem**? | Energy conservation (symplectic integrators); ergodic sampling in NVT/NPT |
| What **breaks**? | Energy drift; wrong ensemble; cutoff artifacts in EAM fits |

The handoff table above closes the upward exports from atomistics: stacking-fault energy and core structures feed Part VII mobility; cohesive energy and moduli feed Part VI and Part IV elastic steps. What MD cannot invent — the potential surface itself — is Part IX's responsibility. Classical MD assumes Born–Oppenheimer surfaces; the next part derives them from electron density.

## Intermission: atomistics end, electronics begin {#intermission-atomistics-ends-electronics-begin}

If you have read linearly since [Part VII's intermission](../part07-defects/03-polycrystal-and-fem-handoff.md#intermission-mesoscale-ends-atomistics-begin), Part VIII was the second descent — vibrating nuclei replacing line cutoffs. This chapter is the **last atomistic stop** before electrons enter explicitly: it exports EAM parameters and mobility yaml the mesoscale codes consume, and names every quantity that still hides in **electronic structure** MD cannot derive.

The three signals from Part VI reappear here with atomistic vocabulary answered and electronic vocabulary deferred: **history** (EAM-fit audit replaces blind literature potentials); **rate** (NVT shear supplies \(M(\tau,T)\) with temperature pedigree); **notch** (the Lab act above gates million-atom nucleation runs). Part IX resolves the deferred signal — cohesive energy, \(C_{ij}\), \(\gamma_{\text{sf}}\), vacancy \(E_f\) — without asking you to leave the wire on the bench. The specimen does not change; only the state variable does.

When EAM matches bulk moduli but no one cites a DFT input deck, the plot turns downward one last time: [Part IX's third descent rung](../part09-dft/00-opening.md#third-descent-rung-viii-midpoint-reunion) is where trajectories become self-consistent electron density.

## Bridge to Part IX {#bridge-to-part-ix}

Classical MD is the workhorse; ab initio MD and QM/MM are the auditors when potentials fail. Coarse-graining and fitting are how Part VIII **hands numbers upward** to DDD and FEM and **requests truth downward** from electronic structure. Part IX makes that downward request precise: the Hohenberg–Kohn theorems, the Kohn–Sham equations, and the Quantum ESPRESSO-style workflows that turn a copper crystal into cohesive energy, elastic constants, and the potential datasets MD cannot invent.

The EAM-fit checklist and handoff table above already named the quantities MD exports upward. Part IX re-derives each from electron density \(\rho(\mathbf{r})\):

| Quantity | Part VIII role (this chapter) | Part IX re-derivation |
|----------|-------------------------------|------------------------|
| \(E_{\text{coh}}\) | Sanity check on EAM fit; bulk modulus anchor | Total energy per atom from converged SCF on fcc Cu |
| \(C_{ij}\) (elastic constants) | NPT stress–strain vs DFT \(C_{11}\) | Small-strain energy derivatives w.r.t. lattice strain |
| \(\gamma_{\text{sf}}\) | Stacking-fault energy for partial dislocations | Generalized stacking-fault energy surface from slab calculations |
| \(E_f^v\) (vacancy formation) | Diffusion and creep parameters at high \(T\) | Supercell with one removed atom; total-energy difference |

**Scale-boundary handshake (VIII.3 → Part IX → epilogue).**

| MD export (this chapter) | DFT audit gate (Part IX) | Upstream consumer | Failure mode |
|----------------------------|--------------------------|-------------------|--------------|
| EAM-fit \(a_0\), \(E_{\text{coh}}\) | Murnaghan SCF vs volume (`pw.x`) | LAMMPS equilibrium box (Act V notch) | Bulk-fit wrong at dislocation core |
| \(\gamma_{\text{sf}}\) from slab pulls | GSF surface from [IX.3](../part09-dft/03-dft-workflows.md) | Part VII partial separation \(d\) | 10% \(\gamma_{\text{sf}}\) error shifts hardening curve |
| \(C_{11}, C_{12}\) from NPT | Strained fcc cells (±0.5% uniaxial) | Part IV elastic step; Part VI \(\mathbb{C}\) | Wrong functional for elastic constants |
| Trial \(M(\tau)\) from shear cell | NEB barrier from DFT endpoints | OpenDiS mobility yaml | Mixing potentials across rungs |
| KMC rate table from NEB | \(\Delta E_m\) converged in SCF | Part VI creep at high \(T\) | Barriers from different functional than MD |

Part VIII assumed Born–Oppenheimer surfaces and fit potentials to match these numbers. Part IX is the **audit chapter** — the same copper cell Part VIII vibrated, now solved for \(\rho(\mathbf{r})\) before the epilogue climbs back up the ladder. See also the [two clocks note](../part08-md/00-opening.md#two-clocks-reading-order-vs-foundation-pedigree): chapter order descends VII → VIII → IX; workflow order builds input decks IX → VIII → VII → IV.

Return to the [prologue](../../prologue/00-many-scales.md): **Act V — Notch** is where the EAM-fit audit Lab act above must pass before million-atom nucleation runs; **Act VI — Foundation** is where someone chose Young's modulus, stacking-fault energy, and a mobility table before any wire-scale FEM run — parameters whose pedigree this chapter traced to EAM fits and coarse-grained exports. Part IX re-derives each from first principles so the ladder has a floor, not folklore. The [Part IX opening](../part09-dft/00-opening.md) frames that descent explicitly; [IX.1](../part09-dft/01-born-oppenheimer.md) separates fast electrons from slow nuclei before the Kohn–Sham machinery begins.

### Pedigree checklist before the epilogue

Linear readers should carry this checklist into Part IX — each row is a **contract** the epilogue's multiscale afternoon will ask you to honor:

| Export upward | Minimum DFT evidence (Part IX) | Typical MD use (Part VIII) |
|---------------|-------------------------------|----------------------------|
| Lattice parameter \(a_0\) | SCF energy vs volume (Murnaghan fit) | EAM equilibrium box in LAMMPS |
| \(E_{\text{coh}}\) | Total energy per atom at equilibrium | Bulk modulus sanity check on EAM |
| \(C_{11}, C_{12}\) | Strained fcc cells (±0.5% uniaxial) | NPT elastic response vs DFT |
| \(\gamma_{\text{sf}}\) | Relaxed stacking-fault slab | Partial dislocation separation in DDD |
| \(E_f^v\) | 3×3×3 supercell, one vacancy removed | Diffusion/creep at high \(T\) |

If a row in your project folder has only "EAM fit to experiment" with no QE `pw.x` log, Part IX is the audit chapter that closes the loop. Part II taught that honest FEM requires a convergence target in \(H^1\); Part IX teaches that honest multiscale mechanics requires a **convergence target in SCF energy** — same instinct, finer rung.

Turn the page when the EAM potential matches bulk moduli but no one can cite the DFT input deck that produced it — that is the signal the foundation run is missing, and Part IX is where the audit starts.
