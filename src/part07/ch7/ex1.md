## 7.1 Dislocation theory in brief

### Elastic fields

In isotropic elasticity, a straight dislocation produces stress $\boldsymbol{\sigma} \sim \mu b / r$ at distance $r$ from the line. Image forces, free surfaces, and anisotropy modify this field but the $1/r$ decay is universal.

### Peach–Köhler force

The driving force on a dislocation segment of length $L$ with tangent $\boldsymbol{\xi}$ is

$$
\mathbf{f} = (\boldsymbol{\sigma} \cdot \mathbf{b}) \times \boldsymbol{\xi},
$$

projecting resolved shear stress onto the slip system. Segments glide when $|\mathbf{f}|$ exceeds friction from lattice resistance and forest interactions.

### Rules of motion

DDD codes implement:

- **Glide** on slip planes
- **Climb** (vacancy diffusion mediated—slow at room temperature)
- **Cross-slip** (out-of-plane motion for screw segments)
- **Short-range reactions** (annihilation, junction formation, jog production)

Elastic interactions between all pairs of segments dominate cost—$O(N^2)$ naive, accelerated with fast multipole or domain decomposition.

**Takeaway.** DDD is MD without every atom—only the defects that carry plastic strain.
