## 5.4 Shock tubes and wave propagation

### Sod shock tube

A classic validation problem: two gas states separated by a diaphragm at $t=0$. Riemann solution produces shock, contact, and rarefaction waves. FVM with an approximate Riemann solver reproduces the analytic profile; naive centered differencing produces unphysical oscillations.

The author's *Finite Volume Method & Shock Tube* seminar walks through:

1. 1D Euler system in conservation form
2. Cell averaging and face fluxes
3. Godunov / approximate Riemann flux
4. Time marching with CFL-limited $\Delta t$

### Wave propagation mechanisms

FVM enforces the correct **upwind bias**: information flows along characteristics. This is why FVM is favored for:

- Compressible aerodynamics
- Blast waves
- Astrophysical MHD (Illustris-TNG-class cosmological simulations use related hydro schemes)

### Pros and cons (summary)

| Pros | Cons |
|------|------|
| Exact conservation on discrete level | Higher-order needs reconstruction |
| Natural on unstructured meshes | Elliptic subproblems (pressure) need care |
| Robust shock capturing | Accuracy on smooth flows may lag spectral methods |

### Closing Part V

We now have two continuum discretizations: **FEM** for variational elliptic/parabolic problems, **FVM** for conservation laws. Both return linear algebra from Part I.

The copper wire's plasticity and hardening, however, are not captured by either method alone—they require **defects** and **microstructure**. Part VI connects continuum inelasticity to discrete defects; Part VII tracks dislocations directly.
