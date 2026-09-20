# Kohn–Sham DFT: Equations, Convergence, and Practice

Kohn–Sham DFT turns the abstract Hohenberg–Kohn energy functional into a **self-consistent field (SCF)** problem — orbitals, eigenvalues, and a cycle that must converge before any property is trusted. This is the chapter practitioners live in: plane waves, pseudopotentials, k-point meshes, and the discipline of convergence studies.

For copper, a typical calculation fits in a few hundred atoms' worth of plane-wave coefficients — yet supplies the cohesive energy and elastic constants that anchor every coarser model of the wire.

## Scene: the self-consistent loop

A Quantum ESPRESSO run on fcc copper begins with a guess for the electron density \(\rho(\mathbf{r})\). From that guess, build an effective potential; solve single-particle Schrödinger-like equations for orbitals; reconstruct a new density from occupied states; mix old and new densities; repeat until \(\rho\) stops changing — the **SCF cycle**. Each iteration is linear algebra on orbital coefficients; convergence is the signal that the Kohn–Sham equations are satisfied.

Only after SCF converges do we trust the total energy, the stress tensor, and the numbers we will export upward: cohesive energy for vacancy formation, elastic constants for continuum moduli, surface energies for fracture models. The copper wire's baseline — what it costs to create a defect, how stiff the lattice is at 0 K — lives in this loop. Part IX's final chapter will show the input files; this chapter shows the **story inside the loop** that makes those files worth running.

## Kohn–Sham equations

Kohn and Sham (1965) introduced auxiliary **non-interacting orbitals** \(\psi_i(\mathbf{r})\) that reproduce the interacting density:

\[
\rho(\mathbf{r}) = \sum_{i}^{\text{occ}} f_i \, |\psi_i(\mathbf{r})|^2,
\]

where \(f_i\) are occupation numbers (0 or 1 at 0 K for insulators; Fermi–Dirac at finite smearing for metals).

The orbitals satisfy single-particle equations:

\[
\left[-\tfrac{1}{2}\nabla^2 + V_{\text{eff}}[\rho](\mathbf{r})\right]\psi_i(\mathbf{r}) = \epsilon_i \psi_i(\mathbf{r}),
\]

with effective potential

\[
V_{\text{eff}}[\rho] = v_{\text{ext}}(\mathbf{r}) + \int \frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\, d\mathbf{r}' + v_{\text{xc}}[\rho](\mathbf{r}).
\]

The Hartree term is the Coulomb potential of the total density; \(v_{\text{xc}} = \delta E_{\text{xc}}/\delta\rho\). **Kinetic energy** of the interacting system is recovered from non-interacting orbitals:

\[
T = -\sum_i f_i \langle \psi_i | \nabla^2 | \psi_i \rangle.
\]

### Self-consistency cycle

1. **Guess** initial \(\rho(\mathbf{r})\) (atomic superposition, random noise, or previous geometry).
2. **Build** \(V_{\text{eff}}[\rho]\).
3. **Solve** Kohn–Sham equations for \(\psi_i\) (diagonalize Hamiltonian in basis).
4. **Construct** new \(\rho\) from occupied orbitals.
5. **Mix** new and old density: \(\rho_{\text{in}} = \alpha \rho_{\text{new}} + (1-\alpha)\rho_{\text{old}}\) (linear, Pulay/Broyden, Kerker for metals).
6. Repeat until \(\|\rho_{\text{new}} - \rho_{\text{old}}\|\) and total energy change fall below thresholds.

Unconverged SCF is **structured noise** — energies and forces are meaningless. Metals like copper require **smearing** of occupations (Gaussian, Methfessel–Paxton) because Fermi surface crossings make zero-temperature SCF oscillate.

### SCF as fixed-point iteration — the Part I eigenvalue loop with feedback

The SCF cycle is a **fixed-point problem**: find \(\rho^\star\) such that \(\rho^\star = \mathcal{G}(\rho^\star)\), where \(\mathcal{G}\) maps an old density through build-potential → solve orbitals → construct new density. Each inner step — diagonalizing the Kohn–Sham Hamiltonian — is the **generalized eigenvalue problem** from [Part I.3](../part01-linear-algebra/03-eigenvalues.md):

\[
\mathbf{H}[\rho]\,\mathbf{c}_n = \epsilon_n\,\mathbf{S}\,\mathbf{c}_n,
\]

