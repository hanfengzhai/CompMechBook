# Operators, Duality, and Weak Convergence

Matrices act on column vectors. Differential operators act on functions. Dual spaces act on vectors and functions alike through pairing — the language of loads, constraints, and virtual work. This chapter develops the operator vocabulary that makes weak formulations, mixed finite elements, and convergence under mesh refinement precise. When the copper wire's displacement field \(u_h\) changes with mesh size, we ask not only whether \(\|u_h - u\|\) shrinks, but in what **sense** the sequence approaches the limit. Strong convergence in norm is the strongest answer; weak convergence is often enough, and sometimes all that holds.

## Scene: the load is not a vector of numbers

The grip applies a fixed displacement; gravity pulls downward with a force per unit volume; a contact constraint pushes only where the wire touches the wedge. In the weak form, each load becomes a linear functional on the displacement space — not an entry in a column vector until we choose a basis. Dual spaces are where virtual work lives: they translate physical loads into data the weak form can consume, and they explain why refining the mesh changes the discrete vector but not the underlying load object.

## Bounded linear operators

Let \(H_1\) and \(H_2\) be Hilbert spaces. A linear operator \(A: H_1 \to H_2\) is **bounded** if there exists a constant \(C \ge 0\) such that

\[
\|Au\|_{H_2} \le C \|u\|_{H_1} \quad \forall u \in H_1.
\]

The **operator norm** is

\[
\|A\| = \sup_{\|u\|_{H_1} = 1} \|Au\|_{H_2}.
\]

Boundedness is equivalent to continuity: small changes in input produce bounded changes in output. In mechanics, stability estimates often bound \(\|u\|_{H^1}\) by \(\|f\|_{L^2}\) for the load — a statement that the solution operator \(f \mapsto u\) is bounded from \(L^2\) to \(H^1\).

**Example (identity embedding).** The inclusion \(I: H^1(\Omega) \hookrightarrow L^2(\Omega)\) is linear and bounded on bounded domains: \(\|u\|_{L^2} \le \|u\|_{H^1}\). It is not an isomorphism: not every \(L^2\) function is \(H^1\).

**Example (Laplacian).** The operator \(-\Delta: H^2(\Omega) \cap H^1_0(\Omega) \to L^2(\Omega)\) is bounded when the domain is regular enough. As a map from \(H^1_0\) to \(L^2\) without restricting the domain of definition, the Laplacian is **unbounded** — a central reason weak forms replace strong forms. We do not apply \(-\Delta\) directly to \(H^1\) functions; we apply the bilinear form \(a(u,v) = \int \nabla u \cdot \nabla v\) instead.

**Example (stiffness operator).** For fixed mesh \(V_h \subset H^1_0\), the Galerkin operator \(A_h: V_h \to V_h\) defined by \(a(u_h, v_h) = (A_h u_h, v_h)_{L^2}\) is bounded and, when \(a\) is coercive, invertible on \(V_h\). Assembly computes the matrix of \(A_h\) in a chosen basis.

## Dual spaces

The **dual space** \(H^*\) of a normed space \(H\) consists of all **continuous linear functionals** \(\ell: H \to \mathbb{R}\), with norm

\[
\|\ell\|_{H^*} = \sup_{\|v\|_H = 1} |\ell(v)|.
\]

Elements of \(H^*\) are not functions in the usual sense; they are **rules for pairing** against test functions. In weak mechanics, loads are functionals.

**Examples on \(H^1(\Omega)\):**

- **Body force:** \(\ell(v) = \int_\Omega f v \, d\Omega\) for \(f \in L^2(\Omega)\). Bounded by Cauchy–Schwarz: \(|\ell(v)| \le \|f\|_{L^2} \|v\|_{L^2}\).

- **Boundary traction:** \(\ell(v) = \int_{\Gamma_N} t v \, dS\) for surface traction \(t \in L^2(\Gamma_N)\), when the trace of \(v\) on \(\Gamma_N\) is in \(L^2\).

- **Thermal source:** Same structure for steady conduction on the wire: integrated source against test temperature.

Riesz representation identifies \(H^* \cong H\) when \(H\) is a Hilbert space, via \(\ell(v) = (g,v)_H\). But **mixed methods** naturally inhabit product spaces where velocity and pressure, or displacement and stress, live in different spaces with different norms. The dual of a product is a product of duals; saddle-point formulations in Part IV exploit this split rather than forcing everything into a single Riesz identification.

