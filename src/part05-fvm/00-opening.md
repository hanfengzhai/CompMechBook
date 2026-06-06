# Part V — Conservation on Cells

Part IV discretized elliptic problems on the copper wire — tension, conduction, bending — with trial functions and global stiffness. Many mechanical phenomena, however, are not elliptic equilibria. They are **conservation laws**: mass, momentum, and energy transported by fluxes, often at finite speed, sometimes forming shocks.

The finite volume method discretizes the **integral form** of conservation: fluxes through cell faces, cell averages as unknowns, numerical flux functions that borrow information from neighbors. Where FEM minimizes energy functionals, FVM balances fluxes — the natural language for Navier–Stokes, compressible flow, and the cooling air around a heated conductor. This part follows the author's CFD and FVM notes: 1D advection and Burgers' equation first, then Riemann solvers, then the path to incompressible and compressible Navier–Stokes.

The layout follows the **FVM Notes** in [`writings/fvm/`](../../writings/fvm/): numbered chapters, verification cases (Sod tube, advection), and **Bridge** sections toward Part VI, where the same conservation laws appear in continuum notation.
