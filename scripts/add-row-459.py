#!/usr/bin/env python3
"""Add row 459 meta-stitch (Row 68 → Row 439 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–450) by delta for meta-stitch copy."""
    out = text

    def in_band(n: int) -> bool:
        return 100 <= n <= 450

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


def bump439_to_459(text: str) -> str:
    protected = (
        ("row-459-", "__P459__"),
        ("skill-navigation-row-459", "__S459__"),
        ("prologue-preview-row-459", "__PR459__"),
        ("{#row-459-closing-stitch}", "__ST459__"),
        ("{#row-459-closing-loop}", "__LP459__"),
        (
            "row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459",
            "__IDX439__",
        ),
        (
            "row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion",
            "__BB439__",
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
    start = preface.index("### Row 439 skill checkpoint")
    end = preface.index("\n## The copper wire through the book", start)
    row459_preface = bump439_to_459(preface[start:end]) + "\n\n"

    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    compass_line = "| Row 68 → Row 419 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 439) |"
    c0 = prologue.index(compass_line)
    c1 = prologue.find("\n", c0)
    prologue_compass = bump439_to_459(prologue[c0 : c1 + 1]).replace(
        "Handshake 3 meta prelude capstone reunion (row 439) |",
        "Handshake 3 meta prelude capstone reunion (row 459) |",
        1,
    )

    stitch_start = "**Row 439 closing stitch (Row 68 → Row 439"
    stitch_end = "\n\n**Row 419 closing stitch"
    prologue_stitch = bump439_to_459(
        prologue[prologue.index(stitch_start) : prologue.index(stitch_end)].replace(
            "{#row-439-closing-stitch}", "{#row-459-closing-stitch}", 1
        ).replace(
            "**Row 439 closing stitch (Row 68 → Row 439",
            "**Row 459 closing stitch (Row 68 → Row 439",
            1,
        )
    )
    if not prologue_stitch.endswith("\n\n"):
        prologue_stitch = prologue_stitch.rstrip() + "\n\n"

    preview_start = '| <span id="prologue-preview-row-439"></span>'
    preview_end = '| <span id="prologue-preview-row-419"></span>'
    prologue_preview = bump439_to_459(
        _slice_between(prologue, preview_start, preview_end).replace(
            "Row 439 preview", "Row 459 preview", 1
        )
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    ep_marker = (
        "### Row 439 closing loop (Row 68 → Row 419 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-439-closing-loop}"
    )
    ep_tail = epilogue.index(ep_marker) + len(ep_marker)
    ep_body = epilogue[ep_tail : epilogue.index("\n\n\n\n\n\n", ep_tail)]
    epilogue_loop = bump439_to_459(ep_marker + ep_body)
    epilogue_loop = epilogue_loop.replace(
        "### Row 459 closing loop (Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-459-closing-loop}",
        "### Row 459 closing loop (Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-459-closing-loop}",
        1,
    ).rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src_header = (
        "## Row 68 → Row 419 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 439) "
        "{#row68-row419-handshake3-meta-prelude-capstone-reunion-index-row-439}"
    )
    src_start = sources.rfind(src_header)
    if src_start < 0:
        raise SystemExit("sources row 439 header not found")
    src_end = (
        "## Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 419) "
        "{#row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419}"
    )
    src_stop = sources.index(src_end, src_start + len(src_header))
    sources_index = bump439_to_459(sources[src_start:src_stop])
    sources_index = sources_index.replace(
        "## Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 459) "
        "{#row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459}",
        "## Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 459) "
        "{#row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459}\n",
        1,
    )

    sources_table = (
        "| 459 | Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion | "
        "[Preface row 459](../preface.md#skill-navigation-row-459) · "
        "[Reunion index](#row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459) · "
        "[Prologue preview](../prologue/00-many-scales.md#prologue-preview-row-459) · "
        "[Closing stitch](../prologue/00-many-scales.md#row-459-closing-stitch) · "
        "[Epilogue loop](../epilogue/multiscale.md#row-459-closing-loop) |\n"
    )

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_anchor = (
        "### Row 439 baby picture {#row-439-baby-picture-row68-row419-handshake3-meta-prelude-capstone-reunion}"
    )
    mem_end = (
        "\n\n### Row 419 baby picture {#row-419-baby-picture-row68-row399-handshake3-meta-prelude-capstone-reunion}"
    )
    memory_baby = bump439_to_459(_slice_between(memory, mem_anchor, mem_end))
    memory_baby = memory_baby.replace(
        "### Row 459 baby picture {#row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion} "
        "{#row-399-baby-picture-row68-row379-handshake3-meta-prelude-capstone-reunion}",
        "### Row 459 baby picture {#row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    memory_table = (
        "| 459 | Meta | [Row 68 → Row 439 Handshake 3 meta prelude capstone reunion index]"
        "(sources.md#row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459) · "
        "[preface row 459 skill checkpoint](../preface.md#skill-navigation-row-459) · "
        "[prologue row 459 preview](../prologue/00-many-scales.md#prologue-preview-row-459) · "
        "[prologue row 459 closing stitch](../prologue/00-many-scales.md#row-459-closing-stitch) · "
        "[epilogue row 459 closing loop](../epilogue/multiscale.md#row-459-closing-loop) | "
        "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified "
        "DFT workflows meta prelude capstone on the full capstone path — read row 68 + row 458 or row 439 "
        "gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[row 459 baby picture](#row-459-baby-picture-row68-row439-handshake3-meta-prelude-capstone-reunion) |\n"
    )

    return {
        "row459_preface": row459_preface,
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
    "before row 439 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 459 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW259_STITCH_OLD = (
    "before row 380 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW259_STITCH_NEW = (
    "before row 400 Handshake 3 meta prelude capstone opens on the full capstone path."
)

ROW239_STITCH_OLD = (
    "before row 440 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW239_STITCH_NEW = (
    "before row 460 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW238_STITCH_OLD = (
    "before row 439 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW238_STITCH_NEW = (
    "before row 459 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW459_EPILOGUE_OLD = (
    "Proceed to [row 439](#row-439-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW459_EPILOGUE_NEW = (
    "Proceed to [row 459](#row-459-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 439 closing stitch (Row 68 → Row 439 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-439-closing-stitch}"
)

ROW459_INSERT_MARKER = (
    "### Row 439 closing loop (Row 68 → Row 419 Row 68 → Row 59 "
    "Handshake 3 meta prelude capstone reunion) {#row-439-closing-loop}"
)


def _insert_row459_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 459 closing loop" in epilogue:
        return epilogue
    if ROW459_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 439 insert anchor not found")
    return epilogue.replace(ROW459_INSERT_MARKER, proper_loop + "\n\n" + ROW459_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 459 skill checkpoint" in preface:
        print("preface: row 459 already present")
    else:
        if "### Row 439 skill checkpoint" not in preface:
            raise SystemExit("row 439 must exist before row 459")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row459_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 459")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 459) |" not in prologue:
        needle = (
            "| Row 68 → Row 419 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 439) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 439 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-439"></span>Row 439 preview'
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
        print("prologue: added row 459")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW459_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW459_EPILOGUE_OLD, ROW459_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row459_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 459")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row439-handshake3-meta-prelude-capstone-reunion-index-row-459" not in sources:
        src439_header = (
            "## Row 68 → Row 419 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 439) "
            "{#row68-row419-handshake3-meta-prelude-capstone-reunion-index-row-439}"
        )
        src439_pos = sources.rfind(src439_header)
        if src439_pos < 0:
            raise SystemExit("sources row 439 insert anchor not found")
        sources = (
            sources[:src439_pos]
            + b["sources_index"]
            + sources[src439_pos:]
        )
        sources_path.write_text(sources)
        print("sources: added row 459")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-459-baby-picture-row68-row439" not in memory:
        meta_anchor = "| 439 | Meta | [Row 68 → Row 419 Handshake 3 meta prelude capstone reunion index]"
        if meta_anchor in memory:
            memory = memory.replace(meta_anchor, b["memory_table"] + meta_anchor, 1)
        baby_anchor = (
            "### Row 439 baby picture {#row-439-baby-picture-row68-row419-handshake3-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory sheet row 439 baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 459")


if __name__ == "__main__":
    main()
