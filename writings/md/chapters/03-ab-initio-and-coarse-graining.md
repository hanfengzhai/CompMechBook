# Ab Initio MD, Coarse-Graining, and the Ladder Upward

Classical molecular dynamics of Part VIII assumes nuclei move on a **potential energy surface** — usually empirical (EAM) or fitted to quantum data. This chapter closes the atomistic part by making that assumption explicit: **Born–Oppenheimer ab initio MD** computes forces from DFT each timestep; **coarse-graining** and **potential fitting** translate DFT landscapes into EAM tables DDD and production MD can afford.

The copper wire at laboratory scale will never be a full DFT supercell. The wire at atomic scale **must** be described quantum mechanically when bonds rearrange, chemistry appears, or empirical potentials have never been validated. The art is knowing when ab initio MD is mandatory, when classical MD suffices, and how to compress atomistic trajectories into numbers the mesoscale accepts.

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

## Worked example: fitting EAM for copper (checklist)

Mirror the Part IX Quantum ESPRESSO discipline with an explicit copper workflow. The goal is a LAMMPS-ready EAM file that reproduces bulk moduli **and** one generalized stacking-fault (GSF) curve along \(\langle 111\rangle\{111\}\) slip.

| Step | Action | Target / pass criterion |
|------|--------|-------------------------|
| 1 | DFT relax fcc Cu (`vc-relax`), record \(a_0\), \(E_{\text{coh}}\) | \(a_0 \approx 3.61\) Å (PBE typical) |
| 2 | DFT elastic constants \(C_{11}, C_{12}, C_{44}\) (small strains) | Symmetric stiffness matrix |
| 3 | DFT GSF: rigidly shift half-crystals along slip plane | \(\gamma_{\text{sf}} \approx 45\) mJ/m² (functional-dependent) |
| 4 | DFT vacancy formation energy \(E_f^v\) in supercell | Compare to experiment ~1.17 eV |
| 5 | Choose EAM functional form (Finnis–Sinclair or DYNAMO-style) | Cutoff \(\sim 5\)–\(6\) Å for Cu |
| 6 | Optimize weights on bulk + GSF + \(E_f^v\) (force matching on snapshots optional) | Weight GSF ≥ bulk if DDD mobility is the consumer |
| 7 | Validate: phonon at \(\Gamma\), melt test (qualitative), screw dislocation core relaxation | No imaginary phonons; core width sensible |
| 8 | Export `.eam.alloy` or `.eam.fs` and archive DFT inputs | Version-control alongside manuscript |

Step 6 is where teams disagree: a potential that nails \(B\) but misses \(\gamma_{\text{sf}}\) by 30% will mis-predict Peierls stress in Part VII. When in doubt, **prioritize configurations the wire actually visits** — faulted planes, surfaces, compressed cores — over perfect-lattice EOS alone.

## Minimal LAMMPS deck (EAM copper)

After Step 8, a sanity-check NVT run on fcc Cu at 300 K:

```lammps
units           metal
atom_style      atomic
boundary        p p p

lattice         fcc 3.615
region          box block 0 20 0 20 0 20
create_box      1 box
create_atoms    1 box

pair_style      eam/alloy
pair_coeff      * * Cu_u3.eam.alloy Cu

mass            1 63.546
velocity        all create 300.0 12345

fix             1 all nvt temp 300 300 0.1
thermo          100
run             10000
```

Replace `Cu_u3.eam.alloy` with your fitted file. Compare:

- relaxed lattice parameter vs. DFT \(a_0\),
- mean pressure in NPT (not shown) vs. zero,
- cohesive energy per atom vs. DFT.

Then run a **screw dislocation** periodic cell (Part VII preview): if the core spreads or collapses unphysically, return to Step 6 with core configurations in the training set — do not patch mobility laws in DDD to compensate for a bad potential.

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

**Neural network potentials** (Behler–Parrinello, DeepMD, etc.) interpolate DFT data with near-DFT accuracy at MD cost after training. A typical copper workflow:

1. **Initial DFT pool**: bulk fcc, compressed/dilated cells, vacancy, surface (111), GSF points, small amorphous clusters.
2. **Active learning loop**: run short LAMMPS/DeepMD probes; where force uncertainty exceeds a threshold, add that configuration to the DFT pool and retrain.
3. **Train** on energies and forces (weighted; forces often dominate for dynamics).
4. **Deploy** in LAMMPS via `pair_style deepmd` or PyTorch interface; benchmark against held-out DFT configs before exporting mobilities to DDD.

| Stage | Tooling | Output for the wire story |
|-------|---------|---------------------------|
| DFT reference | Quantum ESPRESSO / VASP | Labeled \((\mathbf{R}, E, \mathbf{F})\) sets |
| Dataset curation | ASE, dpdata | Train/validation splits with functional labels |
| Training | DeePMD-kit, NequIP | Frozen model + metadata JSON |
| Production MD | LAMMPS + plugin | Core structures, \(\gamma_{\text{sf}}\), fracture trajectories |
| Upward export | Post-processing scripts | Mobility tables, Peierls estimates for OpenDiS |

For multiscale copper studies, ML potentials increasingly replace hand-tuned EAM when **reactive** or **complex** configurations matter — notched fracture, oxidation at the surface, or alloy additions to the wire. The ladder logic is unchanged: electronic structure defines the surface; atomistics explores it; mesoscale inherits statistics. ML does not remove Part IX; it **amplifies** how much of the DFT landscape classical MD can faithfully visit.

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

## Bridge to Part IX

Classical MD is the workhorse; ab initio MD and QM/MM are the auditors when potentials fail. Coarse-graining and fitting are how Part VIII **hands numbers upward** to DDD and FEM and **requests truth downward** from electronic structure. Part IX makes that downward request precise: the Hohenberg–Kohn theorems, the Kohn–Sham equations, and the Quantum ESPRESSO-style workflows that turn a copper crystal into cohesive energy, elastic constants, and the potential datasets MD cannot invent.
