#!/usr/bin/env python3
"""Add row 250 meta-stitch (Row 68 → Row 230 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 90, 108,
}


def bump_meta_plus20(text: str) -> str:
    """Shift capstone-path meta row numbers by +20; preserve plot-spine row ids."""

    def repl(m: re.Match[str]) -> str:
        n = int(m.group(1))
        if n in PRESERVE_ROW_NUMS:
            return m.group(0)
        return m.group(0).replace(str(n), str(n + 20))

    for pat in (
        r"(?<![0-9])row (\d+)",
        r"(?<![0-9])Row (\d+)",
        r"skill-navigation-row-(\d+)",
        r"prologue-preview-row-(\d+)",
        r"row-(\d+)-closing",
        r"row-(\d+)-baby-picture",
        r"row68-row(\d+)",
        r"reunion-index-row-(\d+)",
        r"index-row-(\d+)",
    ):
        text = re.sub(pat, repl, text)
    return text


def t230_to_250(text: str) -> str:
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
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add230():
    spec = importlib.util.spec_from_file_location("add230", ROOT / "scripts/add-row-230.py")
    add230 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add230)
    return add230


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 230 skill checkpoint")
    end = preface.index("\n\n### Row 231 skill checkpoint", start)
    row250_preface = t230_to_250(preface[start:end]).strip() + "\n\n"

    b230 = _load_add230()._build_blocks()
    epilogue_loop = t230_to_250(b230["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace(
        "### Row 250 closing loop (Row 68 → Row 230",
        "### Row 230 closing loop (Row 68 → Row 230",
        1,
    )
    for spill in ("\n\n\n\n### Row 249 closing loop", "\n\n\n\n### Row 250 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    return {
        "row250_preface": row250_preface,
        "prologue_compass": t230_to_250(b230["prologue_compass"]),
        "prologue_stitch": t230_to_250(b230["prologue_stitch"]),
        "prologue_preview": t230_to_250(b230["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t230_to_250(b230["sources_table"]).replace(
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
            "row 230 gate + VII.1 Bridge → VII.2 + row 50; confirm slip-line Lab act; "
            "[row 250 baby picture](#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": (
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}\n\n"
            "**Row 250 baby picture:** when row 68 closed the midpoint prelude and row 249 or row 230 closed "
            "taxonomy meta prelude capstone / DDD meta prelude but **row 50's VII.1 → VII.2 audit or the "
            "Bridge → Peach–Köhler chain still feel like separate checklists on the full capstone path**, "
            "open the [Row 68 → Row 230 DDD meta prelude capstone reunion index]"
            "(sources.md#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250) — read "
            "[preface row 68](../preface.md#skill-navigation-row-68) gate → "
            "[preface row 249](../preface.md#skill-navigation-row-249) or "
            "[preface row 230](../preface.md#skill-navigation-row-230) taxonomy meta prelude capstone / "
            "DDD meta prelude gate → [VII.1 Bridge](../part07-defects/01-defect-taxonomy.md#bridge) through "
            "[VII.2 opening hinge from VII.1](../part07-defects/02-dislocation-dynamics.md#opening-hinge-vii1-to-vii2) "
            "aloud → [preface row 50](../preface.md#skill-navigation-row-50) five-step audit → confirm "
            "slip-line Lab act before OpenDiS mobility tables on the full capstone path.\n\n"
            "```mermaid\n"
            "flowchart LR\n"
            "  MP[Midpoint row 68]\n"
            "  TM[Taxonomy meta prelude capstone row 249]\n"
            "  BR[VII.1 Bridge]\n"
            "  R50[row 50 meta gate]\n"
            "  MP --> TM --> BR --> R50\n"
            "```\n\n"
            "When row 250 feels disconnected from row 249, read them as **taxonomy meta prelude capstone vs "
            "DDD meta prelude capstones on the full capstone path**: row 249 when **VII.0 Bridge and "
            "Row 68 → Row 49 meta must read on the same wire before any VII.1 → VII.2 audit on the full "
            "capstone path**; row 250 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same "
            "wire before row 251 homogenization meta prelude capstone opens on the full capstone path** — "
            "same copper wire, same Functional Analysis Notes layout, one continuous Burgers → Peach–Köhler "
            "afternoon after verified taxonomy meta prelude capstone on the full capstone path.\n\n"
        ),
    }


PROLOGUE_STITCH_ANCHOR = (
    "**Row 209 closing stitch (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-249-closing-stitch}"
)

ROW250_INSERT_MARKER = (
    "### Row 228 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-248-closing-loop}"
)

ROW249_STITCH_OLD = "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
ROW249_STITCH_NEW = "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."


def _epilogue_has_row250_at_capstone(text: str) -> bool:
    if ROW250_INSERT_MARKER not in text:
        return False
    idx = text.index(ROW250_INSERT_MARKER)
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
        preface = preface.replace(copper, "\n" + b["row250_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 250")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "DDD meta prelude capstone reunion (row 250) |" not in prologue:
        needle = (
            "| Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 249) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 249 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-249"></span>Row 249 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW249_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW249_STITCH_OLD, ROW249_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 250")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row250_at_capstone(epilogue):
        marker = ROW250_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 249 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 250")
    else:
        print("epilogue: row 250 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "| 250 | Row 68 → Row 230" not in sources:
        sources = sources.replace(
            "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            b["sources_table"] + "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 250 continuity table row")
    else:
        print("sources: row 250 continuity table row already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 250 baby picture {#row-250-baby-picture-row68-row230" not in memory:
        memory = memory.replace(
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index](sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
            b["memory_table"]
            + "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index](sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
            1,
        )
        baby_anchor = (
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 250")
    else:
        print("memory-sheet: row 250 baby already present")


if __name__ == "__main__":
    main()
