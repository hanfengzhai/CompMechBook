#!/usr/bin/env python3
"""Add row 268 meta-stitch (Row 68 → Row 248 ↔ Row 48 midpoint meta prelude capstone reunion, full capstone path)."""
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


def bump248_to_268(text: str) -> str:
    protected = (
        ("row-268-", "__P268__"),
        ("skill-navigation-row-268", "__S268__"),
        ("prologue-preview-row-268", "__PR268__"),
        ("{#row-268-closing-stitch}", "__ST268__"),
        ("{#row-268-closing-loop}", "__LP268__"),
        (
            "row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268",
            "__IDX268__",
        ),
        (
            "row-268-baby-picture-row68-row248-midpoint-meta-prelude-capstone-reunion",
            "__BABY268__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add248():
    spec = importlib.util.spec_from_file_location("add248", ROOT / "scripts/add-row-248.py")
    add248 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add248)
    return add248


def _row268_sources_index() -> str:
    """Single row-268 reunion index block."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 268) "
        "{#row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 267)",
            start,
        )
        if end == -1:
            end = sources.find("\n\n## Row 68 → Row 268", start)
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump248_to_268(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 248 skill checkpoint", 1)[1]
        .split("### Row 255 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 268 closes the **midpoint meta prelude capstone** on the full capstone path — "
        + "see [preface row 268](../preface.md#skill-navigation-row-268) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 248 skill checkpoint")
    end = preface.index("\n\n### Row 255 skill checkpoint", start)
    row268_preface = bump248_to_268(preface[start:end]).strip() + "\n\n"

    b248 = _load_add248()._build_blocks()
    prologue_stitch = bump248_to_268(
        b248["prologue_stitch"]
        .replace("{#row-248-closing-stitch}", "{#row-268-closing-stitch}")
        .replace(
            "**Row 248 closing stitch (Row 68 → Row 228",
            "**Row 268 closing stitch (Row 68 → Row 248",
        )
    )
    prologue_compass = bump248_to_268(b248["prologue_compass"]).replace(
        "midpoint meta prelude capstone reunion (row 248) |",
        "midpoint meta prelude capstone reunion (row 268) |",
        1,
    )
    prologue_preview = bump248_to_268(b248["prologue_preview"]).replace(
        "Row 248 preview", "Row 268 preview", 1
    )

    epilogue_loop = bump248_to_268(b248["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-248-closing-loop}", "{#row-268-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 248 closing loop (Row 68 → Row 228",
        "### Row 268 closing loop (Row 68 → Row 248",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 267 closing loop",
        "\n\n\n\n### Row 268 closing loop",
        "\n\n\n\n### Row 269 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = _row268_sources_index()
    sources_table = bump248_to_268(b248["sources_table"])
    sources_table = re.sub(
        r"^\| 248 \| Row 68 → Row 228",
        "| 268 | Row 68 → Row 248",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 268 | Row 68 → Row 248" not in sources_table:
        sources_table = sources_table.replace(
            "| 248 | Row 68 → Row 228", "| 268 | Row 68 → Row 248", 1
        )

    memory_table = bump248_to_268(b248["memory_table"])
    memory_table = memory_table.replace("| 248 | Meta |", "| 268 | Meta |", 1)

    memory_baby = bump248_to_268(b248["memory_baby"]).rstrip() + "\n\n"
    if "{#row-268-baby-picture-row68-row248" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 248 baby picture",
            "### Row 268 baby picture {#row-268-baby-picture-row68-row248-midpoint-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row268_preface": row268_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW267_STITCH_OLD = (
    "before row 268 midpoint meta prelude capstone reunion opens on the full capstone path."
)
ROW267_STITCH_NEW = (
    "before row 269 taxonomy meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 267 closing stitch (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** "
    "{#row-267-closing-stitch}"
)

ROW268_INSERT_MARKER = (
    "### Row 267 closing loop (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-267-closing-loop}"
)

ROW267_EPILOGUE_OLD = (
    "Proceed to [row 267](#row-267-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 266 on the full capstone path,"
)
ROW267_EPILOGUE_NEW = (
    "Proceed to [row 268](#row-268-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 267 on the full capstone path,"
)


def _dedupe_epilogue_row268(epilogue: str, proper_loop: str) -> str:
    """Remove trailing orphan row 267/268 stubs appended at file end."""
    orphan = "### Row 268 closing loop (Row 68 → Row 268 Row 68 → Row 48"
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
    if "### Row 268 skill checkpoint" in preface and preface.index("### Row 268 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 268 already present")
    else:
        if "### Row 267 skill checkpoint" not in preface:
            raise SystemExit("row 267 must exist before row 268")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row268_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 268")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "midpoint meta prelude capstone reunion (row 268) |" not in prologue:
        needle = (
            "| Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 267) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 267 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR not in prologue:
            # Insert stitch via fix-row-268-anchors if missing
            stitch_anchor = (
                "**Row 267 closing stitch (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** "
                "{#row-267-closing-stitch}"
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
        preview_anchor = '| <span id="prologue-preview-row-267"></span>Row 267 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW267_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW267_STITCH_OLD, ROW267_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 268")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW267_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW267_EPILOGUE_OLD, ROW267_EPILOGUE_NEW, 1)
    if epilogue.count("{#row-268-closing-loop}") < 2:
        marker = ROW268_INSERT_MARKER
        if marker in epilogue and b["epilogue_loop"].strip() not in epilogue:
            epilogue = epilogue.replace(marker, marker + "\n\n" + b["epilogue_loop"], 1)
            print("epilogue: added row 268")
        elif "{#row-268-closing-loop}" not in epilogue:
            raise SystemExit("epilogue row 267 insert anchor not found")
        else:
            print("epilogue: row 268 closing loop already present")
    epilogue = _dedupe_epilogue_row268(epilogue, b["epilogue_loop"])
    epilogue_path.write_text(epilogue)

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    idx_anchor = "row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268"
    if idx_anchor not in sources or "reunion index (row 268)" not in sources.split(idx_anchor)[0][-200:]:
        src_header = (
            "## Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 267) "
            "{#row68-row247-part-boundary-meta-prelude-capstone-reunion-index-row-267}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"].strip() + "\n\n" + src_header, 1)
        needle = "| 267 | Meta | [Row 68 → Row 247 part-boundary meta prelude capstone reunion index]"
        if needle in sources and b["sources_table"].strip() not in sources:
            sources = sources.replace(
                needle,
                b["sources_table"] + needle,
                1,
            )
        sources_path.write_text(sources)
        print("sources: added row 268")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 268 baby picture {#row-268-baby-picture-row68-row248" not in memory:
        needle = "| 267 | Meta | [Row 68 → Row 247 part-boundary meta prelude capstone reunion index]"
        if needle in memory and b["memory_table"].strip() not in memory:
            memory = memory.replace(needle, b["memory_table"] + needle, 1)
        inserted = False
        for baby_anchor in (
            "### Row 267 baby picture {#row-267-baby-picture-row68-row247-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 268")


if __name__ == "__main__":
    main()
