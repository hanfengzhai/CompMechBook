# Part V — Conservation on Cells

Part IV discretized elliptic problems by choosing trial functions and enforcing weak statements — the Galerkin philosophy, natural for solids and structures. Fluids and hyperbolic transport obey a different instinct: **conservation laws** integrated over control volumes, with fluxes balanced across cell faces.

The finite volume method is the discrete expression of that instinct. Where FEM asks "in what subspace does the solution live?", FVM asks "how much mass, momentum, or energy crosses each face?" The copper wire heated by current is a solid problem for FEM; the air cooling it, or the turbulent jet in a surrounding duct, is a fluid problem for FVM.

This part develops integral forms of conservation, one-dimensional FVM, Riemann fluxes for shocks, and the Navier–Stokes equations that anchor computational fluid dynamics. The layout follows [`writings/fvm/`](../../writings/fvm/), drawing on the author's CFD and FVM course notes. Read the four chapters in order; Chapter 04 reunites with Part VI, where the stress–balance language both FEM and FVM approximate is written in continuum form.
