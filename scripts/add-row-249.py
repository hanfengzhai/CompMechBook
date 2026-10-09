#!/usr/bin/env python3
"""Add row 249 meta-stitch (Row 68 → Row 229 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–250) by delta for meta-stitch copy."""

    def in_band(n: int) -> bool:
        return 100 <= n <= 250

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


def bump229_to_249(text: str) -> str:
    protected = (
        ("row-249-", "__P249__"),
        ("skill-navigation-row-249", "__S249__"),
        ("prologue-preview-row-249", "__prologue-preview-row-249__"),
        ("{#row-249-closing-stitch}", "__{#row-249-closing-stitch}__"),
        ("{#row-249-closing-loop}", "__{#row-249-closing-loop}__"),
        (
            "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249",
            "__row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249__",
        ),
        (
            "row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion",
            "__row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add229():
    spec = importlib.util.spec_from_file_location("add229", ROOT / "scripts/add-row-229.py")
    add229 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add229)
    return add229


def _row249_sources_index() -> str:
    """Single row-249 reunion index block (avoid duplicating legacy row-229 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249) "
        "{#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 248)",
            start,
        )
        if end == -1:
            end = sources.find(
                "\n\n## Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 229)",
                start,
            )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump229_to_249(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 229 skill checkpoint", 1)[1]
        .split("### Row 230 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 249 closes the **taxonomy meta prelude capstone** on the full capstone path — "
        + "see [preface row 249](../preface.md#skill-navigation-row-249) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 229 skill checkpoint")
    end = preface.index("\n\n### Row 230 skill checkpoint", start)
    row249_preface = bump229_to_249(preface[start:end]).strip() + "\n\n"

    b229 = _load_add229()._build_blocks()
    out = {
        "row249_preface": row249_preface,
        "prologue_compass": bump229_to_249(b229["prologue_compass"]),
        "prologue_stitch": bump229_to_249(b229["prologue_stitch"]),
        "prologue_preview": bump229_to_249(b229["prologue_preview"]),
        "epilogue_loop": bump229_to_249(b229["epilogue_loop"]),
        "sources_table": bump229_to_249(b229["sources_table"]).replace(
            "| 229 | Row 68 → Row 209", "| 249 | Row 68 → Row 229", 1
        ),
        "memory_table": (
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]"
            "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249) · "
            "[preface row 249 skill checkpoint](../preface.md#skill-navigation-row-249) · "
            "[prologue row 249 preview](../prologue/00-many-scales.md#prologue-preview-row-249) · "
            "[prologue row 249 closing stitch](../prologue/00-many-scales.md#row-249-closing-stitch) · "
            "[epilogue row 249 closing loop](../epilogue/multiscale.md#row-249-closing-loop) | "
            "Row 68 closed but row 49 taxonomy meta reunion feels disconnected from verified "
            "midpoint meta prelude capstone on the full capstone path — read row 68 + row 248 or "
            "row 229 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; confirm "
            "`hardening.yaml` beside Act IV; "
            "[row 249 baby picture](#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row249_sources_index(),
        "memory_baby": (
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}\n\n"
            "**Row 249 baby picture:** when row 68 closed the midpoint prelude and row 248 or row 229 "
            "closed midpoint meta prelude capstone / taxonomy meta prelude on the full capstone path "
            "but **row 49's VII.0 → VII.1 audit or the Bridge → Burgers chain still feel like separate "
            "checklists on the full capstone path**, open the "
            "[Row 68 → Row 229 taxonomy meta prelude capstone reunion index]"
            "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 248](../preface.md#skill-navigation-row-248) or "
            "[preface row 229](../preface.md#skill-navigation-row-229) midpoint meta prelude capstone / "
            "taxonomy meta prelude gate → [VII.0 Bridge](../part07-defects/00-opening.md#bridge) "
            "through [VII.1 opening hinge from VII.0](../part07-defects/01-defect-taxonomy.md#opening-hinge-vii0-to-vii1) "
            "aloud → [preface row 49](../preface.md#skill-navigation-row-49) five-step audit → confirm "
            "`hardening.yaml` beside Act IV before row 250 DDD meta prelude capstone opens on the full capstone path.\n\n"
            "```mermaid\nflowchart LR\n  MP[Midpoint row 68]\n  MM[Midpoint meta row 248]\n"
            "  BR[VII.0 Bridge to VII.1]\n  R49[row 49 meta gate]\n  MP --> MM --> BR --> R49\n```\n\n"
            "When row 249 feels disconnected from row 248, read them as **midpoint meta prelude capstone "
            "vs taxonomy meta prelude capstones on the full capstone path**: row 248 when "
            "**VI.4 intermission and Row 67 → Row 48 meta must read on the same wire before any "
            "VII.0 → VII.1 audit on the full capstone path**; row 249 when "
            "**VII.0 Bridge and Row 68 → Row 49 meta must read on the same wire before "
            "row 250 DDD meta prelude capstone opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous forest landing → "
            "Burgers afternoon after verified midpoint meta prelude capstone on the full capstone path. "
            "When row 248 closed but taxonomy meta reunion still lags on the full capstone path, switch to [row 249]"
            "(#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion).\n\n\n"
        ),
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 249 closing loop (Row 68 → Row 229",
        "### Row 229 closing loop (Row 68 → Row 229",
        1,
    )
    for spill in ("\n\n\n\n### Row 248 closing loop", "\n\n\n\n### Row 249 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 248 closing stitch (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-248-closing-stitch}"
)

ROW249_INSERT_MARKER = (
    "### Row 228 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-248-closing-loop}"
)

ROW248_TAIL_OLD = (
    "When row 248 is complete, proceed to [row 249](preface.md#skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 229](preface.md#skill-navigation-row-209) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 209](preface.md#skill-navigation-row-169) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 128](preface.md#skill-navigation-row-128) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 248](preface.md#skill-navigation-row-248) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 247](preface.md#skill-navigation-row-247) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW248_TAIL_NEW = (
    "When row 248 is complete, proceed to [row 249](preface.md#skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 229](preface.md#skill-navigation-row-229) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 209](preface.md#skill-navigation-row-189) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 128](preface.md#skill-navigation-row-128) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 228](preface.md#skill-navigation-row-228) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 247](preface.md#skill-navigation-row-247) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW248_STITCH_OLD = (
    "before row 229 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW248_STITCH_NEW = (
    "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
)


def _strip_orphan_row249_epilogue(text: str) -> str:
    """Remove misplaced duplicate row-249 closing loops."""
    pattern = (
        r"\n\n### Row 249 closing loop \(Row 68 → Row 229 Row 68 → Row 49 "
        r"taxonomy meta prelude capstone reunion\) \{#row-249-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def _epilogue_has_row249_at_capstone(text: str) -> bool:
    marker = ROW249_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return "{#row-249-closing-loop}" in window and "memory sheet row 249" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 249 skill checkpoint" in preface:
        print("preface: row 249 already present")
    else:
        if "### Row 248 skill checkpoint" not in preface:
            raise SystemExit("row 248 must exist before row 249")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        if ROW248_TAIL_OLD in preface:
            preface = preface.replace(ROW248_TAIL_OLD, ROW248_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row249_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 249")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "taxonomy meta prelude capstone reunion (row 249) |" not in prologue and (
        "prologue-preview-row-249" not in prologue
    ):
        needle = (
            "| Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 248) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 248 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-248"></span>Row 248 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW248_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW248_STITCH_OLD, ROW248_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 249")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row249_epilogue(epilogue)
    if not _epilogue_has_row249_at_capstone(epilogue):
        marker = ROW249_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 248 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 249")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 249 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249" not in sources:
        sources = sources.replace(
            "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            b["sources_table"] + "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 248) "
            "{#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 249")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 249 baby picture {#row-249-baby-picture-row68-row229" not in memory:
        memory = memory.replace(
            "| 248 | Meta | [Row 68 → Row 228 midpoint meta prelude capstone reunion index](sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248)",
            b["memory_table"]
            + "| 248 | Meta | [Row 68 → Row 228 midpoint meta prelude capstone reunion index](sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
            "### Row 228 baby picture {#row-228-baby-picture-row68-row208-midpoint-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 249")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 249 baby already present")


if __name__ == "__main__":
    main()
