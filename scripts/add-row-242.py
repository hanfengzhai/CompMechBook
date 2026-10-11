#!/usr/bin/env python3
"""Add row 242 meta-stitch (Row 68 → Row 222 ↔ Row 62 Handshake 4b meta prelude capstone reunion, full capstone path)."""
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


def bump222_to_242(text: str) -> str:
    protected = (
        ("row-242-", "__P242__"),
        ("skill-navigation-row-242", "__S242__"),
        ("prologue-preview-row-242", "__prologue-preview-row-242__"),
        ("{#row-242-closing-stitch}", "__{#row-242-closing-stitch}__"),
        ("{#row-242-closing-loop}", "__{#row-242-closing-loop}__"),
        (
            "row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242",
            "__row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242__",
        ),
        (
            "row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion",
            "__row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add222():
    spec = importlib.util.spec_from_file_location("add222", ROOT / "scripts/add-row-222.py")
    add221 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add221)
    return add221


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index(
        "### Row 222 skill checkpoint — Row 68 → Row 202 Row 68 → Row 62"
    )
    end = preface.index("\n\n### Row 223 skill checkpoint", start)
    row242_preface = bump222_to_242(preface[start:end]).strip() + "\n\n"

    b222 = _load_add222()._build_blocks()
    out = {
        "row242_preface": row242_preface,
        "prologue_compass": bump222_to_242(b222["prologue_compass"]).replace(
            "Handshake 4b meta prelude capstone reunion (row 242) |",
            "Handshake 4b meta prelude capstone reunion (row 242) |",
            1,
        ).replace(
            "row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242",
            "row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242",
        ).replace(
            "skill-navigation-row-242",
            "skill-navigation-row-242",
        ).replace(
            "row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion",
            "row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion",
        ).replace(
            "#row-242-closing-stitch",
            "#row-242-closing-stitch",
        ).replace(
            "#row-242-closing-loop",
            "#row-242-closing-loop",
        ),
        "prologue_stitch": bump222_to_242(b222["prologue_stitch"]).replace(
            "{#row-242-closing-stitch}", "{#row-242-closing-stitch}"
        ).replace(
            "**Row 242 closing stitch (Row 68 → Row 222",
            "**Row 241 closing stitch (Row 68 → Row 221",
        ),
        "prologue_preview": bump222_to_242(b222["prologue_preview"]).replace(
            "Row 242 preview", "Row 241 preview", 1
        ).replace("prologue-preview-row-242", "prologue-preview-row-242"),
        "epilogue_loop": bump222_to_242(b222["epilogue_loop"]),
        "sources_table": bump222_to_242(b222["sources_table"]).replace(
            "| 242 | Row 68 → Row 222", "| 241 | Row 68 → Row 221", 1
        ),
        "sources_index": bump222_to_242(b222["sources_index"]).replace(
            "row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242",
            "row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242",
        ).replace(
            "## Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 242) {#row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242}",
            "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 241) "
            "{#row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242}",
            1,
        ),
        "memory_table": bump222_to_242(b222["memory_table"]).replace("| 242 | Meta |", "| 241 | Meta |", 1),
        "memory_baby": bump222_to_242(b222["memory_baby"]),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace("{#row-242-closing-loop}", "{#row-242-closing-loop}", 1)
    loop = loop.replace(
        "### Row 242 closing loop (Row 68 → Row 222",
        "### Row 241 closing loop (Row 68 → Row 221",
        1,
    )
    for spill in ("\n\n\n\n### Row 241 closing loop", "\n\n\n\n### Row 221 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    if "{#row-242-baby-picture-row68-row222" not in out["memory_baby"]:
        out["memory_baby"] = out["memory_baby"].replace(
            "### Row 241 baby picture",
            "### Row 242 baby picture {#row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion}",
            1,
        )
    return out


def _row241_tail() -> str:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    idx = preface.index("When row 241 is complete,")
    end = preface.index(" or extend prose only under `writings/` then sync.", idx)
    return preface[idx:end] + " or extend prose only under `writings/` then sync."


ROW241_TAIL_OLD = _row241_tail()


def _row241_tail_new() -> str:
    return ROW241_TAIL_OLD.replace(
        "proceed to [row 221](preface.md#skill-navigation-row-242)",
        "proceed to [row 241](preface.md#skill-navigation-row-242)",
        1,
    )


ROW241_EPILOGUE_OLD = (
    "Proceed to [row 221](#row-242-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 240 on the full capstone path,"
)
ROW241_EPILOGUE_NEW = (
    "Proceed to [row 242](#row-242-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 241 on the full capstone path,"
)

ROW241_STITCH_OLD = (
    "before row 243 orchestration meta prelude capstone reunion opens on the full capstone path."
)
ROW241_STITCH_NEW = (
    "before row 243 orchestration meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 241 closing stitch (Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-241-closing-stitch}"
)

ROW241_INSERT_MARKER = (
    "### Row 240 closing loop (Row 68 → Row 220 Row 68 → Row 60 "
    "Handshake 3 meta prelude capstone reunion) {#row-240-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"
    row240_tail_new = _row241_tail_new()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 242 skill checkpoint" in preface:
        print("preface: row 242 already present")
    else:
        if "### Row 241 skill checkpoint" not in preface:
            raise SystemExit("row 241 must exist before row 242")
        if ROW241_TAIL_OLD in preface:
            preface = preface.replace(ROW241_TAIL_OLD, row240_tail_new, 1)
        elif row240_tail_new in preface:
            print("preface: row 241 tail already updated")
        else:
            raise SystemExit("row 241 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row242_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 242")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 4b meta prelude capstone reunion (row 242) |" not in prologue:
        needle = "| Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 241) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 241 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-241"></span>Row 241 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW241_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW241_STITCH_OLD, ROW241_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 242")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW241_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW241_EPILOGUE_OLD, ROW241_EPILOGUE_NEW, 1)
    if "{#row-242-closing-loop}" not in epilogue:
        marker = ROW241_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 241 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 242")
    else:
        print("epilogue: row 242 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if (
        "| 242 | Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone"
        not in sources
    ):
        sources = sources.replace(
            "| 222 | Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            b["sources_table"] + "| 222 | Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 242) {#row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 242")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-242-baby-picture-row68-row222" not in memory:
        memory = memory.replace(
            "| 242 | Meta | [Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index]",
            b["memory_table"] + "| 242 | Meta | [Row 68 → Row 201 Handshake 4a meta prelude capstone reunion index]",
            1,
        )
        for baby_anchor in (
            "### Row 221 baby picture {#row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion}",
            "### Row 241 baby picture {#row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion} (Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 242")


if __name__ == "__main__":
    main()