**The dual pairing.** Write \(\langle \ell, v \rangle = \ell(v)\) for the action of a functional on a test function. The weak form \(\langle \ell, v \rangle = a(u,v)\) separates **kinematically admissible** test functions \(v\) from the solution \(u\) sought in a trial space. Virtual work in Part VI is this pairing written in mechanical language.

## Weak convergence

A sequence \(\{u_n\} \subset H\) converges **strongly** to \(u\) if \(\|u_n - u\| \to 0\). It converges **weakly** to \(u\), written \(u_n \rightharpoonup u\), if

\[
(u_n, v) \to (u, v) \quad \forall v \in H
\]

when \(H\) is a Hilbert space — more generally, \(\ell(u_n) \to \ell(u)\) for all \(\ell \in H^*\).

Weak convergence captures stabilization of **averages** against smooth test functions even when norms do not decay. An oscillatory sequence can have constant \(L^2\) norm while its averages against any fixed smooth \(\phi\) converge — the oscillations blur under pairing.

**Example.** On \((0,1)\), \(u_n(x) = \sin(n\pi x)\) satisfies \(\|u_n\|_{L^2} = 1/\sqrt{2}\) for all \(n\), yet \((u_n, v) \to 0\) for every \(v \in L^2(0,1)\) because high-frequency sines average to zero against fixed \(v\). Thus \(u_n \rightharpoonup 0\) weakly in \(L^2\), but \(\|u_n\|\) does not tend to zero.

For elliptic FEM on the copper wire, energy-norm convergence \(\|u - u_h\|_a \to 0\) is strong convergence in the energy space. \(L^2\) convergence often follows by compact embedding (Rellich–Kondrachov, below). Problems with unresolved microstructure — plastic slip, damage localization — may produce sequences converging weakly but not strongly in norms that detect fine-scale oscillation.

## Weak* convergence

When the space \(H\) is itself a dual — for example, \(L^\infty = (L^1)^*\) — **weak* convergence** applies to sequences of functionals or to elements of \(H\) acting through pairing on a separable predual. \(\ell_n\) converges weak* to \(\ell\) if

\[
\ell_n(v) \to \ell(v) \quad \forall v \in \text{predual}.
\]

In computational mechanics, weak* convergence underlies convergence of stress measures, of residual distributions in limit analysis, and of probability measures in stochastic homogenization. The detail belongs to specialized courses; the habit matters here: **not every physically meaningful limit is a strong limit in a single norm**.

## Compact operators

A bounded operator \(K: H_1 \to H_2\) is **compact** if bounded sets in \(H_1\) map to **relatively compact** sets in \(H_2\) — sets whose closure is compact. Equivalently, if \(\{u_n\}\) is bounded in \(H_1\), then \(\{Ku_n\}\) has a convergent subsequence in \(H_2\).

Compact operators generalize the finite-rank behavior of matrices. On infinite-dimensional spaces, the identity operator is **not** compact — another way infinite dimensions differ from \(\mathbb{R}^N\).

**Example (integral operators).** On \(L^2(0,L)\), the operator

\[
(Ku)(x) = \int_0^L G(x,y) u(y) \, dy
\]

with square-integrable kernel \(G\) is compact. Green's operators for elliptic PDEs — mapping source terms to displacements with smoothing — are often compact or compact on appropriate subspaces, which explains why inverting them yields eigenvalue problems with discrete spectra.

**Example (finite-rank Galerkin).** Restriction to \(V_h\) followed by projection back is finite-rank on \(H\), hence compact. FEM approximations of compact operators inherit discrete spectra that converge to the continuous spectrum — the mathematical basis of lumped mass versus consistent mass in vibration analysis.

## The Rellich–Kondrachov theorem

Embeddings between Sobolev spaces on bounded domains are not merely continuous; at subcritical exponents they are **compact**.

**Theorem (Rellich–Kondrachov).** If \(\Omega \subset \mathbb{R}^d\) is bounded and Lipschitz, the embedding

\[
H^1(\Omega) \hookrightarrow L^2(\Omega)
\]

is **compact**: every bounded sequence in \(H^1(\Omega)\) has a subsequence converging strongly in \(L^2(\Omega)\).

