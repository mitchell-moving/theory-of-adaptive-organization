"""Runs the locked T77 gravitational-floor checks and compares stdout to the stored run."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record_ratio_dual_checks")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "2987944137966540eb8c6b56977bea2250d792041c247d8806b9ecbe531bc73a"
LOCKED_SHADOW = "4e306d8394d5237d3a7ca82c8f5f504ac7725cca0b6369ff7d7a0d596eea25ec"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def test_floor_prereg_lock_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG_FLOOR.md")) == LOCKED_PREREG
    lock = open(os.path.join(HERE, "PREREG_FLOOR.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG
    # The shadow-price lock is not edited by this check.
    assert _sha256(os.path.join(HERE, "PREREG.md")) == LOCKED_SHADOW


def _allowed_theory_blobs():
    """The lock-time blob, plus THEORY.md at both parents of recent merges on the
    first-parent line. This branch must not edit THEORY.md, but main may change it
    after the lock and be merged in (as #284 did)."""
    allowed = {LOCKED_THEORY}
    merges = subprocess.run(
        ["git", "rev-list", "--first-parent", "--merges", "-20", "HEAD"],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    ).stdout.split()
    for m in merges:
        for p in ("^1", "^2"):
            r = subprocess.run(
                ["git", "rev-parse", "--verify", "-q", m + p + ":THEORY.md"],
                capture_output=True, text=True, cwd=ROOT, timeout=30,
            )
            if r.returncode == 0:
                allowed.add(r.stdout.strip())
    return allowed


def test_theory_blob_unchanged_floor():
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() in _allowed_theory_blobs()


def test_floor_checks_match_stored_stdout():
    script = os.path.join(HERE, "floor_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 0" in r.stdout
    assert "NO-EPS" in r.stdout
    with open(os.path.join(HERE, "floor_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
