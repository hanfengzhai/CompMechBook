#!/usr/bin/env python3
"""Add row 192 meta-stitch (Row 68 → Row 172 ↔ Row 52 atomistic meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump172_to_192(text: str) -> str:
    """Transform row-172 capstone-path meta copy to row 192 (152→172 inner, 191 gate)."""
    out = text.replace("row 173", "TEMP_ROW173")
    repl = [
        ("Row 68 → Row 152 Row 68 → Row 52", "Row 68 → Row 172 Row 68 → Row 52"),
        (
            "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
            "TEMP_ROW192_ATOM_INDEX",
        ),
        (
            "row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion",
            "row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion",
        ),
        ("### Row 172 skill checkpoint", "### Row 192 skill checkpoint"),
        ("skill-navigation-row-172", "skill-navigation-row-192"),
        ("prologue-preview-row-172", "prologue-preview-row-192"),
        ("row-172-closing-stitch", "row-192-closing-stitch"),
        ("row-172-closing-loop", "row-192-closing-loop"),
        ("Row 172 three-way audit", "Row 192 three-way audit"),
        (
            "[row 171](preface.md#skill-navigation-row-171) or [row 152](preface.md#skill-navigation-row-152)",
            "[row 191](preface.md#skill-navigation-row-191) or [row 172](preface.md#skill-navigation-row-172)",
        ),
        (
            "[row 171](preface.md#skill-navigation-row-171) or [Row 68 → Row 152 atomistic meta prelude capstone reunion index (row 172)](appendix/sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172)",
            "[row 191](preface.md#skill-navigation-row-191) or [Row 68 → Row 172 atomistic meta prelude capstone reunion index (row 192)](appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192)",
        ),
        (
            "verified homogenization meta prelude capstone closure on the full capstone path (row 171)",
            "verified homogenization meta prelude capstone closure on the full capstone path (row 191)",
        ),
        (
            "verified homogenization meta prelude capstone closure (row 171)",
            "verified homogenization meta prelude capstone closure (row 191)",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW192_ATOM_INDEX",
        "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192",
    )
    out = out.replace("Row 172 does not replace", "Row 192 does not replace")
    out = out.replace("When row 172 is complete", "When row 192 is complete")
    out = out.replace("When row 171 closed", "When row 191 closed")
    out = out.replace("after row 172 alone", "after row 192 alone")
    out = out.replace("Recite [preface row 171]", "Recite [preface row 191]")
    out = out.replace("row 171 or row 152 recited", "row 191 or row 172 recited")
    out = out.replace("row 171 and row 52", "row 191 and row 52")
    out = out.replace("after row 171", "after row 191")
    out = out.replace("row 171's polycrystal", "row 191's polycrystal")
    out = out.replace("row 112", "row 132")
    out = out.replace("Row 112", "Row 132")
    out = out.replace("row 132", "row 152")
    out = out.replace("Row 132", "Row 152")
    out = out.replace(
        "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132",
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
    )
    out = out.replace(
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        "TEMP_ATOM152IDX",
    )
    out = out.replace("row 152", "row 172")
    out = out.replace("Row 152", "Row 172")
    out = out.replace(
        "TEMP_ATOM152IDX",
        "row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172",
    )
    out = out.replace("row 131", "row 151")
    out = out.replace("Row 131", "Row 151")
    out = out.replace(
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    out = out.replace("row 151", "row 171")
    out = out.replace("Row 151", "Row 171")
    out = out.replace("row 171", "row 191")
    out = out.replace("Row 171", "Row 191")
    out = out.replace(
        "[row 193](preface.md#skill-navigation-row-173)",
        "[row 173](preface.md#skill-navigation-row-173)",
    )
    out = out.replace("row 192 or row 172", "row 191 or row 172")
    out = out.replace("memory sheet row 172 baby picture", "memory sheet row 192 baby picture")
    out = out.replace("prologue row 172 closing stitch", "prologue row 192 closing stitch")
    out = out.replace("prologue row 172 preview", "prologue row 192 preview")
    out = out.replace("epilogue row 172 closing loop", "epilogue row 192 closing loop")
    out = out.replace(
        "reunion index (row 172)](appendix/sources.md#row68-row152-atomistic-meta-prelude-capstone-reunion-index-row-172)",
        "reunion index (row 192)](appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192)",
    )
    out = out.replace(
        "Prologue preview ([row 172](prologue/00-many-scales.md#prologue-preview-row-192))",
        "Prologue preview ([row 192](prologue/00-many-scales.md#prologue-preview-row-192))",
    )
    out = out.replace("TEMP_ROW173", "row 173")
    return out


def extract_preface_row172(preface: str) -> str:
    start = preface.index("### Row 172 skill checkpoint")
    end = preface.index("\n\n### Row 173 skill checkpoint", start)
    return preface[start:end]


ROW192_PREFACE = bump172_to_192(
    extract_preface_row172((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 192) | "
    "[Preface: row 192 skill checkpoint](../preface.md#skill-navigation-row-192) · "
    "[Row 68 → Row 172 atomistic meta prelude capstone reunion index](../appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192) · "
    "[memory sheet row 192 baby picture](../appendix/memory-sheet.md#row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion) · "
    "[prologue row 192 preview row](#prologue-preview-row-192); [prologue row 192 closing stitch](#row-192-closing-stitch); "
    "[epilogue row 192 closing loop](../epilogue/multiscale.md#row-192-closing-loop) — "
    "read row 68 gate + row 191 or row 172 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud "
    "when polycrystal handoff is clean on the full capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row172_stitch_line = next(
    line for line in _prologue.splitlines() if line.startswith("**Row 172 closing stitch")
)
PROLOGUE_STITCH = bump172_to_192(_row172_stitch_line) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-192"></span>Row 192 preview (Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.3 → VIII.1 meta (row 52) must be read together with the Bridge → phase-space chain after verified homogenization meta prelude capstone on the full capstone path before DAMASK exports and LAMMPS EAM tables feel like separate courses | "
    'One sentence: "read row 68 gate + row 191 or row 172 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud when polycrystal handoff is clean on the full capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path" — '
    "[preface row 192 skill checkpoint](../preface.md#skill-navigation-row-192); [prologue row 192 closing stitch](#row-192-closing-stitch); "
    "[Row 68 → Row 172 reunion index](../appendix/sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192); "
    "[memory sheet row 192 baby picture](../appendix/memory-sheet.md#row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion); "
    "[VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii); "
    "[VII.3 opening hinge to VIII.1](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1); "
    "[preface row 52 skill checkpoint](../preface.md#skill-navigation-row-52); "
    "[preface row 191 skill checkpoint](../preface.md#skill-navigation-row-191); "
    "[epilogue row 192 closing loop](../epilogue/multiscale.md#row-192-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump172_to_192(
    "### Row 172 closing loop"
    + _epilogue.split("### Row 172 closing loop")[1].split("### Row 173 closing loop")[0]
)

SOURCES_TABLE = (
    "| 192 | Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone on full capstone path ↔ row 52 meta) | "
    "[Row 68 → Row 172 atomistic meta prelude capstone reunion index](#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192) · "
    "[preface row 192](../preface.md#skill-navigation-row-192) · "
    "[prologue row 192 preview](../prologue/00-many-scales.md#prologue-preview-row-192) · "
    "[prologue row 192 closing stitch](../prologue/00-many-scales.md#row-192-closing-stitch) · "
    "[epilogue row 192 closing loop](../epilogue/multiscale.md#row-192-closing-loop) · "
    "[memory sheet row 192 baby picture](memory-sheet.md#row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the full capstone path** — "
    "read row 68 + row 191 or row 172 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[preface row 52](../preface.md#skill-navigation-row-52) |\n"
)

SOURCES_INDEX = bump172_to_192(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)")[1]
    .split("## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 192)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 192 | Meta | [Row 68 → Row 172 atomistic meta prelude capstone reunion index](sources.md#row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192) · "
    "[preface row 192 skill checkpoint](../preface.md#skill-navigation-row-192) · "
    "[prologue row 192 preview](../prologue/00-many-scales.md#prologue-preview-row-192) · "
    "[prologue row 192 closing stitch](../prologue/00-many-scales.md#row-192-closing-stitch) · "
    "[epilogue row 192 closing loop](../epilogue/multiscale.md#row-192-closing-loop) | "
    "Row 68 closed but row 52 atomistic meta reunion feels disconnected from verified homogenization meta prelude capstone on the full capstone path — "
    "read row 68 + row 191 or row 172 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
    "[row 192 baby picture](#row-192-baby-picture-row68-row172-atomistic-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump172_to_192(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 172 baby picture")[1]
    .split("### Row 173 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 192 baby picture (Row 68 → Row 172 Row 68 → Row 52 atomistic meta prelude capstone reunion)"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 192 baby picture" + MEMORY_BABY
)

ROW191_TAIL_OLD = (
    "When row 191 is complete, proceed to [row 172](preface.md#skill-navigation-row-172) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 152](preface.md#skill-navigation-row-132) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 171](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 171](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 190](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 51](preface.md#skill-navigation-row-51) when only VII.2 → VII.3 stalls, or extend prose only under `writings/` then sync."
)
ROW191_TAIL_NEW = (
    "When row 191 is complete, proceed to [row 192](preface.md#skill-navigation-row-192) when LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone on the full capstone path, to [row 172](preface.md#skill-navigation-row-172) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the opening-hinge capstone path alone, to [row 152](preface.md#skill-navigation-row-152) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge prelude path alone, to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 151](preface.md#skill-navigation-row-151) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 190](preface.md#skill-navigation-row-190) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the full capstone path, to [row 52](preface.md#skill-navigation-row-52) when only VII.3 → VIII.1 stalls, or extend prose only under `writings/` then sync."
)

ROW191_STITCH_OLD = (
    "before row 172 atomistic meta prelude capstone reunion opens on the full capstone path."
)
ROW191_STITCH_NEW = (
    "before row 192 atomistic meta prelude capstone reunion opens on the full capstone path."
)

ROW191_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 172](#row-172-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 171 on the full capstone path,"
)
ROW191_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 192](#row-192-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 191 on the full capstone path,"
)

ROW191_BABY_OLD = (
    "row 171 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 172 atomistic meta prelude capstone opens on the full capstone path**"
)
ROW191_BABY_NEW = (
    "row 191 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 192 atomistic meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 192 skill checkpoint" in preface and preface.index("### Row 192 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 192 already present")
    else:
        if ROW191_TAIL_OLD not in preface:
            raise SystemExit("row 191 tail proceed string not found")
        preface = preface.replace(ROW191_TAIL_OLD, ROW191_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 172](preface.md#skill-navigation-row-172) before row 52 closes on the full capstone path",
            "when opening [row 192](preface.md#skill-navigation-row-192) before row 52 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW192_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 192")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-192" not in prologue:
        needle = "| Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 191) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 191 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-192-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 191 closing stitch",
                PROLOGUE_STITCH + "**Row 191 closing stitch",
                1,
            )
            if "row-192-closing-stitch" not in prologue:
                prologue = prologue.replace(
                    "**Row 172 closing stitch",
                    PROLOGUE_STITCH + "**Row 172 closing stitch",
                    1,
                )
        preview_anchor = '| <span id="prologue-preview-row-191"></span>Row 191 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 191 not found")
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        if ROW191_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW191_STITCH_OLD, ROW191_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 192")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-192-closing-loop" not in epilogue:
        if ROW191_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW191_EPILOGUE_PROCEED_OLD, ROW191_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 192")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row172-atomistic-meta-prelude-capstone-reunion-index-row-192" not in sources:
        sources = sources.replace(
            "| 172 | Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone",
            SOURCES_TABLE + "| 172 | Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)",
            SOURCES_INDEX + "## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 192")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-192-baby-picture-row68-row172" not in memory:
        memory = memory.replace(
            "| 191 | Meta | [Row 68 → Row 171 homogenization meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 191 | Meta | [Row 68 → Row 171 homogenization meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 172 baby picture (Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion}",
            MEMORY_BABY
            + "### Row 172 baby picture (Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-172-baby-picture-row68-row152-atomistic-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW191_BABY_OLD in memory:
            memory = memory.replace(ROW191_BABY_OLD, ROW191_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 192")


if __name__ == "__main__":
    main()
