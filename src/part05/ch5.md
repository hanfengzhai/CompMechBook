# 5. Conservation Laws on Control Volumes

> *Where FEM asks "what is the energy inner product?", FVM asks "what flux crosses this face?"*

The **finite volume method** (FVM) discretizes **integral conservation laws** on **control volumes** (cells). It is the standard choice in computational fluid dynamics when **mass, momentum, and energy must be conserved** explicitly—especially across shocks, contact discontinuities, and complex geometries with unstructured meshes.

This part draws on the author's *Computational Fluid Dynamics* notes (Shanghai University) and the *Finite Volume Method & Shock Tube* seminar. We develop the 1D Euler system, the semidiscrete flux differencing formula, and the connection to Riemann solvers—then relate FVM to the Navier–Stokes conservation form introduced in Part III.

FEM and FVM are not rivals; they are complementary chapters of the same book. Solid mechanics often lives in FEM; compressible CFD often lives in FVM. Coupled problems may use both.
