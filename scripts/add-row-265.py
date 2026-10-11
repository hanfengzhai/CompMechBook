#!/usr/bin/env python3
"""Add row 265 meta-stitch (Row 68 → Row 245 ↔ Row 65 second-pass meta prelude capstone reunion, full capstone path)."""
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


def bump245_to_265(text: str) -> str:
    protected = (
        ("row-265-", "__P265__"),
        ("skill-navigation-row-265", "__S265__"),
        ("prologue-preview-row-265", "__PR265__"),
        ("{#row-265-closing-stitch}", "__ST265__"),
        ("{#row-265-closing-loop}", "__LP265__"),
        (
            "row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265",
            "__IDX265__",
        ),
        (
            "row-265-baby-picture-row68-row245-second-pass-meta-prelude-capstone-reunion",
            "__BABY265__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add245():
    spec = importlib.util.spec_from_file_location("add245", ROOT / "scripts/add-row-245.py")
    add245 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add245)
    return add245


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 245 skill checkpoint")
    end = preface.index("\n\n### Row 246 skill checkpoint", start)
    row265_preface = bump245_to_265(preface[start:end]).strip() + "\n\n"

    b245 = _load_add245()._build_blocks()
    prologue_stitch = bump245_to_265(
        b245["prologue_stitch"]
        .replace("{#row-245-closing-stitch}", "{#row-265-closing-stitch}")
        .replace(
            "**Row 245 closing stitch (Row 68 → Row 225",
            "**Row 265 closing stitch (Row 68 → Row 245",
        )
    )
    prologue_compass = bump245_to_265(b245["prologue_compass"]).replace(
        "second-pass meta prelude capstone reunion (row 245) |",
        "second-pass meta prelude capstone reunion (row 265) |",
        1,
    )
    prologue_preview = bump245_to_265(b245["prologue_preview"]).replace(
        "Row 245 preview", "Row 265 preview", 1
    )

    epilogue_loop = bump245_to_265(b245["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-245-closing-loop}", "{#row-265-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 225 closing loop (Row 68 → Row 225",
        "### Row 265 closing loop (Row 68 → Row 245",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 265 closing loop",
        "\n\n\n\n### Row 266 closing loop",
        "\n\n\n\n### Row 245 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump245_to_265(b245["sources_index"])
    sources_index = sources_index.replace(
        "row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245",
        "row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265",
    ).replace(
        "## Row 68 → Row 205 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 225) "
        "{#row68-row205-second-pass-meta-prelude-capstone-reunion-index-row-225}",
        "## Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 265) "
        "{#row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265}",
        1,
    )

    sources_table = bump245_to_265(b245["sources_table"])
    sources_table = re.sub(
        r"^\| 245 \| Row 68 → Row 245",
        "| 265 | Row 68 → Row 245",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 265 | Row 68 → Row 245" not in sources_table:
        sources_table = sources_table.replace(
            "| 245 | Row 68 → Row 225", "| 265 | Row 68 → Row 245", 1
        )

    memory_table = bump245_to_265(b245["memory_table"])
    memory_table = memory_table.replace("| 245 | Meta |", "| 265 | Meta |", 1)

    memory_baby = bump245_to_265(b245["memory_baby"]).rstrip() + "\n\n"
    if "{#row-265-baby-picture-row68-row245" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 265 baby picture",
            "### Row 265 baby picture {#row-265-baby-picture-row68-row245-second-pass-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row265_preface": row265_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW264_STITCH_OLD = (
    "before row 265 second-pass meta prelude capstone reunion on the full capstone path (then row 245 second-pass meta"
)
ROW264_STITCH_NEW = (
    "before row 266 Writings canonical meta prelude capstone reunion on the full capstone path (then row 246 Writings meta"
)

ROW264_INSERT_MARKER = (
    "### Row 264 closing loop (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion) "
    "{#row-264-closing-loop}"
)

ROW264_EPILOGUE_OLD = (
    "Proceed to [row 245](#row-245-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 244 on the capstone path,"
)
ROW264_EPILOGUE_NEW = (
    "Proceed to [row 265](#row-265-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 264 on the capstone path,"
)

PREMATURE_EPILOGUE_HEADER = (
    "### Row 265 closing loop (Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion) "
    "{#row-245-closing-loop}"
)

WRONG_ROW264_HEADER = (
    "### Row 244 closing loop (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion) "
    "{#row-264-closing-loop}"
)
CORRECT_ROW264_HEADER = (
    "### Row 264 closing loop (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion) "
    "{#row-264-closing-loop}"
)


def _insert_row265_epilogue(epilogue: str, proper_loop: str) -> str:
    if WRONG_ROW264_HEADER in epilogue:
        epilogue = epilogue.replace(WRONG_ROW264_HEADER, CORRECT_ROW264_HEADER, 1)
    if PREMATURE_EPILOGUE_HEADER in epilogue:
        start = epilogue.find(PREMATURE_EPILOGUE_HEADER)
        end = epilogue.find("\n\n### Row 266 closing loop", start)
        if end == -1:
            end = epilogue.find("\n\n### Row 246 closing loop", start)
        if end != -1:
            epilogue = epilogue[:start] + proper_loop.rstrip() + "\n\n" + epilogue[end + 2 :]
            return epilogue
    pos = epilogue.find("{#row-265-closing-loop}")
    if pos != -1:
        near = epilogue.find(ROW264_INSERT_MARKER)
        if near != -1 and 0 < pos - near < 8000:
            header_start = epilogue.rfind("\n### ", 0, pos)
            if header_start != -1:
                end = epilogue.find("\n\n### Row 266 closing loop", pos)
                if end == -1:
                    end = epilogue.find("\n\n### Row 246 closing loop", pos)
                if end != -1:
                    return epilogue[: header_start + 1] + proper_loop.rstrip() + "\n\n" + epilogue[end + 2 :]
    if ROW264_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 264 insert anchor not found")
    return epilogue.replace(ROW264_INSERT_MARKER, ROW264_INSERT_MARKER + "\n\n" + proper_loop.rstrip() + "\n\n", 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 265 skill checkpoint" in preface and preface.index("### Row 265 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 265 already present")
    else:
        if "### Row 264 skill checkpoint" not in preface:
            raise SystemExit("row 264 must exist before row 265")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row265_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 265")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "second-pass meta prelude capstone reunion (row 265) |" not in prologue:
        needle = "| Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 264) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 264 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchors = (
            "**Row 264 closing stitch (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion).** "
            "{#row-264-closing-stitch}",
            "**Row 284 closing stitch (Row 68 → Row 264 Row 68 → Row 64 book-loop meta prelude capstone reunion).** "
            "{#row-264-closing-stitch}",
        )
        for stitch_anchor in stitch_anchors:
            if stitch_anchor in prologue:
                prologue = prologue.replace(
                    stitch_anchor,
                    b["prologue_stitch"] + stitch_anchor,
                    1,
                )
                break
        preview_anchor = '| <span id="prologue-preview-row-264"></span>Row 264 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW264_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW264_STITCH_OLD, ROW264_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 265")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW264_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW264_EPILOGUE_OLD, ROW264_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row265_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 265")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    idx_anchor = "row68-row245-second-pass-meta-prelude-capstone-reunion-index-row-265"
    if idx_anchor not in sources or "| 265 | Meta |" not in sources:
        table_needle = "| 245 | Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone"
        if table_needle in sources and "| 265 | Row 68 → Row 245" not in sources:
            sources = sources.replace(
                table_needle,
                b["sources_table"] + table_needle,
                1,
            )
        src_header = (
            "## Row 68 → Row 225 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 245) "
            "{#row68-row225-second-pass-meta-prelude-capstone-reunion-index-row-245}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 265")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "| 265 | Meta |" not in memory:
        if "| 264 | Meta |" in memory:
            memory = memory.replace(
                "| 264 | Meta | [Row 68 → Row 224 book-loop meta prelude capstone reunion index]",
                b["memory_table"] + "| 264 | Meta | [Row 68 → Row 224 book-loop meta prelude capstone reunion index]",
                1,
            )
        else:
            raise SystemExit("memory row 264 table anchor not found")
    if "### Row 265 baby picture {#row-265-baby-picture-row68-row245" not in memory:
        for baby_anchor in (
            "### Row 264 baby picture {#row-264-baby-picture-row68-row244-book-loop-meta-prelude-capstone-reunion}",
            "### Row 245 baby picture {#row-265-baby-picture-row68-row245-second-pass-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                if baby_anchor.startswith("### Row 245 baby picture {#row-265"):
                    memory = memory.replace(
                        baby_anchor,
                        b["memory_baby"].rstrip(),
                        1,
                    )
                else:
                    memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 265")


if __name__ == "__main__":
    main()
