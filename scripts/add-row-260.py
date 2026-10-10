#!/usr/bin/env python3
"""Add row 260 meta-stitch (Row 68 → Row 240 ↔ Row 60 Handshake 3 meta prelude capstone reunion, full capstone path)."""
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


def bump240_to_260(text: str) -> str:
    protected = (
        ("row-260-", "__P260__"),
        ("skill-navigation-row-260", "__S260__"),
        ("prologue-preview-row-260", "__PR260__"),
        ("{#row-260-closing-stitch}", "__ST260__"),
        ("{#row-260-closing-loop}", "__LP260__"),
        (
            "row68-row240-handshake3-meta-prelude-capstone-reunion-index-row-260",
            "__IDX260__",
        ),
        (
            "row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion",
            "__BABY260__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add240():
    spec = importlib.util.spec_from_file_location("add240", ROOT / "scripts/add-row-240.py")
    add240 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add240)
    return add240


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 240 skill checkpoint")
    end = preface.index("\n\n### Row 241 skill checkpoint", start)
    row260_preface = bump240_to_260(preface[start:end]) + "\n\n"

    b240 = _load_add240()._build_blocks()
    prologue_stitch = bump240_to_260(
        b240["prologue_stitch"]
        .replace("{#row-240-closing-stitch}", "{#row-260-closing-stitch}")
        .replace(
            "**Row 240 closing stitch (Row 68 → Row 220",
            "**Row 260 closing stitch (Row 68 → Row 240",
        )
    )
    prologue_compass = bump240_to_260(b240["prologue_compass"]).replace(
        "Handshake 3 meta prelude capstone reunion (row 240) |",
        "Handshake 3 meta prelude capstone reunion (row 260) |",
        1,
    )
    prologue_preview = bump240_to_260(b240["prologue_preview"]).replace(
        "Row 240 preview", "Row 260 preview", 1
    )

    epilogue_loop = bump240_to_260(b240["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-240-closing-loop}", "{#row-260-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 240 closing loop (Row 68 → Row 220",
        "### Row 260 closing loop (Row 68 → Row 240",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 260 closing loop",
        "\n\n\n\n### Row 240 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump240_to_260(b240["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 220 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 240) "
        "{#row68-row220-handshake3-meta-prelude-capstone-reunion-index-row-240}",
        "## Row 68 → Row 260 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 260) "
        "{#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260}",
        1,
    )
    if "{#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260}" not in sources_index:
        sources_index = re.sub(
            r"## Row 68 → Row \d+ Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index \(row 240\)[^\n]*",
            "## Row 68 → Row 260 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 260) "
            "{#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260}",
            sources_index,
            count=1,
        )

    sources_table = bump240_to_260(b240["sources_table"])
    sources_table = re.sub(
        r"^\| 240 \| Row 68 → Row 240",
        "| 260 | Row 68 → Row 240",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 260 | Row 68 → Row 240" not in sources_table:
        sources_table = sources_table.replace(
            "| 240 | Row 68 → Row 220", "| 260 | Row 68 → Row 240", 1
        )

    memory_table = bump240_to_260(b240["memory_table"])
    memory_table = memory_table.replace("| 240 | Meta |", "| 260 | Meta |", 1)

    memory_baby = bump240_to_260(b240["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 260 baby picture {#row-240-baby-picture",
        "### Row 260 baby picture {#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion} {#row-240-baby-picture",
        1,
    )
    if "{#row-260-baby-picture-row68-row240" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 260 baby picture",
            "### Row 260 baby picture {#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row260_preface": row260_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW259_STITCH_OLD = (
    "before row 260 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW259_STITCH_NEW = (
    "before row 261 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)

ROW259_INSERT_MARKER = (
    "### Row 239 closing loop (Row 68 → Row 239 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) "
    "{#row-259-closing-loop}"
)


def _insert_row260_epilogue(epilogue: str, proper_loop: str) -> str:
    if "{#row-260-closing-loop}" in epilogue and proper_loop.strip() in epilogue:
        return epilogue
    if ROW259_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 259 insert anchor not found")
    if "{#row-260-closing-loop}" in epilogue:
        return epilogue
    return epilogue.replace(ROW259_INSERT_MARKER, proper_loop + "\n\n" + ROW259_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 260 skill checkpoint" in preface and preface.index("### Row 260 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 260 already present")
    else:
        if "### Row 259 skill checkpoint" not in preface:
            raise SystemExit("row 259 must exist before row 260")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row260_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 260")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 260) |" not in prologue:
        needle = "| Row 68 → Row 239 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 259) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 259 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchor = (
            "**Row 259 closing stitch (Row 68 → Row 239 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** "
            "{#row-259-closing-stitch}"
        )
        if stitch_anchor in prologue:
            prologue = prologue.replace(
                stitch_anchor,
                b["prologue_stitch"] + stitch_anchor,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-259"></span>Row 259 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW259_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW259_STITCH_OLD, ROW259_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 260")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue_new = _insert_row260_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 260")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    sources_changed = False
    row260_table_marker = "reunion-index-row-260)"
    if row260_table_marker not in sources:
        needle259 = "row68-row239-handshake3-meta-prelude-capstone-reunion-index-row-259)"
        if needle259 in sources:
            idx = sources.index(needle259)
            line_end = sources.find("\n|", idx)
            if line_end != -1:
                sources = (
                    sources[:line_end]
                    + "\n"
                    + b["sources_table"].rstrip()
                    + sources[line_end:]
                )
                sources_changed = True
    src_header = (
        "## Row 68 → Row 259 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 259) "
        "{#row68-row259-handshake3-meta-prelude-capstone-reunion-index-row-259}"
    )
    if src_header in sources and "row68-row240-handshake3-meta-prelude-capstone-reunion-index-row-260" not in sources:
        sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_changed = True
    if sources_changed:
        sources_path.write_text(sources)
        print("sources: added row 260")
    else:
        print("sources: row 260 already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion" not in memory:
        memory = memory.replace(
            "| 259 | Meta | [Row 68 → Row 239 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 259 | Meta | [Row 68 → Row 239 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        for baby_anchor in (
            "### Row 259 baby picture {#row-259-baby-picture-row68-row239-handshake3-meta-prelude-capstone-reunion}",
            "### Row 259 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 260")


if __name__ == "__main__":
    main()
