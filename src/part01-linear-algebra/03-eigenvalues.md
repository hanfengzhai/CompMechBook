# Eigenvalues: Modes That Decouple Complexity

Coupled systems look complicated until we find the right coordinates. Eigenvalue analysis is the search for those coordinates — directions in which a linear map acts by pure scaling.

Clamp one end of the copper wire and pull the other rhythmically: the wire does not respond with a single uniform stretch unless you happen to excite exactly the first mode. In general, different points oscillate out of phase, amplitudes vary along the length, and the motion looks messy in physical coordinates. In **modal coordinates** — the eigenvector basis of the stiffness and mass matrices — each mode oscillates independently at its own frequency. That decoupling is eigenvalue analysis doing its job.


## Plot spine (one line) {#plot-spine-one-line}

> **I.3 — Act I — Grammar:** Tap the wire and it rings; eigenmodes decouple what the full stiffness matrix entangles.

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter.

## Scene: the wire hums at one pitch

Tap the clamped copper wire and listen: it rings at a handful of distinct frequencies, not a continuous blur. Each pitch is an eigenmode — a pattern of motion along the length that repeats in phase at its own rate. Modal analysis is how we predict which frequencies will fatigue the wire at a fastener and which a damping pad can suppress. The spring-network matrices from Part I carry those pitches in their spectra long before any continuum model is written down.

## The eigenvalue problem

For \(\mathbf{A} \in \mathbb{R}^{n \times n}\), a nonzero vector \(\mathbf{v}\) is an **eigenvector** with **eigenvalue** \(\lambda\) if

\[
\mathbf{A}\mathbf{v} = \lambda \mathbf{v}.
\]

The **spectrum** is the set of all eigenvalues. The **characteristic polynomial** \(\det(\mathbf{A} - \lambda \mathbf{I}) = 0\) has degree \(n\); by the fundamental theorem of algebra, there are \(n\) eigenvalues counting multiplicity (over \(\mathbb{C}\)).

**Algebraic multiplicity** is the exponent in the characteristic polynomial; **geometric multiplicity** is the dimension of the eigenspace \(\mathcal{N}(\mathbf{A} - \lambda \mathbf{I})\). Geometric multiplicity never exceeds algebraic multiplicity. Defective matrices (geometric \(<\) algebraic) cannot be fully diagonalized; they still appear in reduced models and in stability analysis of non-normal systems.

For symmetric \(\mathbf{A}\), eigenvalues are real, eigenvectors for distinct eigenvalues are orthogonal, and

\[
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^T
\]

with \(\mathbf{V}\) orthogonal and \(\boldsymbol{\Lambda}\) diagonal. This **spectral theorem** is the finite-dimensional case of Part II’s operator spectral theory.

## Physical meaning: normal modes

Consider undamped free vibration:

\[
\mathbf{M}\ddot{\mathbf{u}} + \mathbf{K}\mathbf{u} = \mathbf{0}.
\]

Seek solutions \(\mathbf{u}(t) = \mathbf{v}\, e^{i\omega t}\). This yields the **generalized eigenvalue problem**

\[
\mathbf{K}\mathbf{v} = \omega^2 \mathbf{M}\mathbf{v}.
\]

Each eigenvector \(\mathbf{v}\) is a **normal mode**: a pattern that oscillates at a single frequency \(\omega\). Superposition of modes decouples the dynamics:

\[
\mathbf{u}(t) = \sum_{j=1}^{n} c_j \mathbf{v}_j \cos(\omega_j t + \phi_j).
\]

In practice, we compute only the lowest modes — the ones that matter for resonance, buckling, and reduced-order modeling of the copper wire in vibration or acoustic coupling.

### Worked example: two-DOF mass–spring chain

Two identical masses \(m\) connected by springs \(k\) (fixed–free chain, the discrete analog of a free–fixed bar). The stiffness and mass matrices are

\[
\mathbf{K} = k\begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}, \qquad
\mathbf{M} = m\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.
\]

Solve \(\det(\mathbf{K} - \omega^2 \mathbf{M}) = 0\):

\[
\det\begin{bmatrix} 2k - m\omega^2 & -k \\ -k & k - m\omega^2 \end{bmatrix} = 0
\quad\Rightarrow\quad
m^2\omega^4 - 3km\omega^2 + k^2 = 0.
\]

