# Dislocation dynamics

## What is a dislocation?

A **dislocation** is a line defect in a crystal lattice: a boundary between slipped and unslipped regions. The **Burgers vector** \(\mathbf{b}\) quantifies the lattice closure failure around the line.

Edge and screw dislocations are limiting geometries; real lines curve and superpose.

**Stress field (screw, isotropic elasticity):**

\[
\tau_\theta = \frac{\mu b}{2\pi r},
\]

with shear modulus \(\mu\) and distance \(r\) from the line.

## Why simulate dislocations?

Continuum plasticity averages over millions of dislocations. **Dislocation dynamics (DD)** resolves individual lines when:

- studying strain hardening mechanisms,
- connecting microstructure to yield stress,
- validating crystal plasticity parameters.

The author's doctoral work on **dislocation link statistics** during strain hardening uses large-scale DDD simulations (OpenDiS and related tools) to show how active slip systems develop stress-driven link-length distributions—physics invisible to standard FEM.

## Equations of motion

In the **mobility law** formulation, each dislocation segment of length \(L\) moves with velocity \(\mathbf{v}\) proportional to the **Peach–Koehler force** per unit length:

\[
\mathbf{f} = (\boldsymbol{\sigma}\cdot\mathbf{b}) \times \mathbf{t},
\]

with stress \(\boldsymbol{\sigma}\), line tangent \(\mathbf{t}\), and mobility tensor linking \(\mathbf{v}\) to \(\mathbf{f}\).

Short-range interactions (reaction, junction formation, annihilation) require **cutoff rules** and **remeshing** of dislocation lines.

## DDD workflow

```
  Initial microstructure (FRANK-Read sources, random lines)
        ↓
  Apply loading / boundary conditions (FEM-coupled or analytical)
        ↓
  Time integrate segment velocities; handle topology changes
        ↓
  Extract density, link statistics, stress-strain response
```

**FEM–DDD coupling:** FEM supplies \(\boldsymbol{\sigma}(\mathbf{x})\) from macroscopic boundary conditions; DD supplies plastic strain rate from dislocation motion.

## Scale bridge

| Method | Length scale | Time scale |
|--------|--------------|------------|
| DFT | Å | fs |
| MD | nm | ps–ns |
| DD | µm | µs–ms |
| FEM | mm–m | s |

No single method spans all scales; **multiscale** workflows pass information upward (homogenization) or downward (representative volume elements).

<div class="bridge">

**Bridge (end of Part VI).** Dislocations are still continuum objects—lines in an elastic medium. At atomic resolution, positions and velocities of nuclei matter: **molecular dynamics**.

</div>
