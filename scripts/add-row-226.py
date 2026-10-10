#!/usr/bin/env python3
"""Add row 226 meta-stitch (Row 68 → Row 206 ↔ Row 66 Writings canonical meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def t206_to_226(text: str) -> str:
    """Transform row-206 capstone-path meta copy to row 226 (206→226, 186→206 inner, 225 gate)."""
    out = text.replace("row 227", "__R227__")
    out = out.replace("row 226", "__R226__")
    out = out.replace("row 225", "__R225__")
    repl = [
        ("Row 68 → Row 186 Row 68 → Row 66", "Row 68 → Row 206 Row 68 → Row 66"),
        (
            "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206",
            "TEMP226WIDX",
        ),
        (
            "row-206-baby-picture-row68-row186-writings-meta-prelude-capstone-reunion",
            "row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion",
        ),
        ("### Row 206 skill checkpoint", "### Row 226 skill checkpoint"),
        ("skill-navigation-row-206", "TEMP226NAV"),
        ("prologue-preview-row-206", "prologue-preview-row-226"),
        ("row-206-closing-stitch", "row-226-closing-stitch"),
        ("row-206-closing-loop", "row-226-closing-loop"),
        ("Row 206 three-way audit", "Row 226 three-way audit"),
        (
            "[row 205](preface.md#skill-navigation-row-205) or [row 206](preface.md#skill-navigation-row-206)",
            "[row 225](preface.md#skill-navigation-row-225) or [row 206](preface.md#skill-navigation-row-206)",
        ),
        (
            "[row 205](preface.md#skill-navigation-row-205) or [Row 68 → Row 186 Writings canonical meta prelude capstone reunion index (row 206)](appendix/sources.md#row68-row186-writings-meta-prelude-capstone-reunion-index-row-206)",
            "[row 225](preface.md#skill-navigation-row-225) or [Row 68 → Row 206 Writings canonical meta prelude capstone reunion index (row 226)](appendix/sources.md#row68-row206-writings-meta-prelude-capstone-reunion-index-row-226)",
        ),
        (
            "verified second-pass meta prelude capstone closure on the full capstone path (row 205)",
            "verified second-pass meta prelude capstone closure on the full capstone path (row 225)",
        ),
        (
            "before row 207 part-boundary meta prelude capstone reunion opens on the full capstone path",
            "before row 227 part-boundary meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("TEMP226WIDX", "row68-row206-writings-meta-prelude-capstone-reunion-index-row-226")
    out = out.replace("TEMP226NAV", "skill-navigation-row-206")
    out = out.replace("Row 68 → Row 206 Row 68 → Row 66", "TEMP226TITLE")
    out = out.replace(
        "**Row 206 closing stitch (Row 68 → Row 186",
        "**Row 226 closing stitch (Row 68 → Row 206",
    )
    out = out.replace("row 206", "row 226")
    out = out.replace("Row 206", "Row 226")
    out = out.replace("TEMP226TITLE", "Row 68 → Row 206 Row 68 → Row 66")
    out = out.replace("skill-navigation-row-206", "skill-navigation-row-226")
    out = out.replace(
        "[row 226](preface.md#skill-navigation-row-225)",
        "[row 225](preface.md#skill-navigation-row-225)",
    )
    out = out.replace(
        "[row 226](preface.md#skill-navigation-row-226)",
        "[row 206](preface.md#skill-navigation-row-206)",
    )
    out = out.replace(
        "[row 206](preface.md#skill-navigation-row-226)",
        "[row 206](preface.md#skill-navigation-row-206)",
    )
    out = out.replace("when row 205 closed", "when row 225 closed")
    out = out.replace("When row 205 closed", "When row 225 closed")
    out = out.replace("row 205 closed", "row 225 closed")
    out = out.replace("after row 205 alone", "after row 225 alone")
    out = out.replace("Recite [preface row 205]", "Recite [preface row 225]")
    out = out.replace("from row 205's", "from row 225's")
    out = out.replace("row 205 and row 66", "row 225 and row 66")
    out = out.replace("row 205 or row 186", "row 225 or row 206")
    out = out.replace("row 186", "row 206")
    out = out.replace("Row 186", "Row 206")
    out = out.replace("row 166", "row 186")
    out = out.replace("Row 166", "Row 186")
    out = out.replace(
        "row68-row166-writings-meta-prelude-capstone-reunion-index-row-186",
        "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206",
    )
    out = out.replace(
        "row68-row186-writings-meta-prelude-capstone-reunion-index-row-206",
        "row68-row206-writings-meta-prelude-capstone-reunion-index-row-226",
    )
    out = out.replace("row 205", "row 225")
    out = out.replace("Row 205", "Row 225")
    out = out.replace("row 204", "row 224")
    out = out.replace("Row 204", "Row 224")
    out = out.replace("row 185", "row 205")
    out = out.replace("Row 185", "Row 205")
    out = out.replace("opening [row 167]", "opening [row 187]")
    out = out.replace("skill-navigation-row-167", "skill-navigation-row-187")
    out = out.replace("__R225__", "row 225")
    out = out.replace("__R226__", "row 226")
    out = out.replace("__R227__", "row 227")
    out = out.replace(
        "[row 225](preface.md#skill-navigation-row-225) or [row 226](preface.md#skill-navigation-row-226)",
        "[row 225](preface.md#skill-navigation-row-225) or [row 206](preface.md#skill-navigation-row-206)",
    )
    out = out.replace(
        "Row 68 → Row 226 Writings canonical meta prelude capstone reunion index",
        "Row 68 → Row 206 Writings canonical meta prelude capstone reunion index",
    )
    return out


def _load_add206():
    spec = importlib.util.spec_from_file_location("add206", ROOT / "scripts/add-row-206.py")
    add206 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add206)
    return add206


def _build_blocks() -> dict[str, str]:
    add206 = _load_add206()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 206 skill checkpoint")
    end = preface.index("\n\n### Row 207 skill checkpoint", start)
    row226_preface = t206_to_226(preface[start:end]) + "\n\n"

    row206_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 206 closing stitch (Row 68 → Row 186")
    )
    prologue_stitch = t206_to_226(
        row206_stitch.replace("{#row-206-closing-stitch}", "{#row-226-closing-stitch}").replace(
            "**Row 206 closing stitch (Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).",
            "**Row 226 closing stitch (Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).",
        )
    ) + "\n\n"

    b206 = add206._build_blocks()
    prologue_compass = t206_to_226(b206["prologue_compass"])
    prologue_preview = t206_to_226(b206["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row206_loop_anchor = (
        "### Row 206 closing loop (Row 68 → Row 186 Row 68 → Row 66 "
        "Writings canonical meta prelude capstone reunion) {#row-206-closing-loop}"
    )
    row207_loop_end = (
        "### Row 207 closing loop (Row 68 → Row 187 Row 68 → Row 67 "
        "part-boundary meta prelude capstone reunion) {#row-207-closing-loop}"
    )
    epilogue_loop = t206_to_226(
        row206_loop_anchor + epilogue.split(row206_loop_anchor, 1)[1].split(row207_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-206-closing-loop}", "{#row-226-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 206 closing loop (Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)",
        "### Row 226 closing loop (Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src206_header = (
        "## Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206)"
    )
    next207_header = (
        "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167)"
    )
    sources_index = t206_to_226(sources.split(src206_header, 1)[1].split(next207_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 226) "
        "{#row68-row206-writings-meta-prelude-capstone-reunion-index-row-226}"
        + sources_index
    )

    sources_table = t206_to_226(b206["sources_table"])
    sources_table = sources_table.replace("| 206 | Row 68 → Row 206", "| 226 | Row 68 → Row 206", 1)

    memory_table = t206_to_226(b206["memory_table"])
    memory_table = memory_table.replace("| 206 | Meta |", "| 226 | Meta |", 1)

    memory_baby = t206_to_226(b206["memory_baby"])
    if "{#row-226-baby-picture-row68-row206" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 226 baby picture (Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)",
            "### Row 226 baby picture {#row-226-baby-picture-row68-row206-writings-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 206 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)",
            1,
        )

    return {
        "row226_preface": row226_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW225_TAIL_OLD = (
    "When row 225 is complete, proceed to [row 206](preface.md#skill-navigation-row-206) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)
ROW225_TAIL_NEW = (
    "When row 225 is complete, proceed to [row 226](preface.md#skill-navigation-row-226) when row 68 closed but Writings canonical meta prelude capstone still lags after second-pass meta prelude capstone on the full capstone path"
)

ROW225_EPILOGUE_OLD = (
    "Proceed to [row 206](#row-206-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 225 on the full capstone path,"
)
ROW225_EPILOGUE_NEW = (
    "Proceed to [row 226](#row-226-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 225 on the full capstone path,"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 226 skill checkpoint" in preface:
        print("preface: row 226 already present")
    else:
        if "### Row 225 skill checkpoint" not in preface:
            raise SystemExit("row 225 must exist before row 226")
        if ROW225_TAIL_OLD not in preface:
            raise SystemExit("row 225 tail proceed string not found")
        preface = preface.replace(ROW225_TAIL_OLD, ROW225_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 166](preface.md#skill-navigation-row-166) before row 66 closes on the full capstone path",
            "when opening [row 226](preface.md#skill-navigation-row-226) before row 66 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row226_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 226")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-226" not in prologue:
        needle = (
            "| Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 225) | "
            "[Preface: row 225 skill checkpoint](../preface.md#skill-navigation-row-225)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 225 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 226 closing stitch" not in prologue:
            for anchor in ("**Row 225 closing stitch", "**Row 205 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-225"></span>Row 225 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 226")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-226-closing-loop}" not in epilogue:
        if ROW225_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW225_EPILOGUE_OLD, ROW225_EPILOGUE_NEW, 1)
        marker = "### Row 225 closing loop (Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 225 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 226")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row206-writings-meta-prelude-capstone-reunion-index-row-226" not in sources:
        sources = sources.replace(
            "| 206 | Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone",
            b["sources_table"] + "| 206 | Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone",
            1,
        )
        src206_header = (
            "## Row 68 → Row 186 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 206)"
        )
        sources = sources.replace(src206_header, b["sources_index"] + src206_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 226")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-226-baby-picture-row68-row206" not in memory:
        memory = memory.replace(
            "| 206 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            b["memory_table"] + "| 206 | Meta | [Row 68 → Row 184 book-loop meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 225 baby picture (Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion)",
            "### Row 205 baby picture {#row-225-baby-picture-row68-row205-second-pass-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 226")


if __name__ == "__main__":
    main()
