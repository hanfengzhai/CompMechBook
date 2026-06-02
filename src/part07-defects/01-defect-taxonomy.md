# Point, Line, and Surface Defects

Perfect crystals exist in textbooks. Real materials carry defects — localized disruptions of order that control strength, diffusion, and optical properties.

## Taxonomy

| Defect | Dimension | Example | Mechanical role |
|--------|-----------|---------|-----------------|
| Vacancy | 0 | Missing atom | Diffusion, creep |
| Interstitial | 0 | Extra atom | Hardening, swelling |
| Dislocation | 1 | Extra half-plane of atoms | Plasticity, work hardening |
| Grain boundary | 2 | Misoriented crystal meeting | Hall–Petch strengthening |
| Stacking fault | 2 | Wrong stacking sequence | Twinning, partial dislocations |

The author's [defects notes](https://hanfengzhai.github.io/file/defects_notes.pdf) develop thermodynamics and mechanics of these structures — the conceptual bridge between atomistic lattices and continuum plasticity.

## Elastic fields of defects

A screw dislocation in isotropic elasticity has displacement field scaling as \(\theta\) around the core — a singularity at the origin in linear elasticity. The **Burgers vector** quantifies the closure failure around a loop enclosing the core:

\[
\mathbf{b} = \oint d\mathbf{u}.
\]

Stress fields decay as \(1/r\) away from line defects — slow decay means dislocations interact over long ranges, making many-body simulations essential.

## Homogenization preview

Continuum plasticity models (J2 flow, crystal plasticity) **homogenize** defect motion into yield surfaces and hardening laws. Parameters like initial yield stress and hardening modulus come from underlying dislocation density — connecting Part VII to Part VI.

## Bridge

Dislocation dynamics simulates line defects directly — too coarse for every atom, too fine for pure FEM. It is the mesoscale chapter of our story.
