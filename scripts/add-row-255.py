#!/usr/bin/env python3
"""Add row 255 meta-stitch (Row 68 → Row 235 ↔ Row 55 electronic audit meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–270) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

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


def bump235_to_255(text: str) -> str:
    protected = (
        ("row-255-", "__P255__"),
        ("skill-navigation-row-255", "__S255__"),
        ("prologue-preview-row-255", "__prologue-preview-row-255__"),
        ("{#row-255-closing-stitch}", "__{#row-255-closing-stitch}__"),
        ("{#row-255-closing-loop}", "__{#row-255-closing-loop}__"),
        (
            "row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
            "__row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255__",
        ),
        (
            "row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion",
            "__row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add235():
    spec = importlib.util.spec_from_file_location("add235", ROOT / "scripts/add-row-235.py")
    add235 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add235)
    return add235


def _row255_prologue_preview() -> str:
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    anchor = '| <span id="prologue-preview-row-254"></span>'
    if anchor not in prologue:
        raise SystemExit("prologue row 254 preview anchor not found for row 255 preview template")
    start = prologue.index(anchor)
    end = prologue.find("\n", start)
    line = prologue[start:end]
    protected = (
        ("row-255-", "__P255__"),
        ("skill-navigation-row-255", "__S255__"),
        ("prologue-preview-row-255", "__prologue-preview-row-255__"),
        (
            "row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
            "__IDX254__",
        ),
        (
            "row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion",
            "__BABY254__",
        ),
    )
    out = line
    for old, new in protected:
        out = out.replace(old, new)

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

    delta = 20

    for pat in (
        r"row68-row(\d{3})",
        r"index-row-(\d{3})",
        r"skill-navigation-row-(\d{3})",
        r"prologue-preview-row-(\d{3})",
        r"row-(\d{3})-(closing-stitch|closing-loop|baby-picture)",
    ):
        out = re.sub(
            pat,
            lambda m, d=delta: (
                m.group(0).replace(m.group(1), str(int(m.group(1)) + d))
                if in_band(int(m.group(1)))
                else m.group(0)
            ),
            out,
        )
    out = re.sub(
        r"\brow (\d{3})\b",
        lambda m: f"row {int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"\bRow (\d{3})\b",
        lambda m: f"Row {int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    for old, new in protected:
        out = out.replace(new, old)
    return out + "\n"


def _row255_sources_index() -> str:
    """Single row-255 reunion index block."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 255 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 255) "
        "{#row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 254 Row 68 → Row 54 export meta prelude capstone reunion index (row 254)",
            start,
        )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump235_to_255(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 235 skill checkpoint", 1)[1]
        .split("### Row 236 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 255 closes the **electronic audit meta prelude capstone** on the full capstone path — "
        + "see [preface row 255](../preface.md#skill-navigation-row-255) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 235 skill checkpoint")
    end = preface.index("\n\n### Row 236 skill checkpoint", start)
    row255_preface = bump235_to_255(preface[start:end]).strip() + "\n\n"
    row255_preface = row255_preface.replace(
        "### Row 255 skill checkpoint — Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion audit {#skill-navigation-row-255}",
        "### Row 255 skill checkpoint — Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion audit {#skill-navigation-row-255}",
        1,
    )

    b235 = _load_add235()._build_blocks()
    memory_baby = bump235_to_255(b235["memory_baby"])
    memory_baby = memory_baby.replace(
        "### Row 235 baby picture {#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}",
        "### Row 255 baby picture {#row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion}",
        1,
    )
    memory_baby = memory_baby.replace("**Row 235 baby picture:**", "**Row 255 baby picture:**", 1)
    memory_baby = memory_baby.replace(
        "before row 254 export meta prelude capstone opens on the full capstone path.",
        "before row 256 Born–Oppenheimer meta prelude capstone opens on the full capstone path.",
        1,
    )

    memory_table = bump235_to_255(b235["memory_table"])
    memory_table = memory_table.replace("| 235 | Meta |", "| 255 | Meta |", 1)

    sources_table = bump235_to_255(b235["sources_table"])
    sources_table = sources_table.replace("| 235 | Row 68 → Row 215", "| 255 | Row 68 → Row 235", 1)

    out = {
        "row255_preface": row255_preface,
        "prologue_compass": bump235_to_255(b235["prologue_compass"]),
        "prologue_stitch": bump235_to_255(b235["prologue_stitch"]),
        "prologue_preview": _row255_prologue_preview(),
        "epilogue_loop": bump235_to_255(b235["epilogue_loop"]),
        "sources_table": sources_table,
        "memory_table": memory_table,
        "sources_index": _row255_sources_index(),
        "memory_baby": memory_baby,
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 215 closing loop (Row 68 → Row 215",
        "### Row 255 closing loop (Row 68 → Row 235",
        1,
    )
    loop = loop.replace(
        "### Row 235 closing loop (Row 68 → Row 215",
        "### Row 255 closing loop (Row 68 → Row 235",
        1,
    )
    loop = loop.replace("{#row-235-closing-loop}", "{#row-255-closing-loop}", 1)
    for spill in ("\n\n\n\n### Row 249 closing loop", "\n\n\n\n### Row 250 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 254 closing stitch (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-254-closing-stitch}"
)

ROW255_INSERT_MARKER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-252-closing-loop}"
)

