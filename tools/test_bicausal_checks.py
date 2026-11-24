"""Runs the locked T79 bi-causal checks and compares stdout to the stored run."""
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record-ratio-bicausal-2026-11-24")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "b78addd0edf765e9fa76c1f0d82cfdc88a30d9105b8bb0ddd5a4e6410a37e39e"
LOCKED_PREREG_3 = "6f89428bca13a08d9714f08cca260c83e4719ae4a7f735055f815ad5c66430c9"
HYPOTHESIS = "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment."
NOTES = ("PREREG.md", "PREREG_3.md", "MEMO.md", "RUN_LOG.md", "bicausal_checks.py")


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def test_bicausal_prereg_locks_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG.md")) == LOCKED_PREREG
    assert _sha256(os.path.join(HERE, "PREREG_3.md")) == LOCKED_PREREG_3
    lock = open(os.path.join(HERE, "PREREG.sha256"), encoding="utf-8").readline().split()[0]
    lock3 = open(os.path.join(HERE, "PREREG_3.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG
    assert lock3 == LOCKED_PREREG_3


def test_theory_blob_unchanged_bicausal():
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == LOCKED_THEORY


def test_hypothesis_sentence_byte_identical_bicausal():
    core = open(os.path.join(ROOT, "CORE.md"), encoding="utf-8").read().splitlines()[6]
    assert core.strip("*") == HYPOTHESIS
    for name in ("PREREG.md", "PREREG_3.md", "MEMO.md"):
        text = open(os.path.join(HERE, name), encoding="utf-8").read()
        assert HYPOTHESIS in text


def test_bicausal_checks_match_stored_stdout():
    script = os.path.join(HERE, "bicausal_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 5" in r.stdout
    assert "P1 FAIL" in r.stdout
    assert "G-parent PASS" in r.stdout
    assert "G-rev PASS" in r.stdout
    with open(os.path.join(HERE, "bicausal_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_bicausal_notes_keep_the_wording_bounds():
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
