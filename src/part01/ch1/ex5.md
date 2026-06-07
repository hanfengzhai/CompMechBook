## 1.5 Eigenvalues, SVD, and conditioning

### Eigenvalues and eigenvectors

For $A \in \mathbb{R}^{n \times n}$, a nonzero $\mathbf{v}$ is an **eigenvector** with **eigenvalue** $\lambda$ if

$$
A \mathbf{v} = \lambda \mathbf{v}.
$$

Eigenvalues reveal **modes**: natural frequencies in vibration ($K\mathbf{u} = \omega^2 M \mathbf{u}$), buckling loads, stability of time integrators.

For symmetric $A$, eigenvectors are orthogonal and all $\lambda \in \mathbb{R}$—a fact we use constantly in modal analysis and in proving SPD properties of stiffness matrices.

### Generalized eigenvalue problems

Structural dynamics solves

$$
K \boldsymbol{\phi} = \lambda M \boldsymbol{\phi},
$$

with stiffness $K$ and mass $M$. Modes $\boldsymbol{\phi}$ decouple the equations of motion in linear vibration—each mode oscillates at $\sqrt{\lambda}$.

### Singular value decomposition

Every $A \in \mathbb{R}^{m \times n}$ admits an **SVD** $A = U \Sigma V^T$ with orthogonal $U, V$ and diagonal $\Sigma \succeq 0$. Singular values $\sigma_i$ generalize eigenvalues to rectangular matrices.

The SVD exposes **rank**, **condition number** $\sigma_{\max}/\sigma_{\min}$, and optimal low-rank approximations—used in reduced-order modeling of FE and fluid systems.

### Conditioning revisited

For symmetric positive definite $K$,

$$
\kappa(K) = \frac{\lambda_{\max}}{\lambda_{\min}}.
$$

A mesh with elements of wildly different sizes can spread eigenvalues and inflate $\kappa(K)$, slowing iterative solvers and amplifying roundoff.

**Practical rule.** If direct solvers succeed but iterative ones stall, check mesh quality and material contrast before blaming the algorithm.

**Takeaway.** Eigenanalysis connects discrete matrices to physical modes. When we study error estimates in FEM, eigenvalues of the stiffness matrix in different mesh spaces will reappear as stability constants.
