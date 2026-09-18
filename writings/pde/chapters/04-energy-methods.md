# Energy Methods and Minimum Principles

Many PDEs of mechanics are Euler–Lagrange equations of an energy functional. Minimizing energy — or finding stationary points — is both a theoretical tool and a practical algorithm (nonlinear FEM, phase-field models, variational time integrators).

Pull the copper wire in tension: in linear elasticity, equilibrium minimizes stored elastic energy minus work done by the load. Heat the wire: steady conduction minimizes a thermal dissipation functional subject to boundary data. Even when the physics is not literally "energy" (electrostatics, Darcy flow), a convex functional often lurks behind the PDE — and convexity is what makes minimizers unique and computable.

## Scene: the wire finds its rest

Load the copper wire in the tensile frame and hold the grip displacement fixed. Microscopically, atoms rearrange for milliseconds; macroscopically, the wire **settles** to an equilibrium shape that minimizes total potential energy — elastic stored energy minus work done by the grips. Plot energy versus a trial displacement field: the true equilibrium sits at the bottom of a bowl; perturb it slightly and the energy rises, a sign of stability.

The same variational picture governs steady heating: among all temperature fields satisfying boundary data, the physical one minimizes a thermal functional whose Euler–Lagrange equation is Fourier's law. Part III ends here because Part IV will **discretize this minimization** — replace the infinite-dimensional search over admissible fields with a finite-dimensional search over nodal values, and call the result finite element assembly. Energy methods are the bridge from weak PDEs to algorithms.

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

### Worked example: thermoelastic energy on the wire

Return to prologue **Act II — Heating**: steady current raises the copper wire's temperature above room value, and thermal expansion adds strain even before the grips ramp load. The coupled stationary problem minimizes a **sum of energies** — mechanical plus thermal — subject to the heat equation as a constraint (or solved in staggered fashion).

For a 1D bar of length \(L\), cross-section \(A\), fixed at \(x=0\), free at \(x=L\) with tensile traction \(F\), and Joule heating \(q(x)\):

\[
\Pi(u, T) = \int_0^L \left[\tfrac{EA}{2}\left(u' - \alpha(T - T_{\text{ref}})\right)^2 + \tfrac{kA}{2}(T')^2\right] dx - F\, u(L).
\]

Stationarity in \(u\) at fixed \(T\) gives the mechanical equilibrium with thermal eigenstrain \(\varepsilon_{\text{th}} = \alpha(T - T_{\text{ref}})\). Stationarity in \(T\) gives steady conduction \(-(kT')' = q(x)/A\) with natural boundary conditions at the ends. The two fields **talk through \(\alpha\)**:

1. Heat raises \(T\); thermal strain lowers effective mechanical strain and stress at fixed grip displacement.
2. Mechanical work done at \(x=L\) does not appear in the heat equation at steady state — but transient heating (Act II in lab time) couples through \(\rho c_p \partial T/\partial t\).

Numbers for copper at modest \(\Delta T = 50\,\text{K}\): \(\alpha \approx 17 \times 10^{-6}\,\text{K}^{-1}\), so \(\varepsilon_{\text{th}} \approx 8.5 \times 10^{-4}\). With \(E = 120\,\text{GPa}\), the thermal stress if expansion were fully constrained would be \(\sigma_{\text{th}} \approx E \varepsilon_{\text{th}} \approx 100\,\text{MPa}\) — comparable to yield in annealed copper and a reminder that **Act II and Act III are not independent** on the same specimen. Part IV's thermoelastic assembly (Chapter 4) and Part V's conjugate heat transfer implement this split functional on the same mesh; Part VI names the tensors inside the integrand.

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

## Concept map checkpoint (Part III)

Part III opened with fields on domains and closes with the **energy** those fields minimize or stationarize. The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) habit — object, structure, theorem, failure mode — summarizes the whole part in one table:

| Question | Part III answer (copper wire) |
|----------|-------------------------------|
| What **object**? | Fields \(u\), \(\mathbf{u}\), \(T\) on the wire domain; loads as functionals |
| What **structure**? | Weak forms in \(H^1\); bilinear forms; convex or saddle functionals |
| What **theorem**? | Lax–Milgram (existence); Dirichlet principle (minimizers); LBB (mixed problems) |
| What **breaks**? | Reentrant corners (no classical \(C^2\) solution); equal-order \(P1\)–\(P1\) Stokes (no inf–sup) |

The pipeline is now complete from physics to algorithm:

