# Weak Formulations and Test Functions

The weak form is the computational mechanic's version of integration by parts: move derivatives from the unknown solution onto smooth test functions, trading pointwise differentiability for integral balance.

[III.1](01-strong-form.md) wrote the copper wire's equilibrium and heating as **pointwise** PDEs — valid where \(C^2\) smoothness holds, failing at the grip corner, thermocouple weld, and mid-span load. This chapter is the corrective move the prologue's recurring character has been walking toward since Part I's nodal balance laws: multiply by a test function, integrate over the domain, integrate by parts once, and ask whether virtual work balances for all admissible perturbations. The answer lives in \(H^1\), not in classical \(C^2\).

Part II's operators and dual loads supplied the vocabulary for that move: the weak residual is not a pointwise check but a **pairing** against test functions in \(H^1_0\) — the same duality [II.4](../part02-functional-analysis/04-operators-duality.md) built before Part III wrote any PDE. When the grip corner breaks \(C^2\) smoothness, integration by parts is not a trick to appease a mesh; it is the honest statement that equilibrium holds in integral form against every admissible virtual displacement.

If the copper wire is fixed at both ends and loaded in the middle, the displacement field may be continuous but not twice differentiable at the load point — the strong form \(-EA u'' = f\) fails classically at a point force. The weak form still asks: for all admissible virtual displacements, is internal virtual work equal to external virtual work? That question has an answer in \(H^1\), and Galerkin discretization turns it into \(\mathbf{K}\mathbf{U}=\mathbf{F}\).

## Story so far (Parts I–III.1)

| Stage | What the wire became | Key object |
|-------|----------------------|------------|
| Part I | Spring network; \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | Discrete equilibrium |
| Part II | Fields in \(H^1\), \(L^2\); Lax–Milgram | Convergence target for refinement |
| [III.1](01-strong-form.md) | Pointwise PDEs for heat and elasticity | Strong form — valid where \(C^2\) holds |
| **III.2 (here)** | Virtual work at corners and welds | Weak form — honest at singularities |

The [prologue](../prologue/00-many-scales.md) introduced the weak form as a **recurring character**. Part I gave it a finite-dimensional prelude (nodal balance laws); Part II built \(H^1\) and dual loads; [III.1](01-strong-form.md) wrote the blackboard physics that breaks at the grip corner and thermocouple weld. This chapter is where the character speaks in full sentences — integration by parts, test functions, and the Galerkin system \(\mathbf{K}\mathbf{U}=\mathbf{F}\) that Part IV will assemble.

## Scene: the grip corner

Mount the copper wire in a rigid bracket with a reentrant corner — an L-shaped steel jaw gripping a cylindrical specimen. Under tension, the displacement field is visually smooth: the wire elongates, the bracket barely flexes. But zoom into the corner where copper meets steel: finite element post-processing shows stress components spiking, and a curious analyst asks whether \(-\nabla\cdot\boldsymbol{\sigma} = \mathbf{0}\) holds **pointwise** in classical sense.

It does not. The corner is a geometric singularity; gradients blow up as power laws of distance from the corner. Demanding a \(C^2\) displacement field is the wrong requirement — the physics still balances forces, but the balance is meaningful only in **integral** form. Multiply the equilibrium equation by a smooth test function, integrate over the domain, integrate stress divergence by parts, and the boundary terms carry the grip traction while the interior asks only that \(\boldsymbol{\sigma}\) be square-integrable in a suitable sense.

That maneuver — one integration by parts, one space of admissible test functions — is the weak form. It is the reason Part II built \(H^1\) before Part III wrote PDEs, and the reason Part IV's shape functions need only be continuous, not twice differentiable. The copper wire at the grip corner is where the story stops pretending that every field is smooth.

## From springs to weak form: the same question twice

Return to Part I's spring network on the copper wire. Equilibrium at each interior node required the sum of spring forces to vanish — a **discrete balance law**. Multiply that balance by an arbitrary virtual displacement at the node and sum over all nodes: internal virtual work equals external virtual work. That is already a weak statement; the only novelty in the continuum limit is that the index set of nodes becomes the domain \(\Omega\), and the sum becomes an integral.

The pipeline the book has been building now closes a loop:

```mermaid
flowchart LR
  LA[Part I: K u = f] --> FA[Part II: u in H1]
  FA --> SF[Strong PDE]
  SF --> WF[Weak form]
  WF --> FEM[Part IV: K U = F again]
```

