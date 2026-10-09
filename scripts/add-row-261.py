#!/usr/bin/env python3
"""Add row 261 meta-stitch (Row 68 → Row 241 ↔ Row 61 Handshake 4a meta prelude capstone reunion, full capstone path)."""
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


def bump241_to_261(text: str) -> str:
    protected = (
        ("row-261-", "__P261__"),
        ("skill-navigation-row-261", "__S261__"),
        ("prologue-preview-row-261", "__PR261__"),
        ("{#row-261-closing-stitch}", "__ST261__"),
        ("{#row-261-closing-loop}", "__LP261__"),
        (
            "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
            "__IDX261__",
        ),
        (
            "row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion",
            "__BABY261__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add241():
    spec = importlib.util.spec_from_file_location("add241", ROOT / "scripts/add-row-241.py")
    add241 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add241)
    return add241


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 241 skill checkpoint")
    end = preface.index("\n\n### Row 242 skill checkpoint", start)
    row261_preface = bump241_to_261(preface[start:end]).strip() + "\n\n"

    b241 = _load_add241()._build_blocks()
    prologue_stitch = bump241_to_261(
        b241["prologue_stitch"]
        .replace("{#row-241-closing-stitch}", "{#row-261-closing-stitch}")
        .replace(
            "**Row 241 closing stitch (Row 68 → Row 221",
            "**Row 261 closing stitch (Row 68 → Row 241",
        )
    )
    prologue_compass = bump241_to_261(b241["prologue_compass"]).replace(
        "Handshake 4a meta prelude capstone reunion (row 241) |",
        "Handshake 4a meta prelude capstone reunion (row 261) |",
        1,
    )
    prologue_preview = bump241_to_261(b241["prologue_preview"]).replace(
        "Row 241 preview", "Row 261 preview", 1
    )

    epilogue_loop = bump241_to_261(b241["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-241-closing-loop}", "{#row-261-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 241 closing loop (Row 68 → Row 221",
        "### Row 261 closing loop (Row 68 → Row 241",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 261 closing loop",
        "\n\n\n\n### Row 241 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump241_to_261(b241["sources_index"])
    sources_index = sources_index.replace(
        "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
        "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
    ).replace(
        "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 241)",
        "## Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 261) "
        "{#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261}",
        1,
    )

    sources_table = bump241_to_261(b241["sources_table"])
    sources_table = re.sub(
        r"^\| 241 \| Row 68 → Row 241",
        "| 261 | Row 68 → Row 241",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 261 | Row 68 → Row 241" not in sources_table:
        sources_table = sources_table.replace(
            "| 241 | Row 68 → Row 221", "| 261 | Row 68 → Row 241", 1
        )

    memory_table = bump241_to_261(b241["memory_table"])
    memory_table = memory_table.replace("| 241 | Meta |", "| 261 | Meta |", 1)

    memory_baby = bump241_to_261(b241["memory_baby"]).rstrip() + "\n\n"
    if "{#row-261-baby-picture-row68-row241" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 261 baby picture",
            "### Row 261 baby picture {#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row261_preface": row261_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW260_STITCH_OLD = (
    "before row 261 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)
ROW260_STITCH_NEW = (
    "before row 262 Handshake 4b meta prelude capstone reunion opens on the full capstone path."
)

ROW260_INSERT_MARKER = (
    "### Row 260 closing loop (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion) "
    "{#row-260-closing-loop}"
)

ROW260_EPILOGUE_OLD = (
    "Proceed to [row 241](#row-241-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 260 on the full capstone path,"
)
ROW260_EPILOGUE_NEW = (
    "Proceed to [row 261](#row-261-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 260 on the full capstone path,"
)

BROKEN_SOURCES_HEADER = (
    "## Row 68 → Row 261 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 261) "
    "{#row68-row261-handshake4a-meta-prelude-capstone-reunion-index-row-261} "
    "{#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261}"
)


def _remove_broken_sources_261(sources: str) -> str:
    if BROKEN_SOURCES_HEADER not in sources:
        return sources
    start = sources.index(BROKEN_SOURCES_HEADER)
    end = sources.find("\n## Row 68 → Row 182", start)
    if end == -1:
        raise SystemExit("broken row 261 sources block end not found")
    return sources[:start] + sources[end:]


def _remove_orphan_epilogue_261(epilogue: str) -> str:
    orphan = (
        "### Row 261 closing loop (Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion) "
        "{#row-261-closing-loop}"
    )
    if orphan not in epilogue:
        return epilogue
    pos = epilogue.find(orphan)
    near_260 = epilogue.find(ROW260_INSERT_MARKER)
    if near_260 != -1 and abs(pos - near_260) < 5000:
        return epilogue
    end = epilogue.find("\n\n\n\n### Row 240 closing loop", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 240 closing loop", pos)
    if end == -1:
        raise SystemExit("orphan row 261 epilogue end not found")
    return epilogue[:pos] + epilogue[end:]


def _insert_row261_epilogue(epilogue: str, proper_loop: str) -> str:
    if "{#row-261-closing-loop}" in epilogue:
        pos = epilogue.find("{#row-261-closing-loop}")
        near = epilogue.find(ROW260_INSERT_MARKER)
        if near != -1 and pos - near < 8000:
            return epilogue
    if ROW260_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 260 insert anchor not found")
    return epilogue.replace(ROW260_INSERT_MARKER, proper_loop + "\n\n" + ROW260_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 261 skill checkpoint" in preface and preface.index("### Row 261 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 261 already present")
    else:
        if "### Row 260 skill checkpoint" not in preface:
            raise SystemExit("row 260 must exist before row 261")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row261_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 261")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 4a meta prelude capstone reunion (row 261) |" not in prologue:
        needle = "| Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 260) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 260 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchor = (
            "**Row 260 closing stitch (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** "
            "{#row-260-closing-stitch}"
        )
        if stitch_anchor in prologue:
            prologue = prologue.replace(
                stitch_anchor,
                b["prologue_stitch"] + stitch_anchor,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-260"></span>Row 260 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW260_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW260_STITCH_OLD, ROW260_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 261")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _remove_orphan_epilogue_261(epilogue)
    if ROW260_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW260_EPILOGUE_OLD, ROW260_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row261_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 261")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    sources = _remove_broken_sources_261(sources)
    idx_anchor = "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261"
    if idx_anchor not in sources.split("| 261 | Row 68 → Row 241", 1)[0]:
        table_needle = "| 241 | Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone"
        if table_needle in sources and "| 261 | Row 68 → Row 241" not in sources:
            sources = sources.replace(
                table_needle,
                b["sources_table"] + table_needle,
                1,
            )
        src_header = (
            "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 241)"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 261")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-261-baby-picture-row68-row241" not in memory:
        memory = memory.replace(
            "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = "### Row 260 baby picture {#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion}"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 261")


if __name__ == "__main__":
    main()
