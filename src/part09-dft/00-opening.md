# Part IX — Electronic Structure

Part VIII assumed interatomic potentials — Lennard-Jones, EAM, ReaxFF — as given inputs. Those potentials encode quantum mechanical bonding in fitted functional forms. At the finest rung of the ladder, we return to the electrons themselves.

Density functional theory (DFT) solves for the ground-state electron density and energy of a collection of nuclei. Born–Oppenheimer separation decouples fast electrons from slow nuclei; the Hohenberg–Kohn theorems guarantee that the density determines the energy; the Kohn–Sham equations make the problem computable as a self-consistent field iteration on orbitals. The copper wire's cohesive energy, elastic moduli, surface energies, and vacancy formation energies — the numbers that MD potentials and continuum models import — begin here.

The layout follows the **DFT Notes** in [`writings/dft/`](../../writings/dft/): numbered chapters aligned with MSE 5720 coursework, practical convergence guidance, and a **Bridge** to the epilogue, where all scales compose into multiscale workflows.
