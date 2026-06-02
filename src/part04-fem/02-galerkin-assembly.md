# Galerkin's Method and Global Assembly

Global assembly is the finite element algorithm: loop over elements, compute local contributions, scatter into a global matrix. It is structured linear algebra — the change-of-basis story from Part I, executed millions of times.

## Local stiffness and load

On element \(e\), restrict trial functions to polynomial shape functions \(N_a(\xi)\) on a reference element. The **local stiffness** is

\[
k_{ab}^e = \int_{\Omega_e} \nabla N_a \cdot \nabla N_b \, d\Omega.
\]

The **local load** is

\[
f_a^e = \int_{\Omega_e} f N_a \, d\Omega.
\]

Integrals are evaluated by **quadrature** on the reference element, mapped to physical space by the Jacobian \(\mathbf{J}\).

## Assembly

Let \(\mathbf{L}_e\) map local DOF indices to global indices. Then

\[
\mathbf{K} = \sum_e \mathbf{L}_e^T \mathbf{k}^e \mathbf{L}_e, \qquad \mathbf{F} = \sum_e \mathbf{L}_e^T \mathbf{f}^e.
\]

Sparse storage exploits the fact that \(k_{ab}^e \neq 0\) only when nodes \(a\) and \(b\) share an element.

## Example: 1D linear bar element

On \([x_1, x_2]\) with linear shape functions \(N_1 = 1-\xi\), \(N_2 = \xi\), \(\xi \in [0,1]\):

\[
\mathbf{k}^e = \frac{EA}{h}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Two elements in series assemble to a tridiagonal global stiffness — the discrete analog of \(-u''\).

## 2D Poisson with P1 triangles

Each triangle carries three nodes; shape functions are linear barycentric coordinates. Gradients are constant on each element; stiffness integrals reduce to area times gradient dot products. The global matrix pattern reflects the mesh graph: row \(i\) has nonzeros in columns for neighbors of node \(i\).

## Data structures

Production codes store:

- **Mesh**: nodes, element connectivity, boundary markers
- **DOF map**: node + component → global index (for vector problems)
- **Sparsity pattern**: precomputed from connectivity
- **Quadrature tables**: points and weights on reference elements

FEniCS and Firedrake automate symbolic weak form translation into this loop; understanding assembly remains essential for debugging and custom elements.

## Bridge

Shape functions and quadrature rules determine accuracy and cost. The next chapter details elements from P1 triangles to higher-order spectral elements — and the quadrature that makes nonlinear materials tractable.
