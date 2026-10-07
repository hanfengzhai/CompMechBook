#!/usr/bin/env python3
"""Add row 232 meta-stitch (Row 68 → Row 212 ↔ Row 52 atomistic meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R209__", "__R210__", "__R211__", "__R212__", "__R229__", "__R230__", "__R231__", "__R232__", "__R233__"):
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


def bump212_to_232(text: str) -> str:
    protected = (
        ("row-232-", "__P232__"),
        ("skill-navigation-row-232", "__S232__"),
        ("prologue-preview-row-232", "__PR232__"),
        ("{#row-232-closing-stitch}", "__ST232__"),
        ("{#row-232-closing-loop}", "__LP232__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add212():
    spec = importlib.util.spec_from_file_location("add212", ROOT / "scripts/add-row-212.py")
    add212 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add212)
    return add212


def _build_blocks() -> dict[str, str]:
    add212 = _load_add212()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 212 skill checkpoint")
    end = preface.index("\n\n### Row 213 skill checkpoint", start)
    row232_preface = bump212_to_232(preface[start:end]) + "\n\n"

    b212 = add212._build_blocks()
    prologue_stitch = bump212_to_232(
        b212["prologue_stitch"]
        .replace("{#row-212-closing-stitch}", "{#row-232-closing-stitch}")
        .replace(
            "**Row 212 closing stitch (Row 68 → Row 192",
            "**Row 232 closing stitch (Row 68 → Row 212",
        )
        .replace(
            "**Row 192 closing stitch (Row 68 → Row 192",
            "**Row 232 closing stitch (Row 68 → Row 212",
        )
    ).replace("**Row 252 closing stitch", "**Row 232 closing stitch", 1)
    prologue_compass = bump212_to_232(b212["prologue_compass"]).replace(
        "atomistic meta prelude capstone reunion (row 212) |",
        "atomistic meta prelude capstone reunion (row 232) |",
        1,
    )
    prologue_preview = bump212_to_232(b212["prologue_preview"]).replace(
        "Row 212 preview", "Row 232 preview", 1
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row212_loop_anchor = (
        "### Row 192 closing loop (Row 68 → Row 192 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion) {#row-212-closing-loop}"
    )
    row213_loop_end = (
        "### Row 193 closing loop (Row 68 → Row 193 Row 68 → Row 53 "
        "dynamics meta prelude capstone reunion) {#row-213-closing-loop}"
    )
    if row212_loop_anchor in epilogue and row213_loop_end in epilogue.split(row212_loop_anchor, 1)[1]:
        ep_slice = row212_loop_anchor + epilogue.split(row212_loop_anchor, 1)[1].split(row213_loop_end, 1)[0]
    else:
        ep_slice = b212["epilogue_loop"]
    epilogue_loop = bump212_to_232(ep_slice)
    epilogue_loop = epilogue_loop.replace("{#row-212-closing-loop}", "{#row-232-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 212 closing loop (Row 68 → Row 212",
        "### Row 232 closing loop (Row 68 → Row 212",
        1,
    ).replace(
        "### Row 232 closing loop (Row 68 → Row 192",
        "### Row 232 closing loop (Row 68 → Row 212",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src212_header = (
        "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212) "
        "{#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212}"
    )
    next172_header = (
        "## Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    )
    if src212_header in sources:
        sources_index = bump212_to_232(sources.split(src212_header, 1)[1].split(next172_header, 1)[0])
    else:
        sources_index = bump212_to_232(b212["sources_index"])
    sources_index = (
        "## Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 232) "
        "{#row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = bump212_to_232(b212["sources_table"])
    sources_table = sources_table.replace("| 212 | Row 68 → Row 192", "| 232 | Row 68 → Row 212", 1)

    memory_table = bump212_to_232(b212["memory_table"])
    memory_table = memory_table.replace("| 212 | Meta |", "| 232 | Meta |", 1)

    memory_baby = bump212_to_232(b212["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 232 baby picture {#row-212-baby-picture",
        "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion} {#row-212-baby-picture",
        1,
    )
    if "{#row-232-baby-picture-row68-row212" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 232 baby picture",
            "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
            1,
        )

    preface231_start = preface.index("### Row 231 skill checkpoint")
    preface231_end = preface.index("\n\n## The copper wire through the book", preface231_start)
    preface231 = preface[preface231_start:preface231_end]
    tail_after_231 = preface231.split("When row 231 is complete", 1)[1]
    tail_src = (
        "When row 231 is complete"
        + tail_after_231.replace("When row 231 is complete", "__W231__")
        .replace("When row 232 is complete", "__W232__")
    )
    bumped_tail = bump212_to_232(tail_src).replace("__W231__", "When row 251 is complete").replace(
        "__W232__", "When row 252 is complete"
    )
    if "When row 252 is complete" in bumped_tail:
        row251_tail_new = "When row 251 is complete" + bumped_tail.split("When row 252 is complete", 1)[1]
    else:
        row251_tail_new = bumped_tail

    return {
        "row232_preface": row232_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
        "row251_tail_new": row251_tail_new,
    }


ROW231_EPILOGUE_OLD = (
    "Proceed to [row 212](#row-212-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 211 on the full capstone path,"
)
ROW231_EPILOGUE_NEW = (
    "Proceed to [row 232](#row-232-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 231 on the full capstone path,"
)

ROW231_BABY_OLD = (
    "when opening [row 232](preface.md#skill-navigation-row-232) before row 52 closes on the full capstone path"
)
ROW231_BABY_NEW = (
    "when opening [row 233](preface.md#skill-navigation-row-233) before row 52 closes on the full capstone path"
)

ROW231_STITCH_OLD = (
    "before row 232 atomistic meta prelude capstone reunion opens on the full capstone path."
)
ROW231_STITCH_NEW = (
    "before row 233 dynamics meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 188 closing stitch (Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-228-closing-stitch}"
)

ROW231_INSERT_MARKER = (
    "### Row 231 closing loop (Row 68 → Row 211 Row 68 → Row 51 "
    "homogenization meta prelude capstone reunion) {#row-231-closing-loop}"
)


def _strip_or_replace_premature_row232(epilogue: str, proper_loop: str) -> str:
    """Replace placeholder Row 232 loop (wrong heading) or insert before row 231 anchor."""
    bad_start = (
        "\n### Row 191 closing loop (Row 68 → Row 191 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-231-closing-loop}"
    )
    if bad_start in epilogue:
        start = epilogue.index(bad_start)
        end = epilogue.index("\n### Row 210 closing loop", start)
        epilogue = epilogue[:start] + epilogue[end:]

    if "### Row 232 closing loop" in epilogue:
        return epilogue

    bad232 = (
        "\n### Row 212 closing loop (Row 68 → Row 212 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion) {#row-232-closing-loop}"
    )
    if bad232 in epilogue:
        start = epilogue.index(bad232)
        end = epilogue.index("\n" + ROW231_INSERT_MARKER, start)
        return epilogue[:start] + "\n\n" + proper_loop.rstrip() + "\n\n" + epilogue[end + 1 :]
    if ROW231_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 231 insert anchor not found")
    return epilogue.replace(ROW231_INSERT_MARKER, proper_loop + "\n\n" + ROW231_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 232 skill checkpoint" in preface:
        print("preface: row 232 already present")
    else:
        if "### Row 231 skill checkpoint" not in preface:
            raise SystemExit("row 231 must exist before row 232")
        if "When row 249 is complete" in preface:
            idx = preface.index("When row 249 is complete")
            end = preface.find("\n\n\n\n", idx)
            if end == -1:
                end = preface.find("\n\n### Row 209", idx)
            if end == -1:
                end = preface.find(copper, idx)
            old_tail = preface[idx:end]
            preface = preface.replace(old_tail, b["row251_tail_new"], 1)
        preface = preface.replace(copper, "\n" + b["row232_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 232")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "atomistic meta prelude capstone reunion (row 232) |" not in prologue:
        needle = "| Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 231) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 231 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-231"></span>Row 231 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-230"></span>Row 230 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW231_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW231_STITCH_OLD, ROW231_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 232")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW231_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW231_EPILOGUE_OLD, ROW231_EPILOGUE_NEW, 1)
    epilogue_new = _strip_or_replace_premature_row232(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 232")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232" not in sources:
        sources = sources.replace(
            "| 212 | Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone",
            b["sources_table"] + "| 212 | Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone",
            1,
        )
        src212_header = (
            "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212) "
            "{#row68-row192-atomistic-meta-prelude-capstone-reunion-index-row-212}"
        )
        sources = sources.replace(
            src212_header,
            b["sources_index"] + src212_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 232")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-232-baby-picture-row68-row212" not in memory:
        memory = memory.replace(
            "| 212 | Meta | [Row 68 → Row 192 atomistic meta prelude capstone reunion index]",
            b["memory_table"] + "| 212 | Meta | [Row 68 → Row 192 atomistic meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 212 baby picture {#row-212-baby-picture-row68-row192-atomistic-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 212 baby picture"
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW231_BABY_OLD in memory:
            memory = memory.replace(ROW231_BABY_OLD, ROW231_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 232")


if __name__ == "__main__":
    main()
