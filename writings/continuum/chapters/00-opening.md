# Part VI — Continuum Mechanics

Parts III–V discretized PDEs — weak forms for FEM, integral forms for FVM. Those PDEs did not appear from nowhere. They are the **continuum mechanics** of deformable bodies and flowing fluids: kinematics, stress, balance laws, constitutive relations.

This part supplies the physics vocabulary that FEM and FVM implementations approximate. The copper wire is a deformable body: axial stretch, shear in torsion, thermal expansion if current heats it. We write deformation gradients and strain measures, Cauchy stress and traction boundary conditions, and the virtual work principle that is the weak form of elasticity in disguise. Nonlinear extensions preview the path from linear Part IV examples to industrial solid mechanics.

The layout follows the **Continuum Mechanics Notes** in [`writings/continuum/`](../../writings/continuum/): numbered chapters tied to elasticity coursework, and **Bridge** sections toward Part VII, where smooth continuum fields break down at defects.
