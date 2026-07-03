# From \(\mathbb{R}^n\) to Functions: The First Step Up

So far our state vectors have had finite length \(N\). A temperature field on a bar, however, is specified by a value at **every** point \(x \in [0,L]\). Informally, that is infinitely many degrees of freedom. Making this precise without losing the linear-algebraic intuition is the job of functional analysis — but we can already see the path.

Heat the copper wire at one end and wait: the temperature is not a vector of three numbers unless we pretend there are only three sensors. It is a function \(T(x)\) for \(x\) along the wire. Discretize that function finely enough and \(\mathbf{T} \in \mathbb{R}^N\) becomes a good proxy; coarsen the mesh and the proxy lies. The **true** state, in the continuum model, is the function itself — or rather, an element of an infinite-dimensional vector space equipped with norms that make the approximation problem well posed.

## Functions as infinite vectors

Discretize a function \(u(x)\) on \([0,L]\) by sampling at \(N\) points:

\[
u_i \approx u(x_i), \quad i = 1,\ldots,N.
\]

The vector \(\mathbf{u} \in \mathbb{R}^N\) is a **proxy** for the function. Refining the mesh increases \(N\). The limit \(N \to \infty\) suggests a function \(u: [0,L] \to \mathbb{R}\).

We add and scale functions pointwise:

\[
(\alpha u + \beta v)(x) = \alpha u(x) + \beta v(x),
\]

just as we add and scale vectors componentwise. Function spaces are vector spaces — often infinite-dimensional ones.

### Riemann sums and the inner product

A discrete inner product \(\sum_i u_i v_i \Delta x\) approximates the continuum inner product as the mesh refines:

\[
\sum_{i=1}^{N} u(x_i)\, v(x_i)\,\Delta x \;\longrightarrow\; \int_0^L u(x)\, v(x)\, dx.
\]

The mass matrix \(\mathbf{M}\) in finite elements is designed so that \(\mathbf{u}^T \mathbf{M}\mathbf{v}\) equals this quadrature exactly for polynomial data on each element. The linear algebra **is** the quadrature rule for the function-space inner product.

## Inner products on functions

The **\(L^2\) inner product** on \([0,L]\) is

\[
(u, v)_{L^2} = \int_0^L u(x)\, v(x)\, dx.
\]

This replaces the sum \(\sum_i u_i v_i\). The associated norm is

\[
\|u\|_{L^2} = \sqrt{(u,u)_{L^2}}.
\]

In finite elements, \(\mathbf{M}\) approximates this inner product on the subspace of mesh functions:

\[
\mathbf{u}^T \mathbf{M} \mathbf{v} \approx \int_\Omega u_h v_h \, d\Omega.
\]

Orthogonality of functions — \((u,v)_{L^2} = 0\) — generalizes orthogonal eigenvectors. Fourier modes \(\sin(n\pi x/L)\) are mutually orthogonal on \([0,L]\) with Dirichlet boundaries; they are the continuum eigenvectors of the Laplacian, the limit of discrete vibration modes from Chapter 3 as \(N \to \infty\).

## Matrices become operators

A matrix \(\mathbf{K}\) maps \(\mathbb{R}^N \to \mathbb{R}^N\). A **linear operator** \(K\) maps a function space to itself. The discrete problem \(\mathbf{K}\mathbf{u}=\mathbf{f}\) approximates

\[
K u = f \quad \text{in a domain},
\]

with boundary conditions. For Poisson's equation \(-u'' = f\) on \((0,L)\), the operator is minus the second derivative, inverted (with boundary data) by integration.

### Worked example: 1D Laplacian on the wire

On \((0,L)\) with \(u(0)=u(L)=0\), consider \(-u'' = f\). Define \(K u = -u''\) on the space of smooth functions satisfying the boundary conditions. For \(f = 1\) (uniform volumetric heating of the wire cross-section, steady state), the strong solution is \(u(x) = x(L-x)/2\).

Discretize with finite differences: \( -u''(x_i) \approx -(u_{i-1} - 2u_i + u_{i+1})/\Delta x^2 \). The discrete operator is a tridiagonal matrix \(\mathbf{K}_h\). As \(h \to 0\), \(\mathbf{K}_h \mathbf{u}_h \to f\) in a sense made precise in Part II — and the discrete solution \(\mathbf{u}_h\) converges to \(u(x)\).

| Discrete (Part I) | Continuum (Part II–III) |
|-------------------|-------------------------|
| \(\mathbf{u} \in \mathbb{R}^N\) | \(u \in V\) (e.g. \(H^1_0\)) |
| \(\mathbf{K}\mathbf{u} = \mathbf{f}\) | Find \(u\) such that \(a(u,v) = \ell(v)\) |
| \(\mathbf{u}^T \mathbf{K}\mathbf{u}\) | \(a(u,u) = \int |\nabla u|^2\) |
| Eigenvalues of \(\mathbf{K}\) | Spectrum of operator \(K\) |

## The heat equation as a first PDE

Beyond equilibrium lies evolution. The **heat equation** on the copper wire:

\[
u_t - \alpha u_{xx} = f(x,t), \quad 0 < x < L, \quad t > 0,
\]

with \(u(0,t)=u(L,t)=0\) and initial temperature \(u(x,0) = u_0(x)\), says that temperature diffuses at rate \(\alpha\). Semidiscretization in space (FEM or finite differences) produces a system of ODEs

\[
\mathbf{M}\dot{\mathbf{u}} + \mathbf{K}\mathbf{u} = \mathbf{f}(t),
\]

the same \(\mathbf{M}\) and \(\mathbf{K}\) from vibration, now coupled to time integration. Part III develops the weak form of parabolic problems; Part IV time-marches the resulting matrices; Part V treats diffusive fluxes in finite volume form for fluids around the wire.