This is stronger than boundedness of the inclusion. It says that bounded \(H^1\) sequences cannot sustain indefinitely fine oscillations in \(L^2\) without paying gradient cost — a form of compactness tailored to FEM.

Consequences for the copper wire and for general elliptic problems:

1. **Spectral discreteness:** Elliptic eigenvalue problems on bounded domains have discrete spectra accumulating to infinity; eigenfunctions can be chosen orthonormal in \(L^2\).

2. **Error improvement:** Energy-norm FEM error control often yields \(L^2\) error one order higher (Aubin–Nitsche duality argument), using compact embedding as the key analytic input.

3. **Existence of minimizers:** In nonlinear elasticity and plasticity, compact embeddings support direct methods in the calculus of variations — extracting convergent subsequences from minimizing sequences.

Without Rellich–Kondrachov on unbounded domains, spectra can become continuous and FEM eigenvalue convergence subtler. For the bounded specimens of laboratory mechanics, compact embedding is the standard hypothesis.

## The Galerkin projector

Let \(H\) be a Hilbert space with inner product inducing norm \(\|\cdot\|\), let \(a(\cdot,\cdot)\) be a coercive bilinear form on \(H\), and let \(V_h \subset H\) be finite-dimensional. The **Galerkin solution** \(u_h \in V_h\) for a given \(u \in H\) (or for load functional \(\ell\)) can be viewed through the **Galerkin projector** \(P_h: H \to V_h\) defined implicitly by

\[
a(u - P_h u, v_h) = 0 \quad \forall v_h \in V_h.
\]

For the source problem with solution operator \(S: \ell \mapsto u\), the discrete solution is \(u_h = P_h u\). The projector depends on \(a\), not on the load alone: energy orthogonality defines \(P_h\).

**Properties.** \(P_h\) is linear on \(H\), idempotent on \(V_h\) (\(P_h v_h = v_h\)), and bounded in the energy norm:

\[
\|P_h u\|_a \le C \|u\|_a
\]

with \(C\) independent of \(h\) when \(a\) is coercive and continuous. Céa's lemma states

\[
\|u - P_h u\|_a \le \frac{M}{m} \inf_{v_h \in V_h} \|u - v_h\|_a.
\]

The projector is quasi-optimal: it cannot beat the best approximation in \(V_h\) by more than a constant depending only on the form \(a\).

**Example.** For Poisson's equation with piecewise linear elements on a mesh of size \(h\), \(P_h u\) is the unique piecewise linear field whose energy inner product with every test function vanishes against the error. If \(u\) is smooth, interpolation \(I_h u \in V_h\) satisfies \(\|u - I_h u\|_a = O(h)\), hence \(\|u - P_h u\|_a = O(h)\) by Céa. The projector realizes the approximation power of the element space.

## Adjoint operators

For bounded \(A: H_1 \to H_2\) between Hilbert spaces, the **adjoint** \(A^*: H_2 \to H_1\) satisfies

\[
(Au, v)_{H_2} = (u, A^* v)_{H_1} \quad \forall u \in H_1,\, v \in H_2.
\]

Self-adjoint operators — \(A = A^*\) on a single space — govern symmetric bilinear forms. The Laplacian in weak form is associated with a self-adjoint, positive operator on \(H^1_0\). Mixed formulations produce block operators that are not self-adjoint but satisfy inf-sup conditions on paired spaces.

For sensitivity analysis of the wire's response to a perturbation in load \(\delta f\), the adjoint solution encodes how functionals of interest change — a duality pattern that extends to optimization and uncertainty quantification in computational mechanics.

## Summary table

| Concept | Finite-dimensional analogue | Mechanics role |
|---------|----------------------------|----------------|
| Bounded operator | Matrix with bounded norm | Stability of solution map |
| Dual functional | Row vector \(\mathbf{f}^T\) | Loads, tractions, sources |
| Weak convergence | Componentwise convergence without norm decay | Limits with oscillation |
| Compact operator | Matrix limit of finite-rank | Green's operators, embeddings |
| Galerkin projector | Oblique projection \(\mathbf{P}_h\) | FEM solution as best energy fit |

## Uniform boundedness and stability of families

