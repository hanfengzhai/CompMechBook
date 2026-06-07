# 1. Vectors, Matrices, and Computation

> *Every finite element stiffness matrix, every MD force vector, every DFT Kohn–Sham Hamiltonian begins as a collection of numbers arranged in rows and columns. Linear algebra is the grammar of those arrangements.*

Before we ask what it means for a *function* $u(x)$ to converge to another function, we must be fluent with finite lists of numbers. Linear algebra supplies the vocabulary—vector, matrix, rank, eigenvalue—and the algorithms—elimination, factorization, orthogonalization—that make large-scale computation possible.

This part develops that fluency with an eye on what comes later. Vector spaces generalize to function spaces; inner products generalize to $L^2$ inner products; the Euclidean norm generalizes to Sobolev norms. The finite-dimensional intuition you build here is not a detour; it is the scaffold.

## Chapter map

| Section | Topic | Payoff for later parts |
|---------|-------|------------------------|
| 1.1 | Vectors and matrices | Assembly of FE global matrices |
| 1.2 | Linear systems | Solving $K\mathbf{U}=\mathbf{F}$ |
| 1.3 | Vector spaces | Trial and test spaces in weak forms |
| 1.4 | Orthogonality | $L^2$ projection and least squares |
| 1.5 | Eigenvalues and SVD | Modes, stability, conditioning |
| 1.6 | Norms | Convergence in FA and error estimates |

We proceed in the style of the *Functional Analysis Notes*: definitions first, then examples, then the theorems and techniques that survive discretization.
