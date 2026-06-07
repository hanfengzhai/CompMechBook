## 6.2 Point, line, and surface defects

### Classification

| Dimension | Defect | Example | Continuum signature |
|-----------|--------|---------|---------------------|
| 0D | Vacancy, interstitial | Point defect | Diffusion, creep |
| 1D | Dislocation | Edge, screw | Plastic slip, hardening |
| 2D | Grain boundary, stacking fault | Interface | Hall–Petch, toughening |
| 3D | Void, precipitate | Inclusion | Damage nucleation |

### Burgers vector

A dislocation carries **Burgers vector** $\mathbf{b}$: the closure failure of a Burgers circuit around the defect line. Edge dislocations insert half-planes; screw dislocations twist the lattice. Glide on slip systems $\{ \text{plane}, \text{direction} \}$ produces shear at rates orders of magnitude faster than vacancy diffusion.

### Energy scales

Dislocation line energy scales as $\mu b^2$; grain boundary energy per area is $\gamma_{\text{GB}}$. These enter **Gibbs free energy** competitions that determine whether cracks deflect at enamel rod interfaces (the author's enamel fracture work) or whether voids nucleate at inclusions.

### Homogenization preview

Polycrystal FEM homogenizes grain-scale fields to effective moduli $\mathbb{C}^{\text{eff}}$—averaging over representative volume elements (RVEs). Crystal plasticity FEM assigns slip systems per grain orientation, bridging continuum and discrete slip.

**Takeaway.** Defects explain *why* phenomenological $\sigma_y$ and hardening exist. Part VII simulates dislocations directly; Part VIII simulates atoms.
