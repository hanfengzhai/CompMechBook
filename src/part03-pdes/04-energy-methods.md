# Energy Methods and Minimum Principles

Many PDEs of mechanics are Euler–Lagrange equations of an energy functional. Minimizing energy — or finding stationary points — is both a theoretical tool and a practical algorithm (nonlinear FEM, phase-field models, variational time integrators).

## The Dirichlet principle

For Poisson's equation with homogeneous Dirichlet data, define

\[
\Pi(u) = \int_\Omega \tfrac{1}{2}|\nabla u|^2 - f u \, d\Omega.
\]

Stationary points satisfy \(\delta \Pi(u; v) = 0\) for all admissible variations \(v\), which recovers the weak form. **Coercivity** implies the stationary point is a **global minimizer**.

## Elastic strain energy

In linear elasticity,

\[
\Pi(\mathbf{u}) = \int_\Omega \tfrac{1}{2}\boldsymbol{\varepsilon}(\mathbf{u}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega - \int_\Omega \mathbf{f}\cdot\mathbf{u} \, d\Omega - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u} \, dS.
\]

Equilibrium displacements minimize (or stationarize) \(\Pi\). Hyperelastic materials use nonlinear strain energy \(\psi(\mathbf{F})\); Neo-Hookean, Mooney–Rivlin, and Ogden models differ in how they penalize stretch.

## Rayleigh–Ritz method

The **Rayleigh–Ritz** method minimizes \(\Pi\) over a finite-dimensional subspace \(V_h\):

\[
u_h = \arg\min_{v_h \in V_h} \Pi(v_h).
\]

For quadratic \(\Pi\), this is equivalent to Galerkin's method. For nonlinear energies, Rayleigh–Ritz gives a nonlinear algebraic system solved by Newton–Raphson — the backbone of nonlinear FEA.

## Saddle-point formulations

Not all problems are minimization. Stokes flow seeks a saddle point of

\[
\mathcal{L}(\mathbf{v}, p) = \int \tfrac{\mu}{2}|\nabla \mathbf{v}|^2 - \int p \nabla\cdot\mathbf{v} - \int \mathbf{f}\cdot\mathbf{v},
\]

leading to mixed finite elements (Taylor–Hood, stabilized equal-order). Inf–sup stability replaces coercivity — the Ladyzhenskaya–Babuška–Brezzi (LBB) condition.

## Time-dependent problems

For parabolic problems, energy **decreases**:

\[
\frac{d}{dt}\int \tfrac{1}{2}|u|^2 + \int |\nabla u|^2 = \int f u.
\]

Discrete energy stability — does the numerical scheme preserve this dissipation? — guides choice of time integrators (backward Euler is unconditionally stable for heat; explicit schemes require CFL).

## Bridge to Part IV

We have:

- Weak forms from integration by parts
- Sobolev spaces for admissible fields
- Energy principles for well-posedness and algorithms

Part IV asks: how do we choose \(V_h\), compute integrals, and assemble \(\mathbf{K}\)? The finite element method is the answer — and it is the workhorse of computational solid mechanics.
