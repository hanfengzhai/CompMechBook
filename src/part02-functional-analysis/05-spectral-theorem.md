# Compactness and the Spectral Theorem

[II.4](04-operators-duality.md) named stiffness as a bounded operator, loads as elements of the dual \(H^*\), and weak convergence as the limit behavior norms alone miss — the vocabulary Part III needs when concentrated forces and oscillatory residuals appear at grip corners. This chapter closes Part II by asking what happens when that operator is **self-adjoint and compact**: eigenvalues become real, eigenmodes become orthogonal, and the discrete spectra from Part I's spring network acquire a continuum limit worth trusting.

Eigenvalues decouple finite-dimensional vibration problems. A symmetric stiffness matrix diagonalizes in orthonormal modes; each mode oscillates at its own frequency, independently of the others. The **spectral theorem** for self-adjoint operators on Hilbert spaces is the same story without a fixed matrix size. It governs the normal modes of a copper wire, the buckling loads of a slender column, the diffusion rates of heat along that wire, and the convergence of finite element eigenvalues as the mesh refines. Part II has built the spaces, the inner products, and the compactness that make this theorem true. Here we state it, apply it, and hand the toolkit to Part III.

## Story so far (Prologue & Parts I–II)

| Stage | What the wire became | Key object |
|-------|----------------------|------------|
| Part I | \(\mathbf{K}\mathbf{u}=\mathbf{f}\); eigenmodes decouple vibration | Discrete stiffness and mass matrices |
| [II.1–II.4](01-motivation.md) | Fields \(u(x)\), \(T(x)\) in \(H^1\); operators, duality | Bilinear forms, weak convergence, Galerkin projector |
| **II.5 (here)** | Normal modes of the continuous bar | Self-adjoint compact operators; spectral theorem |

