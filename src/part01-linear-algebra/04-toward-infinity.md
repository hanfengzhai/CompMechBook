# From \(\mathbb{R}^n\) to Functions: The First Step Up

So far our state vectors have had finite length \(N\). A temperature field on a bar, however, is specified by a value at **every** point \(x \in [0,L]\). Informally, that is infinitely many degrees of freedom. Making this precise without losing the linear-algebraic intuition is the job of functional analysis — but we can already see the path.

## Functions as infinite vectors

Discretize a function \(u(x)\) on \([0,L]\) by sampling at \(N\) points:

\[
u_i \approx u(x_i), \quad i = 1,\ldots,N.
\]

The vector \(\mathbf{u} \in \mathbb{R}^N\) is a **proxy** for the function. Refining the mesh increases \(N\). The limit \(N \to \infty\) suggests a function \(u: [0,L] \to \mathbb{R}\).

We add and scale functions pointwise:

\[
(\alpha u + \beta v)(x) = \alpha u(x) + \beta v(x),
\]

just as we add and scale vectors componentwise. Function spaces are vector spaces — often infinite-dimensional ones.

## Inner products on functions

The **\(L^2\) inner product** on \([0,L]\) is

\[
(u, v)_{L^2} = \int_0^L u(x)\, v(x)\, dx.
\]

This replaces the sum \(\sum_i u_i v_i\). The associated norm is

\[
\|u\|_{L^2} = \sqrt{(u,u)_{L^2}}.
\]

In finite elements, \(\mathbf{M}\) approximates this inner product on the subspace of mesh functions:

\[
\mathbf{u}^T \mathbf{M} \mathbf{v} \approx \int_\Omega u_h v_h \, d\Omega.
\]

## Matrices become operators

A matrix \(\mathbf{K}\) maps \(\mathbb{R}^N \to \mathbb{R}^N\). A **linear operator** \(K\) maps a function space to itself. The discrete problem \(\mathbf{K}\mathbf{u}=\mathbf{f}\) approximates

\[
K u = f \quad \text{in a domain},
\]

with boundary conditions. For Poisson's equation \(-u'' = f\) on \((0,L)\), the operator is differentiation twice, inverted by integration twice plus boundary data.

## Why infinity changes the questions

In finite dimensions:

- Every Cauchy sequence converges (in \(\mathbb{R}^N\)).
- Every bounded sequence has a convergent subsequence (Bolzano–Weierstrass).

In infinite-dimensional function spaces, these fail without extra structure. **Completeness** (Cauchy sequences converge) and **compactness** (bounded sets behave nicely) become nontrivial requirements. Part II develops the spaces where standard PDE and FEM theory lives.

## The central cast, introduced early

Three spaces will dominate the rest of the book:

| Space | Norm / inner product | Role |
|-------|---------------------|------|
| \(L^2(\Omega)\) | \(\|u\|_{L^2}^2 = \int \|u\|^2\) | Energy of fields, least squares |
| \(H^1(\Omega)\) | \(\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2\) | Weak derivatives, FEM |
| Product spaces | Mixed norms | Fluids (velocity–pressure), contact |

We do not need full rigor yet. We need the picture: **finite elements are linear algebra in \(H^1\)**.

## Bridge to Part II

Linear algebra taught us to solve \(\mathbf{K}\mathbf{u}=\mathbf{f}\). Mechanics asks us to solve PDEs. The bridge is:

1. Write the PDE in **weak form** (multiply by a test function, integrate by parts).
2. Choose a finite-dimensional subspace \(V_h \subset H^1\).
3. Solve the resulting matrix system.

Steps 1–2 require function spaces. Part II supplies them — and explains why the approximations converge as \(h \to 0\).

Turn the page. We leave the comfort of \(\mathbb{R}^N\) and enter the space of admissible fields.
