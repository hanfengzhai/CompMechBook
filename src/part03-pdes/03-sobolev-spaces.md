# Sobolev Spaces: Regularity for Computation

Sobolev spaces measure how much smoothness a function has in an \(L^2\) sense. They are the native habitat of weak solutions and conforming finite elements.

## Weak derivatives

A function \(u \in L^2(\Omega)\) has **weak derivative** \(\partial u / \partial x_i = w \in L^2(\Omega)\) if

\[
\int_\Omega u \frac{\partial \phi}{\partial x_i} = -\int_\Omega w \phi \quad \forall \phi \in C_c^\infty(\Omega).
\]

Integration by parts in the classical sense becomes a **definition** in the weak sense. Functions with kinks can have well-defined weak derivatives; the derivative is itself a function in \(L^2\), not a delta distribution at the kink (unless we enlarge the space).

## The Sobolev space \(H^1(\Omega)\)

\[
H^1(\Omega) = \left\{ u \in L^2(\Omega) : \frac{\partial u}{\partial x_i} \in L^2(\Omega),\; i = 1,\ldots,d \right\}
\]

with norm

\[
\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2.
\]

\(H^1(\Omega)\) is a Hilbert space. **Sobolev embedding** in 2D and 3D: \(H^1 \hookrightarrow L^p\) for \(p \le 2d/(d-2)\) — in 3D, \(H^1 \hookrightarrow L^6\).

## Boundary traces

Functions in \(H^1(\Omega)\) have **traces** on \(\partial\Omega\): there exists a bounded operator \(\gamma: H^1(\Omega) \to L^2(\partial\Omega)\) such that \(\gamma u = u|_{\partial\Omega}\) when \(u\) is smooth. Dirichlet boundary conditions are imposed on \(\gamma u\).

The subspace

\[
H^1_0(\Omega) = \{ u \in H^1(\Omega) : \gamma u = 0 \text{ on } \partial\Omega \}
\]

is closed. It is the standard trial space for homogeneous Dirichlet problems.

## Poincaré inequality

For bounded \(\Omega\),

\[
\|u\|_{L^2} \le C_P \|\nabla u\|_{L^2} \quad \forall u \in H^1_0(\Omega).
\]

Coercivity of the Laplacian bilinear form on \(H^1_0\) follows. The constant \(C_P\) depends on domain geometry — narrow domains have large \(C_P\), worsening conditioning of stiffness matrices.

## Conforming finite elements

A **conforming** finite element space \(V_h \subset H^1(\Omega)\) satisfies:

1. Global continuity across element interfaces (for scalar Lagrange elements)
2. Polynomial structure on each element

Non-conforming methods (discontinuous Galerkin) enlarge the space and weakly enforce continuity through numerical fluxes — common in hyperbolic problems (Part V).

## Higher-order Sobolev spaces

\(H^2(\Omega)\) requires weak second derivatives in \(L^2\). Classical \(C^2\) solutions of Poisson's equation live in \(H^2\), enabling **optimal** \(H^1\) error estimates for linear elements on smooth domains. Corner singularities reduce regularity; adaptive mesh refinement targets the resulting localized loss of \(H^2\) regularity.

## Bridge

Energy methods package weak forms as minimization problems. They unify FEM, provide physical intuition, and extend naturally to nonlinear elasticity where the energy functional may be polyconvex rather than quadratic.
