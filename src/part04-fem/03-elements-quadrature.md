# Elements, Shape Functions, and Quadrature

An element is a local coordinate system, a set of shape functions, and a quadrature rule. Together they define how geometry, approximation, and integration interact.

## Reference elements

Common choices:

| Element | Reference domain | Nodes | Order |
|---------|------------------|-------|-------|
| P1 segment | \([0,1]\) | 2 | Linear |
| P1 triangle | Reference triangle | 3 | Linear |
| Q1 quadrilateral | \([-1,1]^2\) | 4 | Bilinear |
| P2 triangle | 3 vertices + 3 edge midpoints | 6 | Quadratic |

**Isoparametric mapping**: geometry and solution use the same shape functions:

\[
\mathbf{x}(\xi) = \sum_a X_a N_a(\xi), \qquad u_h(\xi) = \sum_a U_a N_a(\xi).
\]

Curved boundaries are captured without body-fitted mesh regeneration at the cost of slightly distorted quadrature.

## Shape function properties

On element \(e\), **partition of unity**:

\[
\sum_a N_a(\xi) = 1.
\]

**Kronecker property** at nodes: \(N_a(\xi_b) = \delta_{ab}\). Hence \(u_h(\xi_a) = U_a\) — nodal values are interpolants.

Derivatives transform with the inverse Jacobian:

\[
\nabla_x N_a = \mathbf{J}^{-T} \nabla_\xi N_a.
\]

Ill-conditioned \(\mathbf{J}\) (sliver elements) degrades stiffness conditioning — mesh quality matters.

## Quadrature

Exact integration of polynomials on reference elements uses **Gauss rules**. For P1 triangles in 2D, one-point quadrature suffices for constant \(\nabla N_a \cdot \nabla N_b\). For nonlinear materials, \(\int \boldsymbol{\sigma}(\boldsymbol{\varepsilon}) : \delta\boldsymbol{\varepsilon}\) requires enough points to avoid **hourglassing** and locking.

**Reduced integration** can soften locking in nearly incompressible materials but must be paired with stabilization or mixed formulations.

## Locking and mixed elements

Incompressible or nearly incompressible elasticity with Q1 displacement elements exhibits **volumetric locking**: spurious stresses resist volume change. Remedies:

- Mixed \(u\)–\(p\) elements satisfying LBB
- Selective reduced integration
- Enhanced strain formulations

The pattern repeats in Stokes and incompressible Navier–Stokes.

## Bridge

Poisson's equation is the scalar training ground. Vector elasticity adds tensor constitutive laws, block structure, and boundary traction integrals — but the assembly loop is unchanged.