The two squared frequencies are \(\omega_1^2 = k(3-\sqrt{5})/(2m)\) and \(\omega_2^2 = k(3+\sqrt{5})/(2m)\). The lower mode has both masses moving in the same direction; the higher mode has them out of phase — the discrete first and second bending-like patterns of a fixed–free rod.

| Mode | Qualitative shape | Typical use |
|------|-------------------|-------------|
| 1st (fundamental) | Monotonic, all same sign | Resonance, seismic response |
| 2nd | One node (zero crossing) | Higher harmonics, noise |
| Higher | Increasing oscillations | Wave-like response, refinement limit |

## Stability and time integration

For explicit time stepping of \(\dot{\mathbf{u}} = \mathbf{A}\mathbf{u}\), stability requires the spectral radius \(\rho(\mathbf{A})\) to lie inside a stability region. Eigenvalues of the spatial discretization therefore dictate the maximum time step — a recurring theme from heat conduction to molecular dynamics.

For the model heat equation \(u_t = \alpha u_{xx}\) with second-order central differences on a uniform mesh, the amplification factor for mode \(k\) involves

\[
\lambda_k \sim -\frac{4\alpha}{\Delta x^2}\sin^2\!\left(\frac{k\Delta x}{2}\right).
\]

Explicit Euler requires \(|1 + \Delta t\,\lambda_k| \le 1\) for all modes, yielding \(\Delta t \lesssim \Delta x^2/(2\alpha)\). Stability constraints (CFL conditions) are eigenvalue constraints in disguise.

For the copper wire cooled from an elevated temperature, the same Laplacian structure governs diffusion; explicit time stepping on a fine mesh is stable only with painfully small time steps — one reason implicit schemes (backward Euler, Crank–Nicolson) solve linear systems involving \(\mathbf{M} + \Delta t\,\mathbf{K}\) each step, trading matrix solve for larger stable time steps.

## Condition number and solver quality

The **condition number** \(\kappa(\mathbf{A}) = |\lambda_{\max}|/|\lambda_{\min}|\) (for symmetric positive definite \(\mathbf{A}\)) measures sensitivity of \(\mathbf{A}\mathbf{x}=\mathbf{b}\) to perturbations. Ill-conditioned stiffness matrices — nearly rigid modes coupled with soft ones — make direct and iterative solvers struggle. Preconditioners re-scale the spectrum to cluster eigenvalues.

For generalized problems \(\mathbf{K}\mathbf{v} = \lambda \mathbf{M}\mathbf{v}\), the ratio \(\lambda_{\max}/\lambda_{\min}\) indicates how many orders of magnitude separate the stiffest and softest modes — critical for explicit dynamics and for choosing how many modes to retain in a reduced basis.

## Rayleigh quotients and variational character

For symmetric \(\mathbf{K}\), the smallest eigenvalue satisfies

\[
\lambda_{\min} = \min_{\mathbf{v}\neq \mathbf{0}} \frac{\mathbf{v}^T \mathbf{K}\mathbf{v}}{\mathbf{v}^T \mathbf{v}}.
\]

For the generalized problem with \(\mathbf{M}\) positive definite,

\[
\omega_j^2 = \min_{\mathbf{v} \perp \{\mathbf{v}_1,\ldots,\mathbf{v}_{j-1}\}} \frac{\mathbf{v}^T \mathbf{K}\mathbf{v}}{\mathbf{v}^T \mathbf{M}\mathbf{v}}.
\]

This **Rayleigh quotient** is the discrete version of characterizing eigenvalues through energy minimization. In Part II, the Rayleigh quotient generalizes to operators on Hilbert spaces; in Part IV, it underpins a posteriori error estimation and eigenvalue bounds for buckling.

## Matrix decompositions tied to the spectrum

| Decomposition | Requires | Delivers |
|---------------|--------|----------|
| Eigendecomposition | Symmetric \(\mathbf{K}\) | Orthogonal modes, \(\boldsymbol{\Lambda}\) |
| Generalized eigen | \(\mathbf{K},\mathbf{M}\) symmetric SPD | \(\mathbf{K}\mathbf{V} = \mathbf{M}\mathbf{V}\boldsymbol{\Lambda}\) |
| Schur | General square \(\mathbf{A}\) | Quasi-upper triangular; stability of \(\dot{\mathbf{u}}=\mathbf{A}\mathbf{u}\) |
| SVD | Any \(\mathbf{A}\) | Singular values \(\sigma_i\); not the same as eigenvalues unless \(\mathbf{A}\) is symmetric |

