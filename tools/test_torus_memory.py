"""Runs theory/torus_memory_checks/torus_memory_checks.py (OPEN_WORK T82)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "torus_memory_checks")


def test_torus_memory_scoreboard_matches():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "torus_memory_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SCOREBOARD COMPLETE" in r.stdout
    assert "SCORED_FAIL P7" in r.stdout
    assert "HEADLINE PASS" in r.stdout
    with open(os.path.join(HERE, "torus_memory_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
