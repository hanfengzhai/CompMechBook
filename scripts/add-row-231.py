#!/usr/bin/env python3
"""Add row 231 meta-stitch (Row 68 → Row 211 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R209__", "__R210__", "__R211__", "__R229__", "__R230__", "__R231__", "__R232__"):
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


def bump211_to_231(text: str) -> str:
    protected = (
        ("row-231-", "__P231__"),
        ("skill-navigation-row-231", "__S231__"),
        ("prologue-preview-row-231", "__PR231__"),
        ("{#row-231-closing-stitch}", "__ST231__"),
        ("{#row-231-closing-loop}", "__LP231__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add211():
    spec = importlib.util.spec_from_file_location("add211", ROOT / "scripts/add-row-211.py")
    add211 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add211)
    return add211


def _build_blocks() -> dict[str, str]:
    add211 = _load_add211()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 211 skill checkpoint")
    end = preface.index("\n\n### Row 212 skill checkpoint", start)
    row231_preface = bump211_to_231(preface[start:end]) + "\n\n"

    b211 = add211._build_blocks()
    prologue_stitch = bump211_to_231(
        b211["prologue_stitch"]
        .replace("{#row-211-closing-stitch}", "{#row-231-closing-stitch}")
        .replace(
            "**Row 211 closing stitch (Row 68 → Row 191",
            "**Row 231 closing stitch (Row 68 → Row 211",
        )
        .replace(
            "**Row 211 closing stitch (Row 68 → Row 211",
            "**Row 231 closing stitch (Row 68 → Row 211",
        )
    )
    prologue_compass = bump211_to_231(b211["prologue_compass"])
    prologue_preview = bump211_to_231(b211["prologue_preview"]).replace(
        "Row 211 preview", "Row 231 preview", 1
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row211_loop_anchor = (
        "### Row 191 closing loop (Row 68 → Row 191 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-211-closing-loop}"
    )
    row212_loop_end = (
        "### Row 192 closing loop (Row 68 → Row 192 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion) {#row-212-closing-loop}"
    )
    if row211_loop_anchor in epilogue and row212_loop_end in epilogue.split(row211_loop_anchor, 1)[1]:
        ep_slice = row211_loop_anchor + epilogue.split(row211_loop_anchor, 1)[1].split(row212_loop_end, 1)[0]
    else:
        ep_slice = b211["epilogue_loop"]
    epilogue_loop = bump211_to_231(ep_slice)
    epilogue_loop = epilogue_loop.replace("{#row-211-closing-loop}", "{#row-231-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 231 closing loop (Row 68 → Row 191",
        "### Row 231 closing loop (Row 68 → Row 211",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src211_header = (
        "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211) "
        "{#row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211}"
    )
    next212_header = (
        "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212)"
    )
    if src211_header in sources:
        sources_index = bump211_to_231(sources.split(src211_header, 1)[1].split(next212_header, 1)[0])
    else:
        sources_index = bump211_to_231(b211["sources_index"])
    sources_index = (
        "## Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 231) "
        "{#row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = bump211_to_231(b211["sources_table"])
    sources_table = sources_table.replace("| 211 | Row 68 → Row 191", "| 231 | Row 68 → Row 211", 1)

    memory_table = bump211_to_231(b211["memory_table"])
    memory_table = memory_table.replace("| 211 | Meta |", "| 231 | Meta |", 1)

    memory_baby = bump211_to_231(b211["memory_baby"]).rstrip() + "\n\n"
    memory_baby = memory_baby.replace(
        "### Row 231 baby picture {#row-131-baby-picture",
        "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion} {#row-131-baby-picture",
        1,
    )
    if "{#row-231-baby-picture-row68-row211" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 231 baby picture",
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
            1,
        )

    preface230_start = preface.index("### Row 230 skill checkpoint")
    preface230_end = preface.index("\n\n## The copper wire through the book", preface230_start)
    preface230 = preface[preface230_start:preface230_end]
    tail_after_230 = preface230.split("When row 230 is complete", 1)[1]
    tail_src = (
        "When row 230 is complete"
        + tail_after_230.replace("When row 230 is complete", "__W230__")
        .replace("When row 231 is complete", "__W231__")
    )
    bumped_tail = bump211_to_231(tail_src).replace("__W230__", "When row 250 is complete").replace(
        "__W231__", "When row 251 is complete"
    )
    row249_tail_new = "When row 249 is complete" + bumped_tail.split("When row 250 is complete", 1)[1]

    return {
        "row231_preface": row231_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
        "row249_tail_new": row249_tail_new,
    }


ROW230_EPILOGUE_OLD = (
    "Proceed to [row 211](#row-211-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 210 on the full capstone path,"
)
ROW230_EPILOGUE_NEW = (
    "Proceed to [row 231](#row-231-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 230 on the full capstone path,"
)

ROW230_BABY_OLD = (
    "when opening [row 231](preface.md#skill-navigation-row-231) before row 51 closes on the full capstone path"
)
ROW230_BABY_NEW = (
    "when opening [row 232](preface.md#skill-navigation-row-232) before row 51 closes on the full capstone path"
)

ROW230_STITCH_OLD = (
    "before row 231 homogenization meta prelude capstone reunion opens on the full capstone path."
)
ROW230_STITCH_NEW = (
    "before row 232 atomistic meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 188 closing stitch (Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-228-closing-stitch}"
)

ROW210_INSERT_MARKER = (
    "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
    "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
)


def _strip_or_replace_premature_row231(epilogue: str, proper_loop: str) -> str:
    """Replace placeholder Row 231 loop (wrong heading) or insert before row 210 anchor."""
    bad_start = (
        "\n### Row 211 closing loop (Row 68 → Row 211 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-231-closing-loop}"
    )
    if bad_start in epilogue:
        start = epilogue.index(bad_start)
        end = epilogue.index("\n" + ROW210_INSERT_MARKER, start)
        return epilogue[:start] + "\n\n" + proper_loop.rstrip() + "\n\n" + epilogue[end + 1 :]
    if "{#row-231-closing-loop}" in epilogue:
        return epilogue
    if ROW210_INSERT_MARKER not in epilogue:
        raise SystemExit("epilogue row 210 insert anchor not found")
    return epilogue.replace(ROW210_INSERT_MARKER, proper_loop + "\n\n" + ROW210_INSERT_MARKER, 1)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 231 skill checkpoint" in preface:
        print("preface: row 231 already present")
    else:
        if "### Row 230 skill checkpoint" not in preface:
            raise SystemExit("row 230 must exist before row 231")
        if "When row 248 is complete" in preface:
            idx = preface.index("When row 248 is complete")
            end = preface.find("\n\n\n\n", idx)
            if end == -1:
                end = preface.find("\n\n### Row 209", idx)
            if end == -1:
                end = preface.find(copper, idx)
            old_tail = preface[idx:end]
            preface = preface.replace(old_tail, b["row249_tail_new"], 1)
        preface = preface.replace(copper, "\n" + b["row231_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 231")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "homogenization meta prelude capstone reunion (row 231) |" not in prologue:
        needle = "| Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion (row 230) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 230 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-230"></span>Row 230 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-229"></span>Row 229 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW230_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW230_STITCH_OLD, ROW230_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 231")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW230_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW230_EPILOGUE_OLD, ROW230_EPILOGUE_NEW, 1)
    epilogue_new = _strip_or_replace_premature_row231(epilogue, b["epilogue_loop"])
    if epilogue_new != epilogue:
        epilogue_path.write_text(epilogue_new)
        print("epilogue: added row 231")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row211-homogenization-meta-prelude-capstone-reunion-index-row-231" not in sources:
        sources = sources.replace(
            "| 211 | Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone",
            b["sources_table"] + "| 211 | Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src211_header := (
                "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211) "
                "{#row68-row191-homogenization-meta-prelude-capstone-reunion-index-row-211}"
            ),
            b["sources_index"] + src211_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 231")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-231-baby-picture-row68-row211" not in memory:
        memory = memory.replace(
            "| 211 | Meta | [Row 68 → Row 191 homogenization meta prelude capstone reunion index]",
            b["memory_table"] + "| 211 | Meta | [Row 68 → Row 191 homogenization meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 211 baby picture {#row-211-baby-picture-row68-row191-homogenization-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = "### Row 211 baby picture"
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        if ROW230_BABY_OLD in memory:
            memory = memory.replace(ROW230_BABY_OLD, ROW230_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 231")


if __name__ == "__main__":
    main()
