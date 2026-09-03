# Normed Spaces and Completeness

When the copper wire heats under current, we may ask how far its temperature field \(T(x)\) deviates from a uniform reference, or how large its spatial gradients are near a clamp. These are questions about **size** — not of a single number, but of an entire function. Normed spaces make that notion precise. They generalize the length of a vector in \(\mathbb{R}^N\) to settings where the "components" are infinitely many values indexed by points in a domain. Completeness — the property that Cauchy sequences converge within the space — is what allows mesh refinement arguments to conclude that discrete solutions approach a genuine weak solution rather than escaping into a larger, physically meaningless class.

We begin with metric spaces, because convergence is fundamentally about distance. Norms are the most important way mechanics assigns distance, but not the only one.


## Plot spine (one line) {#plot-spine-one-line}

> **II.2 — Act I — Grammar:** Energy norms need a complete room — Cauchy sequences must converge before we trust the limit solution.

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter.

## Scene: how wrong is "wrong enough"?

Two temperature fields along the heated wire can disagree by at most 0.1 K everywhere, or agree on average yet differ by 5 K at the clamp. Those are different notions of "close" — sup norm versus \(L^2\). When the engineer asks whether the thermal FEM is converged, the answer depends on which ruler we use. Normed spaces name those rulers and let mesh-refinement arguments conclude in the norm the physics actually cares about.

## Metric spaces: convergence before length

A **metric space** \((X,d)\) is a set \(X\) equipped with a distance function \(d: X \times X \to \mathbb{R}_{\ge 0}\) satisfying, for all \(x,y,z \in X\):

1. \(d(x,y) = 0\) if and only if \(x = y\)
2. \(d(x,y) = d(y,x)\)
3. \(d(x,z) \le d(x,y) + d(y,z)\) (triangle inequality)

A sequence \(\{x_n\} \subset X\) **converges** to \(x \in X\) if \(d(x_n, x) \to 0\) as \(n \to \infty\). The metric topology — open balls, continuity, density — is built from this notion alone.

**Example (function space with sup metric).** On \(C([0,L])\), the continuous functions on \([0,L]\), define

\[
d_\infty(u,v) = \max_{x \in [0,L]} |u(x) - v(x)| = \|u - v\|_{L^\infty}.
\]

Two temperature fields are close in this metric if they differ by at most \(\varepsilon\) **everywhere** along the wire. This is the natural metric for uniform convergence and for bounding maximum stress.

**Example (discrete mesh functions).** On a fixed mesh with nodes \(x_i\), \(d(\mathbf{u}, \mathbf{v}) = \max_i |u_i - v_i|\) recovers the \(\ell^\infty\) norm on \(\mathbb{R}^N\). Refining the mesh changes \(N\) and the metric itself — one reason the limit \(h \to 0\) must be treated in a function space, not as a sequence of ever-larger vector spaces with incompatible metrics.

A metric space is **complete** if every Cauchy sequence converges in \(X\). Completeness depends on both the set and the metric: the same set of functions can be complete in one metric and incomplete in another.

## Norms and normed spaces

A **norm** on a vector space \(V\) is a map \(\|\cdot\|: V \to \mathbb{R}_{\ge 0}\) such that for all \(u,v \in V\) and \(\alpha \in \mathbb{R}\):

1. \(\|v\| = 0\) if and only if \(v = 0\)
2. \(\|\alpha v\| = |\alpha|\,\|v\|\)
3. \(\|v + w\| \le \|v\| + \|w\|\) (triangle inequality)

A **normed space** \((V, \|\cdot\|)\) is a vector space with a norm. Every norm induces a metric \(d(u,v) = \|u - v\|\), hence a notion of convergence compatible with vector space operations.

Norms are not unique on the same space, and the choice encodes physical priority. Mean-square error weights all points equally in an \(L^2\) sense; energy norms emphasize gradients; \(L^\infty\) captures worst-case values. A convergence proof in one norm may fail in another — and in mechanics, knowing which norm certifies the quantity we care about is part of the modeling contract.

## The \(L^p\) spaces

Let \(\Omega \subset \mathbb{R}^d\) be a bounded domain with Lebesgue measure. For \(1 \le p < \infty\), define

\[
\|u\|_{L^p} = \left(\int_\Omega |u|^p \, d\Omega\right)^{1/p}.
\]

Functions with finite \(L^p\) norm (modulo equality almost everywhere) form the Banach space \(L^p(\Omega)\). The case \(p = 2\) is the default for energy, least squares, and statistical variance: the mean-square deviation of the wire's temperature from a target profile is an \(L^2\) quantity.

