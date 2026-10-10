#!/usr/bin/env python3
"""Add row 258 meta-stitch (Row 68 → Row 258 ↔ Row 58 DFT workflows meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–280) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R238__", "__R239__", "__R257__", "__R258__", "__R259__"):
        out = out.replace(tag, tag)

    def in_band(n: int) -> bool:
        return 100 <= n <= 280

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


def bump238_to_258(text: str) -> str:
    protected = (
        ("row-258-", "__P258__"),
        ("skill-navigation-row-258", "__S258__"),
        ("prologue-preview-row-258", "__PR258__"),
        ("{#row-258-closing-stitch}", "__ST258__"),
        ("{#row-258-closing-loop}", "__LP258__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add238():
    spec = importlib.util.spec_from_file_location("add238", ROOT / "scripts/add-row-238.py")
    add238 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add238)
    return add238


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 238 skill checkpoint")
    end = preface.index("\n\n### Row 239 skill checkpoint", start)
    row258_preface = bump238_to_258(preface[start:end]) + "\n\n"
    row258_preface = (
        row258_preface.replace("when row 237 closed", "when row 257 closed", 1)
        .replace("after row 237 on the full capstone path", "after row 257 on the full capstone path", 1)
        .replace("after row 237.", "after row 257.", 1)
    )

    b238 = _load_add238()._build_blocks()
    prologue_stitch = bump238_to_258(
        b238["prologue_stitch"]
        .replace("{#row-238-closing-stitch}", "{#row-258-closing-stitch}")
        .replace(
            "**Row 238 closing stitch (Row 68 → Row 218",
            "**Row 258 closing stitch (Row 68 → Row 238",
        )
        .replace(
            "**Row 218 closing stitch (Row 68 → Row 198",
            "**Row 258 closing stitch (Row 68 → Row 238",
        )
    ).replace("**Row 258 closing stitch", "**Row 258 closing stitch", 1)
    prologue_compass = bump238_to_258(b238["prologue_compass"]).replace(
        "DFT workflows meta prelude capstone reunion (row 238) |",
        "DFT workflows meta prelude capstone reunion (row 258) |",
        1,
    )
    prologue_preview = bump238_to_258(b238["prologue_preview"]).replace(
        "Row 238 preview", "Row 258 preview", 1
    )

    epilogue_loop = bump238_to_258(b238["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace(
        "### Row 238 closing loop (Row 68 → Row 218",
        "### Row 258 closing loop (Row 68 → Row 238",
        1,
    ).replace(
        "### Row 258 closing loop (Row 68 → Row 218",
        "### Row 258 closing loop (Row 68 → Row 238",
        1,
    ).replace(
        "### Row 238 closing loop (Row 68 → Row 238",
        "### Row 258 closing loop (Row 68 → Row 238",
        1,
    )
    for spill in (
        "\n\n\n\n### Row 259 closing loop",
        "\n\n\n\n### Row 239 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources_index = bump238_to_258(b238["sources_index"])
    sources_index = sources_index.replace(
        "## Row 68 → Row 218 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 238) "
        "{#row68-row218-dft-workflows-meta-prelude-capstone-reunion-index-row-238}",
        "## Row 68 → Row 258 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 258) "
        "{#row68-row238-dft-workflows-meta-prelude-capstone-reunion-index-row-258}",
        1,
    )

    sources_table = bump238_to_258(b238["sources_table"])
    sources_table = re.sub(
        r"^\| 238 \| Row 68 → Row 258",
        "| 258 | Row 68 → Row 258",
        sources_table,
        count=1,
        flags=re.MULTILINE,
    )
    if "| 258 | Row 68 → Row 258" not in sources_table:
        sources_table = sources_table.replace(
            "| 238 | Row 68 → Row 218", "| 258 | Row 68 → Row 258", 1
        )

    memory_table = bump238_to_258(b238["memory_table"])
    memory_table = memory_table.replace("| 238 | Meta |", "| 258 | Meta |", 1)

    memory_baby = bump238_to_258(b238["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 258 baby picture {#row-238-baby-picture",
        "### Row 258 baby picture {#row-258-baby-picture-row68-row238-dft-workflows-meta-prelude-capstone-reunion} {#row-238-baby-picture",
        1,
    )
    if "{#row-258-baby-picture-row68-row238" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 258 baby picture",
            "### Row 258 baby picture {#row-258-baby-picture-row68-row238-dft-workflows-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row258_preface": row258_preface,
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
    "before row 258 DFT workflows meta prelude capstone reunion opens on the full capstone path."
)
ROW257_STITCH_NEW = (
    "before row 259 Handshake 3 meta prelude capstone reunion opens on the full capstone path."
)

ROW257_LOOP_PROCEED_OLD = (
    "Proceed to [row 238](#row-238-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 237 on the full capstone path,"
)
ROW257_LOOP_PROCEED_NEW = (
    "Proceed to [row 258](#row-258-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 257 on the full capstone path,"
)

ROW257_BABY_OLD = (
    "when opening [row 198](preface.md#skill-navigation-row-198) before row 58 closes on the full capstone path"
)
ROW257_BABY_NEW = (
    "when opening [row 258](preface.md#skill-navigation-row-258) before row 59 closes on the full capstone path"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 257 closing stitch (Row 68 → Row 257 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-257-closing-stitch}"
)

CAPSTONE_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

CAPSTONE_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)


def _load_add257():
    spec = importlib.util.spec_from_file_location("add257", ROOT / "scripts/add-row-257.py")
    add257 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add257)
    return add257


def _canonical_capstone_loops(b: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    add257 = _load_add257()
    bb = add257._build_blocks()
    l253, l254, l255, l256, l257 = add257._canonical_capstone_loops(bb)
    l257 = l257.replace(ROW257_LOOP_PROCEED_OLD, ROW257_LOOP_PROCEED_NEW, 1)
    loop258 = b["epilogue_loop"]
    loop258 = loop258.replace(
        "When row 58 feels like DFT coursework after row 237 alone,",
        "When row 58 feels like DFT coursework after row 257 alone,",
        1,
    ).replace(
        "when row 237 closed Kohn–Sham meta prelude capstone",
        "when row 257 closed Kohn–Sham meta prelude capstone",
        1,
    ).replace(
        "Kohn–Sham meta prelude capstone closure (row 237)",
        "Kohn–Sham meta prelude capstone closure (row 257)",
        1,
    ).replace(
        "Recite [preface row 217](../preface.md#skill-navigation-row-217)",
        "Recite [preface row 257](../preface.md#skill-navigation-row-257)",
        1,
    )
    for spill in ("\n\n\n\n### Row 259 closing loop", "\n\n\n\n### Row 239 closing loop"):
        if spill in loop258:
            loop258 = loop258.split(spill, 1)[0].rstrip() + "\n\n"
            break
    return l253, l254, l255, l256, l257, loop258.rstrip() + "\n\n"


def _rebuild_capstone_mid(
    mid: str, l253: str, l254: str, l255: str, l256: str, l257: str, l258: str
) -> str:
    marker = "### Row 253 closing loop"
    if marker not in mid:
        raise SystemExit("row 253 closing loop header missing in capstone mid")
    start = mid.index(marker)
    return mid[:start] + l253 + l254 + l255 + l256 + l257 + l258


def _epilogue_has_row258_in_capstone_chain(text: str) -> bool:
    if CAPSTONE_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(CAPSTONE_EPILOGUE_AFTER)
    window = text[idx : idx + 60000]
    return (
        "{#row-258-closing-loop}" in window
        and "### Row 258 closing loop (Row 68 → Row 238" in window
        and "after row 257 alone" in window
    )


def _strip_orphan_row258_loops(epilogue: str) -> str:
    """Remove duplicate row-258 loops pasted outside the capstone chain."""
    orphan_header = (
        "### Row 238 closing loop (Row 68 → Row 238 Row 68 → Row 58 "
        "DFT workflows meta prelude capstone reunion) {#row-258-closing-loop}"
    )
    while orphan_header in epilogue:
        idx = epilogue.index(orphan_header)
        if CAPSTONE_EPILOGUE_AFTER in epilogue[:idx]:
            cap_idx = epilogue.index(CAPSTONE_EPILOGUE_AFTER)
            cap_end = epilogue.index(CAPSTONE_EPILOGUE_BEFORE, cap_idx)
            if cap_idx < idx < cap_end:
                break
        next_h = epilogue.find("\n\n### Row ", idx + 10)
        if next_h == -1:
            epilogue = epilogue[:idx]
        else:
            epilogue = epilogue[:idx] + epilogue[next_h + 2 :]
    return epilogue


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if "### Row 258 skill checkpoint" in before_copper:
        print("preface: row 258 capstone already present")
    else:
        if "### Row 257 skill checkpoint" not in before_copper:
            raise SystemExit("row 257 must exist before row 258")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row258_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 258")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue_changed = False
    if "DFT workflows meta prelude capstone reunion (row 258) |" not in prologue:
        needle = (
            "| Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 257) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 257 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue_changed = True
    if "**Row 258 closing stitch" not in prologue and PROLOGUE_STITCH_ANCHOR in prologue:
        prologue = prologue.replace(
            PROLOGUE_STITCH_ANCHOR,
            b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
            1,
        )
        prologue_changed = True
    if '<span id="prologue-preview-row-258">' not in prologue:
        preview_anchor = '| <span id="prologue-preview-row-257"></span>Row 257 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-237"></span>Row 237 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_changed = True
    if ROW257_STITCH_OLD in prologue:
        prologue = prologue.replace(ROW257_STITCH_OLD, ROW257_STITCH_NEW)
        prologue_changed = True
    if prologue_changed:
        prologue_path.write_text(prologue)
        print("prologue: added row 258")
    else:
        print("prologue: row 258 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row258_loops(epilogue)
    force_rebuild = not _epilogue_has_row258_in_capstone_chain(epilogue)
    if force_rebuild:
        if CAPSTONE_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if CAPSTONE_EPILOGUE_BEFORE not in epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(CAPSTONE_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(CAPSTONE_EPILOGUE_BEFORE, 1)
        l253, l254, l255, l256, l257, l258 = _canonical_capstone_loops(b)
        mid = _rebuild_capstone_mid(mid, l253, l254, l255, l256, l257, l258)
        epilogue = head + CAPSTONE_EPILOGUE_AFTER + mid + CAPSTONE_EPILOGUE_BEFORE + rest
        epilogue_path.write_text(epilogue)
        print("epilogue: rebuilt capstone chain through row 258")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 258 closing loop already present in capstone chain")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row238-dft-workflows-meta-prelude-capstone-reunion-index-row-258" not in sources:
        sources = sources.replace(
            "| 218 | Row 68 → Row 198 Row 68 → Row 58 DFT workflows meta prelude capstone",
            b["sources_table"] + "| 218 | Row 68 → Row 198 Row 68 → Row 58 DFT workflows meta prelude capstone",
            1,
        )
        src218_header = (
            "## Row 68 → Row 198 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 218) "
            "{#row68-row198-dft-workflows-meta-prelude-capstone-reunion-index-row-218}"
        )
        if src218_header not in sources:
            src218_header = (
                "## Row 68 → Row 198 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 218)"
            )
        sources = sources.replace(
            src218_header,
            b["sources_index"] + src218_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 258")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    memory_changed = False
    if "| 258 | Meta |" not in memory:
        if "| 257 | Meta |" in memory and "| 258 | Meta |" not in memory:
            anchor = "| 257 | Meta | [Row 68 → Row 237 Kohn–Sham meta prelude capstone reunion index](sources.md#row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257)"
            if anchor in memory:
                memory = memory.replace(
                    anchor,
                    anchor
                    + " · [preface row 257 skill checkpoint](../preface.md#skill-navigation-row-257) · [prologue row 257 preview](../prologue/00-many-scales.md#prologue-preview-row-257) · [prologue row 257 closing stitch](../prologue/00-many-scales.md#row-257-closing-stitch) · [epilogue row 257 closing loop](../epilogue/multiscale.md#row-257-closing-loop) | Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path — read row 68 + row 256 or row 237 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; [row 237 baby picture](#row-257-baby-picture-row68-row237-kohn-sham-meta-prelude-capstone-reunion) |\n"
                    + b["memory_table"].strip(),
                    1,
                )
            else:
                memory = memory.replace(
                    "| 257 | Meta | [Row 68 → Row 237 Kohn–Sham meta prelude capstone reunion index]",
                    "| 257 | Meta | [Row 68 → Row 237 Kohn–Sham meta prelude capstone reunion index]"
                    + "\n"
                    + b["memory_table"].strip(),
                    1,
                )
        else:
            memory = memory.replace(
                "| 218 | Meta | [Row 68 → Row 198 DFT workflows meta prelude capstone reunion index]",
                b["memory_table"] + "| 218 | Meta | [Row 68 → Row 198 DFT workflows meta prelude capstone reunion index]",
                1,
            )
        memory_changed = True
    if "row-258-baby-picture-row68-row238" not in memory:
        baby_anchor = (
            "### Row 238 baby picture {#row-218-baby-picture-row68-row218-dft-workflows-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 238 baby picture"
        if baby_anchor in memory:
            memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
            memory_changed = True
    if ROW257_BABY_OLD in memory:
        memory = memory.replace(ROW257_BABY_OLD, ROW257_BABY_NEW)
        memory_changed = True
    if memory_changed:
        memory_path.write_text(memory)
        print("memory-sheet: added row 258")


if __name__ == "__main__":
    main()
