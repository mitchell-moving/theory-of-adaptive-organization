#!/usr/bin/env python3
"""Mutation test for tools/check_consistency.py: plant known errors in a temp
copy of the maintained docs and confirm each one is caught. Exit 0 = every
planted error was detected and the clean copy passes."""
import os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MUTATIONS = [
    ("README.md", "\n\nN26 OPEN.\n", "N-status"),
    ("README.md", "\n\nGTAO is a universal law of adaptive organization.\n", "law"),
    ("README.md", "\n\nThe MV gates become binding once Chad signs off.\n", "gates-await-sign-off"),
    ("README.md", "\n\nThe MATCH1 measles test passed.\n", "unlabeled field verdict"),
    ("THEORY.md", "\n\nGTAO is a theory of everything.\n", "theory-of-everything"),
    ("README.md", "\n\nGTAO is solved.\n", "solved-claim"),
    ("README.md", "\n\nThe theory is silent on black holes.\n", "stale-scope"),
    ("README.md", "\n\nSee CLAIM_MAP N99.\n", "N-ref"),
    # process rules R1-R5 (reviews/lock_2026-11-18/PROCESS.md)
    ("README.md", "\n\nThe independent review `reviews/reach_2026-11-18/REVIEW.md` passed.\n", "self-review-called-independent"),
    ("README.md", "\n\n| a | b |\n|---|---|\n| x | y | z |\n", "table-cells"),
    ("applications/README.md", "\n\nColonies follow the √N law.\n", "law-named"),
    ("tests/README.md", "\n\nThe repository is private.\n", "stale-private"),
    # added in the independent review of the lock pass (INDEPENDENT_REVIEW.md)
    ("README.md", "\n\nThe lock audit `reviews/lock_2026-11-18/LOCK_AUDIT.md` is an independent review.\n", "self-review-called-independent"),
    ("README.md", "\n\nAn independent hostile referee pass is in `reviews/night2/SCALE_ENDS_REVIEW.md`.\n", "self-review-called-independent"),
    ("README.md", "\n\nSee `reviews/reach_2026-11-18/REVIEW.md`, which is independent.\n", "self-review-called-independent"),
    ("README.md", "\n\nShared trails obey a √N scaling law.\n", "law-named"),
    ("README.md", "\n\nThe repository remains private.\n", "stale-private"),
    # core rules R6-R8 (THEORY v2.0, 19 Nov 2026)
    ("THEORY.md", "\n| CT99 | An unlisted result | §0 | OPEN | CT99 | none |\n", "core-index"),
    ("CORE.md", "\n\n| Way | Pays |\n|---|---|\n| **Keep** (frozen) | Nothing |\n| **Hold** (self-regulating) | A flow |\n", "spine-duplicate"),
]
# (file, text): sentences that must NOT be flagged (known false positives, now fixed)
CLEAN = [
    ("README.md", "\n\nIndependent review 2 superseded the earlier pass in `reviews/reach_2026-11-18/REVIEW.md`.\n"),
    ("README.md", "\n\nInventory pooling follows the square-root law of Maister (1976), which is prior art.\n"),
    ("README.md", "\n\nThe MATCH1 test logged a miss (signed size -0.12, located in proxy MV2).\n"),
    ("README.md", "\n\nA qualifying design outside the band is a miss for that class.\n"),
]
# (file, old text, new text, key): replacements that must be caught
REPLACEMENTS = [
    ("measurement/CLAIM_MAP_v2.md", "| **Total** | **", "| **Total** | **1", "tally"),
    ("THEORY.md", "| CX1 | Theorem P for drifting worlds | §5, §8 | OPEN |", "| CX1 | Theorem P for drifting worlds | §5, §8 | PROVED (in-model) |", "core-index"),
    ("THEORY.md", "| CT15 | The level's technology sets the exponent | §6, Result 4 | MATH-CORRECTED (exponent stands; scope narrowed) | N12 |", "| CT15 | The level's technology sets the exponent | §6, Result 4 | MATH-CORRECTED (exponent stands; scope narrowed) | N13 |", "core-index"),
    ("THEORY.md", "## Appendix A. The model and notation", "## The model and notation", "length"),
]
def run(d):
    r = subprocess.run([sys.executable, os.path.join(d, "tools", "check_consistency.py")], cwd=d, capture_output=True, text=True)
    return r.returncode, r.stdout
def copy():
    d = tempfile.mkdtemp()
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f.endswith((".md", ".py")):
                src = os.path.join(root, f); dst = os.path.join(d, os.path.relpath(src, ROOT))
                os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy(src, dst)
    return d
def run_all():
    """Return True iff the clean copy passes and every planted error is caught."""
    ok = True
    d = copy(); rc, out = run(d); shutil.rmtree(d)
    print("clean copy:", "PASS" if rc == 0 else "FAIL"); ok &= rc == 0
    for f, text, key in MUTATIONS:
        d = copy()
        with open(os.path.join(d, f), "a", encoding="utf-8") as fh: fh.write(text)
        rc, out = run(d); shutil.rmtree(d)
        caught = rc != 0 and key in out
        print("planted %-24s in %-10s -> %s" % (key, f, "caught" if caught else "MISSED")); ok &= caught
    for f, a, b, key in REPLACEMENTS:
        d = copy(); p = os.path.join(d, f); t = open(p, encoding="utf-8").read()
        assert a in t, (f, a)
        open(p, "w", encoding="utf-8").write(t.replace(a, b, 1))
        rc, out = run(d); shutil.rmtree(d)
        caught = rc != 0 and key in out
        print("planted %-24s in %-10s -> %s" % (key, f, "caught" if caught else "MISSED")); ok &= caught
    for f, text in CLEAN:
        d = copy()
        with open(os.path.join(d, f), "a", encoding="utf-8") as fh: fh.write(text)
        rc, out = run(d); shutil.rmtree(d)
        print("clean sentence in %-10s -> %s" % (f, "passes" if rc == 0 else "FALSE POSITIVE")); ok &= rc == 0
    # R7 is a soft warning: an over-long README warns but does not fail
    d = copy()
    with open(os.path.join(d, "README.md"), "a", encoding="utf-8") as fh: fh.write("\n\n" + "word " * 1000 + "\n")
    rc, out = run(d); shutil.rmtree(d)
    soft = rc == 0 and "WARN length" in out
    print("over-long README -> %s" % ("warns, does not fail" if soft else "WRONG (must warn only)")); ok &= soft
    # version drift
    import re
    cur = re.search(r"^# .*? v(\d+\.\d+(?:\.\d+)?[a-z]?) draft", open(os.path.join(ROOT, "THEORY.md"), encoding="utf-8").read(), re.M).group(1)
    d = copy(); p = os.path.join(d, "CORE.md"); s = open(p, encoding="utf-8").read().replace("(v%s draft" % cur, "(v1.4.0 draft"); open(p, "w", encoding="utf-8").write(s)
    rc, out = run(d); shutil.rmtree(d); caught = rc != 0 and "versions" in out
    print("planted %-24s in %-10s -> %s" % ("stale version copy", "CORE.md", "caught" if caught else "MISSED")); ok &= caught
    print("RESULT:", "PASS" if ok else "FAIL")
    return ok


def test_check_consistency():
    """pytest entry point."""
    assert run_all()


if __name__ == "__main__":
    sys.exit(0 if run_all() else 1)
