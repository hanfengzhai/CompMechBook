#!/usr/bin/env python3
"""Add row 263 meta-stitch (Row 68 → Row 243 ↔ Row 63 orchestration meta prelude capstone reunion, full capstone path)."""
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


def bump243_to_263(text: str) -> str:
    protected = (
        ("row-263-", "__P263__"),
        ("skill-navigation-row-263", "__S263__"),
        ("prologue-preview-row-263", "__PR263__"),
        ("{#row-263-closing-stitch}", "__ST263__"),
        ("{#row-263-closing-loop}", "__LP263__"),
        (
            "row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263",
            "__IDX263__",
        ),
        (
            "row-263-baby-picture-row68-row243-orchestration-meta-prelude-capstone-reunion",
            "__BABY263__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add243():
    spec = importlib.util.spec_from_file_location("add243", ROOT / "scripts/add-row-243.py")
    add243 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add243)
    return add243


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 243 skill checkpoint")
    end = preface.index("\n\n### Row 244 skill checkpoint", start)
    row263_preface = bump243_to_263(preface[start:end]).strip() + "\n\n"

    b243 = _load_add243()._build_blocks()
    prologue_stitch = bump243_to_263(
        b243["prologue_stitch"]
        .replace("{#row-243-closing-stitch}", "{#row-263-closing-stitch}")
        .replace(
            "**Row 243 closing stitch (Row 68 → Row 223",
            "**Row 263 closing stitch (Row 68 → Row 243",
        )
    )
    prologue_compass = bump243_to_263(b243["prologue_compass"]).replace(
        "orchestration meta prelude capstone reunion (row 243) |",
        "orchestration meta prelude capstone reunion (row 263) |",
        1,
    )
    prologue_preview = bump243_to_263(b243["prologue_preview"]).replace(
        "Row 243 preview", "Row 263 preview", 1
    )

    epilogue_loop = bump243_to_263(b243["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-243-closing-loop}", "{#row-263-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 243 closing loop (Row 68 → Row 223",
        "### Row 263 closing loop (Row 68 → Row 243",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 263 closing loop",
        "\n\n\n\n### Row 243 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump243_to_263(b243["sources_index"])
    sources_index = sources_index.replace(
        "row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243",
        "row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263",
    ).replace(
        "## Row 68 → Row 223 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 243)",
        "## Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 263) "
        "{#row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263}",
        1,
    )

    sources_table = bump243_to_263(b243["sources_table"])
    sources_table = re.sub(
        r"^\| 243 \| Row 68 → Row 223",
        "| 263 | Row 68 → Row 243",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 263 | Row 68 → Row 243" not in sources_table:
        sources_table = sources_table.replace(
            "| 243 | Row 68 → Row 223", "| 263 | Row 68 → Row 243", 1
        )

    memory_table = bump243_to_263(b243["memory_table"])
    memory_table = memory_table.replace("| 243 | Meta |", "| 263 | Meta |", 1)

    memory_baby = bump243_to_263(b243["memory_baby"]).rstrip() + "\n\n"
    if "{#row-263-baby-picture-row68-row243" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 263 baby picture",
            "### Row 263 baby picture {#row-263-baby-picture-row68-row243-orchestration-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row263_preface": row263_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW262_STITCH_OLD = (
    "before row 263 orchestration meta prelude capstone reunion opens on the full capstone path."
)
ROW262_STITCH_NEW = (
    "before row 264 book-loop meta prelude capstone reunion opens on the full capstone path."
)

ROW262_INSERT_MARKER = (
    "### Row 262 closing loop (Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) "
    "{#row-262-closing-loop}"
)

ROW262_EPILOGUE_OLD = (
    "Proceed to [row 263](#row-263-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 262 on the full capstone path,"
)
ROW262_EPILOGUE_NEW = (
    "Proceed to [row 263](#row-263-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 262 on the full capstone path,"
)

BROKEN_SOURCES_HEADER = (
    "## Row 68 → Row 263 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 263) "
    "{#row68-row263-orchestration-meta-prelude-capstone-reunion-index-row-263} "
    "{#row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263}"
)


def _remove_broken_sources_263(sources: str) -> str:
    if BROKEN_SOURCES_HEADER not in sources:
        return sources
    start = sources.index(BROKEN_SOURCES_HEADER)
    end = sources.find("\n## Row 68 → Row 182", start)
    if end == -1:
        raise SystemExit("broken row 263 sources block end not found")
    return sources[:start] + sources[end:]


def _remove_orphan_epilogue_263(epilogue: str) -> str:
    orphan = (
        "### Row 263 closing loop (Row 68 → Row 243 Row 68 → Row 63 orchestration meta prelude capstone reunion) "
        "{#row-263-closing-loop}"
    )
    if orphan not in epilogue:
        return epilogue
    pos = epilogue.find(orphan)
    near_262 = epilogue.find(ROW262_INSERT_MARKER)
    if near_262 != -1 and abs(pos - near_262) < 5000:
        return epilogue
    end = epilogue.find("\n\n\n\n### Row 240 closing loop", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 240 closing loop", pos)
    if end == -1:
        raise SystemExit("orphan row 263 epilogue end not found")
    return epilogue[:pos] + epilogue[end:]


def _insert_row263_epilogue(epilogue: str, proper_loop: str) -> str:
    if "{#row-263-closing-loop}" in epilogue:
        pos = epilogue.find("{#row-263-closing-loop}")
        near = epilogue.find(ROW262_INSERT_MARKER)
        if near != -1 and pos - near < 8000:
            return epilogue
    if ROW262_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 262 insert anchor not found")
    return epilogue.replace(ROW262_INSERT_MARKER, proper_loop + "\n\n" + ROW262_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 263 skill checkpoint" in preface and preface.index("### Row 263 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 263 already present")
    else:
        if "### Row 262 skill checkpoint" not in preface:
            raise SystemExit("row 262 must exist before row 263")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row263_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 263")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "orchestration meta prelude capstone reunion (row 263) |" not in prologue:
        needle = (
            "| Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 262) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 262 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchor = (
            "**Row 262 closing stitch (Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** "
            "{#row-262-closing-stitch}"
        )
        if stitch_anchor in prologue:
            prologue = prologue.replace(
                stitch_anchor,
                b["prologue_stitch"] + stitch_anchor,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-262"></span>Row 262 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW262_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW262_STITCH_OLD, ROW262_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 263")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _remove_orphan_epilogue_263(epilogue)
    if ROW262_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW262_EPILOGUE_OLD, ROW262_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row263_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 263")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    sources = _remove_broken_sources_263(sources)
    idx_anchor = "row68-row243-orchestration-meta-prelude-capstone-reunion-index-row-263"
    if idx_anchor not in sources:
        src_header = (
            "## Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 262) "
            "{#row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"].strip() + "\n\n" + src_header, 1)
        if "| 262 | Meta |" not in sources and "| 263 | Row 68 → Row 243" not in sources:
            sources = sources.replace(
                "| 262 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]",
                b["sources_table"]
                + "| 262 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]",
                1,
            )
        sources_path.write_text(sources)
        print("sources: added row 263")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 263 baby picture {#row-263-baby-picture" not in memory:
        memory = memory.replace(
            "| 262 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]",
            b["memory_table"] + "| 262 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 262 baby picture {#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion}"
        )
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 263")


if __name__ == "__main__":
    main()
