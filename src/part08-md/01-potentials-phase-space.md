# Interatomic Potentials and Phase Space

Molecular dynamics (MD) treats atoms as classical particles interacting through potentials fitted to quantum data or experiments. It is the workhorse of atomistic materials mechanics.

## Phase space and Hamiltonian

For \(N\) atoms with positions \(\mathbf{r}_i\) and momenta \(\mathbf{p}_i\), the **Hamiltonian** is

\[
H = \sum_i \frac{\|\mathbf{p}_i\|^2}{2m_i} + V(\{\mathbf{r}_i\}).
\]

Newton's equations (or Hamilton's equations) govern trajectories:

\[
m_i \ddot{\mathbf{r}}_i = -\nabla_{\mathbf{r}_i} V.
\]

## Interatomic potentials

| Class | Form | Use case |
|-------|------|----------|
| Lennard-Jones | Pairwise \(r^{-12} - r^{-6}\) | Noble gases, benchmarks |
| EAM / MEAM | Many-body embedding | Metals |
| Tersoff / Stillinger–Weber | Bond order | Covalent solids (Si, C) |
| ReaxFF | Reactive | Chemistry, fracture |
| ML potentials | Neural network on local env | DFT accuracy at MD cost |

The author's [atomistic modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf) and graphene fracture studies illustrate MD for crack propagation and thermal effects — where continuum fields cannot resolve bond breaking.

## Periodic boundaries and defects

Crystals use **periodic boundary conditions** to mimic bulk behavior. Defects are introduced by removing/adding atoms or using flexible boundary methods coupling to continuum elasticity.

## Bridge

Potentials define forces; integrators and statistical ensembles define how trajectories sample the correct thermodynamic state — the subject of the next chapter.
