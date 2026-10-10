#!/usr/bin/env python3
"""Add row 244 meta-stitch (Row 68 → Row 224 ↔ Row 64 book-loop meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 250

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


def bump224_to_244(text: str) -> str:
    protected = (
        ("row-244-", "__P244__"),
        ("skill-navigation-row-244", "__S244__"),
        ("prologue-preview-row-244", "__prologue-preview-row-244__"),
        ("{#row-244-closing-stitch}", "__{#row-244-closing-stitch}__"),
        ("{#row-244-closing-loop}", "__{#row-244-closing-loop}__"),
        (
            "row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244",
            "__row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244__",
        ),
        (
            "row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion",
            "__row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add224():
    spec = importlib.util.spec_from_file_location("add224", ROOT / "scripts/add-row-224.py")
    add224 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add224)
    return add224


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 224 skill checkpoint")
    end = preface.index("\n\n### Row 225 skill checkpoint", start)
    row244_preface = bump224_to_244(preface[start:end]).strip() + "\n\n"

    b224 = _load_add224()._build_blocks()
    out = {
        "row244_preface": row244_preface,
        "prologue_compass": bump224_to_244(b224["prologue_compass"]),
        "prologue_stitch": bump224_to_244(b224["prologue_stitch"]),
        "prologue_preview": bump224_to_244(b224["prologue_preview"]),
        "epilogue_loop": bump224_to_244(b224["epilogue_loop"]),
        "sources_table": bump224_to_244(b224["sources_table"]).replace(
            "| 224 | Row 68 → Row 204", "| 244 | Row 68 → Row 224", 1
        ),
        "sources_index": bump224_to_244(b224["sources_index"]).replace(
            "## Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 224) "
            "{#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224}",
            "## Row 68 → Row 224 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 244) "
            "{#row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244}",
            1,
        ),
        "memory_table": bump224_to_244(b224["memory_table"]).replace("| 224 | Meta |", "| 244 | Meta |", 1),
        "memory_baby": bump224_to_244(b224["memory_baby"]),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace("{#row-244-closing-loop}", "{#row-244-closing-loop}", 1)
    loop = loop.replace(
        "### Row 244 closing loop (Row 68 → Row 224",
        "### Row 224 closing loop (Row 68 → Row 224",
        1,
    )
    for spill in ("\n\n\n\n### Row 243 closing loop", "\n\n\n\n### Row 244 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    if "{#row-244-baby-picture-row68-row224" not in out["memory_baby"]:
        out["memory_baby"] = out["memory_baby"].replace(
            "### Row 244 baby picture",
            "### Row 244 baby picture {#row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion}",
            1,
        )
    return out


ROW243_EPILOGUE_OLD = (
    "Proceed to [row 244](#row-244-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 223 on the full capstone path,"
)
ROW243_EPILOGUE_NEW = (
    "Proceed to [row 244](#row-244-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 243 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 243 closing stitch (Row 68 → Row 223 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-243-closing-stitch}"
)

ROW244_INSERT_MARKER = (
    "### Row 223 closing loop (Row 68 → Row 223 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-243-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 244 skill checkpoint" in preface:
        print("preface: row 244 already present")
    else:
        if "### Row 243 skill checkpoint" not in preface:
            raise SystemExit("row 243 must exist before row 244")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row244_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 244")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "book-loop meta prelude capstone reunion (row 244) |" not in prologue:
        needle = "| Row 68 → Row 223 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 243) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 243 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-243"></span>Row 223 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 244")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW243_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW243_EPILOGUE_OLD, ROW243_EPILOGUE_NEW, 1)
    if "{#row-244-closing-loop}" not in epilogue:
        marker = ROW244_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 243 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 244")
    else:
        print("epilogue: row 244 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row224-book-loop-meta-prelude-capstone-reunion-index-row-244" not in sources:
        sources = sources.replace(
            "| 224 | Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone",
            b["sources_table"] + "| 224 | Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 204 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 224) "
            "{#row68-row204-book-loop-meta-prelude-capstone-reunion-index-row-224}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 244")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-244-baby-picture-row68-row224" not in memory:
        memory = memory.replace(
            "| 243 | Meta | [Row 68 → Row 223 orchestration meta prelude capstone reunion index](sources.md#row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243)",
            b["memory_table"]
            + "| 243 | Meta | [Row 68 → Row 223 orchestration meta prelude capstone reunion index](sources.md#row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 243 baby picture {#row-243-baby-picture-row68-row223-orchestration-meta-prelude-capstone-reunion}",
            "### Row 224 baby picture {#row-224-baby-picture-row68-row204-book-loop-meta-prelude-capstone-reunion}",
            "### Row 223 baby picture {#row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 244")


if __name__ == "__main__":
    main()
