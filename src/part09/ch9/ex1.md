## 9.1 Hohenberg–Kohn and Kohn–Sham

### Hohenberg–Kohn theorems

1. Ground-state energy is a **functional** of density $\rho(\mathbf{r})$: $E[\rho] = T[\rho] + V_{ext}[\rho] + E_{H}[\rho] + E_{xc}[\rho]$.
2. The minimizing $\rho$ is unique (for non-degenerate ground states).

### Kohn–Sham equations

Introduce auxiliary non-interacting orbitals $\psi_i$ solving

$$
\left[ -\frac{1}{2}\nabla^2 + V_{\text{eff}}[\rho](\mathbf{r}) \right] \psi_i = \varepsilon_i \psi_i,
$$

with $\rho(\mathbf{r}) = \sum_i f_i |\psi_i(\mathbf{r})|^2$ and $V_{\text{eff}} = V_{ext} + V_H + V_{xc}$.

The **exchange–correlation functional** $E_{xc}$ is approximated (LDA, GGA-PBE, meta-GGA, hybrids). Errors in $E_{xc}$ dominate systematic error for metals, molecules, and defects.

### Born–Oppenheimer MD

Solve Kohn–Sham at fixed nuclear positions $\{\mathbf{R}_I\}$, compute forces, move nuclei, repeat—**ab initio MD**. Expensive ($O(N^3)$ traditional planewave codes) but parameter-free.

**Takeaway.** DFT is the root of the parameter tree. Fit EAM to DFT energies; trust propagates upward.
