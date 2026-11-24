"""Runs the locked T80 corner checks and compares stdout to the stored run."""
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record-ratio-corners-2026-11-24")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "367adf39a76ef6adebe3881702a8a8f7997099280e10313b66d8f105dba3f69f"
HYPOTHESIS = "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment."
NOTES = (
    "PREREG.md",
    "MEMO.md",
    "RUN_LOG.md",
    "DEVIATIONS.md",
    "corner_checks.py",
    "corner_checks.out",
)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def test_corner_prereg_lock_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG.md")) == LOCKED_PREREG
    lock = open(os.path.join(HERE, "PREREG.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG


def test_theory_blob_unchanged_corners():
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == LOCKED_THEORY


def test_hypothesis_sentence_byte_identical_corners():
    core = open(os.path.join(ROOT, "CORE.md"), encoding="utf-8").read().splitlines()[6]
    assert core.strip("*") == HYPOTHESIS
    for name in ("PREREG.md", "MEMO.md"):
        text = open(os.path.join(HERE, name), encoding="utf-8").read()
        assert HYPOTHESIS in text


def test_corner_checks_match_stored_stdout():
    script = os.path.join(HERE, "corner_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 3" in r.stdout
    assert "P1 PASS" in r.stdout
    assert "P2 PASS" in r.stdout
    assert "P3 PASS" in r.stdout
    assert "P4c FAIL" in r.stdout
    assert "G-dyn PASS" in r.stdout
    with open(os.path.join(HERE, "corner_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_corner_notes_keep_the_wording_bounds():
    needles = (
        "theor" + "y of everything",
        "solv" + "ed",
        "bi" + "ll",
        "ki" + "ll",
        "verdi" + "ct",
    )
    reserved = "la" + "w"
    for name in NOTES:
        text = open(os.path.join(HERE, name), encoding="utf-8").read().lower()
        for needle in needles:
            assert needle not in text, (name, needle)
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(r"\b" + reserved + r"\b", line, re.I) and HYPOTHESIS.lower() not in line:
                raise AssertionError("%s:%d reserved word outside the hypothesis sentence" % (name, i))
