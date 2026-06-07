# Part IX — Electronic Structure

Part VIII assumed classical nuclei interacting through potentials fitted to data or theory. Part IX asks where those potentials originate: in the **quantum mechanical electron density** that binds copper atoms into a crystal, sets its cohesive energy, and determines the elastic constants and defect formation energies that every coarser model inherits.

Density functional theory makes the ground-state energy a functional of the electron density — tractable on computers with plane waves, pseudopotentials, and self-consistent field iteration. Born–Oppenheimer separation justifies treating nuclei as classical particles on surfaces defined by electronic structure; Hohenberg–Kohn theorems explain why the density alone suffices.

Two chapters cover Born–Oppenheimer and the Hohenberg–Kohn framework, then Kohn–Sham equations, convergence practice, and the outputs that feed MD, DDD, and continuum models. The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters with **Bridge** sections leading to the epilogue's multiscale coupling story.

## Bridge

Part VIII treated atoms as classical particles. The first chapter below separates electrons from nuclei — the Born–Oppenheimer approximation — and explains why the ground-state electron density alone determines the energy landscape on which MD and elasticity ultimately rest.
