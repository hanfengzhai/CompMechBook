# 3. Governing Equations of Continua

> *PDEs are the contracts between physics and computation: they state what must balance, what must diffuse, and what must be conserved.*

With functional analysis in place, we can state the **partial differential equations** that computational mechanics solves. This part is not a catalogue of every constitutive law; it is a structured introduction to the equations that reappear in Parts IV–IX.

We organize by mathematical character—**elliptic**, **parabolic**, **hyperbolic**—because the character guides discretization: elliptic problems favor FEM energy formulations; hyperbolic conservation laws favor FVM flux differencing; parabolic problems often combine both.

Source material: *Partial Differential Equations* (ME300B), *Foundations of Solid Mechanics* (MAE6110), *Elasticity & Inelasticity*, and *Computational Fluid Dynamics* notes.
