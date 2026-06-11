# Eigenvalues and spectral decomposition

## Definition and meaning

For \(\mathbf{A} \in \mathbb{R}^{n \times n}\), a nonzero vector \(\mathbf{v}\) is an **eigenvector** with **eigenvalue** \(\lambda\) if

\[
\mathbf{A}\mathbf{v} = \lambda \mathbf{v}.
\]

**Mechanics reading.** Eigenvectors are patterns that the operator preserves up to scaling. Eigenvalues tell you how strongly each pattern is amplified or damped.

Examples:

- **Vibration:** \(\mathbf{K}\mathbf{x} = \omega^2 \mathbf{M}\mathbf{x}\) — squared natural frequencies on the diagonal after simultaneous diagonalization.
- **Stability:** eigenvalues of a Jacobian determine whether a time-stepping scheme grows perturbations.
- **Stress:** principal stresses are eigenvalues of the symmetric Cauchy stress tensor.

## Symmetric matrices

If \(\mathbf{A} = \mathbf{A}^\top\), then:

1. All eigenvalues are real.
2. Eigenvectors for distinct eigenvalues are orthogonal.
3. \(\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^\top\) with orthogonal \(\mathbf{Q}\) and diagonal \(\mathbf{\Lambda}\).

This is the **spectral theorem**—the finite-dimensional version of expanding operators in orthonormal modes.

## Generalized eigenvalue problems

In FEM dynamics,

\[
\mathbf{K}\mathbf{u} = \lambda \mathbf{M}\mathbf{u},
\]

with \(\mathbf{K}\) stiffness and \(\mathbf{M}\) consistent mass. If \(\mathbf{M}\) is PD, we reduce to standard form:

\[
\mathbf{M}^{-1/2}\mathbf{K}\mathbf{M}^{-1/2} \tilde{\mathbf{u}} = \lambda \tilde{\mathbf{u}}.
\]

Lowest modes approximate physical resonance; high modes are mesh-dependent noise unless resolved with sufficient elements.

## Condition number and numerics

The **condition number**

\[
\kappa(\mathbf{A}) = \|\mathbf{A}\|\,\|\mathbf{A}^{-1}\|
\]

(measured in a chosen norm) bounds sensitivity of \(\mathbf{A}\mathbf{x} = \mathbf{b}\) to perturbations. Ill-conditioned stiffness matrices arise from:

- nearly incompressible materials (locking),
- thin structures,
- poorly scaled units.

Preconditioners and mixed formulations are engineering responses to bad spectra.

## Rayleigh quotient

For symmetric \(\mathbf{A}\),

\[
R(\mathbf{x}) = \frac{\mathbf{x}^\top \mathbf{A}\mathbf{x}}{\mathbf{x}^\top \mathbf{x}}
\]

satisfies \(\lambda_{\min} \le R(\mathbf{x}) \le \lambda_{\max}\). Minimizing \(R\) over \(\mathbf{x}\) yields the smallest eigenvalue—foundation of variational eigenvalue methods used in buckling and modal analysis.

## Preview: operators on functions

Replace \(\mathbf{x}\) with function \(u(x)\) and \(\mathbf{A}\) with operator \(-d^2/dx^2\) on \([0,\pi]\) with \(u(0)=u(\pi)=0\). Eigenfunctions are \(\sin(nx)\) with eigenvalues \(n^2\). FEM approximates this spectrum by solving finite-dimensional eigenproblems \(\mathbf{K}\mathbf{u} = \lambda \mathbf{M}\mathbf{u}\).

The story is the same; only the space grew infinite-dimensional.

<div class="bridge">

**Bridge.** Eigenvalues diagonalize symmetric maps. Tensors generalize matrices to multilinear maps on vectors—exactly what stress, strain, and conductivity are in continuum mechanics.

</div>
