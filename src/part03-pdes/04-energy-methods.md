# Energy Methods and Minimum Principles

Many PDEs of mechanics are Euler–Lagrange equations of an energy functional. Minimizing energy — or finding stationary points — is both a theoretical tool and a practical algorithm (nonlinear FEM, phase-field models, variational time integrators).

Pull the copper wire in tension: in linear elasticity, equilibrium minimizes stored elastic energy minus work done by the load. Heat the wire: steady conduction minimizes a thermal dissipation functional subject to boundary data. Even when the physics is not literally "energy" (electrostatics, Darcy flow), a convex functional often lurks behind the PDE — and convexity is what makes minimizers unique and computable.

## The Dirichlet principle

For Poisson's equation with homogeneous Dirichlet data, define

\[
\Pi(u) = \int_\Omega \tfrac{1}{2}|\nabla u|^2 - f u \, d\Omega.
\]

The **Gâteaux derivative** at \(u\) in direction \(v\) is

\[
\delta \Pi(u; v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega - \int_\Omega f v \, d\Omega = a(u,v) - \ell(v).
\]

Stationary points satisfy \(\delta \Pi(u; v) = 0\) for all admissible variations \(v\), which recovers the weak form. When \(a\) is coercive on \(H^1_0\), \(\Pi\) is strictly convex; the stationary point is a **global minimizer**:

\[
\Pi(u) = \min_{v \in H^1_0(\Omega)} \Pi(v).
\]

This is the **Dirichlet principle** — existence of a minimizer proves existence of a weak solution without constructing one explicitly.

### Worked example: 1D quadratic energy

On \((0,L)\) with \(u(0)=u(L)=0\) and \(f=1\), \(\Pi(u) = \int \tfrac{1}{2}(u')^2 - u \, dx\). The Euler–Lagrange equation is \(-u'' = 1\), giving \(u(x) = x(L-x)/2\). Direct integration yields

\[
\int_0^L \tfrac{1}{2}(u')^2 \, dx = \frac{L^3}{24}, \qquad \int_0^L u \, dx = \frac{L^3}{12}, \qquad \Pi(u) = -\frac{L^3}{24}.
\]

At the minimizer, \(a(u,u) = \ell(u)\), so \(\Pi(u) = \tfrac{1}{2}a(u,u) - \ell(u) = -\tfrac{1}{2}\ell(u)\) — the negative sign reflects work done by the load against the restoring stiffness. Rayleigh–Ritz on a two-element mesh (Part I assembly) approximates this minimum in \(V_h\); the minimizing \(\mathbf{U}\) solves \(\mathbf{K}\mathbf{U}=\mathbf{F}\).

## Elastic strain energy

In linear elasticity,

\[
\Pi(\mathbf{u}) = \int_\Omega \tfrac{1}{2}\boldsymbol{\varepsilon}(\mathbf{u}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega - \int_\Omega \mathbf{f}\cdot\mathbf{u} \, d\Omega - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u} \, dS.
\]

Equilibrium displacements minimize (or stationarize) \(\Pi\). For isotropic copper,

\[
\boldsymbol{\varepsilon}:\mathbb{C}:\boldsymbol{\varepsilon} = \lambda (\mathrm{tr}\,\boldsymbol{\varepsilon})^2 + 2\mu \boldsymbol{\varepsilon}:\boldsymbol{\varepsilon},
\]

with \(\lambda, \mu\) from \(E\) and \(\nu\). Uniaxial tension of the wire in the linear range recovers \(\Pi = \tfrac{1}{2}EA (u'/L_{\text{ref}})^2\) integrated over volume — the continuum version of \(\tfrac{1}{2}\mathbf{u}^T\mathbf{K}\mathbf{u}\).

Hyperelastic materials use nonlinear strain energy \(\psi(\mathbf{F})\); Neo-Hookean, Mooney–Rivlin, and Ogden models differ in how they penalize stretch. Nonlinear FEM minimizes \(\Pi\) by Newton–Raphson on the discrete energy — no separate "force vector" at the continuum level beyond \(\delta \Pi\).

| Model | Strain energy density | Use |
|-------|----------------------|-----|
| Linear elastic | \(\tfrac{1}{2}\boldsymbol{\varepsilon}:\mathbb{C}:\boldsymbol{\varepsilon}\) | Small strain copper wire |
| Neo-Hookean | \(\tfrac{\mu}{2}(I_1 - 3) - \mu\ln J + \tfrac{\lambda}{2}(J-1)^2\) | Moderate rubber-like stretch |
| Phase-field fracture | \(\psi(\boldsymbol{\varepsilon}) + G_c \gamma(\phi)\) | Crack on wire surface |

## Rayleigh–Ritz method

The **Rayleigh–Ritz** method minimizes \(\Pi\) over a finite-dimensional subspace \(V_h\):

\[
u_h = \arg\min_{v_h \in V_h} \Pi(v_h).
\]

For quadratic \(\Pi\), \(\partial \Pi/\partial U_i = 0\) yields \(\mathbf{K}\mathbf{U}=\mathbf{F}\) — equivalent to Galerkin's method when \(a\) is symmetric. For nonlinear energies, Rayleigh–Ritz gives a nonlinear algebraic system solved by Newton–Raphson — the backbone of nonlinear FEA.

**Céa's lemma** (Part IV): Galerkin FEM is quasi-optimal in the energy norm,

\[
\|u - u_h\|_{\text{energy}} \le C \inf_{v_h \in V_h} \|u - v_h\|_{\text{energy}}.
\]

Energy minimization on \(V_h\) picks the best approximation the mesh can represent, up to a constant.

## Lax–Milgram as energy minimization

For symmetric coercive \(a\), solving \(a(u,v)=\ell(v)\) is equivalent to minimizing

\[
J(u) = \tfrac{1}{2}a(u,u) - \ell(u).
\]

Coercivity gives \(J(u) \to +\infty\) as \(\|u\| \to \infty\) — **coercivity implies inf-sup for pure minimization**. Nonsymmetric problems (advection–diffusion with weak skew part) may still have weak solutions via Lax–Milgram without a minimization principle; stabilized Petrov–Galerkin methods (Part IV–V) restore usable variational structure.

## Saddle-point formulations

Not all problems are minimization. Stokes flow seeks a saddle point of

\[
\mathcal{L}(\mathbf{v}, p) = \int \tfrac{\mu}{2}|\nabla \mathbf{v}|^2 - \int p \nabla\cdot\mathbf{v} - \int \mathbf{f}\cdot\mathbf{v},
\]

leading to mixed finite elements (Taylor–Hood \(P2/P1\), stabilized equal-order). **Inf–sup stability** (Ladyzhenskaya–Babuška–Brezzi, LBB) replaces coercivity:

\[
\inf_{q \in Q_h} \sup_{\mathbf{v} \in V_h} \frac{b(\mathbf{v},q)}{\|\mathbf{v}\|_{V_h}\|q\|_{Q_h}} \ge \beta > 0.
\]

Coolant flowing around the copper wire in the low-Reynolds limit may be Stokes-like near the surface; pressure is not determined by minimization alone — it is a Lagrange multiplier enforcing \(\nabla\cdot\mathbf{v}=0\).

| Formulation | Structure | Stability condition |
|-------------|-----------|---------------------|
| Elliptic Poisson | Minimization | Coercivity (Poincaré) |
| Linear elasticity | Minimization | Korn + coercivity |
| Stokes | Saddle point | LBB inf–sup |
| Incompressible elasticity | Mixed / penalty | LBB or \(\chi\) penalty limit |

## Complementary energy and dual methods

In linear elasticity, a **complementary energy** functional in stress \(\boldsymbol{\tau}\) yields a maximization principle among statically admissible stress fields. Hybrid and mixed methods (stress–displacement formulations) exploit this duality. Part VI’s variational elasticity chapter connects these principles to implementation choices in industrial codes.

## Time-dependent problems

For parabolic problems, define energy

\[
E(t) = \tfrac{1}{2}\|u(t)\|_{L^2}^2.
\]

Differentiating and using the weak heat equation with homogeneous boundary data,

\[
\frac{dE}{dt} = -\int_\Omega |\nabla u|^2 + \int_\Omega f u \le \int_\Omega f u.
\]

Without forcing, \(E(t)\) decreases — **dissipation**. Discrete energy stability asks whether the numerical scheme preserves this dissipation (or a discrete analogue). Backward Euler is unconditionally stable for heat; explicit schemes require CFL bounds from eigenvalues (Part I, Chapter 3).

For second-order hyperbolic problems (wave equation on a vibrating wire), a different energy — kinetic plus potential — is conserved. Symplectic integrators in molecular dynamics (Part VIII) preserve a similar structure; variational integrators discretize the action integral rather than the PDE directly.

## Variational inequalities and contact

Press the copper wire against a rigid plane: equilibrium minimizes elastic energy subject to \(u \ge 0\) (unilateral constraint). The result is a **variational inequality** rather than a linear equation. Contact algorithms (penalty, augmented Lagrangian, mortar) are energy-based solvers at the discrete level — nonlinear extensions of Rayleigh–Ritz.

## Connection to FVM and conservation

Finite volume schemes often derive from **integral conservation** rather than pointwise energy minimization, but for self-adjoint elliptic operators the FVM system is sometimes equivalent to a Galerkin method on a dual mesh — hence still tied to an energy. For hyperbolic conservation laws (Part V), entropy conditions replace convex energy minimization; the "energy" is an entropy functional that decreases along admissible shocks.

## Summary table: variational landscape

| Problem | Functional | Stationarity | Discrete method |
|---------|------------|--------------|-----------------|
| Poisson | Dirichlet \(\Pi\) | Minimum | FEM Galerkin |
| Elasticity | Strain energy | Minimum | FEM |
| Heat (steady) | Thermal action | Minimum | FEM / FVM |
| Heat (transient) | Dissipation + \(L^2\) norm | Decrease in time | Time march + FEM |
| Stokes | Saddle Lagrangian | Saddle point | Mixed FEM |
| Navier–Stokes | Not global convex | Stationary point | FVM / stabilized FEM |

## Bridge to Part IV

We have:

- Weak forms from integration by parts
- Sobolev spaces for admissible fields
- Energy principles for well-posedness and algorithms

Part IV asks: how do we choose \(V_h\), compute integrals, and assemble \(\mathbf{K}\)? The finite element method is the answer — weighted residuals, element-by-element assembly, quadrature rules, and convergence theory that make the copper wire’s discrete model faithful to the continuum energy we minimized here.

Part V offers the alternative discretization philosophy for fluids and hyperbolic problems: balance fluxes on control volumes, Riemann solvers, and CFL-limited time stepping — still grounded in the PDEs and weak ideas from this part, but oriented toward conservation rather than trial functions in \(H^1\).

Turn the page. Assembly awaits: the same \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from Part I, now built from shape functions, Jacobians, and the bilinear forms defined in Part III.
