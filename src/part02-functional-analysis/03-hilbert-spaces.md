# Inner Products and Hilbert Spaces

Where a norm tells us how large an object is, an inner product tells us how two objects align. On \(\mathbb{R}^3\), the dot product measures the angle between force and displacement vectors and determines whether work is done. On function spaces, the same idea governs orthogonality of vibration modes, projection onto finite element subspaces, and the conversion of loads into data the weak form can consume. **Hilbert spaces** — complete inner-product spaces — are the stage on which elliptic mechanics becomes geometry.

Pull the copper wire again and consider two displacement fields \(u\) and \(v\) along its length. If one mode of vibration is even and another odd about the midpoint, their product integrated over the domain averages to zero: they are **orthogonal** in the \(L^2\) inner product. Decoupling of normal modes in linear vibration analysis is not a numerical convenience; it is a theorem about orthogonality of eigenfunctions in a Hilbert space.


## Plot spine (one line) {#plot-spine-one-line}

> **II.3 — Act I — Grammar:** Inner products make orthogonality precise; modal decoupling from Part I survives the passage to \(H^1\).

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter.

## Scene: modes that ignore each other

Clamp the wire and strike it softly: the fundamental bend and the second bend do not exchange energy arbitrarily — their displacements integrate to orthogonal patterns over the length. That decoupling is Hilbert geometry: an inner product turns mode orthogonality into a theorem, and Galerkin projection into best approximation in energy. The wire's vibration spectrum is a Hilbert-space story told before any tetrahedral mesh exists.

**Contract handoff (II.2 → II.3 → III.2).** [II.2](02-normed-spaces.md) gave the wire's displacement a norm and proved Cauchy sequences stay in \(H^1\); inner products below add angles so "orthogonal modes" and "best approximation on a mesh" become theorems rather than finite-difference folklore. Riesz representation is the hinge: a grip load, a thermocouple constraint, and a distributed body force all become continuous functionals \(\ell(v)\) on the same Hilbert space where \(u\) lives — which is exactly what [III.2](../part03-pdes/02-weak-form.md) will pair against test functions in the weak form. When Galerkin error is discussed in Part IV, Céa's lemma will cite the projection geometry defined here; if modes from [I.3](../part01-linear-algebra/03-eigenvalues.md) decouple on the spring mesh but look coupled on a coarse FEM mesh, the fix is subspace choice in \(V_h\), not a new physical model.

## Definition

An **inner product** on a real vector space \(V\) is a map \((\cdot,\cdot): V \times V \to \mathbb{R}\) such that for all \(u,v,w \in V\) and \(\alpha \in \mathbb{R}\):

1. \((u,u) \ge 0\), with equality if and only if \(u = 0\) (positive definiteness)
2. \((u,v) = (v,u)\) (symmetry)
3. \((u, \alpha v + w) = \alpha (u,v) + (u,w)\) (linearity in the second argument)

Complex spaces use conjugate-linearity in the second slot; mechanics on real domains uses real Hilbert spaces throughout.

Every inner product induces a norm

\[
\|u\| = \sqrt{(u,u)},
\]

which satisfies the Cauchy–Schwarz inequality

\[
|(u,v)| \le \|u\|\,\|v\|
\]

and the parallelogram law

\[
\|u+v\|^2 + \|u-v\|^2 = 2\|u\|^2 + 2\|v\|^2.
\]

A **Hilbert space** is a complete inner-product space: a complete normed space whose norm comes from an inner product. \(L^2(\Omega)\) and \(H^1(\Omega)\) are Hilbert spaces; the energy space for Dirichlet problems uses a related inner product defined below.

## \(L^2\) as the canonical Hilbert space

On a bounded domain \(\Omega\),

\[
(u,v)_{L^2} = \int_\Omega u(x)\, v(x)\, d\Omega
\]

