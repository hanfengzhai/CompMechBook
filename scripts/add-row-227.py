#!/usr/bin/env python3
"""Add row 227 meta-stitch (Row 68 → Row 207 ↔ Row 67 part-boundary meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def t207_to_227(text: str) -> str:
    """Transform row-207 capstone-path meta copy to row 227 (207→227, 187→207 inner, 226 gate)."""
    out = text.replace("row 228", "__R228__")
    out = out.replace("row 227", "__R227__")
    out = out.replace("row 226", "__R226__")
    repl = [
        ("Row 68 → Row 187 Row 68 → Row 67", "Row 68 → Row 207 Row 68 → Row 67"),
        (
            "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207",
            "TEMP227WIDX",
        ),
        (
            "row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion",
            "row-227-baby-picture-row68-row207-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("### Row 207 skill checkpoint", "### Row 227 skill checkpoint"),
        ("skill-navigation-row-207", "TEMP227NAV"),
        ("prologue-preview-row-207", "prologue-preview-row-227"),
        ("row-207-closing-stitch", "row-227-closing-stitch"),
        ("row-207-closing-loop", "row-227-closing-loop"),
        ("Row 207 three-way audit", "Row 227 three-way audit"),
        (
            "[row 206](preface.md#skill-navigation-row-206) or [row 207](preface.md#skill-navigation-row-207)",
            "[row 226](preface.md#skill-navigation-row-226) or [row 207](preface.md#skill-navigation-row-207)",
        ),
        (
            "[row 206](preface.md#skill-navigation-row-186) or [row 207](skill-navigation-row-207)",
            "[row 226](preface.md#skill-navigation-row-226) or [row 227](TEMP227NAV)",
        ),
        (
            "[row 206](preface.md#skill-navigation-row-186) or [Row 68 → Row 187 part-boundary meta prelude capstone reunion index (row 207)](appendix/sources.md#row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207)",
            "[row 226](preface.md#skill-navigation-row-226) or [Row 68 → Row 207 part-boundary meta prelude capstone reunion index (row 227)](appendix/sources.md#row68-row207-part-boundary-meta-prelude-capstone-reunion-index-row-227)",
        ),
        (
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 206)",
            "verified Writings canonical meta prelude capstone closure on the full capstone path (row 226)",
        ),
        (
            "before row 208 midpoint meta prelude capstone reunion opens on the full capstone path",
            "before row 228 midpoint meta prelude capstone reunion opens on the full capstone path",
        ),
        (
            "before row 208 midpoint meta prelude capstone opens on the full capstone path",
            "before row 228 midpoint meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 148 midpoint meta prelude capstone opens on the full capstone path",
            "before row 168 midpoint meta prelude capstone opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP227WIDX",
        "row68-row207-part-boundary-meta-prelude-capstone-reunion-index-row-227",
    )
    out = out.replace("TEMP227NAV", "skill-navigation-row-207")
    out = out.replace("Row 68 → Row 207 Row 68 → Row 67", "TEMP227TITLE")
    out = out.replace(
        "**Row 207 closing stitch (Row 68 → Row 187",
        "**Row 227 closing stitch (Row 68 → Row 207",
    )
    out = out.replace("row 207", "row 227")
    out = out.replace("Row 207", "Row 227")
    out = out.replace("TEMP227TITLE", "Row 68 → Row 207 Row 68 → Row 67")
    out = out.replace("skill-navigation-row-207", "skill-navigation-row-227")
    out = out.replace(
        "[row 227](preface.md#skill-navigation-row-207)",
        "[row 207](preface.md#skill-navigation-row-207)",
    )
    out = out.replace(
        "[row 227](preface.md#skill-navigation-row-227)",
        "[row 207](preface.md#skill-navigation-row-207)",
    )
    out = out.replace("when row 206 closed", "when row 226 closed")
    out = out.replace("When row 206 closed", "When row 226 closed")
    out = out.replace("row 206 closed", "row 226 closed")
    out = out.replace("after row 206 alone", "after row 226 alone")
    out = out.replace("Recite [preface row 206]", "Recite [preface row 226]")
    out = out.replace("from row 206's", "from row 226's")
    out = out.replace("row 206 and row 67", "row 226 and row 67")
    out = out.replace("row 206 or row 187", "row 226 or row 207")
    out = out.replace("row 187", "row 207")
    out = out.replace("Row 187", "Row 207")
    out = out.replace("row 167", "row 187")
    out = out.replace("Row 167", "Row 187")
    out = out.replace(
        "row68-row167-part-boundary-meta-prelude-capstone-reunion-index-row-187",
        "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207",
    )
    out = out.replace(
        "row68-row187-part-boundary-meta-prelude-capstone-reunion-index-row-207",
        "row68-row207-part-boundary-meta-prelude-capstone-reunion-index-row-227",
    )
    out = out.replace("row 206", "row 226")
    out = out.replace("Row 206", "Row 226")
    out = out.replace("row 205", "row 225")
    out = out.replace("Row 205", "Row 225")
    out = out.replace("row 208", "row 228")
    out = out.replace("Row 208", "Row 228")
    out = out.replace("row 188", "row 208")
    out = out.replace("Row 188", "Row 208")
    out = out.replace("row 148", "row 168")
    out = out.replace("Row 148", "Row 168")
    out = out.replace("opening [row 208]", "opening [row 228]")
    out = out.replace("skill-navigation-row-208", "skill-navigation-row-228")
    out = out.replace("__R226__", "row 226")
    out = out.replace("__R227__", "row 227")
    out = out.replace("__R228__", "row 228")
    out = out.replace(
        "[row 226](preface.md#skill-navigation-row-226) or [row 227](preface.md#skill-navigation-row-227)",
        "[row 226](preface.md#skill-navigation-row-226) or [row 207](preface.md#skill-navigation-row-207)",
    )
    out = out.replace(
        "Row 68 → Row 227 part-boundary meta prelude capstone reunion index",
        "Row 68 → Row 207 part-boundary meta prelude capstone reunion index",
    )
    return out



def _load_add207():
    spec = importlib.util.spec_from_file_location("add207", ROOT / "scripts/add-row-207.py")
    add207 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add207)
    return add207


def _build_blocks() -> dict[str, str]:
    add207 = _load_add207()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 207 skill checkpoint")
    end = preface.index("\n\n### Row 208 skill checkpoint", start)
    row227_preface = t207_to_227(preface[start:end]) + "\n\n"

    row207_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 207 closing stitch (Row 68 → Row 187")
    )
    prologue_stitch = t207_to_227(
        row207_stitch.replace("{#row-207-closing-stitch}", "{#row-227-closing-stitch}").replace(
            "**Row 207 closing stitch (Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion).",
            "**Row 227 closing stitch (Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion).",
        )
    ) + "\n\n"

    b207 = add207._build_blocks()
    prologue_compass = t207_to_227(b207["prologue_compass"])
    prologue_preview = t207_to_227(b207["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row207_loop_anchor = (
        "### Row 207 closing loop (Row 68 → Row 187 Row 68 → Row 67 "
        "part-boundary meta prelude capstone reunion) {#row-207-closing-loop}"
    )
    row208_loop_end = (
        "### Row 208 closing loop (Row 68 → Row 188 Row 68 → Row 48 "
        "midpoint meta prelude capstone reunion) {#row-208-closing-loop}"
    )
    epilogue_loop = t207_to_227(
        row207_loop_anchor + epilogue.split(row207_loop_anchor, 1)[1].split(row208_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-207-closing-loop}", "{#row-227-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 207 closing loop (Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion)",
        "### Row 227 closing loop (Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src207_header = (
        "## Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 207)"
    )
    next208_header = (
        "## Row 68 → Row 188 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 208)"
    )
    sources_index = t207_to_227(sources.split(src207_header, 1)[1].split(next208_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 227) "
        "{#row68-row207-part-boundary-meta-prelude-capstone-reunion-index-row-227}"
        + sources_index
    )

    sources_table = t207_to_227(b207["sources_table"])
    sources_table = sources_table.replace("| 207 | Row 68 → Row 207", "| 227 | Row 68 → Row 207", 1)

    memory_table = t207_to_227(b207["memory_table"])
    memory_table = memory_table.replace("| 207 | Meta |", "| 227 | Meta |", 1)

    memory_baby = t207_to_227(b207["memory_baby"])
    if "{#row-227-baby-picture-row68-row207" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 227 baby picture (Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion)",
            "### Row 227 baby picture {#row-227-baby-picture-row68-row207-part-boundary-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 207 Row 68 → Row 67 part-boundary meta prelude capstone reunion)",
            1,
        )

    return {
        "row227_preface": row227_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW226_TAIL_OLD = (
    "When row 226 is complete, proceed to [row 207](preface.md#skill-navigation-row-207) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path"
)
ROW226_TAIL_NEW = (
    "When row 226 is complete, proceed to [row 227](preface.md#skill-navigation-row-227) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path"
)

ROW226_EPILOGUE_OLD = (
    "Proceed to [row 207](#row-207-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 226 on the full capstone path,"
)
ROW226_EPILOGUE_NEW = (
    "Proceed to [row 227](#row-227-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 226 on the full capstone path,"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 227 skill checkpoint" in preface:
        print("preface: row 227 already present")
    else:
        if "### Row 226 skill checkpoint" not in preface:
            raise SystemExit("row 226 must exist before row 227")
        if ROW226_TAIL_OLD not in preface:
            raise SystemExit("row 226 tail proceed string not found")
        preface = preface.replace(ROW226_TAIL_OLD, ROW226_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 187](preface.md#skill-navigation-row-187) before row 67 closes on the full capstone path",
            "when opening [row 227](preface.md#skill-navigation-row-227) before row 67 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row227_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 227")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-227" not in prologue:
        needle = (
            "| Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 226) | "
            "[Preface: row 226 skill checkpoint](../preface.md#skill-navigation-row-226)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 226 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 227 closing stitch" not in prologue:
            for anchor in ("**Row 226 closing stitch", "**Row 206 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-226"></span>Row 226 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 227")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-227-closing-loop}" not in epilogue:
        if ROW226_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW226_EPILOGUE_OLD, ROW226_EPILOGUE_NEW, 1)
        marker = "### Row 226 closing loop (Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 226 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 227")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row207-part-boundary-meta-prelude-capstone-reunion-index-row-227" not in sources:
        sources = sources.replace(
            "| 207 | Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone",
            b["sources_table"] + "| 207 | Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone",
            1,
        )
        src207_header = (
            "## Row 68 → Row 187 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 207)"
        )
        sources = sources.replace(src207_header, b["sources_index"] + src207_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 227")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-227-baby-picture-row68-row207" not in memory:
        memory = memory.replace(
            "| 207 | Meta | [Row 68 → Row 187 part-boundary meta prelude capstone reunion index]",
            b["memory_table"] + "| 207 | Meta | [Row 68 → Row 187 part-boundary meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 226 baby picture (Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)",
            "### Row 226 baby picture {#row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion}",
            "### Row 207 baby picture {#row-207-baby-picture-row68-row187-part-boundary-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 227")


if __name__ == "__main__":
    main()
