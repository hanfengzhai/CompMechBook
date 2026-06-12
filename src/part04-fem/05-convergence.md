# Convergence, Norms, and Error Estimates

A finite element mesh of the copper wire can look impressively fine — thousands of tetrahedra, smooth color contours of stress — and still be wrong. Visualization is not verification. Convergence theory answers the question that every computational mechanician must ask: *if I refine the mesh, does the error decrease at a predictable rate, and in which norm?*

This chapter connects Part I's discrete norms, Part II's function-space error analysis, and Part IV's implementation choices (\(h\), \(p\), element type) into a coherent refinement strategy.

## Galerkin orthogonality and Céa's lemma

Let \(u \in V\) solve the weak problem \(a(u,v) = \ell(v)\) for all \(v \in V\), and let \(u_h \in V_h \subset V\) solve the discrete problem \(a(u_h, v_h) = \ell(v_h)\) for all \(v_h \in V_h\).

The **Galerkin orthogonality of the error** states:

\[
a(u - u_h, v_h) = 0 \quad \forall v_h \in V_h.
\]

The continuous error \(e = u - u_h\) is orthogonal to the test space in the energy inner product — the discrete solution is the **best approximation** in that sense.

**Céa's lemma** bounds the error by the best approximation error in the same norm. If \(a(\cdot,\cdot)\) is coercive and continuous on \(V\),

\[
\|u - u_h\|_{H} \le C \inf_{v_h \in V_h} \|u - v_h\|_{H},
\]

where \(\|\cdot\|_H\) is the norm induced by \(a(\cdot,\cdot)\) (the **energy norm**) and \(C\) depends on coercivity and continuity constants but not on \(h\).

Consequence: FEM does not introduce extra error beyond discretization. If the approximation space can represent the solution well, the FEM solution is nearly as good as the best possible approximation in that space.

## Approximation theory and mesh size \(h\)

The infimum in Céa's lemma is controlled by **approximation properties** of \(V_h\). For Lagrange elements of order \(p\) on quasi-uniform meshes of characteristic size \(h\):

\[
\inf_{v_h \in V_h} \|u - v_h\|_{H^1} \le C h^{p} \|u\|_{H^{p+1}}
\]

when \(u\) has sufficient regularity (\(u \in H^{p+1}\)). For **P1 elements** (\(p = 1\)):

\[
\|u - u_h\|_{H^1} = O(h), \qquad \|u - u_h\|_{L^2} = O(h^2).
\]

The \(L^2\) rate is one order higher — a **duality argument** (Aubin–Nitsche trick) that exploits elliptic regularity. Part I's discrete \(L^2\) norm with mass matrix \(\mathbf{M}\) is the finite-dimensional shadow of this result.

For **P2 elements** (\(p = 2\)):

\[
\|u - u_h\|_{H^1} = O(h^2), \qquad \|u - u_h\|_{L^2} = O(h^3).
\]

\(p\)-refinement increases accuracy on fixed meshes when solutions are smooth — but each element carries more DOFs and denser local matrices.

## Energy norm vs. field norms

| Norm | Definition (discrete) | Physical meaning |
|------|----------------------|------------------|
| Energy | \(\|u - u_h\|_a = \sqrt{a(u-u_h, u-u_h)}\) | Natural for elliptic problems; equals strain energy of error |
| \(L^2\) | \(\sqrt{\int (u-u_h)^2}\) | Mean-square field error (temperature, displacement) |
| \(L^\infty\) | \(\max_x |u(x) - u_h(x)|\) | Worst-point error; harder to estimate a priori |
| Stress (postprocessed) | \(\|\boldsymbol{\sigma} - \boldsymbol{\sigma}_h\|\) | Often **not** superconvergent; stresses derived from derivatives |

For the copper wire under tension, displacement in \(L^2\) may converge at \(O(h^2)\) with P1 elements, but stress at nodes — computed from strains via Hooke's law — converges more slowly and oscillates near boundaries unless **superconvergent patch recovery** or higher-order elements are used.

