# Operators, Duality, and Weak Convergence

Matrices act on vectors. Operators act on functions. Dual spaces act on operators. This chapter develops the vocabulary that makes weak formulations and mixed methods precise.

## Bounded linear operators

An operator \(A: H_1 \to H_2\) is **bounded** if

\[
\|Au\|_{H_2} \le C \|u\|_{H_1}
\]

for some constant \(C\). Boundedness is continuity. The Laplacian is not bounded on \(L^2\) — it maps \(H^2\) to \(L^2\) — which is why we pass to weak forms.

## Dual spaces

The **dual** \(H^*\) consists of continuous linear functionals on \(H\). For the Hilbert space \(H^1(\Omega)\), elements of \((H^1)^*\) include:

- Body forces: \(v \mapsto \int f v\)
- Boundary tractions: \(v \mapsto \int_{\Gamma_N} t v\)
- Point loads (carefully, via distributions)

Riesz representation identifies \(H^* \cong H\) when \(H\) is Hilbert, but **mixed methods** naturally live in products where this identification is split across variables (velocity and pressure in Stokes flow, displacement and stress in elasticity).

## Weak convergence

A sequence \(\{u_n\}\) converges **weakly** to \(u\) in \(H\) if

\[
(u_n, v) \to (u,v) \quad \forall v \in H.
\]

Weak convergence captures oscillatory behavior: norms may not decrease, but averages against smooth test functions stabilize. In computational mechanics, mesh refinement often produces sequences that converge weakly in \(L^2\) but strongly in energy norms for elliptic problems.

**Weak* convergence** (for functionals) underlies convergence of residual measures and is central in limit analysis of plasticity.

## Compact operators

An operator \(K\) is **compact** if bounded sets map to relatively compact sets. Integral operators (Green's functions, stress operators in elasticity) are often compact on appropriate spaces. Compactness makes eigenvalue problems discrete-friendly: spectra accumulate at zero or infinity in controlled ways.

The **Rellich–Kondrachov theorem** states that the embedding \(H^1(\Omega) \hookrightarrow L^2(\Omega)\) is compact for bounded domains. This is why elliptic eigenvalue problems have discrete spectra accumulating to infinity — the mathematical reason finite element eigenvalues approximate continuous ones.

## Galerkin projection as an operator

Let \(V_h = \text{span}\{\phi_1,\ldots,\phi_N\} \subset H\). The **Galerkin projector** \(P_h: H \to V_h\) maps \(u\) to the unique \(u_h \in V_h\) satisfying

\[
a(u - u_h, v_h) = 0 \quad \forall v_h \in V_h.
\]

Céa's lemma bounds \(\|u - u_h\|_{H} \le C \inf_{v_h \in V_h} \|u - v_h\|_{H}\). Approximation theory (how well \(u\) can be interpolated) feeds directly into discretization error.

## Bridge

Spectral theory for self-adjoint operators generalizes eigenvalue analysis. The spectral theorem guarantees orthonormal eigenbases and variational characterizations — the infinite-dimensional explanation for normal modes, buckling loads, and vibration frequencies.
