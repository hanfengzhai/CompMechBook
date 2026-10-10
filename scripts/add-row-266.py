#!/usr/bin/env python3
"""Add row 266 meta-stitch (Row 68 → Row 246 ↔ Row 66 Writings canonical meta prelude capstone reunion, full capstone path)."""
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


def bump246_to_266(text: str) -> str:
    protected = (
        ("row-266-", "__P266__"),
        ("skill-navigation-row-266", "__S266__"),
        ("prologue-preview-row-266", "__PR266__"),
        ("{#row-266-closing-stitch}", "__ST266__"),
        ("{#row-266-closing-loop}", "__LP266__"),
        (
            "row68-row266-writings-meta-prelude-capstone-reunion-index-row-266",
            "__IDX266__",
        ),
        (
            "row-266-baby-picture-row68-row266-writings-meta-prelude-capstone-reunion",
            "__BABY266__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add246():
    spec = importlib.util.spec_from_file_location("add246", ROOT / "scripts/add-row-246.py")
    add246 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add246)
    return add246


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 246 skill checkpoint")
    end = preface.index("\n\n### Row 247 skill checkpoint", start)
    row266_preface = bump246_to_266(preface[start:end]).strip() + "\n\n"

    b246 = _load_add246()._build_blocks()
    prologue_stitch = bump246_to_266(
        b246["prologue_stitch"]
        .replace("{#row-246-closing-stitch}", "{#row-266-closing-stitch}")
        .replace(
            "**Row 246 closing stitch (Row 68 → Row 226",
            "**Row 266 closing stitch (Row 68 → Row 246",
        )
    )
    prologue_compass = bump246_to_266(b246["prologue_compass"]).replace(
        "Writings canonical meta prelude capstone reunion (row 246) |",
        "Writings canonical meta prelude capstone reunion (row 266) |",
        1,
    )
    prologue_preview = bump246_to_266(b246["prologue_preview"]).replace(
        "Row 246 preview", "Row 266 preview", 1
    ).replace("Row 226 preview", "Row 266 preview", 1)

    epilogue_loop = bump246_to_266(b246["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-246-closing-loop}", "{#row-266-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 246 closing loop (Row 68 → Row 226",
        "### Row 266 closing loop (Row 68 → Row 246",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 265 closing loop",
        "\n\n\n\n### Row 246 closing loop",
        "\n\n\n\n### Row 267 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump246_to_266(b246["sources_index"])
    sources_index = sources_index.replace(
        "row68-row226-writings-meta-prelude-capstone-reunion-index-row-246",
        "row68-row266-writings-meta-prelude-capstone-reunion-index-row-266",
    ).replace(
        "## Row 68 → Row 226 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 246)",
        "## Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 266) "
        "{#row68-row266-writings-meta-prelude-capstone-reunion-index-row-266}",
        1,
    )

    sources_table = bump246_to_266(b246["sources_table"])
    sources_table = re.sub(
        r"^\| 246 \| Row 68 → Row 226",
        "| 266 | Row 68 → Row 246",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 266 | Row 68 → Row 246" not in sources_table:
        sources_table = sources_table.replace(
            "| 246 | Row 68 → Row 226", "| 266 | Row 68 → Row 246", 1
        )

    memory_table = bump246_to_266(b246["memory_table"])
    memory_table = memory_table.replace("| 246 | Meta |", "| 266 | Meta |", 1)

    memory_baby = bump246_to_266(b246["memory_baby"]).rstrip() + "\n\n"
    if "{#row-266-baby-picture-row68-row266" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 246 baby picture",
            "### Row 266 baby picture {#row-266-baby-picture-row68-row266-writings-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row266_preface": row266_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW265_STITCH_OLD = (
    "before row 266 Writings canonical meta prelude capstone reunion opens on the full capstone path."
)
ROW265_STITCH_NEW = (
    "before row 267 part-boundary meta prelude capstone reunion opens on the full capstone path."
)

ROW265_INSERT_MARKER = (
    "### Row 265 closing loop (Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion) "
    "{#row-265-closing-loop}"
)

ROW265_EPILOGUE_OLD = (
    "Proceed to [row 266](#row-246-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 265 on the full capstone path,"
)
ROW265_EPILOGUE_NEW = (
    "Proceed to [row 265](#row-265-closing-loop) when row 68 closed but second-pass meta capstone still lags after row 264 on the full capstone path,"
)

EPILOGUE_266_STUB = (
    "### Row 246 closing loop (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) "
    "{#row-246-closing-loop}"
)


def _replace_epilogue_266_stub(epilogue: str, proper_loop: str) -> str:
    if EPILOGUE_266_STUB in epilogue:
        start = epilogue.index(EPILOGUE_266_STUB)
        end = epilogue.find("\n\n### Row 266 closing loop", start)
        if end == -1:
            end = epilogue.find("\n\n\n\n### Row 266 closing loop", start)
        if end == -1:
            raise SystemExit("row 266 epilogue stub end not found")
        return epilogue[:start] + proper_loop.strip() + "\n\n" + epilogue[end:]
    return epilogue


def _insert_row266_epilogue(epilogue: str, proper_loop: str) -> str:
    if EPILOGUE_266_STUB in epilogue:
        return _replace_epilogue_266_stub(epilogue, proper_loop)
    if "{#row-266-closing-loop}" in epilogue:
        pos = epilogue.find("{#row-266-closing-loop}")
        near = epilogue.find(ROW265_INSERT_MARKER)
        if near != -1 and abs(pos - near) < 12000:
            return epilogue
        return epilogue
    if ROW265_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 265 insert anchor not found")
    return epilogue.replace(ROW265_INSERT_MARKER, ROW265_INSERT_MARKER + "\n\n" + proper_loop, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 266 skill checkpoint" in preface and preface.index("### Row 266 skill checkpoint") < preface.index(
        copper
    ):
        print("preface: row 266 already present")
    else:
        if "### Row 265 skill checkpoint" not in preface:
            raise SystemExit("row 265 must exist before row 266")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row266_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 266")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Writings canonical meta prelude capstone reunion (row 266) |" not in prologue:
        needle = (
            "| Row 68 → Row 245 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 265) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 265 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchor = (
            "**Row 265 closing stitch (Row 68 → Row 245 Row 68 → Row 64 book-loop meta prelude capstone reunion).** "
            "{#row-265-closing-stitch}"
        )
        if stitch_anchor in prologue:
            prologue = prologue.replace(
                stitch_anchor,
                b["prologue_stitch"] + stitch_anchor,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-265"></span>Row 265 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW265_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW265_STITCH_OLD, ROW265_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 266")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW265_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW265_EPILOGUE_OLD, ROW265_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row266_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 266")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    idx_anchor = "row68-row266-writings-meta-prelude-capstone-reunion-index-row-266"
    if idx_anchor not in sources or "reunion index (row 266)" not in sources:
        src_header = (
            "## Row 68 → Row 244 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 264) "
            "{#row68-row244-book-loop-meta-prelude-capstone-reunion-index-row-264}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"].strip() + "\n\n" + src_header, 1)
        needle = "| 265 | Meta | [Row 68 → Row 245 second-pass meta prelude capstone reunion index]"
        if needle in sources and b["sources_table"].strip() not in sources:
            sources = sources.replace(
                needle,
                b["sources_table"] + needle,
                1,
            )
        sources_path.write_text(sources)
        print("sources: added row 266")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 266 baby picture {#row-266-baby-picture" not in memory:
        table_needles = (
            "| 265 | Meta | [Row 68 → Row 245 second-pass meta prelude capstone reunion index]",
            "| 264 | Meta | [Row 68 → Row 224 book-loop meta prelude capstone reunion index]",
        )
        for needle in table_needles:
            if needle in memory and b["memory_table"].strip() not in memory:
                memory = memory.replace(needle, b["memory_table"] + needle, 1)
                break
        inserted = False
        for baby_anchor in (
            "### Row 265 baby picture {#row-265-baby-picture-row68-row245-second-pass-meta-prelude-capstone-reunion}",
            "### Row 244 baby picture {#row-244-baby-picture-row68-row224-book-loop-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 266")


if __name__ == "__main__":
    main()
