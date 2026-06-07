## 2.3 Inner products and Hilbert spaces

### Inner product spaces

An **inner product** on $V$ is a map $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$ that is linear in the first argument, symmetric, and positive definite: $\langle u,u \rangle \ge 0$ with equality iff $u = 0$.

It induces a norm $\|u\| = \sqrt{\langle u, u \rangle}$. The **Cauchy–Schwarz inequality**

$$
|\langle u, v \rangle| \le \|u\| \|v\|
$$

underlies every energy estimate in PDE theory.

### Hilbert spaces

A **Hilbert space** is a complete inner product space. $L^2(\Omega)$ and $H^1(\Omega)$ are Hilbert spaces with inner products

$$
\langle u, v \rangle_{L^2} = \int_\Omega u v \, d\Omega, \qquad
\langle u, v \rangle_{H^1} = \int_\Omega \big( uv + \nabla u \cdot \nabla v \big) \, d\Omega.
$$

### Orthogonality and projection

Vectors $u \perp v$ if $\langle u, v \rangle = 0$. For a closed subspace $W \subset H$, every $u \in H$ splits uniquely as $u = u_W + u_\perp$ with $u_W \in W$ and $u_\perp \perp W$. The **orthogonal projection** $P_W u = u_W$ minimizes $\|u - w\|$ over $w \in W$.

Galerkin FEM chooses $u_h$ in a finite-dimensional subspace $V_h \subset H^1$ so that the residual is orthogonal to $V_h$ in the energy inner product—finite-dimensional orthogonal projection generalized.

### Riesz representation

For a Hilbert space $H$ and continuous linear functional $\ell \in H'$, there exists unique $g \in H$ with $\ell(u) = \langle g, u \rangle$ for all $u \in H$.

This theorem is why weak formulations work: specifying $\ell(v)$ is equivalent to specifying a "load vector" $g$ in the same space as displacements.

**Takeaway.** Hilbert spaces are where variational mechanics is rigorous. The FE stiffness matrix is the Riesz representation of the bilinear form restricted to $V_h$.
