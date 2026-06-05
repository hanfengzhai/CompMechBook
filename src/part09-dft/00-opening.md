# Part IX — Electronic Structure

Part VIII assumed classical nuclei on a potential energy surface. That surface is not fundamental — it is the **Born–Oppenheimer** shadow of quantum electrons binding the copper crystal together. At ångströms, the notion of an atom as a ball on a spring dissolves into an electron density \(\rho(\mathbf{r})\) and a total energy functional that ground-state quantum mechanics minimizes.

Density functional theory (DFT) is how practitioners compute that energy daily. Hohenberg and Kohn proved that the ground-state density determines the energy; Kohn and Sham recast the problem as a self-consistent set of single-particle equations tractable on a computer. The cohesive energy, elastic moduli, surface energies, and reaction barriers that Parts VI–VIII import as input begin here.

The copper wire's chemistry — oxidation at the surface, alloying, the very existence of metallic bonding — is an electronic-structure question. This part closes the downward arc of the book. The layout follows [`writings/dft/`](../../writings/dft/), informed by DFT coursework and atomistic modeling notes. Read the two chapters in order; the epilogue then asks how to couple all nine parts into multiscale workflows that no single code runs alone.
