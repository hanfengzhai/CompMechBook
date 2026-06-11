# Molecular dynamics

## The atomistic viewpoint

**Molecular dynamics (MD)** integrates Newton's equations for atoms (or coarse-grained particles):

\[
m_i \frac{d^2 \mathbf{r}_i}{dt^2} = -\nabla_{\mathbf{r}_i} V(\mathbf{r}_1,\ldots,\mathbf{r}_N),
\]

with interaction potential \(V\) encoding chemistry and mechanics.

Where FEM discretizes space and DD discretizes defect lines, MD discretizes **matter into particles**—no PDE mesh in the traditional sense.

## Potentials

| Class | Examples | Use |
|-------|----------|-----|
| Empirical | Lennard-Jones, EAM, Tersoff | metals, semiconductors |
| Reactive | ReaxFF | chemistry |
| Machine-learned | DeePMD, M3GNet | DFT-accurate at MD cost |

The author's *Atomistic Modeling* notes (2022) cover periodic boundaries, integrators, thermostats, and barostats—the infrastructure around the force law.

## Time integration

**Verlet** and **velocity Verlet** are standard:

\[
\mathbf{r}_i^{n+1} = \mathbf{r}_i^n + \Delta t\, \mathbf{v}_i^n + \tfrac{1}{2}(\Delta t)^2 \mathbf{a}_i^n,
\]
\[
\mathbf{v}_i^{n+1} = \mathbf{v}_i^n + \tfrac{1}{2}\Delta t\,(\mathbf{a}_i^n + \mathbf{a}_i^{n+1}).
\]

Stability requires \(\Delta t\) small enough to resolve the highest vibrational frequencies—typically femtoseconds for atomic systems.

## Ensembles

- **NVE:** isolated system, constant energy.
- **NVT:** thermostat (Nosé–Hoover, Langevin) fixes temperature.
- **NPT:** barostat allows stress-controlled loading.

Mechanical loading (uniaxial strain, shear) connects MD to continuum stress–strain curves via **virial stress**.

## Applications in the author's work

- Graphene fracture and thermal gradients (multiscale bridging).
- DeePMD potentials trained on DFT data for fast accurate MD.
- OpenDiS and MD inform dislocation mobility laws at finer scale.

## Limitations

- Time scales: nanoseconds routine, microseconds heroic.
- Length scales: billions of atoms possible on supercomputers, still far below engineering parts.
- Potentials: accuracy is only as good as the force model.

MD is a microscope, not a blueprint for a bridge—unless bridged upward by homogenization or surrogate models.

<div class="bridge">

**Bridge.** MD needs forces. For electrons, forces come from quantum mechanics—often approximated by **density functional theory**.

</div>
