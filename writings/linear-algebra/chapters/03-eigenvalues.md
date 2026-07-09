# Eigenvalues: Modes That Decouple Complexity

Coupled systems look complicated until we find the right coordinates. Eigenvalue analysis is the search for those coordinates — directions in which a linear map acts by pure scaling.

Clamp one end of the copper wire and pull the other rhythmically: the wire does not respond with a single uniform stretch unless you happen to excite exactly the first mode. In general, different points oscillate out of phase, amplitudes vary along the length, and the motion looks messy in physical coordinates. In **modal coordinates** — the eigenvector basis of the stiffness and mass matrices — each mode oscillates independently at its own frequency. That decoupling is eigenvalue analysis doing its job.

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

## Bridge

We have stayed in finite dimensions: \(\mathbf{A}\mathbf{v} = \lambda \mathbf{v}\), finitely many modes, matrices we can factor. The copper wire's ringing pitches — normal modes of the spring network — live entirely in that world for fixed \(N\). Yet mechanics specifies fields at every point: temperature along the wire, displacement in every direction, pressure in every fluid cell. Refining the mesh adds eigenvalues without bound; their limit is a **spectrum** of a differential operator, not a longer list in \(\mathbb{R}^N\).

| What I.3 fixed at finite \(N\) | What I.4 + Part II take to the limit |
|-------------------------------|--------------------------------------|
| Modal coordinates decouple \(\mathbf{M}\ddot{\mathbf{u}}+\mathbf{K}\mathbf{u}=\mathbf{0}\) | Fields \(u(x)\), \(T(x)\); operators on \(H^1\), \(L^2\) |
| \(\mathbf{K}\mathbf{v}=\omega^2\mathbf{M}\mathbf{v}\), finitely many \(\omega_j\) | Laplacian eigenvalues accumulate; mesh \(\omega_{h,j}\to\omega_j\) as \(h\to 0\) |
| Lanczos on sparse \(\mathbf{K}\) for lowest modes | Spectral theory for elliptic operators (Part II.5 → Part IV.5) |
| Resonance diagnosis on the wire fixture | Same decoupling picture at atomistic scales (Part VIII) |

The [prologue](../../prologue/00-many-scales.md) introduced the specimen as one ladder with many rungs; eigenmodes are the **first time decoupling appears** in the book — a preview of orthogonality in Hilbert space and of dominant modes in molecular dynamics. [I.2](02-linear-maps.md) showed change of coordinates; eigenvectors are the coordinates in which the stiffness map acts by pure scaling.

The next chapter takes the first step from \(\mathbb{R}^N\) toward function spaces: inner products become integrals, matrices become operators, and the eigenvalue problem becomes a spectral problem for differential operators. Part II makes that transition rigorous; Part III writes down the PDEs those operators encode.

Turn the page when the wire's modes outgrow any fixed mesh count — that is the signal that vectors are no longer enough.
