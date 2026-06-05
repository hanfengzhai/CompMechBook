# Part VI — Continuum Mechanics

Parts IV and V showed how to **compute** field equations — Galerkin assembly for elliptic solids, flux balance for fluids. Part VI asks what those equations **mean** in the language of solid mechanics: how bodies deform, how stress measures internal force, how balance laws connect motion to loads, and how variational principles unify statics and dynamics.

The copper wire under tension is no longer a mesh of bar elements or a thermal diffusion problem alone. It is a deformable body with a strain energy density, a Cauchy stress tensor, and boundary conditions that fix or load its ends. The moduli and yield surfaces that appear here are the quantities Parts VII–IX will explain from finer scales.

This part is the hinge of the book. Above it, we discretize; below it, we derive. The layout follows [`writings/continuum/`](../../writings/continuum/). Read the three chapters in order; Chapter 03 hands off to Part VII, where singularities and line defects force us below the smooth continuum.
