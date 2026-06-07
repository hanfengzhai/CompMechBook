## 1.4 Orthogonality and least squares

### Inner product on $\mathbb{R}^n$

The **Euclidean inner product** is

$$
\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v} = \sum_{i=1}^n u_i v_i.
$$

Vectors are **orthogonal** if $\mathbf{u} \cdot \mathbf{v} = 0$. The **norm** induced by the dot product is $\|\mathbf{u}\|_2 = \sqrt{\mathbf{u} \cdot \mathbf{u}}$.

Orthogonality is the finite-dimensional shadow of $L^2$ orthogonality between functions: $\int_\Omega u v \, d\Omega = 0$.

### Orthonormal bases

A set $\{\mathbf{q}_1, \ldots, \mathbf{q}_n\}$ is **orthonormal** if $\mathbf{q}_i \cdot \mathbf{q}_j = \delta_{ij}$. Expanding a vector in an orthonormal basis is trivial: $c_i = \mathbf{x} \cdot \mathbf{q}_i$.

The **Gram–Schmidt process** constructs an orthonormal basis from independent vectors. In finite precision, **modified Gram–Schmidt** or **Householder QR** is preferred—orthogonality of computed $Q$ in $A = QR$ degrades when $\kappa(A)$ is large, exactly as in ill-conditioned FE fits.

### Projections and least squares

When $A\mathbf{x} = \mathbf{b}$ is overdetermined (no exact solution), we seek $\mathbf{x}$ minimizing $\|A\mathbf{x} - \mathbf{b}\|_2$. The **normal equations**

$$
A^T A \mathbf{x} = A^T \mathbf{b}
$$

give the **least-squares** solution when $A$ has full column rank. Geometrically, $A\hat{\mathbf{x}}$ is the **orthogonal projection** of $\mathbf{b}$ onto $\mathcal{C}(A)$.

In mechanics, least squares appears in parameter identification (fit moduli to data), model reduction (POD modes), and meshless collocation.

### QR and numerical stability

Factoring $A = QR$ with orthonormal $Q$ and upper triangular $R$ avoids forming $A^T A$ explicitly and improves stability. Many production FE eigensolvers and least-squares solvers use QR or SVD internally.

**Takeaway.** Galerkin's method in Part IV chooses coefficients so the residual is orthogonal to the test space—a least-squares-like condition in an infinite-dimensional setting. The normal equations you know here become the weak form there.
