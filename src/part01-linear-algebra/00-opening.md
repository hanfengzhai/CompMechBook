# Part I — The Grammar of Computation

Every simulation, at every scale, eventually reduces to finite-dimensional algebra. A million-node finite element model solves \(\mathbf{K}\mathbf{u}=\mathbf{f}\). A Kohn–Sham self-consistent cycle diagonalizes a Hamiltonian matrix. A molecular dynamics timestep updates positions with a force vector assembled from pairwise interactions. The software changes; the pattern does not.

This part refreshes the linear algebra that those reductions assume: vectors and matrices as the syntax of state, linear maps as the syntax of evolution, eigenvalues as the syntax of stability and modes. We work in \(\mathbb{R}^N\) not because mechanics is linear, but because discretization makes it finite — and because the infinite-dimensional limits of Part II and Part III are understood by watching what happens as \(N\) grows.

The copper wire from the prologue appears here as a chain of coupled springs (a bar in axial elasticity), a thermal network (nodes along its length), and a vibration problem whose natural frequencies are eigenvalues of a stiffness–mass pair. By the end of Chapter 4 we will see why a temperature field \(T(x)\) is not a vector in any fixed \(\mathbb{R}^N\), yet every mesh approximation of \(T\) is.

The layout follows the **Linear Algebra Notes** in [`writings/linear-algebra/`](../../writings/linear-algebra/): numbered chapters, mechanics-motivated examples, and a **Bridge** at the end of each chapter. Read the four chapters in order; Chapter 4 hands off directly to Part II, where functions replace vectors and operators replace matrices.