with overlap matrix \(\mathbf{S}\) from non-orthogonal plane-wave or PAW bases. The outer loop is what Part I did not have: the matrix \(\mathbf{H}\) depends on the eigenvectors through the density, so the spectrum and the operator co-evolve until self-consistency.

| Part I object | Kohn–Sham analogue | What changes in SCF |
|---------------|---------------------|---------------------|
| Fixed \(\mathbf{K}\) | \(\mathbf{H}[\rho]\) from converged density | \(\mathbf{H}\) updated each outer iteration |
| CG on \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | Pulay/Broyden mixing on \(\rho\) | Nonlinear fixed-point acceleration |
| Jacobi preconditioner ([I.1](../part01-linear-algebra/01-vectors-matrices.md)) | Kerker preconditioner on \(\delta\rho\) | Damp long-wavelength charge sloshing in metals |
| Residual \(\|\mathbf{r}_k\|\) vs iteration | \(\|\rho_{\text{new}} - \rho_{\text{old}}\|\), \(\Delta E\) | Same diagnostic habit: plot until flat |
| Ill-conditioned \(\mathbf{K}\) | SCF oscillation near \(E_F\) | Smearing replaces sharp Fermi step |

**Kerker mixing as preconditioner.** In metals, low-\(\mathbf{G}\) components of \(\delta\rho = \rho_{\text{new}} - \rho_{\text{old}}\) oscillate slowly and destabilize linear mixing. Kerker scaling attenuates those components — the electronic analogue of Jacobi rescaling diagonal entries before CG. The engineering instinct is identical: identify the stiff modes (long-wavelength charge transfer), damp them, iterate on the well-conditioned remainder.

**Convergence plot discipline.** Archive two curves for every production run:

1. Total energy \(E[\rho_n]\) vs SCF iteration \(n\) — should decrease then flatten.
2. Maximum residual force \(\max_I \|\mathbf{F}_I\|\) vs \(n\) — should fall below threshold (often 0.001 Ry/Bohr) before exporting elastic constants.

If energy flattens but forces remain large, the calculation is **not converged** — the same trap as stopping CG when the residual looks small but the solution has not reached the true \(\mathbf{u}\). Part IV's mesh-refinement certificate and Part IX's SCF certificate are the same verification culture at different scales.

**Smearing and the Fermi step.** At 0 K, occupation numbers are Heaviside functions: states below \(E_F\) are filled, above are empty. For copper, bands cross \(E_F\) at many \(\mathbf{k}\)-points; a sharp step makes \(\rho(\mathbf{k})\) discontinuous and SCF oscillates. **Gaussian smearing** replaces the step with a smooth Fermi–Dirac-like broadening:

\[
f(\epsilon_{n\mathbf{k}}) = \frac{1}{2}\left[1 - \mathrm{erf}\left(\frac{\epsilon_{n\mathbf{k}} - \mu}{\sigma}\right)\right],
\]

with smearing width \(\sigma\) (often 0.01–0.05 Ry). Too large \(\sigma\) blurs the Fermi surface and over-stabilizes SCF; too small \(\sigma\) restores oscillation. Converge \(\sigma\) downward: start with 0.02 Ry for fcc Cu bulk, halve until energy changes fall below 1 meV/atom — the electronic analogue of mesh refinement.

## Plane-wave basis and periodic crystals

Copper wire bulk interior has **periodic** crystal symmetry. Bloch's theorem expands orbitals as

\[
\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}), \qquad
u_{n\mathbf{k}}(\mathbf{r}+\mathbf{T}) = u_{n\mathbf{k}}(\mathbf{r}),
\]

with periodic part \(u\) expanded in **plane waves**:

\[
u_{n\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} c_{n\mathbf{k},\mathbf{G}}\, e^{i\mathbf{G}\cdot\mathbf{r}}.
\]

Reciprocal lattice vectors \(\mathbf{G}\) are truncated at **cutoff energy**:

\[
E_{\text{cut}} = \frac{\hbar^2}{2m}|\mathbf{k}+\mathbf{G}|^2_{\max}.
\]

Higher \(E_{\text{cut}}\) → more plane waves → higher accuracy and cost. For Cu with norm-conserving or PAW pseudopotentials, \(E_{\text{cut}} \sim 40\)–\(80\) Ry is a typical starting range — always **converged**, never assumed.