makes \(L^2(\Omega)\) a Hilbert space. The norm \(\|u\|_{L^2} = \sqrt{(u,u)_{L^2}}\) is mean-square amplitude. For a temperature fluctuation along the wire, \(\|T\|_{L^2}^2\) is the integrated squared deviation — the quantity minimized in least-squares fitting of experimental data.

**Parseval's identity** generalizes Pythagoras to orthonormal bases. If \(\{\phi_k\}_{k=1}^\infty\) is orthonormal in \(L^2(\Omega)\) — \((\phi_j, \phi_k) = \delta_{jk}\) — then for every \(u \in L^2\),

\[
\|u\|_{L^2}^2 = \sum_{k=1}^\infty |(u,\phi_k)|^2.
\]

Fourier modes on a fixed interval are orthonormal in \(L^2\); Parseval's identity is why spectral methods decouple when the basis matches the geometry. Eigenfunctions of the Laplacian with Dirichlet conditions on the wire's domain form another orthonormal family; vibration analysis expands arbitrary initial data in that basis.

**Example.** On \((0,L)\), \(\phi_k(x) = \sqrt{2/L}\sin(k\pi x/L)\) are orthonormal eigenfunctions of \(-d^2/dx^2\) with zero boundary conditions. Any \(u \in L^2(0,L)\) admits an expansion \(u = \sum_k c_k \phi_k\) with \(c_k = (u,\phi_k)\), and \(\|u\|_{L^2}^2 = \sum_k c_k^2\).

## Best approximation in subspaces

Finite elements replace an infinite-dimensional solution by one living in a finite-dimensional subspace \(V_h \subset H\). The fundamental geometric fact is **best approximation**.

**Theorem.** Let \(H\) be a Hilbert space, \(W \subset H\) a closed subspace, and \(u \in H\). There exists a unique \(u_W \in W\) minimizing \(\|u - w\|\) over \(w \in W\). Moreover, \(u_W\) is characterized by the **orthogonality condition**

\[
(u - u_W, w) = 0 \quad \forall w \in W.
\]

The residual \(u - u_W\) is perpendicular to every direction in \(W\). In \(\mathbb{R}^N\), this is orthogonal projection onto a subspace; in \(L^2\), it is the mean-square best fit by functions in \(W\).

When the norm is the energy norm \(\|v\|_a = \sqrt{a(v,v)}\) from a coercive bilinear form, the best approximant in \(V_h\) satisfies

\[
a(u - u_h, v_h) = 0 \quad \forall v_h \in V_h.
\]

That is precisely the **Galerkin condition**. The finite element solution is not merely a convenient linear system; it is the unique best approximation in the trial space, measured in energy — provided we use the correct inner product geometry.

## Riesz representation

Weak forms pair the solution against test functions. Loads appear on the right-hand side as **linear functionals** \(\ell(v)\). On a Hilbert space, every such functional is inner product with a fixed vector.

**Theorem (Riesz representation).** Let \(H\) be a Hilbert space and \(\ell: H \to \mathbb{R}\) be continuous and linear. There exists a unique \(f \in H\) such that

\[
\ell(v) = (f, v) \quad \forall v \in H.
\]

Moreover, \(\|\ell\|_{H^*} = \|f\|_H\), where \(\|\ell\|_{H^*} = \sup_{\|v\|=1} |\ell(v)|\).

For Poisson's equation with \(f \in L^2(\Omega)\), the load functional \(\ell(v) = \int_\Omega f v \, d\Omega\) is continuous on \(H^1_0(\Omega)\). Riesz representation (with the \(H^1\) inner product, or equivalently through Lax–Milgram) identifies the weak solution as the unique element satisfying the variational equation. Body forces, thermal sources, and distributed tractions on the wire all enter through such functionals.

**Example.** A point load at the midpoint of a wire is not a function in \(L^2\), but defines a continuous functional on \(H^1_0(0,L)\) by \(\ell(v) = v(L/2)\). Riesz representation yields a **Green's function** \(G \in H^1\) with \(\ell(v) = (G,v)_{H^1}\) in the energy inner product. Point loads are therefore admissible in weak formulations even when classical strong forms require delta distributions.

