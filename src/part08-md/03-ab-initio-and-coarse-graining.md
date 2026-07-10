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

### Handoff summary for the copper wire

| Quantity | Source chapter | Consumer |
|----------|----------------|----------|
| \(a_0\), \(E_{\text{coh}}\) | Part IX DFT | EAM fit, sanity checks |
| \(\gamma_{\text{sf}}\), core width | Part VIII MD (this chapter) | Part VII Peierls, mobility |
| \(M(\tau, T)\) | Part VIII NVT shear | OpenDiS |
| \(E\), \(\nu\) polycrystal average | Part VIII NPT + Part VI | Part IV elastic step |

Document every conversion at the boundary: Ry → eV, Bohr → Å, metal units → SI when feeding DAMASK or Abaqus.

## Concept map checkpoint (Part VIII)

Part VIII followed the MD Notes from phase space through coarse-graining. The four questions summarize the atomistic arc:

| Question | Part VIII answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Positions \(\{\mathbf{r}_i\}\), momenta, interatomic potential \(V\) |
| What **structure**? | Hamiltonian mechanics, thermostats, periodic boundaries, cutoff radius |
| What **theorem**? | Energy conservation (symplectic integrators); ergodic sampling in NVT/NPT |
| What **breaks**? | Energy drift; wrong ensemble; cutoff artifacts in EAM fits |

The handoff table above closes the upward exports from atomistics: stacking-fault energy and core structures feed Part VII mobility; cohesive energy and moduli feed Part VI and Part IV elastic steps. What MD cannot invent — the potential surface itself — is Part IX's responsibility. Classical MD assumes Born–Oppenheimer surfaces; the next part derives them from electron density.

## Bridge to Part IX

Classical MD is the workhorse; ab initio MD and QM/MM are the auditors when potentials fail. Coarse-graining and fitting are how Part VIII **hands numbers upward** to DDD and FEM and **requests truth downward** from electronic structure. Part IX makes that downward request precise: the Hohenberg–Kohn theorems, the Kohn–Sham equations, and the Quantum ESPRESSO-style workflows that turn a copper crystal into cohesive energy, elastic constants, and the potential datasets MD cannot invent.

The EAM-fit checklist and handoff table above already named the quantities MD exports upward. Part IX re-derives each from electron density \(\rho(\mathbf{r})\):

| Quantity | Part VIII role (this chapter) | Part IX re-derivation |
|----------|-------------------------------|------------------------|
| \(E_{\text{coh}}\) | Sanity check on EAM fit; bulk modulus anchor | Total energy per atom from converged SCF on fcc Cu |
| \(C_{ij}\) (elastic constants) | NPT stress–strain vs DFT \(C_{11}\) | Small-strain energy derivatives w.r.t. lattice strain |
| \(\gamma_{\text{sf}}\) | Stacking-fault energy for partial dislocations | Generalized stacking-fault energy surface from slab calculations |
| \(E_f^v\) (vacancy formation) | Diffusion and creep parameters at high \(T\) | Supercell with one removed atom; total-energy difference |

Part VIII assumed Born–Oppenheimer surfaces and fit potentials to match these numbers. Part IX is the **audit chapter** — the same copper cell Part VIII vibrated, now solved for \(\rho(\mathbf{r})\) before the epilogue climbs back up the ladder. See also the [two clocks note](../part08-md/00-opening.md#two-clocks-reading-order-vs-foundation-pedigree): chapter order descends VII → VIII → IX; workflow order builds input decks IX → VIII → VII → IV.

Return to the prologue's **Act VI — Foundation**: before any wire-scale FEM run, someone chose Young's modulus, stacking-fault energy, and a mobility table — parameters whose pedigree this chapter traced to EAM fits and coarse-grained exports. Part IX re-derives each from first principles so the ladder has a floor, not folklore. The [Part IX opening](../part09-dft/00-opening.md) frames that descent explicitly; [IX.1](../part09-dft/01-born-oppenheimer.md) separates fast electrons from slow nuclei before the Kohn–Sham machinery begins.

| Prologue act | Part VIII assumed on trust | Part IX audit target |
|--------------|---------------------------|----------------------|
| VI — Foundation | \(E_{\text{coh}}\), \(a_0\) in EAM fit | Converged SCF total energy per atom |
| IV — Hardening | \(\gamma_{\text{sf}}\) for partial dislocations | Generalized stacking-fault surface from slabs |
| V — Notch | Vacancy/interstitial formation for creep | Supercell defect energies with archived k-mesh |
| III — Pulling | Elastic constants \(C_{ij}\) in the mesh | Small-strain derivatives w.r.t. lattice strain |

Turn the page when the EAM potential matches bulk moduli but no one can cite the DFT input deck that produced it — that is the signal the foundation run is missing, and Part IX is where the audit starts.
