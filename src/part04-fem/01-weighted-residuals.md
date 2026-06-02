# The Method of Weighted Residuals

The finite element method is one member of a family: **weighted residual methods**. They all seek an approximate solution that makes a PDE residual small in a weighted average sense.

## Residuals

For a differential operator \(\mathcal{L}\) and right-hand side \(f\), the **residual** of an approximation \(u_h\) is

\[
r = f - \mathcal{L} u_h.
\]

If \(u_h\) were exact, \(r = 0\) pointwise. Generally \(r \neq 0\). Weighted residual methods enforce

\[
\int_\Omega r \, w_i \, d\Omega = 0 \quad i = 1,\ldots,N
\]

for chosen **weight functions** \(w_i\).

## Collocation, least squares, Galerkin

| Method | Weights \(w_i\) | Character |
|--------|-----------------|-----------|
| Collocation | \(\delta(x - x_i)\) | Residual zero at points |
| Least squares | \(\partial(r w_i)/\partial \text{coef}\) | Minimize \(\|r\|_{L^2}\) |
| Galerkin | Same as trial \(\phi_i\) | Variational structure |
| Petrov–Galerkin | Different trial and test spaces | Stabilization, advection |

**Galerkin's method** chooses weights equal to trial functions. For self-adjoint elliptic problems, Galerkin coincides with Rayleigh–Ritz — the FEM path with the cleanest energy interpretation.

## Weak form as weighted residual

Integrating by parts before weighting moves derivatives onto test functions. The resulting **weak residual**

\[
R_{\text{weak}}(v) = a(u_h, v) - \ell(v)
\]

is zero for all \(v \in V_h\) iff \(u_h\) satisfies the Galerkin equations. This is why implementation begins with the weak form, not the strong residual.

## Boundary conditions

Essential BCs are built into the trial space: only functions satisfying \(u = g\) on \(\Gamma_D\) are admissible. Alternatively, **penalty methods** add \(\alpha \int_{\Gamma_D} (u_h - g)^2\) to the energy; **Nitsche's method** weakly enforces Dirichlet data without polluting conditioning at high penalty.

Natural BCs emerge from integration by parts — no special treatment required if the weak form is derived correctly.

## Bridge

Galerkin's method on a finite element space becomes a matrix system through assembly. The next chapter walks through global assembly — the algorithm every FEM code shares, from academic Matlab scripts to industrial solvers.
