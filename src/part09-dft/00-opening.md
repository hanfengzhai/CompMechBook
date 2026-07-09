# Part IX — Electronic Structure

Part VIII assumed classical nuclei interacting through potentials fitted to data or theory. Part IX asks where those potentials originate: in the **quantum mechanical electron density** that binds copper atoms into a crystal, sets its cohesive energy, and determines the elastic constants and defect formation energies that every coarser model inherits.

Density functional theory makes the ground-state energy a functional of the electron density — tractable on computers with plane waves, pseudopotentials, and self-consistent field iteration. Born–Oppenheimer separation justifies treating nuclei as classical particles on surfaces defined by electronic structure; Hohenberg–Kohn theorems explain why the density alone suffices.

Three chapters cover Born–Oppenheimer and the Hohenberg–Kohn framework, Kohn–Sham equations and convergence practice, and reproducible Quantum ESPRESSO workflows that export numbers to MD, DDD, and continuum models. The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters with **Bridge** sections leading to the epilogue's multiscale coupling story.

## Scene

Part VIII ended with nuclei vibrating on an interatomic potential — EAM parameters fit to experiments, MD trajectories, or machine-learned surfaces. That potential is a **practical fiction**: it assumes electrons adjust instantaneously to nuclear motion, and it hides the quantum mechanics that sets cohesive energy, stacking-fault energy, and vacancy formation enthalpy.

The copper wire at the electronic scale is not a chain of balls on springs. It is a periodic crystal of nuclei immersed in a sea of valence electrons whose density \(\rho(\mathbf{r})\) determines how strongly the lattice resists drawing, how easily dislocations slip, and how vacancies cost energy. DFT resolves that density; every number exported upward — \(E_{\text{coh}}\), \(C_{ij}\), \(\gamma_{\text{sf}}\) — is a contract between Part IX and Parts VI–VIII.

## The concept map

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Electron density \(\rho(\mathbf{r})\), Kohn–Sham orbitals, total energy |
| What **structure** does it add? | Hohenberg–Kohn mapping, SCF iteration, k-point sampling |
| What **theorem** becomes possible? | Variational ground state, force theorem, elastic constants from strain |
| What **breaks** if structure is missing? | Wrong functional, SCF oscillation, size-extensive errors on small cells |

```mermaid
flowchart LR
  BO[Born-Oppenheimer] --> HK[Hohenberg-Kohn]
  HK --> KS[Kohn-Sham SCF]
  KS --> QE[Quantum ESPRESSO workflows]
  QE --> MS[Multiscale epilogue]
```

**Baby picture:** separate fast electrons from slow nuclei, prove the ground-state energy is a functional of density alone, solve Kohn–Sham equations self-consistently, then export cohesive energy and elastic moduli upward to MD, DDD, and FEM. The copper wire's valence electrons live here.

## Representative schematics (DFT Coursework)

The [MSE 5720 DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) and teaching materials follow the same concept-map layout: each schematic is a baby picture of the electronic-structure pipeline. Use them as a visual index while reading:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Born–Oppenheimer separation; Hohenberg–Kohn theorems; density as fundamental variable | [IX.1](01-born-oppenheimer.md) |
| 2 | Kohn–Sham equations, SCF cycle, plane-wave basis, convergence practice | [IX.2](02-kohn-sham.md) |
| 3 | Quantum ESPRESSO workflows on fcc Cu; exporting \(E_{\text{coh}}\), \(C_{ij}\), \(\gamma_{\text{sf}}\) upward | [IX.3](03-dft-workflows.md) |

Each schematic answers the four concept-map questions for one electronic layer. When an EAM potential in Part VIII feels like a black box, return to the matching row: *what object, what structure, what theorem, what breaks?* Part I's eigenvalue loop reappears here as Kohn–Sham orbitals; Part IV's basis discretization reappears as plane waves and k-points.

## Story so far (Parts I–VIII)

The descent from continuum to atoms is complete; Part IX reaches the **finest rung**:

| Part | Scale | Wire story beat |
|------|-------|-----------------|
| I–VI | Mathematics → FEM/FVM → continuum stress/strain | Meshed cylinder; virtual work; J₂ plasticity **preview** |
| VII | Dislocation lines | Forest hardening from cold drawing; DDD exports \(\tau(\gamma)\) |
| VIII | Atoms on potentials | EAM cores, LAMMPS workflows; mobility and \(\gamma_{\text{sf}}\) upward |

Part VIII assumed nuclei move on a potential surface — EAM, MEAM, or machine-learned — and exported moduli, stacking-fault energies, and mobility tables to DDD and FEM. That potential is a **practical fiction**: electrons adjust instantaneously to nuclear motion, but the quantum mechanics that sets cohesive energy, vacancy formation enthalpy, and elastic constants was hidden. Part IX makes the downward contract explicit: DFT resolves \(\rho(\mathbf{r})\), the ground-state energy is a functional of density alone, and every number exported upward — \(E_{\text{coh}}\), \(C_{ij}\), \(\gamma_{\text{sf}}\) — is traceable to a self-consistent Kohn–Sham cycle. The epilogue will ask how to climb back up with those numbers in a reproducible workflow.

