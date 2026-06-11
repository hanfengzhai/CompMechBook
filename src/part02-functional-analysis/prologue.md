# From finite to infinite dimensions

In Part I, unknowns were vectors \(\mathbf{u} \in \mathbb{R}^n\). In continuum mechanics the unknown is a **field**—for example, displacement \(u : \Omega \to \mathbb{R}\) on a domain \(\Omega \subset \mathbb{R}^d\).

How many degrees of freedom does \(u\) have? Infinitely many: one value per point. Yet we still add functions, scale them, and apply linear operators such as

\[
(Lu)(x) = -\frac{d}{dx}\left(k(x)\frac{du}{dx}\right).
\]

Functional analysis is the linear algebra of **infinite-dimensional vector spaces**, equipped with notions of distance and convergence that make analysis rigorous.

## The central question of discretization

FEM does not approximate \(u\) at every point. It chooses a finite-dimensional subspace \(V_h \subset V\) and seeks \(u_h \in V_h\) such that

\[
a(u_h, v_h) = \langle f, v_h \rangle \quad \forall v_h \in V_h,
\]

where \(a(\cdot,\cdot)\) is a bilinear form and \(\langle f, \cdot \rangle\) a linear functional. Every symbol in that sentence lives in functional analysis:

- \(V\) is a function space (often a Sobolev space).
- \(a\) is a bilinear form induced by a differential operator.
- Convergence \(u_h \to u\) is a statement about **norms** and **completeness**.

## Road map (Functional Analysis Notes style)

Following the structure of classical functional analysis notes (metric spaces → normed spaces → operators → functionals), we will:

1. Define **distance** and **convergence** (metric spaces).
2. Add **vector space structure** and **norms** (Banach spaces).
3. Add **inner products** (Hilbert spaces—where FEM variational forms live most naturally).
4. Study **bounded linear operators** and **dual spaces**.
5. Introduce **weak derivatives** and **Sobolev spaces**—the native habitat of weak formulations.

> **Story beat.** The engineer asks: "Is my mesh fine enough?" The analyst asks: "Does \(u_h\) converge to \(u\) in \(H^1\) as \(h \to 0\)?" Functional analysis is what makes the second question precise—and sometimes answerable.
