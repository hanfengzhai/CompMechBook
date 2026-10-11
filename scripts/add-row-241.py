#!/usr/bin/env python3
"""Add row 241 meta-stitch (Row 68 → Row 221 ↔ Row 61 Handshake 4a meta prelude capstone reunion, full capstone path)."""
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


def bump221_to_241(text: str) -> str:
    protected = (
        ("row-241-", "__P241__"),
        ("skill-navigation-row-241", "__S241__"),
        ("prologue-preview-row-241", "__PR241__"),
        ("{#row-241-closing-stitch}", "__ST241__"),
        ("{#row-241-closing-loop}", "__LP241__"),
        (
            "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
            "__IDX241__",
        ),
        (
            "row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion",
            "__BABY241__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add221():
    spec = importlib.util.spec_from_file_location("add221", ROOT / "scripts/add-row-221.py")
    add221 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add221)
    return add221


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index(
        "### Row 221 skill checkpoint — Row 68 → Row 201 Row 68 → Row 61"
    )
    end = preface.index("\n\n### Row 222 skill checkpoint", start)
    row241_preface = bump221_to_241(preface[start:end]).strip() + "\n\n"

    b221 = _load_add221()._build_blocks()
    out = {
        "row241_preface": row241_preface,
        "prologue_compass": bump221_to_241(b221["prologue_compass"]).replace(
            "Handshake 4a meta prelude capstone reunion (row 221) |",
            "Handshake 4a meta prelude capstone reunion (row 241) |",
            1,
        ).replace(
            "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
            "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
        ).replace(
            "skill-navigation-row-221",
            "skill-navigation-row-241",
        ).replace(
            "row-221-baby-picture-row68-row201-handshake4a-meta-prelude-capstone-reunion",
            "row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion",
        ).replace(
            "#row-221-closing-stitch",
            "#row-241-closing-stitch",
        ).replace(
            "#row-221-closing-loop",
            "#row-241-closing-loop",
        ),
        "prologue_stitch": bump221_to_241(b221["prologue_stitch"]).replace(
            "{#row-221-closing-stitch}", "{#row-241-closing-stitch}"
        ).replace(
            "**Row 221 closing stitch (Row 68 → Row 201",
            "**Row 241 closing stitch (Row 68 → Row 221",
        ),
        "prologue_preview": bump221_to_241(b221["prologue_preview"]).replace(
            "Row 221 preview", "Row 241 preview", 1
        ).replace("prologue-preview-row-221", "prologue-preview-row-241"),
        "epilogue_loop": bump221_to_241(b221["epilogue_loop"]),
        "sources_table": bump221_to_241(b221["sources_table"]).replace(
            "| 221 | Row 68 → Row 221", "| 241 | Row 68 → Row 221", 1
        ),
        "sources_index": bump221_to_241(b221["sources_index"]).replace(
            "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
            "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
        ).replace(
            "## Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 221)",
            "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 241) "
            "{#row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241}",
            1,
        ),
        "memory_table": bump221_to_241(b221["memory_table"]).replace("| 221 | Meta |", "| 241 | Meta |", 1),
        "memory_baby": bump221_to_241(b221["memory_baby"]),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace("{#row-221-closing-loop}", "{#row-241-closing-loop}", 1)
    loop = loop.replace(
        "### Row 201 closing loop (Row 68 → Row 201",
        "### Row 241 closing loop (Row 68 → Row 221",
        1,
    )
    for spill in ("\n\n\n\n### Row 241 closing loop", "\n\n\n\n### Row 221 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    if "{#row-241-baby-picture-row68-row221" not in out["memory_baby"]:
        out["memory_baby"] = out["memory_baby"].replace(
            "### Row 241 baby picture",
            "### Row 241 baby picture {#row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion}",
            1,
        )
    return out


def _row240_tail() -> str:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    idx = preface.index("When row 240 is complete,")
    end = preface.index(" or extend prose only under `writings/` then sync.", idx)
    return preface[idx:end] + " or extend prose only under `writings/` then sync."


ROW240_TAIL_OLD = _row240_tail()


def _row240_tail_new() -> str:
    return ROW240_TAIL_OLD.replace(
        "proceed to [row 221](preface.md#skill-navigation-row-221)",
        "proceed to [row 241](preface.md#skill-navigation-row-241)",
        1,
    )


ROW240_EPILOGUE_OLD = (
    "Proceed to [row 221](#row-221-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 240 on the full capstone path,"
)
ROW240_EPILOGUE_NEW = (
    "Proceed to [row 241](#row-241-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 240 on the full capstone path,"
)

ROW240_STITCH_OLD = (
    "before row 241 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)
ROW240_STITCH_NEW = (
    "before row 242 Handshake 4b meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 240 closing stitch (Row 68 → Row 220 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-240-closing-stitch}"
)

ROW240_INSERT_MARKER = (
    "### Row 240 closing loop (Row 68 → Row 220 Row 68 → Row 60 "
    "Handshake 3 meta prelude capstone reunion) {#row-240-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"
    row240_tail_new = _row240_tail_new()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 241 skill checkpoint" in preface:
        print("preface: row 241 already present")
    else:
        if "### Row 240 skill checkpoint" not in preface:
            raise SystemExit("row 240 must exist before row 241")
        if ROW240_TAIL_OLD in preface:
            preface = preface.replace(ROW240_TAIL_OLD, row240_tail_new, 1)
        elif row240_tail_new in preface:
            print("preface: row 240 tail already updated")
        else:
            raise SystemExit("row 240 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row241_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 241")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 4a meta prelude capstone reunion (row 241) |" not in prologue:
        needle = "| Row 68 → Row 220 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 240) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 240 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-240"></span>Row 240 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW240_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW240_STITCH_OLD, ROW240_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 241")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW240_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW240_EPILOGUE_OLD, ROW240_EPILOGUE_NEW, 1)
    if "{#row-241-closing-loop}" not in epilogue:
        marker = ROW240_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 240 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 241")
    else:
        print("epilogue: row 241 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if (
        "| 241 | Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone"
        not in sources
    ):
        sources = sources.replace(
            "| 221 | Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            b["sources_table"] + "| 221 | Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 221)"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 241")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-241-baby-picture-row68-row221" not in memory:
        memory = memory.replace(
            "| 221 | Meta | [Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index]",
            b["memory_table"] + "| 221 | Meta | [Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index]",
            1,
        )
        for baby_anchor in (
            "### Row 221 baby picture {#row-221-baby-picture-row68-row201-handshake4a-meta-prelude-capstone-reunion}",
            "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 241")


if __name__ == "__main__":
    main()
