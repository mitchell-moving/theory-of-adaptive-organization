"""Runs theory/ctc_fixed_point_checks/ctc_fixed_point_checks.py (OPEN_WORK T85)."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "ctc_fixed_point_checks")
PREREG = os.path.join(ROOT, "theory", "ctc-fixed-point-2026-11-24", "PREREG.md")
LOCKED = "756d9f0c257d4dcf73d53440cde43a50dd8092633cdc3383cf7b21ad3b0e2f8e"


def test_prereg_hash_unchanged():
    digest = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    assert digest == LOCKED


def test_ctc_fixed_point_scored():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "ctc_fixed_point_checks.py")],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "definition DEUTSCH-FIXED-POINT" in r.stdout
    assert "P1a PASS" in r.stdout
    assert "P1b-grid PASS nonunique=20/64" in r.stdout
    assert "P2-bound PASS" in r.stdout
    assert "P2-candidate UNSUPPORTED" in r.stdout
    assert "not-a-process" in r.stdout
    assert "P3-candidate UNSUPPORTED" in r.stdout
    assert "P4-cycle PASS" in r.stdout
    assert "P4-half PASS sum=-0.500000000000" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "FAILS 1" not in r.stdout
    with open(os.path.join(HERE, "ctc_fixed_point_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