Part I's eigenvalues on the spring chain were a finite-dimensional rehearsal. Part II built the room those modes converge toward as \(h \to 0\). This chapter closes Part II's [**concept map**](00-opening.md#the-concept-map-me-412) with the theorem that certifies modal analysis: real eigenvalues, orthogonal mode shapes, Rayleigh quotients that FEM eigenvalue solvers approximate. Part III will write the PDEs whose eigenfunctions those discrete modes chase.

## Scene: the wire sings

Tap the clamped end of the copper wire with a small impulse and listen — not with your ears, but with an accelerometer and a spectrum analyzer. The time trace looks complicated: many frequencies mixed together, amplitudes changing along the length. Transform to **modal coordinates** — the eigenvector basis of the stiffness and mass matrices from Part I — and the picture simplifies: mode 1 oscillates at \(f_1\), mode 2 at \(f_2\), each shape fixed, each amplitude decoupled from the others. That decoupling is finite-dimensional spectral theory doing its job on a mesh.

Refine the mesh and the spectrum shifts — but not arbitrarily. The lowest modes converge toward the normal modes of the **continuous** bar, governed by a self-adjoint operator on \(H^1\). The spectral theorem is the guarantee that this limit makes sense: real eigenvalues, orthogonal mode shapes, a discrete spectrum accumulating toward a continuous one. Part II closes with this scene because every vibration, buckling, and diffusion problem in Parts III–VI will ask the same question: **what are the modes of the operator**, and do the mesh eigenvalues converge to them?

## Self-adjoint operators

Let \(H\) be a Hilbert space. A bounded linear operator \(A: H \to H\) is **self-adjoint** if

\[
(Au, v) = (u, Av) \quad \forall u, v \in H.
\]

Self-adjoint operators generalize symmetric matrices. Their spectra lie on the real line; their eigenvectors — when they exist — are orthogonal. In mechanics, symmetric stiffness and mass matrices produce real natural frequencies; the continuous analog is self-adjointness of the elasticity operator and of the Laplacian in appropriate weak form.

**Example (Laplacian with Dirichlet BCs).** On \(H = H^1_0(\Omega)\), define \(a(u,v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega\). By Lax–Milgram, for each \(f \in L^2(\Omega)\) there is unique \(u \in H^1_0\) with \(a(u,v) = (f,v)_{L^2}\). The map \(f \mapsto u\) is the **solution operator** for \(-\Delta\) with zero boundary data. Its inverse, in the sense of recovering \(f\) from \(u\) when \(u\) is smooth enough, is the Laplacian. On bounded domains, the eigenvalue problem

\[
a(\phi, v) = \lambda (\phi, v)_{L^2} \quad \forall v \in H^1_0
\]

defines a self-adjoint, positive operator with discrete spectrum \(0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty\).

**Unbounded operators.** The Laplacian is not bounded as a map from all of \(H^1_0\) to \(L^2\); domain issues matter for full rigor. We work through the **forms** associated with self-adjoint operators — the bilinear forms of weak mechanics — and treat the spectral theorem on compact operators and on the natural extensions of elliptic eigenproblems. That level is sufficient for FEM modal analysis and for the heat and wave equations on bounded specimens like the wire.

## Compact self-adjoint operators: the spectral theorem

Compactness, from the previous chapter, distinguishes operators whose spectra behave like finite matrices from pathological infinite-dimensional cases.

**Theorem (Spectral theorem, compact self-adjoint case).** Let \(H\) be a Hilbert space and \(A: H \to H\) be compact and self-adjoint. Then:

1. \(A\) has a **countable** sequence of real eigenvalues \(\{\lambda_n\}\) accumulating only at \(0\). If \(H\) is infinite-dimensional and \(A\) has infinitely many eigenvalues, then \(\lambda_n \to 0\).

2. Each nonzero eigenvalue has **finite-dimensional** eigenspace.

3. Eigenvectors can be chosen **orthonormal** in \(H\). If \(\{\phi_n\}\) is an orthonormal basis of eigenvectors with \(A\phi_n = \lambda_n \phi_n\), then for every \(u \in H\),

\[
Au = \sum_{n=1}^\infty \lambda_n (u, \phi_n) \phi_n.
\]

4. \(A\) is the **limit in operator norm** of finite-rank operators obtained by truncating this sum.

For **inverse** operators — solving \(-\Delta u = f\) rather than applying \(-\Delta\) — eigenvalues grow rather than decay. The Laplacian's inverse on \(L^2\) (restricted to appropriate domains) is compact with eigenvalues \(\mu_n = 1/\lambda_n \to 0\). The spectral picture is the same, with indices reversed.

**Example (fixed-fixed wire).** On \((0,L)\) with \(u(0) = u(L) = 0\), eigenfunctions \(\phi_n(x) = \sqrt{2/L}\sin(n\pi x/L)\) satisfy \(-\phi_n'' = \lambda_n \phi_n\) with \(\lambda_n = (n\pi/L)^2\). High modes oscillate rapidly — visible as mesh-resolved wiggles in FEM eigenvectors when \(h\) is small enough. Low modes dominate long-wavelength bending and low-frequency vibration.

## Rayleigh–Ritz variational characterization

Eigenvalues are not merely roots of a characteristic polynomial; they **minimize Rayleigh quotients**. For the Laplacian eigenvalue problem on \(H^1_0(\Omega)\),

\[
\lambda_n = \min_{\substack{W \subset H^1_0 \\ \dim W = n}} \max_{\substack{0 \ne w \in W}} \frac{a(w,w)}{(w,w)_{L^2}} = \max_{\substack{W \subset H^1_0 \\ \dim W = n}} \min_{\substack{0 \ne w \in W}} \frac{a(w,w)}{(w,w)_{L^2}}.
\]

The first equality is the **max-min** (Courant–Fischer) principle; the second is the dual **min-max** form. The \(n\)-th eigenvalue is the best possible upper bound obtained by maximizing the Rayleigh quotient over \(n\)-dimensional subspaces.

**Finite element eigenvalues** arise by restricting the Rayleigh quotient to \(V_h \subset H^1_0\). If \(V_h\) has dimension \(N\), the discrete problem yields \(N\) eigenvalues \(\lambda_1^{(h)} \le \cdots \le \lambda_N^{(h)}\). For conforming Lagrange elements approximating the standard Laplacian with fixed boundary conditions, **discrete eigenvalues bracket the continuous ones from above** in the standard ordering (for the \(n\)-th eigenvalue, once \(V_h\) is rich enough to capture the corresponding mode):

\[
\lambda_n \le \lambda_n^{(h)}
\]

when the discrete space is conforming and the form is unchanged — a useful sanity check when a coarse mesh **under-estimates** frequencies if misread. Practitioners remember: refining the mesh lowers discrete eigenvalue approximations toward the true values from above for this sign convention on the Laplacian.

**Example.** A coarse mesh on the vibrating wire captures the fundamental mode reasonably but over-estimates \(\lambda_1\); finer meshes reduce the Rayleigh quotient of the discrete first mode until it approaches the analytical \(\pi^2/L^2\). Buckling analysis of a column under compression uses the same Rayleigh–Ritz logic: the critical load is the smallest \(\lambda\) for which a nontrivial equilibrium exists — an eigenvalue of a stiffness–geometry operator.

## Modal expansion and the heat equation

Parabolic problems inherit the elliptic spectral decomposition. For the heat equation on a bounded domain,

\[
\frac{\partial u}{\partial t} - \Delta u = 0 \quad \text{in } \Omega, \qquad u = 0 \quad \text{on } \partial\Omega,
\]

with initial data \(u(x,0) = u_0(x)\), separation of variables yields

\[
u(x,t) = \sum_{n=1}^\infty c_n e^{-\lambda_n t} \phi_n(x),
\]

where \(\{\phi_n\}\) are Laplacian eigenfunctions orthonormal in \(L^2\), \(\lambda_n > 0\), and \(c_n = (u_0, \phi_n)_{L^2}\).

**Physical reading.** High modes — large \(\lambda_n\) — decay rapidly in time. Low modes persist. If the copper wire is heated non-uniformly and then allowed to equilibrate, short-wavelength hot spots diffuse away quickly; the longest-wavelength temperature difference is the last to vanish. Explicit time integrators for parabolic problems must resolve the largest \(\lambda_n\) imposed by mesh spacing — a **stability and stiffness** constraint linking spatial FEM to temporal eigenvalues, familiar from the CFL condition's elliptic cousin.

**Galerkin in time.** A \(p\)-step modal truncation keeps only the first \(p\) modes, producing a diagonal system of ordinary differential equations \(\dot{c}_n = -\lambda_n c_n\). This is exact for the heat equation when \(u_0\) lies in the span of the first \(p\) eigenfunctions; otherwise it is a reduced-order model whose quality depends on how fast \(\lambda_n\) grows and how \(u_0\) distributes across modes.

## The wave equation and oscillatory modes

The second-order wave equation

\[
\frac{\partial^2 u}{\partial t^2} - \Delta u = 0
\]

expands similarly in Laplacian eigenfunctions, with solutions \(\cos(\sqrt{\lambda_n}\, t)\) and \(\sin(\sqrt{\lambda_n}\, t)\) multiplying modal amplitudes. Natural frequencies are \(\omega_n = \sqrt{\lambda_n}\). For the wire fixed at both ends, \(\omega_n = n\pi/L\) in appropriate units — the harmonics of a vibrating string.

FEM with consistent mass matrices approximates these frequencies; lumped mass shifts eigenvalues and can improve explicit time-stepping stability at the cost of spectral accuracy. The spectral theorem explains **what** is being approximated: orthonormal modes of a self-adjoint operator, not arbitrary diagonalizations of a nonsymmetric system.

## Beyond the compact case

Not every operator of interest is compact. The Laplacian on all of \(\mathbb{R}^d\) has continuous spectrum. Unbounded domains and lossy systems require more general spectral theory. For bounded laboratory specimens — wires, beams, plates, machined parts — compact embedding of \(H^1\) into \(L^2\) ensures discrete spectra for standard elliptic eigenproblems, and that is the regime of most FEM vibration and buckling codes.

When defects and dislocations enter in Part VII, spectra become more subtle: continuous bands, localized modes at defects. The compact picture from Part II remains the baseline against which those richer structures are measured.

## Computational checklist

When running modal or transient analysis on a mesh, the spectral viewpoint suggests questions worth asking before trusting output:

1. **Are boundary conditions the same in the eigenproblem and in the physical problem?** Fixed ends impose \(H^1_0\); free ends change the form and the spectrum.

2. **Is the mesh fine enough for the modes of interest?** Each eigenfunction \(\phi_n\) must be approximable in \(V_h\). High modes require small \(h\) or high-order elements.

3. **Does the time integrator resolve \(\max \lambda_n\)?** Explicit schemes for diffusion need \(\Delta t \lesssim C / \lambda_{\max}^{(h)}\).

4. **Are eigenvalues real?** Unexpected complex eigenvalues in a supposedly self-adjoint problem signal inconsistent boundary conditions, unsymmetric assembly, or non-conforming coupling.

## Min-max and physical intuition

The Courant–Fischer characterization has a mechanical reading. To estimate the \(n\)-th eigenvalue from above, guess an \(n\)-dimensional family of kinematically admissible modes and compute the largest Rayleigh quotient in that family. The true \(\lambda_n\) is the **minimum** over all such families of that maximum — you cannot fool the variational principle by a clever subspace choice; the operator picks the optimal one.

For a vibrating wire, the fundamental frequency corresponds to \(\lambda_1\): the smallest nonzero Rayleigh quotient over all nontrivial displacements vanishing at the ends. Higher modes add nodes — points that remain stationary during oscillation — and increase the quotient. A numerical eigenvalue solver on \(V_h\) performs this optimization restricted to mesh functions; convergence as \(h \to 0\) is convergence of those restricted max-min values to the continuous spectrum.

## FEM eigenvalue convergence

For conforming finite elements on the Laplacian eigenproblem, **a priori** error bounds take the form

\[
|\lambda_n - \lambda_n^{(h)}| \le C h^{2k} \|\phi_n\|_{H^{k+1}}
\]

when elements of polynomial order \(k\) approximate an eigenfunction \(\phi_n\) smooth enough. The exponent depends on regularity of \(\phi_n\) and on whether mass matrices are lumped or consistent. Non-conforming elements (Morley plate elements, some discontinuous methods) can still yield spectral convergence but require separate proof techniques.

Practical implication for the copper wire: if the mesh resolves half a wavelength of mode \(n\) with insufficient elements, \(\lambda_n^{(h)}\) is a poor estimate. Adaptive mesh refinement for eigenproblems targets elements where local Rayleigh quotients vary sharply — often near boundaries and constraints.

## Semigroup picture for heat flow

Write the heat equation as an evolution in \(L^2(\Omega)\):

\[
\frac{du}{dt} + A u = 0, \qquad u(0) = u_0,
\]

where \(A\) is the positive self-adjoint operator associated with \(-\Delta\) and Dirichlet boundary conditions. The solution operator \(e^{-tA}\) is a **contraction semigroup** on \(L^2\): \(\|e^{-tA} u_0\|_{L^2} \le \|u_0\|_{L^2}\). Spectral decomposition diagonalizes the semigroup:

\[
e^{-tA} u_0 = \sum_n e^{-\lambda_n t} (u_0, \phi_n) \phi_n.
\]

Each mode decays independently. Numerical schemes — backward Euler, Crank–Nicolson, Runge–Kutta — approximate \(e^{-tA}\) on \(V_h\). Stiffness in time appears when \(\lambda_{\max}^{(h)}\) is large, exactly as explicit Euler requires \(\Delta t \lesssim 2/\lambda_{\max}\) for the model problem \(u' = -\lambda u\).

Cooling of the wire after current shutoff is this semigroup. Hot interior regions dominated by low modes cool slowly; sharp surface transients involving high modes equilibrate quickly if the spatial mesh resolves them.

## Generalized eigenvalue problems in mechanics

Undamped free vibration seeks \((\lambda, \phi)\) with

\[
a(\phi, v) = \lambda \, m(\phi, v) \quad \forall v \in H,
\]

where \(a\) is stiffness and \(m\) is mass — both symmetric, \(a\) coercive, \(m\) positive on \(H\). This is a **generalized** eigenproblem. On \(V_h\), it becomes \(\mathbf{K}\mathbf{V} = \lambda \mathbf{M}\mathbf{V}\). Compactness of the inverse stiffness operator embedded in \(L^2\) yields discrete spectra accumulating to infinity under standard assumptions.

For the wire with non-uniform cross-section, \(a\) and \(m\) vary spatially through elastic modulus and density. The spectral theorem applies to the operator \(\mathbf{M}^{-1}\mathbf{K}\) on the discrete side and to the continuous generalized problem on \(H^1_0\). Orthogonality of modes is with respect to both forms: \(a(\phi_i, \phi_j) = \lambda_i m(\phi_i, \phi_j)\) and \(m(\phi_i, \phi_j) = 0\) for \(i \ne j\) after scaling.

## Concept map checkpoint (Part II)

Part II followed the Functional Analysis Notes concept map chapter by chapter. Before Part III writes weak PDEs, the four questions summarize the whole part:

| Question | Part II answer (copper wire) |
|----------|------------------------------|
| What **object**? | Fields \(u(x)\), \(T(x)\) in \(H^1\) and \(L^2\), not vectors \(\mathbf{u}\in\mathbb{R}^N\) |
| What **structure**? | Norms (energy), inner products (orthogonality), completeness (limits stay inside) |
| What **theorem**? | Lax–Milgram existence; Galerkin best approximation; spectral convergence |
| What **breaks**? | Cauchy sequences leaving the space; corners with no classical \(C^2\) solution |

We now possess, in order:

- **Motivation:** Infinite-dimensional limits arise when mesh size \(h \to 0\); weak forms live in function spaces, not in \(\mathbb{R}^N\).

- **Normed spaces:** Metrics, \(L^p\) and \(H^1\) norms, Cauchy sequences, Banach completeness, Poincaré's inequality.

- **Hilbert spaces:** Inner products, best approximation, Riesz representation, Galerkin orthogonality, Céa's lemma.

- **Operators and duality:** Bounded maps, dual loads, weak convergence, compact embeddings, the Galerkin projector.

- **Spectral theory:** Self-adjoint compact operators, Rayleigh–Ritz quotients, modal expansions for heat and wave.

The copper wire at continuum scale is now a mathematical object: displacement and temperature in Sobolev spaces, loads in duals, stiffness as a bilinear form, vibration as eigenvalues of a self-adjoint operator. Part III applies this toolkit to Poisson, heat, and elasticity; Part IV discretizes the resulting weak forms.

## Bridge

Part III applies this toolkit to **partial differential equations** directly. We will write strong forms for physical intuition — what the PDE says at each point — and weak forms for computation — what the FEM assembles. Sobolev spaces supply the regularity theory; energy methods package existence and uniqueness as minimization. The finite element method of Part IV stands at the end of that road, but the road begins with the first weak formulation of Poisson's equation and the function spaces we have spent Part II learning to trust.

| What Part II supplied | What Part III opens |
|-----------------------|---------------------|
| \(H^1\), \(L^2\), completeness | Domains \(\Omega\) where fields live |
| Bilinear forms \(a(u,v)\); dual loads \(\ell\) | Weak forms \(a(u,v)=\ell(v)\) for Poisson, heat, elasticity |
| Lax–Milgram and spectral convergence | Energy methods that package existence as minimization |
| Galerkin best approximation on \(V_h\) | The equations Parts IV and V will discretize |
| [II.5 checkpoint](#concept-map-checkpoint-part-ii) | [III opening](../part03-pdes/00-opening.md#closing-the-arc-from-part-ii) **Closing the arc from Part II** |

The [prologue](../../prologue/00-many-scales.md) named the weak form a **recurring character** — born here as integration by parts, destined to become Galerkin assembly in Part IV, virtual work in Part VI, and a variational statement on electron density in Part IX. Part II built the room that character speaks in: \(H^1\) for admissible fields, dual spaces for concentrated loads, compact embeddings so Galerkin projections have targets. Part III is the act where the character first has lines on stage: multiply by a test function, integrate by parts, and ask whether internal and external virtual work balance for every admissible virtual displacement. The copper wire at the grip corner — where Part III opens — is where that character stops pretending every field is \(C^2\).

| Prologue act | Spectral object on the wire | Part II theorem that certifies it |
|--------------|----------------------------|-----------------------------------|
| II — Warming | Thermal modes of the 1D rod; decay rates of Fourier harmonics | Self-adjoint heat operator; Rayleigh quotients for \(T(x)\) |
| III — Pulling | Axial vibration modes before plasticity | Stiffness operator on \(H^1_0\); Galerkin eigenvalue convergence |
| VI — Foundation (preview) | Phonon frequencies feeding MD and elasticity | Same eigenvalue loop, now on atomic cells from Part IX |

Part I's discrete eigenmodes on the spring chain were the finite-dimensional rehearsal of this chapter's spectral theorem. Part III will write the PDEs whose eigenfunctions those modes approximate as \(h \to 0\). Turn the page when modal analysis on a mesh still feels like linear algebra with extra steps — strong forms first: what the blackboard demands at every point, and where that demand breaks.

| Part II chapter | Operator vocabulary on the wire | Part III chapter that uses it |
|-----------------|--------------------------------|------------------------------|
| II.2 Normed spaces | \(\|u\|_{H^1}\), completeness | III.3 Sobolev spaces |
| II.3 Hilbert spaces | Lax–Milgram, Galerkin orthogonality | III.2 Weak form, III.4 Energy methods |
| II.4 Operators/duality | Dual loads, weak convergence | III.2 Point forces as \(\ell \in H^{-1}\) |
| II.5 Spectral theorem (here) | Normal modes, Rayleigh quotients | III.1 Heat/wave eigenstructure |
