#!/usr/bin/env python3
"""Add row 259 meta-stitch (Row 68 → Row 239 ↔ Row 59 Handshake 3 meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R239__", "__R240__", "__R258__", "__R259__", "__R260__"):
        out = out.replace(tag, tag)

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


def bump239_to_259(text: str) -> str:
    protected = (
        ("row-259-", "__P259__"),
        ("skill-navigation-row-259", "__S259__"),
        ("prologue-preview-row-259", "__PR259__"),
        ("{#row-259-closing-stitch}", "__ST259__"),
        ("{#row-259-closing-loop}", "__LP259__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add239():
    spec = importlib.util.spec_from_file_location("add239", ROOT / "scripts/add-row-239.py")
    add239 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add239)
    return add239


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 239 skill checkpoint")
    end = preface.index("\n\n### Row 240 skill checkpoint", start)
    row259_preface = bump239_to_259(preface[start:end]) + "\n\n"

    b239 = _load_add239()._build_blocks()
    prologue_stitch = bump239_to_259(
        b239["prologue_stitch"]
        .replace("{#row-239-closing-stitch}", "{#row-259-closing-stitch}")
        .replace(
            "**Row 239 closing stitch (Row 68 → Row 219",
            "**Row 259 closing stitch (Row 68 → Row 239",
        )
        .replace(
            "**Row 199 closing stitch (Row 68 → Row 179",
            "**Row 259 closing stitch (Row 68 → Row 239",
        )
    ).replace("**Row 279 closing stitch", "**Row 259 closing stitch", 1)
    prologue_compass = bump239_to_259(b239["prologue_compass"]).replace(
        "Handshake 3 meta prelude capstone reunion (row 259) |",
        "Handshake 3 meta prelude capstone reunion (row 259) |",
        1,
    )
    prologue_preview = bump239_to_259(b239["prologue_preview"]).replace(
        "Row 239 preview", "Row 259 preview", 1
    )

    epilogue_loop = bump239_to_259(b239["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-239-closing-loop}", "{#row-259-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 239 closing loop (Row 68 → Row 219",
        "### Row 259 closing loop (Row 68 → Row 239",
        1,
    ).replace(
        "### Row 259 closing loop (Row 68 → Row 219",
        "### Row 259 closing loop (Row 68 → Row 239",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 240 closing loop",
        "\n\n\n\n### Row 219 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump239_to_259(b239["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 219 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 239) "
        "{#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219}",
        "## Row 68 → Row 259 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 259) "
        "{#row68-row259-handshake3-meta-prelude-capstone-reunion-index-row-259}",
        1,
    )

    sources_table = bump239_to_259(b239["sources_table"])
    sources_table = re.sub(
        r"^\| 239 \| Row 68 → Row 239",
        "| 259 | Row 68 → Row 239",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 259 | Row 68 → Row 239" not in sources_table:
        sources_table = sources_table.replace(
            "| 239 | Row 68 → Row 219", "| 259 | Row 68 → Row 239", 1
        )

    memory_table = bump239_to_259(b239["memory_table"])
    memory_table = memory_table.replace("| 239 | Meta |", "| 259 | Meta |", 1)

    memory_baby = bump239_to_259(b239["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 259 baby picture {#row-239-baby-picture",
        "### Row 259 baby picture {#row-259-baby-picture-row68-row239-handshake3-meta-prelude-capstone-reunion} {#row-238-baby-picture",
        1,
    )
    if "{#row-259-baby-picture-row68-row239" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 259 baby picture",
            "### Row 259 baby picture {#row-259-baby-picture-row68-row239-handshake3-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row259_preface": row259_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW258_TAIL_OLD = (
    "When row 258 is complete, proceed to [row 259](preface.md#skill-navigation-row-259) when `foundation_export.yaml` exists but Handshake 3 meta prelude capstone still lags after verified DFT workflows meta prelude capstone on the full capstone path, to [row 239](preface.md#skill-navigation-row-239) when `foundation_export.yaml` exists but IX.3 → Handshake 3 still feels disconnected from verified DFT workflows meta prelude capstone on the opening-hinge capstone path alone, to [row 219](preface.md#skill-navigation-row-219) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to [row 258](preface.md#skill-navigation-row-258) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone, to [row 238](preface.md#skill-navigation-row-238) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 79](preface.md#skill-navigation-row-79) for the Row 68 ↔ Row 59 prelude audit alone, to [row 257](preface.md#skill-navigation-row-257) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
)
ROW258_TAIL_NEW = ROW258_TAIL_OLD

ROW258_EPILOGUE_OLD = (
    "Proceed to [row 239](#row-239-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 238 on the full capstone path,"
)
ROW258_EPILOGUE_NEW = (
    "Proceed to [row 259](#row-259-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 258 on the full capstone path,"
)

ROW258_STITCH_OLD = (
    "before row 259 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)
ROW258_STITCH_NEW = (
    "before row 260 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 258 closing stitch (Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-258-closing-stitch}"
)

ROW258_INSERT_MARKER = (
    "### Row 238 closing loop (Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) "
    "{#row-258-closing-loop}"
)


def _insert_row259_epilogue(epilogue: str, proper_loop: str) -> str:
    if epilogue.count("{#row-259-closing-loop}") >= 1 and proper_loop.strip() in epilogue:
        return epilogue
    if ROW258_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 258 insert anchor not found")
    if "{#row-259-closing-loop}" in epilogue:
        return epilogue
    return epilogue.replace(ROW258_INSERT_MARKER, proper_loop + "\n\n" + ROW258_INSERT_MARKER, 1)


def _remove_orphan_row259_loops(epilogue: str) -> str:
    """Drop duplicate row-259 closing loops after the dynamics band (second occurrence onward)."""
    marker = "{#row-259-closing-loop}"
    first = epilogue.find(marker)
    if first == -1:
        return epilogue
    second = epilogue.find(marker, first + len(marker))
    if second == -1:
        return epilogue
    # Remove from second ### Row heading through end of that subsection (before next ### at same level)
    start = epilogue.rfind("\n\n### ", 0, second)
    if start == -1:
        start = second - 4
    nxt = epilogue.find("\n\n\n\n\n\n", second)
    if nxt == -1:
        nxt = epilogue.find("\n\n### Row ", second + 10)
    if nxt == -1:
        return epilogue
    return epilogue[:start] + epilogue[nxt:]


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 259 skill checkpoint" in preface and preface.index("### Row 259 skill checkpoint") < preface.index(copper):
        print("preface: row 259 already present")
    else:
        if "### Row 258 skill checkpoint" not in preface:
            raise SystemExit("row 258 must exist before row 259")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        # Remove broken partial row 259 if inserted after copper wire only
        if preface.index(copper) < preface.find("### Row 259 skill checkpoint", preface.find("### Row 258 skill checkpoint")):
            pass
        preface = preface.replace(copper, "\n" + b["row259_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 259")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "Handshake 3 meta prelude capstone reunion (row 259) |" not in prologue:
        needle = "| Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 258) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 258 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch_anchor = "**Row 258 closing stitch (Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-258-closing-stitch}"
        if stitch_anchor not in prologue:
            stitch_anchor = "**Row 258 closing stitch (Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-238-closing-stitch}"
        if stitch_anchor in prologue:
            prologue = prologue.replace(
                stitch_anchor,
                b["prologue_stitch"] + stitch_anchor.replace("{#row-238-closing-stitch}", "{#row-258-closing-stitch}"),
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-258"></span>Row 258 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW258_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW258_STITCH_OLD, ROW258_STITCH_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 259")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW258_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW258_EPILOGUE_OLD, ROW258_EPILOGUE_NEW, 1)
    epilogue_new = _insert_row259_epilogue(epilogue, b["epilogue_loop"])
    epilogue_new = _remove_orphan_row259_loops(epilogue_new)
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: updated row 259")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row259-handshake3-meta-prelude-capstone-reunion-index-row-259" not in sources:
        sources = sources.replace(
            "| 219 | Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            b["sources_table"] + "| 219 | Row 68 → Row 199 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 219 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 239) "
            "{#row68-row199-handshake3-meta-prelude-capstone-reunion-index-row-219}"
        )
        if src_header not in sources:
            src_header = (
                "## Row 68 → Row 219 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 239)"
            )
        sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 259")
    else:
        # Fix header id if only partial insert exists
        sources = sources.replace(
            "{#row68-row239-handshake3-meta-prelude-capstone-reunion-index-row-259}",
            "{#row68-row259-handshake3-meta-prelude-capstone-reunion-index-row-259}",
        )
        sources_path.write_text(sources)

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-259-baby-picture-row68-row239" not in memory:
        memory = memory.replace(
            "| 258 | Meta | [Row 68 → Row 238 DFT workflows meta prelude capstone reunion index]",
            b["memory_table"] + "| 258 | Meta | [Row 68 → Row 238 DFT workflows meta prelude capstone reunion index]",
            1,
        )
        for baby_anchor in (
            "### Row 239 baby picture {#row-239-baby-picture-row68-row219-handshake3-meta-prelude-capstone-reunion}",
            "### Row 239 baby picture",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                break
        else:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 259")


if __name__ == "__main__":
    main()
