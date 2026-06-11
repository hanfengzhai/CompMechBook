# Prologue: Why we compute mechanics

Before we write a single finite element matrix or integrate a single molecular dynamics timestep, we make a quiet promise: **the physics lives in equations, and the computer only sees numbers arranged in tables.**

That promise sounds obvious until one tries to simulate a turbine blade, a polycrystal, or a protein. The blade is a three-dimensional body whose temperature, displacement, and stress vary in space and time. A polycrystal contains millions of grains and defects whose collective behavior produces hardening. A protein is a collection of atoms whose electrons determine the forces between nuclei. Different scales, different physics—yet every simulation pipeline passes through the same three movements:

1. **Model** the phenomenon with equations (often PDEs or conservation laws).
2. **Discretize** those equations so that functions become vectors and operators become matrices.
3. **Solve** the algebraic system and **interpret** the numbers as physical fields.

Linear algebra is the vocabulary of step 2. It is not a detour on the way to "real" mechanics; it is the language in which FEM stiffness matrices, CFD flux Jacobians, and DFT Kohn–Sham Hamiltonians are written.

## A concrete starting point

Consider a truss with \(n\) nodes. Each node may move in two directions, so the displacement vector

\[
\mathbf{u} = (u_1, v_1, u_2, v_2, \ldots, u_n, v_n)^\top \in \mathbb{R}^{2n}
\]

collects all unknown displacements. Hooke's law, in discrete form, becomes

\[
\mathbf{K}\mathbf{u} = \mathbf{f},
\]

where \(\mathbf{K}\) is the **stiffness matrix** and \(\mathbf{f}\) the load vector. The matrix \(\mathbf{K}\) is not arbitrary: it is **symmetric** and, for proper boundary conditions, **positive definite**. Those adjectives are not linear-algebra decoration—they encode conservation of energy and stability of the equilibrium.

The same pattern appears everywhere:

| Scale | Unknown "vector" | Operator / matrix |
|-------|------------------|-------------------|
| Truss FEM | nodal displacements | stiffness matrix |
| Heat conduction FEM | nodal temperatures | conductivity matrix |
| CFD | cell-averaged conserved variables | flux differencing |
| DFT | expansion coefficients of orbitals | Kohn–Sham Hamiltonian |

## What Part I will do

We will develop the linear-algebra tools that reappear in every later chapter:

- **Matrix algebra** and the logic of linear systems.
- **Linear maps**, basis changes, and why stiffness matrices depend on coordinate choices.
- **Eigenvalues** and spectral decompositions—previewing normal modes, stability, and principal stresses.
- **Tensors and index notation**—the bridge to continuum mechanics in Part III.

> **Story beat.** A mechanics student who masters linear algebra does not merely learn to invert matrices. She learns to recognize *structure*: symmetry, definiteness, sparsity, and low-rank updates. That recognition is what separates a naive coder from a computational mechanician.

In the next chapter we begin with vectors and matrices themselves—the alphabet of every simulation we will build.