## Closing the arc from Part VIII

If you have read linearly since the prologue, Part VIII's closing checkpoint fitted EAM potentials and exported moduli upward on **trust**. Part IX is the **audit chapter** — where every interatomic parameter receives an electronic pedigree:

| Part VIII (atoms on the wire) | Part IX (electrons in copper) |
|-------------------------------|-------------------------------|
| EAM potential \(V(\{\mathbf{r}_i\})\) on trust | Born–Oppenheimer: nuclei on \(E[\rho]\) surface |
| Cohesive energy from MD or experiment | \(E_{\text{coh}}\) from Kohn–Sham ground state |
| Elastic constants from stress–strain fluctuations | \(C_{ij}\) from strained unit cells (force theorem) |
| Stacking-fault energy for DDD mobility | \(\gamma_{\text{sf}}\) from relaxed faulted supercells |
| [VIII.3 Bridge](03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) requests DFT pedigree | [IX.3](03-dft-workflows.md) exports QE numbers upward |

Part VIII's LAMMPS trajectories assumed electrons follow nuclei instantaneously; Part IX separates the timescales and proves the ground-state energy is a **functional of density alone** — the finest rung of the prologue's ladder. The copper wire's valence electrons determine cohesive energy, bond stiffness, and defect formation enthalpies that every coarser model inherits. Part I's eigenvalue loop reappears as Kohn–Sham orbitals; Part IV's basis discretization reappears as plane waves and k-points. The epilogue will wire DFT → MD → DDD → FEM into one reproducible afternoon; Part IX supplies the numbers at the bottom of that chain.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** from the opening table reappear here with new vocabulary — and how the **same mathematical moves** from Part I return at the finest scale:

| Part I (springs on the wire) | Part IX (electrons in copper) |
|------------------------------|-------------------------------|
| State vector \(\mathbf{u}\) | Electron density \(\rho(\mathbf{r})\) |
| Stiffness matrix \(\mathbf{K}\) | Kohn–Sham Hamiltonian operator |
| Eigenmodes decouple vibration | Kohn–Sham orbitals diagonalize the effective potential |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) from energy minimization | Ground-state \(\rho\) minimizes \(E[\rho]\) |
| Mesh refinement sends \(N\to\infty\) | Plane-wave cutoff and k-mesh send basis size \(\to\infty\) |

Part II taught that Galerkin convergence is projection onto finite subspaces; Part IX's plane-wave basis is the same idea with Bloch phases instead of shape functions. Part III's weak forms asked us to multiply by test functions and integrate by parts; DFT's Hohenberg–Kohn framework replaces pointwise Schrödinger equations with a **variational statement on density** — the same instinct that made FEM honest at reentrant corners.

The copper wire that began as a chain of coupled springs ends as a periodic crystal whose valence electrons are solved by a self-consistent **eigenvalue loop** (Part I), in function spaces of orbitals (Part II), arising from a variational principle (Part III), discretized on a basis (Part IV's assembly philosophy), and exported upward as moduli and potentials (Parts VI–VIII). Part IX is not a new subject bolted onto the end. It is the **finest rung** of the ladder the prologue promised — and the epilogue will ask how to climb back up with the numbers computed here.

## Lab act: VI — Foundation (always, in parallel)

Before the operator mounted the wire, someone chose Young's modulus, Poisson's ratio, and a yield stress for the input deck. **Act VI** is that invisible afternoon — DFT on a small fcc cell, MD fitting an EAM potential, DDD calibrating mobility — run in parallel with Acts I–V and supplying every number the coarser codes trust. Part IX is where the foundation becomes explicit: cohesive energy, elastic constants, and stacking-fault energies exported upward with a pedigree traceable to Kohn–Sham orbitals.

## Reading Part IX after Part VIII

Part VIII already ran LAMMPS on an EAM potential **on trust** — cohesive energy, lattice parameter, and mobility tables appeared without a full electronic-structure derivation. If that felt like using numbers before understanding them, you have arrived at the right chapter.

| Role | Analogy in the book |
|------|---------------------|
| Part II for Part I | Named the limit object (\(H^1\), operators) behind every stiffness matrix |
| Part IX for Part VIII | Names the limit object (\(\rho(\mathbf{r})\), Kohn–Sham) behind every interatomic potential |

**Chapter order** (VII → VIII → IX) descends to finer physics after continuum and atomistics show where parameters hide their history. **Workflow order** (IX → VIII → VII → IV) is how practitioners actually build input decks — documented in [Act VI of the sources appendix](../appendix/sources.md#six-acts--parts-laboratory-time) and the [two clocks note](../part08-md/00-opening.md#two-clocks-reading-order-vs-foundation-pedigree) at the Part VIII opening. Linear readers should treat Part IX as the **audit chapter**: the same copper cell Part VIII vibrated, now solved for \(\rho(\mathbf{r})\) before the epilogue climbs back up the ladder.

## Bridge

Part VIII treated atoms as classical particles. The first chapter below separates electrons from nuclei — the Born–Oppenheimer approximation — and explains why the ground-state electron density alone determines the energy landscape on which MD and elasticity ultimately rest.
