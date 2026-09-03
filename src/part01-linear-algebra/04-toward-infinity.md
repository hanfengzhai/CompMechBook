# From \(\mathbb{R}^n\) to Functions: The First Step Up

So far our state vectors have had finite length \(N\). A temperature field on a bar, however, is specified by a value at **every** point \(x \in [0,L]\). Informally, that is infinitely many degrees of freedom. Making this precise without losing the linear-algebraic intuition is the job of functional analysis — but we can already see the path.

Heat the copper wire at one end and wait: the temperature is not a vector of three numbers unless we pretend there are only three sensors. It is a function \(T(x)\) for \(x\) along the wire. Discretize that function finely enough and \(\mathbf{T} \in \mathbb{R}^N\) becomes a good proxy; coarsen the mesh and the proxy lies. The **true** state, in the continuum model, is the function itself — or rather, an element of an infinite-dimensional vector space equipped with norms that make the approximation problem well posed.


## Plot spine (one line) {#plot-spine-one-line}

> **I.4 — Act I — Grammar:** Refine the mesh until nodal values become a field — \(N\to\infty\) is the gate where grammar becomes analysis.

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter. **Ascent gate (row 20):** this chapter is the first mandatory pause in row 17's straight read — recite the sentence above aloud, then read the [Bridge to Part II](#bridge-to-part-ii) before opening functional analysis.

## Scene: the sensors multiply

Return to the spring network from Chapters 1–3, now with a twist in the experiment. An engineer places thermocouples along the copper wire — first three, then ten, then forty, then a hundred — each reading \(T(x_i)\) at a node of a finer mesh. Every refinement produces a longer column vector \(\mathbf{T}_N\), yet the plotted profile along the axis stops changing shape once the spacing is fine enough. The family of vectors is not converging to a **longer** vector; it is converging to a **function** \(T(x)\) defined at every \(x\), the limit object Part II will name.

The same story holds for axial displacement under tension: halve the bar element length, double \(N\), reassemble \(\mathbf{K}_N\), solve again. The discrete solution \(\mathbf{u}_N\) is a different array each time, but the engineer's eye sees one smooth elongation profile emerging. Part I ends here — not with a bigger matrix, but with the question Part II must answer: **what space do these profiles live in**, and what operator does \(\mathbf{K}_N\) approximate as \(N \to \infty\)?

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

### Worked preview: block structure for thermo-mechanical coupling

The copper wire in the lab does not heat and stretch in isolation. Joule heating raises temperature; thermal expansion changes grip displacement; conductivity redistributes heat along the axis. At the discrete level — before Part IV assembles tetrahedra or Part V fluxes air around the cylinder — the coupling is already visible as a **block matrix**.

Partition unknowns into displacement \(\mathbf{u} \in \mathbb{R}^{N_u}\) and temperature \(\mathbf{T} \in \mathbb{R}^{N_T}\). A linearized steady coupled problem takes the form

\[
\begin{bmatrix} \mathbf{K}_{uu} & \mathbf{K}_{uT} \\ \mathbf{K}_{Tu} & \mathbf{K}_{TT} \end{bmatrix}
\begin{bmatrix} \mathbf{u} \\ \mathbf{T} \end{bmatrix}
=
\begin{bmatrix} \mathbf{f}_u \\ \mathbf{f}_T \end{bmatrix}.
\]

Each block is assembled with the same scatter grammar from [I.2](02-linear-maps.md):

| Block | Physical meaning | Typical assembly |
|-------|------------------|------------------|
| \(\mathbf{K}_{uu}\) | Elastic stiffness (bar or solid elements) | \(\sum_e \mathbf{L}_e^T \mathbf{k}_e^{uu} \mathbf{L}_e\) |
| \(\mathbf{K}_{TT}\) | Thermal conduction (same mesh or a thermal-only line) | \(\sum_e \mathbf{L}_e^T \mathbf{k}_e^{TT} \mathbf{L}_e\) |
| \(\mathbf{K}_{uT}\), \(\mathbf{K}_{Tu}\) | Thermal strain load; temperature-dependent modulus (often one-way in first pass) | Coupling vectors or sparse off-diagonal blocks |

