"""Runs the locked T76 quantum-record checks and compares stdout to the stored run."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "record_ratio_reframes_checks")
LOCKED_THEORY = "6caadae569116a94a74563398be94cebf6e99e9b"
LOCKED_PREREG = "1ac92e314705b3378e3b6a1bd665d36ec6dc9f7f812760a20bc4556617b817d3"

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


def test_quantum_prereg_lock_unchanged():
    assert _sha256(os.path.join(HERE, "PREREG_QUANTUM.md")) == LOCKED_PREREG
    lock = open(os.path.join(HERE, "PREREG_QUANTUM.sha256"), encoding="utf-8").readline().split()[0]
    assert lock == LOCKED_PREREG


def test_theory_blob_unchanged_quantum():
    r = subprocess.run(
        ["git", "hash-object", os.path.join(ROOT, "THEORY.md")],
        capture_output=True, text=True, cwd=ROOT, timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() in _theory_blobs_allowed()


def _split_out(text):
    """Original stored run, then the dated errata appendix."""
    marker = "# Errata, 24 November 2026"
    assert marker in text
    original, rest = text.split(marker, 1)
    return original, marker + rest


def test_quantum_original_run_log_preserved():
    with open(os.path.join(HERE, "quantum_record_checks.out"), encoding="utf-8") as f:
        stored = f.read()
    original, appendix = _split_out(stored)
    assert original == (
        "Q-comm PASS frobenius=0.176776695297\n"
        "Q-slope PASS min_PD=0.025450 max_PD=0.025714\n"
        "Q-pointer PASS PD0=0.025450 PDpi2=0.025450\n"
        "Q-garble PASS min_gap=0.150000\n"
        "Q-state PASS trace_distance=0.300000\n"
        "Q-reuse FAIL I_cond=0.017070 PD_total=0.084896 gap1=0.084896 gap2=0.169791\n"
        "Q-rank PASS PD=0.000e+00 I=0.000e+00 ledger_gap=0.346573590280 half_ln2=0.346573590280\n"
        "Q-coh PASS PD=0.065406 cost_gap=0.065406\n"
        "FAILS 1\n"
        "\n"
    )
    assert "Q-coh FAIL PD=0.000000 cost_gap=0.000000" in appendix
    assert appendix.strip().endswith("FAILS 2")


def test_quantum_record_checks_match_rescore_stdout():
    script = os.path.join(HERE, "quantum_record_checks.py")
    r = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Q-reuse FAIL" in r.stdout
    assert "Q-coh FAIL PD=0.000000 cost_gap=0.000000" in r.stdout
    assert "FAILS 2" in r.stdout
    with open(os.path.join(HERE, "quantum_record_checks.out"), encoding="utf-8") as f:
        stored = f.read()
    _original, appendix = _split_out(stored)
    rescore_lines = [ln for ln in appendix.splitlines() if ln and not ln.startswith("#")]
    expected = "\n".join(rescore_lines) + "\n"
    assert r.stdout == expected
