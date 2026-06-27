# Part IV — The Finite Element Method

Part III reduced continuum mechanics to weak forms: bilinear forms on Sobolev spaces, loads as dual functionals, energy functionals with unique minimizers. Part IV asks the engineer's question: *how do we compute those solutions on a mesh?*

The finite element method is the answer for elliptic and parabolic problems on complex geometries — the copper wire in tension, a bracket with a reentrant corner, a heated solid coupled to a fluid boundary. We begin with **weighted residuals**, the family of methods that includes Galerkin's method as its most important member, then build element-by-element assembly, quadrature, and convergence theory that connects discrete stiffness matrices to the infinite-dimensional operators of Part II.

The layout follows the **FEM Notes** in [`writings/fem/`](../../writings/fem/): five numbered chapters from residuals through error estimates, with **Bridge** sections linking each chapter to the next. Part V offers the complementary philosophy for fluids and hyperbolic conservation laws; both discretizations approximate the PDEs defined here.

## The concept map (FEA notes)

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | A discrete field \(u_h \in V_h \subset H^1\) on a mesh |
| What **structure** does it add? | Weighted residuals; Galerkin orthogonality; element assembly |
| What **theorem** becomes possible? | Céa's lemma; best approximation; a priori convergence in \(H^1\) |
| What **breaks** if structure is missing? | Locking; spurious modes; inconsistent quadrature |

```mermaid
flowchart LR
  Weak[Weak form from Part III] --> WR[Weighted residuals]
  WR --> Gal[Galerkin method]
  Gal --> Asm[Element assembly K u = f]
  Asm --> Conv[Convergence h → 0]
  Conv --> Elast[Poisson → elasticity]
```

**Baby picture:** choose trial and test spaces on a mesh, assemble local stiffness into a global system, and trust that \(\mathbf{K}\) is the Galerkin projection of the operator Part II defined — not an arbitrary sparse matrix.

## Bridge

Part III ended with energy methods and the promise of assembly. The first chapter below introduces weighted residuals — the unifying idea behind Galerkin's method — and shows why choosing test functions as trial functions is the natural discretization of the weak form the copper wire's equilibrium demands.
