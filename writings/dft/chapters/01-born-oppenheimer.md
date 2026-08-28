# Born–Oppenheimer and the Hohenberg–Kohn Theorems

Electrons determine almost all material properties at the chemical level. Density functional theory (DFT) makes the ground-state energy a functional of the electron density — tractable on computers. Before Kohn–Sham equations and plane-wave codes, we need two foundational approximations: **Born–Oppenheimer separation** (nuclei vs. electrons) and **Hohenberg–Kohn theorems** (why the density alone suffices).

For copper, DFT answers the most basic question the wire poses at the finest scale: **why does the crystal cohere at all?** The answer lives in the quantum mechanical balance between kinetic energy, electrostatic attraction, and exchange–correlation — not in a spring constant inserted by hand.


## Plot spine (one line) {#plot-spine-one-line}

> **IX.1 — Act III — Descent:** Born–Oppenheimer separates fast electrons from slow nuclei — the finest scale split on copper.

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter.

## Scene: electrons adjust in a blink

Freeze a snapshot from Part VIII's molecular dynamics: copper nuclei mid-vibration, positions \(\{\mathbf{R}_I\}\) changing on picosecond timescales. The electrons that bind those nuclei respond in **femtoseconds** — three orders of magnitude faster because \(m_e \ll m_{\text{Cu}}\). In the laboratory frame, nuclei appear nearly stationary while the electron cloud rearranges around each geometry almost instantly.

That separation is the **Born–Oppenheimer** picture this chapter opens with. Part VIII's EAM potential treated nuclei as classical particles on a fixed energy surface; Part IX asks where that surface came from. The answer is not a fitted spline through experimental data alone — it is the **ground-state electron density** \(\rho(\mathbf{r})\) that minimizes total energy for each nuclear configuration. The copper wire at this scale is a periodic lattice of nuclei immersed in a sea of valence electrons; cohesive energy, elastic constants, and vacancy formation enthalpies are all consequences of that quantum balance. The sections below make the separation and the density functional theorems precise enough to run in Quantum ESPRESSO and export numbers upward to MD, DDD, and FEM.

## Born–Oppenheimer approximation

The full molecular Hamiltonian includes kinetic energy of \(N_n\) nuclei and \(N_e\) electrons, electron–nuclear attraction, electron–electron repulsion, and nuclear–nuclear repulsion. Mass scales differ dramatically: \(m_e \ll m_{\text{nucleon}}\).

Nuclei move slowly; electrons respond almost instantly. **Born–Oppenheimer (BO) approximation** separates the problem:

1. For fixed nuclear positions \(\{\mathbf{R}_I\}\), solve the **electronic Schrödinger equation** for ground-state energy \(E_e(\{\mathbf{R}_I\})\) and density \(\rho(\mathbf{r}; \{\mathbf{R}_I\})\).
2. Nuclei move on the **potential energy surface** \(V_{\text{BO}}(\{\mathbf{R}_I\}) = E_e(\{\mathbf{R}_I\})\) (plus nuclear repulsion).

Formally, BO expands in powers of \((m_e/m_I)^{1/4}\); for copper, corrections are tiny at room temperature.

### Consequences for the simulation ladder

| Without BO | With BO |
|------------|---------|
| Coupled electron–nuclear dynamics (expensive) | Fixed-nuclei electronic problem at each geometry |
| Ab initio MD requires explicit electron propagation | **Born–Oppenheimer MD**: forces = \(-\nabla_{\mathbf{R}_I} E_e\) from DFT |
| Hard to define a potential for classical MD | \(V_{\text{BO}}\) defines MD potential (exact in principle, approximated in practice) |

Classical MD of copper (Part VIII) assumes nuclei live on a BO surface. **Ab initio MD** (Car–Parrinello, Born–Oppenheimer MD) still uses BO but computes forces from DFT each step — bridging Part VIII and Part IX without empirical EAM.

### When BO fails

- **Proton transfer**, **photochemistry**: electrons do not adiabatically follow.
- **Light elements** (H): nuclear quantum effects (zero-point motion) matter.
- **Metals at high temperature**: Fermi smearing treats partial occupancies; still BO-like but with entropic electronic contributions.

For fcc copper elasticity and vacancy formation, BO is the standard starting point.

