# Sobolev Spaces: Regularity for Computation

Sobolev spaces measure how much smoothness a function has in an \(L^2\) sense. They are the native habitat of weak solutions and conforming finite elements.

When we approximate the temperature on the copper wire with piecewise-linear hat functions, the discrete field is continuous but has kinks at nodes. It is not twice differentiable in the classical sense — yet finite element solutions of Poisson's equation are meaningful because kinks are allowed in \(H^1\): only the **first** weak derivative must live in \(L^2\). Sobolev spaces encode exactly that level of regularity.

## Scene: kinks at the nodes

Mesh the copper wire for steady Joule heating with ten linear bar elements. Plot the temperature: a continuous broken line, slope changing abruptly at each node, nowhere twice differentiable in the classical sense. A mathematician trained on \(C^2\) solutions might reject the picture; a finite element practitioner recognizes it as a **conforming \(H^1\)** approximation — continuous across elements, square-integrable gradient piecewise constant.

Now refine to a hundred elements. The kinks remain at nodes, but the profile smooths toward the true \(T(x)\). Sobolev spaces are the room where both the limit function and every mesh refinement live together: we measure regularity by \(\|\nabla T\|_{L^2}\), not by pointwise second derivatives. This scene is why weak formulations beat classical ones at grip corners and reentrant notches — the physics cares about energy in gradients, not about curvature at every point.

## Weak derivatives

A function \(u \in L^2(\Omega)\) has **weak derivative** \(\partial u / \partial x_i = w \in L^2(\Omega)\) if

\[
\int_\Omega u \frac{\partial \phi}{\partial x_i} = -\int_\Omega w \phi \quad \forall \phi \in C_c^\infty(\Omega).
\]

Integration by parts in the classical sense becomes a **definition** in the weak sense. Smooth functions satisfy this definition with \(w = \partial u / \partial x_i\); piecewise smooth functions with jumps in slope satisfy it with \(w\) piecewise equal to the classical derivative on each smooth piece.

### Worked example: absolute value on \((-1,1)\)

\(u(x) = |x|\) is not classically differentiable at \(0\), but it has weak derivative \(u'(x) = \mathrm{sign}(x)\) in \(L^2(-1,1)\). Verify with integration by parts against \(\phi \in C_c^\infty\): boundary terms vanish, and the integral of \(|x|\,\phi'\) equals \(-\int \mathrm{sign}(x)\,\phi\). The kink does not break membership in \(H^1\).

Functions with **discontinuities** (jumps) generally do **not** belong to \(H^1\): a jump creates a delta-like object in the weak derivative, not an \(L^2\) function. Conforming scalar Lagrange elements are therefore **continuous** across element boundaries — \(H^1\) conformity requires \(C^0\) continuity in typical FEM.

## The Sobolev space \(H^1(\Omega)\)

\[
H^1(\Omega) = \left\{ u \in L^2(\Omega) : \frac{\partial u}{\partial x_i} \in L^2(\Omega),\; i = 1,\ldots,d \right\}
\]

with norm

\[
\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2.
\]

\(H^1(\Omega)\) is a Hilbert space with inner product \((u,v)_{H^1} = (u,v)_{L^2} + (\nabla u, \nabla v)_{L^2}\). Completeness (Part II) ensures Cauchy sequences of approximate wire temperatures converge to a limit in \(H^1\), not merely pointwise.

The **Sobolev number** \(k - d/p\) governs embedding: for \(H^k\) in \(L^p\), one needs \(k - d/p > 0\) for continuous embedding into \(L^p\).

## Boundary traces

Functions in \(H^1(\Omega)\) have **traces** on \(\partial\Omega\): there exists a bounded operator \(\gamma: H^1(\Omega) \to L^2(\partial\Omega)\) such that \(\gamma u = u|_{\partial\Omega}\) when \(u\) is smooth. Dirichlet boundary conditions are imposed on \(\gamma u\).

The subspace

\[
H^1_0(\Omega) = \{ u \in H^1(\Omega) : \gamma u = 0 \text{ on } \partial\Omega \}
\]

is closed. It is the standard trial space for homogeneous Dirichlet problems — fixed temperature on the entire boundary of the wire, or clamped displacement on a specimen.

