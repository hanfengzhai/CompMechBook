# Born–Oppenheimer and the Hohenberg–Kohn Theorems

Electrons determine almost all material properties at the chemical level. Density functional theory (DFT) makes the ground-state energy a functional of the electron density — tractable on computers. Before Kohn–Sham equations and plane-wave codes, we need two foundational approximations: **Born–Oppenheimer separation** (nuclei vs. electrons) and **Hohenberg–Kohn theorems** (why the density alone suffices).

For copper, DFT answers the most basic question the wire poses at the finest scale: **why does the crystal cohere at all?** The answer lives in the quantum mechanical balance between kinetic energy, electrostatic attraction, and exchange–correlation — not in a spring constant inserted by hand.

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

## Bridge

Kohn–Sham DFT replaces the interacting many-body problem with an auxiliary non-interacting system sharing the same density — implemented as a self-consistent field cycle over orbitals and eigenvalues. The next chapter states the equations practitioners solve daily, the convergence rituals that separate physics from numerical artifact, and the plane-wave basis that makes periodic copper crystals computable.
