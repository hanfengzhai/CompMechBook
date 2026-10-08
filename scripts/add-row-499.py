#!/usr/bin/env python3
"""Add row 499 meta-stitch (Row 68 → Row 459 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–490) by delta for meta-stitch copy."""
    out = text

    def in_band(n: int) -> bool:
        return 100 <= n <= 490

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


def bump479_to_499(text: str) -> str:
    protected = (
        ("row-499-", "__P499__"),
        ("skill-navigation-row-499", "__S499__"),
        ("prologue-preview-row-499", "__PR499__"),
        ("{#row-499-closing-stitch}", "__ST499__"),
        ("{#row-499-closing-loop}", "__LP499__"),
        (
            "row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499",
            "__IDX499__",
        ),
        (
            "row-499-baby-picture-row68-row479-handshake3-meta-prelude-capstone-reunion",
            "__BB499__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _slice_between(text: str, start: str, end: str) -> str:
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i:j]


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 479 skill checkpoint")
    end = preface.index("\n## The copper wire through the book", start)
    row499_preface = bump479_to_499(preface[start:end]) + "\n\n"

    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    compass_line = "| Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 479) |"
    c0 = prologue.index(compass_line)
    c1 = prologue.find("\n", c0)
    prologue_compass = bump479_to_499(prologue[c0 : c1 + 1]).replace(
        "Handshake 3 meta prelude capstone reunion (row 479) |",
        "Handshake 3 meta prelude capstone reunion (row 499) |",
        1,
    )

    stitch_start = "**Row 479 closing stitch (Row 68 → Row 479"
    stitch_end = "\n\n**Row 439 closing stitch"
    prologue_stitch = bump479_to_499(
        prologue[prologue.index(stitch_start) : prologue.index(stitch_end)].replace(
            "{#row-479-closing-stitch}", "{#row-479-closing-stitch}", 1
        ).replace(
            "**Row 479 closing stitch (Row 68 → Row 479",
            "**Row 479 closing stitch (Row 68 → Row 459",
            1,
        )
    )
    if not prologue_stitch.endswith("\n\n"):
        prologue_stitch = prologue_stitch.rstrip() + "\n\n"

    preview_start = '| <span id="prologue-preview-row-479"></span>'
    preview_end = '| <span id="prologue-preview-row-459"></span>'
    prologue_preview = bump479_to_499(
        _slice_between(prologue, preview_start, preview_end).replace(
            "Row 499 preview", "Row 499 preview", 1
        )
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    ep_marker = (
        "### Row 479 closing loop (Row 68 → Row 459 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-479-closing-loop}"
    )
    ep_tail = epilogue.index(ep_marker) + len(ep_marker)
    ep_body = epilogue[ep_tail : epilogue.index("\n\n\n\n\n\n", ep_tail)]
    epilogue_loop = bump479_to_499(ep_marker + ep_body)
    epilogue_loop = epilogue_loop.replace(
        "### Row 499 closing loop (Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-499-closing-loop}",
        "### Row 499 closing loop (Row 68 → Row 479 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-499-closing-loop}",
        1,
    ).rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src_header = (
        "## Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 479) "
        "{#row68-row459-handshake3-meta-prelude-capstone-reunion-index-row-479}"
    )
    src_start = sources.rfind(src_header)
    if src_start < 0:
        raise SystemExit("sources row 459 header not found")
    src_end = (
        "## Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 459) "
        "{#row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459}"
    )
    src_stop = sources.index(src_end, src_start + len(src_header))
    sources_index = bump479_to_499(sources[src_start:src_stop])
    sources_index = sources_index.replace(
        "## Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 479) "
        "{#row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499}",
        "## Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 479) "
        "{#row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499}\n",
        1,
    )

    sources_table = (
        "| 499 | Row 68 → Row 479 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion | "
        "[Preface row 459](../preface.md#skill-navigation-row-499) · "
        "[Reunion index](#row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499) · "
        "[Prologue preview](../prologue/00-many-scales.md#prologue-preview-row-479) · "
        "[Closing stitch](../prologue/00-many-scales.md#row-479-closing-stitch) · "
        "[Epilogue loop](../epilogue/multiscale.md#row-479-closing-loop) |\n"
    )

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_anchor = (
        "### Row 479 baby picture {#row-479-baby-picture-row68-row459-handshake3-meta-prelude-capstone-reunion}"
    )
    mem_end = (
        "\n\n### Row 459 baby picture {#row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion}"
    )
    memory_baby = bump479_to_499(_slice_between(memory, mem_anchor, mem_end))
    memory_baby = memory_baby.replace(
        "### Row 479 baby picture {#row-499-baby-picture-row68-row479-handshake3-meta-prelude-capstone-reunion} "
        "{#row-399-baby-picture-row68-row379-handshake3-meta-prelude-capstone-reunion}",
        "### Row 479 baby picture {#row-499-baby-picture-row68-row479-handshake3-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    memory_table = (
        "| 499 | Meta | [Row 68 → Row 479 Handshake 3 meta prelude capstone reunion index]"
        "(sources.md#row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499) · "
        "[preface row 499 skill checkpoint](../preface.md#skill-navigation-row-499) · "
        "[prologue row 499 preview](../prologue/00-many-scales.md#prologue-preview-row-479) · "
        "[prologue row 499 closing stitch](../prologue/00-many-scales.md#row-479-closing-stitch) · "
        "[epilogue row 499 closing loop](../epilogue/multiscale.md#row-479-closing-loop) | "
        "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified "
        "DFT workflows meta prelude capstone on the full capstone path — read row 68 + row 478 or row 459 "
        "gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[row 499 baby picture](#row-479-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion) |\n"
    )

    return {
        "row499_preface": row499_preface,
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
    "before row 479 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 499 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW259_STITCH_OLD = (
    "before row 460 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW259_STITCH_NEW = (
    "before row 480 Handshake 3 meta prelude capstone opens on the full capstone path."
)

ROW239_STITCH_OLD = (
    "before row 480 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW239_STITCH_NEW = (
    "before row 500 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW238_STITCH_OLD = (
    "before row 479 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW238_STITCH_NEW = (
    "before row 499 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW499_EPILOGUE_OLD = (
    "Proceed to [row 459](#row-459-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW499_EPILOGUE_NEW = (
    "Proceed to [row 479](#row-479-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 479 closing stitch (Row 68 → Row 479 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-479-closing-stitch}"
)

ROW499_INSERT_MARKER = (
    "### Row 479 closing loop (Row 68 → Row 459 Row 68 → Row 59 "
    "Handshake 3 meta prelude capstone reunion) {#row-479-closing-loop}"
)


def _insert_row499_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 499 closing loop" in epilogue:
        return epilogue
    if ROW499_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 459 insert anchor not found")
    return epilogue.replace(ROW499_INSERT_MARKER, proper_loop + "\n\n" + ROW499_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 499 skill checkpoint" in preface:
        print("preface: row 499 already present")
    else:
        if "### Row 479 skill checkpoint" not in preface:
            raise SystemExit("row 459 must exist before row 479")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row499_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 499")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 499) |" not in prologue:
        needle = (
            "| Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 479) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 459 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "Row 499 closing stitch" not in prologue and PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-479"></span>Row 479 preview'
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
        print("prologue: added row 499")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW499_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW499_EPILOGUE_OLD, ROW499_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row499_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 499")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row479-handshake3-meta-prelude-capstone-reunion-index-row-499" not in sources:
        src479_header = (
            "## Row 68 → Row 459 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 479) "
            "{#row68-row459-handshake3-meta-prelude-capstone-reunion-index-row-479}"
        )
        src479_pos = sources.rfind(src479_header)
        if src479_pos < 0:
            raise SystemExit("sources row 479 insert anchor not found")
        sources = (
            sources[:src479_pos]
            + b["sources_index"]
            + sources[src479_pos:]
        )
        sources_path.write_text(sources)
        print("sources: added row 499")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-499-baby-picture-row68-row479" not in memory:
        meta_anchor = "| 479 | Meta | [Row 68 → Row 459 Handshake 3 meta prelude capstone reunion index]"
        if meta_anchor in memory:
            memory = memory.replace(meta_anchor, b["memory_table"] + meta_anchor, 1)
        baby_anchor = (
            "### Row 459 baby picture {#row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory sheet row 499 baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 499")


if __name__ == "__main__":
    main()
