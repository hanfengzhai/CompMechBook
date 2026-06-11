# Weak derivatives and Sobolev spaces

## Motivation

Classical solutions of PDEs require derivatives in the classical sense. Many physical fields have singularities (crack tips, shocks) where classical derivatives fail. **Weak derivatives** extend differentiation to broader function classes.

## Weak derivative

Let \(u \in L^1_{\mathrm{loc}}(\Omega)\). A function \(D^\alpha u \in L^1_{\mathrm{loc}}(\Omega)\) is a **weak derivative** of multi-index \(\alpha\) if

\[
\int_\Omega u\, D^\alpha \phi\, dx = (-1)^{|\alpha|} \int_\Omega (D^\alpha u)\, \phi\, dx
\]

for all smooth test functions \(\phi \in C_c^\infty(\Omega)\) (compact support).

Integration by parts motivates the definition: if \(u\) is smooth, the identity recovers classical derivatives.

## Sobolev spaces

For \(k \in \mathbb{N}\) and \(1 \le p \le \infty\),

\[
W^{k,p}(\Omega) = \{ u \in L^p(\Omega) : D^\alpha u \in L^p(\Omega)\ \forall\, |\alpha| \le k \},
\]

with norm

\[
\|u\|_{W^{k,p}}^p = \sum_{|\alpha|\le k} \|D^\alpha u\|_{L^p}^p.
\]

For \(p=2\), write \(H^k(\Omega) = W^{k,2}(\Omega)\).

**Key space for second-order elliptic FEM:** \(H^1(\Omega)\), with semi-norm \(\|\nabla u\|_{L^2}\).

**Homogeneous Dirichlet boundary conditions:** \(H^1_0(\Omega)\) is the closure of \(C_c^\infty(\Omega)\) in \(H^1\).

## Sobolev embedding (statement)

In 2D and 3D, \(H^1(\Omega) \hookrightarrow L^q(\Omega)\) for bounded domains and \(q \le 2d/(d-2)\) (2D: any finite \(q\); 3D: \(q \le 6\)). Functions in \(H^1\) are not necessarily continuous pointwise in high dimension—only defined almost everywhere.

## Trace theorem

Restriction of \(H^1(\Omega)\) functions to \(\partial\Omega\) defines a bounded operator into \(H^{1/2}(\partial\Omega)\)—making boundary data for Neumann problems meaningful.

## Energy space for elasticity

Vector fields \(\mathbf{u} \in [H^1(\Omega)]^d\) with \(\boldsymbol{\varepsilon}(\mathbf{u}) \in L^2\) form the natural space for weak elasticity. Korn's inequality controls \(\|\nabla \mathbf{u}\|_{L^2}\) by \(\|\boldsymbol{\varepsilon}(\mathbf{u})\|_{L^2}\) modulo rigid motions.

## Galerkin approximation in \(H^1\)

FEM chooses \(V_h \subset H^1_0\). Céa's lemma (Part IV) bounds error in energy norm:

\[
\|u - u_h\|_a \le C \inf_{v_h \in V_h} \|u - v_h\|_a.
\]

Approximation theory in Sobolev spaces (interpolation estimates) connects mesh size \(h\) to convergence rate.

<div class="bridge">

**Bridge (end of Part II).** We now possess the language to state mechanics problems correctly: function spaces for unknowns, bilinear forms for operators, functionals for loads. Part III writes the **governing physics**—balance laws and constitutive equations that become the PDEs we discretize.

</div>
