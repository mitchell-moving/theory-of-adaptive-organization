#!/usr/bin/env python3
"""Headline-claim check for the GTAO repository (stdlib only).

The canonical statuses live in the headline ledger of
measurement/CLAIM_MAP_v2.md (between the ledger markers). No other page copies
them: README.md, CORE.md and THEORY.md carry a one-line link to that ledger
instead of a claims view. This script fails when a page carries a claims view
or a front page lacks the link, when a cited source or review path is missing, when an edge is invalid,
when a front page states a headline status the ledger does not, when the
hypothesis sentence changes, or when a page claims Lean coverage the ledger
does not give.

Run from the repo root:  python3 tools/check_claims.py
Exit 0 = no FAIL. A local pass is not a server-side publication gate.
"""
from __future__ import annotations

import glob
import os
import re
import sys

HYPOTHESIS = (
    "The law of adaptive organization (hypothesis): "
    "strongly selected systems minimize the cost of judgment."
)
HYP_FILES = [
    "README.md",
    "CORE.md",
    "THEORY.md",
    "theory/COADAPTATION.md",
    "theory/GROWTH_BRIDGE.md",
    "theory/FEEDBACK_FLOOR_2026-11-23.md",
    "theory/SWARM_RULE_2026-11-23.md",
    "theory/AREA_LAW_PROBE_2026-11-23.md",
]
FRONT = ["README.md", "CORE.md", "THEORY.md"]
# Claims views are retired (25 November 2026): each front page carries a one-line link to the ledger instead.
LINK_FILES = ["README.md", "CORE.md", "THEORY.md"]
LINK_RX = re.compile(r"\[`?measurement/CLAIM_MAP_v2\.md`?\]\(measurement/CLAIM_MAP_v2\.md\)")
STATUSES = {
    "proved-in-model",
    "known",
    "open",
    "conjecture",
    "hypothesis",
    "false",
    "synthesis",
    "interpretation",
}
EDGE_KINDS = {"proved", "known", "interpretation", "open", "conjecture"}
LEDGER_BEGIN = "<!-- headline-ledger:begin -->"
LEDGER_END = "<!-- headline-ledger:end -->"
RULES_BEGIN = "<!-- claim-rules:begin -->"
RULES_END = "<!-- claim-rules:end -->"
VIEW_BEGIN = "<!-- claims-view:begin -->"
VIEW_END = "<!-- claims-view:end -->"
LEAN_OVERCLAIM = re.compile(
    r"whole physical theorem is formalized|all of the physics is formalized|"
    r"every heat floor is formalized|the physical argument as a whole is formalized",
    re.I,
)
UNMANAGED = re.compile(
    r"\b(T\d{2,}|CX\d+|CT\d{2}|CA\d+|F\d+|CL\d{2}|BICAUSAL|IP5)\b"
    r"[^.\n]{0,100}\b(PROVED|OPEN|CONJECTURE)\b"
)
ROW_ID = re.compile(r"^\| ([A-Za-z][A-Za-z0-9-]*) \|")
CLAIM_ROW = re.compile(r"^\| ((?:[A-Z]{1,2}\d+[′']?[a-z]?)) \|")
GAP_ID = re.compile(r"^\| ([A-Z][A-Z0-9-]*) \|")


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(root, path):
    with open(os.path.join(root, path), encoding="utf-8") as fh:
        return fh.read()


