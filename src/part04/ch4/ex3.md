## 4.3 Shape functions and isoparametric maps

### Reference elements

On a reference interval $[-1,1]$, quadrilateral $[-1,1]^2$, or triangle, **shape functions** $N_a(\xi)$ are fixed polynomials with $N_a(\xi_b) = \delta_{ab}$ at nodes $\xi_b$.

**P1 (linear) triangles** in 2D: $N_a = \lambda_a$ (barycentric coordinates)—three nodes, three functions, $u_h$ linear on each triangle.

**P1 (linear) quads** in 2D: bilinear functions on $[-1,1]^2$—four nodes.

### Isoparametric mapping

Physical element $\Omega_e$ maps from reference $\hat{\Omega}$ via

$$
\mathbf{x}(\xi) = \sum_a \mathbf{x}_a N_a(\xi),
$$

using the **same** shape functions for geometry and solution (**isoparametric**). The Jacobian $J = \partial \mathbf{x}/\partial \xi$ enters integrals:

$$
\int_{\Omega_e} g \, d\Omega = \int_{\hat{\Omega}} g(\mathbf{x}(\xi)) |\det J| \, d\xi.
$$

Gradients transform as $\partial N / \partial \mathbf{x} = J^{-T} \partial N / \partial \boldsymbol{\xi}$.

### Numerical quadrature

Integrals over $\hat{\Omega}$ are evaluated by **Gauss quadrature**—weighted sums at quadrature points. Exact integration of $K^e$ for linear $k$ and P1 elements may use low-order rules; nonlinear materials or curved boundaries need higher order.

### h- and p-refinement

- **h-refinement:** more elements, smaller $h$
- **p-refinement:** higher polynomial degree on fixed mesh

hp methods combine both for optimal convergence on singularities (crack tips, reentrant corners).

**Takeaway.** Shape functions are the bridge between mesh geometry and approximation space. Isoparametric maps let you mesh curved domains without abandoning reference-element quadrature.
