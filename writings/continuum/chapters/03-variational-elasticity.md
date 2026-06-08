# Variational Elasticity and Nonlinear Extensions

Static equilibrium of an elastic body is equivalent to minimizing total potential energy — or finding a saddle point when constraints appear. This is where continuum theory and FEM meet on equal footing: the weak form Part III derived is the first variation of an energy; the assembly loop Part IV implemented is Rayleigh–Ritz on that energy.

The copper wire under tension minimizes (or rather, stationarizes) elastic energy stored in its stretched atomic lattice — a minimization FEM approximates on a mesh. When the load exceeds yield, minimization gives way to incremental variational inequalities; when deformation grows large, the energy depends on \(\mathbf{F}\), not \(\boldsymbol{\varepsilon}\). This chapter walks that path.

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

Defects are where the continuum picture admits its limitations — and where mesoscale models take over. Crack tips, dislocation lines, and grain boundaries are not nuisances to mesh around forever; they are the physical mechanisms behind yield, fracture, and work hardening in the copper wire. Part VII begins that descent: defect taxonomy, dislocation dynamics, and the models that replace singular continuum fields with structured mesoscale physics.
