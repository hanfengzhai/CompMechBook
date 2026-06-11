# Convergence, norms, and error estimates

## Types of convergence

| Norm | Measures | Typical use |
|------|----------|-------------|
| \(L^2\) | \(\|u-u_h\|_{L^2}\) | average field error |
| \(H^1\) / energy | \(\|\nabla(u-u_h)\|_{L^2}\) | stiffness-dominated elliptic |
| \(L^\infty\) | pointwise max | peak stress (careful) |

ME335A Session 8 emphasizes **norms and convergence** in numerical analysis: stability + consistency \(\Rightarrow\) convergence.

## Céa's lemma

If \(a\) is coercive and continuous on \(H\), Galerkin solution \(u_h \in V_h\) satisfies

\[
\|u - u_h\|_a \le C \inf_{v_h \in V_h} \|u - v_h\|_a.
\]

**Meaning.** FEM error is controlled by how well \(V_h\) can approximate the true solution—pure approximation theory.

## Interpolation error

For P1 elements on quasi-uniform meshes of size \(h\), smooth solutions satisfy

\[
\|u - \Pi_h u\|_{H^1} \le C h \|u\|_{H^2},
\]

with \(\Pi_h\) the interpolant. Hence \(\|u - u_h\|_{H^1} = O(h)\) under standard regularity.

Higher-order elements (\(\mathbb{P}_2\), \(\mathbb{P}_3\)) improve rates when \(u\) is smooth enough.

## Locking and instability

- **Locking:** poor \(H^1\) behavior for nearly incompressible materials on low-order elements.
- **Hourglass modes:** spurious zero-energy modes in under-integrated solids.
- **Pollution:** high wave numbers on coarse meshes degrade accuracy.

Remedies: mixed formulations, selective reduced integration, stabilized methods.

## A posteriori estimates (outline)

Element-wise error indicators from residual jumps guide adaptive mesh refinement (\(h\)-refinement). Goal: equidistribute error so \(\|u-u_h\|\) decreases optimally with DOF count.

## Heat transfer capstone (ME335A Session 9)

The course closes with 2D heat conduction using P1 elements—scalar Poisson with thermal conductivity, Dirichlet/Neumann BCs, and postprocessing fluxes. It is the same pipeline as elasticity with different constitutive constant.

<div class="bridge">

**Bridge (end of Part IV).** FEM excels at elliptic and parabolic problems where global coupling and variational structure dominate. **Hyperbolic conservation laws**—shocks, compressible flow—invite a cell-based viewpoint: finite volumes.

</div>