**One-dimensional toy on the wire axis.** Take \(N_u = N_T = 3\) nodes at the same locations (co-located thermo-mechanical mesh). Let \(\mathbf{K}_{uu} = \mathbf{K}\) be the bar stiffness from [I.1](01-vectors-matrices.md), \(\mathbf{K}_{TT} = (k_t/h)\mathbf{K}_{\text{pattern}}\) the conduction matrix from the Lab act below (same tridiagonal pattern, different conductivity \(k_t\)), and suppose thermal strain loads displacement through \(\mathbf{f}_u = \alpha E A \,\mathbf{G}\,\mathbf{T}\) with thermal expansion coefficient \(\alpha\) and a coupling matrix \(\mathbf{G}\) (discrete version of integrating \(\alpha T'\) against test functions). Joule heating enters as \(\mathbf{f}_T = \mathbf{j}\), a nodal heat source from current density.

For copper at room temperature, \(\alpha \approx 17 \times 10^{-6}\,\text{K}^{-1}\), \(E = 120\,\text{GPa}\), \(k_t = 400\,\text{W/(m·K)}\). With \(\Delta T = 50\,\text{K}\) above ambient at mid-span and fixed ends, the thermal strain contribution to end reaction is order \(\alpha E A \Delta T \approx 100\,\text{N}\) — small compared to the kilonewton grip loads of Act III, but not negligible for precision metrology. The block system makes the coupling **explicit**: you cannot solve for \(\mathbf{u}\) with a frozen temperature field unless \(\mathbf{K}_{uT}\) and the updated \(\mathbf{f}_u\) are intentionally neglected.

**Partitioned vs monolithic solve.** Engineering codes often use a **staggered** loop that Part V later names Picard iteration for conjugate heat transfer:

1. Solve \(\mathbf{K}_{TT}\mathbf{T} = \mathbf{f}_T(\mathbf{u})\) for temperature (FEM conduction in Part IV).
2. Update \(\mathbf{f}_u \leftarrow \mathbf{f}_u^{\text{mech}} + \mathbf{K}_{uT}\mathbf{T}\) (thermal strain and modulus shift).
3. Solve \(\mathbf{K}_{uu}\mathbf{u} = \mathbf{f}_u\) for displacement.
4. Repeat until \(\|\mathbf{T}^{k+1} - \mathbf{T}^k\|\) and \(\|\mathbf{u}^{k+1} - \mathbf{u}^k\|\) fall below tolerance.

Each step is the \(\mathbf{K}\mathbf{x}=\mathbf{b}\) grammar from Part I; the **story** is that two fields share one specimen. Part V's FVM–FEM conjugate heat transfer example is the same loop with a fluid mesh supplying \(\mathbf{f}_T\) at the wire surface through convection fluxes. Recognizing the block structure early prevents treating CHT as a special CFD trick — it is coupled linear algebra with different meshes on each block row.

| Coupling level | Part I preview | Where the book develops it |
|----------------|----------------|----------------------------|
| Co-located 1D bar + conduction | Block \((3+3) \times (3+3)\) system | Lab act below; Part III heat weak form |
| Staggered Picard | Two solves per iteration | Part V.4 Navier–Stokes + FEM wall |
| Monolithic Newton | Single tangent for \(\partial(\mathbf{R}_u,\mathbf{R}_T)/\partial(\mathbf{u},\mathbf{T})\) | Part VI nonlinear thermoelasticity |

When the block matrix feels abstract, return to the lab: Act II switches on current (\(\mathbf{f}_T\)), Act III ramps displacement (\(\mathbf{f}_u\)), and Act V adds air cooling at the surface (boundary flux into \(\mathbf{f}_T\)). Part I names the algebraic skeleton those acts share.

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

## Lab act: thermocouples converge to a temperature field

Return to the heated copper wire from the opening scene. Steady one-dimensional conduction along the axis (no Joule heating yet — that is Act II in Part VI) satisfies \(-k T''(x) = 0\) with \(T(0) = T_L\) and \(T(L) = T_R\). The exact solution is the linear profile \(T(x) = T_L + (T_R - T_L)\, x/L\).

**Step 1 — discretize with finite differences.** Place \(N\) nodes at \(x_i = i h\) with \(h = L/(N-1)\). The discrete equations are the tridiagonal system \(\mathbf{K}_T \mathbf{T} = \mathbf{b}\) with \(K_{ii} = 2k/h\), \(K_{i,i\pm1} = -k/h\), and Dirichlet rows replacing the first and last equations. This is the same tridiagonal pattern as the bar stiffness in [I.2](02-linear-maps.md) — heat and mechanics share assembly grammar.

**Step 2 — refine and watch the profile stop changing.** With \(T_L = 100\,^\circ\text{C}\), \(T_R = 25\,^\circ\text{C}\), \(L = 0.5\,\text{m}\), and \(k = 400\,\text{W/(m·K)}\) for copper, solve for \(N = 3, 5, 11, 21\). Plot \(T_i\) versus \(x_i\): the broken line segments straighten toward the same linear graph. The nodal values are not converging to a **longer** vector; they are converging to a **function** \(T(x)\).

**Step 3 — read the inner product.** The discrete energy \(\mathbf{T}^T \mathbf{K}_T \mathbf{T}\) approximates \(k \int_0^L (T')^2 \, dx\) — the same "energy norm" Part II will name for \(H^1\). Refining the mesh reduces the gap between discrete and continuum energy; that gap is the FEM error Part IV bounds with Céa's lemma.

| \(N\) | Max error \(\max_i |T(x_i) - T_{\text{exact}}(x_i)|\) | Story beat |
|-------|-------------------------------------|------------|
| 3 | \(\sim 0\) (exact on linear profile for linear elements) | Three thermocouples suffice for this simple field |
| 5 | still \(\sim 0\) for linear \(T(x)\) | More sensors, same answer — redundancy, not new physics |
| 11+ | machine precision | The limit object is the function, not the vector length |

**Step 4 — connect to the lab session.** Act II (Part VI) adds Joule heating \(\dot{q}(x)\) and makes \(T(x)\) nonlinear; Act I's mounting (Part I) already placed the first thermocouple at the grip. This exercise shows why Part II must exist: without a named space for \(T(x)\), mesh refinement is "more numbers" with no convergence target. When the profile stops changing as \(N\) grows, you have found the continuum state variable the prologue promised.

## Scale-boundary handshake: displacement convergence toward \(H^1\)

The thermocouple Lab act above treated **temperature** — a scalar field whose continuum limit is clear once nodal values stabilize. **Displacement** under end load tells the same story with a richer norm: the copper wire in Act III stretches along its axis, and mesh refinement must converge not only in pointwise elongation but in **strain energy**, the quantity Part II will name \(\|u\|_{H^1}\).

Return to the fixed–free bar from [I.1](01-vectors-matrices.md): unit load at the free end, \(EA = 120\,\text{kN}\), \(L = 1\,\text{m}\). The exact continuum solution is linear, \(u(x) = x/L\), with constant strain \(u' = 1/L\). Discretize with \(N\) nodes and linear bar elements; solve \(\mathbf{K}_N \mathbf{u}_N = \mathbf{f}\).

### Discrete energy versus continuum energy

For piecewise-linear \(u_h\) on a uniform mesh with spacing \(h = L/(N-1)\), the **discrete strain-energy proxy** is

\[
E_h = \frac{1}{2}\, \mathbf{u}_N^T \mathbf{K}_N \mathbf{u}_N
= \frac{EA}{2L^2} \sum_{e=1}^{N-1} h\, (\Delta u_e)^2,
\]

where \(\Delta u_e\) is the element elongation. For linear \(u(x) = x/L\), **P1 elements reproduce the exact solution on every mesh** — the discrete profile is exact at nodes, and \(E_h = EA/(2L)\) for all \(N \ge 2\). That is the happy case: refinement changes nothing because the trial space already contains the truth.

Now introduce a **nonlinear manufactured test** that P1 cannot represent exactly: impose a body force \(f(x) = \sin(\pi x/L)\) with fixed ends \(u(0) = u(L) = 0\). The strong solution is

\[
u(x) = \frac{L^2}{\pi^2 E A}\, \sin\!\left(\frac{\pi x}{L}\right),
\qquad
\|u'\|_{L^2}^2 = \frac{L^3}{2\pi^2 E^2 A^2}.
\]

Assemble \(\mathbf{K}_N \mathbf{u}_N = \mathbf{f}_N\) with consistent nodal loads from \(f(x)\). Track two scalars as \(N\) grows:

| \(N\) | \(h\) (m) | \(\max_i |u_h(x_i) - u(x_i)|\) | Relative energy error \(|E_h - E_{\text{exact}}|/E_{\text{exact}}\) |
|-------|-----------|--------------------------------------|---------------------------------------------------------------------|
| 5 | 0.250 | \(\mathcal{O}(h^2)\) | \(\mathcal{O}(h^2)\) |
| 11 | 0.100 | decreases | decreases |
| 21 | 0.050 | decreases | decreases |
| 41 | 0.025 | \(\sim 0.1\%\) | \(\sim 0.1\%\) |

The energy error is the discrete face of \(\|u - u_h\|_{H^1}\): Part II.2's hat-function exercise showed that **kinks** dominate the \(H^1\) seminorm; here the trial space is smooth enough that convergence is second-order in \(L^2\) and first-order in energy for P1 — the rates Part IV.5 will prove as Céa's lemma.

### What crosses the boundary to Part II

Part I can compute tables; Part II names the **target**:

| Part I artifact | Part II name | Part IV consumer |
|-----------------|--------------|------------------|
| \(\mathbf{u}_N^T \mathbf{K}_N \mathbf{u}_N\) | Bilinear form \(a(u_h, u_h) = \int (EA) (u_h')^2 \, dx\) | Element stiffness assembly |
| \(\max_i |u_h(x_i) - u(x_i)|\) | \(L^\infty\) or nodal sampling of \(H^1\) error | Post-processing only — misleading alone |
| Energy error vs \(h\) | \(\|u - u_h\|_{H^1} \to 0\) as \(h \to 0\) | Mesh refinement certificate |
| \(\mathbf{K}_N \to \infty\) | Operator \(K u = -(EA u')'\) on \(H^1_0\) | Weak form in Part III.2 |

**What breaks without the handshake.** Refining a mesh while watching only maximum nodal displacement can declare "converged" when strain energy is still 5% high — the wire plot looks smooth, but Act III's load cell prediction is wrong. Conversely, chasing energy convergence without checking boundary conditions (slip in the grip adds effective compliance) refines toward the wrong limit operator. The handshake is: **track energy and displacement together; name the continuum operator the matrix approximates.**

### Python sketch (manufactured solution)

```python
import numpy as np

def bar_energy_error(N, L=1.0, EA=120e3):
    h = L / (N - 1)
    K = (EA / h) * (np.diag(2*np.ones(N)) - np.diag(np.ones(N-1),1) - np.diag(np.ones(N-1),-1))
    K[0,0] = K[-1,-1] = EA/h  # fixed ends
    x = np.linspace(0, L, N)
    f = np.sin(np.pi * x / L)
    f[0] = f[-1] = 0
    f_nodal = f * h  # consistent load vector (trapezoidal lump)
    u_h = np.linalg.solve(K, f_nodal)
    E_h = 0.5 * u_h @ K @ u_h
    u_exact = (L**2 / (np.pi**2 * EA)) * np.sin(np.pi * x / L)
    E_exact = 0.5 * EA * np.trapz(np.gradient(u_exact, x)**2, x)
    return np.max(np.abs(u_h - u_exact)), abs(E_h - E_exact) / E_exact

for N in [5, 11, 21, 41, 81]:
    err_u, err_E = bar_energy_error(N)
    print(f"N={N:3d}  max|u| err={err_u:.2e}  rel energy err={err_E:.2e}")
```

Run the loop before opening Part II: when both errors fall predictably with \(h\), you have evidence that \(\mathbf{K}_N\) is approximating an operator on a function space, not merely returning a longer vector. Part II supplies the completeness theorem that makes the limit honest; Part III writes the weak form of \(-(EA u')' = f\); Part IV assembles the same \(\mathbf{K}_N\) from shape functions. The copper wire's Act III ramp inherits every row of the handshake table above.

## Concept map checkpoint (Part I)

Part I opened with the four questions the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) later formalize for infinite dimensions. Before leaving \(\mathbb{R}^N\), summarize the grammar every later part inherits:

| Question | Part I answer (copper wire) |
|----------|----------------------------|
| What **object**? | State vector \(\mathbf{u}\), stiffness \(\mathbf{K}\), eigenmodes |
| What **structure**? | Inner product (energy), symmetry (reciprocity), sparsity (local coupling) |
| What **theorem**? | Spectral theorem; SPD \(\mathbf{K}\) \(\Rightarrow\) unique equilibrium |
| What **breaks**? | Ill-conditioning; spurious modes; \(N\to\infty\) without a target space |

The wire began as a chain of springs — \(\mathbf{K}\mathbf{u}=\mathbf{f}\) at fixed \(N\). Chapter 4 showed that refining the mesh sends \(N\) without bound and displacements toward a **function** \(u(x)\). Part II names the space that limit lives in; Part III writes the weak PDE; Part IV assembles \(\mathbf{K}\) from shape functions. The matrix was never arbitrary — it was always a finite-dimensional shadow of something larger.

## Bridge to Part II {#bridge-to-part-ii}

Linear algebra taught us to solve \(\mathbf{K}\mathbf{u}=\mathbf{f}\). Mechanics asks us to solve PDEs. The bridge is:

1. Write the PDE in **weak form** (multiply by a test function, integrate by parts).
2. Choose a finite-dimensional subspace \(V_h \subset H^1\).
3. Solve the resulting matrix system.

Steps 1–2 require function spaces. Part II supplies normed spaces, completeness, Hilbert space structure, and compactness — the vocabulary for existence, uniqueness, and convergence. Part III writes the weak forms for Poisson, heat, and elasticity that Part IV discretizes.

| What Part I established at finite \(N\) | What Part II will name |
|----------------------------------------|------------------------|
| \(\mathbf{u}_N^T \mathbf{K}_N \mathbf{u}_N\) | Bilinear form \(a(u,u)\) on \(H^1\) |
| Mesh refinement: \(N\to\infty\) | Completeness; limit field \(u(x)\in V\) |
| Energy error vs \(h\) | \(\|u-u_h\|_{H^1}\to 0\); Céa's lemma preview |
| Eigenvalue accumulation | Spectral problem for elliptic operators |
| Three-node → million-node solve | Galerkin projection \(u_h\in V_h\subset H^1\) |

**Scale-boundary handshake (I.4 → Part II → Part III).** {#scale-boundary-handshake-i4-to-part-ii}

| Part I export (this chapter) | Functional analysis consumer (Part II) | PDE consumer (Part III) | Failure mode |
|------------------------------|----------------------------------------|-------------------------|--------------|
| \(\mathbf{K}_N \mathbf{u}_N = \mathbf{f}_N\) | Operator \(K: H^1_0\to H^{-1}\) | Weak form \(-(EA u')' = f\) | Refining mesh without convergence target |
| Energy \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | Coercive bilinear form \(a(u,v)\) | Lax–Milgram existence | Nodal displacement "converged" but energy 5% high |
| Thermocouple profile \(T(x)\) | \(T\in H^1\); \(\|T\|_{H^1}\) energy norm | Steady heat \(-kT''=q\) weak form | Strong form at reentrant corners |
| Manufactured-solution energy error | Completeness of \(H^1\) | Sobolev embedding preview | Slip in grip → wrong limit operator |
| [Bridge to Part II](#bridge-to-part-ii) ascent gate | [II.1 motivation](../part02-functional-analysis/01-motivation.md) | [III.2 weak form](../part03-pdes/02-weak-form.md) | Treating \(N\to\infty\) as "bigger vector" |

The displacement-convergence and thermocouple Lab acts above are the operational version of this handshake: track energy and displacement together; name the continuum operator the matrix approximates. Part II's [Closing the arc from Part I](../part02-functional-analysis/00-opening.md#closing-the-arc-from-part-i) recasts the same four questions from the prologue in \(H^1\) and \(L^2\). The [preface ascent continuity hinge](../preface.md#ascent-continuity-hinges) marks this Bridge as the first mandatory pause in row 17's straight read — recite the [plot spine one line](#plot-spine-one-line) aloud before opening Part II.

The [prologue](../prologue/00-many-scales.md) named the weak form a **recurring character** — it will return as Galerkin assembly in Part IV, virtual work in Part VI, and a variational statement on electron density in Part IX. Part I could not give that character a stage: at fixed \(N\), equilibrium is \(\mathbf{K}\mathbf{u}=\mathbf{f}\), not integration by parts. Chapter 4 showed why refinement sends \(N\) without bound and why the limit object is a **function**, not a longer vector. Part II opens with [**Closing the arc from Part I**](../part02-functional-analysis/00-opening.md#closing-the-arc-from-part-i) — the same four questions from the prologue, now in \(H^1\) and \(L^2\) — and builds the room the weak form will speak in.

Turn the page. We leave the comfort of \(\mathbb{R}^N\) and enter the space of admissible fields. The copper wire’s temperature and displacement live there; our meshes are finite-dimensional shadows of those fields, and the shadow improves as \(h \to 0\).
