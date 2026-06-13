# Part VIII — Atomistic Simulation

Parts I–VII treated the copper wire as a continuum or a network of line defects. Part VIII descends to the scale where matter resolves into **individual atoms** — nuclei moving on a potential energy surface, thermal vibrations exchanging energy with a heat bath, bonds stretching and breaking at crack tips where no elliptic PDE can remain valid without regularization.

Consider the notch root on a copper wire specimen. Part VI's stress concentration factor predicts infinite stress at a sharp corner; Part VII's dislocation pile-up regularizes the field but still assumes a continuum core structure. At the atomistic scale, bonds stretch across the notch, surfaces nucleate, and fracture initiates through rearrangements that only a trajectory in phase space can resolve. Molecular dynamics (MD) is the workhorse that captures this physics — and supplies the interatomic potentials, stacking-fault energies, and mobility parameters that Parts VI and VII inherit rather than derive.

MD is also where **temperature** enters honestly. The wire heated by electric current (prologue) exchanges energy through atomic vibrations; ensembles and thermostats translate that microscopic kinetics into the temperature fields that Part V's conjugate heat transfer and Part VI's thermal expansion models approximate.

## What this part covers

| Chapter | Focus | Copper wire connection |
|---------|-------|------------------------|
| 01 — Potentials & phase space | Lennard-Jones, EAM, Hamiltonian mechanics | Cohesive energy and elastic constants feeding continuum moduli |
| 02 — Ensembles & integrators | NVE, NVT, NPT; Verlet, LAMMPS workflows | Annealing kinetics after drawing; thermal conductivity estimates |
| 03 — Ab initio & coarse-graining | AIMD, EAM fitting, upward exports | Closing the loop to DFT (Part IX) and downward to DDD mobility |

The layout follows the **MD Notes** in [`writings/md/`](../../writings/md/): numbered chapters with **Bridge** sections and explicit upward links to DDD (Part VII) and DFT (Part IX), matching the [Functional Analysis Notes](../functional-analysis/) structure.

## The atomistic question

At the atomic scale the four prologue questions become:

- **State**: positions and momenta \(\{(\mathbf{r}_i, \mathbf{p}_i)\}\) (or velocities) for \(N \sim 10^3\)–\(10^9\) atoms.
- **Equations**: Newton's laws on a potential energy surface \(V(\{\mathbf{r}_i\})\), optionally coupled to a thermostat or barostat.
- **Discretization**: timestep \(\Delta t\), cutoff radius, neighbor lists, periodic boundary conditions on a simulation box.
- **Upward export**: fitted potentials, surface energies, mobility tables, fracture trajectories, thermal transport coefficients.

Classical MD assumes nuclei follow **Born–Oppenheimer** surfaces defined by electrons. Part IX derives those surfaces; Part VIII shows how to simulate on them at scale.

## Bridge

Part VII ended with dislocation lines and the admission that atoms matter at cores and crack tips. The first chapter below puts those atoms back: phase space, Hamiltonian mechanics, and the interatomic potentials that define forces in every MD simulation of copper.
