# Part IX — Electronic Structure

Part VIII assumed classical nuclei interacting through potentials fitted to data or theory. Part IX asks where those potentials originate: in the **quantum mechanical electron density** that binds copper atoms into a crystal, sets its cohesive energy, and determines the elastic constants and defect formation energies that every coarser model inherits.

Density functional theory makes the ground-state energy a functional of the electron density — tractable on computers with plane waves, pseudopotentials, and self-consistent field iteration. Born–Oppenheimer separation justifies treating nuclei as classical particles on surfaces defined by electronic structure; Hohenberg–Kohn theorems explain why the density alone suffices.

Three chapters cover Born–Oppenheimer and the Hohenberg–Kohn framework, Kohn–Sham equations and convergence practice, and reproducible Quantum ESPRESSO workflows that export numbers to MD, DDD, and continuum models. The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters with **Bridge** sections leading to the epilogue's multiscale coupling story.

## Where we left the wire

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

## Bridge

Part VIII treated atoms as classical particles. The first chapter below separates electrons from nuclei — the Born–Oppenheimer approximation — and explains why the ground-state electron density alone determines the energy landscape on which MD and elasticity ultimately rest.