**Linear algebra** gave us \(\mathbf{K}\mathbf{u}=\mathbf{f}\). **Functional analysis** explained why the limit as the mesh refines lives in \(H^1\). **Strong forms** wrote the PDE the mesh approximates. **Weak forms** are the variational statement FEM implements — and they return us to a matrix system whose entries are integrals of shape-function gradients. The copper wire never changed; only the language did.

Read the diagram above as the plot spine of the novel, not a syllabus chart: every arrow is the same specimen seen through a different lens. When Part IV assembles \(\mathbf{K}\) from shape functions, you are not learning a new method — you are closing the loop Part I opened with nodal equilibrium. When Part VI writes virtual work, you will recognize the same pairing of stress with a virtual strain. When Part IX minimizes \(E[\rho]\), the instinct is unchanged: pick an admissible trial object, integrate, and let boundary conditions carry what pointwise equations cannot.

This is why the weak form is not a numerical trick. It is the **correct continuum statement** for problems whose classical solutions fail at corners, kinks, and point loads — exactly the situations the drawn wire presents when clamped, notched, or loaded at a grip.

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

### Point load at midspan: where the strong form breaks

Suppose instead the wire carries a concentrated force \(P\) at \(x = L/2\). The strong form \(-EA u'' = P\,\delta(x - L/2)\) uses a **Dirac delta** on the right-hand side — not a function in \(L^2\), but a **linear functional** on test functions (Part II, Chapter 4). The weak form remains well posed: seek \(u \in H^1_0(0,L)\) such that

\[
\int_0^L EA\, u' v' \, dx = P\, v(L/2) \quad \forall v \in H^1_0(0,L).
\]

The load appears as evaluation of the test function at the load point — the discrete analogue of a nodal force in Part I's spring network. A finite element mesh with a node at midspan assembles \(F_i = P\) at that node directly; no delta function is ever stored in memory. This is the computational mechanic's everyday encounter with **distributions**: the weak form absorbs singular loads; the assembly code sees numbers at nodes.

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

| What the weak form established | What Sobolev spaces (next chapter) formalize |
|--------------------------------|---------------------------------------------|
| Integration by parts moves derivatives to test functions | \(H^1\): \(\nabla u \in L^2\) even when \(u\) is only piecewise smooth |
| Galerkin system \(\mathbf{K}\mathbf{U}=\mathbf{F}\) preview | \(H^1_0\) encodes Dirichlet BC; trace operators on boundaries |
| Point loads as functionals, not \(L^2\) densities | \(H^{-1}\) dual loads; concentrated forces on the wire |
| Corners break classical \(C^2\) smoothness | Regularity ladder: \(H^1\) membership vs. \(H^2\) for optimal FEM rates |

The [prologue](../prologue/00-many-scales.md) named this formulation a **recurring character** — born here as integration by parts, returning as Galerkin orthogonality in Part IV, virtual work in Part VI, and a variational statement on electron density in Part IX. Part II built the room (\(H^1\), dual loads, completeness); this chapter gave the character its first lines on stage. When the grip corner breaks classical \(C^2\) smoothness, the weak form still balances virtual work — that is the plot hinge the rest of the book assumes you will trust.

| Prologue act | Strong form that breaks at corners | Weak form statement this chapter writes |
|--------------|-------------------------------------|----------------------------------------|
| II — Warming | \(-\nabla\cdot(k\nabla T)=q_J\) pointwise | Find \(T\in H^1\) s.t. \(\int k\nabla T\cdot\nabla v = \int q_J v\) for all \(v\in H^1_0\) |
| III — Pulling | \(-\nabla\cdot(EA\nabla u)=f\) pointwise | Find \(u\in H^1_0\) s.t. \(\int EA u' v' = \int f v\) for all \(v\in H^1_0\) |
| IV — Hardening (preview) | Nonlinear stress–strain history | Virtual work with evolving \(\boldsymbol{\sigma}\); Newton at each increment |
| V — Notch (preview) | Concentrated traction at a scratch | Point load as \(\ell\in H^{-1}\), not an \(L^2\) density |

The weak form is the **honest continuum contract** every discretization in Parts IV–IX inherits — Galerkin assembly, virtual work in Part VI, and the Hohenberg–Kohn variational principle in Part IX are the same insistence that residuals vanish against admissible test functions, in different Hilbert rooms. [III.1](01-strong-form.md) named the blackboard physics; [III.3](03-sobolev-spaces.md) makes "admissible" precise; [III.4](04-energy-methods.md) recasts the balance as minimization before Part IV turns it into \(\mathbf{K}\mathbf{U}=\mathbf{F}\).

Turn the page when "test function" still feels informal — Sobolev spaces are the contract that makes FEM assembly honest.
