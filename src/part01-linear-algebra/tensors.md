# Tensors and index notation

## Why tensors appear

In a bar, a single number (stress) might suffice. In a solid, the traction on a cut plane depends on the plane's orientation. That dependence is **linear in the normal vector** and encoded by the **Cauchy stress tensor** \(\boldsymbol{\sigma}\):

\[
\mathbf{t}(\mathbf{n}) = \boldsymbol{\sigma}\mathbf{n}, \qquad t_i = \sigma_{ij} n_j.
\]

The last equality uses **Einstein summation**: repeated indices are summed.

## Index notation rules

1. **Free index** appears once in a term (e.g. \(i\) in \(t_i\)).
2. **Dummy index** is summed over (e.g. \(j\) in \(\sigma_{ij} n_j\)).
3. **Kronecker delta** \(\delta_{ij} = 1\) if \(i=j\), else \(0\).
4. **Levi-Civita symbol** \(\varepsilon_{ijk}\) for cross products and determinants.

**Example (identity).** \(\delta_{ij} v_j = v_i\).

## Transformation law

Under change of orthonormal basis \(\mathbf{Q}\),

\[
\sigma'_{ij} = Q_{ik} Q_{jl} \sigma_{kl}.
\]

A second-order tensor is a quantity that transforms this way. Scalars are zeroth-order; vectors first-order.

## Strain and stress in small elasticity

**Infinitesimal strain:**

\[
\varepsilon_{ij} = \tfrac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right).
\]

**Hooke's law (isotropic):**

\[
\sigma_{ij} = \lambda \varepsilon_{kk}\delta_{ij} + 2\mu \varepsilon_{ij},
\]

with Lamé parameters \(\lambda, \mu\).

In Voigt notation we pack symmetric tensors into 6-vectors for FEM implementation—but the tensor form reveals coordinate invariance.

## Voigt notation and FEM

\[
\begin{pmatrix} \sigma_{11} \\ \sigma_{22} \\ \sigma_{33} \\ \sigma_{23} \\ \sigma_{13} \\ \sigma_{12} \end{pmatrix}
=
\mathbf{D}
\begin{pmatrix} \varepsilon_{11} \\ \varepsilon_{22} \\ \varepsilon_{33} \\ 2\varepsilon_{23} \\ 2\varepsilon_{13} \\ 2\varepsilon_{12} \end{pmatrix}.
\]

The factors of 2 on shear strains preserve energy pairing \(\sigma_{ij}\varepsilon_{ij}\).

## Fourth-order stiffness tensor

Anisotropic elasticity uses

\[
\sigma_{ij} = \mathbb{C}_{ijkl}\varepsilon_{kl}.
\]

Major and minor symmetries reduce independent components from 81 to 21.

## From tensors to function spaces

Continuum unknowns become fields \(u_i(\mathbf{x})\)—vector-valued functions. Balance laws are PDEs coupling partial derivatives. To discretize them rigorously we need spaces where derivatives make sense: **Sobolev spaces**, built in Part II on the foundation of normed spaces and weak convergence.

<div class="bridge">

**Bridge (end of Part I).** We began with finite vectors and matrices. Tensors showed that even at the continuum scale, physics is multilinear algebra in disguise. But a displacement *field* is not a finite vector—it is a function. Part II asks: *Can we do linear algebra when the vectors have infinitely many components?* The answer, developed through metric spaces, normed spaces, and operators, is functional analysis—and it is the language of weak forms, FEM, and modern PDE theory.

</div>
