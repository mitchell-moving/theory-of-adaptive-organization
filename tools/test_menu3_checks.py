"""Byte-for-byte rerun of the non-orthogonal menu (OPEN_WORK T72, PREREG_3)."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "menu3_checks")


def test_menu3_matches_locked_output():
    with open(os.path.join(HERE, "SHA256SUMS"), encoding="utf-8") as fh:
        digest, name = fh.read().split()
    env = dict(os.environ)
    env["OMP_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "run_menu3.py")],
        cwd=HERE, capture_output=True, text=True, timeout=600, env=env,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "P-loss PASS" in r.stdout
    assert "P-gmax PASS" in r.stdout
    assert "P-win FAIL" in r.stdout
    assert "headline Model implication conditional_on Hardy_ln_K_AB TIE" in r.stdout
    got = hashlib.sha256(open(os.path.join(HERE, name), "rb").read()).hexdigest()
    assert got == digest
