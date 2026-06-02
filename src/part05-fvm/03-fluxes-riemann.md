# Fluxes, Riemann Problems, and Shock Capturing

At a discontinuity, pointwise PDEs fail but integral conservation holds. Riemann solvers are the local engines that translate cell averages into consistent face fluxes.

## The Riemann problem

Given left and right states \(U_L, U_R\) separated by a face, the **Riemann problem** solves

\[
U_t + F(U)_x = 0, \quad U(x,0) = \begin{cases} U_L & x < 0 \\ U_R & x > 0 \end{cases}
\]

self-similarly. The solution consists of shocks, rarefactions, and contact waves depending on \(U_L, U_R\).

The **Godunov flux** uses the exact Riemann solution evaluated at the face:

\[
F_{j+1/2} = F(U^*(0; U_j, U_{j+1})).
\]

## Approximate Riemann solvers

Exact Riemann solvers exist for Euler equations but are expensive. **Roe's solver** linearizes the flux Jacobian; **HLL** uses only wave speed estimates; **HLLC** resolves contact discontinuities. Each balances robustness, accuracy, and cost.

## Shock tube: the standard test

Sod's shock tube initializes piecewise constant states with a diaphragm at \(x=0\). The resulting shock, contact, and rarefaction structure tests whether a scheme:

- Conserves mass, momentum, energy
- Avoids spurious oscillations at shocks
- Resolves contact discontinuities sharply

The author's FVM notes use this problem as the canonical verification case — the CFD equivalent of a patch test in FEM.

## Limiters and high-order schemes

Linear reconstruction \(U(x) = U_j + (x - x_j) s_j\) on each cell, combined with limited slopes \(s_j\), yields second-order MUSCL schemes. **Total variation diminishing (TVD)** limiters prevent new extrema at shocks.

Discontinuous Galerkin methods blend FEM's trial functions with FVM-like numerical fluxes — increasingly popular for high-order hyperbolic PDEs.

## Bridge

Navier–Stokes adds viscous fluxes and incompressibility. CFD combines hyperbolic advection (FVM strengths) with elliptic pressure fields (FEM-like solvers). The next chapter situates the full fluid mechanics pipeline.
