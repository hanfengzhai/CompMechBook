#!/usr/bin/env python3
"""Add row 256 meta-stitch (Row 68 → Row 236 ↔ Row 56 Born–Oppenheimer meta prelude capstone reunion, full capstone path)."""
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


def bump236_to_256(text: str) -> str:
    protected = (
        ("row-256-", "__P256__"),
        ("skill-navigation-row-256", "__S256__"),
        ("prologue-preview-row-256", "__prologue-preview-row-256__"),
        ("{#row-256-closing-stitch}", "__{#row-256-closing-stitch}__"),
        ("{#row-256-closing-loop}", "__{#row-256-closing-loop}__"),
        (
            "row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256",
            "__row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256__",
        ),
        (
            "row-256-baby-picture-row68-row256-born-oppenheimer-meta-prelude-capstone-reunion",
            "__row-256-baby-picture-row68-row256-born-oppenheimer-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add236():
    spec = importlib.util.spec_from_file_location("add236", ROOT / "scripts/add-row-236.py")
    add236 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add236)
    return add236


def _row256_prologue_preview() -> str:
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    anchor = '| <span id="prologue-preview-row-236"></span>'
    if anchor not in prologue:
        raise SystemExit("prologue row 236 preview anchor not found for row 256 preview template")
    start = prologue.index(anchor)
    end = prologue.find("\n", start)
    line = prologue[start:end]
    return bump236_to_256(line) + "\n"


def _row256_sources_index() -> str:
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 256 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 256) "
        "{#row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 255 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 255)",
            start,
        )
        if end == -1:
            end = sources.find(
                "\n\n## Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236)",
                start,
            )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump236_to_256(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 236 skill checkpoint", 1)[1]
        .split("### Row 237 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 256 closes the **Born–Oppenheimer meta prelude capstone** on the full capstone path — "
        + "see [preface row 256](../preface.md#skill-navigation-row-256) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 236 skill checkpoint")
    end = preface.index("\n\n### Row 237 skill checkpoint", start)
    row256_preface = bump236_to_256(preface[start:end]).strip() + "\n\n"
    row256_preface = row256_preface.replace(
        "### Row 256 skill checkpoint — Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion audit {#skill-navigation-row-256}",
        "### Row 256 skill checkpoint — Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion audit {#skill-navigation-row-256}",
        1,
    )

    b236 = _load_add236()._build_blocks()
    memory_baby = bump236_to_256(b236["memory_baby"])
    memory_baby = memory_baby.replace(
        "### Row 236 baby picture {#row-236-baby-picture-row68-row216-born-oppenheimer-meta-prelude-capstone-reunion}",
        "### Row 256 baby picture {#row-256-baby-picture-row68-row256-born-oppenheimer-meta-prelude-capstone-reunion}",
        1,
    )
    memory_baby = memory_baby.replace("**Row 236 baby picture:**", "**Row 256 baby picture:**", 1)
    memory_baby = memory_baby.replace(
        "before row 255 electronic audit meta prelude capstone opens on the full capstone path.",
        "before row 257 Kohn–Sham meta prelude capstone opens on the full capstone path.",
        1,
    )

    memory_table = bump236_to_256(b236["memory_table"])
    memory_table = memory_table.replace("| 236 | Meta |", "| 256 | Meta |", 1)

    sources_table = bump236_to_256(b236["sources_table"])
    sources_table = sources_table.replace("| 236 | Row 68 → Row 216", "| 256 | Row 68 → Row 236", 1)

    prologue_stitch = bump236_to_256(b236["prologue_stitch"]).replace(
        "**Row 256 closing stitch", "**Row 256 closing stitch", 1
    )
    prologue_compass = bump236_to_256(b236["prologue_compass"]).replace(
        "Born–Oppenheimer meta prelude capstone reunion (row 236) |",
        "Born–Oppenheimer meta prelude capstone reunion (row 256) |",
        1,
    ).replace(
        "[Preface: row 236 skill checkpoint]",
        "[Preface: row 256 skill checkpoint]",
        1,
    )

    epilogue_loop = bump236_to_256(b236["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-236-closing-loop}", "{#row-256-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 216 closing loop (Row 68 → Row 216",
        "### Row 256 closing loop (Row 68 → Row 236",
        1,
    ).replace(
        "### Row 236 closing loop (Row 68 → Row 216",
        "### Row 256 closing loop (Row 68 → Row 236",
        1,
    ).replace(
        "### Row 256 closing loop (Row 68 → Row 216",
        "### Row 256 closing loop (Row 68 → Row 236",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 257 closing loop",
        "\n\n\n\n### Row 237 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump236_to_256(b236["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236) "
        "{#row68-row216-born-oppenheimer-meta-prelude-capstone-reunion-index-row-236}",
        "## Row 68 → Row 256 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 256) "
        "{#row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256}",
        1,
    )

    return {
        "row256_preface": row256_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": _row256_prologue_preview(),
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "memory_table": memory_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
    }


PROLOGUE_STITCH_ANCHOR = (
    "**Row 255 closing stitch (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-255-closing-stitch}"
)

ROW256_INSERT_MARKER = (
    "### Row 255 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
    "{#row-255-closing-loop}"
)

ROW255_STITCH_OLD = (
    "before row 256 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."
)
ROW255_STITCH_NEW = (
    "before row 257 Kohn–Sham meta prelude capstone reunion opens on the full capstone path."
)

ROW255_EPILOGUE_OLD = (
    "Proceed to [row 236](#row-236-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 235 on the full capstone path,"
)
ROW255_EPILOGUE_NEW = (
    "Proceed to [row 256](#row-256-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 255 on the full capstone path,"
)

ROW255_TAIL_OLD = (
    "When row 255 is complete, proceed to [row 256](preface.md#skill-navigation-row-256) when `cu.relax.out` exists on the full capstone path, to [row 236](preface.md#skill-navigation-row-236) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 236](preface.md#skill-navigation-row-236) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 255](preface.md#skill-navigation-row-255) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 254](preface.md#skill-navigation-row-254) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)
ROW255_TAIL_NEW = (
    "When row 255 is complete, proceed to [row 256](preface.md#skill-navigation-row-256) when `cu.relax.out` exists on the full capstone path, to [row 236](preface.md#skill-navigation-row-236) when `cu.relax.out` exists but IX.1 still feels disconnected from verified electronic audit meta prelude capstone on the opening-hinge capstone path alone, to [row 216](preface.md#skill-navigation-row-216) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 255](preface.md#skill-navigation-row-255) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge capstone path alone, to [row 254](preface.md#skill-navigation-row-254) when yaml exports still stall after verified export meta prelude capstone on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
)


def _strip_orphan_row256_epilogue(text: str) -> str:
    """Remove misplaced duplicate row-256 closing loops (wrong anchor region)."""
    marker = ROW256_INSERT_MARKER
    if marker not in text:
        return text
    cap_idx = text.index(marker)
    pattern = (
        r"\n\n### Row 256 closing loop \(Row 68 → Row 256 Row 68 → Row 56 "
        r"Born–Oppenheimer meta prelude capstone reunion\) \{#row-256-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop|\Z)"
    )

    def repl(m: re.Match[str]) -> str:
        if m.start() < cap_idx:
            return ""
        return m.group(0)

    return re.sub(pattern, repl, text, flags=re.DOTALL)


def _epilogue_has_row256_at_capstone(text: str) -> bool:
    marker = ROW256_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return (
        "### Row 256 closing loop (Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion)"
        in window
        and "{#row-256-closing-loop}" in window
        and "memory sheet row 256" in window
    )


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 256 skill checkpoint" in preface:
        print("preface: row 256 already present")
    else:
        if "### Row 255 skill checkpoint" not in preface:
            raise SystemExit("row 255 must exist before row 256")
        if ROW255_TAIL_OLD in preface:
            preface = preface.replace(ROW255_TAIL_OLD, ROW255_TAIL_NEW, 1)
        elif ROW255_TAIL_NEW in preface:
            print("preface: row 255 tail already updated")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row256_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 256")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Born–Oppenheimer meta prelude capstone reunion (row 256) |" not in prologue:
        needle = (
            "| Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 255) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 255 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(PROLOGUE_STITCH_ANCHOR, b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR, 1)
        preview_anchor = '| <span id="prologue-preview-row-236"></span>Row 236 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW255_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW255_STITCH_OLD, ROW255_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 256")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row256_epilogue(epilogue)
    if ROW255_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW255_EPILOGUE_OLD, ROW255_EPILOGUE_NEW, 1)
    if _epilogue_has_row256_at_capstone(epilogue):
        epilogue_path.write_text(epilogue)
        print("epilogue: row 256 closing loop already present at capstone anchor")
    else:
        if ROW256_INSERT_MARKER not in epilogue:
            raise SystemExit("epilogue row 255 insert anchor not found")
        epilogue = epilogue.replace(ROW256_INSERT_MARKER, b["epilogue_loop"] + "\n\n" + ROW256_INSERT_MARKER, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 256")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row256-born-oppenheimer-meta-prelude-capstone-reunion-index-row-256" not in sources:
        sources = sources.replace(
            "| 255 | Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone",
            b["sources_table"] + "| 255 | Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 255 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 255) "
            "{#row68-row255-electronic-audit-meta-prelude-capstone-reunion-index-row-255}"
        )
        if src_header not in sources:
            src_header = (
                "## Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 236) "
                "{#row68-row216-born-oppenheimer-meta-prelude-capstone-reunion-index-row-236}"
            )
        if b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 256")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 256 baby picture {#row-256-baby-picture-row68-row256" not in memory:
        memory = memory.replace(
            "| 255 | Meta | [Row 68 → Row 235 electronic audit meta prelude capstone reunion index]",
            b["memory_table"] + "| 255 | Meta | [Row 68 → Row 235 electronic audit meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 255 baby picture {#row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion}",
            "**Row 255 baby picture:**",
            "### Row 254 baby picture {#row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 256")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 256 baby already present")


if __name__ == "__main__":
    main()
