## 4.2 Galerkin approximation and assembly

### Finite-dimensional subspaces

Choose a mesh $\mathcal{T}_h$ of $\Omega$ and a local polynomial degree $p$. The **finite element space** $V_h \subset H^1(\Omega)$ consists of functions that are polynomials of degree $\le p$ on each element and continuous across interfaces (for $H^1$-conforming elements).

Seek $u_h \in V_h$ (satisfying Dirichlet BCs) such that

$$
a(u_h, v_h) = \ell(v_h) \quad \forall v_h \in V_h.
$$

With basis $\{N_1, \ldots, N_N\}$ of $V_h$, expand $u_h = \sum_{j=1}^N U_j N_j$. Testing against $N_i$ yields the **algebraic system**

$$
\sum_{j=1}^N a(N_j, N_i) U_j = \ell(N_i), \qquad K_{ij} = a(N_j, N_i), \quad F_i = \ell(N_i).
$$

Hence $K\mathbf{U} = \mathbf{F}$—the stiffness system from Part I.

### Element matrices

On element $e$, restrict to local shape functions $\{N^e_a\}$:

$$
K^e_{ab} = \int_{\Omega_e} k \frac{\partial N^e_b}{\partial x} \frac{\partial N^e_a}{\partial x} \, d\Omega + \int_{\Omega_e} c N^e_b N^e_a \, d\Omega.
$$

$$
F^e_a = \int_{\Omega_e} f N^e_a \, d\Omega.
$$

### Assembly

The **local-to-global map** connects element node indices $(a,b)$ to global indices $(I,J)$. Add $K^e_{ab}$ into $K_{IJ}$ (and similarly for $\mathbf{F}$). This scatter-add is the core FE loop.

### Symmetry and SPD

If $a(\cdot,\cdot)$ is symmetric and coercive on $V$, $K$ is symmetric positive semidefinite; with sufficient Dirichlet constraints, $K$ is SPD and Cholesky or CG applies.

**Takeaway.** Assembly is bookkeeping around the same bilinear form Lax–Milgram already approved at the continuum level.