If \(\{A_n\}\) is a sequence of bounded operators and \(\sup_n \|A_n\| < \infty\), then for each fixed \(u\), \(\{A_n u\}\) is bounded — pointwise in operator index. The **uniform boundedness principle** (Banach–Steinhaus) strengthens this: if \(\{A_n u\}\) is bounded for every \(u\), then \(\sup_n \|A_n\|\) is finite. In FEM, stability constants in a priori error bounds must be uniform in \(h\) as the mesh refines; otherwise "convergence" might hide blowing operator norms.

For the wire problem, the discrete solution operators \(S_h: f \mapsto u_h\) should satisfy \(\|S_h f\|_{H^1} \le C \|f\|_{L^2}\) with \(C\) independent of \(h\) when the bilinear form is coercive and the spaces are conforming. That uniform bound is the discrete echo of Lax–Milgram on the continuous problem.

## Aubin–Nitsche duality (preview)

Energy-norm error \(\|u - u_h\|_a\) is often the natural first result. Engineers frequently ask for mean-square error \(\|u - u_h\|_{L^2}\) instead. **Aubin–Nitsche** duality uses an auxiliary problem — typically an elliptic problem with source term \(u - u_h\) — and compact embedding \(H^1 \hookrightarrow L^2\) to prove

\[
\|u - u_h\|_{L^2} \le C h^2 \|f\|_{L^2}
\]

for piecewise linear elements on smooth problems, one order better than energy error. The argument is operator-theoretic: the error is paired against a **dual** variable solving with the adjoint operator. We preview it here because it is the clearest application of compact embedding and duality together — themes of this chapter applied in Part IV's error analysis.

## Distribution of loads and convergence of functionals

Suppose a sequence of load functionals \(\ell_n\) converges weak* to \(\ell\): \(\ell_n(v) \to \ell(v)\) for all smooth \(v\). Under stability of the solution map, the corresponding solutions \(u_n\) converge weakly to \(u\). Concentrating a distributed load onto a single node as the mesh refines is such a sequence; the limit is often a point load functional on \(H^1\).

For the wire, replacing a distributed weight by equivalent nodal forces is standard FEM practice. Weak* convergence of loads is the condition under which the discrete solutions converge to the weak solution of the limit problem — not merely to a different physics because the loading was mishandled.

## Fredholm alternative (compact perturbation)

For \(I - K\) with compact \(K\), the Fredholm alternative states: either \(I - K\) is invertible, or \(\ker(I - K)\) is nontrivial with finite dimension. Resonance in vibration — natural frequencies where a nonzero mode satisfies homogeneous equilibrium without load — is the kernel of an operator \(I - \lambda K\). Finite-dimensional linear algebra's rank-nullity theorem survives in compact operator form.

Buckling analysis searches for \(\lambda\) where stiffness loses ellipticity; the lowest such \(\lambda\) is the critical load factor. On a mesh, \(\det(\mathbf{K} - \lambda \mathbf{K}_g) = 0\); in the limit, eigenvalues of a compact operator. The spectral chapter ahead makes the connection explicit.

## Bridge

Operators on Hilbert spaces become transparent when they are **self-adjoint** and **compact**: spectra decompose into real eigenvalues and orthonormal eigenvectors. The spectral theorem is the infinite-dimensional generalization of diagonalizing a symmetric matrix.

| What this chapter gave (operators) | What the next chapter completes (spectra) |
|------------------------------------|-------------------------------------------|
| Bounded operators as infinite matrices | Compact operators: spectra accumulate at zero |
| Dual functionals \(\ell(v)\) for loads | Self-adjoint operators: real eigenvalues, orthogonal modes |
| Weak convergence of sequences | Spectral theorem: diagonalization in Hilbert space |
| Aubin–Nitsche preview for \(L^2\) error | Wire vibration, buckling, heat decay as eigenvalue problems |

On the copper wire, the stiffness operator from Part I's spring network becomes a differential operator in the limit; its eigenfunctions are standing-wave patterns along the bar, its eigenvalues are squared natural frequencies. Buckling searches for \(\lambda\) where \(\mathbf{K} - \lambda \mathbf{K}_g\) loses invertibility — the same Fredholm logic previewed above. The next chapter states the spectral theorem explicitly and closes Part II with the **well-posedness triangle** that hands off to Part III: strong forms for intuition, weak forms for computation, Sobolev spaces for regularity. Turn the page when operator language feels natural — PDEs in Part III are where those operators finally have names like \(-\Delta\) and \(-\nabla\cdot(k\nabla\cdot)\).
