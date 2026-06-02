# Eigenvalues: Modes That Decouple Complexity

Coupled systems look complicated until we find the right coordinates. Eigenvalue analysis is the search for those coordinates — directions in which a linear map acts by pure scaling.

## The eigenvalue problem

For \(\mathbf{A} \in \mathbb{R}^{n \times n}\), a nonzero vector \(\mathbf{v}\) is an **eigenvector** with **eigenvalue** \(\lambda\) if

\[
\mathbf{A}\mathbf{v} = \lambda \mathbf{v}.
\]

The **spectrum** is the set of all eigenvalues. For symmetric \(\mathbf{A}\), eigenvalues are real, eigenvectors for distinct eigenvalues are orthogonal, and

\[
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^T
\]

with \(\mathbf{V}\) orthogonal and \(\boldsymbol{\Lambda}\) diagonal.

## Physical meaning: normal modes

Consider undamped free vibration:

\[
\mathbf{M}\ddot{\mathbf{u}} + \mathbf{K}\mathbf{u} = \mathbf{0}.
\]

Seek solutions \(\mathbf{u}(t) = \mathbf{v}\, e^{i\omega t}\). This yields the **generalized eigenvalue problem**

\[
\mathbf{K}\mathbf{v} = \omega^2 \mathbf{M}\mathbf{v}.
\]

Each eigenvector \(\mathbf{v}\) is a **normal mode**: a pattern that oscillates at a single frequency \(\omega\). Superposition of modes decouples the dynamics. In practice, we compute only the lowest modes — the ones that matter for resonance and buckling.

## Stability and time integration

For explicit time stepping of \(\dot{\mathbf{u}} = \mathbf{A}\mathbf{u}\), stability requires the spectral radius \(\rho(\mathbf{A})\) to lie inside a stability region. Eigenvalues of the spatial discretization therefore dictate the maximum time step — a recurring theme from heat conduction to molecular dynamics.

For the model problem \(u_t = \alpha u_{xx}\) with second-order central differences, the amplification factor for mode \(k\) involves

\[
\lambda_k \sim -\frac{4\alpha}{\Delta x^2}\sin^2\!\left(\frac{k\Delta x}{2}\right).
\]

Stability constraints (CFL conditions) are eigenvalue constraints in disguise.

## Condition number and solver quality

The **condition number** \(\kappa(\mathbf{A}) = |\lambda_{\max}|/|\lambda_{\min}|\) (for symmetric positive definite \(\mathbf{A}\)) measures sensitivity of \(\mathbf{A}\mathbf{x}=\mathbf{b}\) to perturbations. Ill-conditioned stiffness matrices — nearly rigid modes coupled with soft ones — make direct and iterative solvers struggle. Preconditioners re-scale the spectrum to cluster eigenvalues.

## Rayleigh quotients and variational character

For symmetric \(\mathbf{K}\), the smallest eigenvalue satisfies

\[
\lambda_{\min} = \min_{\mathbf{v}\neq \mathbf{0}} \frac{\mathbf{v}^T \mathbf{K}\mathbf{v}}{\mathbf{v}^T \mathbf{v}}.
\]

This **Rayleigh quotient** is the discrete version of characterizing eigenvalues through energy minimization. In Part II, the Rayleigh quotient generalizes to operators on Hilbert spaces; in Part IV, it underpins a posteriori error estimation.

## From discrete modes to continuous spectra

On a fixed mesh, there are finitely many eigenvalues. As the mesh refines, they approximate the spectrum of a differential operator. For the Laplacian on a bounded domain with Dirichlet conditions, eigenvalues accumulate toward infinity; the corresponding eigenfunctions become oscillatory.

This limit — finite matrices approximating infinite operators — is the hinge between Part I and Part II. We have been working with \(\mathbb{R}^N\). Mechanics wants function spaces. The next chapter takes the first step up.