## The electronic ground-state problem

At fixed nuclei, the many-electron Schrödinger equation

\[
\hat{H}_{\text{el}} \Psi = E \Psi
\]

lives in \(3N_e\)-dimensional configuration space — intractable for direct wavefunction methods beyond small molecules. **Density functional theory** reduces the problem to a function of three spatial variables \(\rho(\mathbf{r})\).

## Hohenberg–Kohn theorems (1964)

For a non-degenerate ground state of a system of interacting electrons in an external potential \(v_{\text{ext}}(\mathbf{r})\) (from nuclei):

**Theorem 1 (HK1):** The ground-state electron density \(\rho(\mathbf{r})\) uniquely determines the external potential (up to a constant). The many-body ground state is a **functional** of \(\rho\).

**Theorem 2 (HK2):** There exists a universal functional \(F[\rho]\) such that the total energy

\[
E[\rho] = F[\rho] + \int v_{\text{ext}}(\mathbf{r})\,\rho(\mathbf{r})\, d\mathbf{r}
\]

is minimized at the ground-state density \(\rho_0\), and the minimum value is the ground-state energy.

### What HK does and does not say

HK **does** justify searching for the best \(\rho\) rather than the best \(3N_e\)-dimensional wavefunction.

HK **does not** provide the form of \(F[\rho]\) — only its existence. All practical DFT is **approximate DFT**, defined by how we model the unknown pieces.

HK applies to ground states. **Excited states**, **band gaps**, and **spectroscopy** require extensions (Δ-SCF, GW, TDDFT) beyond standard ground-state DFT — relevant when the copper wire's electrical conductivity (Fermi surface) is discussed, but ground-state DFT still supplies cohesive energy and elastic constants.

### HK as a compression theorem (Part II returns)

Part II asked what **state variable** carries enough information for well-posed mechanics. For interacting electrons, the naive answer is the full many-body wavefunction \(\Psi(\mathbf{r}_1,\ldots,\mathbf{r}_{N_e})\) — a function on \(3N_e\) dimensions. Hohenberg–Kohn is a stunning compression: the **ground-state** energy depends only on \(\rho(\mathbf{r})\), a scalar field on three dimensions.

| Part II habit | Electronic-scale analogue |
|---------------|---------------------------|
| Choose a minimal state in a function space | \(\rho \in L^1\) (or finer Sobolev classes in Kohn–Sham) |
| Energy as a functional of that state | \(E[\rho] = F[\rho] + \int v_{\text{ext}}\rho\) |
| Minimizer exists under structure | HK2: ground-state \(\rho_0\) minimizes \(E[\rho]\) |
| Approximation = projection / trial subspace | LDA, GGA, hybrids are **ansätze** for unknown \(E_{\text{xc}}\) |

The copper wire's Joule heating (Part V) and elastic stiffness (Part VI) ultimately trace to how \(\rho(\mathbf{r})\) binds nuclei. HK does not tell us how to compute \(F[\rho]\) — that is the exchange–correlation approximation — but it tells us **what object** every DFT code is optimizing. When Quantum ESPRESSO reports `convergence has been achieved`, it has found a self-consistent \(\rho\) that minimizes an approximate \(E[\rho]\) on a periodic cell representing a tiny patch of the wire's crystal.

## Copper valence: what DFT sees in the wire

Bulk copper is fcc with one valence electron per atom in the metallic picture: a filled \(3d^{10}\) core and a partially delocalized \(4s\) band crossing the Fermi level. DFT does not need chemists' orbital cartoons to run, but the picture explains exports upward:

- **Metallic cohesion** comes from the balance of electron kinetic energy (Pauli pressure) and electrostatic attraction to ion cores — not from pairwise springs.
- **Near-incompressibility** at small strain (bulk modulus \(B \approx 140\) GPa) is the curvature of \(E(V)\) around equilibrium volume — the same second-derivative habit as Part I's stiffness matrix \(\mathbf{K}\), now on a unit cell.
- **Electrical conductivity** of the wire under current (prologue Act II) is a **Fermi-surface** property: partially occupied bands at \(E_F\). Ground-state DFT locates \(E_F\) qualitatively; quantitative resistivity often needs beyond-DFT or Boltzmann transport — but lattice constant and elastic constants from the same run still anchor multiscale workflows.