| Space | Boundary behavior | Typical BC |
|-------|-------------------|------------|
| \(H^1(\Omega)\) | Trace \(\gamma u \in L^2(\partial\Omega)\) | Dirichlet on part of \(\partial\Omega\) |
| \(H^1_0(\Omega)\) | \(\gamma u = 0\) | Homogeneous Dirichlet |
| \(H^1_0 \cap \{u: \gamma u|_{\Gamma_D} = g\}\) | Affine space | Inhomogeneous Dirichlet |

Inhomogeneous Dirichlet data \(u = g\) on \(\Gamma_D\) is handled by writing \(u = g + w\) with \(w \in H^1_0\) (or zero extension of \(g\) when \(g\) is a trace of an \(H^1\) function).

## Poincaré inequality

For bounded \(\Omega\),

\[
\|u\|_{L^2} \le C_P \|\nabla u\|_{L^2} \quad \forall u \in H^1_0(\Omega).
\]

Coercivity of the Laplacian bilinear form on \(H^1_0\) follows: \(a(u,u) = \|\nabla u\|_{L^2}^2 \ge C_P^{-2}\|u\|_{L^2}^2\), so \(\|\nabla u\|_{L^2}\) and \(\|u\|_{H^1}\) are equivalent on \(H^1_0\). The constant \(C_P\) depends on domain geometry — narrow domains (long thin copper wire segments in 2D/3D models) have large \(C_P\), worsening conditioning of stiffness matrices.

** Friedrichs inequality** is the vector analogue for elasticity: \(\|\mathbf{u}\|_{L^2} \le C \|\boldsymbol{\varepsilon}(\mathbf{u})\|_{L^2}\) on kinematically admissible fields — Korn's inequality makes this precise.

## Sobolev embedding (selected cases)

| Dimension | Embedding | Consequence for FEM |
|-----------|-----------|---------------------|
| \(d=1\) | \(H^1 \hookrightarrow C^0\) | Continuous functions; nodal values meaningful |
| \(d=2\) | \(H^1 \hookrightarrow L^p\), \(p < \infty\) | Not necessarily pointwise defined |
| \(d=3\) | \(H^1 \hookrightarrow L^6\) | \(L^6\) control on nonlinear terms (hyperelasticity) |
| \(d=3\) | \(H^2 \hookrightarrow C^0\) on nice domains | Quadratic elements yield continuous fields |

In 1D, \(H^1\) functions are continuous — the temperature along the wire is unambiguous at nodes. In 3D, \(H^1\) fields may not have point values; FEM still assigns nodal values because basis functions are smooth enough that restrictions to nodes make sense.

## Conforming finite elements

A **conforming** finite element space \(V_h \subset H^1(\Omega)\) satisfies:

1. Global continuity across element interfaces (for scalar Lagrange elements)
2. Polynomial structure on each element

Assembly uses \(a(u_h, v_h)\) with \(u_h, v_h \in V_h\); conformity ensures the discrete bilinear form is the restriction of the continuum form — no extra interface terms for standard elliptic problems.

**Non-conforming** methods (e.g. Crouzeix–Raviart, discontinuous Galerkin) enlarge or shift the space and weakly enforce continuity through numerical fluxes — common in hyperbolic problems (Part V). DG for Poisson adds penalty terms on jumps; advection–diffusion uses upwind fluxes.

| Element | Local space | Global conformity | Order (Poisson) |
|---------|-------------|-------------------|-----------------|
| P1 (linear) | \(\mathbb{P}_1\) | \(H^1\) | \(O(h)\) in \(H^1\) |
| P2 (quadratic) | \(\mathbb{P}_2\) | \(H^1\) | \(O(h^2)\) in \(H^1\) on smooth solutions |
| CR | piecewise linear | not \(H^1\) | Non-conforming elliptic schemes |

## Higher-order Sobolev spaces

\[
H^k(\Omega) = \{ u \in L^2 : D^\alpha u \in L^2,\; |\alpha| \le k \}.
\]

