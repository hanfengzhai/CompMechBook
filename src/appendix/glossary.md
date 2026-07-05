# Glossary and Cross-Scale Index

This appendix is a **reverse index** for reading the book as one continuous story. When a symbol or phrase reappears in a new part, use the tables below to see what it meant earlier — and where the copper wire carries the same idea under new vocabulary.

The layout mirrors the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf): at every scale, four questions organize the material — **object**, **structure**, **theorem**, **failure mode**. Part openings and closing checkpoints state these explicitly; this page collects them in one place.

## The four questions at every scale

| Part | Object | Structure | Theorem / principle | What breaks |
|------|--------|-----------|---------------------|-------------|
| I | \(\mathbf{u}\), \(\mathbf{K}\), eigenmodes | Inner product, symmetry, sparsity | SPD \(\mathbf{K}\) \(\Rightarrow\) unique equilibrium; spectral theorem | Ill-conditioning; \(N\to\infty\) without target space |
| II | Fields \(u\), operators \(A\) | Norm, completeness, Hilbert geometry | Lax–Milgram; Galerkin best approximation | Cauchy sequences leave the space |
| III | \(u(\mathbf{x},t)\) on \(\Omega\) | Strong/weak form, energy functional | Energy minimization; well-posedness in \(H^1\) | Corners, delta loads, non-physical oscillations |
| IV | \(V_h\), shape functions, \(\mathbf{K}\) | Galerkin orthogonality, \(h\)-refinement | Céa lemma; a priori rates | Locking, hourglass modes, pollution |
| V | Cell averages, fluxes | Conservation on control volumes | Godunov/Riemann upwinding | Diffusion instability; wrong wall flux |
| VI | \(\mathbf{F}\), \(\boldsymbol{\sigma}\), \(\mathbb{C}\) | Objectivity, balance laws | Virtual work; hyperelastic energy | Yield, notches — need mesoscale physics |
| VII | Dislocation segments, density | Peach–Köhler, mobility law | Taylor hardening; forest statistics | Polycrystal texture; link-length tails |
| VIII | \(\{\mathbf{r}_i\}\), potential \(V\) | Hamiltonian, thermostats, PBC | Symplectic energy conservation; ergodic sampling | Energy drift; cutoff artifacts |
| IX | \(\rho(\mathbf{r})\), KS orbitals | Hohenberg–Kohn; SCF loop | Variational ground state; force theorem | Wrong functional; k-mesh too coarse |

See the [chapter roadmap](sources.md) for one-line roles of every numbered chapter.

## Recurring symbols (same habit, new meaning)

| Symbol | Part I | Part II–III | Part IV–V | Part VI | Part VII–IX |
|--------|--------|-------------|-----------|---------|-------------|
| \(u\) | Nodal displacement vector | Displacement field \(u(x)\) | FEM DOFs; FVM scalar fields | \(\mathbf{u}(\mathbf{X})\) | — |
| \(\mathbf{K}\) | Stiffness matrix | — (operator \(A\)) | Assembled stiffness | Elastic tensor \(\mathbb{C}\) in integrals | — |
| Energy | \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | \(\|u\|_{H^1}\), bilinear form | Element strain energy | \(\int \boldsymbol{\sigma}:\boldsymbol{\varepsilon}\) | \(E_{\text{coh}}\), stacking fault \(\gamma_{\text{sf}}\) |
| Modes | Eigenvectors of \(\mathbf{K}\) | Orthonormal basis in \(H^1\) | Shape functions \(\phi_i\) | Normal modes of bar | Slip systems; phonon bands (MD) |
| Load | \(\mathbf{f}\) | Linear functional \(\ell(v)\) | Neumann data, body force | Traction \(\mathbf{t}\) | Peach–Köhler force on dislocations |
| Mesh / basis | Spring network | Refinement limit \(h\to 0\) | Elements, quadrature | Same FEM mesh | Supercell (MD/DFT); segment mesh (DDD) |

**Reading tip:** When Part IX writes a self-consistent **eigenvalue loop**, read it as Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) with the operator replaced by the Kohn–Sham Hamiltonian and the basis replaced by plane waves — the [Part IX opening](../part09-dft/00-opening.md) states this parallel explicitly.

## The copper wire: state variable by part

