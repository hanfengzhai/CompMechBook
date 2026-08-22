# The Method of Weighted Residuals

Return to the copper wire from the prologue. At the engineering scale we want its temperature under Joule heating, or its displacement under tension — fields governed by elliptic PDEs. Part III showed how to weaken those PDEs: multiply by a test function, integrate by parts, and obtain a bilinear form. Part IV asks the operational question: *how do we approximate the solution on a mesh?*

The answer begins not with triangles and quadrature, but with a family of methods united by one idea. **Weighted residual methods** seek an approximate field \(u_h\) that makes the PDE residual small in a weighted average sense. The finite element method is the most important member of that family — Galerkin's method on a piecewise-polynomial space — but understanding the family clarifies why FEM is structured the way it is, and why alternatives (collocation, least squares, Petrov–Galerkin) appear when elliptic intuition fails.

## Scene: a guess that almost works

Joule heating has raised the copper wire's temperature profile above ambient. An analyst guesses a simple shape — perhaps a straight line from hot grip to cool grip — plugs it into the heat equation, and finds the **residual** nonzero everywhere: the guess violates the PDE at almost every point. Weighted residuals ask a softer question: can we adjust the guess so that, when weighted and averaged over the domain, the residual vanishes in a finite number of directions?

Choose three test functions — constants, a linear ramp, a parabola — and demand three weighted integrals of the residual equal zero. Three equations, three unknown coefficients: a miniature finite-dimensional problem already. Galerkin's method chooses the test functions from the same family as the trial space; on a mesh, that family becomes hat functions and the "three equations" become millions. This scene is the birth of FEM: not triangles yet, but the insistence that a good approximate field makes the PDE wrong in a **controlled average sense**, not at every point.

## Residuals: measuring how wrong we are

Consider a differential operator \(\mathcal{L}\) and source term \(f\) on a domain \(\Omega\). The strong-form problem is

\[
\mathcal{L} u = f \quad \text{in } \Omega,
\]

supplemented by boundary conditions. Given any candidate \(u_h\), define the **pointwise residual**

\[
r(x) = f(x) - \mathcal{L} u_h(x).
\]

If \(u_h\) were the exact solution, \(r \equiv 0\). For a nontrivial approximation, \(r \neq 0\) in general. Weighted residual methods do not demand pointwise annihilation — that would require infinitely many degrees of freedom. Instead they require

\[
\int_\Omega r(x)\, w_i(x)\, d\Omega = 0, \qquad i = 1,\ldots,N,
\]

for a chosen set of **weight functions** (or **test functions**) \(\{w_i\}\). Each equation is one scalar constraint. With \(N\) unknown coefficients in \(u_h\), we need \(N\) independent weights.

This is the discrete shadow of Part II's orthogonality: the error is forced to be "invisible" to a finite set of observers.

### Handshake with Part II.4: loads, projectors, and residuals

[Part II.4](../../part02-functional-analysis/04-operators-duality.md) named two objects weighted residuals inherit without re-deriving them:

| Part II.4 object | Weighted residual form | FEM manifestation |
|------------------|------------------------|-------------------|
| Load functional \(\ell(v)\) | Right-hand side \(\ell(\phi_i)\) in each weighted equation | Nodal forces from \(\int f \phi_i\, dx\) |
| Stiffness operator \(A\) | Bilinear form \(a(u_h, \phi_i)\) on the left | Entries of assembled \(\mathbf{K}\) |
| Galerkin projector \(P_h\) | Residual orthogonal to \(V_h\) | \(u_h\) is best energy fit when \(A\) is self-adjoint |
| Weak* convergence \(\ell_N \to \ell\) | Same limit equations as mesh refines | Load lumping that preserves midspan displacement trend |

The **residual orthogonality** \(\int r\, w_i = 0\) is Galerkin's way of saying the error \(u - u_h\) is invisible to the test space in the energy inner product — the finite-dimensional echo of Part II.3's projection theorem. When the right-hand side is a concentrated grip load, II.4's weak* limit justifies replacing a distributed contact pressure with equivalent nodal forces as the mesh refines; when that replacement fails, the weighted residual equations are solving the **wrong** physics even if assembly is flawless.

Part [IV.2](02-galerkin-assembly.md) automates the scatter; Part [IV.5](05-convergence.md) proves \(P_h u\) tracks \(u\) as \(h \to 0\). This chapter is the hinge: residuals first, then assembly, then convergence — the same order Part II used for operators, then spectra, then weak PDEs.

## The approximation space

Write the approximate solution as

\[
u_h(x) = \sum_{j=1}^{N} U_j \phi_j(x),
\]

where \(\{\phi_j\}\) are **trial functions** — the basis of an approximation space \(V_h\). The coefficients \(U_j\) are the unknowns. In FEM, the \(\phi_j\) are local **shape functions** tied to mesh nodes; in spectral methods they might be global polynomials or Fourier modes.