Classical \(C^2\) solutions of Poisson's equation on smooth domains with smooth \(f\) live in \(H^2\), enabling **optimal** \(H^1\) error estimates: \(\|u - u_h\|_{H^1} = O(h^p)\) for degree-\(p\) elements when \(u \in H^{p+1}\).

Corner singularities on the L-shaped domain (or at the loaded point on a coarse model of the wire) reduce regularity: \(u \in H^{1+s}\) for some \(s < 1\) only. Adaptive refinement targets localized loss of \(H^2\) regularity; a priori rates degrade to \(O(h^s)\) in energy norm.

### Regularity checklist for the practitioner

| Geometry / data | Typical regularity | FEM implication |
|-----------------|-------------------|-----------------|
| Smooth domain, smooth \(f\) | \(u \in H^{p+1}\) | Optimal rates for degree-\(p\) elements |
| Reentrant corner | \(u \notin H^2\) locally | Refine near corner; suboptimal rate |
| Discontinuous \(f\) | \(u \in H^2\) away from jumps | Refine at load discontinuities |
| Neumann on part of boundary | Need compatibility \(\int f = 0\) | Pure Neumann adds constant null mode |

## Fractional Sobolev spaces on boundaries

Trace spaces on \(\partial\Omega\) are not \(H^1(\partial\Omega)\) but **fractional** Sobolev spaces \(H^{1/2}(\partial\Omega)\) for the values and \(H^{-1/2}(\partial\Omega)\) for fluxes. This fine print matters in mortar methods and domain decomposition — coupling subdomains that model different parts of a copper fixture. For standard conforming FEM on a single mesh, enforcing Dirichlet data on nodal values suffices; the trace theory explains *why* those nodal values are legitimate.

## Dual spaces and linear functionals

The dual \(H^{-1}(\Omega) = (H^1_0(\Omega))^*\) contains point loads and fluxes. A point force on the wire is not an \(L^2\) function; it is a functional \(\ell(v) = F v(x_0)\). Lax–Milgram still applies when \(\ell \in H^{-1}\) — bounded on \(H^1_0\). FEM represents such loads by lumping or by regularizing over a small element.

## Trace operators and interface conditions

On a subdomain interface \(\Gamma\) between solid and fluid (copper wire and coolant), traces \(T|_\Gamma\) and flux \(-k\partial T/\partial n\) appear in coupled formulations. Sobolev trace theory ensures these quantities are in \(L^2(\Gamma)\) for \(H^1\) fields — the mathematical basis for conjugate heat transfer coupling in industrial codes.

## Connection to finite volumes

FVM (Part V) often works with **cell averages** in \(L^2\)-like spaces on dual meshes rather than nodal \(H^1\) conformity. Discontinuous fields across faces are expected; flux quadrature replaces weak derivatives of test functions. Sobolev theory still underlies stability proofs for elliptic FVM through discrete Poincaré inequalities on mesh-dependent spaces.

## Worked example: checking \(H^1\) membership

On \(\Omega = (0,1)\), \(u(x) = x^{1/2}\) is in \(L^2\) but \(u'(x) = \tfrac{1}{2}x^{-1/2}\) is not square-integrable near \(0\), so \(u \notin H^1(0,1)\). By contrast, \(u(x) = x^{3/2}\) has \(u' \sim x^{1/2} \in L^2\) — admissible in a weak formulation on the full interval. This explains why singular corners and reentrant notches are trouble spots: local behavior mimics fractional powers that strip \(H^2\) regularity even when \(H^1\) membership holds.

Piecewise-linear finite element fields on the copper wire are globally in \(H^1\) (continuous, slope jumps in \(L^2\)) but generally not in \(H^2\). That gap between \(H^1\) and \(H^2\) is exactly the regularity margin standard Lagrange elements require — and why optimal \(H^1\) error estimates need \(H^2\) on the true solution, not on the discrete one.

## Summary: Sobolev vocabulary for coding

| Symbol | Meaning in code |
|--------|-----------------|
| \(H^1_0\) | Trial space with zero Dirichlet BC on \(\Gamma_D\) |
| \(\gamma u\) | Nodal boundary values / Dirichlet constraints |
| \(\|\nabla u\|_{L^2}\) | Strain energy seminorm in elasticity |
| \(H^{-1}\) load | Point forces, concentrated fluxes |
| \(H^2\) regularity | Enables \(O(h^2)\) convergence for P1 on Poisson |

