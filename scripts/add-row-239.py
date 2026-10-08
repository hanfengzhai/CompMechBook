#!/usr/bin/env python3
"""Add row 239 meta-stitch (Row 68 → Row 219 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text

    def in_band(n: int) -> bool:
        return 100 <= n <= 250

    def repl_row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"row {n + delta}" if in_band(n) else m.group(0)

    def repl_Row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"Row {n + delta}" if in_band(n) else m.group(0)

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


def bump219_to_239(text: str) -> str:
    protected = (
        ("row-239-", "__P239__"),
        ("skill-navigation-row-239", "__S239__"),
        ("prologue-preview-row-239", "__PR239__"),
        ("{#row-239-closing-stitch}", "__ST239__"),
        ("{#row-239-closing-loop}", "__LP239__"),
        (
            "row68-row219-handshake3-meta-prelude-capstone-reunion-index-row-239",
            "__IDX239__",
        ),
        (
            "row-239-baby-picture-row68-row219-handshake3-meta-prelude-capstone-reunion",
            "__BB239__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add219():
    spec = importlib.util.spec_from_file_location("add219", ROOT / "scripts/add-row-219.py")
    add219 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add219)
    return add219


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 219 skill checkpoint")
    end = preface.index("\n\n### Row 220 skill checkpoint", start)
    row239_preface = bump219_to_239(preface[start:end]) + "\n\n"

    b219 = _load_add219()._build_blocks()
    prologue_stitch = bump219_to_239(
        b219["prologue_stitch"]
        .replace("{#row-219-closing-stitch}", "{#row-239-closing-stitch}")
        .replace(
            "**Row 219 closing stitch (Row 68 → Row 199",
            "**Row 239 closing stitch (Row 68 → Row 219",
        )
        .replace(
            "**Row 199 closing stitch (Row 68 → Row 179",
            "**Row 239 closing stitch (Row 68 → Row 219",
        )
    ).replace("**Row 259 closing stitch", "**Row 239 closing stitch", 1)
    prologue_compass = bump219_to_239(b219["prologue_compass"]).replace(
        "Handshake 3 meta prelude capstone reunion (row 219) |",
        "Handshake 3 meta prelude capstone reunion (row 239) |",
        1,
    )
    prologue_preview = bump219_to_239(b219["prologue_preview"]).replace(
        "Row 219 preview", "Row 239 preview", 1
    )

    epilogue_loop = bump219_to_239(b219["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-219-closing-loop}", "{#row-239-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 219 closing loop (Row 68 → Row 199",
        "### Row 239 closing loop (Row 68 → Row 219",
        1,
    ).replace(
        "### Row 239 closing loop (Row 68 → Row 199",
        "### Row 239 closing loop (Row 68 → Row 219",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 220 closing loop",
        "\n\n\n\n### Row 200 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump219_to_239(b219["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 219) "
        "{#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219}",
        "## Row 68 → Row 219 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 239) "
        "{#row68-row219-handshake3-meta-prelude-capstone-reunion-index-row-239}",
        1,
    )

    sources_table = bump219_to_239(b219["sources_table"])
    sources_table = re.sub(
        r"^\| 219 \| Row 68 → Row 219",
        "| 239 | Row 68 → Row 219",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 239 | Row 68 → Row 219" not in sources_table:
        sources_table = sources_table.replace(
            "| 219 | Row 68 → Row 199", "| 239 | Row 68 → Row 219", 1
        )

    memory_table = bump219_to_239(b219["memory_table"])
    memory_table = memory_table.replace("| 219 | Meta |", "| 239 | Meta |", 1)

    memory_baby = bump219_to_239(b219["memory_baby"]).rstrip() + "\n\n"
    if "{#row-239-baby-picture-row68-row219" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 239 baby picture",
            "### Row 239 baby picture {#row-239-baby-picture-row68-row219-handshake3-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row239_preface": row239_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW237_STITCH_OLD = (
    "before row 239 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW237_STITCH_NEW = (
    "before row 259 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW238_STITCH_OLD = (
    "before row 199 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW238_STITCH_NEW = (
    "before row 239 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW237_EPILOGUE_OLD = (
    "Proceed to [row 238](#row-238-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 237 on the full capstone path,"
)
ROW237_EPILOGUE_NEW = (
    "Proceed to [row 239](#row-239-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

ROW238_EPILOGUE_OLD = (
    "Proceed to [row 219](#row-219-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 218 on the full capstone path,"
)
ROW238_EPILOGUE_NEW = (
    "Proceed to [row 239](#row-239-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 238 closing stitch (Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-238-closing-stitch}"
)

ROW238_INSERT_MARKER = (
    "### Row 218 closing loop (Row 68 → Row 218 Row 68 → Row 58 "
    "DFT workflows meta prelude capstone reunion) {#row-238-closing-loop}"
)


def _insert_row239_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 239 closing loop" in epilogue:
        return epilogue
    if ROW238_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 238 insert anchor not found")
    return epilogue.replace(ROW238_INSERT_MARKER, proper_loop + "\n\n" + ROW238_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 239 skill checkpoint" in preface:
        print("preface: row 239 already present")
    else:
        if "### Row 238 skill checkpoint" not in preface:
            raise SystemExit("row 238 must exist before row 239")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row239_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 239")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 239) |" not in prologue:
        needle = "| Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 238) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 238 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-238"></span>Row 238 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW237_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW237_STITCH_OLD, ROW237_STITCH_NEW, 1)
        if ROW238_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW238_STITCH_OLD, ROW238_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 239")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW237_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW237_EPILOGUE_OLD, ROW237_EPILOGUE_NEW, 1)
    if ROW238_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW238_EPILOGUE_OLD, ROW238_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row239_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 239")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row219-handshake3-meta-prelude-capstone-reunion-index-row-239" not in sources:
        sources = sources.replace(
            "| 219 | Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 219 | Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            1,
        )
        src219_header = (
            "## Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 219) "
            "{#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219}"
        )
        if src219_header not in sources:
            src219_header = (
                "## Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 219)"
            )
        sources = sources.replace(
            src219_header,
            b["sources_index"] + src219_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 239")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-239-baby-picture-row68-row219" not in memory:
        memory = memory.replace(
            "| 219 | Meta | [Row 68 → Row 199 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 219 | Meta | [Row 68 → Row 199 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 219 baby picture {#row-219-baby-picture-row68-row199-handshake3-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 219 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 239")


if __name__ == "__main__":
    main()
