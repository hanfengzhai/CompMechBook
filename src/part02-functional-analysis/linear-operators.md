# Linear operators

## Definition

If \(V, W\) are normed spaces over the same field, a map \(T : V \to W\) is a **linear operator** if

\[
T(\alpha u + \beta v) = \alpha Tu + \beta Tv.
\]

\(T\) is **bounded** if \(\|T\| < \infty\) with operator norm

\[
\|T\| = \sup_{\|u\|=1} \|Tu\|.
\]

The space of bounded linear operators \(V \to W\) is denoted \(\mathcal{B}(V,W)\).

## Examples from mechanics

| Operator | Domain → Range | Equation |
|----------|----------------|----------|
| Gradient | \(H^1(\Omega) \to L^2(\Omega)^d\) | \(\nabla u\) |
| Divergence | \(H(\mathrm{div},\Omega) \to L^2(\Omega)\) | \(\nabla\cdot\boldsymbol{\sigma}\) |
| Laplacian | \(H^2_0(\Omega) \to L^2(\Omega)\) | \(-\Delta u\) |
| Elasticity | \(H^1_0(\Omega)^d \to H^{-1}(\Omega)^d\) | \(-\mathrm{div}(\mathbb{C}\boldsymbol{\varepsilon} u)\) |

Differential operators are often unbounded on \(L^2\) but bounded as maps between Sobolev spaces of different order.

## Kernel and range

\(\mathcal{N}(T) = \{u : Tu = 0\}\), \(\mathcal{R}(T) = \{Tu : u \in V\}\).

Rigid-body modes are \(\mathcal{N}(\boldsymbol{\varepsilon})\) for the strain operator on an unconstrained body.

## Adjoint operators

For Hilbert spaces \(H, K\) and bounded \(T : H \to K\), the **adjoint** \(T^\ast : K \to H\) satisfies

\[
\langle Tu, v \rangle_K = \langle u, T^\ast v \rangle_H \quad \forall u \in H,\, v \in K.
\]

Self-adjoint operators have real spectra and variational characterizations—central to structural eigenproblems.

## Compact operators (statement)

\(T\) is **compact** if bounded sets in \(V\) map to relatively compact sets in \(W\). Compact perturbations of identity arise in Fredholm theory; in FEM, discrete operators approximate compact resolvents of elliptic PDEs.

---

**Theorem (closed graph lemma, statement).** A closed linear operator with dense domain is bounded if it is everywhere defined on a Banach space.

Unbounded operators (e.g. \(\Delta\) on \(L^2\) without restricting domain) require care; Sobolev spaces are the standard remedy.

## Discrete realization

FEM replaces \(T\) with a matrix \(\mathbf{K}\). If \(\{\phi_i\}\) is a basis of \(V_h\),

\[
K_{ij} = a(\phi_j, \phi_i),
\]

so \(\mathbf{K}\) is the **Galerkin discretization** of operator \(A\) defined by \(a(u,v) = \langle Au, v \rangle\).

<div class="bridge">

**Bridge.** Operators eat vectors and return vectors. **Functionals** eat vectors and return scalars—loads, energies, constraints.

</div>