## Lab act: patch-test \(H^1\) membership on the heated wire (Act II — Warming)

**Act II** reports a thermocouple climb while the grips stay fixed. The FEM temperature you will assemble in Part IV is not a smooth \(C^2\) curve — it is a broken line of hat functions, kinked at every node. Sobolev spaces are the contract that makes those kinks legal.

Take the copper wire segment \((0,L)\) with \(L = 1\,\text{m}\) and a **three-node** mesh: nodes at \(0\), \(L/2\), and \(L\), with \(T(0) = T(L) = 300\,\text{K}\). Approximate the interior rise with a single hat function \(\phi_1(x)\) peaked at mid-span:

\[
T_h(x) = 300 + \Delta T \,\phi_1(x), \qquad \phi_1(x) = \begin{cases} 2x/L & x \le L/2 \\ 2(L-x)/L & x \ge L/2 \end{cases}
\]

| Check | Computation | Verdict |
|-------|-------------|---------|
| \(T_h \in L^2\)? | \(\|T_h\|_{L^2}^2 = \int (300 + \Delta T \phi_1)^2 < \infty\) | Yes — bounded on finite domain |
| Weak derivative \(T_h' \in L^2\)? | \(T_h' = \Delta T \cdot (\pm 2/L)\) piecewise constant | Yes — jump at \(L/2\) is fine in \(L^2\) |
| \(T_h \in H^2\)? | \(T_h''\) is a delta at the node, not an \(L^2\) function | **No** — explains why P1 gives \(O(h)\), not \(O(h^2)\), without extra regularity |
| Dirichlet trace | \(T_h(0) = T_h(L) = 300\) | Satisfied — \(H^1\) conformity for scalar Lagrange elements |

