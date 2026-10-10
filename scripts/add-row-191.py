#!/usr/bin/env python3
"""Add row 191 meta-stitch (Row 68 → Row 171 ↔ Row 51 homogenization meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump171_to_191(text: str) -> str:
    """Transform row-171 capstone-path meta copy to row 191 (151→171 inner, 190 gate)."""
    out = text.replace("row 172", "TEMP_ROW172")
    repl = [
        ("Row 68 → Row 151 Row 68 → Row 51", "Row 68 → Row 171 Row 68 → Row 51"),
        (
            "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
            "TEMP_ROW191_HOMOG_INDEX",
        ),
        (
            "row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion",
            "row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion",
        ),
        ("### Row 171 skill checkpoint", "### Row 191 skill checkpoint"),
        ("skill-navigation-row-171", "skill-navigation-row-191"),
        ("prologue-preview-row-171", "prologue-preview-row-191"),
        ("row-171-closing-stitch", "row-191-closing-stitch"),
        ("row-171-closing-loop", "row-191-closing-loop"),
        ("Row 171 three-way audit", "Row 191 three-way audit"),
        (
            "[row 170](preface.md#skill-navigation-row-170) or [row 151](preface.md#skill-navigation-row-151)",
            "[row 190](preface.md#skill-navigation-row-190) or [row 171](preface.md#skill-navigation-row-171)",
        ),
        (
            "[row 170](preface.md#skill-navigation-row-170) or [Row 68 → Row 151 homogenization meta prelude capstone reunion index (row 171)](appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171)",
            "[row 190](preface.md#skill-navigation-row-190) or [Row 68 → Row 171 homogenization meta prelude capstone reunion index (row 191)](appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191)",
        ),
        (
            "verified DDD meta prelude capstone closure on the full capstone path (row 170)",
            "verified DDD meta prelude capstone closure on the full capstone path (row 190)",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW191_HOMOG_INDEX",
        "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191",
    )
    out = out.replace("Row 171 does not replace", "Row 191 does not replace")
    out = out.replace("When row 171 is complete", "When row 191 is complete")
    out = out.replace("When row 170 closed", "When row 190 closed")
    out = out.replace("after row 170 alone", "after row 190 alone")
    out = out.replace("Recite [preface row 170]", "Recite [preface row 190]")
    out = out.replace("row 170 or row 151 recited", "row 190 or row 171 recited")
    out = out.replace("row 170 and row 51", "row 190 and row 51")
    out = out.replace("after row 170", "after row 190")
    out = out.replace("row 170's segment", "row 190's segment")
    out = out.replace("row 112", "row 132")
    out = out.replace("Row 112", "Row 132")
    out = out.replace("row 132", "row 152")
    out = out.replace("Row 132", "Row 152")
    out = out.replace("row 111", "row 131")
    out = out.replace("Row 111", "Row 131")
    out = out.replace(
        "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
    )
    out = out.replace("row 131", "row 151")
    out = out.replace("Row 131", "Row 151")
    out = out.replace(
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "TEMP_HOMOG151IDX",
    )
    out = out.replace("row 151", "row 171")
    out = out.replace("Row 151", "Row 171")
    out = out.replace(
        "TEMP_HOMOG151IDX",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    out = out.replace("row 150", "row 170")
    out = out.replace("Row 150", "Row 170")
    out = out.replace("row 170", "row 190")
    out = out.replace("Row 170", "Row 190")
    out = out.replace(
        "[row 291](preface.md#skill-navigation-row-190)",
        "[row 190](preface.md#skill-navigation-row-190)",
    )
    out = out.replace("row 191 or row 171", "row 190 or row 171")
    out = out.replace(
        "[row 192](preface.md#skill-navigation-row-172)",
        "[row 172](preface.md#skill-navigation-row-172)",
    )
    out = out.replace("memory sheet row 171 baby picture", "memory sheet row 191 baby picture")
    out = out.replace("prologue row 171 closing stitch", "prologue row 191 closing stitch")
    out = out.replace("prologue row 171 preview", "prologue row 191 preview")
    out = out.replace("epilogue row 171 closing loop", "epilogue row 191 closing loop")
    out = out.replace(
        "reunion index (row 171)](appendix/sources.md#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171)",
        "reunion index (row 191)](appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191)",
    )
    out = out.replace(
        "Prologue preview ([row 171](prologue/00-many-scales.md#prologue-preview-row-191))",
        "Prologue preview ([row 191](prologue/00-many-scales.md#prologue-preview-row-191))",
    )
    out = out.replace("TEMP_ROW172", "row 172")
    return out


def extract_preface_row171(preface: str) -> str:
    start = preface.index("### Row 171 skill checkpoint")
    end = preface.index("\n\n### Row 172 skill checkpoint", start)
    return preface[start:end]


ROW191_PREFACE = bump171_to_191(
    extract_preface_row171((ROOT / "writings/preface/chapters/preface.md").read_text())
) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 191) | "
    "[Preface: row 191 skill checkpoint](../preface.md#skill-navigation-row-191) · "
    "[Row 68 → Row 171 homogenization meta prelude capstone reunion index](../appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191) · "
    "[memory sheet row 191 baby picture](../appendix/memory-sheet.md#row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion) · "
    "[prologue row 191 preview row](#prologue-preview-row-191); [prologue row 191 closing stitch](#row-191-closing-stitch); "
    "[epilogue row 191 closing loop](../epilogue/multiscale.md#row-191-closing-loop) — "
    "read row 68 gate + row 190 or row 171 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud "
    "when Peach–Köhler DDD is clean on the full capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone on the full capstone path |\n"
)

_prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
_row171_stitch_line = next(
    line for line in _prologue.splitlines() if line.startswith("**Row 171 closing stitch")
)
PROLOGUE_STITCH = bump171_to_191(_row171_stitch_line) + "\n\n"

PROLOGUE_PREVIEW = (
    '| <span id="prologue-preview-row-191"></span>Row 191 preview (Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion) | '
    "Explain why midpoint closure (row 68) and VII.2 → VII.3 meta (row 51) must be read together with the Bridge → homogenization chain after verified DDD meta prelude capstone on the full capstone path before OpenDiS exports and DAMASK texture tables feel like separate courses | "
    'One sentence: "read row 68 gate + row 190 or row 171 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud when Peach–Köhler DDD is clean on the full capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone on the full capstone path" — '
    "[preface row 191 skill checkpoint](../preface.md#skill-navigation-row-191); [prologue row 191 closing stitch](#row-191-closing-stitch); "
    "[Row 68 → Row 171 reunion index](../appendix/sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191); "
    "[memory sheet row 191 baby picture](../appendix/memory-sheet.md#row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion); "
    "[VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3); "
    "[VII.2 opening hinge to VII.3](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3); "
    "[preface row 51 skill checkpoint](../preface.md#skill-navigation-row-51); "
    "[preface row 190 skill checkpoint](../preface.md#skill-navigation-row-190); "
    "[epilogue row 191 closing loop](../epilogue/multiscale.md#row-191-closing-loop) |\n"
)

_epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
EPILOGUE_LOOP = bump171_to_191(
    "### Row 171 closing loop"
    + _epilogue.split("### Row 171 closing loop")[1].split("### Row 172 closing loop")[0]
)

SOURCES_TABLE = (
    "| 191 | Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone on full capstone path ↔ row 51 meta) | "
    "[Row 68 → Row 171 homogenization meta prelude capstone reunion index](#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191) · "
    "[preface row 191](../preface.md#skill-navigation-row-191) · "
    "[prologue row 191 preview](../prologue/00-many-scales.md#prologue-preview-row-191) · "
    "[prologue row 191 closing stitch](../prologue/00-many-scales.md#row-191-closing-stitch) · "
    "[epilogue row 191 closing loop](../epilogue/multiscale.md#row-191-closing-loop) · "
    "[memory sheet row 191 baby picture](memory-sheet.md#row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 51 VII.2 → VII.3 opening hinge still feels disconnected from verified DDD meta prelude capstone on the full capstone path** — "
    "read row 68 + row 190 or row 171 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
    "[preface row 51](../preface.md#skill-navigation-row-51) |\n"
)

SOURCES_INDEX = bump171_to_191(
    (ROOT / "writings/appendix/chapters/sources.md")
    .read_text()
    .split("## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)")[1]
    .split("## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)")[0]
)
SOURCES_INDEX = (
    "## Row 68 → Row 171 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 191)"
    + SOURCES_INDEX
)

MEMORY_TABLE = (
    "| 191 | Meta | [Row 68 → Row 171 homogenization meta prelude capstone reunion index](sources.md#row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191) · "
    "[preface row 191 skill checkpoint](../preface.md#skill-navigation-row-191) · "
    "[prologue row 191 preview](../prologue/00-many-scales.md#prologue-preview-row-191) · "
    "[prologue row 191 closing stitch](../prologue/00-many-scales.md#row-191-closing-stitch) · "
    "[epilogue row 191 closing loop](../epilogue/multiscale.md#row-191-closing-loop) | "
    "Row 68 closed but row 51 homogenization meta reunion feels disconnected from verified DDD meta prelude capstone on the full capstone path — "
    "read row 68 + row 190 or row 171 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
    "[row 191 baby picture](#row-191-baby-picture-row68-row171-homogenization-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = bump171_to_191(
    (ROOT / "writings/appendix/chapters/memory-sheet.md")
    .read_text()
    .split("### Row 171 baby picture")[1]
    .split("### Row 172 baby picture")[0]
)
MEMORY_BABY = (
    "### Row 191 baby picture"
    + MEMORY_BABY.split(")", 1)[1]
    if ")" in MEMORY_BABY
    else "### Row 191 baby picture" + MEMORY_BABY
)

ROW190_TAIL_OLD = (
    "When row 190 is complete, proceed to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 151](preface.md#skill-navigation-row-151) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 150](preface.md#skill-navigation-row-150) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge prelude path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync."
)
ROW190_TAIL_NEW = (
    "When row 190 is complete, proceed to [row 191](preface.md#skill-navigation-row-191) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the full capstone path, to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge capstone path alone, to [row 151](preface.md#skill-navigation-row-151) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge prelude path alone, to [row 190](preface.md#skill-navigation-row-190) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge capstone path alone, to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge prelude path alone, to [row 50](preface.md#skill-navigation-row-50) when only VII.1 → VII.2 stalls, to [row 90](preface.md#skill-navigation-row-90) for the Row 68 ↔ Row 50 DDD opening prelude audit alone, or extend prose only under `writings/` then sync."
)

ROW190_STITCH_OLD = (
    "before row 171 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW190_STITCH_NEW = (
    "before row 191 homogenization meta prelude capstone reunion opens on the full capstone path."
)

ROW190_EPILOGUE_PROCEED_OLD = (
    "Proceed to [row 171](#row-171-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the full capstone path,"
)
ROW190_EPILOGUE_PROCEED_NEW = (
    "Proceed to [row 191](#row-191-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 190 on the full capstone path,"
)

ROW190_BABY_OLD = (
    "row 170 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before row 171 homogenization meta prelude capstone opens on the full capstone path**"
)
ROW190_BABY_NEW = (
    "row 190 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before row 191 homogenization meta prelude capstone opens on the full capstone path**"
)


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 191 skill checkpoint" in preface and preface.index("### Row 191 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 191 already present")
    else:
        if ROW190_TAIL_OLD not in preface:
            raise SystemExit("row 190 tail proceed string not found")
        preface = preface.replace(ROW190_TAIL_OLD, ROW190_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 171](preface.md#skill-navigation-row-171) before row 51 closes on the full capstone path",
            "when opening [row 191](preface.md#skill-navigation-row-191) before row 51 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + ROW191_PREFACE + copper)
        preface_path.write_text(preface)
        print("preface: added row 191")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-191" not in prologue:
        needle = "| Row 68 → Row 170 Row 68 → Row 50 DDD meta prelude capstone reunion (row 190) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 190 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-191-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 190 closing stitch",
                PROLOGUE_STITCH + "**Row 190 closing stitch",
                1,
            )
            if "row-191-closing-stitch" not in prologue:
                prologue = prologue.replace(
                    "**Row 171 closing stitch",
                    PROLOGUE_STITCH + "**Row 171 closing stitch",
                    1,
                )
        preview_anchor = '| <span id="prologue-preview-row-190"></span>Row 190 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview row 190 not found")
        prologue = prologue.replace(preview_anchor, PROLOGUE_PREVIEW + preview_anchor)
        if ROW190_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW190_STITCH_OLD, ROW190_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 191")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-191-closing-loop" not in epilogue:
        if ROW190_EPILOGUE_PROCEED_OLD in epilogue:
            epilogue = epilogue.replace(ROW190_EPILOGUE_PROCEED_OLD, ROW190_EPILOGUE_PROCEED_NEW)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, EPILOGUE_LOOP + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 191")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row171-homogenization-meta-prelude-capstone-reunion-index-row-191" not in sources:
        sources = sources.replace(
            "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone",
            SOURCES_TABLE + "| 171 | Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone",
            1,
        )
        sources = sources.replace(
            "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)",
            SOURCES_INDEX + "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 191")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-191-baby-picture-row68-row171" not in memory:
        memory = memory.replace(
            "| 190 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 190 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 171 baby picture (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion}",
            MEMORY_BABY
            + "### Row 171 baby picture (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion}",
            1,
        )
        if ROW190_BABY_OLD in memory:
            memory = memory.replace(ROW190_BABY_OLD, ROW190_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 191")


if __name__ == "__main__":
    main()
