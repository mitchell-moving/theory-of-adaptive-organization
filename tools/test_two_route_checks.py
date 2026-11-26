"""Runs the two-route checks (theory/two-route-2026-11-25/checks): route_a_w2.py (A-C1, A-T2),
route_a_t1ppp.py (A-T1''') and route_b_t2p.py (B-T2', B-C3 code gate)."""
import json
import os
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "two-route-2026-11-25", "checks")
sys.path.insert(0, HERE)


def _close(a, b, tol=1e-9):
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(_close(a[k], b[k], tol) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(_close(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        return abs(a - b) <= tol * max(1.0, abs(a), abs(b))
    return a == b


def test_route_a_w2_reproduces_stored_output():
    r = subprocess.run([sys.executable, os.path.join(HERE, "route_a_w2.py")],
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr
    stored = json.load(open(os.path.join(HERE, "route_a_w2.out")))
    assert _close(json.loads(r.stdout), stored, 1e-6)
    assert stored["A-C1_max_abs_Qx_at_g0"] == 0.0
    assert stored["JP_heat_violations_of_2000"] == 0


def test_route_a_t1ppp_closed_form_matches_lyapunov():
    import route_a_t1ppp as m
    rng = np.random.default_rng(3)
    for _ in range(200):
        gamma, c, g = np.exp(rng.uniform(-2, 4)), rng.uniform(-1, 2), rng.uniform(0, 2)
        if g * c >= 0.95:
            continue
        assert m.lyap_check(gamma, c, g, 1.0) < 1e-8


def test_route_a_t1ppp_stored_run_verifies():
    r = subprocess.run([sys.executable, os.path.join(HERE, "route_a_t1ppp.py"), "verify",
                        os.path.join(HERE, "route_a_t1ppp.out")], capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "FAILS 0" in r.stdout
    runs = json.load(open(os.path.join(HERE, "route_a_t1ppp.out")))["runs"]
    assert sorted({x["w_x"] for x in runs}) == [0.5, 1.0, 2.0]
    for x in runs:
        assert x["joint_min"]["boundary"] is False


def test_route_b_edmonds_matches_brute_force():
    import route_b_t2p as m
    rng = np.random.default_rng(11)
    for _ in range(10):
        J = rng.uniform(size=9)
        for c in ((1.0, 3.0), (1.0, 1.0)):
            assert np.max(np.abs(m.stochastic_potential(J, c) - m.brute_sp(J, c))) < 1e-12


def test_route_b_stored_output_consistent():
    out = json.load(open(os.path.join(HERE, "route_b_t2p.out")))
    k = out["counts"]
    assert k["qualifying"] + k["sp_ties"] + k["not_two_minima"] == k["draws"] == 20000
    assert abs(out["f"] - k["worse_selected"] / k["qualifying"]) < 1e-15
    assert out["code_gate_B_C3"]["worse_selected"] == 0
    assert out["brute_force"]["checked"] == 200 and out["brute_force"]["max_abs_diff"] < 1e-12