```
Strong PDE  →  Weak form  →  Energy / saddle functional  →  (Part IV) discrete search on V_h
```

The copper wire's tensile equilibrium, steady heating, and low-Re cooling flow each occupy a row in the summary table above. Part IV does not change the physics — it chooses \(V_h\), computes integrals, and assembles the \(\mathbf{K}\) that Rayleigh–Ritz minimization demands.

## Lab act: minimize thermal energy on two bar elements (Act II — Warming)

**Act II** holds grip displacement fixed while current heats the wire. Part III closes with the variational statement that steady temperature **minimizes** a quadratic functional — the thermal analogue of elastic energy minimization in Act III.

Model steady conduction on \((0,L)\), \(L = 1\,\text{m}\), with conductivity \(k = 400\,\text{W/m·K}\), uniform Joule source \(q = 10^6\,\text{W/m}^3}\), and \(T(0) = T(L) = 300\,\text{K}\). The Dirichlet functional is

\[
\Pi(T) = \int_0^L \left[\tfrac{k}{2}(T')^2 - q T\right] dx.
\]

Discretize with **two equal bar elements** (three nodes). Use linear hat functions; unknowns are \(T_1 = 300\) (fixed), \(T_2\) at mid-span, \(T_3 = 300\) (fixed).

| Step | Rayleigh–Ritz move | Result |
|------|-------------------|--------|
| 1 | Express \(T_h = N_1 T_1 + N_2 T_2 + N_3 T_3\) with \(T_1 = T_3 = 300\) | One free DOF: \(T_2\) |
| 2 | Substitute into \(\Pi(T_h)\); set \(\partial \Pi / \partial T_2 = 0\) | Scalar equation \(K_{22} T_2 = F_2\) |
| 3 | Compare to weak form \(\int k T' v' = \int q v\) with test hat at node 2 | **Same** \(K_{22}\) and \(F_2\) — Galerkin = energy minimization |
| 4 | Solve for \(T_2\); compare to analytical \(T(L/2) = 300 + qL^2/(8k)\) | Coarse mesh underestimates peak; refine \(h\) |

The mid-span temperature you read on the thermocouple is the **minimizer** of \(\Pi\) in \(V_h\). When Part IV assembles \(\mathbf{K}\mathbf{T} = \mathbf{F}\) for the coupled thermoelastic wire, the mechanical block minimizes elastic energy and the thermal block minimizes this functional — two bowls, one afternoon. If you add thermal expansion \(\varepsilon_{\text{th}} = \alpha(T - T_{\text{ref}})\) before Act III ramps load, the two functionals **couple**: heat lowers effective stress at fixed grip displacement, previewing the thermoelastic energy in the worked example above.

## Bridge to Part IV

We have:

- Weak forms from integration by parts
- Sobolev spaces for admissible fields
- Energy principles for well-posedness and algorithms

Part IV asks: how do we choose \(V_h\), compute integrals, and assemble \(\mathbf{K}\)? The finite element method is the answer — weighted residuals, element-by-element assembly, quadrature rules, and convergence theory that make the copper wire’s discrete model faithful to the continuum energy we minimized here.

| What Part III completed | What Part IV opens |
|-------------------------|-------------------|
| Weak form \(a(u,v)=\ell(v)\) | Galerkin: choose \(u_h, v_h \in V_h\) from the same basis |
| Dirichlet principle: minimize \(\Pi[u]\) in \(H^1\) | Rayleigh–Ritz: minimize \(\Pi[u_h]\) on \(V_h\) → assembled \(\mathbf{K}\) |
| Lax–Milgram well-posedness | Céa lemma: discrete solution tracks continuous minimizer |
| Sobolev \(H^1\) regularity | \(H^1\)-conforming shape functions (continuous across elements) |
| [III.4 checkpoint](#concept-map-checkpoint-part-iii) energy pipeline | [IV opening](../part04-fem/00-opening.md#closing-the-arc-from-part-iii) **Closing the arc from Part III** |

If you need the fluid fork after FEM, [IV.5](../part04-fem/05-convergence.md#bridge-two-doors-from-here) names **Door A** (Part V: FVM and conjugate heat transfer) and **Door B** (Part VI: continuum stress–strain vocabulary) — the canonical place to choose, so this chapter can stay focused on energy → assembly.

Turn the page. Assembly awaits: the same \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from Part I, now built from shape functions, Jacobians, and the bilinear forms defined in Part III.
