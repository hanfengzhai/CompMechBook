#!/usr/bin/env python3
"""Add row 261 meta-stitch (Row 68 → Row 261 ↔ Row 61 Handshake 4a meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–280) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 280

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


def bump241_to_261(text: str) -> str:
    protected = (
        ("row-261-", "__P260__"),
        ("skill-navigation-row-261", "__S260__"),
        ("prologue-preview-row-261", "__PR260__"),
        ("{#row-261-closing-stitch}", "__ST260__"),
        ("{#row-261-closing-loop}", "__LP260__"),
        (
            "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
            "__IDX260__",
        ),
        (
            "row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion",
            "__BABY260__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add241():
    spec = importlib.util.spec_from_file_location("add241", ROOT / "scripts/add-row-241.py")
    add241 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add241)
    return add241


def _load_add260():
    spec = importlib.util.spec_from_file_location("add260", ROOT / "scripts/add-row-260.py")
    add260 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add260)
    return add260


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 241 skill checkpoint")
    end = preface.index("\n\n### Row 242 skill checkpoint", start)
    row261_preface = bump241_to_261(preface[start:end]) + "\n\n"

    b241 = _load_add241()._build_blocks()
    out = {
        k.replace("row241_preface", "row261_preface"): bump241_to_261(v)
        for k, v in b241.items()
        if k != "row241_preface"
    }
    out["row261_preface"] = row261_preface
    loop = out["epilogue_loop"]
    for spill in ("\n\n\n\n### Row 262 closing loop", "\n\n\n\n### Row 242 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


def _row260_tail() -> str:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    idx = preface.index("When row 260 is complete,")
    end = preface.index(" or extend prose only under `writings/` then sync.", idx)
    return preface[idx:end] + " or extend prose only under `writings/` then sync."


ROW260_TAIL_OLD = _row260_tail()
ROW260_TAIL_NEW = ROW260_TAIL_OLD.replace(
    "proceed to [row 261](preface.md#skill-navigation-row-261)",
    "proceed to [row 262](preface.md#skill-navigation-row-262)",
).replace(
    "to [row 261](preface.md#skill-navigation-row-261) when",
    "to [row 261](preface.md#skill-navigation-row-261) when",
)

ROW260_STITCH_OLD = (
    "before row 261 Handshake 4a meta prelude capstone reunion opens on the full capstone path."
)
ROW260_STITCH_NEW = (
    "before row 262 Handshake 4b meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 260 closing stitch (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-240-closing-stitch}"
)

CAPSTONE_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

CAPSTONE_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)


def _canonical_capstone_loops(b: dict[str, str]) -> tuple[str, str, str, str, str, str, str, str, str]:
    add260 = _load_add260()
    bb = add260._build_blocks()
    l253, l254, l255, l256, l257, l258, l259, l260 = add260._canonical_capstone_loops(bb)
    loop261 = b["epilogue_loop"]
    loop261 = loop261.replace(
        "When row 61 feels like epilogue homework after row 240 alone on the full capstone path",
        "When row 61 feels like epilogue homework after row 260 alone on the full capstone path",
        1,
    ).replace(
        "when row 240 closed Handshake 4a meta prelude capstone on the capstone path",
        "when row 260 closed Handshake 4a meta prelude capstone on the full capstone path",
        1,
    ).replace(
        "Recite [preface row 240](../preface.md#skill-navigation-row-220)",
        "Recite [preface row 260](../preface.md#skill-navigation-row-260)",
        1,
    ).replace(
        "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
        "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
    )
    for spill in ("\n\n\n\n### Row 262 closing loop", "\n\n\n\n### Row 242 closing loop"):
        if spill in loop261:
            loop261 = loop261.split(spill, 1)[0].rstrip() + "\n\n"
            break
    return l253, l254, l255, l256, l257, l258, l259, l260, loop261.rstrip() + "\n\n"


def _rebuild_capstone_mid(
    mid: str,
    l253: str,
    l254: str,
    l255: str,
    l256: str,
    l257: str,
    l258: str,
    l259: str,
    l260: str,
    l261: str,
) -> str:
    marker = "### Row 253 closing loop"
    if marker not in mid:
        raise SystemExit("row 253 closing loop header missing in capstone mid")
    start = mid.index(marker)
    return mid[:start] + l253 + l254 + l255 + l256 + l257 + l258 + l259 + l260 + l261


def _epilogue_has_row261_in_capstone_chain(text: str) -> bool:
    if CAPSTONE_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(CAPSTONE_EPILOGUE_AFTER)
    window = text[idx : idx + 65000]
    return (
        "### Row 261 closing loop" in window
        and "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261" in window
        and "after row 260 alone" in window
    )


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if "### Row 261 skill checkpoint" in before_copper:
        print("preface: row 261 capstone already present")
    else:
        if "### Row 260 skill checkpoint" not in before_copper:
            raise SystemExit("row 260 must exist before row 261")
        if ROW260_TAIL_OLD in preface and ROW260_TAIL_OLD != ROW260_TAIL_NEW:
            preface = preface.replace(ROW260_TAIL_OLD, ROW260_TAIL_NEW, 1)
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row261_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 261")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 4a meta prelude capstone reunion (row 261) |" not in prologue:
        needle = (
            "| Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 260) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 260 not found")
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
        if ROW260_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW260_STITCH_OLD, ROW260_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 261")
    else:
        print("prologue: row 261 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row261_in_capstone_chain(epilogue):
        if CAPSTONE_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if CAPSTONE_EPILOGUE_BEFORE not in epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(CAPSTONE_EPILOGUE_BEFORE, 1)
        loops = _canonical_capstone_loops(b)
        mid = _rebuild_capstone_mid(mid, *loops)
        epilogue = head + CAPSTONE_EPILOGUE_AFTER + mid + CAPSTONE_EPILOGUE_BEFORE + rest
        epilogue_path.write_text(epilogue)
        print("epilogue: rebuilt capstone chain through row 261")
    else:
        print("epilogue: row 261 closing loop already present in capstone chain")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "| 261 | Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone" not in sources:
        sources = sources.replace(
            "| 221 | Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            b["sources_table"] + "| 221 | Row 68 → Row 201 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 221) "
            "{#row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-221}"
        )
        if src_header not in sources:
            src_header = (
                "## Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 221)"
            )
        sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 261")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "| 261 | Meta |" not in memory:
        table_row = b["memory_table"].replace("| 241 | Meta |", "| 261 | Meta |", 1)
        memory = memory.replace(
            "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]",
            table_row + "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]",
            1,
        )
    if "row-261-baby-picture-row68-row241" not in memory:
        for baby_anchor in (
            "### Row 241 baby picture {#row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion}",
            "### Row 221 baby picture {#row-221-baby-picture-row68-row201-handshake4a-meta-prelude-capstone-reunion}",
            "### Row 241 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 261")


if __name__ == "__main__":
    main()