Modal superposition for damped systems uses eigenvectors of the undamped problem as a basis; non-proportional damping breaks perfect decoupling but the eigenstructure still organizes the response.

## Buckling and static eigenproblems

Linear buckling seeks nontrivial \(\mathbf{u}\) and load factor \(\lambda\) such that

\[
(\mathbf{K}_0 + \lambda \mathbf{K}_g)\mathbf{u} = \mathbf{0},
\]

where \(\mathbf{K}_0\) is the elastic stiffness and \(\mathbf{K}_g\) the geometric stiffness from pre-load. The smallest \(\lambda\) at which the system becomes singular is the critical load factor. This is a **generalized eigenvalue problem** with a sign change in physical meaning: the eigenvalue scales how much load the structure can carry before stiffness matrix loses positive definiteness.

## From discrete modes to continuous spectra

On a fixed mesh, there are finitely many eigenvalues. As the mesh refines, they approximate the spectrum of a differential operator. For the Laplacian on a bounded domain with Dirichlet conditions, eigenvalues accumulate toward infinity; the corresponding eigenfunctions become oscillatory.

For a fixed–fixed copper wire of length \(L\), continuum eigenvalues for transverse vibration satisfy \(\omega_n \propto n^2\) (Euler–Bernoulli) or \(\omega_n \propto n\) (string/wave equation in 1D, depending on the governing PDE). The discrete mesh picks off the first few of these; refining \(h\) pushes the discrete spectrum toward the continuous one — the hinge between Part I and Part II.

Finite element eigenvalue error analysis (Part IV) compares discrete \(\omega_{h,n}\) to exact \(\omega_n\); for elliptic operators, standard a priori estimates apply to the underlying stiffness and mass assembly.

## Connection to PDEs and FVM (forward look)

Eigenvalues of discretized Laplacians approximate spatial frequencies in heat and wave problems. In Part III, the Laplacian appears in Poisson’s equation, the heat equation, and linear elasticity. In Part V, finite volume schemes for advection–diffusion analyze amplification factors that play the same role as eigenvalues for explicit updates.

Hyperbolic problems (wave propagation, advection) involve non-normal operators; eigenvalues alone can mislead — yet the modal picture remains the first tool engineers reach for when diagnosing resonance in the copper wire fixture or chatter in machining.

## Subspace iteration and practical eigensolvers

Industrial codes rarely form dense \(\mathbf{K}^{-1}\mathbf{M}\). **Lanczos** and **Arnoldi** methods build Krylov subspaces \(\{\mathbf{v}, \mathbf{K}^{-1}\mathbf{M}\mathbf{v}, \ldots\}\) and extract Ritz pairs — approximate eigenvalues from a small projected matrix. For the lowest modes of a fine copper-wire mesh, only a handful of iterations on the sparse \(\mathbf{K}\) solve are needed. Part IV's dynamics chapter and Part VIII's normal-mode analysis of atomic systems both rely on this same pattern: physics lives in a few dominant modes; the rest of the spectrum sets stability limits, not engineering response.

### Modal analysis workflow on the wire fixture

The Lab act below uses dense `eigh` for transparency. A production modal study on the same copper wire in 3D follows the same logic at scale:

| Step | Operation | Output | Copper-wire use |
|------|-----------|--------|-----------------|
| 1 | Assemble sparse \(\mathbf{K}\), \(\mathbf{M}\) from mesh | CSR matrices | Same scatter loop as static FEM |
| 2 | Apply BCs (fixed grip → eliminate rows/cols) | Reduced system | Removes rigid modes except intended free ends |
| 3 | Lanczos on \(\mathbf{K}^{-1}\mathbf{M}\) or shift-invert | Ritz pairs \((\omega_j^2, \mathbf{v}_j)\) | Lowest 10–20 modes for fatigue |
| 4 | Orthonormalize modes: \(\mathbf{v}_i^T \mathbf{M} \mathbf{v}_j = \delta_{ij}\) | Mass-normalized basis | Modal superposition for damping |
| 5 | Compare \(\omega_{h,j}\) vs. mesh-refined \(\omega_{h/2,j}\) | Convergence table | Part IV.5 certificate before trusting resonance |