| Part | What we track on the wire | Typical code / method |
|------|---------------------------|------------------------|
| Prologue | All scales at once (preview) | — |
| I | Spring displacements, vibration modes | Hand calculation, NumPy |
| II | \(u(x)\), \(T(x)\) as limits of refinement | Analysis only |
| III | Weak forms for elasticity and heat | Pen-and-paper → FEM input |
| IV | Nodal \(\mathbf{U}\) on a solid mesh | FEniCS, Abaqus-style assembly |
| V | Air velocity, pressure, enthalpy flux | OpenFOAM-style FVM |
| VI | \(\mathbf{F}\), \(\boldsymbol{\sigma}\), yield preview | Continuum post-processing |
| VII | Dislocation density, link statistics | OpenDiS, ParaDiS → DAMASK |
| VIII | Atomic positions, stresses from EAM | LAMMPS |
| IX | \(\rho(\mathbf{r})\), total energy, \(C_{ij}\) | Quantum ESPRESSO, VASP |
| Epilogue | Coupled workflows across rows | Sequential / concurrent multiscale |

## Lab act index (prologue's six acts)

The [prologue](../prologue/00-many-scales.md#the-experiment-as-plot) maps the copper wire to **six lab acts** — laboratory time, not part number. Use this table when a chapter feels abstract: locate the act, then read the matching part opening's **Lab act** section.

| Act | Lab event | Parts | What the book computes |
|-----|-----------|-------|------------------------|
| **I — Mounting** | Specimen gripped; load cell zeroed | Prologue, I | \(\mathbf{K}\mathbf{u}=\mathbf{f}\); bar elements |
| **II — Warming** | Current on; air cools surface | III, IV, V | Heat PDE → FEM conduction; FVM convection |
| **III — Pulling** | Grip displacement ramps (linear regime) | II, III, IV, VI | Weak forms; Galerkin; Cauchy stress |
| **IV — Hardening** | Force–displacement curve bends | VII | DDD; Taylor hardening |
| **V — Notch** | Stress concentration at scratch/corner | VI, VIII | Atomistic resolution; EAM calibration |
| **VI — Foundation** | Parameters chosen before the test | IX → VIII → VII → IV | DFT → MD → DDD → FEM inputs |

Mathematical reading order (Parts I–IX) and lab act order differ by design: Act VI is a **prequel** run offline; Acts II–III interleave analysis and discretization across Parts II–V.

## Narrative hinges (where to look if the story jumps)

| If you feel a jump between… | Read first… |
|-----------------------------|-------------|
| Springs and function spaces | [I.4 Bridge](../part01-linear-algebra/04-toward-infinity.md) → [II.0 opening](../part02-functional-analysis/00-opening.md) |
| Analysis and meshing | [III.4 Bridge](../part03-pdes/04-energy-methods.md) → [IV.0 opening](../part04-fem/00-opening.md) |
| FEM and fluids | [IV.5 Bridge](../part04-fem/05-convergence.md) (two doors) or [V.0 opening](../part05-fvm/00-opening.md) |
| PDE codes and stress tensors | [VI.0 Story so far](../part06-continuum/00-opening.md) |
| Smooth elasticity and dislocations | [VI.4 Bridge](../part06-continuum/04-nonlinear-plasticity-preview.md) → [VII.0](../part07-defects/00-opening.md) |
| Continuum moduli and atoms | [VII.3 Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md) → [VIII.0](../part08-md/00-opening.md) |
| Potentials and electrons | [VIII.3 Bridge](../part08-md/03-ab-initio-and-coarse-graining.md) → [IX.0](../part09-dft/00-opening.md) |
| DFT and full multiscale | [IX.3 Bridge](../part09-dft/03-dft-workflows.md) → [Epilogue](../epilogue/multiscale.md) |

Every numbered chapter also ends with its own **Bridge** section — the primary narrative hinge within a part.

## Abbreviations

| Term | Meaning | First major appearance |
|------|---------|------------------------|
| FEM | Finite element method | Part IV |
| FVM | Finite volume method | Part V |
| CFD | Computational fluid dynamics | Part V.4 |
| PDE | Partial differential equation | Part III |
| DDD | Dislocation dynamics | Part VII |
| MD | Molecular dynamics | Part VIII |
| DFT | Density functional theory | Part IX |
| SCF | Self-consistent field | Part IX |
| EAM | Embedded atom method | Part VIII |
| PBC | Periodic boundary conditions | Part VIII |
| CHT | Conjugate heat transfer | Part V.4, Epilogue |

## Canonical sources

Chapter markdown is authored under [`writings/`](../../writings/) (Functional Analysis Notes layout) and synced into `src/` via [`scripts/sync-writings.sh`](../../scripts/sync-writings.sh). For PDF links, repositories, and the full chapter roadmap, see [Sources and Further Reading](sources.md).
