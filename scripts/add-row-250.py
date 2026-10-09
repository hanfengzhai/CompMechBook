#!/usr/bin/env python3
"""Add row 250 meta-stitch (Row 68 → Row 230 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–270) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

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


def bump230_to_250(text: str) -> str:
    protected = (
        ("row-250-", "__P250__"),
        ("skill-navigation-row-250", "__S250__"),
        ("prologue-preview-row-250", "__prologue-preview-row-250__"),
        ("{#row-250-closing-stitch}", "__{#row-250-closing-stitch}__"),
        ("{#row-250-closing-loop}", "__{#row-250-closing-loop}__"),
        (
            "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
            "__row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250__",
        ),
        (
            "row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion",
            "__row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add230():
    spec = importlib.util.spec_from_file_location("add230", ROOT / "scripts/add-row-230.py")
    add230 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add230)
    return add230


def _row250_prologue_preview() -> str:
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    anchor = '| <span id="prologue-preview-row-170"></span>'
    if anchor not in prologue:
        raise SystemExit("prologue row 170 preview anchor not found for row 250 preview template")
    start = prologue.index(anchor)
    end = prologue.find("\n", start)
    line = prologue[start:end]
    protected = (
        ("row-250-", "__P250__"),
        ("skill-navigation-row-250", "__S250__"),
        ("prologue-preview-row-250", "__prologue-preview-row-250__"),
        (
            "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
            "__IDX250__",
        ),
        (
            "row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion",
            "__BABY250__",
        ),
    )
    out = line
    for old, new in protected:
        out = out.replace(old, new)

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

    delta = 80

    def bump_num(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return str(n + delta) if in_band(n) else m.group(0)

    for pat in (
        r"row68-row(\d{3})",
        r"index-row-(\d{3})",
        r"skill-navigation-row-(\d{3})",
        r"prologue-preview-row-(\d{3})",
        r"row-(\d{3})-(closing-stitch|closing-loop|baby-picture)",
    ):
        out = re.sub(
            pat,
            lambda m, d=delta: (
                m.group(0).replace(m.group(1), str(int(m.group(1)) + d))
                if in_band(int(m.group(1)))
                else m.group(0)
            ),
            out,
        )
    out = re.sub(
        r"\brow (\d{3})\b",
        lambda m: f"row {int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"\bRow (\d{3})\b",
        lambda m: f"Row {int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    for old, new in protected:
        out = out.replace(new, old)
    return out + "\n"


def _row250_sources_index() -> str:
    """Single row-250 reunion index block (avoid duplicating legacy row-230 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 250) "
        "{#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249)",
            start,
        )
        if end == -1:
            end = sources.find(
                "\n\n## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230)",
                start,
            )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump230_to_250(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 230 skill checkpoint", 1)[1]
        .split("### Row 231 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 250 closes the **DDD meta prelude capstone** on the full capstone path — "
        + "see [preface row 250](../preface.md#skill-navigation-row-250) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 230 skill checkpoint")
    end = preface.index("\n\n### Row 231 skill checkpoint", start)
    row250_preface = bump230_to_250(preface[start:end]).strip() + "\n\n"

    b230 = _load_add230()._build_blocks()
    memory_baby = bump230_to_250(b230["memory_baby"])
    memory_baby = memory_baby.replace(
        "### Row 230 baby picture {#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}",
        "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
        1,
    )
    memory_baby = memory_baby.replace("**Row 230 baby picture:**", "**Row 250 baby picture:**", 1)
    memory_baby = memory_baby.replace(
        "before row 231 homogenization meta prelude capstone opens on the full capstone path.",
        "before row 251 homogenization meta prelude capstone opens on the full capstone path.",
        1,
    )

    out = {
        "row250_preface": row250_preface,
        "prologue_compass": bump230_to_250(b230["prologue_compass"]),
        "prologue_stitch": bump230_to_250(b230["prologue_stitch"]),
        "prologue_preview": _row250_prologue_preview(),
        "epilogue_loop": bump230_to_250(b230["epilogue_loop"]),
        "sources_table": bump230_to_250(b230["sources_table"]).replace(
            "| 230 | Row 68 → Row 210", "| 250 | Row 68 → Row 230", 1
        ),
        "memory_table": (
            "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]"
            "(sources.md#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250) · "
            "[preface row 250 skill checkpoint](../preface.md#skill-navigation-row-250) · "
            "[prologue row 250 preview](../prologue/00-many-scales.md#prologue-preview-row-250) · "
            "[prologue row 250 closing stitch](../prologue/00-many-scales.md#row-250-closing-stitch) · "
            "[epilogue row 250 closing loop](../epilogue/multiscale.md#row-250-closing-loop) | "
            "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified "
            "taxonomy meta prelude capstone on the full capstone path — read row 68 + row 249 or "
            "row 230 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; confirm "
            "slip-line Lab act; "
            "[row 250 baby picture](#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row250_sources_index(),
        "memory_baby": memory_baby,
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 250 closing loop (Row 68 → Row 230",
        "### Row 230 closing loop (Row 68 → Row 230",
        1,
    )
    for spill in ("\n\n\n\n### Row 249 closing loop", "\n\n\n\n### Row 250 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 249 closing stitch (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-249-closing-stitch}"
)

ROW250_INSERT_MARKER = (
    "### Row 229 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion) {#row-249-closing-loop}"
)

ROW249_TAIL_OLD = (
    "When row 249 is complete, proceed to [row 250](preface.md#skill-navigation-row-250) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 230](preface.md#skill-navigation-row-230) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 210](preface.md#skill-navigation-row-210) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 209](preface.md#skill-navigation-row-209) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 229](preface.md#skill-navigation-row-229) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 248](preface.md#skill-navigation-row-248) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW249_TAIL_NEW = (
    "When row 249 is complete, proceed to [row 250](preface.md#skill-navigation-row-250) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 230](preface.md#skill-navigation-row-230) when taxonomy meta prelude capstone is clean but DDD meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 210](preface.md#skill-navigation-row-210) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 209](preface.md#skill-navigation-row-209) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 229](preface.md#skill-navigation-row-229) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 248](preface.md#skill-navigation-row-248) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW249_STITCH_OLD = (
    "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
)
ROW249_STITCH_NEW = (
    "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def _strip_orphan_row250_epilogue(text: str) -> str:
    """Remove misplaced duplicate row-250 closing loops."""
    pattern = (
        r"\n\n### Row 250 closing loop \(Row 68 → Row 230 Row 68 → Row 50 "
        r"DDD meta prelude capstone reunion\) \{#row-250-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def _epilogue_has_row250_at_capstone(text: str) -> bool:
    marker = ROW250_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return "{#row-250-closing-loop}" in window and "memory sheet row 250" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 250 skill checkpoint" in preface:
        print("preface: row 250 already present")
    else:
        if "### Row 249 skill checkpoint" not in preface:
            raise SystemExit("row 249 must exist before row 250")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        if ROW249_TAIL_OLD in preface:
            preface = preface.replace(ROW249_TAIL_OLD, ROW249_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row250_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 250")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "DDD meta prelude capstone reunion (row 250) |" not in prologue and (
        "prologue-preview-row-250" not in prologue
    ):
        needle = (
            "| Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 249) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 249 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch = PROLOGUE_STITCH_ANCHOR
        if stitch in prologue:
            prologue = prologue.replace(stitch, b["prologue_stitch"] + stitch, 1)
        preview_anchor = '| <span id="prologue-preview-row-249"></span>Row 249 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-249"></span>Row 229 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW249_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW249_STITCH_OLD, ROW249_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 250")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row250_epilogue(epilogue)
    if not _epilogue_has_row250_at_capstone(epilogue):
        marker = ROW250_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 249 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 250")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 250 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250" not in sources:
        sources = sources.replace(
            "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249) "
            "{#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 250")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 250 baby picture {#row-250-baby-picture-row68-row230" not in memory:
        memory = memory.replace(
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index](sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
            b["memory_table"]
            + "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index](sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}",
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 250")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 250 baby already present")


if __name__ == "__main__":
    main()