### k-point sampling

Integrals over the Brillouin zone (BZ) become weighted sums over **k-points**:

\[
\sum_{n\mathbf{k}} \rightarrow \sum_{\mathbf{k}} w_{\mathbf{k}} \sum_n.
\]

For metals, dense k-meshes are mandatory: Fermi surface integrals converge slowly. fcc Cu often uses Monkhorst–Pack grids (e.g., \(12\times12\times12\)) for bulk properties — again, **convergence tests** required.

## Pseudopotentials

Core electrons have steep, node-rich wavefunctions near nuclei — expensive in plane waves. **Pseudopotentials** replace core + nucleus with a smooth effective potential acting on **valence** electrons only:

| Type | Idea | Codes |
|------|------|-------|
| **Norm-conserving** | Preserve charge density outside core radius | Quantum ESPRESSO, ABINIT |
| **PAW** | Reconstruct all-electron density in augmentation spheres | VASP, QE (PAW library) |
| **USPP** | Softer, fewer plane waves | Legacy VASP |

The **exchange–correlation** functional is often encoded consistently with the pseudopotential generation (e.g., PBE pseudo for PBE calculations). Mixing LDA pseudo with GGA functional is a common beginner error.

For copper, valence configuration typically includes \(3d^{10}4s^1\) — semicore d-states may be treated as valence in harder potentials for accurate equations of state.

## Convergence workflow (MSE 5720 and beyond)

The author's [MSE 5720 DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) walks through standard exercises that every serious calculation repeats:

### Step 1: Converge cutoff and k-grid

Fix geometry (experimental lattice constant initially). Sweep \(E_{\text{cut}}\) and k-mesh; plot total energy per atom vs. parameters. Choose the **smallest** settings where energy changes are below target tolerance (often 1 meV/atom for total energy, tighter for forces).

Forces converge more slowly than energy — elastic constant calculations need tighter settings than coarse cohesive energy estimates.

### Step 2: Optimize lattice constants

Relax atomic positions and **cell parameters** until forces and stress vanish:

\[
\sigma_{ij} \rightarrow 0, \qquad \mathbf{F}_I \rightarrow 0.
\]

Compare equilibrium volume \(V_0\) and \(a_0\) to experiment (Cu: \(a = 3.615\) Å). Functional error (PBE often overbinds slightly) is acceptable if **consistent** across compared configurations (e.g., vacancy formation uses same pseudo/functional as bulk).

Fit **equation of state** (Murnaghan, Birch–Murnaghan) to energy–volume curve for bulk modulus \(B\).

### Step 3: Compute elastic constants

Apply small strains \(\varepsilon\) to the cell (tetragonal, orthorhombic distortions for full \(C_{ij}\) tensor in cubic symmetry). Quadratic fit of \(E(\varepsilon)\) gives:

\[
C_{11}, \quad C_{12}, \quad C_{44} \quad \text{(three independent constants for cubic Cu)}.
\]

Compare to experiment: \(C_{11} \approx 170\) GPa, \(C_{12} \approx 124\) GPa, \(C_{44} \approx 76\) GPa (room temperature, with anharmonic corrections at finite T from MD).

### Step 4: Band structure and density of states

Along high-symmetry k-paths (\(\Gamma\)–X–W–K–\(\Gamma\)–L for fcc), plot \(\epsilon_n(\mathbf{k})\). Copper is a **metal**: bands cross Fermi level, confirming conductivity. DOS at \(E_F\) relates to electronic contribution to heat capacity (small for Cu).

Band structure validates pseudopotential quality; absolute band energies are not experimental quasiparticle energies without GW corrections.

### Step 5: Pseudopotential and XC sensitivity

Repeat key quantities (lattice constant, \(E_f^v\)) with alternate pseudopotentials or functionals (PBE vs. PBEsol). Document sensitivity — multiscale pipelines should propagate **uncertainty**, not single numbers.

## Defect and surface calculations

**Supercells** embed a defect with periodic images; formation energy converges with supercell size (64–256 atoms for vacancies in Cu is common). **k-point density** scales inversely with cell size — large cells need fewer k-points per dimension but more atoms.

**Surfaces** for wire oxidation or fracture: slab geometry with vacuum gap, dipole corrections, surface energy

