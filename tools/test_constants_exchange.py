"""Runs theory/constants-exchange-2026-11-24/dimension_check.py (T70)."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "constants-exchange-2026-11-24")
PREREG_SHA256 = "777532926d93ba8b2ce53efce56a9aa8bea9311d232ccf68066a93beda4fb6b9"


def test_dimension_check_matches_stored_output():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "dimension_check.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "DIMENSIONS OK" in r.stdout
    with open(os.path.join(HERE, "dimension_check.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_prereg_lock_unchanged():
    h = hashlib.sha256(open(os.path.join(HERE, "PREREG.md"), "rb").read()).hexdigest()
    assert h == PREREG_SHA256
