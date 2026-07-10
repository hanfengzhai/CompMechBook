# Variational Elasticity and Nonlinear Extensions

[VI.2](02-stress-balance.md) named the forces that kinematics alone could not supply — Cauchy stress, Piola–Kirchhoff stress, balance laws that constrain how stress varies in space and time. Parts III and IV already solved the discrete shadow of those laws as \(\mathbf{K}\mathbf{U}=\mathbf{F}\); this chapter explains **why** that linear system is the first variation of an energy functional, and when the energy picture survives load increments versus when history and defects force a different story.

Static equilibrium of an elastic body is equivalent to minimizing total potential energy — or finding a saddle point when constraints appear. This is where continuum theory and FEM meet on equal footing: the weak form Part III derived is the first variation of an energy; the assembly loop Part IV implemented is Rayleigh–Ritz on that energy.

The copper wire under tension minimizes (or rather, stationarizes) elastic energy stored in its stretched atomic lattice — a minimization FEM approximates on a mesh. When the load exceeds yield, minimization gives way to incremental variational inequalities; when deformation grows large, the energy depends on \(\mathbf{F}\), not \(\boldsymbol{\varepsilon}\). This chapter walks that path.

## Scene: energy stored in the stretch

Return to the tensile frame with the load cell climbing. Below yield, the wire lengthens elastically: each increment of grip displacement adds work, and most of that work is **stored** as elastic strain energy recoverable on unloading. Plot \(\Pi(\mathbf{u})\) — total potential energy as a functional of the displacement field — and the equilibrium path is the trajectory that keeps \(\Pi\) stationary under admissible variations.

Part IV assembled \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from element matrices; Part VI now explains **why** that linear system is the discrete first variation of an energy. Virtual work and minimum potential energy are two views of the same equilibrium; variational elasticity makes the connection explicit before Part VII asks what happens when the stored-energy landscape develops singularities at dislocation cores.

## Principle of minimum potential energy

Among **kinematically admissible** displacements \(\mathbf{u}\) — satisfying \(\mathbf{u} = \mathbf{u}_0\) on \(\Gamma_D\) — define the **total potential energy**

\[
\Pi(\mathbf{u}) = \int_{\Omega_0} \psi(\boldsymbol{\varepsilon}(\mathbf{u}))\, dV - \int_{\Omega_0} \mathbf{f}\cdot\mathbf{u}\, dV - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u}\, dS.
\]

For **linear elasticity**, strain energy density is

\[
\psi = \tfrac{1}{2}\boldsymbol{\varepsilon}:\mathbb{C}:\boldsymbol{\varepsilon},
\]

and \(\Pi\) is **quadratic** in \(\mathbf{u}\). Equilibrium displacement minimizes \(\Pi\):

\[
\mathbf{u}^* = \arg\min_{\mathbf{u} \in \mathcal{A}} \Pi(\mathbf{u}),
\]

where \(\mathcal{A}\) is the set of admissible fields.

**Uniqueness** follows from strict convexity of \(\psi\) (positive-definite \(\mathbb{C}\)) and coercivity on displacements modulo rigid modes — fixed by essential BCs.

## Weak form as first variation

Variation \(\mathbf{u} \to \mathbf{u} + \eta\,\delta\mathbf{u}\) with admissible \(\delta\mathbf{u}\) gives

\[
\delta\Pi = \int_{\Omega_0} \boldsymbol{\sigma} : \delta\boldsymbol{\varepsilon}\, dV - \int_{\Omega_0} \mathbf{f}\cdot\delta\mathbf{u}\, dV - \int_{\Gamma_N} \mathbf{t}\cdot\delta\mathbf{u}\, dS,
\]

with \(\boldsymbol{\sigma} = \partial\psi/\partial\boldsymbol{\varepsilon}\). Setting \(\delta\Pi = 0\) for all \(\delta\mathbf{u}\) yields the **principle of virtual work** — the weak form implemented in Part IV.

**Galerkin FEM** is **Rayleigh–Ritz**: minimize \(\Pi\) over \(V_h \subset \mathcal{A}\). For quadratic \(\Pi\), this equals solving \(\mathbf{K}\mathbf{U} = \mathbf{F}\). Part III's energy methods chapter promised this equivalence; Part IV delivered the algorithm.

## Example: 1D bar as energy minimization

Axial energy density \(\psi = \tfrac{1}{2} E \varepsilon_{xx}^2\). Total energy on \([0,L]\):