A DFT unit cell of four Cu atoms is not the wire. It is a **representative volume** whose intensive outputs (eV/atom, GPa moduli) scale upward through homogenization — the same export discipline the prologue's four questions demanded at every rung.

## Decomposing the energy functional

Practitioners write

\[
E[\rho] = T_s[\rho] + E_{\text{Hartree}}[\rho] + E_{\text{xc}}[\rho] + E_{\text{ext}}[\rho] + E_{\text{ion-ion}},
\]

where:

- \(T_s[\rho]\): **Kinetic energy of non-interacting** electrons with density \(\rho\) (Kohn–Sham construction, next chapter).
- \(E_{\text{Hartree}}[\rho] = \frac{1}{2}\iint \frac{\rho(\mathbf{r})\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\, d\mathbf{r}\, d\mathbf{r}'\): classical Coulomb repulsion of the density with itself (includes self-interaction error partially corrected by \(E_{\text{xc}}\)).
- \(E_{\text{ext}}[\rho] = \int v_{\text{ext}}(\mathbf{r})\rho(\mathbf{r})\, d\mathbf{r}\): electron–nuclear attraction.
- \(E_{\text{ion-ion}}\): nuclear repulsion (classical, fixed in BO).
- \(E_{\text{xc}}[\rho]\): **exchange–correlation** — the quantum many-body treasure buried in \(F[\rho]\).

## Exchange–correlation functionals

\(E_{\text{xc}}[\rho]\) captures Pauli exclusion (exchange) and correlation beyond Hartree. It is **not** known exactly except in limiting cases.

| Class | Depends on | Examples | Typical use |
|-------|------------|----------|-------------|
| **LDA** | \(\rho(\mathbf{r})\) locally | Perdew–Zunger | Benchmarks, some metals |
| **GGA** | \(\rho\), \(\|\nabla\rho\|\) | PBE, PBEsol | **General solids**, including Cu |
| **Hybrid** | Mix of DFT and Hartree–Fock exchange | PBE0, HSE06 | Band gaps, molecules |
| **Meta-GGA** | \(\nabla\rho\), Laplacian or kinetic density | SCAN, r\(^2\)SCAN | Improved thermochemistry |
| **ML-DFT** | Trained on databases | NN-XC | Research frontier |

For copper bulk properties — lattice constant \(a\), cohesive energy, elastic constants — **GGA-PBE** or **PBEsol** with appropriate pseudopotentials is standard. Band structure of metals is qualitatively correct (Fermi surface topology), though absolute band energies are not spectroscopic quantities.

### Functional choice is part of the model

XC choice affects:

- **Lattice constants** (equilibrium volume)
- **Elastic constants** (curvature of \(E(V)\))
- **Surface energies** (wire fracture, oxidation)
- **Formation energies** of vacancies and interstitials (defect thermodynamics)

Validation means comparing **like with like**: same functional, same pseudopotential, same cutoff conventions as literature references.

## Copper at the electronic scale

A perfect fcc copper unit cell contains 4 atoms. DFT computes:

\[
E_{\text{coh}} = \frac{E_{\text{bulk}} - N E_{\text{atom}}}{N},
\]

the energy per atom relative to isolated atoms — roughly 3–4 eV/atom depending on functional and reference state.

Small **strain deformations** of the cell give elastic constants:

\[
C_{ijkl} = \frac{1}{V}\frac{\partial^2 E}{\partial \varepsilon_{ij}\partial \varepsilon_{kl}}\bigg|_{\varepsilon=0}.
\]

These numbers propagate upward: EAM fitting targets, continuum \(\mathbb{C}\) for FEM, sanity checks on MD stress–strain at small strain.

A **vacancy** is modeled by removing one atom (with supercell size convergence). Formation energy

\[
E_f^v = E_{\text{vac}} - \frac{N-1}{N}E_{\text{bulk}}
\]

feeds defect thermodynamics in Part VII.

## From DFT to MD potentials

The pipeline sketched in Part VIII:

```
DFT energies/forces on many configurations
    → fit EAM or train ML potential
        → MD at nm scale
            → mobility, fracture, phonons
                → DDD / FEM parameters
```

DFT does not run a whole wire. It runs **small cells** with careful convergence and extracts **intensive** properties and **local** responses. The ladder carries those outputs upward.

**Force matching** minimizes \(\sum_i \|\mathbf{F}_i^{\text{DFT}} - \mathbf{F}_i^{\text{EAM}}\|^2\) over training structures including surfaces, liquids, and compressed/distorted lattices — so the MD potential inherits BO physics where it matters.

### Scale-boundary handshake: Fermi surface and resistivity → Part V Joule heating

The prologue's Act II turns on current: electrons deposit heat along the wire, and Part V's energy equation needs a **volumetric source** \(\dot{q}(x)\). In the continuum model that source comes from **Joule heating** \(\dot{q} = \rho_e J^2\), where \(\rho_e\) is electrical resistivity and \(J\) is current density. Born–Oppenheimer DFT does not compute \(\rho_e\) directly in a ground-state `scf` run — but it supplies the **electronic structure** from which resistivity models are built, and it anchors the **lattice geometry** that sets the Drude scattering length.

Ground-state DFT on fcc Cu locates the **Fermi level** \(E_F\) inside partially filled 4s–4p bands. The Fermi surface — the iso-energy surface in \(\mathbf{k}\)-space at \(E_F\) — determines how many electronic states participate in conduction at 0 K. Qualitative features DFT exports upward:

| DFT output | Physical meaning | Continuum / FVM consumer (Part V–VI) |
|------------|------------------|--------------------------------------|
| Band structure along high-symmetry lines | Number of carriers, Fermi velocity \(v_F\) | Drude model \(\rho_e \sim 1/(n e^2 \tau v_F)\) |
| Density of states at \(E_F\) | \(N(E_F)\) for Sommerfeld heat capacity | Transient heating capacity in coupled runs |
| Equilibrium \(a_0\) from Murnaghan fit | Atomic density \(n\) in Drude formula | Same \(a_0\) as EAM and MD |
| Phonon spectrum ([IX.3](03-dft-workflows.md)) | Electron–phonon scattering timescale \(\tau\) | Temperature-dependent \(\rho_e(T)\) |

**Downward import (experiment).** OFHC copper at 300 K has \(\rho_e \approx 1.7\times 10^{-8}\,\Omega\cdot\text{m}\). A 5 A current in a 1 mm² wire gives \(J = 5\times 10^6\,\text{A/m}^2\) and \(\dot{q} = \rho_e J^2 \approx 4.3\times 10^8\,\text{W/m}^3\) — the order of magnitude Part V's FVM heat source uses in Act II. DFT does not replace that handbook number in a production wire-scale run; it **audits** whether the electronic structure is metallic (Fermi surface crosses \(E_F\)), whether the lattice constant matches the resistivity model's atomic density, and whether phonon modes from the same foundation deck support the temperature dependence of \(\rho_e\) at elevated current.

**Boltzmann transport (beyond this chapter).** Quantitative resistivity requires **linearized Boltzmann transport** on the DFT band structure — codes such as BoltzTraP2 or Wannier90-based workflows compute \(\sigma_{ij}\) and hence \(\rho_e\) from the same converged `scf` as the elastic constants. The workflow pattern mirrors Part VIII's Green–Kubo thermal conductivity: DFT supplies the microscopic input, a transport code integrates over the Brillouin zone, and Part V imports a scalar \(\rho_e\) or \(\kappa\) into the continuum energy equation.

**Handshake checklist** (archive beside `README_DFT.md`):

| Check | DFT artifact | Part V / VI consumer | Pass criterion |
|-------|--------------|----------------------|----------------|
| Metallic character | Band structure plot; \(E_F\) crosses bands | Joule heating model valid | No band gap at \(E_F\) |
| \(a_0\) | `vc-relax.out` | Atomic density in Drude formula | Matches MD EAM \(a_0\) within 0.02 Å |
| Phonons | `ph.x` output | \(\rho_e(T)\) via electron–phonon coupling | Acoustic branches at \(\Gamma\) |
| Resistivity (optional) | BoltzTraP2 \(\sigma\) | \(\dot{q} = \rho_e J^2\) in FVM source | Within 30% of experiment at 300 K |

**What breaks without the handshake.** Using Joule heating in Part V with a resistivity from a handbook while DFT on the same project predicts a non-metallic gap (wrong functional, broken symmetry) is physics inconsistency — the heat source assumes delocalized carriers the electronic structure does not support. Using DFT \(a_0\) for elasticity but a different lattice constant for carrier density double-counts or under-counts \(\dot{q}\). The handshake is: **one foundation deck, one \(a_0\), one band-structure plot** before Act II's coupled run claims multiscale pedigree.

## Limitations and extensions

- **Van der Waals** interactions: standard GGA misses long-range dispersion; add DFT-D3 or vdW-DF for layered or weakly bound systems (less critical for bulk Cu–Cu).
- **Strong correlation**: localized d/f electrons need beyond-DFT (DMFT, hybrid). Copper's valence s-electrons are weakly correlated; standard DFT is appropriate.
- **Magnetism**: copper is non-magnetic in ground state; spin-polarized DFT unnecessary for pure bulk Cu.

## Conceptual placement on the ladder

| Rung | Question for copper wire |
|------|--------------------------|
| DFT | Cohesive energy? Elastic constants? Vacancy cost? |
| MD | How does a notch nucleate dislocations? Thermal expansion? |
| DDD | How does \(\rho\) evolve during cold work? |
| FEM | Will the wire sag? Max current before annealing? |

Born–Oppenheimer and Hohenberg–Kohn justify the **bottom** of the ladder: why energy is a functional of \(\rho\), and why nuclear motion can be separated. Kohn–Sham DFT (next chapter) is how that functional is minimized in practice — in Quantum ESPRESSO, VASP, GPAW, and the workflows taught in courses like MSE 5720.

## Lab act: Murnaghan fit on fcc Cu (Act VI — Foundation)

**Act VI** runs in parallel with the wire-scale afternoon — someone must produce the **foundation deck** before \(E\), \(\nu\), and \(E_{\text{coh}}\) enter Part IV's input file. Born–Oppenheimer justifies treating nuclear coordinates as parameters; this Lab act is the first DFT calculation on the copper ladder.

**Quantum ESPRESSO-style workflow** (4-atom fcc primitive cell, PBE functional, ultrasoft pseudopotential):

| Step | Input | Output to archive |
|------|-------|-------------------|
| 1. Volume scan | Scale lattice \(a = 3.50\)–\(3.70\,\text{Å}\) (7 points) | `scf_*.out` total energies \(E(a)\) |
| 2. Murnaghan fit | Fit \(E(V)\) to equation of state | Equilibrium \(a_0\), bulk modulus \(B_0\) |
| 3. Cohesive energy | \(E_{\text{coh}} = (E_{\text{tot}} - N E_{\text{atom}})/N\) | eV/atom for EAM target |
| 4. Convergence log | \(E_{\text{cut}}\), k-mesh (\(6\times6\times6\) minimum for fcc Cu) | Document in `README_DFT.md` |

Example acceptance gates (typical literature values for PBE Cu):

| Quantity | Expected (PBE) | Your run |
|----------|----------------|----------|
| \(a_0\) | ~3.64 Å | Fill after SCF |
| \(B_0\) | ~140 GPa | From Murnaghan |
| \(E_{\text{coh}}\) | ~3.7 eV/atom | Sign and magnitude check |

**Born–Oppenheimer in practice:** each volume point holds nuclei fixed while SCF finds the electronic ground state — that is the BO surface Part VIII's MD trajectories slide on. Do not mix volumes from under-converged SCF (energy drift \(> 10^{-4}\,\text{Ry/atom}\) between iterations).

When `README_DFT.md` accompanies the wire project's git commit, the foundation run is **citable** — the same audit Part VIII's EAM-fit Lab act demands. [IX.2](02-kohn-sham.md) adds the SCF cycle details; [IX.3](03-dft-workflows.md) wires this deck into the full multiscale export.

## Concept map checkpoint (Born–Oppenheimer and Hohenberg–Kohn)

This chapter is where the multiscale ladder receives its **intellectual floor** — why energy is a functional of electron density. Before Kohn–Sham implements the minimization, summarize what the theorems established:

| Question | Part IX answer (copper wire) |
|----------|------------------------------|
| What **object**? | Electron density \(\rho(\mathbf{r})\); Born–Oppenheimer energy surface \(E_{\text{BO}}(\{\mathbf{R}_I\})\) |
| What **structure**? | Fast electrons / slow nuclei separation; HK universal functional \(F[\rho]\) |
| What **theorem**? | Hohenberg–Kohn: ground-state energy uniquely determined by \(\rho\); variational principle |
| What **breaks**? | BO breakdown (light H); strong correlation; van der Waals with plain GGA |

The Murnaghan-fit Lab act is Act VI's foundation deck: each volume point holds nuclei fixed while SCF finds the electronic ground state — the BO surface Part VIII's MD trajectories slide on. Small-cell DFT computes **intensive** quantities (\(a_0\), \(B_0\), \(E_{\text{coh}}\)) that propagate upward through the entire book.

## Bridge

Born–Oppenheimer separation and Hohenberg–Kohn existence theorems justify treating **energy as a functional of electron density** while nuclei evolve on a slower surface — the intellectual floor under every copper cohesive-energy calculation in this book.

| What Born–Oppenheimer gave | What Kohn–Sham DFT (next chapter) implements |
|------------------------------|---------------------------------------------|
| Fast electrons, slow nuclei; BO energy surface | Self-consistent Kohn–Sham equations solved in QE/VASP/GPAW |
| Energy as functional of \(\rho(\mathbf{r})\) (HK theorem) | Auxiliary non-interacting orbitals with the same density |
| Small-cell DFT computes **intensive** quantities | Plane waves, k-meshes, \(E_{\text{cut}}\) convergence rituals |
| Inputs for Part VIII EAM fits and Part VII defect energies | Workflows from input deck to elastic constants upward |

**Scale-boundary handshake (IX.1 → IX.2 → Part VIII).**

| Theorem output (this chapter) | Kohn–Sham implementation (next chapter) | Upstream consumer | Failure mode |
|-------------------------------|-------------------------------------------|-------------------|--------------|
| BO energy surface \(E_{\text{BO}}(\{\mathbf{R}_I\})\) | SCF loop on fixed nuclear geometry | LAMMPS Born–Oppenheimer MD (VIII.3) | Mixing BO and non-BO dynamics |
| HK variational principle on \(\rho(\mathbf{r})\) | Kohn–Sham orbitals with same density | EAM embedding/density fit (VIII.1) | Using excited-state \(\rho\) for ground-state fit |
| Murnaghan \(a_0\), \(B_0\) from volume scans | Converged `pw.x` at each lattice parameter | Part IV elastic step; Part VI \(\mathbb{C}\) | Under-converged SCF between volume points |
| Cohesive energy \(E_{\text{coh}}\) per atom | Total energy at equilibrium volume | EAM bulk modulus sanity check | Wrong reference energy (isolated atom vs bulk) |
| Defect formation enthalpy definitions | Supercell SCF with one removed atom | Part VII Peierls, Part VIII NEB barriers | Finite-size image errors in small cells |

Part II asked what **state variable** carries enough information for well-posed mechanics; Hohenberg–Kohn answers that question at the electronic scale — \(\rho(\mathbf{r})\) replaces the \(3N_e\)-dimensional wavefunction. Part VIII assumed that compression without proof; this chapter supplies the intellectual floor. See also the [two clocks note](../part08-md/00-opening.md#two-clocks-reading-order-vs-foundation-pedigree): chapter order descends VII → VIII → IX; workflow order builds input decks IX → VIII → VII → IV.

Return to the prologue's **Act VI — Foundation**: before any wire-scale FEM run, someone chose \(E\), \(\nu\), and surface energies whose pedigree traces to calculations like those in this part. Part VIII's EAM potential and Part VII's stacking-fault energies consume what IX.1–IX.3 export; the epilogue wires those exports into multiscale pipelines no single code runs alone.

[IX.2](02-kohn-sham.md) is the practitioner's chapter — SCF cycles, pseudopotentials, and the convergence checklist that separates chemistry from numerical artifact. Turn the page when "DFT gave a number" but cutoff, k-sampling, and functional choice were never documented — that is the signal the foundation run is not yet trustworthy enough to climb the ladder.
