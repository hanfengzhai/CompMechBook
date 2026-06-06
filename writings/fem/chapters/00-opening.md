# Part IV — The Finite Element Method

Part III showed that elliptic boundary value problems — Poisson, linear elasticity, steady heat — admit weak formulations in \(H^1\). Part IV asks the engineer's question: *how do we solve those weak forms on a computer?*

The finite element method answers with a concrete pipeline: choose a mesh, select local shape functions, assemble element stiffness and load contributions into a global sparse system, apply boundary conditions, and solve. The method of weighted residuals and Galerkin's principle explain **why** this pipeline is the natural discretization of the weak form, not an ad hoc trick. The copper wire becomes a mesh of bar elements or tetrahedra; its displacement and temperature are coefficients on piecewise polynomials.

The layout follows the **FEM Notes** in [`writings/fem/`](../../writings/fem/): numbered chapters aligned with the author's FEA teaching materials, assembly examples, and **Bridge** sections toward convergence theory and continuum mechanics. Read the five chapters in order; Chapter 5 connects error estimates in \(H^1\) to mesh refinement practice.
