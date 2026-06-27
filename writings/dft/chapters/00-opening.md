# Part IX — Electronic Structure

Part VIII assumed classical nuclei interacting through potentials fitted to data or theory. Part IX asks where those potentials originate: in the **quantum mechanical electron density** that binds copper atoms into a crystal, sets its cohesive energy, and determines the elastic constants and defect formation energies that every coarser model inherits.

Density functional theory makes the ground-state energy a functional of the electron density — tractable on computers with plane waves, pseudopotentials, and self-consistent field iteration. Born–Oppenheimer separation justifies treating nuclei as classical particles on surfaces defined by electronic structure; Hohenberg–Kohn theorems explain why the density alone suffices.

Three chapters cover Born–Oppenheimer and the Hohenberg–Kohn framework, Kohn–Sham equations and convergence practice, and reproducible Quantum ESPRESSO workflows that export numbers to MD, DDD, and continuum models. The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters with **Bridge** sections leading to the epilogue's multiscale coupling story.

## The concept map (MSE 5720 / DFT)

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Ground-state electron density \(\rho(\mathbf{r})\) and Kohn–Sham orbitals |
| What **structure** does it add? | Born–Oppenheimer separation; Hohenberg–Kohn uniqueness; variational energy |
| What **theorem** becomes possible? | Total energy as functional of \(\rho\); SCF convergence to stationary point |
| What **breaks** if structure is missing? | Wrong functional for metals; k-mesh too coarse; pseudopotential mismatch |

```mermaid
flowchart LR
  BO[Born–Oppenheimer] --> HK[Hohenberg–Kohn]
  HK --> KS[Kohn–Sham equations]
  KS --> SCF[SCF + plane waves]
  SCF --> QE[Quantum ESPRESSO workflows]
  QE --> Up[E_coh, C_ij, γ_sf upward]
```

**Baby picture:** solve for the electron density that minimizes total energy, export cohesive energy and elastic constants upward, and let MD treat nuclei as classical particles on the resulting surface.

## Bridge

Part VIII treated atoms as classical particles. The first chapter below separates electrons from nuclei — the Born–Oppenheimer approximation — and explains why the ground-state electron density alone determines the energy landscape on which MD and elasticity ultimately rest.
