#!/usr/bin/env python3
"""Add row 267 meta-stitch (Row 68 → Row 247 ↔ Row 67 part-boundary meta prelude capstone reunion, full capstone path)."""
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


def bump247_to_267(text: str) -> str:
    protected = (
        ("row-267-", "__P267__"),
        ("skill-navigation-row-267", "__S267__"),
        ("prologue-preview-row-267", "__PR267__"),
        ("{#row-267-closing-stitch}", "__ST267__"),
        ("{#row-267-closing-loop}", "__LP267__"),
        (
            "row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267",
            "__IDX267__",
        ),
        (
            "row-267-baby-picture-row68-row247-part-boundary-meta-prelude-capstone-reunion",
            "__BABY267__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add247():
    spec = importlib.util.spec_from_file_location("add247", ROOT / "scripts/add-row-247.py")
    add247 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add247)
    return add247


def _row267_sources_index() -> str:
    """Single row-267 reunion index block."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 267) "
        "{#row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 266)",
            start,
        )
        if end == -1:
            end = sources.find("\n\n## Row 68 → Row 268", start)
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump247_to_267(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 247 skill checkpoint", 1)[1]
        .split("### Row 248 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 267 closes the **part-boundary meta prelude capstone** on the full capstone path — "
        + "see [preface row 267](../preface.md#skill-navigation-row-267) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 247 skill checkpoint")
    end = preface.index("\n\n### Row 248 skill checkpoint", start)
    row267_preface = bump247_to_267(preface[start:end]).strip() + "\n\n"

    b247 = _load_add247()._build_blocks()
    prologue_stitch = bump247_to_267(
        b247["prologue_stitch"]
        .replace("{#row-247-closing-stitch}", "{#row-267-closing-stitch}")
        .replace(
            "**Row 247 closing stitch (Row 68 → Row 227",
            "**Row 267 closing stitch (Row 68 → Row 247",
        )
    )
    prologue_compass = bump247_to_267(b247["prologue_compass"]).replace(
        "part-boundary meta prelude capstone reunion (row 247) |",
        "part-boundary meta prelude capstone reunion (row 267) |",
        1,
    )
    prologue_preview = bump247_to_267(b247["prologue_preview"]).replace(
        "Row 247 preview", "Row 267 preview", 1
    )

    epilogue_loop = bump247_to_267(b247["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-247-closing-loop}", "{#row-267-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 247 closing loop (Row 68 → Row 227",
        "### Row 267 closing loop (Row 68 → Row 247",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 266 closing loop",
        "\n\n\n\n### Row 267 closing loop",
        "\n\n\n\n### Row 268 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = _row267_sources_index()
    sources_table = bump247_to_267(b247["sources_table"])
    sources_table = re.sub(
        r"^\| 247 \| Row 68 → Row 227",
        "| 267 | Row 68 → Row 247",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 267 | Row 68 → Row 247" not in sources_table:
        sources_table = sources_table.replace(
            "| 247 | Row 68 → Row 227", "| 267 | Row 68 → Row 247", 1
        )

    memory_table = bump247_to_267(b247["memory_table"])
    memory_table = memory_table.replace("| 247 | Meta |", "| 267 | Meta |", 1)

    memory_baby = bump247_to_267(b247["memory_baby"]).rstrip() + "\n\n"
    if "{#row-267-baby-picture-row68-row247" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 247 baby picture",
            "### Row 267 baby picture {#row-267-baby-picture-row68-row247-part-boundary-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row267_preface": row267_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW266_STITCH_OLD = (
    "before row 267 part-boundary meta prelude capstone reunion opens on the full capstone path."
)
ROW266_STITCH_NEW = (
    "before row 268 midpoint meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 266 closing stitch (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** "
    "{#row-266-closing-stitch}"
)

ROW267_INSERT_MARKER = (
    "### Row 266 closing loop (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) "
    "{#row-266-closing-loop}"
)

ROW266_EPILOGUE_OLD = (
    "Proceed to [row 247](#row-247-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 266 on the full capstone path,"
)
ROW266_EPILOGUE_NEW = (
    "Proceed to [row 267](#row-267-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 266 on the full capstone path,"
)


def _dedupe_epilogue_row267(epilogue: str, proper_loop: str) -> str:
    """Remove trailing orphan row 267/268 stubs appended at file end."""
    orphan = "### Row 267 closing loop (Row 68 → Row 267 Row 68 → Row 67"
    while orphan in epilogue:
        idx = epilogue.rfind(orphan)
        if idx < len(epilogue) // 2:
            break
        epilogue = epilogue[:idx].rstrip() + "\n\n"
    return epilogue


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 267 skill checkpoint" in preface and preface.index("### Row 267 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 267 already present")
    else:
        if "### Row 266 skill checkpoint" not in preface:
            raise SystemExit("row 266 must exist before row 267")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row267_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 267")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "part-boundary meta prelude capstone reunion (row 267) |" not in prologue:
        needle = (
            "| Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 266) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 266 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR not in prologue:
            # Insert stitch via fix-row-267-anchors if missing
            stitch_anchor = (
                "**Row 266 closing stitch (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** "
                "{#row-266-closing-stitch}"
            )
            if stitch_anchor in prologue:
                prologue = prologue.replace(
                    stitch_anchor,
                    b["prologue_stitch"] + stitch_anchor,
                    1,
                )
        else:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-266"></span>Row 266 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW266_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW266_STITCH_OLD, ROW266_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 267")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW266_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW266_EPILOGUE_OLD, ROW266_EPILOGUE_NEW, 1)
    if epilogue.count("{#row-267-closing-loop}") < 2:
        marker = ROW267_INSERT_MARKER
        if marker in epilogue and b["epilogue_loop"].strip() not in epilogue:
            epilogue = epilogue.replace(marker, marker + "\n\n" + b["epilogue_loop"], 1)
            print("epilogue: added row 267")
        elif "{#row-267-closing-loop}" not in epilogue:
            raise SystemExit("epilogue row 266 insert anchor not found")
        else:
            print("epilogue: row 267 closing loop already present")
    epilogue = _dedupe_epilogue_row267(epilogue, b["epilogue_loop"])
    epilogue_path.write_text(epilogue)

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    idx_anchor = "row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267"
    if idx_anchor not in sources or "reunion index (row 267)" not in sources.split(idx_anchor)[0][-200:]:
        src_header = (
            "## Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 266) "
            "{#row68-row246-writings-meta-prelude-capstone-reunion-index-row-266}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"].strip() + "\n\n" + src_header, 1)
        needle = "| 266 | Meta | [Row 68 → Row 246 Writings canonical meta prelude capstone reunion index]"
        if needle in sources and b["sources_table"].strip() not in sources:
            sources = sources.replace(
                needle,
                b["sources_table"] + needle,
                1,
            )
        sources_path.write_text(sources)
        print("sources: added row 267")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 267 baby picture {#row-267-baby-picture-row68-row247" not in memory:
        needle = "| 266 | Meta | [Row 68 → Row 246 Writings canonical meta prelude capstone reunion index]"
        if needle in memory and b["memory_table"].strip() not in memory:
            memory = memory.replace(needle, b["memory_table"] + needle, 1)
        inserted = False
        for baby_anchor in (
            "### Row 266 baby picture {#row-266-baby-picture-row68-row266-writings-meta-prelude-capstone-reunion}",
            "### Row 246 baby picture {#row-246-baby-picture-row68-row226-writings-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 267")


if __name__ == "__main__":
    main()
