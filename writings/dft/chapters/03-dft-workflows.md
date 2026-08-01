# DFT Workflows: From Input Files to Multiscale Numbers

Part IX, Chapters 1–2, derived the Kohn–Sham equations and explained why convergence matters. This chapter closes the electronic-structure arc with **practice**: how a DFT calculation is staged, verified, and translated into numbers that upstream parts of this book consume — elastic moduli for Part VI, cohesive energies for Part VIII potentials, surface and vacancy energies for Part VII defect thermodynamics.

The narrative thread remains the copper wire. We will not simulate the whole wire in Quantum ESPRESSO — no cluster has that memory — but we **will** walk through the same workflows used to produce the bulk properties that a wire model assumes: lattice constant, bulk modulus, elastic tensor, phonon check, and defect formation energy in a supercell. The homework archive for Cornell MSE 5720 ([MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW)) supplies worked examples; this chapter distills their logic into a reproducible ritual.

## Scene: bulk copper in a workstation

No cluster will ever run DFT on the full wire. Instead, a small fcc supercell on a workstation yields lattice constant, bulk modulus, elastic constants, vacancy formation energy — the bulk numbers every upstream model assumes. Input files, cutoff convergence, k-mesh tests, relaxation, SCF cycle, property extraction: this chapter is the repeatable ritual that turns Quantum ESPRESSO output into parameters for Parts VI–VIII.

## The calculation ladder inside DFT

Every property calculation is a sequence of controlled approximations:

```
Pseudopotential + functional  →  Cutoff & k-mesh convergence  →  Geometry relaxation
        →  Self-consistent field  →  Property extraction  →  Uncertainty & archiving
```

Skipping a rung produces pretty numbers with no contract to physics. The SCF cycle from Chapter 2 sits in the middle; **everything before it** sets the discretization of electron space; **everything after** exports to MD and continuum.

| Stage | Question answered | Failure symptom |
|-------|-------------------|-----------------|
| Pseudo + XC choice | Which electrons, which exchange–correlation model? | Systematic bias vs experiment |
| \(E_{\text{cut}}\), k-mesh | Is plane-wave / Brillouin-zone sampling adequate? | Energy drifts when grid refined |
| Relaxation | Are nuclei at mechanical equilibrium? | Spurious forces, wrong \(a_0\) |
| SCF | Is the density self-consistent? | Oscillating total energy |
| Property | What derivative / response is needed? | Noisy forces, imaginary phonons |

Treat this table like the convergence checklist in Part IV for mesh refinement — same intellectual habit, different parameters.

## HW1 pattern: convergence before trust (BAs example)

Homework 1 in MSE5720 uses boron arsenide (BAs) as a clean semiconductor example; the **workflow** transfers directly to fcc copper:

1. **Fix pseudopotentials** (ultrasoft or PAW) and functional (PBE is the common default; document the choice).
2. **Sweep plane-wave cutoff** \(E_{\text{cut}}\) at fixed k-mesh; plot total energy vs cutoff until changes fall below a tolerance (5 meV/atom is a typical homework criterion).
3. **Sweep k-point density** at converged cutoff; Monkhorst–Pack grids must respect symmetry.
4. **`vc-relax` or `relax`**: optimize lattice parameters and atomic positions until forces \(\|\mathbf{F}_I\| < \tau_F\).
5. **Extract bulk modulus**: series of `scf` calculations on isotropically scaled volumes; fit energy–volume data to a Birch–Murnaghan or similar equation of state (EOS).

For copper (fcc, 1 atom per primitive cell in some setups, more in conventional cell), the relaxed lattice constant should match experiment within a few percent for GGA-PBE — **systematic**, not tuned. If DFT gives \(a = 3.55\) Å vs experimental \(3.61\) Å, record the gap; do not silently force experimental values into a DFT-derived potential fit without documenting the strain offset.

### Parsing output and automation

Production workflows script the sweeps:

```bash
# Illustrative: cutoff convergence (Quantum ESPRESSO pw.x)
for ecut in 40 50 60 70 80; do
  sed "s/ecutwfc = .*/ecutwfc = $ecut/" template.in > run.in
  mpirun -np 4 pw.x < run.in > run_${ecut}.out
  grep "!" run_${ecut}.out | awk '{print ecut, $5}' >> energy_vs_ecut.dat
done
```

