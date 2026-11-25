#!/usr/bin/env python3
"""Verify the repository's hash locks and account for every one that does not verify.

Read-only. It never edits a locked file. Added 24 November 2026 (process/LOCK_ERRATA.md).

A lock file is any `*.sha256`, `SHA256SUMS*` or `LOCK*.txt` whose lines are
`<64 hex>  <path>`. For each line this script computes the sha256 of the
tracked file and puts the line in one class:

  OK          the file hashes to the locked value;
  SCRUB       the file differs only by the public-readiness scrub `d513528`
              (18 November 2026), which replaced box paths: `<local>` stands
              for `/workspace`, `<repo>` for `/workspace/theory-of-adaptive-organization`.
              The script PROVES this by reversing the substitution in memory
              and checking that the locked hash comes back;
  POST_LOCK   the file was changed after the lock, by a commit named in
              process/LOCK_ERRATA.md. With git history the script finds the
              lock-time blob and confirms it hashes to the locked value;
  UNVERIFIABLE no committed version, with or without the reverse
              substitution, hashes to the locked value;
  MISSING     the locked file is raw external data that was never committed.

The expected members of every class except OK are pinned below, and the current
git blob of each file that no lock covers (stores.py, F1 outcome.py, glucose
analyze.py) is pinned too, so a later edit to one of them fails. The script
fails if a lock stops verifying that is not pinned, if a pinned SCRUB file no
longer reverses, or if a count changes. New locks that verify (OK) are free.

Not scanned (disclosed in process/LOCK_ERRATA.md): lock files whose lines are a bare
hash with no path, and prose locks written as "sha256: ...". Only `hex  path` lines count.

Run from the repo root:  python3 tools/verify_locks.py [-v]
Exit 0 = every lock is OK or accounted for in process/LOCK_ERRATA.md.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCK_FILE_RE = re.compile(r"(\.sha256|SHA256SUMS[^/]*|LOCK[^/]*\.txt)$")
LINE_RE = re.compile(r"^\s*([0-9a-f]{64})\s+\*?(\S.*?)\s*$")
SKIP_DIRS = {".git", ".lake", "lake-packages", "node_modules", "__pycache__"}

SCRUB_MAP = ((b"<repo>", b"/workspace/theory-of-adaptive-organization"), (b"<local>", b"/workspace"))

# Pinned: files whose lock verifies only after reversing the scrub (13).
SCRUB = {
    "prereg/WIKIDATA-BAND/PREREG.md", "prereg/vigil-ona/ona_analyze.py",
    "tests/C3b/PREREG_ADDENDUM_A2.md", "tests/C3b/PREREG_ADDENDUM_A3.md",
    "tests/DECISIVE/banks/PREREG.md",
    "tests/F1/code/analyze.py", "tests/F1/code/analyze_E.py", "tests/F1/code/build_dataset.py",
    "tests/F1/code/covid.py", "tests/F1/code/extract.py", "tests/F1/code/measures.py",
    "tests/F1/code/power.py", "tests/F1/code/sim_dataset.py",
}
# Pinned: changed after the lock. path -> (lock-time commit, lock-time blob, later commit, later blob)
POST_LOCK = {
    "night2/GITHUB/code/pull.py": ("86aa1cc", "44563ed734645b4a9ca649b99663b898897ed4fc", "d9152f2", "ee4f718e0f63121508916eab14d979e9c09b0fe6"),
    "theory/layers_checks/stores.py": ("e50e92f", "c7c1e06bc098e40c2395ef94b4d1a953243a020a", "a1a98aa", "71a113e05eab9f62b70cedbfcf27f0d698bc2f92"),
}
# Pinned: no committed version matches.
UNVERIFIABLE = {"tests/DECISIVE/glucose/code/analyze.py", "tests/F1/code/outcome.py"}
# Pinned: the current git blob of every file whose lock does not verify and whose bytes are not themselves
# locked by another hash. Without this, a later edit to these three files would go unnoticed.
CURRENT_BLOB = {
    "theory/layers_checks/stores.py": "71a113e05eab9f62b70cedbfcf27f0d698bc2f92",
    "tests/F1/code/outcome.py": "3126c5e00f096ce7632f4ea18557fc9b1e734ed5",
    "tests/DECISIVE/glucose/code/analyze.py": "1c9a5051eeb9e058da452ed3a5b86fb0ca4f5e4b",
}
# Pinned: locked files that are raw external data and were never committed, by lock file.
MISSING = {
    "night2/GITHUB/data/SHA256SUMS": 5,
    "prereg/SENSE-CELL/data/SHA256SUMS": 1,
    "prereg/WIKIDATA-BAND/data/SHA256SUMS": 2,
    "prereg/vigil-ona/SHA256SUMS_raw.txt": 30,
    "tests/F1/raw/companyfacts.sha256": 1,
    "tests/F1/raw/submissions.sha256": 1,
    "theory/measured/ecoli/LOCK.txt": 2,
}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def git_blob(b):
    """The git blob id of these bytes (what `git hash-object` prints)."""
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def unscrub(b):
    for a, c in SCRUB_MAP:
        b = b.replace(a, c)
    return b


def lock_files(root):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if LOCK_FILE_RE.search(f):
                yield os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")


def entries(root):
    """[(lock_file, target_path_or_None, locked_hash, target_rel)] for every hash line."""
    out = []
    for lf in sorted(lock_files(root)):
        text = open(os.path.join(root, lf), encoding="utf-8", errors="replace").read()
        d = os.path.dirname(lf)
        for line in text.splitlines():
            m = LINE_RE.match(line)
            if not m:
                continue
            hx, p = m.groups()
            p = p[2:] if p.startswith("./") else p
            cands = [os.path.normpath(os.path.join(d, p)).replace(os.sep, "/"), os.path.normpath(p).replace(os.sep, "/")]
            hit = next((c for c in cands if os.path.isfile(os.path.join(root, c))), None)
            out.append((lf, hit, hx, cands[0]))
    return out



def commit_matches(pin, names):
    """True if `pin` (a possibly short hash) names one of the commits in `names`."""
    pin = (pin or "").lower()
    return any(c.lower().startswith(pin) or pin.startswith(c.lower()) for c in names if c)


def git_history_sha256(root, path):
    """{commit sha: sha256} for every committed version of path, or None without history."""
    if not os.path.exists(os.path.join(root, ".git")):
        return None
    r = subprocess.run(["git", "log", "--all", "--format=%H", "--", path], cwd=root, capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.split():
        return None
    out = {}
    for c in r.stdout.split():
        b = subprocess.run(["git", "show", "%s:%s" % (c, path)], cwd=root, capture_output=True)
        if b.returncode == 0:
            out[c] = sha256(b.stdout)
    return out


def verify(root=ROOT, history=True, scrub=None, post=None, unverifiable=None, missing_pin=None, blobs=None):
    """(fails, counts, notes). The pins default to the module's tables."""
    scrub = SCRUB if scrub is None else scrub
    post = POST_LOCK if post is None else post
    unverifiable = UNVERIFIABLE if unverifiable is None else unverifiable
    missing_pin = MISSING if missing_pin is None else missing_pin
    blobs = CURRENT_BLOB if blobs is None else blobs
    fails, notes = [], []
    counts = {"OK": 0, "SCRUB": 0, "POST_LOCK": 0, "UNVERIFIABLE": 0, "MISSING": 0}
    missing = {}
    seen_scrub, seen_post, seen_unv, seen_later = set(), set(), set(), set()
    for lf, hit, hx, target in entries(root):
        if hit is None:
            missing[lf] = missing.get(lf, 0) + 1
            counts["MISSING"] += 1
            continue
        b = open(os.path.join(root, hit), "rb").read()
        if hit in blobs and hit not in scrub and git_blob(b) != blobs[hit]:
            fails.append("locks: %s changed since it was pinned (git blob %s, now %s); it is outside every lock, so any edit needs a new entry in process/LOCK_ERRATA.md and here" % (hit, blobs[hit][:8], git_blob(b)[:8]))
        # Always check the declared later blob, even when this clone has no lock-time history
        # (B-281-1: a shallow clone must still catch a tamper of pull.py).
        if hit in post and hit not in seen_later:
            seen_later.add(hit)
            want = post[hit][3] if len(post[hit]) > 3 else None
            if want and git_blob(b) != want:
                fails.append("locks: %s changed since the declared later version (git blob %s, now %s)" % (hit, want[:8], git_blob(b)[:8]))
        if sha256(b) == hx:
            counts["OK"] += 1
        elif hit in scrub:
            if sha256(unscrub(b)) == hx:
                counts["SCRUB"] += 1
                seen_scrub.add(hit)
            else:
                fails.append("locks: %s was pinned as scrub-only but reversing the substitution no longer gives the locked hash" % hit)
        elif hit in post:
            counts["POST_LOCK"] += 1
            seen_post.add(hit)
            h = git_history_sha256(root, hit) if history else None
            if h is None:
                notes.append("post-lock history for %s not checked (no git history)" % hit)
            else:
                matching = [c for c, v in h.items() if v == hx]
                if commit_matches(post[hit][0], matching):
                    pass
                elif commit_matches(post[hit][0], h):
                    fails.append("locks: %s: commit %s is in history but does not hash to the locked value" % (hit, post[hit][0]))
                else:
                    notes.append("post-lock history for %s: lock-time commit %s is not in this clone; the erratum in process/LOCK_ERRATA.md still stands" % (hit, post[hit][0]))
        elif hit in unverifiable:
            counts["UNVERIFIABLE"] += 1
            seen_unv.add(hit)
        else:
            fails.append("locks: %s (locked in %s) does not match its hash and is not accounted for in process/LOCK_ERRATA.md" % (hit, lf))
    for name, want, seen in (("scrub-only", set(scrub), seen_scrub), ("post-lock", set(post), seen_post),
                             ("unverifiable", set(unverifiable), seen_unv)):
        for g in sorted(want - seen):
            if os.path.isfile(os.path.join(root, g)):
                fails.append("locks: pinned %s file %s now verifies or lost its lock line; update tools/verify_locks.py and process/LOCK_ERRATA.md" % (name, g))
    if missing != missing_pin:
        fails.append("locks: locked-but-uncommitted files changed: pinned %s, found %s" % (missing_pin, missing))
    return fails, counts, notes


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    fails, counts, notes = verify(ROOT)
    print("locks: %(OK)d OK; %(SCRUB)d scrub-only (proved by reversing the substitution); %(POST_LOCK)d changed after the lock (declared); "
          "%(UNVERIFIABLE)d unverifiable; %(MISSING)d raw data never committed" % counts)
    for n in notes:
        print("  note: " + n)
    for f in fails:
        print("  FAIL " + f)
    print("RESULT:", "FAIL" if fails else "PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