Substituting \(u_h\) into the residual yields equations linear in the \(U_j\) when \(\mathcal{L}\) is linear. Nonlinear problems linearize inside Newton loops, but the weighted residual structure survives at each iteration.

## Collocation, least squares, Galerkin

The choice of weights defines the method:

| Method | Weights \(w_i\) | Character |
|--------|-----------------|-----------|
| Collocation | \(\delta(x - x_i)\) | Residual zero at points |
| Subdomain | Indicator on subdomains | Residual zero on averages |
| Least squares | \(\partial(r w_i)/\partial U_j\) | Minimize \(\|r\|_{L^2}\) |
| Galerkin | Same as trial \(\phi_i\) | Variational structure |
| Petrov–Galerkin | Different trial and test spaces | Stabilization, advection |

**Collocation** evaluates the strong residual at nodes. It is simple and fast when strong solutions are smooth, but it does not naturally accommodate weak derivatives — a second-order operator applied to a linear finite element field is a delta function at element boundaries, not a square-integrable function.

**Galerkin's method** sets \(w_i = \phi_i\). For a self-adjoint elliptic operator with symmetric bilinear form, Galerkin coincides with the **Rayleigh–Ritz** method from Part III: minimize energy over \(V_h\). That is why industrial solid-mechanics codes are overwhelmingly Galerkin FEM: the stiffness matrix is symmetric positive definite, and the discrete solution is the best energy-norm approximation to the true solution (Céa's lemma, developed in Chapter 5).

**Petrov–Galerkin** uses a test space \(W_h \neq V_h\). Streamline-upwind Petrov–Galerkin (SUPG) for advection–diffusion and the discontinuous Petrov–Galerkin (DPG) framework are modern examples. When the operator is not coercive in the trial space alone, a richer test space restores stability.

## From strong residual to weak residual

For second-order elliptic problems, applying \(\mathcal{L}\) to a piecewise-polynomial \(u_h\) produces distributions, not classical functions. The fix — already derived in Part III — is integration by parts before weighting.

For Poisson's equation \(-\Delta u = f\) with homogeneous Dirichlet data, multiply the strong residual by a test function \(v\) and integrate:

\[
\int_\Omega (-\Delta u_h)\, v \, d\Omega = \int_\Omega f v \, d\Omega.
\]

Integration by parts moves one derivative from \(u_h\) onto \(v\):

\[
\int_\Omega \nabla u_h \cdot \nabla v \, d\Omega = \int_\Omega f v \, d\Omega \quad \forall v \in H^1_0(\Omega).
\]

Define the **weak residual** functional

\[
R_{\text{weak}}(v; u_h) = a(u_h, v) - \ell(v), \qquad a(u,v) = \int_\Omega \nabla u\cdot\nabla v\, d\Omega, \quad \ell(v) = \int_\Omega f v\, d\Omega.
\]

Galerkin's method seeks \(u_h \in V_h\) such that \(R_{\text{weak}}(v; u_h) = 0\) for all \(v \in V_h\). This is the weak form restricted to a finite-dimensional subspace — the starting point of every FEM implementation.

The connection to Part I is immediate: choosing a basis \(\{\phi_i\}\) and enforcing \(R_{\text{weak}}(\phi_i; u_h) = 0\) for each \(i\) produces a linear system \(\mathbf{K}\mathbf{U} = \mathbf{F}\).

## Example: 1D bar with second-order operator

Consider a copper wire segment modeled as a 1D bar in equilibrium. The strong form is

\[
-\frac{d}{dx}\left(EA \frac{du}{dx}\right) = f(x), \qquad 0 < x < L,
\]