\[
\gamma = \frac{E_{\text{slab}} - N E_{\text{bulk}}/N_{\text{bulk}}}{2A}.
\]

Surface energies feed crack nucleation models and wettability — linking DFT to Part VII–VIII fracture studies.

## Forces, stress, and geometry optimization

Hellmann–Feynman forces:

\[
\mathbf{F}_I = -\frac{\partial E}{\partial \mathbf{R}_I}
\]

enable **geometry optimization** and **Born–Oppenheimer MD**. Stress tensor from virial theorem allows **variable-cell** relaxation (important for anisotropic wire texture is not in single-crystal bulk calc, but polcrystalline effective properties may use homogenized inputs).

Force convergence threshold (Ry/Bohr) gates structural predictions — a "relaxed" vacancy configuration with residual forces will misreport formation energy.

## Properties for multiscale pipelines

| DFT output | Quantity | Downstream use |
|------------|----------|----------------|
| Total energy | Cohesive energy, \(E_f^v\) | Phase diagrams, defect thermodynamics |
| Elastic tensor | \(C_{ijkl}\) | Continuum \(\mathbb{C}\), sound speeds |
| Phonons (DFPT) | Dispersion, DOS | Thermal conductivity, MD validation |
| Surface energy | \(\gamma\) | Crack models, grain boundary cohesion |
| Forces | \(\mathbf{F}_I(\{\mathbf{R}\})\) | Ab initio MD, EAM/ML fitting |
| NEB barriers | Migration paths | Diffusion coefficients, creep |

Phonon calculations linearize DFT around equilibrium — compare phonon frequencies to inelastic neutron scattering or MD spectra for copper.

## Quantum ESPRESSO workflow sketch

Typical input sections (`pw.x`):

- `&CONTROL`: calculation (`scf`, `relax`, `vc-relax`, `bands`, `nscf`)
- `&SYSTEM`: cutoff, smearing (metal!), nat, ntyp, celldm
- `&ELECTRONS`: mixing, convergence thresholds
- `ATOMIC_SPECIES`, `ATOMIC_POSITIONS`, `K_POINTS`

Example logic for Cu bulk modulus:

1. `vc-relax` at converged cutoff/k-mesh → \(a_0\).
2. Series of `scf` on scaled volumes → \(E(V)\) curve.
3. Fit EOS → \(B\).

Archive inputs, pseudopotential files, and commit hash of the code — reproducibility is non-negotiable in multiscale research.

## SCF as a generalized eigenvalue problem (Part I returns)

The Kohn–Sham cycle is Part I's eigenvalue story in orbital clothing. In a plane-wave basis, each k-point Hamiltonian is a large Hermitian matrix \(\mathbf{H}[\rho]\) whose entries depend on the current density through \(V_{\text{eff}}[\rho]\). Solving

\[
\mathbf{H}[\rho]\,\mathbf{c}_n = \epsilon_n \,\mathbf{S}\,\mathbf{c}_n
\]

is a **generalized eigenvalue problem** — the same mathematical species as vibration modes \(\mathbf{K}\mathbf{v} = \omega^2 \mathbf{M}\mathbf{v}\) from [I.3](../part01-linear-algebra/03-eigenvalues.md), now with overlap matrix \(\mathbf{S}\) from non-orthogonal plane waves (often \(\mathbf{S} = \mathbf{I}\) after orthonormalization).

| Part I (springs on the wire) | Part IX (electrons in Cu) |
|------------------------------|---------------------------|
| Stiffness \(\mathbf{K}\) | Kohn–Sham \(\mathbf{H}[\rho]\) |
| Mass \(\mathbf{M}\) | Overlap \(\mathbf{S}\) (or identity in orthonormal PW basis) |
| Eigenvectors \(\mathbf{v}\) | Orbital coefficients \(\mathbf{c}_n\) |
| Eigenvalues \(\omega^2\) | Kohn–Sham energies \(\epsilon_n\) |
| Fixed matrix | **Self-consistent** matrix: \(\mathbf{H}\) rebuilt each SCF iteration |

Self-consistency is the new ingredient: eigenvectors from step \(k\) build a new density, which rebuilds \(\mathbf{H}\) for step \(k+1\). Convergence means the eigenpairs stop changing — the infinite-dimensional analogue of mesh refinement reaching a limit in Part II.

