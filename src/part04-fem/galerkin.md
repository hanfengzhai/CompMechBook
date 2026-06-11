# Galerkin method and weighted residuals

## Method of weighted residuals

Consider a PDE operator \(A\) such that \(Au = f\) in \(\Omega\). An approximate solution \(u_h \in V_h\) generally leaves a **residual**

\[
R = f - Au_h \neq 0.
\]

Weighted residual methods seek \(u_h\) such that

\[
\int_\Omega R\, w_h\, dx = 0 \quad \forall w_h \in W_h
\]

for a chosen test space \(W_h\).

## Galerkin choice

**Galerkin method:** \(W_h = V_h\) (same trial and test space).

For the Poisson weak form, this is exactly

\[
a(u_h, v_h) = \ell(v_h) \quad \forall v_h \in V_h.
\]

## Matrix assembly

Let \(\{\phi_i\}_{i=1}^N\) span \(V_h\). Expand \(u_h = \sum_j U_j \phi_j\). Then

\[
\sum_j a(\phi_j, \phi_i)\, U_j = \ell(\phi_i), \qquad i = 1,\ldots,N,
\]

or \(\mathbf{K}\mathbf{U} = \mathbf{F}\) with \(K_{ij} = a(\phi_j, \phi_i)\), \(F_i = \ell(\phi_i)\).

**Symmetry.** If \(a\) is symmetric, \(\mathbf{K}\) is symmetric.

## Rayleigh–Ritz equivalence

For problems with variational energy \(J(u) = \tfrac{1}{2}a(u,u) - \ell(u)\), Galerkin solutions minimize \(J\) over \(V_h\) (discrete energy principle).

## Petrov–Galerkin

If \(W_h \neq V_h\), we obtain Petrov–Galerkin methods—used in stabilized formulations (SUPG, GLS) where standard Galerkin is unstable (advection-dominated problems).

## Penalty and Lagrange multipliers

Constraints (incompressibility, contact) may be enforced via:

- **Penalty terms** added to energy (approximate).
- **Lagrange multipliers** introducing extra unknowns (exact, saddle-point structure).

Mixed \(\mathbb{P}_k\)–\(\mathbb{P}_{k-1}\) elements for Stokes flow exemplify the latter.

## Problem session insight (ME335A)

Session 1 formulates variational problems for PDEs; Session 2 clarifies the **vector space of functions**—trial functions need not satisfy the PDE, only the right regularity and boundary conditions; test functions carry the weighted residual orthogonality.

That clarification prevents a common student error: confusing **approximating the solution** with **approximating the equation** pointwise.

<div class="bridge">

**Bridge.** Galerkin gives the algebraic structure; **shape functions** give \(V_h\) a concrete basis on meshes.

</div>