with \(u(0) = 0\) and \(EA\, u'(L) = F\). Here \(u\) is axial displacement, \(EA\) is axial stiffness, and \(F\) is an applied end load.

Approximate with piecewise linear functions on a mesh of \(N\) elements. Galerkin's method gives, on each element \([x_a, x_b]\) of length \(h\),

\[
\int_{x_a}^{x_b} EA\, u_h'\, v'\, dx = \int_{x_a}^{x_b} f v\, dx
\]

for all test functions \(v\) in the element's linear space. Assembly over the mesh yields the familiar tridiagonal stiffness — the discrete analog of \(-d/dx(EA\, d/dx)\). The natural boundary condition at \(x = L\) appears as the load term \(\int_{\Gamma_N} F v\, dS\) without any special "boundary element routine." That is the power of the weak form: boundary physics enters through the same integral machinery as body loads.

## Boundary conditions in weighted residual methods

Boundary data split into two classes, inherited from Part III:

**Essential (Dirichlet) conditions** constrain the solution value: \(u = g\) on \(\Gamma_D\). They must be enforced on the trial space — only functions satisfying the constraint are admissible. Implementation strategies include:

- **Elimination**: remove constrained degrees of freedom from the global system.
- **Substitution**: parametrize the solution as \(u_h = g + \tilde{u}_h\) with \(\tilde{u}_h = 0\) on \(\Gamma_D\).
- **Penalty methods**: add \(\alpha \int_{\Gamma_D} (u_h - g)^2\, dS\) to the energy. Large \(\alpha\) approximates the constraint but worsens conditioning.
- **Nitsche's method**: weakly enforce Dirichlet data with a consistent penalty term that preserves optimal convergence without the ill-conditioning of naive penalties.

**Natural (Neumann) conditions** specify flux or traction: \(\partial u / \partial n = h\) or \(\boldsymbol{\sigma}\mathbf{n} = \mathbf{t}\). They enter the weighted residual through boundary integrals produced by integration by parts. No additional enforcement is needed if the weak form is derived correctly — a common source of bugs when programmers add "boundary load vectors" that duplicate terms already in the weak form.

For the copper wire, fixing one end (\(u = 0\)) is essential; applying a tensile force at the free end is natural.

## Weighted residuals for vector problems

Linear elasticity replaces the scalar field \(u\) with displacement \(\mathbf{u}\) and the Laplacian with the divergence of stress. The weighted residual statement becomes: find \(\mathbf{u}_h\) such that

\[
\int_\Omega \boldsymbol{\sigma}(\mathbf{u}_h) : \nabla \mathbf{v}\, d\Omega = \int_\Omega \mathbf{f}\cdot\mathbf{v}\, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{v}\, dS
\]

for all kinematically admissible virtual displacements \(\mathbf{v}\). This is the **principle of virtual work** — the vector-valued weighted residual that every structural FEM code implements. The trial and test spaces are vector-valued versions of the scalar \(H^1\) space from Part III; each component is discretized with scalar shape functions.

## Relation to the teaching pipeline

Stanford ME 335A (and the author's [FEA teaching notes](https://hanfengzhai.github.io/note.html)) walks this pipeline in problem sessions:

1. Formulate the variational problem for a PDE.
2. Clarify the function space of trial and test functions.
3. Discretize with shape functions on a mesh.
4. Assemble local-to-global systems.
5. Study norms and convergence numerically.

Step 1 is weighted residuals in disguise: the variational statement *is* the Galerkin weighted residual of the weak form. Steps 3–4 are Part IV's assembly machinery; step 5 is Chapter 5.

## What Galerkin buys us

For coercive problems, Galerkin FEM delivers:

- **Symmetric positive definite** stiffness matrices (for self-adjoint operators).
- **Best approximation** in the energy norm (Galerkin orthogonality of the error).
- **Patch tests**: if the exact solution is in \(V_h\), the FEM solution is exact.
- **A priori convergence rates** tied to approximation theory in Sobolev spaces (Part III, Chapter 3).

These properties explain why elliptic solid mechanics — the copper wire under tension, a turbine blade under centrifugal load, a heat sink under steady conduction — lives comfortably in the FEM world.

## Lab act: weighted residual on two bar elements (Act III — Pulling)

**Act III** ramps end displacement; the load cell reads reaction force. Weighted residuals are the **orthogonality condition** that turns that ramp into a matrix system before any industrial assembly loop obscures the pattern.

Reuse the three-node bar from [I.1](../part01-linear-algebra/01-vectors-matrices.md): \(L = 1\,\text{m}\), \(EA = 2.4 \times 10^8\,\text{N·m}\), \(u(0)=0\), prescribed \(u(1)=10\,\mu\text{m}\). Discretize with **two linear hat functions** \(\phi_1(x)\) on \([0,0.5]\), \(\phi_2(x)\) on \([0.5,1]\) (standard FEM basis).

Weak form for \(-(EA u')' = 0\):

\[
\int_0^L EA u_h' v' \, dx = 0 \quad \forall v \in V_h.
\]

With \(u_h = U_1 \phi_1 + U_2 \phi_2\) and Galerkin test \(v = \phi_i\):

| Index \(i\) | Residual equation | Physical meaning |
|-------------|-------------------|------------------|
| \(i=1\) | \(K_{11} U_1 + K_{12} U_2 = 0\) | Force balance at interior node |
| \(i=2\) | \(K_{21} U_1 + K_{22} U_2 = F_2\) | Prescribed displacement enters as load |

Element stiffness contributions (each half-meter bar, \(k = EA/L_e\)):

\[
\mathbf{K}^e = k \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Scatter into global \(\mathbf{K}\), apply \(U_1=0\) and \(U_2=10\,\mu\text{m}\) (or eliminate DOF 1), solve for the free unknown — recover the same \(u_2 = 5\,\mu\text{m}\) and reaction \(\approx 1.2\,\text{kN}\) from the Lab act in I.1.

The weighted residual **is** the assembly loop in embryo: for each test function \(\phi_i\), enforce \(\int (EA u_h' \phi_i' - 0)\, dx = 0\). Part IV.2 automates the scatter; Part IV.3 adds quadrature on general elements. When the load cell trace is linear in Act III, every point is this two-equation system with a larger \(\mathbf{K}\).

## Concept map checkpoint (weighted residuals)

This chapter is where Part III's weak form becomes an **operational** approximation rule. Before assembly automates the scatter, summarize what weighted residuals established:

| Question | Part IV answer (copper wire) |
|----------|------------------------------|
| What **object**? | Residual \(r = f - \mathcal{L}u_h\); weak residual \(R_{\text{weak}}(v; u_h)\) |
| What **structure**? | Trial space \(V_h\), test space \(W_h\); Galerkin: \(W_h = V_h\) |
| What **theorem**? | Rayleigh–Ritz equivalence for coercive self-adjoint problems; virtual work for elasticity |
| What **breaks**? | Collocation on non-smooth \(u_h\); Petrov–Galerkin needed for advection; penalty ill-conditioning |

The two-element bar Lab act is Galerkin in miniature: enforce \(\int (EA u_h' \phi_i' - 0)\, dx = 0\) for each hat function. Every industrial FEM code is this orthogonality condition with millions of test directions — the same character Part III introduced as \(a(u,v)=\ell(v)\), now restricted to \(V_h\).

## Bridge

Galerkin's method on a finite element space becomes a matrix system through **global assembly** — loop over elements, compute local stiffness and load vectors, scatter into a global sparse matrix. That algorithm, identical in academic Matlab scripts and in industrial solvers processing millions of elements, is the subject of the next chapter.

| What IV.1 (weighted residuals) established | What IV.2 (assembly) must compute |
|-------------------------------------------|-----------------------------------|
| Residual \(R_{\text{weak}}(v; u_h)=0\) for all test \(v\) | Local \(\mathbf{K}^e\), \(\mathbf{f}^e\) and scatter into global sparsity |
| Galerkin: trial space = test space | DOF maps, element connectivity, boundary constraints |
| Rayleigh–Ritz equivalence for coercive problems | Same energy minimum as [III.4](../part03-pdes/04-energy-methods.md), now on nodal coefficients |
| Virtual work for scalar Poisson and vector elasticity | Bar/triangle/tet contributions along the copper wire mesh |
| [Part II.4](../part02-functional-analysis/04-operators-duality.md) handshake: loads as dual functionals | \(\ell(\phi_i)\) and \(a(u_h,\phi_i)\) become rows of \(\mathbf{f}\) and \(\mathbf{K}\) |

**Scale-boundary handshake (Parts I–III → IV.1 → IV.2).**

| Upstream quantity | Weighted residual form | Assembly output | Failure mode |
|-------------------|------------------------|-----------------|--------------|
| Part I \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | Galerkin orthogonality on \(V_h\) | Same sparsity pattern at scale | Wrong connectivity scatter |
| Part II energy norm \(\|u\|_a\) | \(R_{\text{weak}}=0 \Leftrightarrow\) energy minimum | SPD \(\mathbf{K}\) when \(a\) is coercive | Petrov–Galerkin without adjoint care |
| Part III \(a(u,v)=\ell(v)\) | Restrict to \(v=\phi_i \in V_h\) | \(\mathbf{K}\mathbf{U}=\mathbf{F}\) | Duplicated Neumann loads |

Recall Part III's closing pipeline: strong PDE → weak form → **energy minimum** (Dirichlet principle) → discrete search on \(V_h\). The [preface ascent continuity hinge](../preface.md#ascent-continuity-hinges) names this as the **well-posedness → assembly** turn — weighted residuals enforce \(R_{\text{weak}}(v; u_h)=0\) for all test \(v\), which is Rayleigh–Ritz minimization on \(V_h\) when \(a\) is symmetric and coercive. The copper wire's tensile equilibrium from [III.4](../part03-pdes/04-energy-methods.md) arrives here as the same \(a(u,v)=\ell(v)\) restricted to piecewise linears; [IV.2](02-galerkin-assembly.md) is how we compute the matrix that minimization demands.

Return to the [prologue](../../prologue/00-many-scales.md): **Act III — Pulling** turns abstract Galerkin orthogonality into numbers the load cell trusts. Part I named \(\mathbf{K}\mathbf{u}=\mathbf{f}\); Part II proved the limit lives in \(H^1\); Part III wrote the bilinear form. The two-element bar Lab act above is assembly in embryo — the stiffness matrix is the Gram matrix of the energy inner product on \(V_h\), not an arbitrary sparse array.

When the weak form is clear but no global matrix exists yet — that is the signal weighted residuals need an assembly loop. Turn the page.