ROW254_STITCH_OLD = (
    "before row 255 electronic audit meta prelude capstone reunion opens on the full capstone path."
)
ROW254_STITCH_NEW = (
    "before row 256 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)

ROW254_EPILOGUE_OLD = (
    "Proceed to [row 215](#row-215-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 234 on the full capstone path,"
)
ROW254_EPILOGUE_NEW = (
    "Proceed to [row 255](#row-255-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 254 on the full capstone path,"
)


def _strip_orphan_row255_epilogue(text: str) -> str:
    """Remove misplaced duplicate row-255 closing loops (wrong headers or late copies)."""
    pattern = (
        r"\n\n### Row 235 closing loop \(Row 68 → Row 235 Row 68 → Row 55 "
        r"electronic audit meta prelude capstone reunion\) \{#row-255-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 252 closing loop)"
    )
    text = re.sub(pattern, "", text, flags=re.DOTALL)
    pattern2 = (
        r"\n\n### Row 255 closing loop \(Row 68 → Row 255 Row 68 → Row 53 "
        r"dynamics meta prelude capstone reunion\) \{#row-255-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\n\n### Row 252 closing loop|\Z)"
    )
    return re.sub(pattern2, "", text, flags=re.DOTALL)


def _epilogue_has_row255_at_capstone(text: str) -> bool:
    marker = ROW255_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return (
        "### Row 255 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion)"
        in window
        and "{#row-255-closing-loop}" in window
        and "memory sheet row 255" in window
    )


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 255 skill checkpoint" in preface:
        print("preface: row 255 already present")
    else:
        if "### Row 254 skill checkpoint" not in preface:
            raise SystemExit("row 254 must exist before row 255")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row255_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 255")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "electronic audit meta prelude capstone reunion (row 255) |" not in prologue and (
        "prologue-preview-row-255" not in prologue
    ):
        needle = (
            "| Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion (row 254) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 254 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch = PROLOGUE_STITCH_ANCHOR
        if stitch in prologue:
            prologue = prologue.replace(stitch, b["prologue_stitch"] + stitch, 1)
        preview_anchor = '| <span id="prologue-preview-row-254"></span>Row 234 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW254_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW254_STITCH_OLD, ROW254_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 255")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row255_epilogue(epilogue)
    if ROW254_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW254_EPILOGUE_OLD, ROW254_EPILOGUE_NEW, 1)
    if _epilogue_has_row255_at_capstone(epilogue):
        epilogue_path.write_text(epilogue)
        print("epilogue: row 255 closing loop already present at capstone anchor")
    else:
        marker = ROW255_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 252 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 255")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255" not in sources:
        sources = sources.replace(
            "| 254 | Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone",
            b["sources_table"] + "| 254 | Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 254 Row 68 → Row 54 export meta prelude capstone reunion index (row 254) "
            "{#row68-row254-export-meta-prelude-capstone-reunion-index-row-254}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 255")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 255 baby picture {#row-255-baby-picture-row68-row235" not in memory:
        memory = memory.replace(
            "| 254 | Meta | [Row 68 → Row 234 export meta prelude capstone reunion index]",
            b["memory_table"] + "| 254 | Meta | [Row 68 → Row 234 export meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "**Row 254 baby picture:**",
            "### Row 254 baby picture {#row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion}",
            "**Row 252 baby picture:**",
            "### Row 252 baby picture {#row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 255")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 255 baby already present")


if __name__ == "__main__":
    main()
