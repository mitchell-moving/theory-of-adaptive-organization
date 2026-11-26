"""Runs theory/clock_term_checks/clock_term_checks.py (T68), the cheap subset of the clock-term checks."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "clock_term_checks")


def test_clock_term_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "clock_term_checks.py")],
        capture_output=True, text=True, timeout=900,
        env={**os.environ, "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2"},
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T68 CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    with open(os.path.join(HERE, "clock_term_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
