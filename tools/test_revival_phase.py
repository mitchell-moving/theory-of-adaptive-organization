"""Runs theory/revival_phase_checks/revival_phase_checks.py (OPEN_WORK T83)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "revival_phase_checks")


def test_revival_phase_checks_scored():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "revival_phase_checks.py")],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "definition MINIMAL-RETURN" in r.stdout
    assert "FAILS 6" in r.stdout
    assert "B-shape 1/3 PASS" in r.stdout
    assert "B-shape 1/7 FAIL" in r.stdout
    assert "P-comm PASS" in r.stdout
    assert "P-incomm PASS" in r.stdout
    assert "P-well PASS" in r.stdout
    assert "C-link PASS" in r.stdout
    assert "reading=RELABEL" in r.stdout
    assert "ALL T83 CHECKS PASS" not in r.stdout
    with open(os.path.join(HERE, "revival_phase_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
