#!/usr/bin/env python3
"""Fail if a maintained page hand-keeps a fact that has another single source.

Since 25 November 2026 no page carries the current `main` SHA, the open-PR list
or a PR head: those change at every merge or push, so a committed copy is stale
as soon as it lands. `tools/brief.py` prints them live. Versions have one source
(the THEORY.md title, the latest CLAIM_MAP note) and the Lean total has one
(formal/lean/AUDIT.json).

What fails, on every maintained page (check_consistency.MAINTAINED_DOCS, every
root .md, process/*.md, formal/lean/README.md):
  - any SHA that is a prefix of one of the last RECENT first-parent commits of
    `main`, in any wording, unless it sits in a history block or right after
    "merged as";
  - any SHA that is the head of an open PR (the live list from
    check_pending.open_pr_heads), in any wording, unless it sits in a history block;
  - the pointer wordings in RULES (they also work with no git history or network),
    including hand-typed PR heads ("head `sha`", "PR #N (head", "is at sha",
    "tip: sha") and Lean declaration totals;
  - a root .md file outside ROOT_ALLOW, and a STATUS.md or OPEN_WORK.md in any
    folder (a status page or work list that comes back);
  - a line that starts with `<!-- history:begin` in README.md, CORE.md, THEORY.md
    or process/PROCESS.md (those pages do not keep a history block; a mid-line
    quote of the marker still passes).
Without network the open-PR head rule is skipped and the result is PARTIAL.
Text between `<!-- history:begin` and `<!-- history:end -->` is a dated record
and is skipped, as are the copies in files this repo may not edit (ALLOW).

Run from the repo root:  python3 tools/check_fresh.py
Exit 0 = no hand pointer. Exit 1 = at least one.
"""
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_consistency import MAINTAINED_DOCS  # noqa: E402

ROOT_ALLOW = {"README.md", "CORE.md", "THEORY.md"}
EXTRA = ["formal/lean/README.md", "applications/README.md"]
LIVE_GLOBS = ["*.md", "process/*.md"]
# Every maintained page is scanned. Dated entries in append-only pages sit inside history blocks.
SKIP = set()
BANNED_NAMES = {"STATUS.md", "OPEN_WORK.md"}
RECENT = 50
SHA = r"`?[0-9a-f]{7,40}\b`?"
HEX = re.compile(r"(?<![0-9A-Za-z/#])([0-9a-f]{7,40})(?![0-9A-Za-z])")
MERGED_AS = re.compile(r"merged\s+as\s*`?$", re.I)
# "on/beside `main` `SHA`" is a pointer only in an As-of header; table rows use the words historically.
ASOF = re.compile(r"^\*\*As of:\*\*.*(?:\n(?!\n|#|\|).*)*", re.M)
ASOF_SHA = re.compile(r"(?:on|beside)\s+`main`\s+`[0-9a-f]{7,40}`", re.I)
RULES = [
    ("main SHA pointer", re.compile(
        r"`main`\s+is\s+" + SHA + r"|\bmain\s+is\s+" + SHA
        + r"|current to\s+`?\bmain\b`?\s+" + SHA
        + r"|\b(?:current|latest)\s+`?(?:main|merge|head)`?\s*(?:is|:)?\s*" + SHA
        + r"|\bas\s+of\s+`?(?:main|head)`?\s*(?:is|at|:)?\s*" + SHA
        + r"|\bHEAD\s+(?:is|at|:)\s*" + SHA
        + r"|\bmain\s+(?:has\s+)?moved\s+to\s+" + SHA, re.I)),
    ("open-PR list", re.compile(r"\bopen\s+(?:upstream\s+|fork\s+)?(?:PRs?|pull requests?)\b[^.\n]{0,40}?:\s*(?:PR\s*)?#\d+", re.I)),
    ("PR head", re.compile(r"\bhead\s+`[0-9a-f]{7,40}`|\bPR\s*#\d+\s*\(head\b"
                           r"|\bis\s+(?:now\s+)?at\s+`?[0-9a-f]{7,40}\b|\btip\s*(?:is|:)\s*`?[0-9a-f]{7,40}\b", re.I)),
    ("version string", re.compile(r"`?THEORY(?:\.md)?`?\s*\(?v\d+\.\d+(?:\.\d+)?[a-z]?\s+draft|`THEORY\.md`\s+v\d+\.\d+"
                                  r"|CLAIM_MAP_v2\.md`?\s*\(v2\.\d+|\(v\d+\.\d+(?:\.\d+)?[a-z]?\s+draft\)")),
    ("Lean total", re.compile(r"\*\*\d[\d,]*\s+declarations\*\*|machine-checks\s+\**\d[\d,]*"
                              r"|\b\d[\d,]*\s+(?:Lean\s+)?declarations\b", re.I)),
]
# Copies in files that may not be edited here; check_consistency.py keeps them equal to their source.
ALLOW = {
    ("CORE.md", "is the canonical statement (v"),
    ("THEORY.md", "Claim statuses: `measurement/CLAIM_MAP_v2.md` (v"),
    # A ledger row that dates a past booking to THEORY v2.0; ledger wording is not edited here.
    ("measurement/CLAIM_MAP_v2.md", "the booking is now fixed** (`THEORY.md` v2.0 §2)"),
}
HIST = re.compile(r"<!-- history:begin.*?<!-- history:end -->", re.S)
# These four pages do not keep a history block. A line that starts with the marker fails.
# A mid-line quote (process/PROCESS.md names the marker inside backticks) still passes.
NO_HIST_BLOCK = {"README.md", "CORE.md", "THEORY.md", "process/PROCESS.md"}
HIST_BEGIN = "<!-- history:begin"


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def live_pages(root):
    pages = [p for p in list(MAINTAINED_DOCS) + EXTRA if os.path.isfile(os.path.join(root, p))]
    for g in LIVE_GLOBS:
        pages += sorted(os.path.relpath(p, root) for p in glob.glob(os.path.join(root, g)))
    seen, out = set(), []
    for p in pages:
        if p not in seen and p not in SKIP:
            seen.add(p)
            out.append(p)
    return out


