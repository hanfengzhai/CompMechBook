#!/usr/bin/env python3
"""Add row 419 meta-stitch (Row 68 → Row 399 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–350) by delta for meta-stitch copy."""
    out = text

    def in_band(n: int) -> bool:
        return 100 <= n <= 410

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


def bump399_to_419(text: str) -> str:
    protected = (
        ("row-419-", "__P419__"),
        ("skill-navigation-row-419", "__S419__"),
        ("prologue-preview-row-419", "__PR419__"),
        ("{#row-419-closing-stitch}", "__ST419__"),
        ("{#row-419-closing-loop}", "__LP419__"),
        (
            "row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419",
            "__IDX399__",
        ),
        (
            "row-419-baby-picture-row68-row399-handshake3-meta-prelude-capstone-reunion",
            "__BB399__",
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
    start = preface.index("### Row 399 skill checkpoint")
    end = preface.index("\n## The copper wire through the book", start)
    row419_preface = bump399_to_419(preface[start:end]) + "\n\n"

    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    compass_line = "| Row 68 → Row 379 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 399) |"
    c0 = prologue.index(compass_line)
    c1 = prologue.find("\n", c0)
    prologue_compass = bump399_to_419(prologue[c0 : c1 + 1]).replace(
        "Handshake 3 meta prelude capstone reunion (row 399) |",
        "Handshake 3 meta prelude capstone reunion (row 419) |",
        1,
    )

    stitch_start = "**Row 399 closing stitch (Row 68 → Row 399"
    stitch_end = "\n\n**Row 237 closing stitch"
    prologue_stitch = bump399_to_419(
        prologue[prologue.index(stitch_start) : prologue.index(stitch_end)].replace(
            "{#row-399-closing-stitch}", "{#row-419-closing-stitch}", 1
        ).replace(
            "**Row 399 closing stitch (Row 68 → Row 399",
            "**Row 419 closing stitch (Row 68 → Row 399",
            1,
        )
    )
    if not prologue_stitch.endswith("\n\n"):
        prologue_stitch = prologue_stitch.rstrip() + "\n\n"

    preview_start = '| <span id="prologue-preview-row-399"></span>'
    preview_end = '| <span id="prologue-preview-row-379"></span>'
    prologue_preview = bump399_to_419(
        _slice_between(prologue, preview_start, preview_end).replace(
            "Row 399 preview", "Row 419 preview", 1
        )
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    ep_marker = (
        "### Row 379 closing loop (Row 68 → Row 379 Row 68 → Row 59 "
        "Handshake 3 meta prelude capstone reunion) {#row-399-closing-loop}"
    )
    ep_tail = epilogue.index(ep_marker) + len(ep_marker)
    ep_body = epilogue[ep_tail : epilogue.index("\n\n\n\n\n\n", ep_tail)]
    epilogue_loop = bump399_to_419(ep_marker + ep_body)
    epilogue_loop = epilogue_loop.replace(
        "### Row 399 closing loop (Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-419-closing-loop}",
        "### Row 419 closing loop (Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) {#row-419-closing-loop}",
        1,
    ).rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src_header = (
        "## Row 68 → Row 379 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 399) "
        "{#row68-row379-handshake3-meta-prelude-capstone-reunion-index-row-399}"
    )
    src_start = sources.rfind(src_header)
    if src_start < 0:
        raise SystemExit("sources row 399 header not found")
    src_end = (
        "## Row 68 → Row 359 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 379) "
        "{#row68-row359-handshake3-meta-prelude-capstone-reunion-index-row-379}"
    )
    src_stop = sources.index(src_end, src_start + len(src_header))
    sources_index = bump399_to_419(sources[src_start:src_stop])
    sources_index = sources_index.replace(
        "## Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 419) "
        "{#row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419}",
        "## Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 419) "
        "{#row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419}\n",
        1,
    )

    sources_table = (
        "| 419 | Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion | "
        "[Preface row 419](../preface.md#skill-navigation-row-419) · "
        "[Reunion index](#row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419) · "
        "[Prologue preview](../prologue/00-many-scales.md#prologue-preview-row-419) · "
        "[Closing stitch](../prologue/00-many-scales.md#row-419-closing-stitch) · "
        "[Epilogue loop](../epilogue/multiscale.md#row-419-closing-loop) |\n"
    )

    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    mem_anchor = (
        "### Row 399 baby picture {#row-399-baby-picture-row68-row379-handshake3-meta-prelude-capstone-reunion} "
        "{#row-339-baby-picture-row68-row319-handshake3-meta-prelude-capstone-reunion}"
    )
    mem_end = "\n\n### Row 379 baby picture {#row-379-baby-picture-row68-row359-handshake3-meta-prelude-capstone-reunion}"
    memory_baby = bump399_to_419(_slice_between(memory, mem_anchor, mem_end))
    memory_baby = memory_baby.replace(
        "### Row 419 baby picture {#row-419-baby-picture-row68-row399-handshake3-meta-prelude-capstone-reunion} "
        "{#row-359-baby-picture-row68-row339-handshake3-meta-prelude-capstone-reunion}",
        "### Row 419 baby picture {#row-419-baby-picture-row68-row399-handshake3-meta-prelude-capstone-reunion}",
        1,
    ).rstrip() + "\n\n"

    memory_table = (
        "| 419 | Meta | [Row 68 → Row 399 Handshake 3 meta prelude capstone reunion index]"
        "(sources.md#row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419) · "
        "[preface row 419 skill checkpoint](../preface.md#skill-navigation-row-419) · "
        "[prologue row 419 preview](../prologue/00-many-scales.md#prologue-preview-row-419) · "
        "[prologue row 419 closing stitch](../prologue/00-many-scales.md#row-419-closing-stitch) · "
        "[epilogue row 419 closing loop](../epilogue/multiscale.md#row-419-closing-loop) | "
        "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified "
        "DFT workflows meta prelude capstone on the full capstone path — read row 68 + row 418 or row 399 "
        "gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[row 419 baby picture](#row-419-baby-picture-row68-row399-handshake3-meta-prelude-capstone-reunion) |\n"
    )

    return {
        "row419_preface": row419_preface,
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
    "before row 419 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 439 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW259_STITCH_OLD = (
    "before row 340 Handshake 3 meta prelude capstone opens on the full capstone path."
)
ROW259_STITCH_NEW = (
    "before row 360 Handshake 3 meta prelude capstone opens on the full capstone path."
)

ROW239_STITCH_OLD = (
    "before row 400 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW239_STITCH_NEW = (
    "before row 420 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW238_STITCH_OLD = (
    "before row 399 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW238_STITCH_NEW = (
    "before row 419 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW419_EPILOGUE_OLD = (
    "Proceed to [row 399](#row-399-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW419_EPILOGUE_NEW = (
    "Proceed to [row 419](#row-419-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 399 closing stitch (Row 68 → Row 399 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-399-closing-stitch}"
)

ROW419_INSERT_MARKER = (
    "### Row 379 closing loop (Row 68 → Row 379 Row 68 → Row 59 "
    "Handshake 3 meta prelude capstone reunion) {#row-399-closing-loop}"
)


def _insert_row419_epilogue(epilogue: str, proper_loop: str) -> str:
    if "### Row 419 closing loop" in epilogue:
        return epilogue
    if ROW419_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 399 insert anchor not found")
    return epilogue.replace(ROW419_INSERT_MARKER, proper_loop + "\n\n" + ROW419_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 419 skill checkpoint" in preface:
        print("preface: row 419 already present")
    else:
        if "### Row 399 skill checkpoint" not in preface:
            raise SystemExit("row 399 must exist before row 419")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row419_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 419")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 419) |" not in prologue:
        needle = (
            "| Row 68 → Row 379 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 399) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 399 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-399"></span>Row 399 preview'
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
        print("prologue: added row 419")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW419_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW419_EPILOGUE_OLD, ROW419_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row419_epilogue(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 419")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row399-handshake3-meta-prelude-capstone-reunion-index-row-419" not in sources:
        src399_header = (
            "## Row 68 → Row 379 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 399) "
            "{#row68-row379-handshake3-meta-prelude-capstone-reunion-index-row-399}"
        )
        src399_pos = sources.rfind(src399_header)
        if src399_pos < 0:
            raise SystemExit("sources row 399 insert anchor not found")
        sources = (
            sources[:src399_pos]
            + b["sources_index"]
            + sources[src399_pos:]
        )
        sources_path.write_text(sources)
        print("sources: added row 419")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-419-baby-picture-row68-row399" not in memory:
        meta_anchor = "| 339 | Meta | [Row 68 → Row 319 Handshake 3 meta prelude capstone reunion index]"
        if meta_anchor in memory:
            memory = memory.replace(meta_anchor, b["memory_table"] + meta_anchor, 1)
        baby_anchor = (
            "### Row 399 baby picture {#row-399-baby-picture-row68-row379-handshake3-meta-prelude-capstone-reunion} "
            "{#row-339-baby-picture-row68-row319-handshake3-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory sheet row 399 baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 419")


if __name__ == "__main__":
    main()
