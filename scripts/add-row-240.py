#!/usr/bin/env python3
"""Add row 240 meta-stitch (Row 68 → Row 220 ↔ Row 60 Handshake 3 meta prelude capstone reunion, full capstone path)."""
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


def bump220_to_240(text: str) -> str:
    protected = (
        ("row-240-", "__P240__"),
        ("skill-navigation-row-240", "__S240__"),
        ("prologue-preview-row-240", "__PR240__"),
        ("{#row-240-closing-stitch}", "__ST240__"),
        ("{#row-240-closing-loop}", "__LP240__"),
        (
            "row68-row220-handshake3-meta-prelude-capstone-reunion-index-row-240",
            "__IDX240__",
        ),
        (
            "row-240-baby-picture-row68-row220-handshake3-meta-prelude-capstone-reunion",
            "__BABY240__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add220():
    spec = importlib.util.spec_from_file_location("add220", ROOT / "scripts/add-row-220.py")
    add220 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add220)
    return add220


def _build_blocks() -> dict[str, str]:
    b220 = _load_add220()._build_blocks()
    out = {k.replace("row220_preface", "row240_preface"): bump220_to_240(v) for k, v in b220.items()}
    loop = out["epilogue_loop"]
    for spill in ("\n\n\n\n### Row 240 closing loop", "\n\n\n\n### Row 220 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


def _row239_tail() -> str:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    idx = preface.index("When row 239 is complete,")
    end = preface.index(" or extend prose only under `writings/` then sync.", idx)
    return preface[idx:end] + " or extend prose only under `writings/` then sync."


ROW239_TAIL_OLD = _row239_tail()


def _row239_tail_new() -> str:
    return ROW239_TAIL_OLD.replace(
        "proceed to [row 220](preface.md#skill-navigation-row-240)",
        "proceed to [row 240](preface.md#skill-navigation-row-240)",
        1,
    )


ROW239_EPILOGUE_OLD = (
    "Proceed to [row 239](#row-239-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW239_EPILOGUE_NEW = (
    "Proceed to [row 240](#row-240-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 239 on the full capstone path,"
)

ROW239_STITCH_OLD = (
    "before row 240 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW239_STITCH_NEW = (
    "before row 241 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 220 closing stitch (Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-220-closing-stitch}"
)

ROW220_INSERT_MARKER = (
    "### Row 200 closing loop (Row 68 → Row 180 Row 68 → Row 60 "
    "Handshake 3 meta prelude capstone reunion) {#row-200-closing-loop}"
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"
    row239_tail_new = _row239_tail_new()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 240 skill checkpoint" in preface:
        print("preface: row 240 already present")
    else:
        if "### Row 239 skill checkpoint" not in preface:
            raise SystemExit("row 239 must exist before row 240")
        if ROW239_TAIL_OLD in preface:
            preface = preface.replace(ROW239_TAIL_OLD, row239_tail_new, 1)
        elif row239_tail_new in preface:
            print("preface: row 239 tail already updated")
        else:
            raise SystemExit("row 239 tail proceed string not found")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row240_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 240")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 240) |" not in prologue:
        needle = "| Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 220) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 220 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-220"></span>Row 220 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW239_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW239_STITCH_OLD, ROW239_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 240")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW239_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW239_EPILOGUE_OLD, ROW239_EPILOGUE_NEW, 1)
    if "{#row-240-closing-loop}" not in epilogue:
        marker = ROW220_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 200 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 240")
    else:
        if ROW239_EPILOGUE_OLD in epilogue or ROW239_EPILOGUE_NEW in epilogue:
            epilogue_path.write_text(epilogue)
        print("epilogue: row 240 closing loop already present")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row220-handshake3-meta-prelude-capstone-reunion-index-row-240" not in sources.split(
        "| 220 | Row 68 → Row 200", 1
    )[0]:
        pass
    if (
        "| 240 | Row 68 → Row 220 Row 68 → Row 60 Handshake 3 meta prelude capstone"
        not in sources
    ):
        sources = sources.replace(
            "| 220 | Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 220 | Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 200 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 220)"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 240")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-240-baby-picture-row68-row220" not in memory:
        memory = memory.replace(
            "| 220 | Meta | [Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index]",
            b["memory_table"] + "| 220 | Meta | [Row 68 → Row 200 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
        for baby_anchor in (
            "### Row 220 baby picture {#row-220-baby-picture-row68-row200-handshake3-meta-prelude-capstone-reunion}",
            "### Row 200 baby picture (Row 68 → Row 180 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 240")


if __name__ == "__main__":
    main()
