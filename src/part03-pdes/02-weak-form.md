# Weak Formulations and Test Functions

The weak form is the computational mechanic's version of integration by parts: move derivatives from the unknown solution onto smooth test functions, trading pointwise differentiability for integral balance.

## Derivation: Poisson with Dirichlet BCs

Start with \(-\Delta u = f\) in \(\Omega\), \(u = 0\) on \(\partial\Omega\). Multiply by a test function \(v\) that also vanishes on the boundary:

\[
\int_\Omega (-\Delta u)\, v \, d\Omega = \int_\Omega f v \, d\Omega.
\]

Integrate by parts (Green's first identity):

\[
\int_\Omega \nabla u \cdot \nabla v \, d\Omega - \int_{\partial\Omega} \frac{\partial u}{\partial n} v \, dS = \int_\Omega f v \, d\Omega.
\]

With \(v = 0\) on \(\partial\Omega\), the boundary term vanishes. The **weak form** seeks \(u \in V = H^1_0(\Omega)\) such that

\[
a(u,v) = \ell(v) \quad \forall v \in V,
\]

where

\[
a(u,v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega, \qquad \ell(v) = \int_\Omega f v \, d\Omega.
\]

## The Lax–Milgram theorem in action

For \(f \in L^2(\Omega)\):

- \(a(\cdot,\cdot)\) is **continuous** on \(H^1_0 \times H^1_0\)
- \(a(\cdot,\cdot)\) is **coercive** on \(H^1_0\) (Poincaré inequality)
- \(\ell(\cdot)\) is continuous on \(H^1_0\)

Hence a **unique weak solution** exists. Moreover, it minimizes the energy functional

\[
\Pi(u) = \tfrac{1}{2}a(u,u) - \ell(u).
\]

## Virtual work in elasticity

For displacements, the weak form is the **principle of virtual work**:

\[
\int_\Omega \boldsymbol{\sigma} : \delta\boldsymbol{\varepsilon} \, d\Omega = \int_\Omega \mathbf{f}\cdot\delta\mathbf{u} \, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\delta\mathbf{u} \, dS
\]

for all kinematically admissible virtual displacements \(\delta\mathbf{u}\). Linearization yields the bilinear form used in FEM.

## Natural boundary conditions

Neumann data \( \partial u / \partial n = h\) enters the weak form as a boundary integral:

\[
\int_\Omega \nabla u \cdot \nabla v = \int_\Omega f v + \int_{\Gamma_N} h v.
\]

Dirichlet data are **essential** — enforced strongly on the trial space. Neumann data are **natural** — appear automatically in the weak form. This distinction guides FEM boundary implementation.

## Galerkin discretization (preview)

Choose \(V_h = \text{span}\{\phi_1,\ldots,\phi_N\} \subset V\). Seek

\[
u_h = \sum_j U_j \phi_j
\]

such that

\[
a(u_h, \phi_i) = \ell(\phi_i) \quad i = 1,\ldots,N.
\]

This is a linear system \(\mathbf{K}\mathbf{U} = \mathbf{F}\). Part IV implements this pipeline.

## Bridge

Weak derivatives make sense in **Sobolev spaces**. The next chapter defines \(H^1\) rigorously enough to code with confidence — and explains why conforming finite elements must be continuous across element boundaries (for standard Lagrange elements).
