# Part IV — The Finite Element Method

Part III reduced continuum mechanics to weak forms: bilinear forms on Sobolev spaces, loads as dual functionals, energy functionals with unique minimizers. Part IV asks the engineer's question: *how do we compute those solutions on a mesh?*

The finite element method is the answer for elliptic and parabolic problems on complex geometries — the copper wire in tension, a bracket with a reentrant corner, a heated solid coupled to a fluid boundary. We begin with **weighted residuals**, the family of methods that includes Galerkin's method as its most important member, then build element-by-element assembly, quadrature, and convergence theory that connects discrete stiffness matrices to the infinite-dimensional operators of Part II.

The layout follows the **FEM Notes** in [`writings/fem/`](../../writings/fem/): five numbered chapters from residuals through error estimates, with **Bridge** sections linking each chapter to the next. Part V offers the complementary philosophy for fluids and hyperbolic conservation laws; both discretizations approximate the PDEs defined here.

## Where we left the wire

Part III wrote the weak forms — virtual work for elasticity, the heat equation in \(H^1\), energy functionals with unique minimizers — and identified the Sobolev regularity FEM solutions possess. The copper wire is now ready for a **mesh**: tetrahedra or hexahedra along its length, shape functions on each element, quadrature rules that assemble local stiffness into a global \(\mathbf{K}\).

At this scale the wire is a solid specimen in a tensile test: displacement unknowns at nodes, boundary conditions at the grips, perhaps a refined region near a stress concentrator. Part IV is the engineer's answer to Part III's mathematics — how weighted residuals become Galerkin assembly, how convergence rates connect discrete matrices to the infinite-dimensional operators of Part II, and why the stiffness matrix is not magic but a best approximation in energy norm.

## The concept map

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Trial space \(V_h\), shape functions, assembled \(\mathbf{K}\) and \(\mathbf{f}\) |
| What **structure** does it add? | Galerkin orthogonality, isoparametric maps, \(h\)-refinement |
| What **theorem** becomes possible? | Best approximation, Céa lemma, a priori convergence rates |
| What **breaks** if structure is missing? | Locking, hourglass modes, pollution on distorted elements |

```mermaid
flowchart LR
  WR[Weighted residuals] --> G[Galerkin]
  G --> A[Assembly]
  A --> EL[Elements / quadrature]
  EL --> P[Poisson to elasticity]
  P --> C[Convergence theory]
```

**Baby picture:** choose trial and test spaces, enforce the weak form by making residuals orthogonal to the test space, assemble element by element, then prove the discrete solution tracks the continuous one as \(h \to 0\). The copper wire in tension is a bar whose stiffness matrix is not magic — it is a Galerkin projection.

## Representative schematics (FEA notes)

The [Finite Element Analysis notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html) index the same discretization pipeline this part implements:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Weighted residuals; Galerkin orthogonality | [IV.1](01-weighted-residuals.md) |
| 2 | Local-to-global assembly; scatter into \(\mathbf{K}\) | [IV.2](02-galerkin-assembly.md) |
| 3 | Shape functions, isoparametric maps, quadrature | [IV.3](03-elements-quadrature.md) |
| 4 | Poisson → vector elasticity on the wire | [IV.4](04-poisson-to-elasticity.md) |
| 5 | Convergence rates; Céa lemma; two exit doors | [IV.5](05-convergence.md) |

Each schematic is a baby picture of the same claim Part II proved in \(H^1\): FEM is projection, not guesswork.

## Story so far (Parts I–III)

If you have read linearly since the prologue, the same specimen has changed language three times without changing material:

| Part | What we learned | What the wire became |
|------|-----------------|----------------------|
| I | \(\mathbf{K}\mathbf{u}=\mathbf{f}\), eigenmodes, \(N\to\infty\) | A chain of coupled springs; a vibration problem |
| II | \(H^1\), Lax–Milgram, Galerkin as projection | Axial displacement \(u(x)\) and temperature \(T(x)\) in function spaces |
| III | Strong vs. weak form, Sobolev regularity, energy methods | Poisson/heat/elasticity PDEs ready for a mesh |

Part III ended with a promise: the weak form of equilibrium is a **minimum principle** (or saddle point for mixed problems), and the minimizer lives in \(H^1\). Part IV is where that promise becomes code — shape functions on elements, quadrature at Gauss points, scatter into a global stiffness matrix. The copper wire that was a spring network in Part I and a field in Part II is now a **meshed solid** whose node values are the discrete shadow of the continuous solution. Convergence as \(h\to 0\) is the story Part II told in function spaces, made numerical in Chapter 5.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** from the opening table reappear here with assembly vocabulary — and how the **same mathematical moves** from Part I return on every mesh:

| Part I (springs on the wire) | Part IV (FEM on the wire) |
|------------------------------|---------------------------|
| Local spring stiffness → global \(\mathbf{K}\) | Element matrices → scatter into global \(\mathbf{K}\) |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) at equilibrium | Galerkin orthogonality: residual \(\perp V_h\) |
| Bar elements along the wire axis | Shape functions \(N_i(x)\) on tetrahedra or hexes |
| Eigenmodes for vibration | Modal analysis on the same assembled \(\mathbf{K}\) |
| \(N\) degrees of freedom | \(h\)-refinement sends element size \(\to 0\) |

Part I assembled \(\mathbf{K}\) from bar elements without naming the continuous limit; Part IV proves that assembly is **Galerkin projection** of the bilinear form Part III wrote — Céa's lemma is the finite-dimensional energy principle made rigorous. The copper wire that began as a chain of coupled springs is now a meshed solid, but the solver still calls the same sparse linear algebra from Part I. Part V will ask whether flux balance on cells is a better dialect for the air cooling this wire; Part VI will name the stress tensor hidden inside \(\mathbf{K}\).

## Bridge

Part III ended with energy methods and the promise of assembly. The first chapter below introduces weighted residuals — the unifying idea behind Galerkin's method — and shows why choosing test functions as trial functions is the natural discretization of the weak form the copper wire's equilibrium demands.
