#!/usr/bin/env python3
"""Banned-word lint for maintained docs and for every line a change adds (stdlib only).

Words: puzzle, bill, kill, dead, verdict (and their plain forms: puzzles, bills,
billed, billing, kills, killed, killing, verdicts). GTAO says miss, cost, open
question, result, and outcome instead (process/PROCESS.md section 2).

Two checks, both run from tools/check_consistency.py:

  A. `puzzle` anywhere in a maintained doc fails (the maintained docs are clean
     after the 24 November 2026 sweep);
  B. any line ADDED to a `.md` file, compared with `origin/main`, that contains one
     of the five words fails. Old lines are not rescanned (many dated records
     use "kill rule" as a locked-test term); a changed line counts as added.

Locked files are never edited to satisfy this lint. A path is skipped, while its bytes are
unchanged, if (1) a hash-lock line (`<sha256>  <path>` in a *.sha256, SHA256SUMS* or
LOCK*.txt file) names it and the file still hashes to that value (or to it after the
public-readiness scrub is reversed), or (2) process/LOCKED_BLOBS.txt, read from
origin/main, lists its path and current git blob id
(for files locked by commit order, not by hash). A new line in that file only
takes effect after it is on main, so a PR cannot add an exemption and a banned
word in the same change. Edit a locked file and the exemption ends.

Exempt: text inside backticks, straight double quotes or curly quotes (the word is
quoted, not used); a line with `<!-- banned-ok: reason -->` (reviewable escape);
and, in process/PROCESS.md, process/VOCABULARY.md and process/FAILURES.md only,
table rows, lines that list two or more of the words, and lines that say the
word is banned.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys

WORD = re.compile(r"\b(puzzles?|bills?|billed|billing|kill(?:s|ed|ing)?|dead|verdicts?)\b", re.I)
PUZZLE = re.compile(r"\bpuzzles?\b", re.I)
QUOTED = re.compile(r"`[^`]*`|\"[^\"]*\"|“[^”]*”|‘[^’]*’")
ESCAPE = re.compile(r"<!--\s*banned-ok:\s*\S.*?-->")
RULE_FILES = {"process/PROCESS.md", "process/VOCABULARY.md", "process/FAILURES.md"}
RULE_SAYS = re.compile(r"\b(banned|bans?|never say|do not say|don't say|not say|wording rule|no \w+ wording)\b", re.I)


def unquoted(line):
    return QUOTED.sub(" ", line)


def hits(line, path=""):
    """The banned words used (not quoted) on this line, or []."""
    if ESCAPE.search(line):
        return []
    found = [m.group(0).lower() for m in WORD.finditer(unquoted(line))]
    if not found:
        return []
    if path in RULE_FILES:
        distinct = {re.sub(r"(s|ed|ing)$", "", f) for f in found}
        if line.lstrip().startswith("|") or len(distinct) >= 2 or RULE_SAYS.search(line):
            return []
    return found


def puzzle_hits(line, path=""):
    if ESCAPE.search(line):
        return []
    if path in RULE_FILES and (line.lstrip().startswith("|") or RULE_SAYS.search(line)):
        return []
    return [m.group(0).lower() for m in PUZZLE.finditer(unquoted(line))]


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def base_ref(root):
    """origin/main if present, else None (shallow or detached checkouts)."""
    r = git(root, "rev-parse", "--verify", "-q", "origin/main")
    return "origin/main" if r.returncode == 0 else None


def added_lines(root, base):
    """{path: [(lineno, text)]} for .md lines added or changed since the merge base with `base`,
    including uncommitted edits."""
    mb = git(root, "merge-base", "HEAD", base)
    if mb.returncode != 0:
        return None
    r = git(root, "diff", "-U0", "--no-color", mb.stdout.strip(), "--", "*.md")
    if r.returncode != 0:
        return None
    out, path, ln = {}, None, 0
    for line in r.stdout.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif line.startswith("@@"):
            m = re.match(r"@@ -\S+ \+(\d+)", line)
            ln = int(m.group(1)) if m else 0
        elif line.startswith("+") and not line.startswith("+++") and path:
            out.setdefault(path, []).append((ln, line[1:]))
            ln += 1
    return out


LOCKED_BLOBS = "process/LOCKED_BLOBS.txt"


def parse_blob_list(text):
    """{path: blob id} from the contents of LOCKED_BLOBS.txt."""
    out = {}
    for line in (text or "").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 2)
        if len(parts) >= 3 and re.fullmatch(r"[0-9a-f]{40}", parts[1]):
            out[parts[0]] = parts[1]
    return out


def blob_list_ref(root):
    """origin/main if that ref exists, else None.

    There is no merge-base fallback: if origin/main is missing,
    `git merge-base HEAD origin/main` also fails.
    """
    if git(root, "rev-parse", "--verify", "-q", "origin/main").returncode == 0:
        return "origin/main"
    return None


def blob_list(root, ref=None):
    """{path: blob id} from process/LOCKED_BLOBS.txt at origin/main, not the working tree.

    A new exemption only takes effect after it is on main.
    """
    ref = ref or blob_list_ref(root)
    if not ref:
        return {}
    r = git(root, "show", "%s:%s" % (ref, LOCKED_BLOBS))
    if r.returncode != 0:
        return {}
    return parse_blob_list(r.stdout)


LOCK_FILE_RE = re.compile(r"(\.sha256|SHA256SUMS[^/]*|LOCK[^/]*\.txt)$")
LOCK_LINE_RE = re.compile(r"^\s*([0-9a-f]{64})\s+\*?(\S.*?)\s*$")
SKIP_DIRS = {".git", ".lake", "node_modules", "__pycache__"}
SCRUB_MAP = ((b"<repo>", b"/workspace/theory-of-adaptive-organization"), (b"<local>", b"/workspace"))


def git_blob(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def locked_paths(root):
    """Paths that are locked and whose bytes still match their lock (hash lines or the blob list).
    Same reading of lock files as tools/verify_locks.py."""
    exempt = set()
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not LOCK_FILE_RE.search(f):
                continue
            lf = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")
            d = os.path.dirname(lf)
            for line in open(os.path.join(root, lf), encoding="utf-8", errors="replace"):
                m = LOCK_LINE_RE.match(line)
                if not m:
                    continue
                hx, p = m.groups()
                p = p[2:] if p.startswith("./") else p
                for cand in (os.path.normpath(os.path.join(d, p)).replace(os.sep, "/"), os.path.normpath(p).replace(os.sep, "/")):
                    fp = os.path.join(root, cand)
                    if os.path.isfile(fp):
                        b = open(fp, "rb").read()
                        un = b
                        for x, y in SCRUB_MAP:
                            un = un.replace(x, y)
                        if hashlib.sha256(b).hexdigest() == hx or hashlib.sha256(un).hexdigest() == hx:
                            exempt.add(cand)
                        break
    for path, blob in blob_list(root).items():
        fp = os.path.join(root, path)
        if os.path.isfile(fp) and git_blob(open(fp, "rb").read()) == blob:
            exempt.add(path)
    return exempt


def check_added(root, base=None):
    """(fails, note). note is a string when the comparison could not run."""
    base = base or base_ref(root)
    if base is None:
        return [], "banned-word check on added lines skipped: no origin/main to compare with (run `git fetch origin main`)"
    added = added_lines(root, base)
    if added is None:
        return [], "banned-word check on added lines skipped: could not diff against %s" % base
    fails = []
    locked = locked_paths(root)
    for path, rows in sorted(added.items()):
        if path in locked:
            continue
        for ln, text in rows:
            h = hits(text, path)
            if h:
                fails.append("banned word %s added at %s:%d: %s" % (sorted(set(h)), path, ln, text.strip()[:140]))
    return fails, None


def check_puzzle(root, maintained):
    fails = []
    for p in maintained:
        fp = os.path.join(root, p)
        if not os.path.exists(fp):
            continue
        for i, text in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
            if puzzle_hits(text, p):
                fails.append("puzzle in maintained doc %s:%d: %s" % (p, i, text.strip()[:140]))
    return fails


def main(argv=None):
    """Standalone entry point: both checks (A and B above). Exit 0 = PASS, 1 = FAIL, 2 = PARTIAL."""
    argv = sys.argv if argv is None else argv
    root = argv[1] if len(argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from check_consistency import MAINTAINED_DOCS
    fails = check_puzzle(root, MAINTAINED_DOCS)
    added, note = check_added(root)
    fails += added
    for f in fails:
        print("  FAIL " + f)
    if note:
        print("  PARTIAL " + note)
    print("banned words: maintained docs %d, %d FAIL(s)" % (len(MAINTAINED_DOCS), len(fails)))
    if fails:
        print("RESULT: FAIL")
        return 1
    if note:
        print("RESULT: PARTIAL (not everything was checked)")
        return 2
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
