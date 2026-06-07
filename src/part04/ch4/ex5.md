## 4.5 Implementation: from local to global

### Algorithm sketch

1. **Mesh:** nodes $\{\mathbf{x}_I\}$, elements $\{\Omega_e\}$, connectivity
2. **Loop elements:** compute $K^e$, $\mathbf{F}^e$ via quadrature
3. **Assemble:** scatter into global $K$, $\mathbf{F}$
4. **Apply BCs:** modify rows/columns or eliminate Dirichlet DOFs
5. **Solve:** $K\mathbf{U} = \mathbf{F}$
6. **Postprocess:** strains, stresses, fluxes from $\mathbf{U}$

### 2D Poisson workflow (teaching example)

Problem sessions walk through global assembly for P1 triangles on a 2D domain: loop elements, compute $3\times3$ element stiffness, map local DOFs to global indices, accumulate. The same pattern scales to millions of elements with sparse matrix formats.

### Software ecosystem

Modern stacks (FEniCS, Firedrake, deal.II, MFEM) automate variational forms: you write $a(u,v)$ and $\ell(v)$ in UFL-like syntax; the framework generates assembly code. Understanding local-to-global remains essential for debugging boundary conditions and singularities.

### Time-dependent and nonlinear extensions

- **Transient:** $M\dot{\mathbf{U}} + K\mathbf{U} = \mathbf{F}(t)$ at each time step
- **Nonlinear:** Newton loop $K_{\text{tangent}} \Delta\mathbf{U} = -\mathbf{R}$ with updated $K$ from current $\mathbf{U}$

### Closing Part IV

FEM is Galerkin on $H^1$ (or mixed) spaces. The copper wire's elastic stretch is computed here. When the wire yields, the constitutive law changes—Part VI—or we descend to dislocation and atomistic models in Parts VII–IX.

Next: **finite volumes**, the natural discretization when **conservation** and **fluxes** dominate, as in compressible flow and shock physics.