## Energy inner products

For the Poisson problem \(-\Delta u = f\) with \(u = 0\) on \(\partial\Omega\), define

\[
a(u,v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega.
\]

On \(H^1_0(\Omega)\), Poincaré's inequality makes \(\|u\|_a = \sqrt{a(u,u)}\) equivalent to the \(H^1\) norm. The bilinear form is an inner product on \(H^1_0\): symmetric, positive definite, inducing the **energy norm** that measures elastic strain energy in linear elasticity analogues.

The weak solution satisfies

\[
a(u,v) = (f,v)_{L^2} \quad \forall v \in H^1_0(\Omega).
\]

Rearranging for the discrete solution \(u_h \in V_h\),

\[
a(u - u_h, v_h) = 0 \quad \forall v_h \in V_h.
\]

The error \(e = u - u_h\) is **\(a\)-orthogonal** to the test space. This is Galerkin orthogonality in its pure form. It holds exactly for the finite element solution, not approximately — a consequence of the definition of \(u_h\), not of mesh luck.

For the heated copper wire in steady state, the same structure governs conduction: temperature minimizes a Dirichlet energy, and the discrete temperature field is the best energy-norm approximation in \(V_h\).

## Céa's lemma (preview)

Best approximation alone does not quantify error; **approximation theory** on \(V_h\) must bound how well \(u\) can be approximated by mesh functions. **Céa's lemma** combines Galerkin orthogonality with approximation properties.

**Theorem (Céa's lemma).** Let \(a(\cdot,\cdot)\) be coercive and continuous on a Hilbert space \(H\), with \(u\) the solution of \(a(u,v) = \ell(v)\) for all \(v \in H\), and \(u_h \in V_h \subset H\) the Galerkin approximation. Then

\[
\|u - u_h\|_a \le \frac{M}{m} \inf_{v_h \in V_h} \|u - v_h\|_a,
\]

where \(m\) and \(M\) are the coercivity and continuity constants of \(a\).

The discrete error is bounded by a constant times the **best approximation error** in the same energy norm. Refining the mesh shrinks the right-hand side if \(V_h\) grows rich enough — for example, if piecewise linears can approximate \(u\) with \(O(h)\) energy error on smooth problems. Céa's lemma is the bridge from abstract Hilbert space geometry to concrete mesh size recommendations in Part IV.

## Orthogonality and modal decoupling

Self-adjoint elliptic operators on bounded domains possess real eigenvalues and \(L^2\)-orthogonal eigenfunctions. If \(L\phi_k = \lambda_k \phi_k\) with homogeneous boundary conditions, then \((\phi_j, \phi_k)_{L^2} = 0\) for \(j \ne k\) after appropriate normalization. Expanding initial data for the wave or heat equation in this basis decouples the dynamics mode by mode — a Hilbert-space fact with direct computational payoff in modal methods.

For a vibrating wire fixed at both ends, low modes bend smoothly; high modes oscillate rapidly but remain \(L^2\)-orthogonal to low modes. A truncated modal expansion in the first \(N\) eigenfunctions is a Galerkin method on an \(N\)-dimensional subspace spanned by exact eigenfunctions rather than mesh polynomials. Orthogonality makes the reduced mass and stiffness matrices diagonal.

## The \(H^1\) inner product and mixed formulations

Sobolev spaces carry the inner product

\[
(u,v)_{H^1} = (u,v)_{L^2} + (\nabla u, \nabla v)_{L^2}.
\]

This is not the same as the energy inner product on \(H^1_0\) — boundary terms matter for non-homogeneous Dirichlet data — but on \(H^1_0\) the two are equivalent norms. **Mixed formulations** in fluid and solid mechanics use product Hilbert spaces \(H^1 \times L^2\) or \(H(\text{div}) \times L^2\), where different variables carry different inner products. Stokes flow pairs velocity in \(H^1\) with pressure in \(L^2\); inf-sup stability is a compatibility condition on that product geometry, developed further in Part IV.

## Numerical linear algebra as finite-dimensional Hilbert geometry

On \(V_h = \text{span}\{\phi_1,\ldots,\phi_N\}\), expanding \(u_h = \sum_j U_j \phi_j\) turns the weak form into \(\mathbf{K}\mathbf{U} = \mathbf{F}\), where

\[
K_{ij} = a(\phi_i, \phi_j), \qquad F_i = \ell(\phi_i).
\]

The stiffness matrix \(\mathbf{K}\) is the Gram matrix of the energy inner product restricted to \(V_h\). Symmetry of \(a\) makes \(\mathbf{K}\) symmetric; coercivity makes it positive definite. Conjugate gradient methods exploit exactly this Hilbert structure. What we solve on a mesh is finite-dimensional Riesz–Galerkin geometry — the same picture as the infinite-dimensional problem, with sums replacing integrals.

## Bessel's inequality and finite-dimensional capture

If \(\{\phi_k\}_{k=1}^M\) is orthonormal in \(H\) (not necessarily complete), then for every \(u \in H\),

\[
\sum_{k=1}^M |(u, \phi_k)|^2 \le \|u\|^2.
\]

Equality holds for all \(u\) if and only if the span is the whole space. Bessel's inequality says a truncated orthonormal expansion captures at most the full energy; the **defect** \(\|u\|^2 - \sum_k |(u,\phi_k)|^2\) measures what higher modes carry.

For modal truncation of wire vibration, keeping \(M\) modes discards orthogonal complement energy. If the initial displacement is mostly in the first few modes — a plucked string — few modes suffice. If the initial data has sharp kinks — a hammer strike — many modes participate and \(M\) must grow.

## The projection theorem: why Galerkin is unique

The best-approximation theorem is worth seeing in proof sketch, because every step reappears in FEM.

Let \(W \subset H\) be closed and convex (subspaces are convex). Minimize \(f(w) = \tfrac{1}{2}\|u - w\|^2\) over \(w \in W\). The minimizer \(u_W\) satisfies \(f'(u_W)(z) = 0\) for all admissible variations \(z\) in \(W\), which expands to \((u - u_W, z) = 0\) for all \(z \in W\). Uniqueness follows from strict convexity of the norm square. For a subspace, \(z\) runs over all of \(W\); for an affine translate (non-homogeneous boundary conditions), \(W\) is shifted but orthogonality of the error to the direction space remains.

Galerkin replaces the \(H^1\) inner product with the energy form \(a(\cdot,\cdot)\). Coercivity makes \(a(v,v)\) an equivalent norm, so the same convexity argument applies in \(\|\cdot\|_a\). The discrete solution \(u_h\) is the unique minimizer of \(\tfrac{1}{2}a(v,v) - \ell(v)\) over \(v \in V_h\) — the **Ritz method** when the form is symmetric.

## Pythagoras in energy space

When \(W\) is a subspace and \(u_W\) is the best approximant,

\[
\|u - w\|_a^2 = \|u - u_W\|_a^2 + \|u_W - w\|_a^2 \quad \forall w \in W
\]

only when \(u - u_W\) is \(a\)-orthogonal to \(W\) — the Pythagorean theorem for oblique energy geometry. Taking \(w = 0\) gives \(\|u\|_a^2 = \|u - u_W\|_a^2 + \|u_W\|_a^2\): energy splits into orthogonal error and discrete field energy. This decomposition underlies **a posteriori** error estimators that compare element-wise contributions to \(\|u - u_h\|_a\).

## The Lax–Milgram–Riesz chain for the wire

Consider the heated copper wire as a one-dimensional rod \(\Omega = (0,L)\) with fixed ends \(T(0) = T(L) = 0\) and steady source \(f\). The weak form

\[
\int_0^L T' v' \, dx = \int_0^L f v \, dx \quad \forall v \in H^1_0(0,L)
\]

has unique solution \(T \in H^1_0\) by Lax–Milgram. Riesz (or the energy minimization equivalent) identifies \(T\) as the minimizer of \(\tfrac{1}{2}\int (T')^2 - \int f T\). A mesh of piecewise linears produces \(T_h \in V_h\) with \(a(T - T_h, v_h) = 0\) for all test functions in \(V_h\). Céa's lemma bounds \(\|T - T_h\|_{H^1}\) by interpolation error. No step requires classical \(C^2\) smoothness of \(T\); if \(f \in L^2\), the theory closes.

## Non-symmetric problems

Convection–diffusion \(-\varepsilon u'' + b u' = f\) produces a nonsymmetric bilinear form. Lax–Milgram still applies under coercivity and boundedness, but the energy is not a simple quadratic functional — Galerkin orthogonality holds in the bilinear form, not in a symmetric inner product. Petrov–Galerkin methods choose test spaces different from trial spaces to improve stability; the Hilbert geometry becomes a Banach-space story with different norms on trial and test sides. Part V on finite volumes treats advection-dominated problems with related stability concerns.

## Lab act: project the grip load onto two bar modes (Act III prelude)

**Act III** ramps grip displacement, but the load cell reading is a **single number** — total axial force — while the wire's displacement field lives in an infinite-dimensional space. Hilbert geometry explains how a scalar measurement relates to a field: the discrete load vector \(\mathbf{f}\) is a **Riesz representative** of a linear functional on \(V_h\), and Galerkin orthogonality says the FEM solution is the best approximation in energy norm.

Take the fixed-fixed bar from [I.3](../part01-linear-algebra/03-eigenvalues.md) with two mode shapes \(\phi_1, \phi_2\) (fundamental and first harmonic, orthonormal in the mass inner product). A uniform end traction is not orthogonal to higher modes — but a **concentrated grip load** projects heavily onto \(\phi_1\).

| Step | Operation | What Hilbert geometry buys |
|------|-----------|----------------------------|
| 1 | Form load functional \(\ell(v) = \int_0^L f v\, dx\) or nodal equivalent | Riesz: \(\ell(v) = (g, v)_M\) for some \(g\) |
| 2 | Expand \(g = c_1 \phi_1 + c_2 \phi_2 + \cdots\) | Bessel: \(\|g\|^2 \ge c_1^2 + c_2^2\) |
| 3 | Solve in 2-mode subspace \(W = \mathrm{span}\{\phi_1, \phi_2\}\) | Projection theorem: unique minimizer of \(\tfrac{1}{2}a(v,v) - \ell(v)\) |
| 4 | Compare to full FEM on 20 elements | Céa: error \(\le C \inf_{w \in W} \|u - w\|_a\) |

In NumPy, build \(\mathbf{K}\) and \(\mathbf{M}\) for a 10-element bar, extract the first two eigenvectors, and solve the 2×2 reduced system \(\mathbf{K}_r \mathbf{c} = \mathbf{f}_r\). The tip displacement from two modes should capture most of the Act III linear elastic response — the same reason commercial codes offer **modal superposition** for small-amplitude vibration. When the operator later trusts a coarse mesh near the grips, this table is the Hilbert justification: the error is projection error, not guesswork.

## Concept map checkpoint (Hilbert spaces)

Hilbert geometry turns loads into projections. Before operators generalize matrices, summarize:

| Question | Hilbert-space answer (copper wire) |
|----------|-------------------------------------|
| What **object**? | Complete inner-product space; trial field \(u\) and test space \(V\) |
| What **structure**? | Orthogonality, best approximation, Riesz representation of loads |
| What **theorem**? | Lax–Milgram existence; Céa's lemma (FEM error is projection error) |
| What **breaks**? | Non-coercive forms; wrong trial/test pairing for advection |

Galerkin orthogonality \(a(u-u_h, v_h)=0\) is not a coding trick — it is the statement that the discrete solution is the energy-best approximation in \(V_h\). Act III's load cell reading is a single functional on this geometry.

## Bridge

Hilbert spaces give us angles, projections, and representations of loads. The next step is **operators**: linear maps between such spaces that generalize matrices. Dual spaces generalize row vectors and Lagrange multipliers; weak and weak* convergence describe limits when norms alone fail to detect oscillations — the behavior we see near shocks, fine-scale microstructure, and unresolved boundary layers. Operators, duality, and compactness complete the analytic toolkit before spectral theory decouples time-dependent and vibration problems into modes.

| What Hilbert geometry gave | What [II.4](04-operators-duality.md) will generalize |
|----------------------------|------------------------------------------------------|
| Inner product \((u,v)\); energy norm \(\|u\|_a\) | Bounded operators \(A: H \to H\) as infinite matrices |
| Galerkin orthogonality \(a(u-u_h, v_h)=0\) | The stiffness operator whose projection is \(\mathbf{K}\) |
| Riesz representation of loads \(\ell(v)=(f,v)\) | Dual spaces \(H^*\); point forces as functionals, not \(L^2\) functions |
| Céa's lemma: best approximation in energy | Compact embeddings \(H^1 \hookrightarrow L^2\); Aubin–Nitsche preview |

**Scale-boundary handshake (II.3 → II.4 → Acts II/III).**

| Hilbert export (this chapter) | Operator consumer ([II.4](04-operators-duality.md)) | Wire location | Failure mode |
|-------------------------------|-----------------------------------------------------|---------------|--------------|
| Riesz load \(\ell(v)=(f,v)\) | Dual functional \(\ell \in H^*\); weak\* convergence of nodal weights | Grip traction and body force in Act III | Concentrated load modeled as \(L^2\) function |
| Galerkin orthogonality \(a(u-u_h,v_h)=0\) | Stiffness operator \(A\) with \(\mathbf{K}=P_h A P_h\) | Linear elastic climb on load cell | Trial/test mismatch for advection |
| Lax–Milgram coercivity | Bounded self-adjoint operators on \(H\) | Steady Joule heating (Act II) | Non-coercive convection treated as elliptic |
| Best approximation in \(\|\cdot\|_a\) | Compact embeddings \(H^1 \hookrightarrow L^2\) | Modal truncation of bar vibration | Two-mode subspace misses hammer-strike kinks |

The grip-load projection Lab act above is the operational version of this handshake: Riesz turns a scalar load-cell reading into a field-level functional before Part IV scatters it into \(\mathbf{f}\). When a thermal FEM run converges despite a thermocouple weld, Lax–Milgram — not pointwise \(C^2\) smoothness — is the contract that makes the mesh honest.

Return to the [prologue](../prologue/00-many-scales.md): **Act II — Warming** turns on current through the copper wire, and the temperature field \(T(x)\) that Joule heating creates is not a vector in \(\mathbb{R}^N\) — it is an element of \(H^1\) whose gradient square-integrates. Lax–Milgram and Riesz in this chapter are why a mesh of piecewise linears can approximate that field without demanding classical \(C^2\) smoothness at the thermocouple weld. Part I's energy \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) reappears here as \(\|u\|_a^2 = a(u,u)\); Part IV's assembly will be the Gram matrix of the same bilinear form restricted to \(V_h\).

[II.2](02-normed-spaces.md) measured size; this chapter added **angles** — orthogonality, projection, and the representation theorem that turns loads into inner products. [II.4](04-operators-duality.md) names the maps between Hilbert spaces: stiffness as an operator, loads in the dual, weak convergence when norms alone miss oscillations. Turn the page when projection feels geometric but the word "operator" still sounds abstract — that is the signal Hilbert space is ready to host matrices that never fit in \(\mathbb{R}^{N \times N}\).
