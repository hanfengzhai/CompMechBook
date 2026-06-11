# Hyperbolic conservation laws

## Conservation form

Many fluid and solid wave problems take the form

\[
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{F}(\mathbf{U})}{\partial x} = 0,
\]

where \(\mathbf{U}\) is a vector of **conserved variables** (mass, momentum, energy) and \(\mathbf{F}\) the **flux**.

**1D Euler equations** (from the author's FVM notes):

\[
\mathbf{U} = \begin{pmatrix} \rho \\ \rho u \\ \rho e_{\mathrm{total}} \end{pmatrix}, \quad
\mathbf{F} = \begin{pmatrix} \rho u \\ \rho u^2 + p \\ (\rho e_{\mathrm{total}} + p) u \end{pmatrix}.
\]

## Integral form

For control volume \(\Omega\) with boundary \(\partial\Omega\),

\[
\frac{d}{dt}\int_\Omega \mathbf{U}\, dV + \oint_{\partial\Omega} \mathbf{F}\cdot\mathbf{n}\, dS = 0.
\]

Finite volume methods discretize this **integral statement** directly—fluxes through cell faces, not pointwise PDE derivatives.

## Characteristics and shocks

For hyperbolic systems, information propagates along **characteristics**. Nonlinear fluxes can steepen into **shocks** and **contact discontinuities** even from smooth initial data.

Classical solutions break down; **weak solutions** satisfy the integral conservation law. Entropy conditions select physically admissible shocks.

## Relationship to Navier–Stokes

**Navier–Stokes** adds viscous and heat-conduction fluxes:

\[
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{F}}{\partial x} = \frac{\partial \mathbf{F}_v}{\partial x} + \mathbf{S}.
\]

Inviscid limit \(\mathbf{F}_v \to 0\) recovers Euler; viscous terms regularize shocks (thin layers) but require resolution or turbulence modeling.

## CFD motivation (from personal notes)

Computational fluid dynamics solves fluid mechanics problems when analytical Navier–Stokes solutions are unavailable due to nonlinearity, complex geometry, and boundary conditions. CFD discretizes the governing equations—continuity, momentum, energy—on meshes or grids.

The author's CFD notes (Shanghai University, 2020) begin from the vector form

\[
\rho \frac{D\mathbf{V}}{Dt} = \rho \mathbf{g} - \nabla P + \mu \nabla^2 \mathbf{V}
\]

and rewrite it in conservative variables \(\mathbf{U}\) for numerical discretization—exactly the passage from physics to algorithm.

<div class="bridge">

**Bridge.** Conservation laws state *what is conserved across control volumes*. The **finite volume method** specifies how to compute fluxes at cell interfaces.

</div>
