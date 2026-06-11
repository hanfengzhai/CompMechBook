# Strong and weak forms of boundary-value problems

## Strong form

A **boundary-value problem** combines a PDE on \(\Omega\), boundary conditions on \(\partial\Omega\), and possibly initial conditions.

**Poisson (scalar prototype):**

\[
-\Delta u = f \text{ in } \Omega, \qquad u = 0 \text{ on } \partial\Omega.
\]

**Linear elasticity:**

\[
-\mathrm{div}(\mathbb{C}\boldsymbol{\varepsilon}(\mathbf{u})) = \mathbf{f} \text{ in } \Omega,
\qquad \mathbf{u} = \mathbf{0} \text{ on } \Gamma_D.
\]

Strong solutions require classical smoothness—often too strict for re-entrant corners, interfaces, and shocks.

## Weak form derivation

Multiply the Poisson equation by test function \(v\) with \(v=0\) on \(\partial\Omega\), integrate, and integrate by parts:

\[
\int_\Omega \nabla u\cdot\nabla v\, dx = \int_\Omega f v\, dx.
\]

Seek \(u \in H^1_0(\Omega)\) such that the equality holds for all \(v \in H^1_0(\Omega)\).

**Why this works.** Integration by parts transfers derivatives from \(u\) to \(v\), lowering regularity demands on \(u\) while requiring \(v\) smooth enough to integrate.

## Bilinear forms and coercivity

Write \(a(u,v) = \int \nabla u\cdot\nabla v\) and \(\ell(v) = \int f v\). Coercivity:

\[
a(u,u) = \|\nabla u\|_{L^2}^2 \ge C \|u\|_{H^1}^2
\]

follows from Poincaré inequality on \(H^1_0\).

Lax–Milgram guarantees a unique weak solution.

## Natural boundary conditions

For mixed boundary \(\partial\Omega = \Gamma_D \cup \Gamma_N\),

\[
a(u,v) = \ell(v) + \int_{\Gamma_N} g v\, dS,
\]

with Neumann data \(g = \partial u/\partial n\) arising **naturally** from integration by parts—no need to enforce them strongly on trial functions beyond the Dirichlet part.

## Hyperbolic vs elliptic (preview)

| Type | Example | Weak form character |
|------|---------|---------------------|
| Elliptic | Poisson, elasticity | Coercive, global coupling |
| Parabolic | Heat equation | Time + elliptic in space |
| Hyperbolic | Wave, Euler | Characteristics, upwinding |

FEM dominates elliptic/parabolic problems; FVM (Part V) excels at hyperbolic conservation laws.

## Teaching note connection

Stanford ME335A problem sessions progress deliberately:

1. **Variational formulation** of PDEs.
2. **Vector space of functions** and clarification of concepts.
3. **Shape functions** and local-to-global assembly.

That pedagogical path mirrors this book: functional analysis first, then FEM.

<div class="bridge">

**Bridge (end of Part III).** Physics is written as PDEs; weak forms make them computable. Part IV implements the Galerkin method—FEM as projection onto finite element spaces.

</div>