\[
\Pi(u) = \int_0^L \tfrac{1}{2} E (u')^2\, dx - \int_0^L f u\, dx - F u(L).
\]

Euler–Lagrange equation: \(-(Eu')' = f\), with natural BC \(Eu'(L) = F\). FEM minimization on piecewise linears reproduces the same system as Galerkin — the copper wire as a 1D energy well.

## Hyperelastic materials

Finite deformation uses strain energy \(\psi(\mathbf{F})\) or \(\psi(\mathbf{E})\). Examples:

- **Neo-Hookean**: \(\psi = \tfrac{\mu}{2}(I_1 - 3) - \mu\ln J + \tfrac{\lambda}{2}(\ln J)^2\), with invariants \(I_1 = \text{tr}(\mathbf{C})\), \(J = \det\mathbf{F}\).
- **Mooney–Rivlin**, **Ogden**: different stretch penalties for rubber and soft tissues.

Stress derives from \(\mathbf{P} = \partial\psi/\partial\mathbf{F}\). **Polyconvexity** of \(\psi\) ensures existence of minimizers in nonlinear elasticity theory — a continuum analog of coercivity.

Copper at large stretch requires crystal plasticity, not rubber models — but hyperelasticity illustrates the nonlinear variational framework that [Nonlinear FEA notes](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) document in detail.

## Nonlinear FEM path

For nonlinear \(\Pi\) or non-quadratic virtual work:

1. **Load stepping**: apply load increment \(\Delta\lambda\) on a reference load vector.
2. **Newton–Raphson**: at each step, solve \(\mathbf{K}_T\,\Delta\mathbf{U} = \mathbf{R}\), where \(\mathbf{R}\) is the **residual** of the weak form (out-of-balance force) and \(\mathbf{K}_T = \partial\mathbf{R}/\partial\mathbf{U}\) is the **consistent tangent stiffness**.
3. **Update**: \(\mathbf{U} \leftarrow \mathbf{U} + \Delta\mathbf{U}\) until \(\|\mathbf{R}\|\) is below tolerance.

**Consistent tangent** — not a numerical perturbation of \(\mathbf{K}\), but the exact derivative of the discretized residual — yields quadratic Newton convergence. Inconsistent tangents converge slowly or stall.

Geometric nonlinearity (\(\mathbf{F}\) far from \(\mathbf{I}\)) and material nonlinearity (plasticity, damage) compose in the same loop. Plasticity adds **internal variables** updated at quadrature points alongside stress.

## Incremental variational principles

Plasticity and viscoplasticity often use **incremental energy potentials** over a time step: minimize or stationarize a functional involving incremental displacement and updated internal variables. **Variational consistency** ensures that the discrete update inherits stability properties of the continuum formulation.

Rate-independent perfect plasticity is not a simple minimization — it is a **variational inequality**. Algorithms (return mapping, active-set methods) project trial stresses onto the yield surface.

## Mixed and constrained formulations

**Incompressibility** (\(J = 1\)) in finite elasticity or Stokes flow leads to saddle-point problems:

\[
\min_{\mathbf{u}} \max_p \Pi(\mathbf{u}, p) \quad \text{subject to } \nabla\cdot\mathbf{u} = 0.
\]

Mixed \(u\)–\(p\) elements (Part III LBB, Part IV locking chapter) discretize the saddle point. **Augmented Lagrangian** and **penalty** methods approximate constraints with penalties — trading exact satisfaction for simpler systems.

## Contact and friction

When the copper wire grips contact a rigid jaw, **non-penetration** constraints apply:

\[
g(\mathbf{u}) = (\mathbf{x}_{\text{contact}} - \mathbf{x}_{\text{body}})\cdot\mathbf{n} \ge 0.
\]

Contact is a **variational inequality**: equilibrium among admissible configurations that satisfy inequalities. Implementation options:

- **Penalty**: add stiffness when penetration detected — simple, conditioning issues.
- **Augmented Lagrangian**: iterate multipliers on contact forces.
- **Mortar methods**: weakly enforce continuity on non-matching interfaces — high accuracy for multibody contact.

Friction adds Coulomb constraints: \(|\mathbf{t}_T| \le \mu t_N\). Non-smooth optimization and active-set strategies select sticking vs. sliding.

## Stability and buckling

Compression of a slender copper wire may **buckle** — equilibrium becomes a saddle point, not a minimum. **Linear buckling analysis** solves the eigenvalue problem \((\mathbf{K} + \lambda \mathbf{K}_g)\mathbf{v} = 0\) for critical load factor \(\lambda\) and mode shape \(\mathbf{v}\), where \(\mathbf{K}_g\) is the geometric stiffness from initial stress.

Post-buckling requires arc-length continuation — tracing equilibrium paths through limit points where tangent stiffness is singular.

## When continuum theory breaks down

Variational elasticity assumes smooth enough fields. **Crack tips** in linear elasticity have \(|\nabla u| \sim r^{-1/2}\): strain is not square-integrable in the classical \(H^1\) sense on a domain containing the tip. **Dislocation cores** have singular lattice distortion over atomic scales.

Remedies:

- **Regularized models**: phase-field fracture smears cracks over a diffuse interface with length scale \(\ell_0\).
- **Enriched bases**: XFEM adds discontinuous or near-tip functions to \(V_h\).
- **Descent to defect models**: Part VII dislocation dynamics; Part VIII molecular dynamics at the core.

The continuum variational framework remains valid **outside** singular sets; enrichment or homogenization patches the failure.

## Worked example: the copper wire as Rayleigh–Ritz

Return to the tensile frame one last time in the elastic range. A cold-drawn copper wire of length \(L = 100\,\text{mm}\), cross-section \(A = 0.785\,\text{mm}^2\) (1 mm diameter), and Young's modulus \(E = 117\,\text{GPa}\) is fixed at \(x = 0\) and stretched to \(u(L) = \delta = 0.10\,\text{mm}\). In 1D linear elasticity the strain energy density is \(\psi = \tfrac{1}{2}E (u')^2\), and the admissible field that minimizes \(\Pi\) under the essential boundary conditions is the linear profile

\[
u(x) = \frac{\delta x}{L}, \qquad \varepsilon_{xx} = \frac{\delta}{L} = 10^{-3}.
\]

The stored elastic energy is

\[
\Pi_{\text{exact}} = \int_0^L \tfrac{1}{2} E \left(\frac{\delta}{L}\right)^2 A\, dx = \tfrac{1}{2}\frac{EA\delta^2}{L} \approx 4.6\,\text{mJ},
\]

and the reaction force at the grip is \(F = EA\delta/L \approx 92\,\text{N}\) — the slope of the early linear region on the load–displacement curve from the prologue.

Now discretize with **three equal bar elements** — the same assembly pattern Part I introduced and Part IV automated. Nodes at \(x_0 = 0, x_1 = L/3, x_2 = 2L/3, x_3 = L\); unknown displacements \(U_2, U_3\) with \(U_0 = 0\) and \(U_3 = \delta\) prescribed. Each element of length \(h = L/3\) contributes

\[
\mathbf{k}_e = \frac{EA}{h}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Assembly gives the \(2 \times 2\) system for the free DOFs,

\[
\frac{EA}{h}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
\begin{bmatrix} U_2 \\ U_3 \end{bmatrix}
=
\begin{bmatrix} 0 \\ F_3 \end{bmatrix},
\]

with \(U_3 = \delta\) enforced. Solving yields \(U_2 = \tfrac{2}{3}\delta\) and \(U_3 = \delta\) — **exact at every node**, because the true solution is linear and three linear elements reproduce any affine field on a uniform mesh.

The discrete energy at the minimizing \(\mathbf{U}\) equals the continuum \(\Pi_{\text{exact}}\). That is not luck: Rayleigh–Ritz on a potential whose minimizer lies in \(V_h\) returns the **exact** energy in one solve. Refine to a nonlinear displacement profile (a wire with a notch, or thermal strain \(\alpha\Delta T\) varying along \(x\)) and the same assembly returns an approximate \(\Pi_h \ge \Pi_{\text{exact}}\) — the discrete solution sits at the bottom of a finite-dimensional energy bowl inside the infinite-dimensional one Part II defined.

This example closes the loop the book has been tracing since Part I:

| Step | Part | What happened on the wire |
|------|------|---------------------------|
| Spring network | I | \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from bar elements |
| Limit \(h \to 0\) | I–II | \(u(x)\) replaces \(\mathbf{U}\); energy norm replaces \(\|\mathbf{U}\|\) |
| Weak form | III | Minimizing \(\Pi\) \(\Leftrightarrow\) virtual work |
| Assembly | IV | Shape functions and quadrature build \(\mathbf{K}\) from \(\psi\) |
| Continuum naming | VI (here) | \(\psi(\boldsymbol{\varepsilon})\) is why the matrix existed |

When the load cell curve bends upward — work hardening, necking, rate effects — the energy is no longer a simple quadratic in \(\mathbf{u}\). The next chapter follows that history-dependent path to yield and explains why Part VII must introduce dislocations to supply the hardening law.

## Multiscale variational coupling

Modern workflows **embed** atomistic or DFT domains inside continuum FEM via **bridging methods**:

- **Quasi-continuum**: FEM with energies from atomistic potentials on refined patches.
- **Concurrent coupling**: handshake between MD and FEM regions with blended forces.

Variational structure (conservative forces from potentials) aids stable coupling — ad hoc force blending without power consistency leaks energy.

## Connection to the full book arc

| Part | Role in variational elasticity |
|------|-------------------------------|
| I | \(\mathbf{K}\mathbf{U} = \mathbf{F}\) as discrete minimization |
| II | \(H^1\) admissible fields, coercivity, best approximation |
| III | Weak form, Lax–Milgram, Rayleigh–Ritz, mixed LBB |
| IV | Assembly, elements, convergence |
| V | Fluid counterpart: saddle points for pressure, not energy minimization |
| VI (this chapter) | Energy and virtual work as unified principle |
| VII+ | When \(\psi\) and \(\mathbb{C}\) must be derived from defects and atoms |

The prologue's copper wire: DFT gives cohesion; MD gives thermal motion; DDD gives work hardening; FEM (Part IV) gives bending and tension; CFD (Part V) gives cooling; Part VI explains why those simulations are minimizing energy or balancing virtual work — until they are not, and we descend further.

## Bridge

Variational elasticity closes the loop the book has traced since Part I's spring network: minimize energy in \(H^1\), derive virtual work, assemble \(\mathbf{K}\) — and recognize the discrete solve as Rayleigh–Ritz on the same functional Part III named.

| What VI.3 established | What VI.4 opens |
|-------------------------|-----------------|
| Hyperelastic energy \(\psi(\boldsymbol{\varepsilon})\); path-independent response | Geometric nonlinearity when strains are large |
| Virtual work \(\delta\Pi = 0\) as FEM's philosophical source | J₂ plasticity when history matters (cold-drawn wire) |
| Worked 1D bar: exact linear solution on P1 mesh | Newton–Raphson at every load increment |
| Elastic springback before yield | Honest admission: smooth fields break at defects |

Return to the [prologue](../../prologue/00-many-scales.md): **Act III** measured the linear elastic climb on the load cell; **Act IV** is the upward bend that variational elasticity cannot explain with a quadratic \(\psi\) alone. Part IV assembled \(\mathbf{K}\) from bilinear forms; this chapter named the stress and strain those forms integrate. [VI.4](04-nonlinear-plasticity-preview.md) is the last continuum stop — phenomenological hardening without dislocations, a fitted curve waiting for Part VII's forest to supply \(\sigma_{y0}\) and \(H\).

| Prologue act | Variational statement on the wire | Where the energy picture breaks |
|--------------|-----------------------------------|--------------------------------|
| III — Pulling | Minimize \(\Pi[\mathbf{u}]=\int\psi(\boldsymbol{\varepsilon})\,\mathrm{d}V\); \(\delta\Pi=0\) | Still valid in the linear elastic regime |
| II — Warming | Coupled thermal–mechanical energy (preview) | Temperature enters moduli and thermal strain |
| IV — Hardening | Path-dependent dissipation; no single \(\psi\) | History and defects require internal variables |
| V — Notch | Concentrated energy at a scratch | Finite-strain and damage force descent to Part VII |

Turn the page when the wire's stress–strain curve bends upward after cold drawing but your elastic energy minimization still returns a straight line — that is the signal history and mesoscale defects have entered the story.

| Energy picture (this chapter) | Where it stops being enough | Part that continues the plot |
|------------------------------|----------------------------|------------------------------|
| Quadratic \(\psi(\boldsymbol{\varepsilon})\) | Yield and path dependence | [VI.4](04-nonlinear-plasticity-preview.md) |
| Path-independent hyperelasticity | Dislocation forest from cold work | [Part VII](../part07-defects/00-opening.md) |
| Virtual work \(\delta\Pi=0\) | Atomistic nucleation at a notch | [Part VIII](../part08-md/00-opening.md) |