For \(p = \infty\),

\[
\|u\|_{L^\infty} = \text{ess sup}_{x \in \Omega} |u(x)|,
\]

the essential supremum — the smallest uniform bound holding almost everywhere. Hot spots in a thermal field are controlled by \(L^\infty\); average behavior is controlled by \(L^2\).

**Hölder's inequality** links the \(L^p\) norms. If \(1/p + 1/q = 1\),

\[
\int_\Omega |uv| \, d\Omega \le \|u\|_{L^p} \|v\|_{L^q}.
\]

For \(p = q = 2\), this is the Cauchy–Schwarz inequality, the workhorse of energy estimates.

**Example.** On \(\Omega = (0,1)\), the function \(u(x) = x^{-1/4}\) lies in \(L^p\) for \(p < 4\) but not in \(L^4\) or \(L^\infty\), because it blows up at zero too sharply. Singularities in mechanics — stress at a crack tip, pressure gradient at a reentrant corner — are diagnosed by membership or non-membership in particular \(L^p\) and Sobolev spaces.

## The Sobolev space \(H^1\): a preview

Square-integrable functions need not be differentiable in the classical sense. Yet Poisson's equation asks for a gradient. The resolution is **weak derivatives**, defined through integration by parts against smooth test functions. The Sobolev space \(H^1(\Omega)\) collects functions \(u \in L^2(\Omega)\) whose weak partial derivatives \(\partial u / \partial x_i\) also lie in \(L^2(\Omega)\), with norm

\[
\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2.
\]

Functions in \(H^1\) may have kinks; their weak derivatives are themselves functions in \(L^2\), not delta distributions at the kink. This is exactly the regularity of conforming finite element solutions: piecewise polynomials with continuous inter-element jumps in classical derivative, but well-defined weak gradients.

