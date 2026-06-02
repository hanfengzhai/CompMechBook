# Compactness and the Spectral Theorem

Eigenvalues decouple finite-dimensional systems. The spectral theorem does the same for self-adjoint operators on Hilbert spaces — and explains why modal analysis, buckling, and heat diffusion share the same mathematical skeleton.

## Self-adjoint operators

A bounded operator \(A: H \to H\) is **self-adjoint** if

\[
(Au, v) = (u, Av) \quad \forall u,v \in H.
\]

For unbounded operators (like \(-\Delta\) with Dirichlet BCs), self-adjointness requires careful domain specification. The Laplacian on \(H^1_0(\Omega)\) associated with the form \(a(u,v) = \int \nabla u \cdot \nabla v\) is self-adjoint and positive.

## The spectral theorem (compact case)

If \(A\) is compact and self-adjoint, then:

1. \(A\) has a countable sequence of real eigenvalues \(\lambda_n \to 0\) (or \(\to\infty\) for inverse operators).
2. Eigenvectors \(\{\phi_n\}\) form an orthonormal basis of \(H\).
3. \(A = \sum_n \lambda_n (\cdot, \phi_n)\phi_n\).

For the Laplacian with Dirichlet conditions, eigenvalues grow: \(0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty\), with eigenfunctions \(\phi_n\) becoming increasingly oscillatory.

## Rayleigh–Ritz characterization

The \(n\)-th eigenvalue satisfies

\[
\lambda_n = \min_{\substack{W \subset H \\ \dim W = n}} \max_{0 \neq w \in W} \frac{a(w,w)}{(w,w)_{L^2}}.
\]

Finite element eigenvalues are obtained by restricting the Rayleigh quotient to \(V_h\). They **over-estimate** the true eigenvalues from below (for the standard Laplacian) — a useful sanity check in vibration analysis.

## Heat equation and modal decay

Solutions of \(u_t - \Delta u = 0\) expand as

\[
u(x,t) = \sum_n c_n e^{-\lambda_n t} \phi_n(x).
\]

High modes decay fast; low modes persist. Explicit time integrators must resolve the largest \(\lambda_n\) on the mesh — another eigenvalue stability story linking Part II to time-dependent PDEs.

## Connection to Part III

We now possess:

- Hilbert spaces for admissible fields
- Bilinear forms for energy
- Compactness for discrete approximations
- Spectral theory for modes and stability

Part III applies this toolkit to PDEs: strong forms for intuition, weak forms for computation, Sobolev spaces for regularity, energy methods for well-posedness. The finite element method of Part IV is waiting at the end of that road.