Problem Session 8 in the [FEA teaching notes](https://hanfengzhai.github.io/note.html) computes these norms numerically on manufactured solutions — the empirical face of the theorems.

## Numerical convergence studies

To verify an implementation, solve a problem with known exact solution \(u\) and measure \(\|u - u_h\|\) on a sequence of meshes with decreasing \(h\). Plot \(\log(\text{error})\) vs. \(\log(h)\); the slope reveals the convergence rate.

Example: Poisson on \((0,1)^2\) with \(u = \sin(\pi x)\sin(\pi y)\). P1 FEM should show slope \(\approx 2\) in \(L^2\) and slope \(\approx 1\) in \(H^1\). Deviations indicate bugs (wrong sign in stiffness, incorrect Jacobian, missed boundary term) or insufficient quadrature.

For elasticity, use the **Kirsch problem** (hole in infinite plate) or **Timoshenko beam** solutions. Compare \(L^2\) displacement error and energy norm error separately.

## A priori vs. a posteriori estimates

**A priori** estimates (Céa's lemma plus approximation theory) require knowledge of the solution's regularity — often unknown for complex geometries. They tell us what rate to expect asymptotically but not whether the current mesh is adequate.

**A posteriori** error estimators use only the computed \(u_h\) to estimate \(\|u - u_h\|\):

- **Residual-based**: element residual \(\|f + \Delta u_h\|_{L^2(K)}\) plus jump terms across faces.
- **Recovery-based (ZZ)**: postprocess \(u_h\) to a smoother \(\tilde{u}\); use \(\|\tilde{u} - u_h\|\) as error indicator.

These indicators drive **adaptive mesh refinement (AMR)**: subdivide elements where local error is large, coarsen where it is small. AMR can achieve target accuracy with far fewer DOFs than uniform refinement — essential for crack-tip resolution and multiscale features.

## Singularities, corners, and pollution

Regularity assumptions fail at:

- **Reentrant corners** (L-shaped domain): \(u \notin H^2\); P1 FEM on uniform meshes yields suboptimal rates.
- **Crack tips**: strain singular; linear elasticity predicts infinite stress.
- **Point loads** in 2D/3D: displacement singularities in classical theory.

**Graded meshes** — smaller elements toward singularities — restore optimal convergence rates. Isoparametric refinement toward a crack tip captures the singularity geometry.

**Pollution** in Helmholtz and wave problems at high wave number \(k\): error is not local; coarse regions pollute fine regions. Resolution requires \(h \sim \lambda/k\) (points per wavelength). FEM for wave propagation is harder than for elliptic Poisson — a warning for vibration and acoustics of the copper wire at high frequency.

## \(h\)-refinement vs. \(p\)-refinement

| Strategy | Action | Best when |
|----------|--------|-----------|
| \(h\)-refinement | More elements, same order | Singularities, complex geometry |
| \(p\)-refinement | Higher order, same mesh | Smooth solutions, high accuracy need |
| \(hp\)-refinement | Both | Exponential convergence for piecewise analytic solutions |

Industrial practice often uses low-order elements (\(p = 1\) or 2) with aggressive \(h\)-refinement because automatic meshers handle geometry better than high-order curved elements. Research codes and isogeometric analysis push \(p\) higher.

## Stability beyond elliptic problems

Céa's lemma requires coercivity. **Stokes flow** and **incompressible elasticity** replace coercivity with inf–sup stability (LBB condition from Part III). Error bounds involve stability constants that degrade if mixed elements are chosen incorrectly — Taylor–Hood \((P2,P1)\) is stable; equal-order \((P1,P1)\) is not without stabilization.

**Maxwell's equations** and **advection-dominated transport** require specialized elements or Petrov–Galerkin stabilization. Convergence theory exists but the constants and norms differ.

## The teaching pipeline completed

Stanford ME 335A problem sessions trace the full arc:

1. Formulate the variational problem (Part III, weighted residuals).
2. Clarify function spaces (Part II, Sobolev).
3. Discretize with shape functions (Chapter 3).
4. Assemble local-to-global systems (Chapter 2).
5. Study norms and convergence numerically (this chapter).

The [Course Summary](https://hanfengzhai.github.io/note.html) ties these steps to primal FEM for elliptic problems in 1D, 2D, and 3D — structural, solid, fluid, and heat transfer applications. The mathematics in this book is the conceptual spine; the problem sessions are the laboratory.

## Copper wire: a refinement narrative

Imagine simulating tensile failure initiation on the copper wire:

1. Coarse mesh: capture global load path; stress peaks are wrong near the grip.
2. Uniform refinement: displacement converges; stress at the notch still poor.
3. Adaptive refinement toward stress concentrations: a posteriori indicators flag the grip region.
4. Optional \(p\)-refinement on smooth regions away from singularities.

Each step checks whether \(\|u - u_h\|\) decreases at the predicted rate. If not, the fault lies in the mesh, the element, or the code — not in the physics.

## Goal-oriented error control

Engineers often care not about \(\|u - u_h\|_{H^1}\) but about a **quantity of interest** \(Q(u)\) — peak stress at the copper wire grip, total reaction force, or compliance under load. **Goal-oriented a posteriori estimation** bounds \(|Q(u) - Q(u_h)|\) using adjoint solutions. Adaptive refinement then targets the mesh where it improves \(Q\), not where a generic \(L^2\) indicator is large.

This adjoint viewpoint connects FEM error analysis to design optimization and sensitivity analysis: the same dual problem that estimates error also supplies gradients for shape optimization.

## Software verification habits

Before trusting a mesh for a design decision:

1. Run at least two successive refinements; confirm error or \(Q(u_h)\) changes at the expected rate.
2. Perform a patch test and a manufactured-solution test on a unit square or bar.
3. Compare against an independent code or analytical solution at a limiting case (e.g., thick-walled cylinder, Bernoulli beam).
4. Document element type, quadrature order, and solver tolerance — convergence in the field can mask a stale linear solve.

These habits mirror verification protocols in the FEA teaching notes and align with ASME and NASA CFD verification guidelines extended to solids.

## Bridge to Part V

Elliptic solids — the copper wire in tension, a bridge under dead load, steady heat conduction — favor FEM: global coupling, symmetric stiffness, energy minimization. Fluids at high Reynolds number, shocks, and steep advection fronts favor a different philosophy: integrate conservation laws over control volumes and balance **fluxes** across faces. The finite volume method, Part V, is that story — complementary to FEM, not competing with it. Coupled fluid–structure problems stitch the two at interfaces where the wire meets the cooling air.
