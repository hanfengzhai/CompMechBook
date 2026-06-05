# Part III — Fields on Domains

Part II equipped us with normed spaces, Hilbert geometry, and operators — the vocabulary of infinite degrees of freedom. Mechanics does not live in abstract Hilbert space alone; it lives on **domains**: a wire segment, a bracket, a turbine blade, the fluid around a heated conductor.

This part writes the field equations of continuum physics in those domains. We begin with the classical **strong form** — PDEs satisfied pointwise — and discover where it breaks down. The **weak form** follows naturally: multiply by a test function, integrate by parts, and replace pointwise differentiability with a variational statement in \(H^1\). Sobolev spaces make that statement rigorous; energy methods reveal the minimum principles that finite elements will exploit.

The copper wire appears as a bar in heat conduction, a body in elasticity, and a domain whose corners and loads demand weak formulations even when engineers think in nodal vectors. The layout follows [`writings/pde/`](../../writings/pde/). Read the four chapters in order; Chapter 04 hands off to Part IV, where the weak form becomes an assembly loop.
