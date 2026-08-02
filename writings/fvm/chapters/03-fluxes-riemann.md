# Fluxes, Riemann Problems, and Shock Capturing

At a discontinuity, pointwise PDEs fail but integral conservation holds. The finite volume method does not resolve the shock as a grid-scale jump in derivatives; it resolves it as a consistent flux between cells. **Riemann solvers** are the local engines that translate left and right cell states into that flux.

The Sod shock tube — a diaphragm separating high- and low-pressure gas, ruptured at \(t = 0\) — is the canonical verification problem in the author's [FVM notes](https://hanfengzhai.github.io/note/FVM.pdf). It is to CFD what the patch test is to FEM: if your code fails Sod, nothing else matters.

## Scene: a rupture in the cooling duct

Imagine a shock tube test bench beside the wire experiment: a diaphragm bursts, pressure jumps, a contact discontinuity races down the tube. Pointwise derivatives fail at the jump, but the integral form still balances mass and momentum. Riemann solvers are how a cell face asks, "Given gas on my left and right, what flux crosses me?" The copper wire's cooling air can stay subsonic, but the same machinery governs supersonic jets and, in other contexts, shock heating that changes annealing behavior.

## The Riemann problem

Given left and right constant states \(U_L, U_R\) separated by a face at \(x = 0\), the **Riemann problem** solves

\[
U_t + F(U)_x = 0, \quad U(x,0) = \begin{cases} U_L & x < 0 \\ U_R & x > 0 \end{cases}
\]

with self-similar solution \(U(x,t) = U(x/t)\). Waves propagate at speeds determined by the eigenstructure of the flux Jacobian \(\mathbf{A} = \partial \mathbf{F}/\partial \mathbf{U}\).

For the 1D Euler equations, the solution typically consists of:

- A **shock wave** (discontinuous jump, supersonic relative to upstream),
- A **rarefaction fan** (continuous expansion wave),
- A **contact discontinuity** (velocity and pressure continuous, density jumps).

The exact wave pattern depends on \(U_L, U_R\). Analytic formulas exist for ideal gas — Toro's textbook is the standard reference.

### Eigenstructure of the Euler flux

Writing the 1D Euler system in quasilinear form \(U_t + \mathbf{J}\, U_x = 0\), the flux Jacobian \(\mathbf{J} = \partial \mathbf{F}/\partial \mathbf{U}\) has real eigenvalues

\[
\lambda_1 = u - c, \qquad \lambda_2 = u, \qquad \lambda_3 = u + c,
\]

where \(c = \sqrt{\gamma p/\rho}\) is the sound speed. The middle eigenvalue \(\lambda_2 = u\) corresponds to the **contact wave** — information advected at the fluid velocity without acoustic coupling. The outer eigenvalues \(\lambda_1, \lambda_3\) are genuinely nonlinear (shocks and rarefactions).

Diagonalizing \(\mathbf{J} = \mathbf{S}^{-1}\boldsymbol{\Lambda}\mathbf{S}\) is the algebraic heart of Roe's solver and of characteristic-based boundary conditions. Every Riemann solver, exact or approximate, is a different way of respecting these three wave speeds at a face.

## Godunov flux

The **Godunov flux** evaluates the exact Riemann solution at the face:

\[
F_{j+1/2} = F(U^*(0; U_j, U_{j+1})),
\]

where \(U^*(0; U_L, U_R)\) is the self-similar solution at \(x = 0\). Godunov's method (1959) is first-order accurate, conservative, and monotone — shocks are smeared over \(O(\Delta x)\) but without spurious oscillations.

Monotonicity implies **total variation diminishing (TVD)** behavior: the number of local extrema does not increase. For scalar conservation laws, this prevents Gibbs phenomena.

## Approximate Riemann solvers

Exact Riemann solvers for Euler are iterative and expensive. Production codes use **approximate Riemann solvers** that capture essential wave speeds at lower cost.

**Roe's solver** linearizes the flux Jacobian about an average state:

\[
\mathbf{A}_{\text{Roe}} = \mathbf{A}\left(\tfrac{1}{2}(U_L + U_R)\right) \quad \text{(with corrections)}.
\]

Discontinuities are replaced by linear wave structures. Roe works well for shocks but can violate entropy conditions (expansion shocks) without fixes.

**HLL (Harten–Lax–van Leer)** uses only wave speed estimates \(S_L, S_R\):

\[
F_{\text{HLL}} = \begin{cases} F_L & \text{if } S_L > 0 \\ F_R & \text{if } S_R < 0 \\ \frac{S_R F_L - S_L F_R + S_L S_R (U_R - U_L)}{S_R - S_L} & \text{otherwise} \end{cases}
\]

