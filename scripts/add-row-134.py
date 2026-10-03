#!/usr/bin/env python3
"""Apply row 134 meta-stitch and backfill incomplete row 133 prologue/memory pieces."""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / "scripts/add-row-133.py"))


def tx(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


P = [
    ("133", "134"),
    ("132", "133"),
    ("113", "114"),
    ("53", "54"),
    ("Row 113", "Row 114"),
    ("row 113", "row 114"),
    (
        "dynamics meta prelude capstone reunion (row 133)",
        "export meta prelude capstone reunion (row 134)",
    ),
    (
        "Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone",
        "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
    ),
    (
        "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
    ),
    (
        "row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion",
        "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
    ),
    (
        "atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53",
        "dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54",
    ),
    (
        "EAM foundation is clean on the capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone",
        "NPT dynamics is clean on the capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone",
    ),
]

ROW134_PREFACE = """
### Row 134 skill checkpoint — Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion audit {#skill-navigation-row-134}

This checkpoint closes the **Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion** chain — the reader meta-stitch when row 68 closed the dual midpoint prelude (part-boundary gate row 67 + VI.4 → VII.0 meta row 48 + intermission → Bridge chain), and [row 133](preface.md#skill-navigation-row-133) or [row 114](preface.md#skill-navigation-row-114) closed the dynamics meta prelude capstone / export meta prelude hinge on the capstone path (VIII.2 Bridge → VIII.3 pedigree recited, [NPT Lab act](part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` beside [dynamics export manifest](part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3) at \\(T_w\\), one NPT → pedigree arc under `writings/md` chapters 02–03 after verified dynamics meta prelude capstone), but **row 54 still opens like standalone coarse-graining homework after VIII.2's NPT Lab act on the capstone path** — `./scripts/sync-writings.sh --check` passes yet [VIII.2 Bridge](part08-md/02-ensembles-integrators.md#bridge) reads correctly in isolation from [VIII.3 pedigree checklist](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3), consumer columns in the checklist feel disconnected from NVE drift certificates and [`cht_export.yaml`](fixtures/cht_export.yaml), or row 54's five-step audit feels like a duplicate checklist rather than the rear-view mirror of row 133's finite-\\(T\\) dynamics → yaml handoff turn at the export meta prelude capstone boundary inside the coupling gate on the capstone path. The [Row 68 → Row 114 export meta prelude capstone reunion index](appendix/sources.md#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) and [memory sheet row 134 baby picture](appendix/memory-sheet.md#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion) are the **navigation halves**; [row 68](preface.md#skill-navigation-row-68) (midpoint prelude gate) and [row 54](preface.md#skill-navigation-row-54) (VIII.2 → VIII.3 meta gate) are the **audit halves**. Row 134 does not replace row 68, row 54, row 133, row 114, row 94, row 74, or row 35 — it reunites **verified dynamics meta prelude capstone closure (row 133) with the full-book VIII.2 → VIII.3 export meta reunion (row 54)** when `cu.elastic/` and row 54 meta both read correctly alone but not as one continuous NPT afternoon → pedigree checklist before row 55 electronic audit meta prelude opens on the capstone path at \\(T_w\\).

| Step | Skill on the Row 68 ↔ Row 54 reunion (capstone path) | Minimal artifact |
|------|------------------------------------------------------|------------------|
| 1 — Row 68 gate | Confirm row 68 closed ([Row 67 → Row 48 reunion index](appendix/sources.md#row67-row48-midpoint-prelude-reunion-index-row-68) recited); `./scripts/sync-writings.sh --check` green | Midpoint Bridge chain recited before export meta prelude capstone |
| 2 — Dynamics meta prelude capstone / export meta prelude gate | Confirm [row 133](preface.md#skill-navigation-row-133) or [Row 68 → Row 94 export meta prelude reunion index (row 114)](appendix/sources.md#row68-row94-export-meta-prelude-reunion-index-row-114) recited | NPT archive at \\(T_w\\) before VIII.2 Bridge → pedigree after verified dynamics meta prelude capstone |
| 3 — Bridge recitation | Read [VIII.2 Bridge](part08-md/02-ensembles-integrators.md#bridge) through [VIII.3 opening hinge from VIII.2](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) aloud | "Trajectories compress into handoff tables with DFT pedigree gates" |
| 4 — Scene audit | Open [VIII.2 Scene](part08-md/02-ensembles-integrators.md#scene-thermometers-in-a-nanoscale-lab) then [VIII.3 Scene](part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough); confirm [NPT Lab act steps 1–7](part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) | Same wire; bulk NPT → notch EAM trust |
| 5 — Row 54 meta gate | Confirm [VIII.2 → VIII.3 reunion index (row 54)](appendix/sources.md#viii2-viii3-opening-hinge-reunion-index-row-54) five-step audit | Dynamics → pedigree reads continuous |

**Row 134 three-way audit (prologue preview ↔ this checkpoint ↔ workflow exam).**

| Step | Prologue preview ([row 134](prologue/00-many-scales.md#prologue-preview-row-134)) | This checkpoint (above) | Workflow exam ([midpoint row](epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book)) |
|------|--------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| 1 | Name row 68 closed before export meta prelude capstone | Step 1 — row 68 gate | Midpoint prelude recited |
| 2 | Name dynamics meta prelude capstone before VIII.2 Bridge | Step 2 — dynamics meta prelude capstone / export meta prelude gate | `cu.elastic/` before pedigree checklist on capstone path |
| 3 | Name VIII.2 Bridge as chapter exit | Step 3 — Bridge recitation | Dumps ≠ handoff tables |
| 4 | Name dynamics manifest before VIII.3 Scene | Step 4 — Scene audit | EAM fails at notch root |
| 5 | [Row 68 → Row 114 reunion index](appendix/sources.md#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) recitation | Step 5 — row 54 meta gate | VIII.2 → VIII.3 reads continuous |

**When to pause.** Read the [prologue row 134 closing stitch](prologue/00-many-scales.md#row-134-closing-stitch) first when row 133 closed but row 54 VIII.2 → VIII.3 reunion still feels like export homework disconnected from verified dynamics meta prelude capstone on the capstone path — it names the dual reunion before the electronic audit meta reunion. Then read the [prologue row 134 preview](prologue/00-many-scales.md#prologue-preview-row-134) when `cu.elastic/` exists on the capstone path but consumer columns in the checklist are empty after row 133. Return to the [Row 68 → Row 114 reunion index](appendix/sources.md#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) when row 133 and row 54 both verify individually but **dynamics meta prelude capstone and VIII.2 → VIII.3 opening hinge still feel like separate stories** — the break is usually skipping [VIII.2's Bridge](part08-md/02-ensembles-integrators.md#bridge), not missing EAM-fit algebra. Read the [memory sheet row 134 baby picture](appendix/memory-sheet.md#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion) when opening [row 115](preface.md#skill-navigation-row-115) before row 55 closes on the capstone path; read the [epilogue row 134 closing loop](epilogue/multiscale.md#row-134-closing-loop) when the competence loop closes. When row 133 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 114](preface.md#skill-navigation-row-114) when dynamics meta capstone is clean but export meta capstone still lags on the opening-hinge path, to [row 94](preface.md#skill-navigation-row-94) for the Row 68 ↔ Row 54 export opening prelude audit alone, to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags after verified EAM foundation on the capstone path, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync.

"""

PROLOGUE_COMPASS = tx(ns["PROLOGUE_COMPASS"], P)
PROLOGUE_PREVIEW_134 = tx(
    ns["PROLOGUE_PREVIEW_133"],
    P
    + [
        ("Row 133 preview", "Row 134 preview"),
        ("prologue-preview-row-133", "prologue-preview-row-134"),
        ("VIII.1 → VIII.2 meta (row 54)", "VIII.2 → VIII.3 meta (row 54)"),
        ("Bridge → NPT chain", "Bridge → pedigree chain"),
        (
            "foundation manifest and thermostat sections",
            "dynamics manifest and coarse-graining sections",
        ),
        ("row-133-closing-stitch", "row-134-closing-stitch"),
        (
            "part08-md/01-potentials-phase-space.md#bridge",
            "part08-md/02-ensembles-integrators.md#bridge",
        ),
        (
            "part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2",
            "part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3",
        ),
    ],
)
PROLOGUE_STITCH_134 = (
    "**Row 134 closing stitch (Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-134-closing-stitch} "
    "When row 133 closed — dynamics meta prelude capstone verified, row 132 or row 53 recited on the capstone path, and VIII.1 Bridge → VIII.2 NPT recited with "
    "[NPT Lab act](../part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` — but **row 54 VIII.2 → VIII.3 opening hinge still opens like standalone coarse-graining homework after the thermostat Scene on the capstone path** — "
    "`writings/md` chapters 02 and 03 build as separate reading acts, pedigree checklist consumer columns feel disconnected from [dynamics export manifest](../part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3) and NVE drift certificates at \\(T_w\\), or row 54's Bridge → export audit feels disconnected from row 133's finite-\\(T\\) dynamics → yaml handoff turn while the unified HTML reads smoothly — "
    "the [preface row 134 When-to-pause opening sentence](../preface.md#skill-navigation-row-134) names the dual reunion before electronic audit meta reunion; read [preface row 134](../preface.md#skill-navigation-row-134), then the "
    "[Row 68 → Row 114 reunion index](../appendix/sources.md#row68-row114-export-meta-prelude-capstone-reunion-index-row-134), then "
    "[epilogue row 134 closing loop](../epilogue/multiscale.md#row-134-closing-loop) before row 55 electronic audit meta prelude capstone opens.\n\n"
)

EPILOGUE_LOOP = tx(
    ns["EPILOGUE_LOOP"],
    P
    + [
        ("potentials → ensembles", "ensembles → coarse-graining"),
        (
            "atomistic meta prelude capstone closure (row 133)",
            "dynamics meta prelude capstone closure (row 133)",
        ),
        ("Row 68 → Row 53 meta (row 114)", "Row 68 → Row 54 meta (row 114)"),
        ("screw-core → NPT afternoon", "NPT → pedigree afternoon"),
        ("row 54 export meta prelude opens", "row 55 electronic audit meta prelude opens"),
        (
            "thermostat homework after the EAM Lab act",
            "coarse-graining homework after the NPT Lab act on the capstone path",
        ),
        (
            "VIII.1 Bridge and VIII.2 ensemble",
            "VIII.2 Bridge and VIII.3 pedigree",
        ),
        ("row 132 closed atomistic", "row 133 closed dynamics meta prelude"),
        (
            "row 53 feels like thermostat homework after row 133",
            "row 54 feels like export homework after row 133",
        ),
        ("VIII.1 Bridge", "VIII.2 Bridge"),
        ("VIII.2 plot spine", "VIII.3 plot spine"),
        ("VIII.2 NPT Lab act", "pedigree checklist"),
        ("row 53 closing loop", "row 54 closing loop"),
        ("row 73", "row 74"),
        ("dynamics reunion", "export reunion"),
        (
            "atomistic meta prelude capstone",
            "dynamics meta prelude capstone",
        ),
        ("EAM Lab act steps 6–7", "NPT Lab act steps 1–7"),
        (
            "cu_eam_a0.txt` and linked `cu.foundation/`",
            "`cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` beside [dynamics export manifest](../part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3)",
        ),
        (
            "row 68 ↔ row 53 reunion on the capstone path) with row 114 (opening-hinge prelude stitch alone) — row 114 names **Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion**; row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
            "row 68 ↔ row 54 reunion on the capstone path) with row 114 (opening-hinge prelude stitch alone) — row 114 names **Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion**; row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
        ),
        (
            "Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            "Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 133](#row-133-closing-loop) when dynamics meta prelude capstone still lags after row 132 on the capstone path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
        ),
    ],
)
EPILOGUE_LOOP = EPILOGUE_LOOP.replace("Row 133 closing loop", "Row 134 closing loop").replace(
    "row-133-closing-loop", "row-134-closing-loop"
)

SOURCES_TABLE = tx(
    ns["SOURCES_TABLE"],
    P
    + [
        (
            "atomistic meta prelude capstone ↔ row 53 meta",
            "dynamics meta prelude capstone ↔ row 54 meta",
        ),
        ("row 53 VIII.1 → VIII.2", "row 54 VIII.2 → VIII.3"),
        (
            "atomistic meta prelude capstone on the capstone path",
            "dynamics meta prelude capstone on the capstone path",
        ),
        (
            "VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53",
            "VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54",
        ),
        ("preface row 53", "preface row 54"),
    ],
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    row133_tail_old = (
        "When row 132 is complete, proceed to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone is clean but dynamics meta prelude capstone still lags after verified EAM foundation on the capstone path, to [row 113](preface.md#skill-navigation-row-113) when atomistic meta capstone is clean but dynamics meta capstone still lags on the opening-hinge path, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the opening-hinge path alone, to [row 132](preface.md#skill-navigation-row-132) when homogenization meta prelude capstone still lags after verified polycrystal closure on the capstone path, to [row 53](preface.md#skill-navigation-row-53) when only VIII.1 → VIII.2 stalls, or extend prose only under `writings/` then sync."
    )
    row133_tail_new = (
        "When row 133 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 114](preface.md#skill-navigation-row-114) when dynamics meta capstone is clean but export meta capstone still lags on the opening-hinge path, to [row 113](preface.md#skill-navigation-row-113) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge path alone, to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags after verified EAM foundation on the capstone path, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync."
    )
    if "skill-navigation-row-134" not in preface:
        preface = preface.replace(row133_tail_old, row133_tail_new)
        preface = preface.replace(anchor, ROW134_PREFACE + anchor)
        preface_path.write_text(preface)
        print("preface: row 134")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "row-132-closing-stitch" not in prologue:
        prologue = prologue.replace(
            "**Row 112 closing stitch",
            ns["PROLOGUE_STITCH_133"] + "**Row 112 closing stitch",
        )
    if '<span id="prologue-preview-row-132">' not in prologue:
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-131"></span>Row 131 preview',
            ns["PROLOGUE_PREVIEW_132"]
            + '| <span id="prologue-preview-row-131"></span>Row 131 preview',
        )
    if "row-133-closing-stitch" not in prologue:
        prologue = prologue.replace(
            "**Row 113 closing stitch",
            ns["PROLOGUE_STITCH_133_CLOSING"] + "**Row 113 closing stitch",
        )
    if '<span id="prologue-preview-row-133">' not in prologue:
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-132"></span>Row 132 preview',
            ns["PROLOGUE_PREVIEW_133"]
            + '| <span id="prologue-preview-row-132"></span>Row 132 preview',
        )
    if '<span id="prologue-preview-row-134">' not in prologue:
        needle = "| Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 133) |"
        idx = prologue.find(needle)
        if idx < 0:
            raise SystemExit("prologue compass row 133 not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-134-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 114 closing stitch",
                PROLOGUE_STITCH_134 + "**Row 114 closing stitch",
            )
        if '<span id="prologue-preview-row-133">' in prologue:
            prologue = prologue.replace(
                '| <span id="prologue-preview-row-133"></span>Row 133 preview',
                PROLOGUE_PREVIEW_134
                + '| <span id="prologue-preview-row-133"></span>Row 133 preview',
            )
        else:
            prologue = prologue.replace(
                '| <span id="prologue-preview-row-132"></span>Row 132 preview',
                ns["PROLOGUE_PREVIEW_133"]
                + PROLOGUE_PREVIEW_134
                + '| <span id="prologue-preview-row-132"></span>Row 132 preview',
            )
        print("prologue: row 134")
    prologue_path.write_text(prologue)

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-134-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "\n### Row 133 closing loop (Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
            EPILOGUE_LOOP
            + "\n### Row 133 closing loop (Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        )
        epilogue = epilogue.replace(
            "Proceed to [row 114](#row-114-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            "Proceed to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            1,
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: row 134")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row114-export-meta-prelude-capstone-reunion-index-row-134" not in sources:
        block = sources.split(
            "## Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion index (row 114)"
        )[1].split("## Row 68 → Row 95")[0]
        block134 = tx(
            block,
            [
                ("row 114", "row 134"),
                ("Row 114", "Row 134"),
                ("row 113", "row 133"),
                ("Row 113", "Row 133"),
                ("dynamics meta capstone", "dynamics meta prelude capstone"),
                ("export meta capstone", "export meta prelude capstone"),
                (
                    "export meta prelude reunion index (row 114)",
                    "export meta prelude capstone reunion index (row 134)",
                ),
                (
                    "row68-row94-export-meta-prelude-reunion-index-row-114",
                    "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
                ),
                (
                    "row-114-baby-picture-row68-row94-export-meta-prelude-reunion",
                    "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
                ),
                ("skill-navigation-row-114", "skill-navigation-row-134"),
                (
                    "Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion",
                    "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion",
                ),
                ("row 113 or row 94", "row 133 or row 114"),
                (
                    "VIII.1 Bridge → VIII.2 NPT recited",
                    "VIII.2 Bridge → VIII.3 pedigree recited on the capstone path",
                ),
                (
                    "export meta capstone boundary",
                    "export meta prelude capstone boundary",
                ),
                (
                    "Row 113 reunion (dynamics meta capstone)",
                    "Row 133 reunion (dynamics meta prelude capstone)",
                ),
                (
                    "row68-row93-dynamics-meta-prelude-reunion-index-row-113",
                    "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
                ),
                (
                    "Row 94 reunion (opening prelude)",
                    "Row 114 reunion (meta prelude)",
                ),
                (
                    "row68-row74-export-meta-prelude-reunion-index-row-94",
                    "row68-row94-export-meta-prelude-reunion-index-row-114",
                ),
                (
                    "Row 113 gate + Bridge before VIII.3",
                    "Row 133 gate + Bridge before VIII.3",
                ),
                (
                    "Recite row 68 gate, then dynamics meta capstone, then row 54",
                    "Recite row 68 gate, then dynamics meta prelude capstone, then row 54",
                ),
                (
                    "verified dynamics meta capstone closure with the export meta reunion",
                    "verified dynamics meta prelude capstone closure with the export meta reunion",
                ),
                (
                    "row 113 verified VIII.1 → VIII.2 on NPT at \\(T_w\\)",
                    "row 133 verified VIII.1 → VIII.2 on NPT at \\(T_w\\) on the capstone path",
                ),
                (
                    "Row 68 → Row 54 move |",
                    "Row 68 → Row 54 move (capstone path) |",
                ),
            ],
        )
        block134 = (
            "## Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion index (row 134) {#row68-row114-export-meta-prelude-capstone-reunion-index-row-134}"
            + block134.split("{#row68-row94-export-meta-prelude-reunion-index-row-114}", 1)[-1]
        )
        sources = sources.replace(
            "| 133 | Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone",
            SOURCES_TABLE + "| 133 | Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 133)",
            block134
            + "## Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 133)",
        )
        extra = (
            "[row 134](#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) reunites **dynamics meta prelude capstone with the export meta prelude capstone boundary** "
            "when row 133 closed dynamics meta prelude capstone at verified NPT archive on the capstone path but `cu.elastic/` and VIII.2 → VIII.3 opening hinge still read like separate courses after verified export meta prelude meta;"
        )
        if extra not in sources:
            sources = sources.replace(
                "when row 132 closed atomistic meta prelude capstone at verified EAM foundation on the capstone path but `cu.foundation/` and VIII.1 → VIII.2 opening hinge still read like separate courses after verified dynamics meta prelude meta;",
                "when row 132 closed atomistic meta prelude capstone at verified EAM foundation on the capstone path but `cu.foundation/` and VIII.1 → VIII.2 opening hinge still read like separate courses after verified dynamics meta prelude meta; "
                + extra,
            )
        sources_path.write_text(sources)
        print("sources: row 134")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    memory_baby_133 = ns["MEMORY_BABY"]
    memory_baby_134 = tx(
        memory_baby_133,
        P
        + [
            ("Row 133 baby picture", "Row 134 baby picture"),
            ("Atomistic meta prelude capstone row 133", "Dynamics meta prelude capstone row 133"),
            ("VIII.1 Bridge", "VIII.2 Bridge"),
            ("row 53 meta gate", "row 54 meta gate"),
            (
                "row 53's VIII.1 Bridge → NPT handoff",
                "row 54's VIII.2 Bridge → pedigree handoff",
            ),
            (
                "atomistic meta prelude capstone / dynamics meta prelude",
                "dynamics meta prelude capstone / export meta prelude",
            ),
            ("preface row 132", "preface row 133"),
            ("preface row 113", "preface row 114"),
            ("preface row 53", "preface row 54"),
            ("EAM Lab act steps 6–7", "NPT Lab act steps 1–7"),
            (
                "cu.foundation/` before row 54 export meta prelude capstone opens",
                "`cu.elastic/` before row 55 electronic audit meta prelude capstone opens",
            ),
            (
                "row 114 export meta capstone or row 54 export reunion",
                "row 115 electronic audit meta capstone or row 55 electronic audit reunion",
            ),
            ("screw-core → NPT afternoon", "NPT → pedigree afternoon"),
            (
                "atomistic meta prelude capstone vs dynamics meta prelude capstones",
                "dynamics meta prelude capstone vs export meta prelude capstones",
            ),
            (
                "row 133 feels disconnected from row 132",
                "row 134 feels disconnected from row 133",
            ),
        ],
    )
    if "### Row 133 baby picture" not in mem:
        mem = mem.replace(
            "\n\n\n\n\n### Act VI baby picture (ME 412 coupling ladder)",
            memory_baby_133 + "\n\n### Act VI baby picture (ME 412 coupling ladder)",
        )
    if "### Row 134 baby picture" not in mem:
        mem = mem.replace(
            "### Act VI baby picture (ME 412 coupling ladder)",
            memory_baby_134 + "\n\n### Act VI baby picture (ME 412 coupling ladder)",
        )
    if "| 133 | Meta |" not in mem:
        mem = mem.replace(
            "[row 132 baby picture](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row 132 baby picture](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion) |\n"
            + ns["MEMORY_TABLE"]
            + tx(ns["MEMORY_TABLE"], P)
            + "| 93 | Meta |",
        )
    if "When row 133 closed but export meta reunion still lags" not in mem:
        mem = mem.replace(
            "When row 132 closed but dynamics meta reunion still lags on the capstone path, switch to [row 133](#row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion).",
            "When row 132 closed but dynamics meta reunion still lags on the capstone path, switch to [row 133](#row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion). When row 133 closed but export meta reunion still lags on the capstone path, switch to [row 134](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion).",
        )
    mem_path.write_text(mem)
    print("memory: row 134")


if __name__ == "__main__":
    main()
