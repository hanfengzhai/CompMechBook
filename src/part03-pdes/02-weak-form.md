# Weak Formulations and Test Functions

The weak form is the computational mechanic's version of integration by parts: move derivatives from the unknown solution onto smooth test functions, trading pointwise differentiability for integral balance.

If the copper wire is fixed at both ends and loaded in the middle, the displacement field may be continuous but not twice differentiable at the load point — the strong form \(-EA u'' = f\) fails classically at a point force. The weak form still asks: for all admissible virtual displacements, is internal virtual work equal to external virtual work? That question has an answer in \(H^1\), and Galerkin discretization turns it into \(\mathbf{K}\mathbf{U}=\mathbf{F}\).

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

Only **first** derivatives of \(u\) appear — hence \(H^1\) suffices. The Laplacian never appears as a pointwise operator in the weak form; it is hidden inside the bilinear form \(a(\cdot,\cdot)\).

## The Lax–Milgram theorem in action

**Theorem (Lax–Milgram).** Let \(H\) be a Hilbert space. If \(a: H \times H \to \mathbb{R}\) is continuous and coercive,

\[
|a(u,v)| \le C \|u\|_H \|v\|_H, \qquad a(u,u) \ge \alpha \|u\|_H^2,
\]

and \(\ell \in H^*\) (continuous linear functional), then there exists a **unique** \(u \in H\) with \(a(u,v) = \ell(v)\) for all \(v \in H\). Moreover,

\[
\|u\|_H \le \frac{1}{\alpha}\|\ell\|_{H^*}.
\]

For Poisson with \(f \in L^2(\Omega)\) and \(V = H^1_0(\Omega)\):

| Hypothesis | Verification |
|------------|--------------|
| Continuity of \(a\) | Cauchy–Schwarz: \(\|\nabla u\|_{L^2}\) controls \(a(u,v)\) |
| Coercivity | Poincaré inequality on \(H^1_0\): \(\|u\|_{L^2} \le C_P \|\nabla u\|_{L^2}\) |
| Continuity of \(\ell\) | \(\|\ell\| \le \|f\|_{L^2}\|v\|_{L^2}\) |

Hence a **unique weak solution** exists. Moreover, it minimizes the energy functional

\[
\Pi(u) = \tfrac{1}{2}a(u,u) - \ell(u) = \int_\Omega \tfrac{1}{2}|\nabla u|^2 - f u \, d\Omega.
\]

Stability: small changes in \(f\) produce small changes in \(u\) in the \(H^1\) norm — essential for well-posed computation.

## Worked example: 1D bar with body force

