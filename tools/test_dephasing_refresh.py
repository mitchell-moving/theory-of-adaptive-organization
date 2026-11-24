"""Runs theory/dephasing_refresh_checks/dephasing_refresh_checks.py (OPEN_WORK T84b)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "dephasing_refresh_checks")


def test_dephasing_refresh_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "dephasing_refresh_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T84b CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "HEADLINE CLUE_REFRESH" in r.stdout
    with open(os.path.join(HERE, "dephasing_refresh_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_dephasing_refresh_addendum_checks():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "dephasing_refresh_addendum_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T84b ADDENDUM CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "HEADLINE OBSERVED_NOT_CLOCK" in r.stdout
    with open(os.path.join(HERE, "dephasing_refresh_addendum_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_dephasing_refresh_review_fold():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "dephasing_refresh_review_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T84b REVIEW-FOLD CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "HEADLINE OBSERVED_ALT_FLIPS" in r.stdout
    with open(os.path.join(HERE, "dephasing_refresh_review_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
