## 4.4 Error estimates and convergence

### Céa's lemma

If $a(\cdot,\cdot)$ is coercive and continuous on $V$, and $u$ is the exact weak solution, the Galerkin approximation $u_h \in V_h$ satisfies

$$
\|u - u_h\|_V \le \frac{C}{\alpha} \inf_{v_h \in V_h} \|u - v_h\|_V.
$$

FEM error is controlled by **approximation theory**—how well $V_h$ can represent $u$—not by luck.

### Standard rates (elliptic, quasi-uniform mesh)

For $u \in H^{k+1}(\Omega)$ and degree-$p$ elements with $p \le k$,

$$
\|u - u_h\|_{H^1} = O(h^p), \qquad \|u - u_h\|_{L^2} = O(h^{p+1})
$$

with Aubin–Nitsche duality for the $L^2$ gain.

### Norms in practice

Report errors in:

- **Energy norm** $\|u-u_h\|_a = \sqrt{a(u-u_h, u-u_h)}$ — natural for Galerkin
- **$L^2$ norm** — pointwise-averaged accuracy
- **$\ell^\infty$ norm** — max nodal error (use with care)

Problem Session 8 in ME335A emphasizes that convergence rates appear on log–log plots of error vs mesh size $h$.

### Locking and instability

Poor elements (fully integrated linear quads in nearly incompressible elasticity) can converge at wrong rates or lock. Mixed formulations, reduced integration, and stabilized methods fix pathologies tied to the **inf–sup** condition for saddle-point problems (Stokes, incompressibility).

**Takeaway.** A mesh that "looks fine" may still converge slowly. Measure $\|u-u_h\|$ under mesh refinement.
