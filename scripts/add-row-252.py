#!/usr/bin/env python3
"""Add row 252 meta-stitch (Row 68 → Row 232 ↔ Row 52 atomistic meta prelude capstone reunion, full capstone path)."""
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


def bump232_to_252(text: str) -> str:
    protected = (
        ("row-252-", "__P250__"),
        ("skill-navigation-row-252", "__S250__"),
        ("prologue-preview-row-252", "__prologue-preview-row-252__"),
        ("{#row-252-closing-stitch}", "__{#row-252-closing-stitch}__"),
        ("{#row-252-closing-loop}", "__{#row-252-closing-loop}__"),
        (
            "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252",
            "__row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252__",
        ),
        (
            "row-252-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion",
            "__row-252-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = shift_meta_bump(out, 20)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add232():
    spec = importlib.util.spec_from_file_location("add232", ROOT / "scripts/add-row-232.py")
    add232 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add232)
    return add232


def _row252_prologue_preview() -> str:
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    anchor = '| <span id="prologue-preview-row-232"></span>'
    if anchor not in prologue:
        raise SystemExit("prologue row 231 preview anchor not found for row 252 preview template")
    start = prologue.index(anchor)
    end = prologue.find("\n", start)
    line = prologue[start:end]
    protected = (
        ("row-252-", "__P250__"),
        ("skill-navigation-row-252", "__S250__"),
        ("prologue-preview-row-252", "__prologue-preview-row-252__"),
        (
            "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252",
            "__IDX250__",
        ),
        (
            "row-252-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion",
            "__BABY251__",
        ),
    )
    out = line
    for old, new in protected:
        out = out.replace(old, new)

    def in_band(n: int) -> bool:
        return 100 <= n <= 270

    delta = 20

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


def _row252_sources_index() -> str:
    """Single row-251 reunion index block (avoid duplicating legacy row-231 index trees)."""
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    header = (
        "## Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 252) "
        "{#row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252}"
    )
    if header in sources:
        start = sources.index(header)
        end = sources.find(
            "\n\n## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249)",
            start,
        )
        if end == -1:
            end = sources.find(
                "\n\n## Row 68 → Row 210 Row 68 → Row 50 homogenization meta prelude capstone reunion index (row 230)",
                start,
            )
        if end != -1:
            return sources[start:end].strip() + "\n\n"
    preface = bump232_to_252(
        (ROOT / "writings/preface/chapters/preface.md")
        .read_text()
        .split("### Row 251 skill checkpoint", 1)[1]
        .split("### Row 252 skill checkpoint", 1)[0]
    )
    return (
        header
        + "\n\n"
        + "Row 252 closes the **atomistic meta prelude capstone** on the full capstone path — "
        + "see [preface row 252](../preface.md#skill-navigation-row-252) and the five-step audit in:\n\n"
        + preface[:800]
        + "…\n\n"
    )


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 232 skill checkpoint")
    end = preface.index("\n\n### Row 233 skill checkpoint", start)
    row252_preface = bump232_to_252(preface[start:end]).strip() + "\n\n"

    b232 = _load_add232()._build_blocks()
    memory_baby = bump232_to_252(b232["memory_baby"])
    memory_baby = memory_baby.replace(
        "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}",
        "### Row 252 baby picture {#row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion}",
        1,
    )
    memory_baby = memory_baby.replace("**Row 232 baby picture:**", "**Row 252 baby picture:**", 1)
    memory_baby = memory_baby.replace(
        "before row 231 atomistic meta prelude capstone opens on the full capstone path.",
        "before row 253 dynamics meta prelude capstone opens on the full capstone path.",
        1,
    )

    out = {
        "row252_preface": row252_preface,
        "prologue_compass": bump232_to_252(b232["prologue_compass"]),
        "prologue_stitch": bump232_to_252(b232["prologue_stitch"]),
        "prologue_preview": _row252_prologue_preview(),
        "epilogue_loop": bump232_to_252(b232["epilogue_loop"]),
        "sources_table": bump232_to_252(b232["sources_table"]).replace(
            "| 232 | Row 68 → Row 212", "| 252 | Row 68 → Row 231", 1
        ),
        "memory_table": (
            "| 252 | Meta | [Row 68 → Row 231 atomistic meta prelude capstone reunion index]"
            "(sources.md#row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252) · "
            "[preface row 252 skill checkpoint](../preface.md#skill-navigation-row-252) · "
            "[prologue row 252 preview](../prologue/00-many-scales.md#prologue-preview-row-252) · "
            "[prologue row 252 closing stitch](../prologue/00-many-scales.md#row-252-closing-stitch) · "
            "[epilogue row 252 closing loop](../epilogue/multiscale.md#row-252-closing-loop) | "
            "Row 68 closed but row 52 atomistic meta reunion feels disconnected from verified "
            "homogenization meta prelude capstone on the full capstone path — read row 68 + row 250 or "
            "row 231 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 51; confirm "
            "handoff Lab act step 5; "
            "[row 252 baby picture](#row-252-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": _row252_sources_index(),
        "memory_baby": memory_baby,
    }
    loop = out["epilogue_loop"]
    loop = loop.replace(
        "### Row 232 closing loop (Row 68 → Row 212",
        "### Row 252 closing loop (Row 68 → Row 231",
        1,
    )
    loop = loop.replace("{#row-232-closing-loop}", "{#row-252-closing-loop}", 1)
    for spill in ("\n\n\n\n### Row 249 closing loop", "\n\n\n\n### Row 250 closing loop"):
        if spill in loop:
            loop = loop.split(spill, 1)[0].rstrip() + "\n\n"
            break
    out["epilogue_loop"] = loop.rstrip() + "\n\n"
    return out


PROLOGUE_STITCH_ANCHOR = (
    "**Row 251 closing stitch (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-251-closing-stitch}"
)

ROW252_INSERT_MARKER = (
    "### Row 231 closing loop (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion) {#row-251-closing-loop}"
)

ROW251_TAIL_OLD = (
    "When row 249 is complete, proceed to [row 250](preface.md#skill-navigation-row-252) when taxonomy meta prelude capstone is clean but homogenization meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 230](preface.md#skill-navigation-row-230) when taxonomy meta prelude capstone is clean but homogenization meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 210](preface.md#skill-navigation-row-210) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 209](preface.md#skill-navigation-row-209) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 229](preface.md#skill-navigation-row-229) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 248](preface.md#skill-navigation-row-248) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW251_TAIL_NEW = (
    "When row 249 is complete, proceed to [row 250](preface.md#skill-navigation-row-252) when taxonomy meta prelude capstone is clean but homogenization meta prelude capstone still lags after verified Burgers closure on the full capstone path, to [row 230](preface.md#skill-navigation-row-230) when taxonomy meta prelude capstone is clean but homogenization meta prelude capstone still lags after verified Burgers closure on the opening-hinge capstone path alone, to [row 210](preface.md#skill-navigation-row-210) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge prelude path alone, to [row 209](preface.md#skill-navigation-row-209) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 229](preface.md#skill-navigation-row-229) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge capstone path alone, to [row 248](preface.md#skill-navigation-row-248) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the full capstone path, to [row 89](preface.md#skill-navigation-row-89) for the Row 68 ↔ Row 49 taxonomy opening prelude audit alone, to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW251_STITCH_OLD = (
    "before row 253 dynamics meta prelude capstone reunion opens on the full capstone path."
)
ROW251_STITCH_NEW = (
    "before row 253 dynamics meta prelude capstone reunion opens on the full capstone path."
)


def _strip_orphan_row252_epilogue(text: str) -> str:
    """Remove misplaced duplicate row-251 closing loops."""
    pattern = (
        r"\n\n### Row 252 closing loop \(Row 68 → Row 232 Row 68 → Row 52 "
        r"atomistic meta prelude capstone reunion\) \{#row-252-closing-loop\}.*?"
        r"(?=\n\n### Row \d+ closing loop)"
    )
    return re.sub(pattern, "", text, flags=re.DOTALL)


def _epilogue_has_row252_at_capstone(text: str) -> bool:
    marker = ROW252_INSERT_MARKER
    if marker not in text:
        return False
    idx = text.index(marker)
    window = text[max(0, idx - 12000) : idx]
    return "{#row-252-closing-loop}" in window and "memory sheet row 252" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 252 skill checkpoint" in preface:
        print("preface: row 252 already present")
    else:
        if "### Row 251 skill checkpoint" not in preface:
            raise SystemExit("row 251 must exist before row 252")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        if ROW251_TAIL_OLD in preface:
            preface = preface.replace(ROW251_TAIL_OLD, ROW251_TAIL_NEW, 1)
        preface = preface.replace(copper, "\n" + b["row252_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 252")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "atomistic meta prelude capstone reunion (row 252) |" not in prologue and (
        "prologue-preview-row-252" not in prologue
    ):
        needle = (
            "| Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 251) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 251 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        stitch = PROLOGUE_STITCH_ANCHOR
        if stitch in prologue:
            prologue = prologue.replace(stitch, b["prologue_stitch"] + stitch, 1)
        preview_anchor = '| <span id="prologue-preview-row-251"></span>Row 251 preview'
        if preview_anchor not in prologue:
            preview_anchor = '| <span id="prologue-preview-row-251"></span>Row 229 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW251_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW251_STITCH_OLD, ROW251_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 252")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_orphan_row252_epilogue(epilogue)
    if (
        "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion)"
        in epilogue
        and "memory sheet row 252" in epilogue
    ):
        epilogue_path.write_text(epilogue)
        print("epilogue: row 252 closing loop already present")
    elif not _epilogue_has_row252_at_capstone(epilogue):
        marker = ROW252_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 251 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 252")
    else:
        epilogue_path.write_text(epilogue)
        print("epilogue: row 252 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252" not in sources:
        sources = sources.replace(
            "| 251 | Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone",
            b["sources_table"] + "| 251 | Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 230 Row 68 → Row 50 homogenization meta prelude capstone reunion index (row 250) "
            "{#row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251}"
        )
        if src_header in sources and b["sources_index"].strip() not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 252")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "### Row 252 baby picture {#row-252-baby-picture-row68-row231" not in memory:
        memory = memory.replace(
            "| 250 | Meta | [Row 68 → Row 230 homogenization meta prelude capstone reunion index](sources.md#row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251)",
            b["memory_table"]
            + "| 250 | Meta | [Row 68 → Row 230 homogenization meta prelude capstone reunion index](sources.md#row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251)",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 251 baby picture {#row-251-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion}",
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 252")
    else:
        memory_path.write_text(memory)
        print("memory-sheet: row 252 baby already present")


if __name__ == "__main__":
    main()
