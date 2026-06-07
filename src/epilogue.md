# 10. Bridging Scales

We opened with a copper wire and asked how its stretch, yield, and hardening connect to computation. We close by naming the bridges explicitly—because multiscale modeling fails when information flows the wrong direction or stops halfway.

## The ladder, reviewed

```text
DFT          electrons → bonding, elastic constants, fault energies
  ↓ fit / ab initio MD
MD           atoms → core structures, mobility hints, fracture sequences
  ↓ statistics / calibration
DDD          dislocation lines → link distributions, hardening laws
  ↓ homogenization / crystal plasticity
FEM/FVM      continua → parts, structures, fluids
  ↑ discretized via
Linear algebra + functional analysis (weak forms, conservation laws)
```

Each rung is legitimate alone. A bridge designer may live entirely on FEM with tabulated $\sigma_y(\bar{\varepsilon}^p)$. A materials scientist may live on DFT + MD for a new alloy. The **book's narrative** is that these are one story with different zoom levels—not unrelated software packages.

## Verification vs validation

- **Verification:** Is the discretization correct? (mesh convergence, CFL, residual norms)
- **Validation:** Does the model match experiment? (tensile tests, link statistics, band gaps)

Functional analysis supplies verification language for FEM ($\|u-u_h\|_{H^1}$). Conservation checks verify FVM. DDD validates against TEM link counts. DFT validates against lattice constants.

## Concurrent and hierarchical multiscale

**Hierarchical:** Run DFT → fit potential → run MD → extract parameters → run DDD → homogenize → FEM. One-way, auditable.

**Concurrent:** FEM and MD (or DDD) run simultaneously with handshake zones—Quasi-continuum, FE², surrogate GNNs predicting polycrystal stress fields. The author's graph-neural-network work on polycrystal plasticity is concurrent multiscale: FEM generates truth; ML accelerates inference if physics constraints are preserved.

## What to learn next

This book intentionally stops before scientific machine learning, inverse design, and optimal control—topics the author works on daily—but the foundation here is what makes those methods trustworthy. A physics-informed neural network without weak-form awareness is curve fitting; with it, the network inherits the same variational structure as FEM.

## Final word

Computational mechanics is not a menu of codes. It is a single plot: **represent geometry**, **state balance laws**, **choose function spaces or control volumes**, **solve linear systems**, **measure error**, and—when continuum parameters demand it—**descend to defects, atoms, and electrons**.

The wire in your hand is still the same wire at every scale. Only the vocabulary changes—from vectors to functions to fluxes to dislocation lines to atoms to electron density. You now have the map. The journey between scales is the rest of your research.
