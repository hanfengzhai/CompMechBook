# The variational road to finite elements

Finite element analysis is not a bag of tricks for meshing triangles. It is a **method of projecting infinite-dimensional problems onto finite subspaces** so that:

1. The projected problem is uniquely solvable (Lax–Milgram).
2. The projection error is controlled (Céa's lemma + approximation theory).
3. The discrete system is sparse and structured for fast linear algebra.

Every FEM code, from academic teaching scripts to industrial solvers, repeats the same pipeline:

```
Weak form  →  choose V_h  →  assemble K  →  solve K u = f  →  postprocess
```

The author's FEA teaching notes (ME335A) and personal *Finite Element Analysis* notes emphasize this pipeline explicitly: weighted residuals, Galerkin orthogonality, shape functions, local-to-global maps, and the mathematical theory tying them together.

We now walk that pipeline with the rigor of Part II and the physics of Part III.
