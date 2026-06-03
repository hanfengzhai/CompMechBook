# Post-SCF Workflows: Convergence, Phonons, and Elasticity

Kohn–Sham self-consistency is the front door. Most properties practitioners care about — elastic moduli, phonon spectra, band gaps, phase stability under pressure — are **post-SCF workflows** built on a converged ground state. This chapter follows the discipline taught in Cornell's [MSE 5720](https://github.com/hanfengzhai/MSE5720-HW) coursework: converge systematically, benchmark against literature at the **same exchange–correlation functional**, and treat every number as conditional on documented input parameters.

For copper, the chain from Chapter 2's SCF cycle to a bulk modulus exported to FEM is not a single `pw.x` run. It is a pipeline of cutoff sweeps, k-mesh sweeps, variable-cell relaxation, energy–volume curves, and optional phonon or band-structure post-processing — each step gated by explicit convergence criteria.

## The convergence ladder

Before any property calculation, three independent thresholds must be satisfied:

| Quantity | Typical criterion | What it guards |
|----------|-------------------|----------------|
| Total energy | \(\Delta E < 5\) meV/formula unit between successive cutoffs | Absolute energies, cohesive energies, energy differences |
| Forces | \(\|\mathbf{F}\| < 10\) meV/Å (tighter for delicate relaxations) | Geometry optimization, phonons, elastic constants |
| k-point mesh | \(\Delta E\) below same energy threshold between successive meshes | Metals (Cu), Fermi-surface integrals, band gaps |

These numbers are not universal laws; they are **engineering tolerances** from the MSE 5720 archive. The principle is universal: never report a property at a single cutoff or k-mesh without demonstrating that the answer is stable under refinement.

### Plane-wave cutoff sweep

Start with `scf` calculations on a fixed geometry. Sweep `ecutwfc` from coarse to fine (e.g., 20–110 Ry in 10 Ry steps for semiconductors; adjust for Cu pseudopotentials). Tabulate total energy vs. cutoff and plot \(\Delta E\) between successive steps on a log scale — the curve should flatten before you stop.

For BAs in HW1, convergence to **5 meV/formula unit** between successive cutoffs was the stopping rule. The same workflow applies to Cu bulk: plot \(E(E_{\text{cut}})\), identify the knee, and document the chosen cutoff in every downstream calculation.

### k-point mesh sweep

Monkhorst–Pack grids (`K_POINTS automatic`) are swept similarly. For fcc Cu, start coarse (e.g., \(4\times4\times4\)) and refine until energy differences fall below threshold. Metals require denser meshes than insulators because Fermi-surface sampling dominates.

**Rule:** converge cutoff at a fixed k-mesh, then converge k-mesh at the chosen cutoff. Interchanging the order can waste compute or hide incomplete convergence.

### Force convergence for relaxations

Variable-cell relaxations (`calculation = 'vc-relax'`, BFGS ionic minimizer) require separate force thresholds. HW3 used **10 meV/Å** for ferroelectric PbTiO₃ where internal atomic coordinates shift under strain. Cu surface or vacancy calculations need similar care: a bulk modulus fit on unrelaxed volumes is meaningless if atomic positions are strained.

## From SCF to elastic constants

Elastic constants connect DFT directly to Part VI continuum mechanics and Part IV FEM. The standard **small-strain** workflow:

1. Fully relax the unit cell at converged cutoff/k (`vc-relax`).
2. Apply independent strain components \(\varepsilon_{ij}\) (Voigt notation: \(\varepsilon_{11}, \varepsilon_{22}, \varepsilon_{33}, \varepsilon_{23}, \varepsilon_{13}, \varepsilon_{12}\)).
3. For each strain, run `scf` (or `relax` if internal coordinates must re-equilibrate) and record total energy \(E(\varepsilon)\).
4. Fit \(E(\varepsilon)\) to a quadratic (or extract stress from the stress tensor output) to obtain \(C_{ijkl}\).

