# Born–Oppenheimer and the Hohenberg–Kohn Theorems

Electrons determine almost all material properties at the chemical level. Density functional theory (DFT) makes their ground-state energy a functional of the electron density — tractable on computers.

## Born–Oppenheimer approximation

Nuclei are much heavier than electrons. On electronic timescales, nuclei appear stationary; on nuclear timescales, electrons adiabatically follow. This **separation of scales** lets us:

1. Solve for electron ground state at fixed nuclear positions
2. Use that energy as the potential surface for nuclear motion (MD or optimization)

Without Born–Oppenheimer, ab initio molecular dynamics requires expensive explicit electron dynamics.

## Hohenberg–Kohn theorems

For a system of interacting electrons in an external potential:

1. The ground-state electron density \(\rho(\mathbf{r})\) uniquely determines the potential (up to constants).
2. A universal functional \(E[\rho]\) exists whose minimum gives the ground-state energy.

We never know \(E[\rho]\) exactly — approximations define practical DFT.

## Exchange–correlation

The **exchange–correlation functional** \(E_{xc}[\rho]\) captures quantum many-body effects missing from classical Coulomb repulsion. Common choices:

- **LDA**: local density approximation
- **GGA**: generalized gradient (PBE, widely used)
- **Hybrid**: mix Hartree–Fock exchange (B3LYP)
- **Meta-GGA, ML functionals**: ongoing accuracy improvements

XC functional choice affects lattice constants, band gaps, and reaction barriers — always compare like with like in validation studies.

## Bridge

Kohn–Sham DFT replaces the interacting problem with an auxiliary non-interacting system sharing the same density — implemented in codes like Quantum ESPRESSO, VASP, and GPAW. The next chapter states the equations practitioners solve daily.
