# Part IV — The Finite Element Method

Parts I–III built the pipeline: linear algebra for discrete systems, functional analysis for function spaces, weak forms for well-posed boundary value problems. Part IV is where that pipeline becomes **code**.

The finite element method is not a bag of tricks for meshing complicated geometries — though it is that too. It is the **Galerkin projection** of a differential operator onto a finite-dimensional subspace of shape functions. Every stiffness matrix is a bilinear form evaluated on a mesh; every load vector is a linear functional; every convergence proof asks whether \(V_h\) approximates \(H^1\) as \(h \to 0\).

The copper wire returns as a chain of bar elements, then as a solid with tetrahedra, then as an elasticity problem whose energy functional Part III wrote and Part IV discretizes. The layout follows [`writings/fem/`](../../writings/fem/). Read the five chapters in order; Chapter 05 hands off to Part V, where a different discretization philosophy — conservation on cells rather than trial functions — takes over for fluids.