Robust and simple; smears contact discontinuities because a single intermediate state is assumed.

**HLLC** adds a **contact wave** at speed \(S_M\), resolving contact discontinuities sharply — standard in many Euler solvers.

| Solver | Waves resolved | Cost | Robustness |
|--------|---------------|------|------------|
| Exact Godunov | All | High | Excellent |
| Roe | Linearized | Medium | Good (with entropy fix) |
| HLL | 2 shocks | Low | Very robust |
| HLLC | 2 shocks + contact | Medium | Standard choice |

## Sod shock tube: setup and diagnostics

Sod's problem (1978) initializes on \([0,1]\):

- Left (\(x < 0.5\)): \(\rho_L = 1\), \(p_L = 1\), \(u_L = 0\)
- Right (\(x \ge 0.5\)): \(\rho_R = 0.125\), \(p_R = 0.1\), \(u_R = 0\)

The exact solution at time \(t = 0.2\) shows a leftward rarefaction, a contact at \(\rho \approx 0.265\), and a rightward shock.

The author's [FVM notes](https://hanfengzhai.github.io/note/FVM.pdf) use two additional verification cases on \([0,1]\) with \(\Delta t = 0.001\), \(t_{\text{final}} = 0.2\), and zero initial velocity on both sides:

| Case | \(\rho_L\) | \(p_L\) | \(\rho_R\) | \(p_R\) | Cells | Wave pattern |
|------|-----------|---------|-----------|---------|-------|--------------|
| Problem I | 1.0 | 0.7 | 1.0 | 0.2 | 300 | Equal density, pressure drop → expansion |
| Problem II (classic Sod) | 1.0 | 1.0 | 0.3 | 0.1 | 200 | Rarefaction–contact–shock |

