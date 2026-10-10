#!/usr/bin/env python3
"""Add row 225 meta-stitch (Row 68 → Row 205 ↔ Row 65 second-pass meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def t205_to_225(text: str) -> str:
    """Transform row-205 capstone-path meta copy to row 225 (205→225, 185→205 inner, 224 gate)."""
    out = text.replace("row 226", "__R226__")
    out = out.replace("row 225", "__R225__")
    out = out.replace("row 224", "__R224__")
    repl = [
        ("Row 68 → Row 185 Row 68 → Row 65", "Row 68 → Row 205 Row 68 → Row 65"),
        (
            "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
            "TEMP_ROW225_EXP_INDEX",
        ),
        (
            "row-205-baby-picture-row68-row185-second-pass-meta-prelude-capstone-reunion",
            "row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion",
        ),
        ("### Row 205 skill checkpoint", "### Row 225 skill checkpoint"),
        ("skill-navigation-row-205", "TEMP_SKILL_NAV_205"),
        ("prologue-preview-row-205", "prologue-preview-row-225"),
        ("row-205-closing-stitch", "row-225-closing-stitch"),
        ("row-205-closing-loop", "row-225-closing-loop"),
        ("Row 205 three-way audit", "Row 225 three-way audit"),
        (
            "[row 204](preface.md#skill-navigation-row-204) or [row 185](preface.md#skill-navigation-row-185)",
            "[row 224](preface.md#skill-navigation-row-224) or [row 205](preface.md#skill-navigation-row-205)",
        ),
        (
            "[row 204](preface.md#skill-navigation-row-204) or [Row 68 → Row 185 second-pass meta prelude capstone reunion index (row 205)](appendix/sources.md#row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205)",
            "[row 224](preface.md#skill-navigation-row-224) or [Row 68 → Row 205 second-pass meta prelude capstone reunion index (row 225)](appendix/sources.md#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225)",
        ),
        (
            "verified book-loop meta prelude capstone closure (row 204)",
            "verified book-loop meta prelude capstone closure (row 224)",
        ),
        (
            "before row 206 Writings canonical meta prelude capstone opens on the full capstone path",
            "before row 226 Writings canonical meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 206 Writings canonical meta prelude capstone reunion on the full capstone path",
            "before row 226 Writings canonical meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW225_EXP_INDEX",
        "row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225",
    )
    out = out.replace("TEMP_SKILL_NAV_205", "skill-navigation-row-205")
    out = out.replace("Row 68 → Row 205 Row 68 → Row 65", "TEMP_ROW205_TITLE")
    out = out.replace(
        "**Row 205 closing stitch (Row 68 → Row 185",
        "**Row 225 closing stitch (Row 68 → Row 205",
    )
    out = out.replace("row 224 or row 204 recited", "row 224 or row 205 recited")
    out = out.replace("row 205", "row 225")
    out = out.replace("Row 205", "Row 225")
    out = out.replace("TEMP_ROW205_TITLE", "Row 68 → Row 205 Row 68 → Row 65")
    out = out.replace("skill-navigation-row-205", "skill-navigation-row-225")
    out = out.replace(
        "[row 225](preface.md#skill-navigation-row-224)",
        "[row 224](preface.md#skill-navigation-row-224)",
    )
    out = out.replace(
        "[row 225](preface.md#skill-navigation-row-225)",
        "[row 225](preface.md#skill-navigation-row-225)",
    )
    out = out.replace(
        "[row 225](preface.md#skill-navigation-row-205)",
        "[row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace(
        "[row 205](preface.md#skill-navigation-row-225)",
        "[row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace("when row 204 closed but row 65", "when row 224 closed but row 65")
    out = out.replace("row 2255", "row 224")
    out = out.replace("row 2256", "row 226")
    out = out.replace("row 225 or row 225", "row 224 or row 205")
    out = out.replace("When row 225 closed", "When row 224 closed")
    out = out.replace("after row 225 alone", "after row 224 alone")
    out = out.replace("When row 204 closed — book-loop", "When row 224 closed — book-loop")
    out = out.replace("When row 204 closed — second-pass", "When row 224 closed — second-pass")
    out = out.replace("row 204 closed book-loop", "row 224 closed book-loop")
    out = out.replace("row 204 closed second-pass", "row 224 closed second-pass")
    out = out.replace("after row 204 alone", "after row 224 alone")
    out = out.replace("Recite [preface row 225]", "Recite [preface row 224]")
    out = out.replace("row 224 or row 205 recited", "row 224 or row 205 recited")
    out = out.replace("from row 225's", "from row 224's")
    out = out.replace("row 204 and row 65", "row 224 and row 65")
    out = out.replace("Recite [preface row 204]", "Recite [preface row 224]")
    out = out.replace("row 185", "row 205")
    out = out.replace("Row 185", "Row 205")
    out = out.replace("row 165", "row 185")
    out = out.replace("Row 165", "Row 185")
    out = out.replace("row 145", "row 165")
    out = out.replace("Row 145", "Row 165")
    out = out.replace("row 125", "row 145")
    out = out.replace("Row 125", "Row 145")
    out = out.replace("row 105", "row 125")
    out = out.replace("Row 105", "Row 125")
    out = out.replace(
        "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
    )
    out = out.replace(
        "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
        "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
    )
    out = out.replace(
        "row68-row185-second-pass-meta-prelude-capstone-reunion-index-row-205",
        "row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225",
    )
    out = out.replace("row 204", "row 224")
    out = out.replace("Row 204", "Row 224")
    out = out.replace("row 184", "row 204")
    out = out.replace("Row 184", "Row 204")
    out = out.replace("row 164", "row 184")
    out = out.replace("Row 164", "Row 184")
    out = out.replace("row 144", "row 164")
    out = out.replace("Row 144", "Row 164")
    out = out.replace(
        "Row 68 → Row 225 second-pass meta prelude capstone reunion index",
        "Row 68 → Row 205 second-pass meta prelude capstone reunion index",
    )
    out = out.replace("Row 225 does not replace", "Row 225 does not replace")
    out = out.replace("When row 225 is complete", "When row 225 is complete")
    out = out.replace("__R224__", "row 224")
    out = out.replace("__R225__", "row 225")
    out = out.replace("__R226__", "row 226")
    out = out.replace(
        "[row 224](preface.md#skill-navigation-row-224) or [row 225](preface.md#skill-navigation-row-225)",
        "[row 224](preface.md#skill-navigation-row-224) or [row 205](preface.md#skill-navigation-row-205)",
    )
    out = out.replace(
        "[row 224](preface.md#skill-navigation-row-204)",
        "[row 224](preface.md#skill-navigation-row-224)",
    )
    return out


def _load_add205():
    spec = importlib.util.spec_from_file_location("add205", ROOT / "scripts/add-row-205.py")
    add205 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add205)
    return add205


def _build_blocks() -> dict[str, str]:
    add205 = _load_add205()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 205 skill checkpoint")
    end = preface.index("\n\n### Row 206 skill checkpoint", start)
    row225_preface = t205_to_225(preface[start:end]) + "\n\n"

    row205_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 205 closing stitch (Row 68 → Row 185")
    )
    prologue_stitch = t205_to_225(
        row205_stitch.replace("{#row-205-closing-stitch}", "{#row-225-closing-stitch}").replace(
            "**Row 205 closing stitch (Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion).",
            "**Row 225 closing stitch (Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion).",
        )
    ) + "\n\n"

    b205 = add205._build_blocks()
    prologue_compass = t205_to_225(b205["prologue_compass"])
    prologue_preview = t205_to_225(b205["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row205_loop_anchor = (
        "### Row 205 closing loop (Row 68 → Row 185 Row 68 → Row 65 "
        "second-pass meta prelude capstone reunion) {#row-205-closing-loop}"
    )
    row206_loop_end = (
        "### Row 206 closing loop (Row 68 → Row 186 Row 68 → Row 66 "
        "Writings canonical meta prelude capstone reunion) {#row-206-closing-loop}"
    )
    epilogue_loop = t205_to_225(
        row205_loop_anchor + epilogue.split(row205_loop_anchor, 1)[1].split(row206_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-205-closing-loop}", "{#row-225-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 205 closing loop (Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
        "### Row 225 closing loop (Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src205_header = (
        "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)"
    )
    next206_header = (
        "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)"
    )
    sources_index = t205_to_225(sources.split(src205_header, 1)[1].split(next206_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225) "
        "{#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225}"
        + sources_index
    )

    sources_table = t205_to_225(b205["sources_table"])
    sources_table = sources_table.replace("| 205 | Row 68 → Row 205", "| 225 | Row 68 → Row 205", 1)

    memory_table = t205_to_225(b205["memory_table"])
    memory_table = memory_table.replace("| 205 | Meta |", "| 225 | Meta |", 1)

    memory_baby = t205_to_225(b205["memory_baby"])
    if "{#row-225-baby-picture-row68-row205" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 225 baby picture (Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
            "### Row 225 baby picture {#row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
            1,
        )

    return {
        "row225_preface": row225_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW224_TAIL_OLD = (
    "When row 224 is complete, proceed to [row 205](preface.md#skill-navigation-row-225) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)
ROW224_TAIL_NEW = (
    "When row 224 is complete, proceed to [row 225](preface.md#skill-navigation-row-225) when row 68 closed but second-pass meta still feels disconnected from novel rhythm after verified book-loop meta prelude capstone on the full capstone path"
)

ROW224_EPILOGUE_OLD = (
    "Proceed to [row 205](#row-205-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 204 on the full capstone path,"
)
ROW224_EPILOGUE_NEW = (
    "Proceed to [row 225](#row-225-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 224 on the full capstone path,"
)

def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 225 skill checkpoint" in preface:
        print("preface: row 225 already present")
    else:
        if "### Row 224 skill checkpoint" not in preface:
            raise SystemExit("row 224 must exist before row 225")
        if ROW224_TAIL_OLD not in preface:
            raise SystemExit("row 224 tail proceed string not found")
        preface = preface.replace(ROW224_TAIL_OLD, ROW224_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 206](preface.md#skill-navigation-row-166) before row 66 closes on the full capstone path on the full capstone path",
            "when opening [row 226](preface.md#skill-navigation-row-206) before row 66 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row225_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 225")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-225" not in prologue:
        needle = (
            "| Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 204) | "
            "[Preface: row 204 skill checkpoint](../preface.md#skill-navigation-row-224)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 224 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 225 closing stitch" not in prologue:
            for anchor in ("**Row 205 closing stitch", "**Row 185 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-224"></span>Row 204 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 225")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-225-closing-loop}" not in epilogue:
        if ROW224_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW224_EPILOGUE_OLD, ROW224_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 225")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225" not in sources:
        sources = sources.replace(
            "| 205 | Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone",
            b["sources_table"] + "| 205 | Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone",
            1,
        )
        src205_header = (
            "## Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 205)"
        )
        sources = sources.replace(src205_header, b["sources_index"] + src205_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 225")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-225-baby-picture-row68-row205" not in memory:
        memory = memory.replace(
            "| 205 | Meta | [Row 68 → Row 185 second-pass meta prelude capstone reunion index]",
            b["memory_table"] + "| 205 | Meta | [Row 68 → Row 185 second-pass meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 205 baby picture (Row 68 → Row 185 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
            "### Row 224 baby picture (Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 225")


if __name__ == "__main__":
    main()
