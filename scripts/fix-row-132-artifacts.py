#!/usr/bin/env python3
"""Repair row 132 / row 131 backfill artifacts in writings/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "writings"

PROLOGUE_STITCH_131 = (
    "**Row 131 closing stitch (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-131-closing-stitch} "
    "When row 130 closed — DDD meta prelude capstone verified, row 129 or row 50 recited, and VII.1 Bridge → VII.2 Peach–Köhler recited with forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening on the capstone path — but **row 51 VII.2 → VII.3 opening hinge still opens like standalone DAMASK homework after the post-yield forest Scene** — "
    "`writings/defects` chapters 02 and 03 build as separate reading acts, Voce calibration and texture tables feel disconnected from \\(\\tau(\\rho)\\) on the single-crystal RVE, or row 51's Bridge → homogenization audit feels disconnected from row 130's segment-network → spool closure while the unified HTML reads smoothly — "
    "the [preface row 131 When-to-pause opening sentence](../preface.md#skill-navigation-row-131) names the dual reunion before the atomistic meta reunion; read [preface row 131](../preface.md#skill-navigation-row-131), then the "
    "[Row 68 → Row 111 reunion index](../appendix/sources.md#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131), then "
    "[epilogue row 131 closing loop](../epilogue/multiscale.md#row-131-closing-loop) before row 52 atomistic meta prelude capstone opens.\n\n"
)

PROLOGUE_PREVIEW_131 = (
    "| <span id=\"prologue-preview-row-131\"></span>Row 131 preview (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and VII.2 → VII.3 meta (row 51) must be read together with the Bridge → homogenization chain "
    "after verified DDD meta prelude capstone before OpenDiS exports and DAMASK texture tables feel like separate courses on the capstone path | "
    "One sentence: \"read row 68 gate + row 130 or row 111 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud "
    "when Peach–Köhler DDD is clean on the capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone\" — "
    "[preface row 131 skill checkpoint](../preface.md#skill-navigation-row-131); [prologue row 131 closing stitch](#row-131-closing-stitch); "
    "[Row 68 → Row 111 reunion index](../appendix/sources.md#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131); "
    "[memory sheet row 131 baby picture](../appendix/memory-sheet.md#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion); "
    "[VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3); "
    "[VII.2 opening hinge to VII.3](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3); "
    "[preface row 51 skill checkpoint](../preface.md#skill-navigation-row-51); "
    "[preface row 130 skill checkpoint](../preface.md#skill-navigation-row-130); "
    "[epilogue row 131 closing loop](../epilogue/multiscale.md#row-131-closing-loop) |\n"
)

MEMORY_BABY_131 = """
### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion}

**Row 131 baby picture:** when row 68 closed the midpoint prelude and row 130 or row 111 closed DDD meta prelude capstone / homogenization meta prelude but **row 51's VII.2 Bridge → polycrystal handoff still feels like separate courses on the capstone path**, open the [Row 68 → Row 111 homogenization meta prelude capstone reunion index](sources.md#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 130](../preface.md#skill-navigation-row-130) or [preface row 111](../preface.md#skill-navigation-row-111) DDD meta prelude capstone / homogenization meta prelude gate → [VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3) through [VII.2 opening hinge to VII.3](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3) aloud → [preface row 51](../preface.md#skill-navigation-row-51) five-step audit → confirm forest-density Lab act linked \\(\\tau(\\gamma)\\) before row 52 atomistic meta prelude capstone opens.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  DM[DDD meta prelude capstone row 130]
  BR[VII.2 Bridge]
  R51[row 51 meta gate]
  MP --> DM --> BR --> R51