Problem I isolates a **contact-like** density interface with a pressure-driven expansion — useful for checking that a scheme does not spuriously mix density when velocity and pressure start uniform. Problem II is the standard Sod configuration. A reference Python implementation is available at [python_finite_volume_solver](https://github.com/bwvdnbro/python_finite_volume_solver).

Comparing first- and second-order FVM against the exact Riemann solution at \(t = 0.2\) reveals the expected tradeoff: first-order schemes smear shocks over several cells but remain monotone; second-order MUSCL sharpens the profile at the cost of needing limiters near discontinuities.

Numerical diagnostics:

1. **Mass, momentum, energy** conserved to machine precision (conservative scheme).
2. **No overshoots** at shock or contact (monotonicity/limiters).
3. **L1 error** vs. exact solution decreases with mesh refinement (first-order near discontinuities, higher in smooth regions for MUSCL).

Failure modes: negative pressure (fix flux or add positivity limiter), oscillations at shock (need upwind or limiter), wrong wave speeds (bug in eigenstructure or units).

## Linear reconstruction and MUSCL

First-order Godunov smears discontinuities over many cells. **Higher-order** schemes reconstruct a piecewise linear profile in each cell:

\[
U(x) = U_j + (x - x_j)\, s_j, \qquad x \in \text{cell } j,
\]

where \(s_j\) is a **slope** from neighboring data. Unrestricted slopes produce oscillations (Godunov's theorem: linear TVD schemes are at most first order).

**MUSCL** (Monotone Upstream-centered Schemes for Conservation Laws) limits slopes:

\[
s_j \leftarrow \text{minmod}(s_j, \kappa \Delta U/\Delta x),
\]

preserving monotonicity while achieving second order in smooth regions. **Superbee**, **van Leer**, and **MC** limiters offer different accuracy–robustness tradeoffs.

The Riemann solver then sees **left and right extrapolated states** at the face:

\[
U_L = U_j + \tfrac{1}{2}\Delta x_j s_j, \qquad U_R = U_{j+1} - \tfrac{1}{2}\Delta x_{j+1} s_{j+1}.
\]

## WENO and very high order

**Weighted Essentially Non-Oscillatory (WENO)** schemes use adaptive stencils to achieve fifth-order accuracy in smooth regions while avoiding oscillations near shocks. WENO5 is standard in direct numerical simulation of compressible turbulence; cost is higher than MUSCL but resolution per cell is better.

For the copper wire's cooling jet at moderate Reynolds number, second-order MUSCL–HLLC suffices. For shock–turbulence interaction in hypersonics, WENO or DG enters.

## Discontinuous Galerkin: FEM meets FVM

**Discontinuous Galerkin (DG)** methods use discontinuous trial functions on elements, coupling cells through **numerical fluxes** identical to FVM Riemann solvers. Volume integrals handle high-order accuracy within cells; face fluxes handle inter-element coupling.

DG is increasingly popular for hyperbolic PDEs because it combines:

- Arbitrary order on unstructured meshes (FEM geometry flexibility),
- Local conservation and shock capturing (FVM philosophy),
- Parallel locality (element-wise operations).

The bridge between Part IV and Part V is explicit in DG: same shape functions as FEM, same Riemann fluxes as FVM.

## Entropy conditions and weak solutions

Nonlinear conservation laws admit multiple weak solutions. **Entropy conditions** (Lax entropy, entropy–viscosity) select the physically relevant shock. Approximate Riemann solvers include **entropy fixes** (e.g., Harten–Hyman for Roe) to prevent expansion shocks.

Viscous regularization provides another selection mechanism: solve Navier–Stokes with small viscosity, take the limit — the **vanishing viscosity** solution. FVM captures this limit when numerical fluxes are consistent and stable.

## 2D extension: dimensional splitting

Multi-D Euler on structured grids often uses **dimensional splitting**: apply 1D Riemann solvers in \(x\), then in \(y\) (or Strang splitting for second order). Unstructured FVM computes face fluxes along arbitrary normals using the normal flux \(\mathbf{F}\cdot\mathbf{n}\) from a 1D Riemann problem in the normal direction.

The 1D machinery in this chapter is not a toy — it is the kernel inside every multidimensional compressible solver.

## Connection to Part III and Part IV

Part III classified hyperbolic PDEs as distinct from elliptic. Part IV's Galerkin method lacks built-in upwinding for advection; SUPG stabilization adds Petrov–Galerkin bias. FVM embeds upwinding in the flux definition — natural for conservation laws.

When a problem mixes elliptic and hyperbolic parts (Navier–Stokes pressure, elastic wave propagation in FEM), choose the discretization per operator: FVM or upwind DG for advection; FEM or implicit FVM for diffusion and pressure.

## Debugging flux implementations

When a shock tube run fails, check in this order:

1. **Units and \(\gamma\)**: inconsistent pressure–energy relation gives wrong wave speeds.
2. **Conservation**: sum \(\Delta x_j U_j\) before and after a step; interior fluxes must telescope.
3. **Positivity**: if \(\rho\) or \(p\) goes negative, reduce CFL or switch to HLL/HLLC with an entropy fix.
4. **Boundary ghosts**: wrong ghost-cell values inject spurious waves at walls and inflows.
5. **Comparison to exact Sod solution** at fixed \(t\): plot \(\rho\), \(u\), \(p\) against Toro's reference.

Passing Sod at reasonable resolution is the gateway to 2D Riemann problems, nozzle flow, and eventually Navier–Stokes with viscous regularization of shocks.

## Lab act: Sod shock tube sanity check (Act II — Warming side channel)

**Act II** heats the wire; air around it carries heat away — a flow problem even if the operator only watches the thermocouple. Before coupling conjugate heat transfer in [V.4](04-navier-stokes-cfd.md), verify that your **hyperbolic kernel** is correct on the canonical 1D test every CFD course uses.

Run a Sod shock tube (Toro, *Riemann Solvers*, Example 4.1.1) with domain \([0,1]\), diaphragm at \(x = 0.5\), and initial left/right states:

| Quantity | Left (\(x < 0.5\)) | Right (\(x > 0.5\)) |
|----------|-------------------|---------------------|
| \(\rho\) | 1.0 | 0.125 |
| \(u\) | 0.0 | 0.0 |
| \(p\) | 1.0 | 0.1 |
| \(\gamma\) | 1.4 | 1.4 |

Use a first-order FVM with **HLLC** (or Roe + entropy fix) and CFL \(\approx 0.4\). At \(t = 0.2\):

| Check | Pass criterion | If it fails |
|-------|----------------|-------------|
| Mass | \(\sum_j \rho_j \Delta x_j\) constant to machine precision | Flux not conservative — check face indexing |
| Positivity | \(\rho > 0\), \(p > 0\) everywhere | Reduce CFL; switch to HLL |
| Shock position | Contact near \(x \approx 0.68\), shock near \(x \approx 0.85\) | Wrong \(\gamma\) or ghost cells |
| vs exact | L¹ error on \(\rho, u, p\) vs Toro reference \(< 5\%\) at 100 cells | Entropy fix or limiter missing |

Conceptual Python/pseudocode skeleton:

```python
for n in range(n_steps):
    for j in range(n_cells):
        UL, UR = left_state(j), right_state(j)
        F_star = hllc_flux(UL, UR, gamma=1.4)
        dU[j] = -(F_star[j+1] - F_star[j]) / dx
    U += dt * dU
```

This test has nothing to do with copper chemistry — it is the **trust gate** for the Riemann machinery that will later advect temperature in a boundary layer around the wire. Passing Sod at 100–200 cells takes minutes; failing it silently poisons every coupled solid–fluid run in Act II. Log the L¹ errors in a one-line regression test before touching wall heat flux handshakes with Part IV.

### Scale-boundary handshake: hyperbolic fluxes meet FEM wall temperature

Act II couples **solid conduction** (Part IV Galerkin on the wire) to **fluid advection–diffusion** (Part V FVM in the surrounding air). The handshake is not "run both solvers" — it is **consistent fluxes at the interface**:

| Interface quantity | FEM side (wire surface) | FVM side (first fluid cell) | Failure mode |
|--------------------|-------------------------|----------------------------|--------------|
| Wall temperature \(T_w\) | Dirichlet or Robin from solid solve | Ghost-cell \(T_{\text{ghost}}\) for advection | 1–2 K mismatch → wrong Biot number |
| Heat flux \(q''\) | \(-k_s \partial T / \partial n\) from solid | Convection \(h(T_w - T_\infty)\) in fluid | Flux imbalance → drifting \(T_w\) in Picard loop |
| Mass flux (if blowing) | Usually zero for passive wire | Normal velocity at wall | Spurious mass source if not conservative |

The Sod shock-tube test certifies the **Riemann kernel** in isolation; the 1D boundary-layer Lab act in [V.2](02-fvm-1d.md) certifies **diffusive fluxes** on linear profiles. Only after both pass should Part V.4's conjugate heat transfer Picard loop exchange \(T_w\) and \(q''\) with Part IV — the same staggered discipline Part I.4 named for thermo-mechanical blocks and Part III.2 named for coupled weak forms.

**What breaks without the handshake.** A converged FEM solid mesh with an FVM air mesh that fails Sod conserves energy in the solid while **advecting negative density** in the fluid — the coupled run looks stable until the boundary layer temperature is wrong by 20 K and Joule heating predictions fail Act II validation.

## Concept map checkpoint (Riemann fluxes)

This chapter is where hyperbolic conservation laws receive **upwind stability**. Before Navier–Stokes adds viscous partners, summarize what Riemann solvers established:

| Question | Part V answer (copper wire) |
|----------|-----------------------------|
| What **object**? | Left/right states \(U_L, U_R\); numerical flux \(F^*_{i+1/2}\); wave speeds |
| What **structure**? | Godunov / Roe / HLLC flux functions; CFL limit \(\Delta t \sim \Delta x / \lambda_{\max}\) |
| What **theorem**? | Rankine–Hugoniot jump conditions; discrete conservation with conservative flux differencing |
| What **breaks**? | Entropy violations (expansion shocks); \(\rho<0\) or \(p<0\) without limiters; wrong ghost cells |

The Sod shock-tube Lab act is the fluid-side patch test: mass conserved to machine precision, shock positions within 5% at 100 cells. Passing Sod before coupling FEM wall temperature to FVM air is the same discipline as Part IV's patch test before trusting Act II conjugate heat transfer.

## Bridge

Navier–Stokes adds viscous fluxes, heat conduction, and the incompressibility constraint. CFD combines hyperbolic advection — FVM's strength — with parabolic diffusion and elliptic pressure fields that resemble Part IV's Stokes solvers.

| What Riemann fluxes gave | What Navier–Stokes CFD (next chapter) adds |
|--------------------------|--------------------------------------------|
| Godunov-type stability for hyperbolic conservation | Viscous and heat fluxes regularize shocks |
| Upwind bias from wave speeds | Reynolds number: advection vs diffusion balance |
| Sod shock tube as correctness gate | Low-Re cooling flow around the copper wire |
| FVM integral balance on cells | Pressure–velocity coupling; turbulence closures at high Re |

The copper wire heated by current needs air to carry heat away — a fluid problem sitting beside the solid conduction Part IV already meshed. Riemann solvers handled the **hyperbolic** vocabulary; Navier–Stokes adds the **parabolic** and **elliptic** partners that make conjugate heat transfer a coupled story rather than two unrelated codes. When the wall temperature and wall flux handshake between solid and fluid, you are watching Part IV and Part V speak at an interface — the same partitioned coupling pattern the epilogue generalizes to DFT→MD→DDD→FEM chains.

The next chapter situates the full fluid mechanics pipeline, from Reynolds number to turbulence models, with the copper wire's cooling flow as motivation. Turn the page when Sod passes but the wire still runs hot — that is the signal to add viscosity, conduction, and the shared continuum vocabulary Part VI will name.