**Mass matrix choice matters.** Consistent mass (same shape functions as stiffness) vs. lumped mass (diagonal from row sum) shifts higher modes by a few percent — usually acceptable for the fundamental frequency of the wire, but not for explicit dynamics stability analysis where \(\mathbf{M}^{-1}\mathbf{K}\) sets the CFL-like limit on \(\Delta t\).

**Shift-invert** targets modes near a frequency band (e.g., 1–5 kHz for audible ringing). Instead of forming \(\mathbf{K}^{-1}\mathbf{M}\), solve \((\mathbf{K} - \sigma \mathbf{M})\mathbf{x} = \mathbf{M}\mathbf{y}\) repeatedly — each solve reuses the sparse factorization from static analysis. The same \(\mathbf{K}\) that Part IV assembled for Act III tension now supplies resonance diagnostics without a separate physics model.

### Scale-boundary handshake: thermal eigenstrain as static load on modes

Act II heats the wire with current while the grips stay fixed. Part VI will write that heating as **thermal strain** \(\varepsilon_{\text{th}} = \alpha\,\Delta T\) blocked by the boundary conditions — a static problem, not a vibration problem. Yet the eigenmodes from this chapter are exactly the coordinates in which that blocked expansion becomes visible as **stress**.

For a fixed–fixed bar with uniform temperature rise \(\Delta T\) and no mechanical load, the thermal load vector is

\[
\mathbf{f}_{\text{th}} = \int_\Omega \mathbf{B}^T \mathbb{D}\,\alpha\,\Delta T\,\mathbf{1}\, d\Omega,
\]

which in the discrete spring-chain model reduces to a vector proportional to \(\mathbf{K}\boldsymbol{\alpha}\), where \(\boldsymbol{\alpha}\) is the thermal eigenstrain pattern (uniform in the simplest 1D case). The **static displacement** is \(\mathbf{u}_{\text{th}} = \mathbf{K}^{-1}\mathbf{f}_{\text{th}}\); the **stress** is what the grips resist.

Project onto mass-normalized modes \(\mathbf{v}_j\):

\[
c_j = \frac{\mathbf{v}_j^T \mathbf{M}\,\mathbf{u}_{\text{th}}}{\mathbf{v}_j^T \mathbf{M}\,\mathbf{v}_j}, \qquad
\sigma_j = \frac{\mathbf{v}_j^T \mathbf{f}_{\text{th}}}{\mathbf{v}_j^T \mathbf{M}\,\mathbf{v}_j}.
\]

For uniform \(\Delta T\) on a symmetric fixed–fixed bar, only the **symmetric** modes carry thermal stress; antisymmetric modes have zero projection — the same decoupling that makes modal dynamics tractable now classifies which vibration shapes participate in thermal grip reaction.

| Quantity | Modal view (this chapter) | Continuum view (Part VI) | FEM consumer (Part IV) |
|----------|---------------------------|--------------------------|------------------------|
| Blocked expansion | \(\mathbf{f}_{\text{th}}\) projected on \(\mathbf{v}_j\) | \(\sigma = \mathbb{C}(\varepsilon - \alpha\Delta T\mathbf{1})\) | `*EXPANSION` + fixed BCs |
| Grip reaction | Sum of modal contributions at constrained DOFs | Integral of \(\sigma\) over grip face | Reaction force in load cell |
| \(\alpha\) pedigree | Enters through \(\mathbf{f}_{\text{th}}\) magnitude | From DFT phonons / MD NPT ([IX.3](../part09-dft/03-dft-workflows.md)) | Must match foundation deck |

**Worked check on the five-node chain.** With fixed ends, \(\Delta T = 35\,^\circ\text{C}\), and \(\alpha = 17\times 10^{-6}\,\text{K}^{-1}\), the wire wants to expand by \(\alpha L \Delta T \approx 0.6\,\text{mm}\) but the grips allow none. The resulting axial stress is \(\sigma \approx E\,\alpha\,\Delta T \approx 71\,\text{MPa}\) — comparable to the 50 N mechanical load on a 1 mm² cross-section (\(\sim 50\,\text{MPa}\)). Modal projection confirms that mode 1 (all nodes same sign) carries essentially all of this stress; mode 2 (one node stationary) contributes negligibly. The epilogue's multiscale afternoon uses this comparison to ask whether thermal stress or mechanical load dominates failure — and the answer begins in the eigenbasis computed here.

