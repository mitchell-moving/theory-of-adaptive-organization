"""Runs theory/gravity_barrier_checks/gravity_barrier_checks.py (T64)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_gravity_barrier_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "theory", "gravity_barrier_checks", "gravity_barrier_checks.py")],
        capture_output=True, text=True, timeout=600,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL GRAVITY-BARRIER CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    out = os.path.join(ROOT, "theory", "gravity_barrier_checks", "gravity_barrier_checks.out")
    with open(out, encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