Archive **inputs, outputs, pseudopotential files, and code version**. Reproducibility is the multiscale contract: MD in Part VIII cannot cite "DFT said so" without a commit hash.

## Worked example: fcc copper from `pw.in` to elastic constants

The BAs homework pattern above is generic; this section walks **copper** end to end — the same material whose Young's modulus appears in Part VI and whose EAM fit is checked in Part VIII. We use Quantum ESPRESSO (`pw.x`) with PBE and ultrasoft pseudopotentials; the deck is abbreviated but complete enough to archive in a repository.

### Step 0 — Primitive cell and pseudopotential

Copper is fcc with one atom in the conventional cell (4 atoms) or one atom in the primitive cell. For bulk modulus and elastic constants, either works if Brillouin-zone sampling is consistent. Download `Cu.pbe-d-v1.0.uspp.F.UPF` from the [SSSP library](https://www.materialscloud.org/discover/sssp) or the Quantum ESPRESSO pseudopotential table; record the hash.

```text
&CONTROL
  calculation = 'vc-relax'
  prefix      = 'cu_bulk'
  pseudo_dir  = './pseudo/'
  outdir      = './tmp/'
  forc_conv_thr = 1.0d-4
/
&SYSTEM
  ibrav = 2
  celldm(1) = 6.80   ! initial guess; Å via celldm(1)*bohr_to_ang
  nat   = 1
  ntyp  = 1
  ecutwfc = 50       ! will sweep; Ry
  occupations = 'smearing'
  smearing = 'mp'
  degauss = 0.02
/
&ELECTRONS
  conv_thr = 1.0d-8
  mixing_beta = 0.3
/
&IONS
  ion_dynamics = 'bfgs'
/
ATOMIC_SPECIES
  Cu  63.546  Cu.pbe-d-v1.0.uspp.F.UPF
ATOMIC_POSITIONS crystal
  Cu  0.0  0.0  0.0
K_POINTS automatic
  12 12 12  0 0 0
```

Run `vc-relax` first; extract converged `celldm(1)` and total energy per atom. For PBE, expect \(a \approx 3.63\text{–}3.66\) Å vs experimental \(3.615\) Å — close enough to trust **trends**, not to force experimental \(a_0\) into a DFT-derived potential without documenting strain.

### Step 1 — Cutoff and k-mesh convergence (archive the curves)

Fix the relaxed lattice constant. Sweep `ecutwfc` at fixed `12 12 12` k-mesh; then sweep k-density at converged cutoff. Tabulate:

| `ecutwfc` (Ry) | \(E/N\) (Ry/atom) | \(\Delta E\) (meV/atom) |
|----------------|-------------------|-------------------------|
| 40 | (run) | — |
| 50 | (run) | (run) |
| 60 | (run) | (run) |
| 70 | (run) | (run) |

Stop when successive \(\Delta E < 5\) meV/atom. Repeat for k-mesh (`8×8×8`, `12×12×12`, `16×16×16`). **Plot both curves** in the study README — the epilogue's multiscale chain is only as honest as these plots.

### Step 2 — Equation of state and bulk modulus

With converged settings, run a series of `scf` jobs on isotropically scaled volumes \(V(\eta) = (1+\eta) V_0\) for \(\eta \in \{-0.04, -0.02, 0, 0.02, 0.04\}\). Fit \(E(V)\) to Birch–Murnaghan; extract \(B\) in GPa. Compare to experiment (\(B \approx 140\) GPa for Cu). Discrepancy is functional error, not a reason to hide the DFT value.

### Step 3 — Elastic constants via stress–strain

Apply small strains to the relaxed cell (±0.005 is typical). For cubic Cu, three independent deformations suffice (uniaxial, shear, volume-preserving). After each `vc-relax` or fixed-cell `scf` with `tprnfor = .true.`, read stresses and fit

\[
C_{11} = \frac{\partial \sigma_1}{\partial \varepsilon_1}\Big|_{\varepsilon=0}, \quad
C_{12} = \frac{\partial \sigma_1}{\partial \varepsilon_2}\Big|_{\varepsilon=0}, \quad
C_{44} = \frac{\partial \sigma_6}{\partial \varepsilon_6}\Big|_{\varepsilon=0}.
\]

Voigt averages give Young's modulus and Poisson's ratio for isotropic polycrystal estimates in Part VI:

\[
E = \frac{9B G}{3B + G}, \qquad \nu = \frac{3B - 2G}{2(3B + G)},
\]

with \(G = (C_{11} - C_{12} + 3C_{44})/5\) for cubic crystals. A typical PBE result: \(C_{11} \approx 170\) GPa, \(C_{12} \approx 120\) GPa, \(C_{44} \approx 75\) GPa — bracketing but not matching room-temperature experiment.

### Step 4 — Vacancy supercell (handoff to Part VII)

Build a \(3\times3\times3\) conventional cell (108 atoms). Remove one atom; relax with fixed cell shape. Formation energy:

\[
E_f^v = E_{107} - \frac{107}{108} E_{108}.
\]

Converge with respect to supercell size and k-mesh. Archive \(E_f^v\) alongside the bulk \(a_0\) and \(C_{ij}\) — Part VII's defect thermodynamics and Part VIII's EAM fitting both consume this number.

### Step 5 — Export table for upstream parts

| Quantity | Typical PBE value | Used in |
|----------|-------------------|---------|
| \(a_0\) | 3.63–3.66 Å | Part VI reference configuration |
| \(B\) | 130–145 GPa | Part VI bulk response |
| \(C_{11}, C_{12}, C_{44}\) | see above | Part IV anisotropic elements |
| \(E_f^v\) | 1.0–1.3 eV | Part VII, Part VIII |
| Phonon DOS (optional `ph.x`) | acoustic branch at \(\Gamma\) | Part VIII thermostat validation |

Commit the converged `pw.in`, pseudopotential, and a one-page README with functional, cutoffs, and final numbers. That commit hash is what you cite when the copper wire FEM model uses \(E = 120\) GPa — not a vague "DFT said so."

## HW2 pattern: bands, DOS, and elasticity (Si extended to metals)

Homework 2 explores silicon: projected density of states (s/p/d character), band structure along high-symmetry paths, and elastic constants from stress–strain linear response. For **copper**, the same machinery applies with metal-specific care:

- **Smearing**: occupations are fractional at the Fermi level; Gaussian or Methfessel–Paxton smearing prevents SCF oscillations. Too little smearing → noisy convergence; too much → blurred Fermi surface.
- **Dense k-meshes** for density integrations; coarser meshes sometimes suffice for band plots along paths (`bands.x`, `nscf` with fixed potential from prior `scf`).
- **Elastic tensor**: apply small strains \(\pm\delta\) to the cell, compute stress via DFT (or use DFPT if available); fit \(C_{ijkl}\). Voigt notation maps to Young's modulus and Poisson's ratio used in Part VI.

Compare DFT \(C_{ijkl}\) to Part VIII MD estimates via fluctuation formulas at finite temperature — they should bracket experiment, not duplicate it exactly (anharmonicity, finite-T effects).

Phonon calculations (`ph.x`, `q2r.x`, `matdyn.x` in the HW2 scripts) linearize DFT around equilibrium. **Imaginary frequencies** signal instability — wrong structure, bad k-mesh, or a phase that is not the ground state. For copper at equilibrium, acoustic branches should pass through zero at \(\Gamma\); optical modes lie at higher frequency. Phonon DOS validates MD thermostats and thermal conductivity estimates downstream.

## HW3 pattern: phase stability under pressure

Homework 3 pushes silicon through pressure-induced phase transitions — diamond vs \(\beta\)-Sn structure — by comparing **enthalpies** \(H = E + PV\) at competing phases. The critical pressure where enthalpies cross (order 10 GPa in the homework narrative) is a DFT prediction testable against experiment.

Copper's fcc structure is stable under ambient wire-drawing conditions, but the lesson generalizes: **when multiple polymorphs compete**, total energy alone misleads at finite pressure. Multiscale models of manufacturing (rolling, drawing) that change texture and defect density sometimes approach phase boundaries in alloyed systems — DFT enthalpy curves are the sanity check.

Phonon dispersion at strained volumes (HW3's \(\pm 5\%\) volume perturbations) probes **mechanical stability**: soft modes foreshadow structural transitions. Link this to Part VI's tangent stiffness: a negative eigenvalue in the elastic stiffness tensor is the continuum hint of an unstable lattice mode.

## HW4 pattern: vibrational spectroscopy and disorder

Homework 4 on calcite demonstrates zone-center phonons, mode intensities, and disordered structures — spectroscopy-facing output. For metals, analogous workflows support:

- **Infrared/Raman inactive** bulk modes but **surface** and **defect** vibrational signatures in nanostructured wires.
- **Disordered** or **alloyed** cells (substitutional defects) requiring larger supercells and careful averaging.

Disorder connects to the drawn wire's polycrystalline texture: bulk single-crystal DFT moduli averaged with Voigt/Reuss bounds (Part VI homogenization preview) approximate effective properties — with error bars when texture is strong.

## Defect calculations: vacancy in copper

Export a number Part VII needs: **vacancy formation energy**

\[
E_f^v = E(N-1) - \frac{N-1}{N}\,E(N),
\]

in a supercell with \(N\) atoms, fully relaxed with fixed cell shape or `vc-relax` depending on boundary conditions. Convergence requires:

- Supercell size increase until \(E_f^v\) stabilizes (images of the vacancy interacting through periodic boundaries).
- k-mesh refinement with cell size.
- Chemical potential reference if vacancies exchange atoms with a reservoir (more relevant for open systems).

Compare to experiment (~1.17 eV for Cu at 0 K, order-of-magnitude) and to EAM/MEAM values used in Part VIII MD. Discrepancy is not failure — it documents functional and pseudo error budgets.

## Worked example: generalized stacking-fault energy (handoff to Part VII)

Part VII's dislocation dynamics consumed a **stacking-fault energy** \(\gamma_{\text{sf}}\) when partial dislocations separated on {111} planes — the energy cost of making a faulted region one atomic layer thick. That number entered mobility tables and hardening curves without a full derivation. Here we close the loop: DFT computes \(\gamma_{\text{sf}}\) from first principles, and Part VII imports it with a pedigree.

### The faulted-supercell construction

Copper is fcc. A stacking fault on {111} shifts every plane above the cut by a partial Burgers vector \(\mathbf{b}_p = \mathbf{a}/6\langle 112\rangle\), creating a local hcp-like stacking sequence (ABC**A**BC instead of ABCABC). The **generalized stacking-fault (GSF) surface** \(\gamma(\mathbf{u})\) maps shear displacement \(\mathbf{u}\) in the fault plane to energy per unit area; the value at the unstable stacking fault (USF) configuration sets the Peierls barrier scale, and the value at the stable fault (SF) configuration is the quantity DDD codes tabulate.

For a first-principles estimate of the stable fault energy:

1. **Build a slab supercell** with at least 12–16 atomic layers along [111], separated by vacuum (or use periodic images with sufficient layer count to suppress interaction).
2. **Cut and shift** the upper half of the slab by the stable-fault displacement — typically implemented as a rigid shift followed by atomic relaxation in the fault plane only (fix bottom layers, relax top layers).
3. **Run `relax` or `vc-relax`** with fixed in-plane cell vectors; total energy minus the perfect-crystal reference gives fault energy.
4. **Divide by fault area** \(A = |\mathbf{a}_1 \times \mathbf{a}_2|\) in the {111} plane.

```text
E_gsf = (E_faulted - E_perfect) / A_fault    [eV/Å²]
γ_sf  = E_gsf × (16.02 / 1.602)             [mJ/m²]
```

The unit conversion (eV/Å² → mJ/m²) is a recurring arithmetic trap — archive the conversion factor in the README beside the raw numbers.

### Convergence checklist specific to GSF

| Parameter | Typical starting value (Cu {111}) | Convergence test |
|-----------|-----------------------------------|------------------|
| Slab layers | 12–16 along [111] | Double layer count; \(\gamma_{\text{sf}}\) should stabilize within 5% |
| k-mesh in plane | \(12 \times 12 \times 1\) Monkhorst–Pack | Increase to \(16 \times 16 \times 1\) |
| Vacuum gap (if non-periodic) | 10–15 Å | Double gap; energy change < 1 meV/atom |
| Relaxation depth | Top 4–6 layers free | Compare to full-slab relaxation |
| Functional | PBE (document choice) | Compare to LDA or SCAN if time permits |

Under-converged slabs produce \(\gamma_{\text{sf}}\) that drifts with layer count — the DFT analogue of a DDD simulation whose box is too small for image forces to decay. Part VII's [Lab act on forest hardening](../part07-defects/02-dislocation-dynamics.md) assumed a tabulated \(\gamma_{\text{sf}}\); this workflow is where that table entry should originate.

### Full GSF curve (optional but illuminating)

A single stable-fault energy is enough for DDD mobility tables, but the **full \(\gamma(\mathbf{u})\) curve** explains why partials dissociate and how cross-slip competes with glide. Sweep in-plane displacements \(\mathbf{u} = \alpha \mathbf{b}_p\) for \(\alpha \in [0, 1]\) (and beyond for the unstable fault):

| \(\alpha\) | Physical meaning | Expected energy trend (Cu) |
|------------|------------------|----------------------------|
| 0 | Perfect crystal | \(\gamma = 0\) (reference) |
| 0.5 | Unstable stacking fault (USF) | Local maximum (~200–300 mJ/m² for Cu) |
| 1.0 | Stable intrinsic fault | Local minimum (~40–50 mJ/m² for Cu, experiment ~45) |

Plot \(\gamma(\alpha)\) and archive the curve — Part VII's partial-dislocation separation width scales as \(\propto \mu \mathbf{b}_p / \gamma_{\text{sf}}\), and the USF peak sets the barrier for cross-slip during cold drawing. When the epilogue wires DFT → MD → DDD → FEM, this curve is the **first handshake** between electronic structure and line-defect mechanics.

### Bridge table: DFT GSF → Part VII DDD

| DFT export | Part VII consumer | Copper wire context |
|------------|-------------------|---------------------|
| \(\gamma_{\text{sf}}\) at stable fault | Partial separation width in DDD | Cold-drawn wire's forest density |
| \(\gamma_{\text{USF}}\) at unstable fault | Cross-slip activation scale | Recovery annealing kinetics |
| \(\mathrm{d}^2\gamma/\mathrm{d}u^2\) at minimum | Dislocation core structure models | Notch tip plastic zone size |
| Full \(\gamma(\mathbf{u})\) surface | Mobility law fitting in DDD | Work-hardening curve in Act IV |

If your project folder contains `cu.gsf/` with converged slab calculations but Part VII's DDD input still cites "literature value 45 mJ/m²" without a path, **Act VI is incomplete** — the downward derivation stopped one rung above where it should have.

## From DFT outputs to the rest of the book

| DFT workflow output | Used in | Copper wire context |
|---------------------|---------|---------------------|
| \(a_0\), \(B\) | Part VI elasticity | Stiffness in tension test FEM |
| \(C_{ijkl}\) | Part VI, IV anisotropic elements | Texture-dependent moduli |
| \(E_f^v\), \(E_f^s\) (surface) | Part VII defects | Recovery annealing, void nucleation |
| Phonons | Part VIII MD validation | Thermal expansion, heat capacity |
| Forces on displaced atoms | EAM fitting | Notch MD with trustworthy potential |
| NEB migration barriers | Part VII kinetics | Creep, diffusion during anneal |

The epilogue's sequential homogenization chain starts here — not at FEM. A wire simulation that imports \(E = 120\) GPa without asking whether it came from Voigt-averaged DFT, room-temperature experiment, or cold-worked polycrystal data carries silent assumptions this chapter makes explicit.

## Common workflow failures (and fixes)

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Total energy shifts when cell duplicated | Extensive vs intensive confusion | Report per-atom or per-formula-unit energies |
| SCF "not converged" | Cutoff too low, bad mixing, metal without smearing | Raise \(E_{\text{cut}}\), adjust `mixing_beta`, add smearing |
| Relaxation stalls | Force threshold too tight, bad initial geometry | Loosen then tighten; check space group |
| Elastic constants non-symmetric | Strain steps too large, insufficient SCF tolerance | Reduce strain, tighten `conv_thr` |
| Imaginary phonons at \(\Gamma\) | Incomplete relaxation, wrong structure | Re-relax; check space group and k-mesh |

Each fix mirrors habits from Part IV: refine discretization, tighten solver tolerance, verify boundary conditions.

## Jupyter, HPC, and team practice

MSE5720 homeworks combine Jupyter notebooks with batch scripts for clusters (XSEDE-style queues). Modern equivalents use Slurm arrays to sweep parameters. The book does not prescribe a cluster — but it prescribes **discipline**:

- Version-control inputs alongside manuscripts.
- One `README` per study listing functional, pseudo, cutoffs, and final converged values.
- Plot convergence curves in supplementary material, not only final answers.

Scientific machine learning surrogates (epilogue) trained on DFT data inherit these metadata requirements. A neural network predicting formation energy without functional labels is not multiscale — it is interpolation without a ladder.

## Concept map checkpoint (Part IX)

Part IX followed the DFT coursework arc from Born–Oppenheimer through Quantum ESPRESSO workflows. The four questions summarize the electronic scale:

| Question | Part IX answer (copper wire) |
|----------|------------------------------|
| What **object**? | Electron density \(\rho(\mathbf{r})\), Kohn–Sham orbitals, ionic positions |
| What **structure**? | Hohenberg–Kohn variational principle; SCF cycle; plane-wave basis, k-mesh |
| What **theorem**? | Hohenberg–Kohn; Kohn–Sham mapping (with approximate \(E_{xc}\)) |
| What **breaks**? | Functional dependence; metals without smearing; pseudopotential transferability |

The export table above is where the **downward derivation** of the ladder begins: \(E_{\text{coh}}\), \(C_{ijkl}\), stacking-fault energies, and phonons feed MD potentials, DDD mobilities, and continuum moduli. A wire simulation that imports \(E = 120\) GPa without asking whether it came from Voigt-averaged DFT, room-temperature experiment, or cold-worked polycrystal data carries silent assumptions this part makes explicit. The epilogue asks how disciplined teams wire these exports into multiscale workflows.

## Lab act: archive the foundation run before the wire-scale solve (Act VI — Foundation)

**Act VI** in the lab is the offline foundation run — the DFT calculation that must finish before anyone trusts the EAM potential, the mobility table, or the Young's modulus in the FEM input deck. This chapter's workflow discipline is not bureaucracy; it is the audit trail the epilogue's multiscale afternoon will ask you to produce.

Before closing Part IX, create one folder — paper or digital — for bulk fcc Cu with this minimum metadata:

| File / record | Must contain | Feeds |
|---------------|--------------|-------|
| `cu.scf.in` | Functional (PBE), cutoff (Ry), k-mesh, converged total energy | \(E_{\text{coh}}\), \(a_0\) |
| `cu.relax.out` | Final forces \(< 10^{-4}\) Ry/Bohr, relaxed \(a\) | Equilibrium lattice for MD box |
| `cu.elastic/` | ±0.5% strain cells, symmetric \(C_{ij}\) | Part VI moduli; Part IV elastic step |
| `README.md` | Pseudo version, QE version, date, who ran it | Team audit; epilogue handoff |

The pedigree checklist in [VIII.3](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) maps each row to a Part VIII use. If your project folder has only "EAM fit to experiment" with no `pw.x` log, **Act VI is missing** — and the wire-scale FEM run carries silent assumptions this chapter makes explicit.

Run one convergence check before archiving: double the plane-wave cutoff and confirm \(E_{\text{tot}}\) changes by less than 1 meV/atom. Part II taught that honest FEM requires a convergence target in \(H^1\); Part IX teaches the same instinct at the electronic scale — SCF energy must settle before any number climbs the ladder.

## Bridge to the epilogue

We have reached the finest rung of the spatial ladder for equilibrium properties of bulk copper: electrons, orbitals, self-consistency, convergence, exports. The copper wire at human scale — sag, Joule heat, work hardening, possible fracture — never lives here. It lives in the **coupling** of what each part computes.

The epilogue gathers sequential homogenization, concurrent handshakes, and surrogate acceleration into workflows that respect the rituals of this chapter: converged DFT feeds potentials; potentials feed MD; MD feeds mobilities; DDD feeds hardening; FEM and CFD feed design. The story that opened with a single material at many scales closes with how disciplined teams make those scales converse — with archived inputs, stated tolerances, and honest error bars. Read the epilogue's [**Closing the arc from Part IX**](../epilogue/multiscale.md#closing-the-arc-from-part-ix) first if you want the export table above mapped directly onto one multiscale afternoon before the general coupling patterns.