Now refine to ten equal elements and plot \(\|T_h'\|_{L^2}^2 = \int (T_h')^2 \, dx\) versus mesh size \(h\). The gradient energy should stabilize toward the true \(\int (T')^2\) as \(h \to 0\) even though kinks persist at nodes — completeness (Part II) guarantees the limit stays in \(H^1\).

**Failure mode to watch:** if you accidentally allow a temperature **jump** across an element interface (discontinuous \(T_h\)), the weak derivative produces a delta-like distribution and \(T_h \notin H^1\). Conforming FEM avoids this by enforcing \(C^0\) continuity — the same reason Part IV's shape functions share nodes. When the thermocouple reading disagrees with a coarse three-node mesh, the fix is refinement in \(H^1\), not higher classical smoothness.

## Concept map checkpoint (Sobolev spaces)

Sobolev spaces are the **room** where the weak form from [III.2](02-weak-form.md) lives. Before energy methods package existence as minimization, name what \(H^1\) and \(L^2\) buy on the copper wire:

| Question | Sobolev answer (copper wire) |
|----------|------------------------------|
| What **object**? | Fields \(u \in H^1(\Omega)\) with \(\nabla u \in L^2\); temperature \(T \in H^1\), flux in \(L^2\) |
| What **structure**? | Weak derivatives; trace theorem (boundary values); Poincaré inequality on \(H^1_0\) |
| What **theorem**? | Rellich–Kondrachov compactness in 2D/3D; embedding \(H^1 \hookrightarrow L^2\) |
| What **breaks**? | Discontinuous \(T_h\) across elements (\(T_h \notin H^1\)); assuming \(H^2\) when only \(H^1\) is guaranteed |

The thermocouple in Act II measures a **continuous** temperature field even when Joule heating kinks the gradient at weld points — that is \(H^1\) membership, not classical \(C^2\) smoothness. Part IV's conforming shape functions are designed to stay inside this room; Part V's cell averages live in a different room (conservation-first, not variational). When mesh refinement stalls, ask whether the discrete field still belongs to the Sobolev space the weak form assumed — the same audit Part II taught for completeness.

## Bridge

Energy methods package weak forms as minimization problems. They unify FEM, provide physical intuition, and extend naturally to nonlinear elasticity where the energy functional may be polyconvex rather than quadratic. The Dirichlet principle identifies weak solutions of Poisson with minimizers of \(\Pi(u)\); coercivity on \(H^1_0\) is the same hypothesis as in Lax–Milgram.

| What Sobolev spaces gave | What energy methods (next chapter) add |
|--------------------------|----------------------------------------|
| \(H^1\) membership: \(\nabla u \in L^2\) | Dirichlet principle: weak solution = energy minimizer |
| \(H^1_0\) encodes Dirichlet BC | Rayleigh–Ritz preview: minimize on \(V_h\) → Part IV assembly |
| \(H^2\) regularity enables \(O(h^2)\) rates | Saddle-point forms where minimization alone fails (Stokes) |
| Piecewise-linear FEM fields live in \(H^1\), not \(H^2\) | Polyconvex energies for nonlinear elasticity (Part VI preview) |

**Scale-boundary handshake (III.3 → III.4 → Part IV).**

| Sobolev contract (this chapter) | Energy method consumer ([III.4](04-energy-methods.md)) | FEM discretization (Part IV) | Failure mode |
|---------------------------------|--------------------------------------------------------|------------------------------|--------------|
| \(T \in H^1\): continuous, \(T' \in L^2\) | Dirichlet principle: minimize \(\Pi[T] = \int \tfrac{k}{2}|\nabla T|^2 - qT\) | P1 hat functions on wire mesh (Act II) | Temperature jump across element → \(T_h \notin H^1\) |
| \(H^1_0\) encodes zero Dirichlet on grips | Elastic \(\Pi[\mathbf{u}]\) with essential BC on displacement | Mechanical block shares mesh with thermal (Act III) | Thermal expansion eigenstrain omitted |
| \(H^2\) regularity → \(O(h^2)\) for P1 Poisson | Rayleigh–Ritz on \(V_h\) equivalent to Galerkin | [IV.2](../part04-fem/02-galerkin-assembly.md) assembly loop | Expecting \(O(h^2)\) when true solution is only \(H^1\) |
| Trace theorem: boundary values in \(L^2(\partial\Omega)\) | Natural BC from \(\delta\Pi\) | Neumann face quadrature in [IV.3](../part04-fem/03-elements-quadrature.md) | Robin convection assembled without trace consistency |
| Rellich–Kondrachov compactness in 2D/3D | Coercivity + compactness → existence | Patch test certifies \(V_h \subset H^1\) | Non-conforming elements without inf–sup audit |

The thermocouple Lab act proved \(T_h \in H^1\) on three nodes but \(T_h \notin H^2\) — the regularity gap that separates **membership** (enough for weak forms) from **rate** (enough for optimal convergence). [III.4](04-energy-methods.md) packages that membership as energy minimization; Part IV discretizes the minimizer on \(V_h\).

The copper wire's displacement minimizes elastic energy in \(H^1\); its temperature minimizes a quadratic functional with conductivity \(k(x)\). Those are not separate tricks — they are the same variational pattern [III.2](02-weak-form.md) wrote as \(a(u,v)=\ell(v)\), now dressed as \(\delta\Pi[u]=0\). When incompressibility or mixed stress–displacement formulations appear, minimization alone is insufficient; saddle-point structure (LBB) enters — the same inf–sup language Part IV will meet again for Stokes.

Return to the [prologue](../prologue/00-many-scales.md): in **Act II — Warming**, the thermocouple climbs while the grips still hold fixed displacement. The temperature field \(T(x)\) that drives that reading must live in \(H^1\) — continuous across the wire, with square-integrable gradient — even though Joule heating and surface convection make \(T\) kinked at the thermocouple weld and insulator corner. Piecewise-linear FEM temperatures are globally in \(H^1\) but not in \(H^2\); that gap is exactly why optimal \(O(h^2)\) rates need smoother true solutions than the discrete fields themselves possess. Sobolev membership is not pedantry — it is the contract the thermocouple and the load cell both assume.

The next chapter develops that variational picture and closes Part III with the energy pipeline that Part IV discretizes: strong PDE → weak form → energy or saddle functional → search on \(V_h\). Turn the page when you want to see why "assemble \(\mathbf{K}\) from shape functions" is Rayleigh–Ritz minimization in disguise.
