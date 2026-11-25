"""Runs the locked T76 checks and compares stdout to the stored run."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record_ratio_reframes_checks")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8"

def _theory_blobs_allowed():
    """The lock-time blob, THEORY.md on a main ref, and THEORY.md from the main
    that was merged into this branch. This branch must not edit THEORY.md.
    Fork main can still hold the lock-time blob after upstream main has moved (#284)."""
    allowed = {LOCKED_THEORY}
    for ref in ("origin/main", "upstream/main"):
        r = subprocess.run(["git", "rev-parse", "--verify", "-q", ref + ":THEORY.md"],
                           capture_output=True, text=True, cwd=ROOT, timeout=30)
        if r.returncode == 0:
            allowed.add(r.stdout.strip())
    latest = subprocess.run(
        ["git", "rev-list", "--first-parent", "--merges", "-1", "HEAD"],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    if latest.returncode == 0 and latest.stdout.strip():
        parent = subprocess.run(
            ["git", "rev-parse", "--verify", "-q", latest.stdout.strip() + "^2:THEORY.md"],
            capture_output=True, text=True, cwd=ROOT, timeout=30,
        )
        if parent.returncode == 0:
            allowed.add(parent.stdout.strip())
    return allowed



def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def test_prereg_lock_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG.md")) == LOCKED_PREREG
    lock = open(os.path.join(HERE, "PREREG.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG


def test_theory_blob_unchanged():
    """The lock records git hash-object, not a raw sha256 of the bytes."""
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() in _theory_blobs_allowed()


def _split_out(text):
    """Original stored run, then the dated errata appendix."""
    marker = "# Errata, 24 November 2026 (America/New_York). K2 net minimum"
    assert marker in text
    original, rest = text.split(marker, 1)
    return original, marker + rest


def test_record_ratio_original_run_log_preserved():
    with open(os.path.join(HERE, "record_ratio_reframes_checks.out"), encoding="utf-8") as f:
        stored = f.read()
    original, appendix = _split_out(stored)
    assert original.endswith("FAILS 4\n")
    assert "net_min=0.0004213774925606595 at=(1.0033319156709788, 0.6581687266183737)" in original
    assert "net_min=0.0014997828907532262 at=(1.0, 0.65)" in appendix
    assert appendix.strip().endswith("FAILS 4")


def test_record_ratio_reframes_checks_match_stored_stdout():
    script = os.path.join(HERE, "record_ratio_reframes_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 4" in r.stdout
    assert "net_min=0.0014997828907532262 at=(1.0, 0.65)" in r.stdout
    assert "ls_max=0.000421" in r.stdout
    with open(os.path.join(HERE, "record_ratio_reframes_checks.out"), encoding="utf-8") as f:
        stored = f.read()
    _original, appendix = _split_out(stored)
    rescore_lines = [ln for ln in appendix.splitlines() if ln and not ln.startswith("#")]
    expected = "\n".join(rescore_lines) + "\n"
    assert r.stdout == expected
