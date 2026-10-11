#!/usr/bin/env python3
"""Add row 264 meta-stitch (Row 68 → Row 244 ↔ Row 64 book-loop meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–280) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 280

    def repl_row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"row {n + delta}" if in_band(n) else m.group(0)

    def repl_Row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"Row {n + delta}" if in_band(n) else m.group(0)

    out = text
    out = re.sub(
        r"row68-row(\d{3})",
        lambda m: f"row68-row{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"index-row-(\d{3})",
        lambda m: f"index-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"skill-navigation-row-(\d{3})",
        lambda m: f"skill-navigation-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"prologue-preview-row-(\d{3})",
        lambda m: f"prologue-preview-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"row-(\d{3})-(closing-stitch|closing-loop|baby-picture)",
        lambda m: f"row-{int(m.group(1)) + delta}-{m.group(2)}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(r"\brow (\d{3})\b", repl_row, out)
    out = re.sub(r"\bRow (\d{3})\b", repl_Row, out)
    return out


def bump244_to_264(text: str) -> str:
    protected = (
        ("row-264-", "__P264__"),
        ("skill-navigation-row-264", "__S264__"),
        ("prologue-preview-row-264", "__PR264__"),
        ("{#row-264-closing-stitch}", "__ST264__"),
        ("{#row-264-closing-loop}", "__LP264__"),
        (
            "row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264",
            "__IDX264__",
        ),
        (
            "row-264-baby-picture-row68-row244-book-loop-meta-prelude-capstone-reunion",
            "__BABY264__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add244():
    spec = importlib.util.spec_from_file_location("add244", ROOT / "scripts/add-row-244.py")
    add244 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add244)
    return add244


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 244 skill checkpoint")
    end = preface.index("\n\n### Row 245 skill checkpoint", start)
    row264_preface = bump244_to_264(preface[start:end]).strip() + "\n\n"

    b244 = _load_add244()._build_blocks()
    prologue_stitch = bump244_to_264(
        b244["prologue_stitch"]
        .replace("{#row-244-closing-stitch}", "{#row-264-closing-stitch}")
        .replace(
            "**Row 244 closing stitch (Row 68 → Row 224",
            "**Row 264 closing stitch (Row 68 → Row 244",
        )
    )
    prologue_compass = bump244_to_264(b244["prologue_compass"]).replace(
        "book-loop meta prelude capstone reunion (row 244) |",
        "book-loop meta prelude capstone reunion (row 264) |",
        1,
    )
    prologue_preview = bump244_to_264(b244["prologue_preview"]).replace(
        "Row 244 preview", "Row 264 preview", 1
    )

    epilogue_loop = bump244_to_264(b244["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-244-closing-loop}", "{#row-264-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 244 closing loop (Row 68 → Row 224",
        "### Row 264 closing loop (Row 68 → Row 244",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 264 closing loop",
        "\n\n\n\n### Row 244 closing loop",
        "\n\n\n\n### Row 224 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump244_to_264(b244["sources_index"])
    sources_index = sources_index.replace(
        "row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244",
        "row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264",
    ).replace(
        "## Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 244) "
        "{#row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244}",
        "## Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 264) "
        "{#row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264}",
        1,
    )

    sources_table = bump244_to_264(b244["sources_table"])
    sources_table = re.sub(
        r"^\| 244 \| Row 68 → Row 244",
        "| 264 | Row 68 → Row 244",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 264 | Row 68 → Row 244" not in sources_table:
        sources_table = sources_table.replace(
            "| 244 | Row 68 → Row 224", "| 264 | Row 68 → Row 244", 1
        )

    memory_table = bump244_to_264(b244["memory_table"])
    memory_table = memory_table.replace("| 244 | Meta |", "| 264 | Meta |", 1)

    memory_baby = bump244_to_264(b244["memory_baby"]).rstrip() + "\n\n"
    if "{#row-264-baby-picture-row68-row244" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 264 baby picture",
            "### Row 264 baby picture {#row-264-baby-picture-row68-row244-book-loop-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row264_preface": row264_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW263_STITCH_OLD = (
    "before row 225 second-pass meta prelude capstone reunion on the full capstone path (then row 205 second-pass meta"
)
ROW263_STITCH_NEW = (
    "before row 265 second-pass meta prelude capstone reunion on the full capstone path (then row 245 second-pass meta"
)

ROW263_INSERT_MARKER = (
    "### Row 263 closing loop (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion) "
    "{#row-263-closing-loop}"
)

ROW263_EPILOGUE_OLD = (
    "Proceed to [row 264](#row-244-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 243 on the full capstone path,"
)
ROW263_EPILOGUE_NEW = (
    "Proceed to [row 264](#row-264-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 263 on the full capstone path,"
)

PREMATURE_EPILOGUE_HEADER = (
    "### Row 264 closing loop (Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion) "
    "{#row-244-closing-loop}"
)


def _insert_row264_epilogue(epilogue: str, proper_loop: str) -> str:
    if "{#row-264-closing-loop}" in epilogue:
        pos = epilogue.find("{#row-264-closing-loop}")
        near = epilogue.find(ROW263_INSERT_MARKER)
        if near != -1 and pos - near < 8000:
            return epilogue
    if PREMATURE_EPILOGUE_HEADER in epilogue:
        start = epilogue.find(PREMATURE_EPILOGUE_HEADER)
        end = epilogue.find("\n\n### Row 265 closing loop", start)
        if end == -1:
            end = epilogue.find("\n\n### Row 245 closing loop", start)
        if end != -1:
            return epilogue[:start] + proper_loop.rstrip() + "\n\n" + epilogue[end + 2 :]
    if ROW263_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 263 insert anchor not found")
    return epilogue.replace(ROW263_INSERT_MARKER, proper_loop + "\n\n" + ROW263_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 264 skill checkpoint" in preface and preface.index("### Row 264 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 264 already present")
    else:
        if "### Row 263 skill checkpoint" not in preface:
            raise SystemExit("row 263 must exist before row 264")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row264_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 264")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "book-loop meta prelude capstone reunion (row 264) |" not in prologue:
        needle = "| Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 263) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 263 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 263 closing stitch (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion).** "
            "{#row-263-closing-stitch}",
            "**Row 283 closing stitch (Row 68 → Row 263 Row 68 → Row 63 orchestration meta prelude capstone reunion).** "
            "{#row-263-closing-stitch}",
        )
        for stitch_anchor in stitch_anchors:
            if stitch_anchor in prologue:
                prologue = prologue.replace(
                    stitch_anchor,
                    b["prologue_stitch"] + stitch_anchor,
                    1,
                )
                break
        preview_anchor = '| <span id="prologue-preview-row-263"></span>Row 263 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW263_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW263_STITCH_OLD, ROW263_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 264")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW263_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW263_EPILOGUE_OLD, ROW263_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row264_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 264")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    idx_anchor = "row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264"
    if idx_anchor not in sources.split("| 264 | Row 68 → Row 244", 1)[0]:
        table_needle = "| 244 | Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone"
        if table_needle in sources and "| 264 | Row 68 → Row 244" not in sources:
            sources = sources.replace(
                table_needle,
                b["sources_table"] + table_needle,
                1,
            )
        src_header = (
            "## Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 244) "
            "{#row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 264")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-264-baby-picture-row68-row244" not in memory:
        table_needle = "| 263 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]"
        if table_needle in memory and "| 264 | Meta |" not in memory:
            memory = memory.replace(
                table_needle,
                b["memory_table"] + table_needle,
                1,
            )
        elif "| 264 | Meta |" not in memory:
            memory = memory.replace(
                "| 263 | Meta | [Row 68 → Row 243 orchestration meta prelude capstone reunion index]",
                b["memory_table"] + "| 263 | Meta | [Row 68 → Row 243 orchestration meta prelude capstone reunion index]",
                1,
            )
        for baby_anchor in (
            "### Row 263 baby picture {#row-263-baby-picture-row68-row243-orchestration-meta-prelude-capstone-reunion}",
            "### Row 263 baby picture (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion)",
            "### Row 244 baby picture {#row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 264")


if __name__ == "__main__":
    main()
