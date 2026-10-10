#!/usr/bin/env python3
"""Add row 228 meta-stitch (Row 68 → Row 208 ↔ Row 48 midpoint meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def t208_to_228(text: str) -> str:
    """Transform row-208 capstone-path meta copy to row 228 (208→228, 188→208 inner, 227 gate)."""
    out = text.replace("row 229", "__R229__")
    out = text.replace("row 228", "__R228__")
    out = text.replace("row 209", "__R209__")
    out = text.replace("row 208", "__R208__")
    repl = [
        ("Row 68 → Row 188 Row 68 → Row 48", "Row 68 → Row 208 Row 68 → Row 48"),
        (
            "row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208",
            "TEMP228IDX",
        ),
        (
            "row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion",
            "row-228-baby-picture-row68-row208-midpoint-meta-prelude-capstone-reunion",
        ),
        ("### Row 208 skill checkpoint", "### Row 228 skill checkpoint"),
        ("skill-navigation-row-208", "skill-navigation-row-228"),
        ("prologue-preview-row-208", "prologue-preview-row-228"),
        ("row-208-closing-stitch", "row-228-closing-stitch"),
        ("row-208-closing-loop", "row-228-closing-loop"),
        ("Row 208 three-way audit", "Row 228 three-way audit"),
        (
            "[row 207](preface.md#skill-navigation-row-207) or [row 188](preface.md#skill-navigation-row-188)",
            "[row 227](preface.md#skill-navigation-row-227) or [row 208](preface.md#skill-navigation-row-208)",
        ),
        (
            "[row 207](preface.md#skill-navigation-row-207) or [Row 68 → Row 188 midpoint meta prelude capstone reunion index (row 208)](appendix/sources.md#row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208)",
            "[row 227](preface.md#skill-navigation-row-227) or [Row 68 → Row 208 midpoint meta prelude capstone reunion index (row 228)](appendix/sources.md#row68-row208-midpoint-meta-prelude-capstone-reunion-index-row-228)",
        ),
        (
            "verified part-boundary meta prelude capstone on the full capstone path (row 207)",
            "verified part-boundary meta prelude capstone on the full capstone path (row 227)",
        ),
        (
            "verified part-boundary meta prelude capstone via [row 207]",
            "verified part-boundary meta prelude capstone via [row 227]",
        ),
        (
            "before row 209 taxonomy meta prelude capstone reunion opens on the full capstone path",
            "before row 229 taxonomy meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 189 taxonomy meta prelude capstone opens on the full capstone path",
            "before row 209 taxonomy meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP228IDX", "row68-row208-midpoint-meta-prelude-capstone-reunion-index-row-228"
    )
    out = out.replace("Row 208 does not replace", "Row 228 does not replace")
    out = out.replace("(row 207) with the full-book", "(row 227) with the full-book")
    out = out.replace("prologue row 208", "prologue row 228")
    out = out.replace("memory sheet row 208", "memory sheet row 228")
    out = out.replace("epilogue row 208", "epilogue row 228")
    out = out.replace("When row 228 is complete", "When row 228 is complete")
    out = out.replace("When row 208 is complete", "When row 228 is complete")
    out = out.replace("When row 207 closed", "When row 227 closed")
    out = out.replace("when row 207 closed", "when row 227 closed")
    out = out.replace("after row 207", "after row 227")
    out = out.replace("after row 207 alone", "after row 227 alone")
    out = out.replace("Recite [preface row 207]", "Recite [preface row 227]")
    out = out.replace("row 207's twin-ladder", "row 227's twin-ladder")
    out = out.replace(
        "[row 209](preface.md#skill-navigation-row-209) before row 49",
        "[row 229](preface.md#skill-navigation-row-229) before row 49",
    )
    out = out.replace(
        "proceed to [row 209](preface.md#skill-navigation-row-209) when midpoint",
        "proceed to [row 229](preface.md#skill-navigation-row-229) when midpoint",
    )
    out = out.replace(
        "[row 188](preface.md#skill-navigation-row-188) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 207](preface.md#skill-navigation-row-207) when part-boundary",
        "[row 208](preface.md#skill-navigation-row-208) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 227](preface.md#skill-navigation-row-227) when part-boundary",
    )
    out = out.replace("Row 68 → Row 188 reunion index", "Row 68 → Row 208 reunion index")
    out = out.replace(
        "Row 68 → Row 188 midpoint meta prelude capstone reunion index",
        "Row 68 → Row 208 midpoint meta prelude capstone reunion index",
    )
    out = out.replace("row 188, row 108", "row 208, row 108")
    out = out.replace("row 207, row 188", "row 227, row 208")
    out = out.replace("row 187", "row 207")
    out = out.replace("Row 187", "Row 207")
    out = out.replace(
        "row68-row168-midpoint-meta-prelude-capstone-reunion-index-row-188",
        "row68-row188-midpoint-meta-prelude-capstone-reunion-index-row-208",
    )
    out = out.replace("row 206", "row 226")
    out = out.replace("Row 206", "Row 226")
    out = out.replace("row 168", "row 188")
    out = out.replace("Row 168", "Row 188")
    out = out.replace("row 149", "row 169")
    out = out.replace("Row 149", "Row 169")
    out = out.replace("row 129", "row 149")
    out = out.replace("Row 129", "Row 149")
    out = out.replace("row 147", "row 167")
    out = out.replace("Row 147", "Row 167")
    out = out.replace("__R208__", "row 208")
    out = out.replace("__R209__", "row 209")
    out = out.replace("__R228__", "row 228")
    out = out.replace("__R229__", "row 229")
    out = out.replace(
        "[row 228](preface.md#skill-navigation-row-227)", "[row 227](preface.md#skill-navigation-row-227)"
    )
    out = out.replace(
        "[row 228](preface.md#skill-navigation-row-208)", "[row 208](preface.md#skill-navigation-row-208)"
    )
    out = out.replace("when row 207 and row 48", "when row 227 and row 48")
    out = out.replace("when row 187 and row 48", "when row 207 and row 48")
    out = out.replace("after row 147 alone", "after row 227 alone")
    out = out.replace("row 147 closed", "row 227 closed")
    out = out.replace("skill-navigation-row-128", "skill-navigation-row-228")
    out = out.replace(
        "row 228 names **Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 228 names",
        "row 208 names **Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion**; row 228 names",
    )
    return out


def _load_add208():
    spec = importlib.util.spec_from_file_location("add208", ROOT / "scripts/add-row-208.py")
    add208 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add208)
    return add208


def _build_blocks() -> dict[str, str]:
    add208 = _load_add208()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 208 skill checkpoint")
    end = preface.index("\n\n### Row 209 skill checkpoint", start)
    row228_preface = t208_to_228(preface[start:end]) + "\n\n"

    prologue_lines = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
    row208_stitch = next(
        line for line in prologue_lines if "{#row-208-closing-stitch}" in line and "closing stitch" in line
    )
    prologue_stitch = t208_to_228(
        row208_stitch.replace("{#row-208-closing-stitch}", "{#row-228-closing-stitch}").replace(
            "**Row 168 closing stitch (Row 68 → Row 188",
            "**Row 228 closing stitch (Row 68 → Row 208",
        )
    ) + "\n\n"

    b208 = add208._build_blocks()
    prologue_compass = t208_to_228(b208["prologue_compass"])
    prologue_preview = t208_to_228(b208["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row208_loop_anchor = (
        "### Row 208 closing loop (Row 68 → Row 188 Row 68 → Row 48 "
        "midpoint meta prelude capstone reunion) {#row-208-closing-loop}"
    )
    row209_loop_end = (
        "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
    )
    epilogue_loop = t208_to_228(
        row208_loop_anchor + epilogue.split(row208_loop_anchor, 1)[1].split(row209_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-208-closing-loop}", "{#row-228-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 208 closing loop (Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion)",
        "### Row 228 closing loop (Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src208_header = (
        "## Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 208)"
    )
    next209_header = (
        "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209)"
    )
    sources_index = t208_to_228(sources.split(src208_header, 1)[1].split(next209_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 228) "
        "{#row68-row208-midpoint-meta-prelude-capstone-reunion-index-row-228}"
        + sources_index
    )

    sources_table = t208_to_228(b208["sources_table"])
    sources_table = sources_table.replace("| 208 | Row 68 → Row 188", "| 228 | Row 68 → Row 208", 1)

    memory_table = t208_to_228(b208["memory_table"])
    memory_table = memory_table.replace("| 208 | Meta |", "| 228 | Meta |", 1)

    memory_baby = t208_to_228(b208["memory_baby"])
    if "{#row-228-baby-picture-row68-row208" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 228 baby picture (Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion)",
            "### Row 228 baby picture {#row-228-baby-picture-row68-row208-midpoint-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion)",
            1,
        )

    return {
        "row228_preface": row228_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW227_EPILOGUE_OLD = (
    "Proceed to [row 228](#row-208-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 227 on the full capstone path,"
)
ROW227_EPILOGUE_NEW = (
    "Proceed to [row 228](#row-228-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 227 on the full capstone path,"
)

ROW227_STITCH_OLD = (
    "before row 228 midpoint meta prelude capstone reunion opens on the full capstone path."
)
ROW227_STITCH_NEW = (
    "before row 229 taxonomy meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 228 skill checkpoint" in preface:
        print("preface: row 228 already present")
    else:
        if "### Row 227 skill checkpoint" not in preface:
            raise SystemExit("row 227 must exist before row 228")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row228_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 228")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-228" not in prologue:
        needle = (
            "| Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 227) | "
            "[Preface: row 227 skill checkpoint](../preface.md#skill-navigation-row-227)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 227 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 228 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 227 closing stitch",
                b["prologue_stitch"] + "**Row 227 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-227"></span>Row 227 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW227_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW227_STITCH_OLD, ROW227_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 228")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-228-closing-loop}" not in epilogue:
        if ROW227_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW227_EPILOGUE_OLD, ROW227_EPILOGUE_NEW, 1)
        marker = (
            "### Row 208 closing loop (Row 68 → Row 188 Row 68 → Row 48 "
            "midpoint meta prelude capstone reunion) {#row-208-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 208 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 228")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row208-midpoint-meta-prelude-capstone-reunion-index-row-228" not in sources:
        sources = sources.replace(
            "| 208 | Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone",
            b["sources_table"] + "| 208 | Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        src208_header = (
            "## Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 208)"
        )
        sources = sources.replace(src208_header, b["sources_index"] + src208_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 228")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-228-baby-picture-row68-row208" not in memory:
        memory = memory.replace(
            "| 208 | Meta | [Row 68 → Row 188 midpoint meta prelude capstone reunion index]",
            b["memory_table"] + "| 208 | Meta | [Row 68 → Row 188 midpoint meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 227 baby picture {#row-227-baby-picture-row68-row207-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 227 baby picture (Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion)",
            "### Row 208 baby picture {#row-208-baby-picture-row68-row188-midpoint-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 228")


if __name__ == "__main__":
    main()
