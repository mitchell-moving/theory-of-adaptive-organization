"""Runs theory/torus_memory_checks/horizon_checks.py (T82c)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "torus_memory_checks")


def test_horizon_scoreboard_matches():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "horizon_checks.py")],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SCOREBOARD COMPLETE" in r.stdout
    assert "SCORED_FAIL P-res H-flow H-walk H-gamma" in r.stdout
    with open(os.path.join(HERE, "horizon_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