For the copper wire in transverse displacement, \(u \in H^1(0,L)\) means the deflection is square-integrable and the slope (weak derivative) is square-integrable — a sensible minimum for elastic energy \(\int |u'|^2\).

The subspace \(H^1_0(\Omega)\) consists of \(H^1\) functions vanishing on \(\partial\Omega\) in trace sense. Homogeneous Dirichlet boundary conditions — fixed ends of the wire — live here. Part III develops Sobolev theory in full; for now, \(H^1\) is the energy space where elliptic weak forms are posed.

## Cauchy sequences and Banach spaces

A sequence \(\{u_n\}\) in a normed space \(V\) is **Cauchy** if

\[
\|u_n - u_m\| \to 0 \quad \text{as } n, m \to \infty.
\]

Every convergent sequence is Cauchy; the converse need not hold. In \(\mathbb{R}^N\) with any norm, every Cauchy sequence converges — finite-dimensional normed spaces are complete. In infinite dimensions, completeness is a nontrivial property of the space.

A normed space is **complete** if every Cauchy sequence converges in the space. A complete normed space is a **Banach space**.

**Example (incompleteness).** Let \(C^\infty([0,1])\) carry the \(L^2\) norm. The sequence of functions that vanish near \(x = 0\) and approach a step function is Cauchy in \(L^2\) but converges in \(L^2\) to a discontinuous function not in \(C^\infty\). Smooth functions with the \(L^2\) metric form an incomplete space. Completion yields all of \(L^2([0,1])\).

**Example (completeness).** \(L^2(\Omega)\) and \(H^1(\Omega)\) are Banach spaces — indeed Hilbert spaces, as the next chapter shows. These are the spaces where we prove that Galerkin sequences have limits that are themselves valid weak solutions.

## Why completeness matters for FEM

Galerkin approximation produces a sequence \(u_h\) indexed by mesh size \(h\). A typical convergence proof establishes that \(\{u_h\}\) is Cauchy in an energy norm \(\|\cdot\|_a\) defined by the bilinear form. If the underlying space is complete, the limit \(u\) belongs to the admissible class — say, \(H^1_0(\Omega)\) — and satisfies the weak form. Without completeness, the limit might exist only in a larger space where the variational statement no longer makes physical sense.

Consider linear elasticity on the copper wire with fixed ends. As the mesh refines, the discrete displacement fields \(u_h\) approach a limit displacement. Completeness of \(H^1\) guarantees that limit is a function with square-integrable weak strain, not merely a formal object. The finite element solution is not an ad hoc vector; it is an approximation to an element of a complete function space.

## Equivalent norms and hidden constants

On a finite-dimensional vector space, all norms are **equivalent**: for any two norms \(\|\cdot\|_a\) and \(\|\cdot\|_b\), there exist constants \(c, C > 0\) such that

\[
c \|v\|_b \le \|v\|_a \le C \|v\|_b \quad \forall v.
\]

In infinite dimensions, equivalence fails between natural norms. On bounded domains, \(H^1(\Omega)\) embeds continuously in \(L^2(\Omega)\): there exists \(C\) such that \(\|u\|_{L^2} \le C \|u\|_{H^1}\). The reverse is false: oscillatory functions can have small \(L^2\) norm while gradients blow up.

This asymmetry is why **coercivity** in the \(H^1\) energy norm controls errors measured in \(L^2\). The bilinear form \(a(u,v) = \int \nabla u \cdot \nabla v\) is coercive on \(H^1_0(\Omega)\) not by magic, but because of **Poincaré's inequality**.

## Poincaré's inequality (preview)

For a bounded domain \(\Omega\) and \(u \in H^1_0(\Omega)\),

\[
\|u\|_{L^2} \le C_P \|\nabla u\|_{L^2},
\]

where \(C_P\) depends on the domain geometry. On a long thin wire — large aspect ratio — \(C_P\) can be large, worsening the conditioning of stiffness matrices even when the physics is benign.

Poincaré's inequality makes the energy seminorm \(\|\nabla u\|_{L^2}\) equivalent to the full \(H^1\) norm on \(H^1_0\). Coercivity of the Laplacian bilinear form follows immediately. The constant \(C_P\) enters error bounds and appears in practice as ill-conditioning of nearly inextensible modes — a numerical echo of a functional-analytic fact.

## Density and approximation

Many spaces are defined abstractly but computed through approximations. **Density theorems** state that smooth functions are dense in Sobolev spaces: given \(u \in H^1(\Omega)\) and \(\varepsilon > 0\), there exists smooth \(u_\varepsilon\) with \(\|u - u_\varepsilon\|_{H^1} < \varepsilon\). Finite element spaces are not smooth, but piecewise polynomial approximations inherit the same logic: the mesh solution approximates the continuum solution because the continuum object is itself a limit of simpler functions.

For the vibrating wire, normal modes are \(H^1\) functions even when classical second derivatives fail at kinks introduced by damage. Completeness and density together justify replacing the infinite-dimensional eigenproblem with a matrix eigenvalue problem on \(V_h\) and expecting convergence as \(h \to 0\).

## Summary of the spaces we carry forward

| Space | Norm | Role in mechanics |
|-------|------|-------------------|
| \(L^2(\Omega)\) | \(\|u\|_{L^2}^2 = \int |u|^2\) | Energy of fields, mean-square error |
| \(L^\infty(\Omega)\) | ess sup \(\|u\|\) | Worst-case stress, uniform bounds |
| \(H^1(\Omega)\) | \(\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2\) | Weak derivatives, FEM trial spaces |
| \(H^1_0(\Omega)\) | Same as \(H^1\) | Homogeneous Dirichlet BCs |

Each is complete in its norm. Each is the setting for a class of convergence theorems we will use without apology in Parts III and IV.

## Sequence spaces and the mesh limit

The space \(\ell^2\) of square-summable sequences \(\{a_n\}\) with norm \(\|\{a_n\}\|_{\ell^2} = (\sum_n |a_n|^2)^{1/2}\) is a Hilbert space modeling countable degrees of freedom without a spatial domain. It appears when expanding in orthonormal bases: Parseval's identity maps \(L^2(\Omega)\) isometrically to coefficient sequences in \(\ell^2\).

A finite element mesh with \(N\) nodes produces vectors in \(\mathbb{R}^N\), not \(\ell^2\), but the **limit as \(N \to \infty\)** is naturally expressed in \(L^2\) or \(H^1\). The sequence of mesh-indexed approximations \(u_h\) is Cauchy in energy norm when the bilinear form is coercive and the approximation family is stable; completeness identifies the limit with the weak solution. Thinking of "infinite DOFs" as \(\ell^2\) coefficients in an orthonormal basis is sometimes cleaner than imagining a continuum of point values — both pictures describe the same Hilbert space geometry.

## Lipschitz continuity and extension

A map \(F: (X,d_X) \to (Y,d_Y)\) is **Lipschitz** if

\[
d_Y(F(x_1), F(x_2)) \le L\, d_X(x_1, x_2)
\]

for some constant \(L\). Lipschitz maps preserve Cauchy sequences and therefore convergence. Nonlinear constitutive maps in mechanics — hyperelastic strain energy, plastic yield functions — are often Lipschitz on bounded sets of strains, which supports stability of Newton iterations in nonlinear FEM.

**Extension operators** map functions from a subspace — say, values on a boundary — into the bulk domain while controlling norm growth. Extension theorems for \(H^1\) guarantee that boundary data can be lifted to bulk functions without exploding the \(H^1\) norm. That lifting is what makes non-homogeneous Dirichlet conditions compatible with variational formulations on \(H^1\) rather than only on \(H^1_0\).

## Banach's fixed-point theorem (preview)

On a complete metric space, a **contraction** — a map \(T\) with \(d(Tx, Ty) \le q\, d(x,y)\) for some \(q < 1\) — has a unique fixed point, obtained as the limit of iterates \(x_{n+1} = T x_n\). Banach's fixed-point theorem on Banach spaces underlies Picard iteration for ODEs and some nonlinear PDE proofs.

In computational mechanics, fixed-point iterations appear in staggered coupling schemes — fluid–structure interaction, contact with friction — where each substep is a well-posed elliptic solve. Completeness of the underlying space ensures the coupled iteration converges when the contraction constant is small enough. The theorem is a completeness result in disguise: Cauchy iterates converge because the space has no holes.

## More examples from mechanics

**Sobolev norms on vector fields.** For displacement \(\mathbf{u}: \Omega \to \mathbb{R}^d\),

\[
\|\mathbf{u}\|_{H^1}^2 = \sum_{i=1}^d \|u_i\|_{H^1}^2.
\]

Linear elasticity energy \(\int \varepsilon(\mathbf{u}) : C : \varepsilon(\mathbf{u})\) is bounded above and below by multiples of \(\|\mathbf{u}\|_{H^1}^2\) when \(C\) is positive definite — Korn's inequality replaces Poincaré for vector fields and is essential for coercivity in elasticity.

**Energy norm for variable conductivity.** Steady heat conduction with conductivity \(k(x)\) uses

\[
\|T\|_a^2 = \int_\Omega k(x) |\nabla T|^2 \, d\Omega.
\]

When \(k\) is bounded above and below by positive constants, \(\|\cdot\|_a\) is equivalent to \(\|\nabla T\|_{L^2}\) on \(H^1_0\), hence to \(\|T\|_{H^1}\). Variable coefficients change constants in equivalence inequalities but not the Banach space framework.

**Maximum principle and \(L^\infty\).** Elliptic maximum principles bound \(\|u\|_{L^\infty}\) by boundary data and source terms for classical solutions. Weak solutions in \(H^1\) do not automatically lie in \(L^\infty\) in high dimension — another instance where the chosen norm encodes what we can guarantee. For the wire in one space dimension, \(H^1(0,L) \hookrightarrow L^\infty(0,L)\), so pointwise values along the specimen are well-defined without extra regularity.

## Lab act: compare energy norms on a hat function (Act III prelude)

**Act III** in the lab will ramp grip displacement and record force on the load cell. Before that ramp, Part II must answer a quieter question: *when two meshes disagree slightly, which norm tells us they disagree?* The answer is not "maximum nodal difference" alone — it is the **energy norm** tied to the bilinear form the wire obeys.

Take the 1D bar from [I.1](../part01-linear-algebra/01-vectors-matrices.md) with \(L = 1\,\text{m}\), fixed left end, and a **hat function** trial displacement on a uniform mesh with spacing \(h\):

\[
u_h(x) = \begin{cases} x/h & 0 \le x \le h \\ 1 & h \le x \le L \end{cases}
\]

(Dirichlet \(u(0)=0\), \(u(L)=1\) enforced at nodes; the kink at \(x=h\) is the whole point.)

| Quantity | Formula on one element | What it measures |
|----------|------------------------|------------------|
| \(\|u_h\|_{L^2}^2\) | \(\int_0^L u_h^2 \, dx\) | Mean-square displacement — smooth-looking error |
| \(\|u_h\|_{H^1}^2\) | \(\int_0^L (u_h')^2 \, dx + \|u_h\|_{L^2}^2\) | Strain energy plus \(L^2\) content |
| \(\|u_h'\|_{L^2}^2\) | Spike \(\sim 1/h\) at the kink | **Dominates** as \(h \to 0\) — the norm sees the corner |

Compute \(\|u_h'\|_{L^2}^2 \approx 1/h\) from the slope jump: one element carries gradient \(1/h\), width \(h\), so the integral of \((u')^2\) is \(\mathcal{O}(1/h)\). Refining the mesh **without** smoothing the kink does not drive the energy norm to zero — completeness in \(H^1\) guarantees a limit exists, but a sequence of kinky hats is not Cauchy in the **energy** norm unless the kink moves toward a smooth target.

In Python or a spreadsheet, plot \(\|u_h\|_{L^2}\) and \(\|u_h'\|_{L^2}\) versus \(h\) for three mesh sizes (\(h = 0.25, 0.1, 0.05\,\text{m}\)). The \(L^2\) norm changes slowly; the \(H^1\) seminorm blows up as the kink sharpens. That is the numerical face of "classical \(C^2\) smoothness fails at corners" from [II.1](01-motivation.md) — and the reason Act III's linear elastic climb is trustworthy only after weak forms (Part III) replace pointwise derivatives with norms that measure strain, not just nodal values.

When the operator later reads a converged FEM log reporting "energy error," this table is what the code is counting.

## Concept map checkpoint (normed spaces)

Norms are the rulers that make convergence honest. Before Hilbert geometry adds angles, summarize:

| Question | Normed-space answer (copper wire) |
|----------|-----------------------------------|
| What **object**? | Functions measured by \(L^2\), \(H^1\), or energy norm \(\|\cdot\|_a\) |
| What **structure**? | Complete metric spaces (Banach); equivalent norms |
| What **theorem**? | Cauchy sequences converge inside the space; Banach fixed point for coupled iterations |
| What **breaks**? | Judging error by nodal max alone; kinks invisible to \(L^2\) but loud in \(H^1\) |

The hat-function Lab act is the numerical face of "corners break classical smoothness": \(\|u_h'\|_{L^2}\) spikes at a kink even when nodal values look reasonable.

## Bridge

Norms measure size; inner products measure angle and projection. When the norm comes from an inner product via \(\|u\| = \sqrt{(u,u)}\), geometry enters: orthogonality, best approximation, Riesz representation. **Hilbert spaces** — complete inner-product spaces — are where Galerkin orthogonality and energy minimization become rigorous.

| What this chapter gave (norms) | What the next chapter adds (Hilbert geometry) |
|--------------------------------|-----------------------------------------------|
| \(\|u\|_{H^1}\) measures strain energy on the wire | Inner product \((u,v)_{H^1}\) defines orthogonality of modes |
| Equivalent norms: same convergence, different constants | Riesz representation: every linear functional is an inner product |
| Banach completeness: limits stay inside the space | Best approximation: FEM error is projection error in energy norm |
| \(L^2\) for temperature; energy norm for displacement | Céa's lemma preview: discrete solution is optimal in \(V_h\) |

**Scale-boundary handshake (II.1 → II.2 → II.3).**

| Motivation export ([II.1](01-motivation.md)) | Normed-space output (this chapter) | Hilbert consumer ([II.3](03-hilbert-spaces.md)) | Failure mode |
|---------------------------------------------|------------------------------------|-------------------------------------------------|--------------|
| Limit field \(u(x)\in H^1\), not \(\mathbf{u}\in\mathbb{R}^N\) | Energy norm \(\|u\|_{H^1}\) measures strain, not nodal max | Inner product \((u,v)\) adds angles for orthogonality | Judging mesh quality by \(L^2\) alone at kinks |
| Well-posedness contract: existence, stability, convergence | Banach completeness: Cauchy sequences stay inside | Riesz representation of loads as inner products | Discrete solutions converging outside admissible class |
| Bar refinement Lab act (\(N=5,20,100\)) | Hat-function spike in \(\|u_h'\|_{L^2}\) at corners | Galerkin best approximation in energy norm | "More nodes look smoother" without energy-norm audit |
| Equivalent norms on the same space | Same convergence story, different constants | Céa's lemma preview: discrete solution is optimal in \(V_h\) | Mixing norm choices when comparing error reports |

The hat-function Lab act is the numerical face of this handshake: \(\|u_h'\|_{L^2}\) spikes at a kink even when nodal values look reasonable — the same diagnostic Act III's load cell will inherit when the grip corner is under-resolved. Part III writes weak PDEs in the normed spaces defined here; Part IV assembles \(\mathbf{K}\) as projection onto \(V_h\) — but only after [II.3](03-hilbert-spaces.md) adds the inner-product geometry that makes "Galerkin is projection" a theorem.

Part I diagonalized \(\mathbf{K}\) by finding orthogonal eigenvectors in \(\mathbb{R}^N\). The copper wire's vibration modes in the limit are the same idea — but orthogonality is now \((u_i, u_j) = 0\) in \(H^1\), not \(\mathbf{u}_i^T \mathbf{u}_j = 0\). The next chapter develops that geometry and connects it directly to the finite element method through best approximation and Céa's lemma. Turn the page when you are ready to see why "Galerkin is projection" is a theorem, not a slogan.