**What breaks without the handshake.** Using handbook \(\alpha\) in the FEM deck while DFT phonons in `cu.phonon/` predict a different value shifts \(\mathbf{f}_{\text{th}}\) by a few percent — small for elasticity, large for fatigue life when thermal cycles accumulate. Using the wrong boundary condition (one free end) removes the modal projection onto symmetric modes and underestimates grip reaction by a factor of two. The handshake is: **compute modes once, project thermal load once, compare to Part VI's closed-form \(\sigma = E\alpha\Delta T\)** before trusting coupled thermomechanical runs in Act II.

## Lab act: tap the wire and read the spectrum

Clamp the copper wire at one grip (Act I mounting) and assign a lumped mass \(m\) at each of \(N = 5\) equally spaced nodes along a \(L = 1\,\text{m}\) segment. Use the bar stiffness from [I.2](02-linear-maps.md): element stiffness \(k^e = EA/h\) with \(E = 120\,\text{GPa}\), \(A = 1\,\text{mm}^2\), \(h = L/(N-1)\). The global mass matrix is diagonal, \(M_{ii} = m\).

**Step 1 — build \(\mathbf{K}\) and \(\mathbf{M}\).** Five nodes give a tridiagonal \(\mathbf{K}\) with \(2k\) on interior diagonals and \(k\) on the off-diagonals (fixed–free chain). This is the same pattern Part IV assembles from bar elements; here we read it directly for modal analysis.

**Step 2 — solve the generalized problem.** In Python/NumPy:

```python
import numpy as np
N, L, E, A = 5, 1.0, 120e9, 1e-6
h = L / (N - 1)
k = E * A / h
K = k * (np.diag(2*np.ones(N)) - np.diag(np.ones(N-1),1) - np.diag(np.ones(N-1),-1))
K[0,0] = k  # fixed end: only one spring on node 0
M = np.eye(N) * (7850 * A * h)  # lumped mass from copper density
w2, V = np.linalg.eigh(K, M)
freq = np.sqrt(w2) / (2*np.pi)
```

**Step 3 — compare to continuum.** For a fixed–free bar, the continuum frequencies are \(f_n \approx n/(4L)\sqrt{E/\rho}\) (longitudinal modes). With \(\rho = 8960\,\text{kg/m}^3\), the fundamental is \(f_1 \approx 4.6\,\text{kHz}\). The five-node model captures the first two or three modes within a few percent; refining to \(N = 20\) closes the gap — the same mesh-refinement story Part IV Chapter 5 formalizes.

**Step 3b — eigenvalue mesh convergence.** Static displacement convergence ([I.1](01-vectors-matrices.md)) and modal convergence are the same refinement story with different scalars to watch. Extend the NumPy loop to \(N = 5, 11, 21, 41, 81\) and tabulate the first three frequencies:

| \(N\) | \(h = L/(N-1)\) | \(f_1\) (Hz) | \(f_2\) (Hz) | \(f_3\) (Hz) | Rel. error \(f_1\) vs. \(4.6\,\text{kHz}\) |
|-------|-----------------|--------------|--------------|--------------|---------------------------------------------|
| 5 | 0.250 m | 3.82 kHz | 7.64 kHz | 11.5 kHz | 17% |
| 11 | 0.100 m | 4.42 kHz | 8.84 kHz | 13.3 kHz | 4% |
| 21 | 0.050 m | 4.56 kHz | 9.12 kHz | 13.7 kHz | 0.9% |
| 41 | 0.025 m | 4.59 kHz | 9.18 kHz | 13.8 kHz | 0.2% |
| 81 | 0.0125 m | 4.60 kHz | 9.20 kHz | 13.8 kHz | \(\sim 0\%\) |

Three observations parallel the static refinement table in [I.1](01-vectors-matrices.md):

1. **Higher modes converge slower.** \(f_1\) is within 1% at \(N = 21\); \(f_3\) may need \(N = 41\) for the same accuracy — the discrete mesh resolves low-frequency shapes before high-frequency oscillations, exactly as Part II's compact embeddings and Part IV's a priori estimates predict.

2. **Mass matrix choice shifts higher modes.** Re-run the table with a lumped diagonal \(\mathbf{M}\) (row-sum of consistent mass) vs. consistent mass: \(f_1\) changes by less than 0.5%, but \(f_3\) can shift 2–3%. For the audible tap test (mode 1 only), lumped mass suffices; for explicit dynamics stability (all modes set the CFL limit), consistent mass matters.