```

When row 131 feels disconnected from row 130, read them as **DDD meta prelude capstone vs homogenization meta prelude capstones**: row 130 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before any VII.2 → VII.3 audit on the capstone path**; row 131 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 132 atomistic meta prelude capstone or row 52 atomistic reunion opens on the capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous OpenDiS → polycrystal afternoon. When row 130 closed but homogenization meta reunion still lags on the capstone path, switch to [row 131](#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion).

"""

ROW132_EPILOGUE = """
### Row 132 closing loop (Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-132-closing-loop}

This subsection is the **downstream half** of [memory sheet row 132](../appendix/memory-sheet.md#continuity-hinges-master-map), the [preface row 132 skill checkpoint](../preface.md#skill-navigation-row-132), and the [Row 68 → Row 112 atomistic meta prelude capstone reunion index](../appendix/sources.md#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132). The [prologue row 132 preview](../prologue/00-many-scales.md#prologue-preview-row-132) and [prologue row 132 closing stitch](../prologue/00-many-scales.md#row-132-closing-stitch) are the **upstream halves** — return there when row 131 closed homogenization meta prelude capstone and row 68 closed the midpoint prelude but **row 52 VII.3 → VIII.1 opening hinge still opens like standalone LAMMPS homework after the handoff Lab act on the capstone path** while VII.3 Bridge and VIII.1 phase-space sections read correctly in isolation. Row 132 closes the **atomistic meta prelude capstone at the defects → md subtree boundary in reading time on the capstone path**: verified homogenization meta prelude capstone closure (row 131) and Row 68 → Row 52 meta (row 112) must read as one spool → screw-core afternoon before row 53 dynamics meta prelude opens in workflow time.

| Step | Prologue preview ([row 132](../prologue/00-many-scales.md#prologue-preview-row-132)) | [Preface row 132](../preface.md#skill-navigation-row-132) | Workflow exam ([midpoint row](#what-you-should-be-able-to-do-after-the-book)) |
|------|--------------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------|
| 1 | Name row 68 closed before atomistic meta prelude capstone | Step 1 — row 68 gate | Midpoint prelude recited |
| 2 | Name homogenization meta prelude capstone before VII.3 Bridge | Step 2 — homogenization meta prelude capstone / atomistic meta prelude gate | `mobility.yaml` before EAM tables on capstone path |
| 3 | Name VII.3 Bridge as part exit | Step 3 — Bridge recitation | Cores need atoms |
| 4 | Name handoff Lab act before VIII.1 Scene | Step 4 — Scene audit | Screw-core RVE planned |
| 5 | [Row 68 → Row 112 reunion index](../appendix/sources.md#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) recitation | Step 5 — row 52 meta gate | VII.3 → VIII.1 reads continuous |

When row 52 feels like LAMMPS homework after row 131 alone on the capstone path, start at [VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) — read through [VII.3 opening hinge to VIII.1](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1), then [VIII.1 opening hinge from VII.3](../part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1) and [VIII.1 plot spine](../part08-md/01-potentials-phase-space.md#plot-spine-one-line) — before the [row 52 closing loop](#row-52-closing-loop). Open [preface row 52](../preface.md#skill-navigation-row-52) and confirm the five-step meta audit matches the same Bridge → phase-space contract per [row 72](../preface.md#skill-navigation-row-72). Recite [preface row 131](../preface.md#skill-navigation-row-131) to split homogenization meta prelude capstone from atomistic reunion. Confirm [handoff Lab act step 5](../part07-defects/03-polycrystal-and-fem-handoff.md#lab-act-archive-the-opendis--damask--fem-handoff-act-ivv) archived `mobility.yaml` before EAM minimize. The [memory sheet row 132 baby picture](../appendix/memory-sheet.md#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion) compresses the dual atomistic meta prelude capstone for index-card review. Do not conflate row 132 (row 68 ↔ row 52 reunion on the capstone path) with row 112 (opening-hinge prelude stitch alone) — row 112 names **Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion**; row 132 names **why that reunion must follow verified homogenization meta prelude capstone (row 131) and the outer midpoint prelude gate (row 68)**. Proceed to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the capstone path, to [row 112](#row-112-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge path alone, to [row 131](#row-131-closing-loop) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, to [row 52](#row-52-closing-loop) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync.

"""

MEMORY_BABY_132 = """
### Row 132 baby picture (Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion}

**Row 132 baby picture:** when row 68 closed the midpoint prelude and row 131 or row 112 closed homogenization meta prelude capstone / atomistic meta prelude but **row 52's VII.3 Bridge → phase-space handoff still feels like separate courses on the capstone path**, open the [Row 68 → Row 112 atomistic meta prelude capstone reunion index](sources.md#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 131](../preface.md#skill-navigation-row-131) or [preface row 112](../preface.md#skill-navigation-row-112) homogenization meta prelude capstone / atomistic meta prelude gate → [VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) through [VII.3 opening hinge to VIII.1](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1) aloud → [preface row 52](../preface.md#skill-navigation-row-52) five-step audit → confirm [handoff Lab act step 5](../part07-defects/03-polycrystal-and-fem-handoff.md#lab-act-archive-the-opendis--damask--fem-handoff-act-ivv) archived `mobility.yaml` before row 53 dynamics meta prelude capstone opens.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  HM[Homogenization meta prelude capstone row 131]
  BR[VII.3 Bridge]
  R52[row 52 meta gate]
  MP --> HM --> BR --> R52
```

When row 132 feels disconnected from row 131, read them as **homogenization meta prelude capstone vs atomistic meta prelude capstones**: row 131 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before any VII.3 → VIII.1 audit on the capstone path**; row 132 when **VII.3 Bridge and Row 68 → Row 52 meta must read on the same wire before row 113 dynamics meta capstone or row 53 dynamics reunion opens on the capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous spool → screw-core afternoon. When row 131 closed but atomistic meta reunion still lags on the capstone path, switch to [row 132](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion).