def split_cells(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    if line.strip().startswith("|"):
        parts = parts[1:]
    if line.strip().endswith("|") and not line.strip().endswith("\\|"):
        parts = parts[:-1]
    return [p.strip() for p in parts]


def parse_ledger(text):
    """Return (rows, rules, errors) from a CLAIM_MAP document."""
    errors = []
    if LEDGER_BEGIN not in text or LEDGER_END not in text:
        return [], [], ["claims: headline ledger markers missing"]
    block = text.split(LEDGER_BEGIN, 1)[1].split(LEDGER_END, 1)[0]
    rows = []
    header = None
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = split_cells(line)
        if header is None:
            header = cells
            continue
        if set(cells) <= {"---", ":---", "---:"} or all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        if len(cells) != len(header):
            errors.append("claims: ledger row has %d cells, header %d (%s)" % (len(cells), len(header), cells[0] if cells else "?"))
            continue
        row = dict(zip(header, cells))
        rows.append(row)
    if not rows:
        errors.append("claims: headline ledger has no rows")
    seen = set()
    for row in rows:
        ident = row.get("id", "")
        if not ident or ident in seen:
            errors.append("claims: duplicate or blank ledger id %r" % ident)
        seen.add(ident)
        if row.get("status") not in STATUSES:
            errors.append("claims: %s has status %r" % (ident, row.get("status")))
        if not row.get("source") or not row.get("anchor") or not row.get("plain"):
            errors.append("claims: %s missing plain, source, or anchor" % ident)
    rules = []
    if RULES_BEGIN not in text or RULES_END not in text:
        errors.append("claims: claim-rules markers missing")
    else:
        rblock = text.split(RULES_BEGIN, 1)[1].split(RULES_END, 1)[0]
        for line in rblock.splitlines():
            line = line.strip()
            if not line or line.startswith("<!--"):
                continue
            parts = line.split(" ", 2)
            if len(parts) < 3 or parts[0] not in {"must", "forbid", "must-near", "forbid-near"}:
                errors.append("claims: bad rule %r" % line[:80])
                continue
            if parts[0].endswith("-near"):
                bits = parts[2].split(" ", 1)
                if len(bits) != 2:
                    errors.append("claims: bad near-rule %r" % line[:80])
                    continue
                rules.append((parts[0], parts[1], bits[0], bits[1]))
            else:
                rules.append((parts[0], parts[1], None, parts[2]))
    return rows, rules, errors


def strip_view(text):
    return re.sub(
        re.escape(VIEW_BEGIN) + r".*?" + re.escape(VIEW_END),
        "",
        text,
        flags=re.S,
    )


def claim_ids(text):
    ids = set()
    # Count only the lettered claim sections, not the headline ledger.
    if LEDGER_BEGIN in text:
        text = text.split(LEDGER_BEGIN, 1)[0]
    for line in text.splitlines():
        m = CLAIM_ROW.match(line)
        if m:
            ids.add(m.group(1))
    return ids


def paragraphs_with(text, ident):
    """Lines that name ident. These pages put one claim on one long line."""
    body = strip_view(text)
    rx = re.compile(r"(?<![A-Za-z0-9-])" + re.escape(ident) + r"(?![A-Za-z0-9-])")
    return [ln for ln in body.splitlines() if rx.search(ln)]


def check_sources(rows, root):
    errors = []
    lean_tree = os.path.isdir(os.path.join(root, "formal", "lean", "GTAO"))
    for row in rows:
        ident = row["id"]
        src = row["source"]
        m = re.match(r"^([^:]+):(\d+)(?:-(\d+))?$", src)
        if not m:
            errors.append("claims: %s source %r is not path:line" % (ident, src))
            continue
        path, start, end = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            errors.append("claims: source missing %s (%s)" % (path, ident))
            continue
        lines = read(root, path).splitlines()
        if start < 1 or end > len(lines) or end < start:
            errors.append("claims: %s source range %s outside %s (%d lines)" % (ident, src, path, len(lines)))
            continue
        chunk = "\n".join(lines[start - 1:end])
        if row["anchor"] not in chunk:
            errors.append("claims: %s anchor not in %s" % (ident, src))
        lean = row.get("lean", "")
        if re.search(r"\b(1185|whole|entire physics|all heat floors)\b", lean, re.I):
            errors.append("claims: %s lean cell treats an aggregate or a whole-physics claim as coverage" % ident)
        for lp in re.findall(r"formal/lean/\S+?\.lean", lean):
            if lean_tree and not os.path.isfile(os.path.join(root, lp)):
                errors.append("claims: %s lean path missing %s" % (ident, lp))
        for rp in re.findall(r"`([^`]+)`", row.get("review", "")):
            if "/" not in rp:
                continue
            if not os.path.isfile(os.path.join(root, rp)):
                errors.append("claims: review path missing %s (%s)" % (rp, ident))
    return errors


def check_edges(rows, known):
    errors = []
    ids = {r["id"] for r in rows}
    for row in rows:
        raw = row.get("connects", "").strip()
        if raw in {"", "-"}:
            errors.append("claims: %s has no connects edge" % row["id"])
            continue
        for edge in raw.split(";"):
            edge = edge.strip()
            if ":" not in edge:
                errors.append("claims: edge %r on %s" % (edge, row["id"]))
                continue
            target, kind = edge.split(":", 1)
            if kind not in EDGE_KINDS:
                errors.append("claims: edge %s has kind %r" % (row["id"], kind))
            if target not in ids and target not in known:
                errors.append("claims: edge %s -> %s is not a ledger or claim-map id" % (row["id"], target))
    return errors


def check_views(rows, root):
    """No page carries a claims view; each front page links to the ledger instead."""
    errors = []
    pages = set(LINK_FILES) | set(direction_pages(root)) | {p for p in glob.glob("**/*.md", root_dir=root, recursive=True)
                                                           if not p.startswith(("reviews/", "theory/reviews/", "prereg/"))}
    for path in sorted(pages):
        if os.path.isfile(os.path.join(root, path)) and VIEW_BEGIN in read(root, path):
            errors.append("claims: %s carries a claims view; link to measurement/CLAIM_MAP_v2.md instead" % path)
    for path in LINK_FILES:
        if not os.path.isfile(os.path.join(root, path)):
            errors.append("claims: front page missing %s" % path)
        elif not LINK_RX.search(read(root, path)):
            errors.append("claims: %s lacks the one-line link to measurement/CLAIM_MAP_v2.md" % path)
    return errors


def check_rules(rules, rows, root):
    errors = []
    ids = {r["id"] for r in rows}
    by_id = {r["id"]: r for r in rows}
    for kind, path, ident, phrase in rules:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            errors.append("claims: rule file missing %s" % path)
            continue
        text = strip_view(read(root, path))
        if ident:
            if ident not in ids:
                errors.append("claims: rule names unknown id %s" % ident)
                continue
            windows = paragraphs_with(read(root, path), ident)
            hit = any(phrase in w for w in windows)
            if kind == "must-near" and not hit:
                errors.append("claims: mismatch %s prose lacks %r near %s" % (path, phrase, ident))
            if kind == "forbid-near" and hit:
                errors.append("claims: mismatch %s prose has %r near %s" % (path, phrase, ident))
            # Status word in the same paragraph must not fight the ledger.
            status = by_id[ident]["status"]
            for w in windows:
                if status == "open" and re.search(r"\bPROVED\b", w) and not re.search(r"\bnot\b[^.]{0,40}\bPROVED\b|no\b[^.]{0,40}\bPROVED\b", w):
                    errors.append("claims: mismatch %s says PROVED near open %s" % (path, ident))
                if status == "proved-in-model" and re.search(r"not worked out|remains open", w) and not re.search(
                    r"beyond|outside those|applying|joined|general case|still open|not worked out\. OPEN", w
                ):
                    errors.append("claims: mismatch %s undersells proved %s" % (path, ident))
        else:
            hit = phrase in text
            if kind == "must" and not hit:
                errors.append("claims: mismatch %s lacks %r" % (path, phrase))
            if kind == "forbid" and hit:
                errors.append("claims: mismatch %s has %r" % (path, phrase))
    return errors


def check_hypothesis(root):
    errors = []
    for path in HYP_FILES:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        if HYPOTHESIS not in read(root, path):
            errors.append("claims: hypothesis sentence changed or missing in %s" % path)
    for path in FRONT:
        full = os.path.join(root, path)
        if os.path.isfile(full) and HYPOTHESIS not in read(root, path):
            errors.append("claims: hypothesis sentence changed or missing in %s" % path)
    # A line that states the hypothesis, marked by "(hypothesis):", must carry the CORE.md:7 sentence.
    # A label that names "(hypothesis)" without the colon is not that sentence.
    import check_consistency
    mark = "(hypothesis):"
    for path in check_consistency.MAINTAINED_DOCS:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        for ln, line in enumerate(read(root, path).splitlines(), 1):
            if mark in line and HYPOTHESIS not in line:
                errors.append("claims: hypothesis sentence altered or incomplete in %s:%d" % (path, ln))
    return errors


def check_unmanaged(rows, root, known):
    errors = []
    ids = {r["id"] for r in rows} | set(known)
    for path in FRONT:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        body = strip_view(read(root, path))
        if path == "THEORY.md" and "## Appendix C" in body:
            body = body.split("## Appendix C", 1)[0]
        if LEAN_OVERCLAIM.search(body):
            errors.append("claims: lean overclaim in %s" % path)
        for m in UNMANAGED.finditer(body):
            ident = m.group(1)
            if ident not in ids:
                errors.append("claims: unmanaged headline %s in %s" % (ident, path))
    return errors


# ------------------------------------------------------------------ direction (README.md, Ranked gaps)
PARKED_IDS = {"DATA-ONE", "RS-SCREEN"}
REAL_IDS = re.compile(r"(?<![A-Za-z0-9-])(DATA-ONE|RS-SCREEN)(?![A-Za-z0-9])")
ORDER = re.compile(r"\brank(?:ed)?\s*\d|\bnext\b|\bthen\b|\bqueued?\b|\bpriority\b|\bin parallel\b|\bbest (?:two|one|candidates?)\b"
                   r"|^\s*\d+\.\s", re.I)
REAL_WORK = re.compile(r"\breal(?:-world)?\b[^.\n]{0,40}\b(?:systems?|data|tests?)\b|\bLevel 2\b|\bfield tests?\b", re.I)
PARKED_OK = re.compile(r"\bparked\b|\bnot ranked\b|\bdownstream\b", re.I)
DIRECTION_LINE = re.compile(r"^\*\*Direction \([^)]*\d{4}\):\*\*", re.M)


def ranked_section(text):
    m = re.search(r"^## Ranked gaps.*", text, re.M | re.S)
    return m.group(0).split("\n## ", 1)[0] if m else None


def direction_pages(root):
    import check_fresh
    pages = set(check_fresh.live_pages(root)) | {p for p in glob.glob("theory/*.md", root_dir=root)}
    return sorted(p for p in pages if p not in ("CORE.md", "THEORY.md"))  # not editable here beyond the claims link


def check_direction(root):
    errors = []
    if not os.path.isfile(os.path.join(root, "README.md")):
        return ["direction: README.md missing"]
    text = read(root, "README.md")
    sec = ranked_section(text)
    if sec is None:
        return ["direction: README.md has no '## Ranked gaps' section"]
    # The direction line has one hand-kept copy: README.md.
    copies = [(p, ln) for p in sorted(set(direction_pages(root)) | {"CORE.md", "THEORY.md"})
              if os.path.isfile(os.path.join(root, p))
              for ln, line in enumerate(read(root, p).split("\n"), 1) if DIRECTION_LINE.match(line)]
    if not any(p == "README.md" for p, _ln in copies):
        errors.append("direction: README.md has no dated '**Direction (..., YYYY):**' line")
    if len(copies) > 1:
        errors.append("direction: the direction line has %d copies (%s); keep one, in README.md"
                      % (len(copies), ", ".join("%s:%d" % c for c in copies)))
    rows = [split_cells(l) for l in sec.splitlines() if GAP_ID.match(l) and not l.startswith("| ID ")]
    if not rows:
        errors.append("direction: README.md Ranked gaps has no rows")
    ranked = sorted((int(c[1]), c) for c in rows if len(c) >= 5 and c[1].isdigit())
    for c in rows:
        ident, rank, tag = c[0], c[1] if len(c) > 1 else "", c[2] if len(c) > 2 else ""
        if rank != "parked" and not rank.isdigit():
            errors.append("direction: %s has rank %r; a rank is a number or 'parked'" % (ident, rank))
        if rank.isdigit() and (ident in PARKED_IDS or tag == "data"):
            errors.append("direction: %s is parked work (tag %s) but has rank %s" % (ident, tag, rank))
        if rank == "parked" and not (re.search(r"\bRestart:", c[-1]) and re.search(r"\bdecider:\s*\w", c[-1], re.I)):
            errors.append("direction: parked row %s needs 'Restart: ...' and 'decider: ...'" % ident)
    for ident in PARKED_IDS - {c[0] for c in rows if len(c) > 1 and c[1] == "parked"}:
        errors.append("direction: %s must stay in README.md Ranked gaps as parked" % ident)
    if ranked and ranked[0][1][2] != "math":
        errors.append("direction: rank 1 (%s) is tagged %s, not math" % (ranked[0][1][0], ranked[0][1][2]))
    # no other page ranks or orders real-system work
    for path in direction_pages(root):
        body = read(root, path)
        if path == "README.md":
            body = body.replace(sec, "\n" * sec.count("\n"))
        for ln, line in enumerate(body.split("\n"), 1):
            if line.startswith("|") and not REAL_IDS.search(line.split("|")[1] if line.count("|") > 1 else ""):
                cells = line
            else:
                cells = line
            if PARKED_OK.search(cells):
                continue
            if (REAL_IDS.search(cells) and ORDER.search(cells)) or (re.search(r"\bin parallel\b", cells, re.I) and REAL_WORK.search(cells)):
                errors.append("direction: %s:%d orders real-system work outside README.md Ranked gaps: %s"
                              % (path, ln, cells.strip()[:120]))
    return errors


# ------------------------------------------------------------------ work rows have one home (README.md)
WORK_SECTIONS = ("## Ranked gaps", "## Waiting on Chad", "## Open, not ranked")
HIST_BLOCK = re.compile(r"<!-- history:begin.*?<!-- history:end -->", re.S)


def work_ids(root):
    """IDs of the README.md ranked-gaps, Waiting-on-Chad, and Open-not-ranked rows."""
    text = read(root, "README.md") if os.path.isfile(os.path.join(root, "README.md")) else ""
    ids = set()
    for head in WORK_SECTIONS:
        m = re.search("^" + re.escape(head) + r".*", text, re.M | re.S)
        if not m:
            continue
        for line in m.group(0).split("\n## ", 1)[0].splitlines():
            c = split_cells(line) if line.startswith("|") else []
            if c and c[0] and c[0] not in ("ID",) and not set(c[0]) <= set("-: "):
                ids.add(c[0].strip("*` "))
    return ids


def check_work_rows(root):
    """A README work row ID used as a table row or an ordered-list item on another page fails.
    measurement/CLAIM_MAP_v2.md and THEORY.md Appendix C are exempt: they index claim statuses under the
    same IDs, not work."""
    ids = work_ids(root)
    if not ids:
        return []
    alt = "|".join(sorted(map(re.escape, ids), key=len, reverse=True))
    row = re.compile(r"^\|\s*[*`]*(%s)[*`]*\s*\|" % alt)
    # an ordered item that names the ID as its label: "3. **T40**", "3. T40:", "3. **T40 —", "1. **BICAUSAL.**"
    item = re.compile(r"^\s*\d+[.)]\s+[*`]*(%s)(?:[*`.]+|\s*[:|\u2014\u2013]|\s+-\s)" % alt)
    errors = []
    pages = sorted((set(direction_pages(root)) | {"CORE.md", "THEORY.md"}) - {"README.md", "measurement/CLAIM_MAP_v2.md"})
    for path in pages:
        if not os.path.isfile(os.path.join(root, path)):
            continue
        body = HIST_BLOCK.sub(lambda m: "\n" * m.group(0).count("\n"), read(root, path))
        if path == "THEORY.md" and "## Appendix C" in body:
            body = body.split("## Appendix C", 1)[0]  # Appendix C indexes claim statuses, like the ledger
        for ln, line in enumerate(body.split("\n"), 1):
            m = row.match(line) or item.match(line)
            if m:
                errors.append("work rows: %s:%d lists README work row %s; README.md holds it" % (path, ln, m.group(1)))
    return errors


# ------------------------------------------------------------------ summaries
SURFACE = {
    "proved-in-model": r"proved-in-model|PROVED \(in-model\)|proved \(in-model\)|proved in-model|proved in (?:the |a )?models?"
                       r"|proved in (?:its|their|the) (?:named |stated )?class(?:es)?",
    "known": r"known", "open": r"open", "false": r"false", "hypothesis": r"hypothesis",
    "interpretation": r"interpretation", "conjecture": r"conjecture", "synthesis": r"synthesis",
}
# A claim is judged when a status or outcome phrase follows its ID in the same clause ("T61 holds", "T49 stays open").
JUDGE_NEAR = re.compile(r"^[^.;]{0,50}?\b(?:(?:is|are|was|were|stays?|remains?|becomes?|became|now|still)\s+(?:now\s+|still\s+|only\s+)?"
                        r"(?:proved|proven|open|known|false|true|settled|established|refuted|confirmed|falsified|wrong|correct|"
                        r"shown|closed)|holds|fails|failed|works|survives|survived)\b", re.I)
WHOLE = [
    re.compile(r"\b(?:the|this|our|GTAO(?:'s)?)\s+theory\s+(?:is|was|looks|seems|appears|has been|stands|holds up)\b[^.\n]{0,60}?"
               r"\b(?:promising|strong|stronger|weak|weaker|wrong|right|correct|true|false|confirmed|refuted|validated|"
               r"vindicated|falsified|on track|in trouble|working|failing|broken|sound|successful|a success|a failure|"
               r"good|bad|robust|fragile|universal|supported|unsupported)\b", re.I),
    re.compile(r"\b(?:the|this|our|GTAO(?:'s)?)\s+theory\s+(?:fails|failed|works|worked|succeeds|succeeded)\b", re.I),
    re.compile(r"\b(?:GTAO|the theory)\s+(?:is|was)\s+(?:confirmed|refuted|validated|falsified|vindicated|supported)\b", re.I),
    re.compile(r"\b(?:GTAO|the theory)\b[^.\n]{0,40}\b(?:nothing|no)\s+(?:\w+\s+)?(?:confirmed|refuted|validated|falsified)\b", re.I),
    re.compile(r"\bthe theory-specific structure (?:failed|fails|held|holds|works|worked)\b", re.I),
]
CONDITIONAL = re.compile(r"\b(?:if|whether|unless|would)\b", re.I)
REACH = re.compile(r"\b(?:the theory|GTAO)(?:'s)?\s+(?:reach|prospects|promise|value|future)\s+(?:is|are|grows|grew|extends|widens|"
                   r"narrows|shrinks|looks|improves|improved|now)\b"
                   r"|\bwhat (?:this|the|a) (?:test|result|miss|hit|run) (?:means|says) (?:for|about) (?:the theory|GTAO)\b", re.I)
QUOTED = re.compile(r"`[^`]*`|\"[^\"\n]*\"|“[^”\n]*”|'[^'\n]{3,}'")


def _sentences(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    for para in text.split("\n"):
        if para.lstrip().startswith(">") or para.lstrip().startswith("|"):
            continue  # quotes, and table rows (the row-by-row form)
        for s in re.split(r"(?<=[.!?])\s+", QUOTED.sub(" ", para)):
            if s.strip():
                yield s.strip()


def summary_fails(text, root=None, where="text", status=None):
    """Failure strings for summary sentences in text (a PR body or added Markdown lines).

    1. A whole-theory judgment ('the theory works', 'the theory is promising', ...) fails.
    2. A sentence on the theory's reach or prospects must name a ledger row with its exact status.
    3. A sentence that judges a ledger claim ("T61 holds", "T49 stays open") must quote that row's exact
       ledger status, or be a table row (the row-by-row form).
    status: {id: ledger status}; default is the ledger in root.
    """
    if status is None:
        rows, _r, _e = parse_ledger(read(root or repo_root(), "measurement/CLAIM_MAP_v2.md"))
        status = {r["id"]: r["status"] for r in rows}
    idrx = re.compile(r"(?<![A-Za-z0-9-])(" + "|".join(sorted(map(re.escape, status), key=len, reverse=True)) + r")(?![A-Za-z0-9-])")
    out = []
    for s in _sentences(text):
        if any(rx.search(s) for rx in WHOLE) and not CONDITIONAL.search(s):
            out.append("%s: whole-theory judgment; report row by row against named rivals: %s" % (where, s[:140]))
            continue
        found = list(idrx.finditer(s))
        exact = {m.group(1) for m in found if re.search(r"(?<![\w-])(?:%s)(?![\w-])" % SURFACE.get(status[m.group(1)], "$^"), s, re.I)}
        # "T57's loophole stays open" judges the loophole, not T57
        judged = {m.group(1) for m in found if not re.match(r"['’]s\b", s[m.end():]) and JUDGE_NEAR.search(s[m.end():])}
        if REACH.search(s) and not exact:
            out.append("%s: judges the theory's reach without a ledger row and its exact status: %s" % (where, s[:140]))
        elif judged - exact and not CONDITIONAL.search(s):
            miss = sorted(judged - exact)
            out.append("%s: judges %s without its exact ledger status (%s): %s"
                       % (where, ", ".join(miss), "; ".join("%s is %s" % (i, status[i]) for i in miss), s[:140]))
    return out


def ledger_status(text):
    rows, _r, _e = parse_ledger(text)
    return {r["id"]: r["status"] for r in rows}


def check_summaries(root):
    """summary_fails on Markdown lines added since origin/main, outside reference/ (archived copies) and locked files."""
    import banned_words
    base = banned_words.base_ref(root)
    added = banned_words.added_lines(root, base) if base else None
    if not added:
        return []
    locked = banned_words.locked_paths(root)
    out = []
    for path, lines in sorted(added.items()):
        if path.startswith("reference/") or path in locked:
            continue
        for ln, line in lines:
            out += ["summary: " + x for x in summary_fails(line, root, "%s:%d" % (path, ln))]
    return out


def check(root=None):
    """Return a list of failure strings (empty means pass)."""
    root = root or repo_root()
    cm_path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
    if not os.path.isfile(cm_path):
        return ["claims: measurement/CLAIM_MAP_v2.md missing"]
    text = read(root, "measurement/CLAIM_MAP_v2.md")
    rows, rules, errors = parse_ledger(text)
    if not rows:
        return errors
    errors.extend(check_sources(rows, root))
    errors.extend(check_edges(rows, claim_ids(text)))
    errors.extend(check_views(rows, root))
    errors.extend(check_rules(rules, rows, root))
    errors.extend(check_hypothesis(root))
    errors.extend(check_unmanaged(rows, root, claim_ids(text)))
    errors.extend(check_direction(root))
    errors.extend(check_work_rows(root))
    errors.extend(check_summaries(root))
    # de-duplicate, keep order
    out, seen = [], set()
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def main(argv=None):
    argv = sys.argv if argv is None else argv
    if "--write" in argv:
        print("claims views are retired: front pages link to measurement/CLAIM_MAP_v2.md; nothing to write")
        return 2
    if "--summary" in argv:
        f = argv[argv.index("--summary") + 1]
        fails = summary_fails(open(f, encoding="utf-8").read(), None, f)
        for x in fails:
            print("  FAIL " + x)
        print("RESULT:", "FAIL" if fails else "PASS")
        return 1 if fails else 0
    root = argv[1] if len(argv) > 1 else repo_root()
    fails = check(root)
    if fails:
        for f in fails:
            print("  FAIL " + f)
        print("RESULT: FAIL")
        return 1
    print("claims: ledger, links, sources, edges, hypothesis, direction: OK")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
