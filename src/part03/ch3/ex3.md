## 3.3 Parabolic and hyperbolic problems

### Heat equation (parabolic)

Transient diffusion on $\Omega$:

$$
\frac{\partial u}{\partial t} - \kappa \Delta u = f(\mathbf{x}, t), \qquad u|_{\partial\Omega} = g, \qquad u(\mathbf{x},0) = u_0.
$$

Semidiscretization in space (FEM) yields a system of ODEs $M \dot{\mathbf{U}} + K \mathbf{U} = \mathbf{F}(t)$ with **mass matrix** $M$ and **stiffness** $K$. Time discretization uses backward Euler (unconditionally stable, dissipative), Crank–Nicolson (second order), or Runge–Kutta for wave problems.

### Wave equation (hyperbolic)

$$
\frac{\partial^2 u}{\partial t^2} - c^2 \Delta u = 0.
$$

Characteristics propagate information at finite speed $c$. Explicit time integrators (central difference, Newmark for structures) respect causality; implicit schemes add numerical dissipation that may smear waves.

### Navier–Stokes (mixed character)

Incompressible flow combines elliptic pressure Poisson subproblems with hyperbolic advection:

$$
\rho \left( \frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla\mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot\mathbf{v} = 0.
$$

The convective term $\mathbf{v}\cdot\nabla\mathbf{v}$ is nonlinear and dominates at high Reynolds number—FVM with upwinding (Part V) handles advection; FEM with stabilization (SUPG, PSPG) is an alternative.

**Takeaway.** Time-dependent mechanics is a sequence of spatial BVPs linked by time differencing. The spatial step is where FEM and FVM earn their keep.