"""

SOURCES_ROW132 = (
    "| 132 | Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone ↔ row 52 meta) | "
    "[Row 68 → Row 112 atomistic meta prelude capstone reunion index](#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) · "
    "[preface row 132](../preface.md#skill-navigation-row-132) · "
    "[prologue row 132 preview](../prologue/00-many-scales.md#prologue-preview-row-132) · "
    "[prologue row 132 closing stitch](../prologue/00-many-scales.md#row-132-closing-stitch) · "
    "[epilogue row 132 closing loop](../epilogue/multiscale.md#row-132-closing-loop) · "
    "[memory sheet row 132 baby picture](memory-sheet.md#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the capstone path** — "
    "read row 68 + row 131 or row 112 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[preface row 52](../preface.md#skill-navigation-row-52) |\n"
)

MEMORY_ROW132 = (
    "| 132 | Meta | [Row 68 → Row 112 atomistic meta prelude capstone reunion index](sources.md#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) · "
    "[preface row 132 skill checkpoint](../preface.md#skill-navigation-row-132) · "
    "[prologue row 132 preview](../prologue/00-many-scales.md#prologue-preview-row-132) · "
    "[prologue row 132 closing stitch](../prologue/00-many-scales.md#row-132-closing-stitch) · "
    "[epilogue row 132 closing loop](../epilogue/multiscale.md#row-132-closing-loop) | "
    "Row 68 closed but row 52 VII.3 → VIII.1 opening hinge feels disconnected from verified homogenization meta prelude capstone on the capstone path — "
    "read row 68 + row 131 or row 112 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[row 132 baby picture](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion) |\n"
)


def main():
    prologue_path = ROOT / "prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = prologue.replace(
        "| Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 131) |",
        "| Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 132) |",
    )
    prologue = prologue.replace(
        "[Preface: row 131 skill checkpoint](../preface.md#skill-navigation-row-132)",
        "[Preface: row 132 skill checkpoint](../preface.md#skill-navigation-row-132)",
    )
    prologue = prologue.replace(
        "[Row 68 → Row 111 atomistic meta prelude capstone reunion index]",
        "[Row 68 → Row 112 atomistic meta prelude capstone reunion index]",
    )
    if "{#row-131-closing-stitch}" not in prologue:
        prologue = prologue.replace(
            "**Row 131 closing stitch",
            PROLOGUE_STITCH_131 + "**Row 131 closing stitch",
            1,
        )
    if '<span id="prologue-preview-row-131">' not in prologue:
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-130"></span>Row 130 preview',
            PROLOGUE_PREVIEW_131 + '| <span id="prologue-preview-row-130"></span>Row 130 preview',
            1,
        )
    prologue_path.write_text(prologue)

    epilogue_path = ROOT / "epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    import re

    epilogue = re.sub(
        r"\n### Row 132 closing loop \(Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion\) \{[^}]+\}.*?(?=\n\n### Row 130 closing loop)",
        ROW132_EPILOGUE + "\n",
        epilogue,
        count=1,
        flags=re.S,
    )
    epilogue_path.write_text(epilogue)

    sources_path = ROOT / "appendix/chapters/sources.md"
    sources = sources_path.read_text()
    dup = "| 131 | Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) | [Row 68 → Row 111 homogenization meta prelude capstone reunion index](#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131)"
    if sources.count(dup) > 1:
        sources = sources.replace(dup + sources[sources.index(dup) + len(dup) : sources.index(dup, sources.index(dup) + 1)].split("\n", 1)[0], dup, 1)
    if "| 132 | Row 68 → Row 112" not in sources:
        sources = sources.replace(
            "| 131 | Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) |",
            SOURCES_ROW132 + "| 131 | Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) |",
            1,
        )
    sources_path.write_text(sources)

    mem_path = ROOT / "appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "### Row 131 baby picture" not in mem:
        mem = mem.replace("### Row 132 baby picture", MEMORY_BABY_131 + "### Row 132 baby picture", 1)
    import re as re2

    mem = re2.sub(
        r"### Row 132 baby picture \(Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion\) \{[^}]+\}.*?(?=\n\n\n\n### Act VI baby picture)",
        MEMORY_BABY_132.strip() + "\n\n\n",
        mem,
        count=1,
        flags=re2.S,
    )
    if "| 132 | Meta |" not in mem:
        mem = mem.replace(
            "| 131 | Meta | [Row 68 → Row 111 homogenization meta prelude capstone reunion index]",
            MEMORY_ROW132 + "| 131 | Meta | [Row 68 → Row 111 homogenization meta prelude capstone reunion index]",
            1,
        )
    mem_path.write_text(mem)
    print("fixed row 132 artifacts")


if __name__ == "__main__":
    main()