def recent_main(root, n=RECENT):
    """Full SHAs of the last n first-parent commits of main (empty without git)."""
    for ref in ("origin/main", "upstream/main", "main", "HEAD"):
        try:
            r = subprocess.run(["git", "-C", root, "rev-list", "--first-parent", "-n", str(n), ref],
                               capture_output=True, text=True, timeout=30)
        except (OSError, subprocess.SubprocessError):
            return []
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.split()
    return []


def hand_pointers(text, path="", recent=(), heads=None):
    """[(line number, rule, excerpt)] for hand-kept live facts in text."""
    text = HIST.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        allowed = any(path == p and frag in line for p, frag in ALLOW)
        hit = False
        for name, rx in RULES:
            m = rx.search(line)
            if not m or allowed:
                continue
            if name == "main SHA pointer" and MERGED_AS.search(line[:m.start()]):
                continue
            hit = True
            out.append((i, name, line[max(0, m.start() - 30):m.end() + 30].strip()))
        if hit or allowed:
            continue
        for m in HEX.finditer(line):
            tok = m.group(1)
            pr = next((v for k, v in (heads or {}).items() if k.startswith(tok)), None)
            if pr:
                out.append((i, "open PR head (%s)" % pr, line[max(0, m.start() - 30):m.end() + 30].strip()))
                hit = True
                break
        if hit or not recent:
            continue
        for m in HEX.finditer(line):
            tok = m.group(1)
            if MERGED_AS.search(line[:m.start()]):
                continue
            if any(full.startswith(tok) for full in recent):
                out.append((i, "recent main SHA", line[max(0, m.start() - 30):m.end() + 30].strip()))
                break
    for para in ASOF.finditer(text):
        for m in ASOF_SHA.finditer(para.group(0)):
            out.append((text.count("\n", 0, para.start() + m.start()) + 1, "main SHA pointer", m.group(0)))
    return sorted(set(out))


def banned_pages(root):
    """STATUS.md or OPEN_WORK.md anywhere in the tree (not under .git)."""
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        out += [os.path.relpath(os.path.join(dirpath, f), root) for f in filenames if f in BANNED_NAMES]
    return sorted(out)


def stray_root_pages(root):
    return sorted(os.path.basename(p) for p in glob.glob(os.path.join(root, "*.md"))
                  if os.path.basename(p) not in ROOT_ALLOW)


def check(root=None, recent=None, heads=None):
    """Failure strings. heads: {open-PR head SHA: label}; None or {} skips that rule (main() fetches it)."""
    root = root or repo_root()
    recent = recent_main(root) if recent is None else list(recent)
    fails = []
    for p in banned_pages(root):
        fails.append("%s is a retired page name; status and open work live in README.md" % p)
    for p in stray_root_pages(root):
        fails.append("root page %s is not in the allow-list %s; status and open work live in README.md"
                     % (p, sorted(ROOT_ALLOW)))
    for p in live_pages(root):
        with open(os.path.join(root, p), encoding="utf-8") as fh:
            text = fh.read()
        if p in NO_HIST_BLOCK:
            for i, line in enumerate(text.split("\n"), 1):
                if line.startswith(HIST_BEGIN):
                    fails.append("history block at %s:%d: a line starts with <!-- history:begin; "
                                 "README.md, CORE.md, THEORY.md and process/PROCESS.md do not keep one" % (p, i))
        for ln, name, ex in hand_pointers(text, p, recent, heads):
            fails.append("hand pointer (%s) at %s:%d: %s; read it live or from its one source" % (name, p, ln, ex))
    return fails


def live_heads(offline=False):
    """({sha: label}, note). note is a string when the live list could not be read."""
    if offline:
        return {}, "open-PR head rule not run (--offline)"
    import check_pending
    try:
        return check_pending.open_pr_heads(), None
    except check_pending.Offline as e:
        return {}, "open-PR head rule not run (%s)" % e


def main(argv=None):
    """Exit 0 = PASS (or PARTIAL with --offline), 1 = FAIL, 2 = PARTIAL that was not asked for."""
    argv = sys.argv if argv is None else argv
    offline = "--offline" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    heads, note = live_heads(offline)
    fails = check(args[0] if args else None, heads=heads)
    for f in fails:
        print("  FAIL " + f)
    if note:
        print("  PARTIAL " + note)
    else:
        print("  open-PR heads checked: %d" % len(heads))
    if fails:
        print("RESULT: FAIL")
        return 1
    if note:
        print("RESULT: PARTIAL (not everything was checked)")
        return 0 if offline else 2
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