## Why infinity changes the questions

In finite dimensions:

- Every Cauchy sequence converges (in \(\mathbb{R}^N\)).
- Every bounded sequence has a convergent subsequence (Bolzano–Weierstrass).

In infinite-dimensional function spaces, these fail without extra structure. **Completeness** (Cauchy sequences converge) and **compactness** (bounded sets behave nicely) become nontrivial requirements. Part II develops the spaces where standard PDE and FEM theory lives.

Consider functions \(u_n(x) = \sin(n\pi x/L)\) on \([0,L]\). They have \(\|u_n\|_{L^2}\) bounded but become increasingly oscillatory — no subsequence converges in \(L^2\) to a smooth limit. Boundedness alone is insufficient; we need **compact embeddings** (e.g. \(H^1\) into \(L^2\)) to extract convergent subsequences in Galerkin proofs.

## Approximation as projection

Given a mesh with piecewise-linear hat functions \(\{\phi_i\}\), the finite element space is

\[
V_h = \text{span}\{\phi_1,\ldots,\phi_N\} \subset H^1(\Omega).
\]

The best approximation \(u_h \in V_h\) to a true solution \(u\) in the energy norm minimizes \(\|u - v_h\|_{\text{energy}}\). Céa’s lemma (Part IV) bounds the FEM error by the best approximation error — linking **infinitely many** degrees of freedom in \(u\) to **finite** ones in \(V_h\).

For the heated copper wire, a coarse mesh captures the gross gradient; a fine mesh resolves boundary layers if the Biot number demands it. Refinement is not merely "more numbers" — it is enlarging a finite-dimensional subspace inside an infinite-dimensional space.

## The central cast, introduced early

Three spaces will dominate the rest of the book:

| Space | Norm / inner product | Role |
|-------|---------------------|------|
| \(L^2(\Omega)\) | \(\|u\|_{L^2}^2 = \int \|u\|^2\) | Energy of fields, least squares |
| \(H^1(\Omega)\) | \(\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2\) | Weak derivatives, FEM |
| Product spaces | Mixed norms | Fluids (velocity–pressure), contact |

We do not need full rigor yet. We need the picture: **finite elements are linear algebra in \(H^1\)**.

Sobolev spaces (Part III, Chapter 3) define what "\(\nabla u\)" means when \(u\) has a kink at a mesh node — exactly the regularity piecewise-linear finite element solutions possess.

## Linear functionals and loads

In \(\mathbb{R}^N\), the load vector \(\mathbf{f}\) pairs with displacements via \(\mathbf{f}^T \mathbf{u}\). In the continuum, a **linear functional** \(\ell(v) = \int_\Omega f v \, d\Omega\) plays the same role: it maps test functions to numbers. Riesz representation (Part II) identifies functionals with elements of the space itself when we have an inner product — the mathematical reason a load can be "represented" as a vector in the discrete problem.

Point loads on the copper wire (a force at a node) are not functions in \(L^2\); they are functionals — delta-like objects handled by weak formulations rather than pointwise strong equations.

## Gram matrices and orthonormal bases on meshes

Given basis functions \(\{\phi_j\}\) on a mesh, the **Gram matrix** \(G_{ij} = (\phi_i, \phi_j)_{L^2}\) is the mass matrix before assembly into physical units. Orthonormalizing the basis (via Gram–Schmidt or QR on sampled values) produces a condition-number-friendly coordinate system — the same idea as orthonormal eigenvectors, now on function spaces. Isoparametric maps (Part IV) generalize this: the Jacobian determinant weights integrals so that reference-element orthogonality becomes physical-space coupling.

## Concept map checkpoint (Part I → Part II)

Part I ends where finite-dimensional algebra meets its limit. The four questions from the opening concept map now change vocabulary without changing discipline:

| Question | At \(N\) nodes (Part I) | At the continuum limit (Part II preview) |
|----------|-------------------------|------------------------------------------|
| **Object** | \(\mathbf{u} \in \mathbb{R}^N\), \(\mathbf{K}\) | \(u \in H^1(\Omega)\), operator \(A\) |
| **Structure** | Symmetry, sparsity, positive definiteness | Inner product, completeness, compact embeddings |
| **Theorem** | Unique \(\mathbf{u}=\mathbf{K}^{-1}\mathbf{f}\); spectral modes | Lax–Milgram; Galerkin best approximation; spectral accumulation |
| **Breaks if missing** | Ill-conditioning as \(N\) grows | Cauchy sequences without limit in the space; loads not in \(L^2\) |

The copper wire's nodal displacements are still numbers on a mesh — but the **limit** those numbers approximate is a function. Part II supplies the spaces where that limit lives and the theorems that make mesh refinement meaningful.

## Bridge to Part II

Linear algebra taught us to solve \(\mathbf{K}\mathbf{u}=\mathbf{f}\). Mechanics asks us to solve PDEs. The bridge is:

1. Write the PDE in **weak form** (multiply by a test function, integrate by parts).
2. Choose a finite-dimensional subspace \(V_h \subset H^1\).
3. Solve the resulting matrix system.

Steps 1–2 require function spaces. Part II supplies normed spaces, completeness, Hilbert space structure, and compactness — the vocabulary for existence, uniqueness, and convergence. Part III writes the weak forms for Poisson, heat, and elasticity that Part IV discretizes.

Turn the page. We leave the comfort of \(\mathbb{R}^N\) and enter the space of admissible fields. The copper wire’s temperature and displacement live there; our meshes are finite-dimensional shadows of those fields, and the shadow improves as \(h \to 0\).
