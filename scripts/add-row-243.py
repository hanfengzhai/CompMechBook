#!/usr/bin/env python3
"""Add row 243 meta-stitch (Row 68 → Row 223 ↔ Row 63 orchestration meta prelude capstone reunion, full capstone path)."""
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


def bump223_to_243(text: str) -> str:
    protected = (
        ("row-243-", "__P243__"),
        ("skill-navigation-row-243", "__S243__"),
        ("prologue-preview-row-243", "__prologue-preview-row-243__"),
        ("{#row-243-closing-stitch}", "__{#row-243-closing-stitch}__"),
        ("{#row-243-closing-loop}", "__{#row-243-closing-loop}__"),
        (
            "row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243",
            "__row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243__",
        ),
        (
            "row-243-baby-picture-row68-row223-orchestration-meta-prelude-capstone-reunion",
            "__row-243-baby-picture-row68-row223-orchestration-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add223():
    spec = importlib.util.spec_from_file_location("add223", ROOT / "scripts/add-row-223.py")
    add223 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add223)
    return add223


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 223 skill checkpoint")
    end = preface.index("\n\n### Row 224 skill checkpoint", start)
    row243_preface = bump223_to_243(preface[start:end]).strip() + "\n\n"

    b223 = _load_add223()._build_blocks()
    out = {
        "row243_preface": row243_preface,
        "prologue_compass": bump223_to_243(b223["prologue_compass"]),
        "prologue_stitch": bump223_to_243(b223["prologue_stitch"]),
        "prologue_preview": bump223_to_243(b223["prologue_preview"]),
        "epilogue_loop": bump223_to_243(b223["epilogue_loop"]),
        "sources_table": bump223_to_243(b223["sources_table"]).replace(
            "| 223 | Row 68 → Row 203", "| 243 | Row 68 → Row 223", 1
        ),
        "sources_index": bump223_to_243(b223["sources_index"]).replace(
            "## Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 223) "
            "{#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223}",
            "## Row 68 → Row 223 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 243) "
            "{#row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243}",
            1,
        ),
        "memory_table": bump223_to_243(b223["memory_table"]).replace("| 223 | Meta |", "| 243 | Meta |", 1),
        "memory_baby": bump223_to_243(b223["memory_baby"]),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace("{#row-243-closing-loop}", "{#row-243-closing-loop}", 1)
    loop = loop.replace(
        "### Row 243 closing loop (Row 68 → Row 223",
        "### Row 242 closing loop (Row 68 → Row 222",
        1,
    )
    for spill in ("\n\n\n\n### Row 242 closing loop", "\n\n\n\n### Row 223 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    if "{#row-243-baby-picture-row68-row223" not in out["memory_baby"]:
        out["memory_baby"] = out["memory_baby"].replace(
            "### Row 243 baby picture",
            "### Row 243 baby picture {#row-243-baby-picture-row68-row223-orchestration-meta-prelude-capstone-reunion}",
            1,
        )
    return out


def _row242_tail() -> str:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    idx = preface.index("When row 242 is complete,")
    end = preface.index(" or extend prose only under `writings/` then sync.", idx)
    return preface[idx:end] + " or extend prose only under `writings/` then sync."


ROW242_TAIL_OLD = _row242_tail()


def _row242_tail_new() -> str:
    return ROW242_TAIL_OLD.replace(
        "proceed to [row 243](preface.md#skill-navigation-row-243)",
        "proceed to [row 243](preface.md#skill-navigation-row-243)",
        1,
    )


ROW242_EPILOGUE_OLD = (
    "Proceed to [row 243](#row-243-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 222 on the full capstone path,"
)
ROW242_EPILOGUE_NEW = (
    "Proceed to [row 243](#row-243-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 242 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 242 closing stitch (Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-242-closing-stitch}"
)

ROW243_INSERT_MARKER = (
    "### Row 222 closing loop (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-242-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 243 skill checkpoint" in preface:
        print("preface: row 243 already present")
    else:
        if "### Row 242 skill checkpoint" not in preface:
            raise SystemExit("row 242 must exist before row 243")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row243_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 243")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "orchestration meta prelude capstone reunion (row 243) |" not in prologue:
        needle = "| Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 242) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 242 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-242"></span>Row 222 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 243")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW242_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW242_EPILOGUE_OLD, ROW242_EPILOGUE_NEW, 1)
    if "{#row-243-closing-loop}" not in epilogue:
        marker = ROW243_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 242 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 243")
    else:
        print("epilogue: row 243 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row223-orchestration-meta-prelude-capstone-reunion-index-row-243" not in sources:
        sources = sources.replace(
            "| 223 | Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone",
            b["sources_table"] + "| 223 | Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 203 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 223) "
            "{#row68-row203-orchestration-meta-prelude-capstone-reunion-index-row-223}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 243")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-243-baby-picture-row68-row223" not in memory:
        memory = memory.replace(
            "| 222 | Meta | [Row 68 → Row 222 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242)",
            b["memory_table"]
            + "| 222 | Meta | [Row 68 → Row 222 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row222-handshake4b-meta-prelude-capstone-reunion-index-row-242)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 243 baby picture {#row-243-baby-picture-row68-row223-orchestration-meta-prelude-capstone-reunion}",
            "### Row 223 baby picture {#row-223-baby-picture-row68-row203-orchestration-meta-prelude-capstone-reunion}",
            "### Row 242 baby picture {#row-242-baby-picture-row68-row222-handshake4b-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 243")


if __name__ == "__main__":
    main()
