"""Runs the locked T77 shadow-price checks and compares stdout to the stored run."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record_ratio_dual_checks")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "4e306d8394d5237d3a7ca82c8f5f504ac7725cca0b6369ff7d7a0d596eea25ec"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def test_dual_prereg_lock_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG.md")) == LOCKED_PREREG
    lock = open(os.path.join(HERE, "PREREG.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG


def test_theory_blob_unchanged_dual():
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == LOCKED_THEORY


def test_shadow_price_checks_match_stored_stdout():
    script = os.path.join(HERE, "shadow_price_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 0" in r.stdout
    assert "NO-NATURAL-D" in r.stdout
    with open(os.path.join(HERE, "shadow_price_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
