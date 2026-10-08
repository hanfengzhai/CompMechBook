#!/usr/bin/env python3
"""Add row 339 meta-stitch (Row 68 → Row 319 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–330) by delta for meta-stitch copy."""
    out = text

    def in_band(n: int) -> bool:
        return 100 <= n <= 330

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


def bump319_to_339(text: str) -> str:
    protected = (
        ("row-339-", "__P339__"),
        ("skill-navigation-row-339", "__S339__"),
        ("prologue-preview-row-339", "__PR339__"),
        ("{#row-339-closing-stitch}", "__ST339__"),
        ("{#row-339-closing-loop}", "__LP339__"),
        (
            "row68-row319-handshake3-meta-prelude-capstone-reunion-index-row-339",
            "__IDX339__",
        ),
        (
            "row-339-baby-picture-row68-row319-handshake3-meta-prelude-capstone-reunion",
            "__BB339__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add319():
    spec = importlib.util.spec_from_file_location("add319", ROOT / "scripts/add-row-319.py")
    add319 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add319)
    return add319


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 319 skill checkpoint")
    end = preface.index("\n## The copper wire through the book", start)
    row339_preface = bump319_to_339(preface[start:end]) + "\n\n"

    b319 = _load_add319()._build_blocks()
    prologue_stitch = bump319_to_339(
        b319["prologue_stitch"]
        .replace("{#row-319-closing-stitch}", "{#row-339-closing-stitch}")
        .replace(
            "**Row 319 closing stitch (Row 68 → Row 299",
            "**Row 339 closing stitch (Row 68 → Row 319",
        )
        .replace(
            "**Row 319 closing stitch (Row 68 → Row 319",
            "**Row 339 closing stitch (Row 68 → Row 319",
        )
    ).replace("**Row 359 closing stitch", "**Row 339 closing stitch", 1)
    prologue_compass = bump319_to_339(b319["prologue_compass"]).replace(
        "Handshake 3 meta prelude capstone reunion (row 319) |",
        "Handshake 3 meta prelude capstone reunion (row 339) |",
        1,
    )
    prologue_preview = bump319_to_339(b319["prologue_preview"]).replace(
        "Row 319 preview", "Row 339 preview", 1
    )

    epilogue_loop = bump319_to_339(b319["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-319-closing-loop}", "{#row-339-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 319 closing loop (Row 68 → Row 299",
        "### Row 339 closing loop (Row 68 → Row 319",
        1,
    ).replace(
        "### Row 339 closing loop (Row 68 → Row 299",
        "### Row 339 closing loop (Row 68 → Row 319",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 260 closing loop",
        "\n\n\n\n### Row 280 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump319_to_339(b319["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 319) "
        "{#row68-row299-handshake3-meta-prelude-capstone-reunion-index-row-319}",
        "## Row 68 → Row 319 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 339) "
        "{#row68-row319-handshake3-meta-prelude-capstone-reunion-index-row-339}",
        1,
    )

    sources_table = bump319_to_339(b319["sources_table"])
    sources_table = re.sub(
        r"^\| 339 \| Row 68 → Row 319",
        "| 339 | Row 68 → Row 319",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 339 | Row 68 → Row 319" not in sources_table:
        sources_table = sources_table.replace(
            "| 319 | Row 68 → Row 259", "| 339 | Row 68 → Row 319", 1
        )

    memory_table = bump319_to_339(b319["memory_table"])
    memory_table = memory_table.replace("| 319 | Meta |", "| 339 | Meta |", 1)

    memory_baby = bump319_to_339(b319["memory_baby"]).rstrip() + "\n\n"
    if "{#row-339-baby-picture-row68-row319" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 339 baby picture",
            "### Row 339 baby picture {#row-339-baby-picture-row68-row319-handshake3-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row339_preface": row339_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW257_STITCH_OLD = (
    "before row 339 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 359 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW259_STITCH_OLD = (
    "before row 280 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW259_STITCH_NEW = (
    "before row 300 Handshake 3 meta prelude capstone opens on the full capstone path."
)

ROW239_STITCH_OLD = (
    "before row 320 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW239_STITCH_NEW = (
    "before row 340 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW238_STITCH_OLD = (
    "before row 319 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW238_STITCH_NEW = (
    "before row 339 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW319_EPILOGUE_OLD = (
    "Proceed to [row 319](#row-319-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW319_EPILOGUE_NEW = (
    "Proceed to [row 339](#row-339-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 319 closing stitch (Row 68 → Row 319 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-319-closing-stitch}"
)

ROW319_INSERT_MARKER = (
    "### Row 299 closing loop (Row 68 → Row 299 Row 68 → Row 59 "
    "Handshake 3 meta prelude capstone reunion) {#row-319-closing-loop}"
)


def _insert_row339_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 339 closing loop" in epilogue:
        return epilogue
    if ROW319_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 319 insert anchor not found")
    return epilogue.replace(ROW319_INSERT_MARKER, proper_loop + "\n\n" + ROW319_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 339 skill checkpoint" in preface:
        print("preface: row 339 already present")
    else:
        if "### Row 319 skill checkpoint" not in preface:
            raise SystemExit("row 319 must exist before row 339")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row339_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 339")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 339) |" not in prologue:
        needle = (
            "| Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 319) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 319 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-319"></span>Row 319 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW257_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW257_STITCH_OLD, ROW257_STITCH_NEW, 1)
        if ROW238_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW238_STITCH_OLD, ROW238_STITCH_NEW, 1)
        if ROW259_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW259_STITCH_OLD, ROW259_STITCH_NEW, 1)
        if ROW239_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW239_STITCH_OLD, ROW239_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 339")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW319_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW319_EPILOGUE_OLD, ROW319_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row339_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 339")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row319-handshake3-meta-prelude-capstone-reunion-index-row-339" not in sources:
        sources = sources.replace(
            "| 319 | Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            b["sources_table"]
            + "| 319 | Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            1,
        )
        src299_header = (
            "## Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 319) "
            "{#row68-row299-handshake3-meta-prelude-capstone-reunion-index-row-319}"
        )
        if src299_header not in sources:
            src299_header = (
                "## Row 68 → Row 299 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 319) "
                "{#row68-row299-handshake3-meta-prelude-capstone-reunion-index-row-319} "
                "{#row68-row299-handshake3-meta-prelude-capstone-reunion-index-row-319}"
            )
        sources = sources.replace(
            src299_header,
            b["sources_index"] + src299_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 339")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-339-baby-picture-row68-row319" not in memory:
        memory = memory.replace(
            "| 319 | Meta | [Row 68 → Row 299 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"]
            + "| 319 | Meta | [Row 68 → Row 299 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 319 baby picture {#row-319-baby-picture-row68-row299-handshake3-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 319 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 339")


if __name__ == "__main__":
    main()
