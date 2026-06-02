# Integral Forms of Conservation Laws

Where FEM whispers "multiply by a test function and integrate by parts," FVM declares "integrate the conservation law over a control volume and balance fluxes." Both respect the same physics; the bookkeeping differs.

## Conservation in integral form

For a conserved quantity \(U\) with flux \(F(U)\), the integral form on control volume \(\Omega_i\) is

\[
\frac{d}{dt}\int_{\Omega_i} U \, dV + \oint_{\partial \Omega_i} \mathbf{F}\cdot\mathbf{n} \, dS = \int_{\Omega_i} S \, dV.
\]

In steady state with no sources, **net flux through the boundary is zero**. This statement is exact for any volume — it does not require smooth fields.

## 1D Euler equations (fluid mechanics)

For ideal gas dynamics in 1D, conserved variables are

\[
\mathbf{U} = \begin{bmatrix} \rho \\ \rho u \\ \rho e_{\text{total}} \end{bmatrix}, \qquad
\mathbf{F} = \begin{bmatrix} \rho u \\ \rho u^2 + p \\ (\rho e_{\text{total}} + p) u \end{bmatrix}.
\]

The PDE \(\partial \mathbf{U}/\partial t + \partial \mathbf{F}/\partial x = 0\) integrates to flux balance on each cell. Shocks and contact discontinuities are weak solutions where fluxes remain consistent even though derivatives blow up pointwise.

## FEM vs FVM: complementary philosophies

| Aspect | FEM (elliptic focus) | FVM (hyperbolic focus) |
|--------|---------------------|------------------------|
| Primary unknown | Field in trial space | Cell averages |
| Locality | Stiffness coupling | Flux through faces |
| Natural BCs | Essential/natural split | Flux specification |
| Shock handling | Less natural | Riemann solvers |

Many production CFD codes are FVM or flux-difference schemes; many solid mechanics codes are FEM. Coupled problems (fluid–structure interaction) stitch the two.

## Applications across scales

Finite volume ideas appear far beyond aerospace CFD:

- **Geophysics**: ocean circulation, tsunami modeling
- **Thermal hydraulics**: nuclear reactor core cooling
- **Mantle convection**: planetary-scale fluid-like solid flow
- **Astrophysics**: Illustris/TNG cosmological simulations (mentioned in the author's FVM notes)

The method is scale-agnostic because conservation is scale-agnostic.

## Bridge

Discretizing the integral form on a 1D grid yields the classic FVM update: cell average changes by net flux through faces. The next chapter writes that algorithm explicitly — the template for shock tubes and beyond.