Part IV's assembly loop and Part IX's SCF loop share the same engineering instinct: **do not trust outputs until the discrete system has converged**. Ill-conditioned \(\mathbf{K}\) and unconverged \(E_{\text{cut}}\) both produce structured noise dressed as physics.

## Lab act: converge cutoff before trusting cohesive energy (Act VI)

**Act VI** runs in parallel with the visible lab session — someone must choose moduli and potentials before the wire-scale job starts. This Lab act is the minimum DFT audit for fcc Cu: converge plane-wave cutoff on total energy per atom.

**Step 1 — fixed geometry, sweep \(E_{\text{cut}}\).** Use experimental lattice constant \(a = 3.615\,\text{Å}\), PBE functional with matching pseudopotential, and a dense k-mesh (e.g. \(12\times12\times12\) Monkhorst–Pack). Run `scf` calculations at \(E_{\text{cut}} = 30, 40, 50, 60, 80\) Ry. Plot total energy per atom versus \(1/E_{\text{cut}}\) — the curve should flatten.

**Step 2 — choose cutoff.** Pick the **smallest** \(E_{\text{cut}}\) where consecutive energy changes are below 1 meV/atom (tighter for forces and elastic constants). Document the choice in the project README — the same discipline Part IV demands for mesh size \(h\).

**Step 3 — cross-check k-mesh.** At the chosen cutoff, repeat with k-meshes \(8^3\), \(10^3\), \(12^3\), \(14^3\). Metals require dense k-sampling because Fermi-surface integrals converge slowly; under-sampled k-meshes are the DFT analogue of too-coarse FEM on a reentrant corner.

**Step 4 — export one number upward.** Report cohesive energy \(E_{\text{coh}} = (E_{\text{tot}}/N_{\text{atoms}}) - E_{\text{atom}}\) with documented cutoff, k-mesh, and functional. Part VIII's EAM fit and Part VI's sanity checks inherit this number — if no QE log exists, the multiscale chain has no floor.

Example convergence table (illustrative — always run your own sweep):

| \(E_{\text{cut}}\) (Ry) | \(E/N\) (eV/atom) | \(\Delta E\) (meV/atom) |
|-------------------------|-------------------|-------------------------|
| 40 | −3.724 | — |
| 50 | −3.726 | 2 |
| 60 | −3.726 | 0.3 |
| 80 | −3.726 | 0.1 |

When \(\Delta E < 1\) meV/atom, proceed to `vc-relax` and elastic-constant calculations in [IX.3](03-dft-workflows.md). Unconverged cutoff is structured noise — the DFT version of an unrefined mesh.

## Concept map checkpoint (Kohn–Sham DFT)

This chapter is where Part I's eigenvalue story reappears as self-consistent electronic structure. Before workflow chapters archive reproducible decks, summarize what Kohn–Sham established:

| Question | Part IX answer (copper wire) |
|----------|------------------------------|
| What **object**? | Kohn–Sham orbitals \(\psi_n\); density \(\rho = \sum f_n |\psi_n|^2\); \(\mathbf{H}[\rho]\), \(\mathbf{S}\) |
| What **structure**? | SCF loop: orbitals → density → potential → new \(\mathbf{H}\); plane-wave / k-point quadrature |
| What **theorem**? | KS equations exact if \(E_{\text{xc}}[\rho]\) exact; variational principle on \(\rho\) |
| What **breaks**? | Approximate XC (PBE); under-converged \(E_{\text{cut}}\) or k-mesh; SCF oscillation in metals |

The cutoff-sweep Lab act is the DFT analogue of Part IV's \(h\)-refinement: pick the smallest \(E_{\text{cut}}\) where energy changes fall below 1 meV/atom before exporting \(E_{\text{coh}}\) to Part VIII's EAM fit. Generalized eigenvalue \(\mathbf{H}\mathbf{c}=\epsilon\mathbf{S}\mathbf{c}\) is Part I.3 with a self-consistent matrix.

## Common failure modes

| Symptom | Likely cause |
|---------|--------------|
| SCF oscillates | Insufficient smearing (metal); bad mixing; too low cutoff |
| Forces noisy | Low cutoff; poorly converged SCF |
| Wrong lattice constant | Wrong functional/pseudo pairing; incomplete relaxation |
| Vacancy energy drifts with cell size | Finite-size effects; need larger supercell |
| Band gap in metal | Insufficient k-sampling or broken symmetry |

