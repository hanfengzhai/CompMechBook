# Shape functions and assembly

## Mesh and elements

Partition \(\Omega\) into elements \(\Omega_e\), \(e = 1,\ldots,n_{\mathrm{el}}\). On each element, approximate \(u\) with local shape functions \(\mathbf{N}_e(\xi)\) in reference coordinates \(\xi\).

**Linear 1D bar element** (nodes at \(\xi=0,1\)):

\[
N_1(\xi) = 1-\xi, \qquad N_2(\xi) = \xi.
\]

Displacement interpolates as \(u_h = N_1 d_1 + N_2 d_2\) with nodal DOFs \(d_1, d_2\).

## Local stiffness

For 1D Poisson with conductivity \(k\),

\[
k_e = \int_{\Omega_e} B^\top D B\, dx, \qquad B = \frac{dN}{dx}.
\]

**2D triangle P1:** \(u_h\) is linear on each triangle, continuous across edges—\(V_h \subset H^1\).

## Isoparametric mapping

Map reference element \(\hat\Omega\) to physical \(\Omega_e\) via \(\mathbf{x} = \sum_k N_k(\xi)\mathbf{x}_k\).

\[
\int_{\Omega_e} (\cdot)\, dx = \int_{\hat\Omega} (\cdot)\, |\det J|\, d\xi,
\]

with Jacobian \(J = \partial \mathbf{x}/\partial \xi\).

## Assembly

**Local-to-global map** (ME335A Session 4): element DOFs connect to global indices via connectivity array. Add \(k_e\) entries into global \(\mathbf{K}\).

Pseudocode:

```
K = zeros(n_dof, n_dof)
for e in elements:
    ke = element_stiffness(e)
    for i, I in connectivity(e):
        for j, J in connectivity(e):
            K[I,J] += ke[i,j]
```

## Numerical integration

Gauss quadrature integrates \(k_e\) exactly for polynomial integrands (P1 elasticity on affine triangles: 1-point rule suffices for constant \(B\)).

## 2D Poisson workflow (Firedrake / FEniCS tutorials)

Teaching tutorials solve \(-\Delta u = f\) on \(\Omega = (0,1)^2\) with \(u=0\) on \(\partial\Omega\):

1. Build mesh.
2. Define function space (e.g. `Lagrange` P1).
3. Specify weak form `dot(grad(u), grad(v))*dx == f*v*dx`.
4. Apply Dirichlet BCs.
5. Solve linear system.

The abstractions hide assembly but execute exactly the mathematics above.

<div class="bridge">

**Bridge.** Assembly produces \(\mathbf{u}_h\); **convergence theory** tells us when \(\mathbf{u}_h\) approaches \(u\).

</div>