On \((0,L)\), \(-(EA u')' = f(x)\), \(u(0)=u(L)=0\). Weak form with test \(v \in H^1_0(0,L)\):

\[
\int_0^L EA u' v' \, dx = \int_0^L f v \, dx.
\]

Take \(f = 1\), constant \(EA\). A piecewise-linear FEM with two elements gives the same \(3 \times 3\) system as Part I’s assembly; solving yields nodal displacements approximating the parabolic exact solution \(u(x) = x(L-x)/(2EA)\). The weak form, Galerkin discretization, and linear algebra pipeline close the loop from Part I to Part IV.

## Worked example: point load at midspan (why the weak form wins)

Return to the copper wire gripped at both ends and loaded by a **point force** \(P\) at midspan \(x = L/2\). Part I modeled this as a spring network; Part III now writes the continuum limit.

**Strong form.** Axial equilibrium is \(-(EA u')' = P\,\delta(x - L/2)\) on \((0,L)\), with \(u(0)=u(L)=0\). Away from the load, \(u'' = 0\), so \(u\) is piecewise linear — a **tent function** with peak at \(L/2\). At the load point, \(u\) is continuous but **not twice differentiable**: a classical \(C^2\) solution does not exist. The strong Laplacian \(\Delta u\) is not defined pointwise at the kink; insisting on a pointwise PDE is the wrong question.

**Weak form.** Multiply by \(v \in H^1_0(0,L)\) and integrate:

\[
\int_0^L EA\, u' v' \, dx = P\, v(L/2).
\]

Only **first** derivatives appear. The right-hand side is a **point evaluation** of the test function — the continuum version of applying a nodal load in Part I. Lax–Milgram applies with coercivity from Poincaré on \(H^1_0\); a unique weak solution exists. It is the tent function \(u(x) = \frac{P}{EA}\min(x, L-x)\) for \(x \in [0,L]\), with \(\|u\|_{H^1}\) finite even though \(u''\) is a delta distribution, not a function.

**Three-node Galerkin (preview of Part IV).** Split \([0,L]\) into two equal elements with nodes at \(0, L/2, L\). Piecewise-linear hat functions \(\phi_0, \phi_1, \phi_2\) give

\[
K_{ij} = \int_0^L EA\, \phi_i' \phi_j' \, dx, \qquad F_i = P\, \phi_i(L/2).
\]

Because \(\phi_0(L/2)=\phi_2(L/2)=0\) and \(\phi_1(L/2)=1\), the load vector is \(\mathbf{F} = (0,\, P,\, 0)^T\) — exactly the middle-node pattern from Part I’s spring assembly. Symmetry and sparsity match the stiffness matrix assembled there; only the **interpretation** has changed: \(\mathbf{K}\) is a Galerkin projection of the operator \(-(EA\,(\cdot)')'\), not an ad hoc graph Laplacian.

| Question | Strong form at \(x=L/2\) | Weak form / FEM |
|----------|--------------------------|-----------------|
| Does a \(C^2\) solution exist? | No (kink) | Not required |
| Where is equilibrium enforced? | Pointwise (fails at load) | Against all admissible \(v\) |
| Discrete unknowns | Ill-defined second derivatives | Nodal displacements in \(H^1\) |
| Link to Part I | — | Same \(\mathbf{K}\mathbf{U}=\mathbf{F}\) pattern |

This example is the narrative hinge between Parts I, III, and IV: linear algebra was always a weak-form discretization in disguise; we simply had not yet named the function space or the integration-by-parts step that makes the point load legitimate.

## Virtual work in elasticity

For displacements, the weak form is the **principle of virtual work**:

\[
\int_\Omega \boldsymbol{\sigma} : \delta\boldsymbol{\varepsilon} \, d\Omega = \int_\Omega \mathbf{f}\cdot\delta\mathbf{u} \, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\delta\mathbf{u} \, dS
\]

for all kinematically admissible virtual displacements \(\delta\mathbf{u}\) (vanishing on \(\Gamma_D\)). Linearization with \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) yields the bilinear form

\[
a(\mathbf{u}, \mathbf{v}) = \int_\Omega \boldsymbol{\varepsilon}(\mathbf{v}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{u}) \, d\Omega,
\]

used in FEM for the copper wire in 3D or for complex fixtures. Nonlinear elasticity replaces the bilinear form with an incremental tangent stiffness — Newton–Raphson in Part IV.

## Natural boundary conditions

Neumann data \(\partial u / \partial n = h\) enters the weak form as a boundary integral:

\[
\int_\Omega \nabla u \cdot \nabla v = \int_\Omega f v + \int_{\Gamma_N} h v.
\]

Dirichlet data are **essential** — enforced strongly on the trial space (or via constraints). Neumann data are **natural** — appear automatically in the weak form after integration by parts. Robin conditions add a boundary stiffness term \(\int_{\Gamma_R} \alpha u v \, dS\) to the left-hand side.

This distinction guides FEM boundary implementation: essential BCs modify the trial space; natural BCs modify the load functional.

### Mixed boundary example

Heat the wire at \(x=0\) (\(T = T_h\)) and impose convective flux at \(x=L\): \(-k T' = h(T - T_\infty)\). The weak form on \(H^1\) with \(T(0)=T_h\) includes the Robin term on the right end. Only \(T(0)\) is essential; the convection condition is natural.

## Weak form of the heat equation

Multiply \(u_t - \alpha \Delta u = f\) by test \(v \in H^1_0(\Omega)\) and integrate:

\[
\int_\Omega u_t v \, d\Omega + \alpha \int_\Omega \nabla u \cdot \nabla v \, d\Omega = \int_\Omega f v \, d\Omega.
\]

Semidiscretization: \(u_h = \sum_j U_j(t) \phi_j\) gives \(\mathbf{M}\dot{\mathbf{U}} + \alpha \mathbf{K}\mathbf{U} = \mathbf{F}\). The mass matrix \(\mathbf{M}\) comes from \(\int \phi_i \phi_j\); the stiffness from \(\int \nabla\phi_i \cdot \nabla\phi_j\). Time discretization (backward Euler, BDF, Runge–Kutta) is layered on top — Part IV for FEM, Part V for FVM flux differencing in fluids.

## Integration by parts in higher dimensions

Green's first identity:

\[
\int_\Omega \nabla u \cdot \nabla v = -\int_\Omega (\Delta u) v + \int_{\partial\Omega} \frac{\partial u}{\partial n} v.
\]

For vector problems, use **divergence theorem**:

\[
\int_\Omega \nabla\cdot\boldsymbol{\sigma} \cdot \mathbf{v} = -\int_\Omega \boldsymbol{\sigma} : \nabla \mathbf{v} + \int_{\partial\Omega} \boldsymbol{\sigma}\mathbf{n}\cdot\mathbf{v}.
\]

Symmetry of \(\boldsymbol{\sigma}\) and the choice of test space determine whether gradients of \(\mathbf{v}\) appear as symmetric gradients — the \(\boldsymbol{\varepsilon}(\mathbf{v})\) in elasticity.

## Galerkin discretization (preview)

Choose \(V_h = \text{span}\{\phi_1,\ldots,\phi_N\} \subset V\). Seek

\[
u_h = \sum_j U_j \phi_j
\]

such that

\[
a(u_h, \phi_i) = \ell(\phi_i) \quad i = 1,\ldots,N.
\]

This is a linear system \(\mathbf{K}\mathbf{U} = \mathbf{F}\) with \(K_{ij} = a(\phi_j, \phi_i)\), \(F_i = \ell(\phi_i)\). Part IV implements assembly of these entries element by element.

| Method | Trial space | Test space | Structure |
|--------|-------------|------------|-----------|
| Galerkin | \(V_h\) | \(V_h\) | Symmetric if \(a\) symmetric |
| Petrov–Galerkin | \(V_h\) | \(W_h \neq V_h\) | Stabilization (advection) |
| Collocation | — | \(\delta\) at points | No weak form; strong residual |
| FVM | cell averages | constants per cell | Integral balance (Part V) |

## Weighted residuals viewpoint

The weak residual \(R(u_h; v) = a(u_h,v) - \ell(v)\) must vanish for all \(v \in V_h\). Galerkin chooses test functions equal to trial basis functions — the orthogonal projection of the solution onto \(V_h\) in the energy inner product. Part IV’s first chapter makes this equivalence explicit for self-adjoint elliptic problems.

## Bridge

Weak derivatives make sense in **Sobolev spaces**. The next chapter defines \(H^1\) rigorously enough to code with confidence — and explains why conforming finite elements must be continuous across element boundaries (for standard Lagrange elements). Without \(H^1\), we cannot state what "\(\nabla u\)" means when \(u\) is only piecewise smooth; with \(H^1\), the weak form of the copper wire's conduction and elasticity problems is not a hack but the correct continuum statement.

Energy methods (Part III, Chapter 4) then recast \(a(u,v)=\ell(v)\) as minimization or saddle-point principles — the variational backbone of FEM and, in nonlinear settings, of hyperelastic and phase-field solvers.
