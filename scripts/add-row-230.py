#!/usr/bin/env python3
"""Add row 230 meta-stitch (Row 68 → Row 210 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""
    out = text
    for tag in ("__R209__", "__R210__", "__R229__", "__R230__", "__R231__"):
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


def bump210_to_230(text: str) -> str:
    protected = (
        ("row-230-", "__P230__"),
        ("skill-navigation-row-230", "__S230__"),
        ("prologue-preview-row-230", "__PR230__"),
        ("{#row-230-closing-stitch}", "__ST230__"),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add210():
    spec = importlib.util.spec_from_file_location("add210", ROOT / "scripts/add-row-210.py")
    add210 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add210)
    return add210


def _load_add190():
    spec = importlib.util.spec_from_file_location("add190", ROOT / "scripts/add-row-190.py")
    add190 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add190)
    return add190


def _build_blocks() -> dict[str, str]:
    add210 = _load_add210()
    add190 = _load_add190()
    t190_to_210 = add210.t190_to_210
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 210 skill checkpoint")
    end = preface.index("\n\n### Row 211 skill checkpoint", start)
    row230_preface = bump210_to_230(preface[start:end]) + "\n\n"

    b210 = add210._build_blocks()
    prologue_stitch = bump210_to_230(
        t190_to_210(add190.PROLOGUE_STITCH.strip())
        .replace("{#row-210-closing-stitch}", "{#row-230-closing-stitch}")
        .replace(
            "**Row 210 closing stitch (Row 68 → Row 190",
            "**Row 230 closing stitch (Row 68 → Row 210",
        )
    ) + "\n\n"
    prologue_compass = bump210_to_230(t190_to_210(add190.PROLOGUE_COMPASS)).replace(
        "(row 210) |", "(row 230) |"
    ).replace(
        "[Preface: row 210 skill checkpoint]", "[Preface: row 230 skill checkpoint]"
    )
    prologue_preview = bump210_to_230(t190_to_210(add190.PROLOGUE_PREVIEW)).replace(
        "Row 210 preview", "Row 230 preview", 1
    )

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row210_loop_anchor = (
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
    )
    row211_loop_end = (
        "### Row 211 closing loop (Row 68 → Row 191 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion) {#row-211-closing-loop}"
    )
    if row210_loop_anchor in epilogue and row211_loop_end in epilogue.split(row210_loop_anchor, 1)[1]:
        ep_slice = row210_loop_anchor + epilogue.split(row210_loop_anchor, 1)[1].split(row211_loop_end, 1)[0]
    else:
        ep_slice = b210["epilogue_loop"]
    epilogue_loop = bump210_to_230(ep_slice)
    epilogue_loop = epilogue_loop.replace("{#row-210-closing-loop}", "{#row-230-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 230 closing loop (Row 68 → Row 190",
        "### Row 230 closing loop (Row 68 → Row 210",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src210_header = (
        "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210) "
        "{#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210}"
    )
    next211_header = (
        "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211)"
    )
    if src210_header in sources:
        sources_index = bump210_to_230(sources.split(src210_header, 1)[1].split(next211_header, 1)[0])
    else:
        sources_index = bump210_to_230(b210["sources_index"])
    sources_index = (
        "## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230) "
        "{#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = bump210_to_230(b210["sources_table"])
    sources_table = sources_table.replace("| 210 | Row 68 → Row 190", "| 230 | Row 68 → Row 210", 1)

    memory_table = (
        "| 230 | Meta | [Row 68 → Row 210 DDD meta prelude capstone reunion index](sources.md#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230) · "
        "[preface row 230 skill checkpoint](../preface.md#skill-navigation-row-230) · "
        "[prologue row 230 preview](../prologue/00-many-scales.md#prologue-preview-row-230) · "
        "[prologue row 230 closing stitch](../prologue/00-many-scales.md#row-230-closing-stitch) · "
        "[epilogue row 230 closing loop](../epilogue/multiscale.md#row-230-closing-loop) | "
        "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified taxonomy meta prelude capstone on the full capstone path — "
        "read row 68 + row 229 or row 209 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
        "[row 230 baby picture](#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion) |\n"
    )
    memory_baby = (
        "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}\n\n"
        "**Row 230 baby picture:** when row 68 closed the midpoint prelude and row 229 or row 209 closed taxonomy meta prelude capstone / DDD meta prelude but "
        "**row 50's VII.1 → VII.2 audit or the Bridge → Peach–Köhler chain still feel like separate checklists on the full capstone path**, open the "
        "[Row 68 → Row 210 DDD meta prelude capstone reunion index](sources.md#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230) — "
        "read [preface row 68](../preface.md#skill-navigation-row-68) gate → "
        "[preface row 229](../preface.md#skill-navigation-row-229) or [preface row 209](../preface.md#skill-navigation-row-209) taxonomy meta prelude capstone / DDD meta prelude gate → "
        "[VII.1 Bridge](../part07-defects/01-defect-taxonomy.md#bridge) through "
        "[VII.2 opening hinge from VII.1](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii1-to-vii2) aloud → "
        "[preface row 50](../preface.md#skill-navigation-row-50) five-step audit → confirm slip-line Lab act before OpenDiS mobility tables on the full capstone path.\n\n"
    )

    preface210 = preface[start:end]
    tail_old = preface210.split("When row 210 is complete", 1)[1]
    row248_tail_new = (
        "When row 248 is complete"
        + bump210_to_230("When row 210 is complete" + tail_old).split("When row 230 is complete", 1)[1]
    )

    return {
        "row230_preface": row230_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
        "row248_tail_new": row248_tail_new,
    }


ROW229_EPILOGUE_OLD = (
    "Proceed to [row 210](#row-210-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 209 on the full capstone path,"
)
ROW229_EPILOGUE_NEW = (
    "Proceed to [row 230](#row-230-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 229 on the full capstone path,"
)

ROW229_BABY_OLD = (
    "when opening [row 230](preface.md#skill-navigation-row-230) before row 50 closes on the full capstone path"
)
ROW229_BABY_NEW = (
    "when opening [row 231](preface.md#skill-navigation-row-231) before row 50 closes on the full capstone path"
)

ROW229_STITCH_OLD = (
    "before row 230 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW229_STITCH_NEW = (
    "before row 231 homogenization meta prelude capstone reunion opens on the full capstone path."
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 188 closing stitch (Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-228-closing-stitch}"
)


def _strip_premature_row230_epilogue(epilogue: str) -> str:
    """Remove placeholder Row 230 loop lacking {#row-230-closing-loop}."""
    if "{#row-230-closing-loop}" in epilogue:
        return epilogue
    return re.sub(
        r"\n### Row 230 closing loop[\s\S]*?(?=\n### Row 210 closing loop)",
        "\n",
        epilogue,
        count=1,
    )


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 230 skill checkpoint" in preface:
        print("preface: row 230 already present")
    else:
        if "### Row 229 skill checkpoint" not in preface:
            raise SystemExit("row 229 must exist before row 230")
        if "When row 228 is complete" in preface:
            idx = preface.index("When row 228 is complete")
            end = preface.find("\n\n\n\n", idx)
            if end == -1:
                end = preface.find(copper, idx)
            old_tail = preface[idx:end]
            preface = preface.replace(old_tail, b["row248_tail_new"], 1)
        preface = preface.replace(copper, "\n" + b["row230_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 230")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 230 closing stitch" not in prologue:
        needle = "| Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 229) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 229 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 230 closing stitch" not in prologue and PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-229"></span>Row 229 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-228"></span>Row 228 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW229_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW229_STITCH_OLD, ROW229_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 230")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_premature_row230_epilogue(epilogue)
    if "{#row-230-closing-loop}" not in epilogue:
        if ROW229_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW229_EPILOGUE_OLD, ROW229_EPILOGUE_NEW, 1)
        marker = (
            "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
            "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 210 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 230")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230" not in sources:
        sources = sources.replace(
            "| 210 | Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 210 | Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src210_header := (
                "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210) "
                "{#row68-row190-ddd-meta-prelude-capstone-reunion-index-row-210}"
            ),
            b["sources_index"] + src210_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 230")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-230-baby-picture-row68-row210" not in memory:
        memory = memory.replace(
            "| 190 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            b["memory_table"] + "| 190 | Meta | [Row 68 → Row 170 DDD meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 190 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            baby_anchor = (
                "### Row 210 baby picture {#row-210-baby-picture-row68-row190-ddd-meta-prelude-capstone-reunion}"
            )
        memory = memory.replace(
            baby_anchor,
            b["memory_baby"].replace("### Row 210 baby picture", "### Row 230 baby picture", 1)
            + baby_anchor,
            1,
        )
        if ROW229_BABY_OLD in memory:
            memory = memory.replace(ROW229_BABY_OLD, ROW229_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 230")


if __name__ == "__main__":
    main()
