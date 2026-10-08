#!/usr/bin/env python3
"""Add row 223 meta-stitch (Row 68 → Row 203 ↔ Row 63 orchestration meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump203_to_223(text: str) -> str:
    """Transform row-203 capstone-path meta copy to row 223 (203→223 inner, 222 Handshake 4b gate)."""
    out = text.replace("row 224", "TEMP_ROW224")
    out = out.replace("row 223", "TEMP_ROW223")
    out = out.replace("row 222", "TEMP_ROW222")
    repl = [
        ("Row 68 → Row 183 Row 68 → Row 63", "Row 68 → Row 203 Row 68 → Row 63"),
        (
            "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
            "TEMP_ROW223_ORCH_INDEX",
        ),
        (
            "row-203-baby-picture-row68-row183-orchestration-meta-prelude-capstone-reunion",
            "row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion",
        ),
        ("### Row 203 skill checkpoint", "### Row 223 skill checkpoint"),
        ("skill-navigation-row-203", "skill-navigation-row-223"),
        ("prologue-preview-row-203", "prologue-preview-row-223"),
        ("row-203-closing-stitch", "row-223-closing-stitch"),
        ("row-203-closing-loop", "row-223-closing-loop"),
        ("Row 203 three-way audit", "Row 223 three-way audit"),
        (
            "[row 202](preface.md#skill-navigation-row-202) or [row 183](preface.md#skill-navigation-row-163)",
            "[row 222](preface.md#skill-navigation-row-222) or [row 203](preface.md#skill-navigation-row-203)",
        ),
        (
            "[row 202](preface.md#skill-navigation-row-182) or [Row 68 → Row 183 orchestration meta prelude capstone reunion index (row 203)](appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203)",
            "[row 222](preface.md#skill-navigation-row-222) or [Row 68 → Row 203 orchestration meta prelude capstone reunion index (row 223)](appendix/sources.md#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223)",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 202)",
            "verified Handshake 4b meta prelude capstone closure (row 222)",
        ),
        (
            "before row 204 book-loop meta prelude capstone opens on the full capstone path",
            "before row 224 book-loop meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 204 book-loop meta prelude capstone reunion on the full capstone path",
            "before row 224 book-loop meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW223_ORCH_INDEX",
        "row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223",
    )
    out = out.replace("Row 203 does not replace", "Row 223 does not replace")
    out = out.replace("When row 203 is complete", "When row 223 is complete")
    out = out.replace("When row 202 closed", "When row 222 closed")
    out = out.replace("when row 202 closed but row 63", "when row 222 closed but row 63")
    out = out.replace("after row 203 alone", "after row 223 alone")
    out = out.replace("Recite [preface row 202]", "Recite [preface row 222]")
    out = out.replace("row 203 or row 183 recited", "row 223 or row 203 recited")
    out = out.replace("row 202 or row 183 recited", "row 222 or row 203 recited")
    out = out.replace("when row 202 and row 63", "when row 222 and row 63")
    out = out.replace("after row 202 alone", "after row 222 alone")
    out = out.replace("after row 202 on the full capstone path", "after row 222 on the full capstone path")
    out = out.replace("skill-navigation-row-183", "TEMP_SKILL_183")
    out = out.replace("row 183", "row 203")
    out = out.replace("Row 183", "Row 203")
    out = out.replace("TEMP_SKILL_183", "skill-navigation-row-183")
    out = out.replace("[row 203](preface.md#skill-navigation-row-202)", "[row 222](preface.md#skill-navigation-row-222)")
    out = out.replace("[row 203](preface.md#skill-navigation-row-203)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("[row 203](preface.md#skill-navigation-row-163)", "[row 203](preface.md#skill-navigation-row-203)")
    out = out.replace("row 163", "row 183")
    out = out.replace("Row 163", "Row 183")
    out = out.replace("row 143", "row 163")
    out = out.replace("Row 143", "Row 163")
    out = out.replace(
        "row68-row163-orchestration-meta-prelude-capstone-reunion-index-row-183",
        "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
    )
    out = out.replace(
        "row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203",
        "row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223",
    )
    out = out.replace("Row 68 → Row 223 Row 68 → Row 63", "Row 68 → Row 203 Row 68 → Row 63")
    out = out.replace("memory sheet row 203 baby picture", "memory sheet row 223 baby picture")
    out = out.replace("prologue row 203 closing stitch", "prologue row 223 closing stitch")
    out = out.replace("prologue row 203 preview", "prologue row 223 preview")
    out = out.replace("epilogue row 203 closing loop", "epilogue row 223 closing loop")
    out = out.replace("opening [row 204]", "opening [row 224]")
    out = out.replace("skill-navigation-row-204", "skill-navigation-row-224")
    out = out.replace(
        "Prologue preview ([row 203](prologue/00-many-scales.md#prologue-preview-row-203))",
        "Prologue preview ([row 223](prologue/00-many-scales.md#prologue-preview-row-223))",
    )
    out = out.replace("preface row 203", "preface row 223")
    out = out.replace(
        "[row 204](preface.md#skill-navigation-row-204)",
        "[row 224](preface.md#skill-navigation-row-224)",
    )
    out = out.replace("TEMP_ROW222", "row 222")
    out = out.replace("TEMP_ROW223", "row 223")
    out = out.replace("TEMP_ROW224", "row 224")
    out = out.replace(
        "proceed to [row 204](preface.md#skill-navigation-row-204)",
        "proceed to [row 224](preface.md#skill-navigation-row-224)",
    )
    out = out.replace(
        "Row 68 → Row 183 reunion index](appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203)",
        "Row 68 → Row 203 reunion index](appendix/sources.md#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223)",
    )
    out = out.replace(
        "reunion index (row 203)](appendix/sources.md#row68-row183-orchestration-meta-prelude-capstone-reunion-index-row-203)",
        "reunion index (row 223)](appendix/sources.md#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223)",
    )
    out = out.replace("row 202's Handshake 4b", "row 222's Handshake 4b")
    out = out.replace("row 203's orchestration", "row 223's orchestration")
    return out


def _load_add203():
    spec = importlib.util.spec_from_file_location("add203", ROOT / "scripts/add-row-203.py")
    add203 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add203)
    return add203


def _build_blocks() -> dict[str, str]:
    add203 = _load_add203()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 203 skill checkpoint")
    end = preface.index("\n\n### Row 204 skill checkpoint", start)
    row223_preface = bump203_to_223(preface[start:end]) + "\n\n"

    row203_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 203 closing stitch (Row 68 → Row 183")
    )
    prologue_stitch = bump203_to_223(
        row203_stitch.replace("{#row-203-closing-stitch}", "{#row-223-closing-stitch}").replace(
            "**Row 203 closing stitch (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion).",
            "**Row 223 closing stitch (Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion).",
        )
    ) + "\n\n"

    b203 = add203._build_blocks()
    prologue_compass = bump203_to_223(b203["prologue_compass"])
    prologue_preview = bump203_to_223(b203["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row203_loop_anchor = (
        "### Row 203 closing loop (Row 68 → Row 183 Row 68 → Row 63 "
        "orchestration meta prelude capstone reunion) {#row-203-closing-loop}"
    )
    row204_loop_end = (
        "### Row 204 closing loop (Row 68 → Row 184 Row 68 → Row 64 "
        "book-loop meta prelude capstone reunion) {#row-204-closing-loop}"
    )
    epilogue_loop = bump203_to_223(
        row203_loop_anchor + epilogue.split(row203_loop_anchor, 1)[1].split(row204_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-203-closing-loop}", "{#row-223-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 203 closing loop (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
        "### Row 223 closing loop (Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src203_header = (
        "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
    )
    next204_header = (
        "## Row 68 → Row 184 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 204)"
    )
    sources_index = bump203_to_223(sources.split(src203_header, 1)[1].split(next204_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 223) "
        "{#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223}"
        + sources_index
    )

    sources_table = bump203_to_223(b203["sources_table"])
    sources_table = sources_table.replace("| 203 | Row 68 → Row 183", "| 223 | Row 68 → Row 203", 1)

    memory_table = bump203_to_223(b203["memory_table"])
    memory_table = memory_table.replace("| 203 | Meta |", "| 223 | Meta |", 1)

    memory_baby = bump203_to_223(b203["memory_baby"])
    if "{#row-223-baby-picture-row68-row203" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 223 baby picture (Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            "### Row 223 baby picture {#row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            1,
        )

    return {
        "row223_preface": row223_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW222_TAIL_OLD = (
    "When row 222 is complete, proceed to [row 203](preface.md#skill-navigation-row-223) when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path,"
)
ROW222_TAIL_NEW = (
    "When row 222 is complete, proceed to [row 223](preface.md#skill-navigation-row-223) when Handshakes 1–4b verify individually but orchestration meta still feels disconnected from Act VI foundation after verified Handshake 4b meta prelude capstone on the full capstone path,"
)

ROW222_EPILOGUE_OLD = (
    "Proceed to [row 203](#row-203-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 202 on the full capstone path,"
)
ROW222_EPILOGUE_NEW = (
    "Proceed to [row 223](#row-223-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 222 on the full capstone path,"
)

ROW222_EPILOGUE_BEFORE_OLD = (
    "before row 223 orchestration meta prelude capstone reunion on the full capstone path (then row 203 orchestration on the full capstone path)."
)
ROW222_EPILOGUE_BEFORE_NEW = (
    "before row 224 book-loop meta prelude capstone reunion on the full capstone path (then row 204 book-loop on the full capstone path)."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 223 skill checkpoint" in preface:
        print("preface: row 223 already present")
    else:
        if "### Row 222 skill checkpoint" not in preface:
            raise SystemExit("row 222 must exist before row 223")
        if ROW222_TAIL_OLD not in preface:
            raise SystemExit("row 222 tail proceed string not found")
        preface = preface.replace(ROW222_TAIL_OLD, ROW222_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 183](preface.md#skill-navigation-row-183) before row 63 closes on the full capstone path",
            "when opening [row 223](preface.md#skill-navigation-row-223) before row 63 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row223_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 223")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-223" not in prologue:
        needle = "| Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 203) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 203 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 223 closing stitch" not in prologue:
            for anchor in ("**Row 203 closing stitch", "**Row 183 closing stitch"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-203"></span>Row 203 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW222_EPILOGUE_BEFORE_OLD in prologue:
            prologue = prologue.replace(ROW222_EPILOGUE_BEFORE_OLD, ROW222_EPILOGUE_BEFORE_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 223")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-223-closing-loop}" not in epilogue:
        if ROW222_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW222_EPILOGUE_OLD, ROW222_EPILOGUE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 223")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223" not in sources:
        sources = sources.replace(
            "| 203 | Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone",
            b["sources_table"] + "| 203 | Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone",
            1,
        )
        src203_header = (
            "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
        )
        sources = sources.replace(src203_header, b["sources_index"] + src203_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 223")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-223-baby-picture-row68-row203" not in memory:
        memory = memory.replace(
            "| 203 | Meta | [Row 68 → Row 183 orchestration meta prelude capstone reunion index]",
            b["memory_table"] + "| 203 | Meta | [Row 68 → Row 183 orchestration meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 203 baby picture (Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 223")


if __name__ == "__main__":
    main()
