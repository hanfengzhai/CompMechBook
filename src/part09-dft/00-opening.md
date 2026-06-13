# Part IX — Electronic Structure

Part VIII assumed classical nuclei interacting through potentials fitted to data or theory. Part IX asks where those potentials originate: in the **quantum mechanical electron density** that binds copper atoms into a crystal, sets its cohesive energy, and determines the elastic constants and defect formation energies that every coarser model inherits.

The copper wire's baseline mechanical properties — bulk modulus, cohesive energy, vacancy formation energy, surface energy — are all **electronic** quantities before they are continuum parameters. A finite element model using \(E = 120\) GPa assumes someone computed or measured that number; DFT can compute it from first principles on a perfect fcc lattice, export it to an EAM potential fit in Part VIII, and cross-check the MD elastic constant that Part VI's variational elasticity approximates on a structural mesh. This part is the bottom rung of the ladder for equilibrium properties: not because atoms are "fundamental" in every sense (nuclei and quarks lie deeper), but because **chemistry and bonding** — the information every empirical potential must encode — live in the electron density.

Density functional theory (DFT) makes the ground-state energy a functional of \(\rho(\mathbf{r})\), tractable on computers with plane waves, pseudopotentials, and self-consistent field iteration. Born–Oppenheimer separation justifies treating nuclei as classical particles on surfaces defined by electronic structure; Hohenberg–Kohn theorems explain why the density alone suffices to determine the energy.

## What this part covers

| Chapter | Focus | Copper wire connection |
|---------|-------|------------------------|
| 01 — Born–Oppenheimer & Hohenberg–Kohn | Separation of scales, existence theorems | Why MD nuclei see a potential energy surface |
| 02 — Kohn–Sham DFT | SCF cycle, plane waves, convergence | Computing \(C_{ijkl}\), \(E_{\text{coh}}\) for copper bulk |
| 03 — DFT workflows | Quantum ESPRESSO inputs, exports upward | Reproducible pipeline from input files to MD/FEM numbers |

The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters with **Bridge** sections leading to the epilogue's multiscale coupling story, in the same [Functional Analysis Notes](../functional-analysis/) style as Parts I–VIII.

## The electronic question

At the electronic scale:

- **State**: electron density \(\rho(\mathbf{r})\) (and auxiliary Kohn–Sham orbitals \(\psi_i\)).
- **Equations**: Kohn–Sham self-consistent field equations with exchange–correlation functional.
- **Discretization**: plane-wave cutoff \(E_{\text{cut}}\), k-point mesh, pseudopotentials, SCF mixing.
- **Upward export**: cohesive energy, elastic tensor, defect formation energies, surface energies, phonon properties.

Unconverged SCF is structured noise — a lesson that echoes Part II's well-posedness theme at a different scale. Before trusting any number that flows upward to MD or FEM, convergence with respect to every discretization parameter is mandatory.

## Bridge

Part VIII treated atoms as classical particles. The first chapter below separates electrons from nuclei — the Born–Oppenheimer approximation — and explains why the ground-state electron density alone determines the energy landscape on which MD and elasticity ultimately rest.
