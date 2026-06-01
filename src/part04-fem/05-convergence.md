# Convergence, Norms, and Error Estimates

A FEM solution that looks smooth is not necessarily accurate. Convergence theory tells us how error decreases with mesh refinement — and which norms matter for which quantities.

## Céa's lemma

For coercive bilinear form \(a(\cdot,\cdot)\) and Galerkin approximation \(u_h\),

\[
\|u - u_h\|_{H} \le C \inf_{v_h \in V_h} \|u - v_h\|_{H}.
\]

The FEM error is bounded by the **best approximation error** in the same norm, up to a constant depending on coercivity and continuity constants.

## Approximation error and mesh size

For P1 elements on quasi-uniform meshes of size \(h\),

\[
\inf_{v_h \in V_h} \|u - v_h\|_{H^1} \le C h \|u\|_{H^2}
\]

when \(u \in H^2\). Hence \(\|u - u_h\|_{H^1} = O(h)\). **Duality arguments** (Aubin–Nitsche) often yield \(\|u - u_h\|_{L^2} = O(h^2)\) — one order higher for the field itself.

Higher-order elements (\(p\)-refinement) increase the power of \(h\) at the cost of denser local matrices.

## A posteriori estimates

**A posteriori** error estimators use the computed \(u_h\) to estimate \(\|u - u_h\|\) without knowing \(u\). Residual-based and recovery-based estimators drive **adaptive mesh refinement** — refining where local error indicators are large.

## Pollution and singularities

Corner singularities reduce regularity below \(H^2\). Uniform refinement then yields suboptimal rates; localized refinement (graded meshes toward corners) restores performance. **Pollution** in Helmholtz problems at high wave number requires resolution per wavelength — FEM for wave propagation is harder than for elliptic Poisson.

## Connection to teaching practice

Stanford ME 335A problem sessions walk this pipeline explicitly:

1. Formulate the variational problem for a PDE
2. Clarify the function space of test and trial functions
3. Discretize with shape functions on a mesh
4. Assemble local-to-global systems
5. Study norms and convergence numerically

Those steps — documented in the [FEA teaching notes](https://hanfengzhai.github.io/note.html) — are the practical face of the theorems in this chapter.

## Bridge to Part V

Elliptic solids favor FEM: global coupling, energy minimization, symmetric stiffness. Hyperbolic fluids favor conservation-form discretizations where fluxes balance across cell interfaces. The finite volume method — Part V — is that story.