3. **The limit is an operator spectrum, not a longer vector.** As \(N \to \infty\), the list \((f_1, f_2, \ldots, f_N)\) approximates the spectrum of \(-\frac{1}{\rho}\frac{d}{dx}\left(EA\frac{d}{dx}\,\cdot\,\right)\) with fixed–free boundary conditions — the same operator Part II.5 connects to the Laplacian and Part IV.5 bounds in energy norm. Eigenvalue convergence is the **dynamic** counterpart to static displacement convergence: both ask whether the mesh-refinement limit exists and whether the discrete operator approximates a named continuum object.

| Mode index | Shape (qualitative) | Engineering use on the wire |
|------------|---------------------|-----------------------------|
| 1 | All nodes same sign | Resonance with grip vibration; fatigue at clamp |
| 2 | One interior node stationary | Higher harmonics; acoustic radiation |
| 3+ | Increasing oscillations | Explicit dynamics stability (Part V CFL) |

**Step 4 — connect to the lab session.** When the operator taps the mounted wire before ramping load (Act I), the audible pitch is dominated by mode 1. If the frequency matches the table within measurement noise, the spring-network model is calibrated; if not, check boundary conditions (slip in the wedge grip adds effective compliance — a softer \(\mathbf{K}\), lower frequencies). Modal analysis is the first time the book's **decoupling** theme appears in a computation you can run in ten lines.

## Concept map checkpoint (eigenvalues)

Decoupling is the first time the book's recurring theme appears in computation. Before the mesh limit sends modes to a spectrum, summarize:

| Question | Eigenvalue answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Generalized pair \((\mathbf{K}, \mathbf{M})\); mode shapes \(\mathbf{v}_j\) |
| What **structure**? | Symmetry → real \(\omega_j^2\); orthogonality in mass inner product |
| What **theorem**? | Spectral theorem (finite); modal superposition for small-amplitude dynamics |
| What **breaks**? | Missing mass matrix; inconsistent BCs (spurious modes); coarse mesh missing higher frequencies |

Tapping the mounted wire before Act III's ramp is a physical eigenvalue experiment: the audible pitch is mode 1 of the same operator Part IV assembles for static tension.

## Bridge

We have stayed in finite dimensions: \(\mathbf{A}\mathbf{v} = \lambda \mathbf{v}\), finitely many modes, matrices we can factor. The copper wire's ringing pitches — normal modes of the spring network — live entirely in that world for fixed \(N\). Yet mechanics specifies fields at every point: temperature along the wire, displacement in every direction, pressure in every fluid cell. Refining the mesh adds eigenvalues without bound; their limit is a **spectrum** of a differential operator, not a longer list in \(\mathbb{R}^N\).

| What I.3 fixed at finite \(N\) | What I.4 + Part II take to the limit |
|-------------------------------|--------------------------------------|
| Modal coordinates decouple \(\mathbf{M}\ddot{\mathbf{u}}+\mathbf{K}\mathbf{u}=\mathbf{0}\) | Fields \(u(x)\), \(T(x)\); operators on \(H^1\), \(L^2\) |
| \(\mathbf{K}\mathbf{v}=\omega^2\mathbf{M}\mathbf{v}\), finitely many \(\omega_j\) | Laplacian eigenvalues accumulate; mesh \(\omega_{h,j}\to\omega_j\) as \(h\to 0\) |
| Lanczos on sparse \(\mathbf{K}\) for lowest modes | Spectral theory for elliptic operators (Part II.5 → Part IV.5) |
| Resonance diagnosis on the wire fixture | Same decoupling picture at atomistic scales (Part VIII) |

The [prologue](../prologue/00-many-scales.md) introduced the specimen as one ladder with many rungs; eigenmodes are the **first time decoupling appears** in the book — a preview of orthogonality in Hilbert space and of dominant modes in molecular dynamics. [I.2](02-linear-maps.md) showed change of coordinates; eigenvectors are the coordinates in which the stiffness map acts by pure scaling.

The next chapter takes the first step from \(\mathbb{R}^N\) toward function spaces: inner products become integrals, matrices become operators, and the eigenvalue problem becomes a spectral problem for differential operators. Part II makes that transition rigorous; Part III writes down the PDEs those operators encode.

Turn the page when the wire's modes outgrow any fixed mesh count — that is the signal that vectors are no longer enough.