For cubic Cu, only three independent constants matter: \(C_{11}, C_{12}, C_{44}\). Bulk modulus follows:

\[
B = \frac{C_{11} + 2C_{12}}{3}.
\]

HW2 computed Si elastic constants this way and compared to experiment. The same bash loop pattern — `for strain in ...; do pw.x < input; done` — scales to any crystal system.

**Non-cubic materials** (HW3 PbTiO₃) require full \(6\times6\) elastic matrices, compliance tensors \(\mathbf{S} = \mathbf{C}^{-1}\), and — with thermal expansion coefficients from quasiharmonic phonons — links to thermomechanical coupling on the copper wire's heated surface.

## Energy–volume curves and equations of state

Cohesive energy and bulk modulus from an **EOS fit** complement the strain approach:

1. Relax at equilibrium volume \(V_0\).
2. Scale the lattice parameter (or cell volume) over a range (±3–5% is typical).
3. Run `scf` at each volume; tabulate \(E(V)\).
4. Fit to Birch–Murnaghan, Vinet, or a polynomial; extract \(E_{\text{coh}}\), \(B\), and optionally \(B'\).

HW1 compared polynomial fits of \(E(a)\) to BFGS relaxation for BAs. HW3 used cohesive energy curves to verify that diamond Si is **0.25 eV/atom** more stable than β-Sn at ambient pressure — a zero-temperature phase stability result that only makes sense after cutoff and k convergence.

For Cu, this workflow supplies the cohesive energy that sets the scale of bond breaking in MD and the bulk modulus that Part IV's structural model consumes.

## Phase stability under pressure

At finite pressure, compare **enthalpies**, not energies:

\[
H = E + PV.
\]

HW3 computed \(H(V)\) for diamond and β-Sn Si at 0.01, 8, and 11 GPa. The equilibrium phase at each pressure is the one with lower \(H\). The transition pressure where curves cross — **≈ 9.6 GPa in LDA**, compared to experiment (8.5–10.8 GPa) — is a direct DFT prediction testable against diamond-anvil experiments.

Copper's fcc structure is stable at ambient conditions, but the enthalpy workflow matters for high-pressure phases, shock physics, and materials where processing history involves pressure (cold drawing writes dislocations, not phase changes — but other alloys in the wire's connectors may not be so simple).

## Band structure and projected density of states

Electronic structure post-processing is a standard QE chain:

```
pw.x (scf)  →  pw.x (bands)  →  bands.x  →  dos.x  →  projwfc.x
```

HW2 on Si demonstrates the full pipeline:

- **Band structure** along high-symmetry k-paths; set Fermi level to zero for plotting.
- **Total DOS** and **atom-resolved** projected DOS (pDOS).
- **Orbital-resolved** pDOS (s, p, d) to assign peak character.

Band gaps from DFT with standard functionals **underestimate** experimental gaps — a limitation to state explicitly, not hide. Pseudopotential choice shifts absolute eigenvalues; compare band structures computed with the **same pseudo and functional**.

For Cu (a metal), bands and DOS diagnose smearing quality and k-mesh adequacy rather than a band gap. For insulating coatings on the wire (oxides, polymers), the same workflow characterizes interface chemistry when combined with slab models.

## Phonons: DFPT and strain response

Lattice dynamics link DFT to thermal properties and to mechanical stability:

**Density functional perturbation theory (DFPT):** `ph.x` with `ldisp = .true.` on a q-point grid computes phonon dispersions. HW2's `si_phonons.sh` and HW4's calcite zone-center modes follow this pattern.

**Finite-difference / strain approach:** HW3 tracked phonon frequencies under ±5% volume strain on Si, observing mode softening and hardening — Grüneisen behavior connecting elasticity to lattice dynamics.

Zone-center frequencies from phonon output feed spectroscopic comparisons (HW4 calcite: intensity ratios \(\nu_2/\nu_3\), \(\nu_4/\nu_3\)) and quasiharmonic thermal expansion when combined with free-energy integrations.