Each failure has the same remedy: **converge systematically**, do not tune until the answer matches experiment.

## Copper wire in perspective

DFT will never simulate the whole wire. It **anchors** the ladder:

- Cohesive energy defines the scale of bond breaking.
- Elastic constants enter structural FEM.
- Defect formation energies inform vacancy diffusion and recovery during annealing.
- Fitted potentials enable MD of notches and dislocation cores.

The intellectual chain from electrons to engineering design passes through these numbers — each with documented convergence and stated functional choice.

## Bridge

The Kohn–Sham equations are the theory; Quantum ESPRESSO inputs and convergence sweeps are the practice.

| What Part VIII assumed | What this chapter derived | What [IX.3](03-dft-workflows.md) will archive |
|------------------------|---------------------------|-----------------------------------------------|
| EAM \(V(\{\mathbf{r}_i\})\) on trust | SCF total energy and converged \(\rho(\mathbf{r})\) | Input decks, pseudopotentials, k-mesh convergence logs |
| Bulk modulus from empirical fit | \(B\) from equation-of-state fits on scaled volumes | Reproducible `vc-relax` + `scf` series for fcc Cu |
| Stacking-fault energy for partials | Generalized stacking-fault surface from slab calculations | Defect supercells with documented finite-size study |
| Phonons for thermal checks | DFPT or finite-difference phonon workflows | Export tables for MD and continuum thermal expansion |

**Scale-boundary handshake (IX.2 → IX.3 → epilogue).**

| Kohn–Sham output (this chapter) | Workflow archive (next chapter) | Upstream consumer | Failure mode |
|---------------------------------|---------------------------------|-------------------|--------------|
| Converged \(\rho(\mathbf{r})\) and \(E_{\text{tot}}\) | Documented `pw.x` input deck + convergence log | Part VIII EAM fit ([VIII.1](../part08-md/01-potentials-phase-space.md)) | Under-converged \(E_{\text{cut}}\) exported to LAMMPS |
| Elastic constants \(C_{ij}\) from strain derivatives | `vc-relax` + stress-strain series for fcc Cu | Part IV/ VI \(\mathbb{C}\) on drawn wire | Single-point stress without relaxation |
| \(\gamma_{\text{sf}}\) from slab calculations | Generalized stacking-fault energy surface | Part VII partial dislocation laws | Wrong slip plane in slab geometry |
| Vacancy formation \(E_f^v\) | Supercell SCF with finite-size study | Part VIII NEB barriers; annealing kinetics | Image charge in too-small cell |
| Phonon DOS from DFPT | `ph.x` export table | Part VIII VACF cross-check ([VIII.2](../part08-md/02-ensembles-integrators.md)) | Incomplete k-mesh in phonon run |

Part I's eigenvalue loop reappears as the self-consistent cycle above; Part II's function spaces as orbital Hilbert spaces; Part IV's assembly philosophy as plane-wave expansions and k-point quadrature. The [Part IX opening](00-opening.md#bridge) framed this part as the **audit chapter** for every potential Part VIII already ran — the same role Part II played for Part I's stiffness matrices. The cutoff-sweep Lab act above is the DFT analogue of Part IV's \(h\)-refinement: pick the smallest \(E_{\text{cut}}\) where energy changes fall below 1 meV/atom before exporting any number upward.

Return to the prologue's **Act VI — Foundation**: before the operator mounted the wire, someone chose Young's modulus and a yield stress. That invisible afternoon is now explicit: cohesive energy per atom, elastic constants \(C_{ij}\), vacancy formation enthalpy, and surface energies — each gated by SCF convergence and documented functional choice. Unconverged cutoff is the DFT analogue of an ill-conditioned \(\mathbf{K}\): structured noise dressed as physics.

[IX.3](03-dft-workflows.md) walks through reproducible workflows — cutoff and k-mesh convergence, relaxation, equations of state, bands and phonons, defect supercells — using the MSE 5720 homework archive as a template. Those workflows produce the numbers Parts VI–VIII import before the [epilogue](../epilogue/multiscale.md) wires DFT → MD → DDD → FEM into one multiscale afternoon.

Turn the page when the SCF loop converges in principle but no input file exists yet — that is the signal that reproducibility, not theory, is what separates research from folklore.
