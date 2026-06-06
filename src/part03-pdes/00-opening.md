# Part III — Fields on Domains

Part II equipped us with function spaces — \(L^2\), \(H^1\), operators, and compactness. Mechanics, however, does not pose abstract problems in Hilbert space. It poses **partial differential equations** on domains: a wire under tension, a plate in bending, heat diffusing through a conductor, fluid flowing around a body.

This part writes those laws in strong form, explains where classical smoothness fails, and introduces the **weak formulation** that makes finite-dimensional approximation legitimate. The copper wire returns as a domain \(\Omega\) with boundary conditions: fixed ends, applied traction, convective cooling at the surface. Sobolev spaces enter not as abstraction but as the precise regularity class in which the weak problem is well posed.

The layout follows the **PDE Notes** in [`writings/pde/`](../../writings/pde/): numbered chapters, energy principles alongside integration-by-parts arguments, and **Bridge** sections that connect each chapter to the next. Read the four chapters in order; Chapter 4 hands off to Part IV (finite elements) and Part V (finite volumes), which discretize the weak and integral forms developed here.