For the copper wire, phonons enter indirectly: Debye temperature affects heat capacity; anharmonic phonon–phonon scattering contributes to thermal conductivity models that couple to Part V CFD.

## Low-symmetry structures and `vc-relax`

Calcite (HW4) illustrates workflows beyond cubic Bravais lattices:

- `ibrav = 0` with explicit `CELL_PARAMETERS` and `ATOMIC_POSITIONS`.
- Converge **both** `celldm(1)` (scale) and `celldm(4)` (rhombohedral angle) plus internal coordinates.
- Compare relaxed parameters to **PBE-on-PBE** literature, not experiment mixed with a different functional.

Disorder studies (HW4: random rhombohedral-angle variations ±5°) probe how vibrational modes respond to structural noise — a bridge toward defect physics in Part VII without full dislocation core calculations.

## Pseudopotential and functional sensitivity

HW1 compared LDA and PBE pseudopotentials for B and As. Absolute energies shift; **energy differences** and **equilibrium volumes** shift too. A multiscale pipeline that fits an EAM potential to DFT energies must record:

- Pseudopotential family (ultrasoft, PAW, norm-conserving),
- XC functional (LDA, PBE, SCAN),
- Cutoff and k-mesh used for the fit,
- Code version and git hash.

Changing any of these without refitting breaks compatibility with MD (Part VIII) and invalidates moduli passed to FEM (Part IV).

## A reproducible workflow template

The MSE 5720 archive encodes a template every DFT study should follow:

```bash
# 1. Convergence (cutoff, k-mesh, forces)
for ecut in 40 50 60 70 80; do
  sed "s/ecutwfc = .*/ecutwfc = $ecut/" template.in > run.in
  mpirun pw.x < run.in > scf_${ecut}.out
done

# 2. Relaxation at converged settings
mpirun pw.x < vc-relax.in > relax.out

# 3. Property calculation (example: elastic constant strain loop)
for eps in -0.005 0 0.005; do
  # build strained cell, scf, extract energy
done

# 4. Post-process with awk / Python; archive inputs and outputs
```

Slurm job scripts, module loads (`module load quantum-espresso`), and versioned input decks in the homework repo show how HPC execution wraps the mathematics.

## Failure modes specific to post-SCF work

| Symptom | Likely cause |
|---------|--------------|
| Elastic constants nonsymmetric | Incomplete strain set; insufficient relaxation of internal coords |
| Phonons with imaginary modes | Unrelaxed structure; wrong symmetry; insufficient cutoff |
| Phase transition pressure wrong | Unconverged k-mesh; comparing \(E\) instead of \(H\) |
| DOS peaks misassigned | Skipped `projwfc.x`; wrong Fermi smearing |
| Literature mismatch | Different functional; different pseudo generation |

Each remedy returns to the convergence ladder — not to tweaking until agreement appears.

## Copper wire: what to export

From a well-converged Cu bulk or slab study, the multiscale exports are:

| Property | DFT workflow | Consumer |
|----------|--------------|----------|
| Bulk modulus \(B\) | EOS or elastic constants | Part IV FEM |
| Cohesive energy | EOS fit | Part VIII MD potential fitting |
| Surface energy | Slab models | Fracture, MD |
| Vacancy formation energy | Supercell `scf` | Diffusion, annealing kinetics |
| Elastic tensor | Strain series | Part VI anisotropic elasticity |

Document every export in a provenance file: functional, pseudo, cutoff, k-mesh, code version, date. The epilogue's sequential homogenization chain is only as trustworthy as this metadata.

## Bridge to the epilogue

We began with a copper wire and asked how each scale describes it. DFT explains cohesion and moduli; MD explains thermal motion and fracture; DDD explains work hardening; FEM explains bending; CFD explains cooling fluid around a heated conductor. Post-SCF workflows are where **abstract SCF cycles become numbers** that other rungs of the ladder can consume.

Multiscale computational mechanics is the craft of making those descriptions converse — sequentially, concurrently, and with quantified uncertainty. The epilogue gathers the coupling paradigms that complete the story.
