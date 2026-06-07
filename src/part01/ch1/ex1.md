## 1.1 Vectors and matrices as data

### Vectors

A **vector** $\mathbf{x} \in \mathbb{R}^n$ is an ordered $n$-tuple of real numbers. In mechanics we meet vectors in two distinct roles:

- **Geometric vectors** in $\mathbb{R}^3$: force, displacement, velocity.
- **Algebraic state vectors** in $\mathbb{R}^n$: nodal displacements in FEM, atomic coordinates flattened in MD, coefficients of a basis expansion.

The distinction matters conceptually but not operationally: both are column matrices, and both transform under linear maps.

### Matrices

A **matrix** $A \in \mathbb{R}^{m \times n}$ represents a linear map $T_A : \mathbb{R}^n \to \mathbb{R}^m$ via $\mathbf{y} = A\mathbf{x}$. Every discretization produces matrices:

| Method | Typical matrix | Unknown vector |
|--------|----------------|----------------|
| FEM (static elasticity) | Stiffness $K$ | Nodal displacements $\mathbf{U}$ |
| FVM (implicit step) | Flux Jacobian | Cell averages $\mathbf{U}^n$ |
| MD (velocity Verlet) | (sparse) force Jacobian for implicit schemes | Position corrections |
| DFT (Kohn–Sham) | Hamiltonian in a basis | Orbital coefficients |

### Matrix multiplication and transpose

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the product $AB$ is defined when the inner dimensions match. The transpose swaps rows and columns: $(AB)^T = B^T A^T$.

**Example (symmetry in mechanics).** The stiffness matrix $K$ from variational elasticity satisfies $K_{IJ} = K_{JI}$ because the bilinear form is symmetric. This is not automatic for every matrix—it is a physical and mathematical property we will derive in Part IV.

### Identity, inverse, and singularity

The **identity** $I_n$ leaves vectors unchanged. A square matrix $A$ is **invertible** if there exists $A^{-1}$ with $A^{-1}A = I$. When $A$ is singular ($\det A = 0$), the linear system $A\mathbf{x} = \mathbf{b}$ either has no solution or infinitely many—a **mechanically singular** structure (rigid body modes not constrained) produces exactly this.

### Block structure and sparsity

Real simulation matrices are rarely dense. A FE stiffness matrix has nonzero entries only where mesh nodes share an element—its **sparsity pattern** mirrors mesh connectivity. Exploiting sparsity (storage formats, fill-reducing orderings) is as important as the underlying algebra.

**Takeaway.** Matrices are not abstract tables; they are the discrete shadows of operators. When Part II introduces the operator $-\nabla \cdot (k \nabla u)$, Part IV will show that its FE discretization is a sparse symmetric positive-definite matrix $K$—the same object we learn to factor in Section 1.2.
