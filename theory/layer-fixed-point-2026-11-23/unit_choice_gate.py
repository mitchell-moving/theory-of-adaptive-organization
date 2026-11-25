#!/usr/bin/env python3
"""Unit and choice gate from PREREG_ADDENDUM_2.md.

The choice arm reads nest_map.json. The unit arm evaluates one stretch,
(mu, gamma) = (4, 4) against (1, 1). Tolerance is criteria.json stable_tol.
"""
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MU_STRETCH = 4.0
GAMMA_STRETCH = 4.0


def load_nest():
    path = os.path.join(HERE, "nest_map.py")
    spec = importlib.util.spec_from_file_location("nest_map", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mean(block):
    vals = [block[k] for k in ("1", "2", "3")]
    return sum(vals) / 3.0, vals


def fmt(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, float):
        return f"{x:.12g}"
    return str(x)


def arm(moved):
    return "FAIL" if moved else "PASS"


def main():
    mod = load_nest()
    crit = mod.load_criteria()
    tol = crit["stable_tol"]
    s = crit["s_primary"]
    b = crit["b_primary"]
    window = crit["windows"][0]
    bracket = crit["golden_log_bracket"]
    gtol = crit["golden_tol"]
    with open(os.path.join(HERE, "nest_map.json"), encoding="utf-8") as fh:
        rec = json.load(fh)

    base_mean, base_vals = mean(rec["slack_primary_window"])
    side_mean, side_vals = mean(rec["slack_b_side"])
    win_mean, _ = mean(rec["slack_refine_window"])
    q_means = []
    for q, block in rec["binding_primary_window"].items():
        mq, _ = mean(block)
        q_means.append((q, mq))

    def stretched_rhos(mu, gamma):
        rhos = {}
        for kind in (1, 2, 3):
            def f(t, kind=kind, mu=mu, gamma=gamma):
                return mu * mod.f_of(kind, s, gamma * t)

            Tf, _, _, _ = mod.slack_maps(f, b, bracket, gtol)
            rho, _ = mod.rayleigh(Tf, kind, s, window["Z"], window["N"])
            rhos[str(kind)] = rho
        return rhos

    unit_block = stretched_rhos(MU_STRETCH, GAMMA_STRETCH)
    unit_mean, unit_vals = mean(unit_block)
    fresh_block = stretched_rhos(1.0, 1.0)
    fresh_mean, _ = mean(fresh_block)

    Tf_b, t0_b, F0_b, _ = mod.slack_maps(mod.f_star, b, bracket, gtol)

    def f_stretched(t):
        return MU_STRETCH * mod.f_star(GAMMA_STRETCH * t)

    _, t0_s, F0_s, _ = mod.slack_maps(f_stretched, b, bracket, gtol)
    t0_hat = t0_b / GAMMA_STRETCH
    F0_hat = MU_STRETCH * F0_b

    per_mode_unit = [abs(unit_vals[i] - base_vals[i]) for i in range(3)]
    per_mode_b = [abs(side_vals[i] - base_vals[i]) for i in range(3)]
    mode_spread = max(base_vals) - min(base_vals)
    unit_move = max(abs(unit_mean - base_mean), max(per_mode_unit))
    record_move = abs(fresh_mean - base_mean)
    b_move = max(abs(side_mean - base_mean), max(per_mode_b))
    window_move = abs(win_mean - base_mean)
    q_move = max(abs(mq - base_mean) for _, mq in q_means)
    # t0 and F0 are the input on which the gate must be able to fire.
    raw_moves = abs(t0_s - t0_b) > tol or abs(F0_s - F0_b) > tol

    unit_fail = unit_move > tol or record_move > tol
    choice_fail = b_move > tol or mode_spread > tol or window_move > tol or q_move > tol
    if unit_fail and choice_fail:
        gate = "FAIL_UNITS_AND_CHOICE"
    elif unit_fail:
        gate = "FAIL_UNITS"
    elif choice_fail:
        gate = "FAIL_CHOICE"
    else:
        gate = "PASS"
    yielded = "none" if gate != "PASS" else fmt(base_mean)

    lines = []
    lines.append("unit and choice gate on the SUPPORT candidate")
    lines.append(f"candidate_mean {fmt(base_mean)} tol {fmt(tol)}")
    lines.append(
        f"unit_arm {arm(unit_fail)} stretch_mean {fmt(unit_mean)} "
        f"move {fmt(unit_move)} fresh_move {fmt(record_move)}"
    )
    for i, kind in enumerate(("1", "2", "3")):
        lines.append(
            f"  phi{kind} record {fmt(base_vals[i])} stretch {fmt(unit_vals[i])} "
            f"abs_diff {fmt(per_mode_unit[i])}"
        )
    lines.append(
        f"choice_b {arm(b_move > tol)} b3_mean {fmt(side_mean)} move {fmt(b_move)}"
    )
    for i, kind in enumerate(("1", "2", "3")):
        lines.append(
            f"  phi{kind} b2 {fmt(base_vals[i])} b3 {fmt(side_vals[i])} "
            f"abs_diff {fmt(per_mode_b[i])}"
        )
    lines.append(
        f"choice_mode {arm(mode_spread > tol)} spread {fmt(mode_spread)}"
    )
    lines.append(
        f"choice_window {arm(window_move > tol)} other_mean {fmt(win_mean)} "
        f"move {fmt(window_move)}"
    )
    lines.append(f"choice_cap {arm(q_move > tol)} move {fmt(q_move)}")
    for q, mq in q_means:
        lines.append(f"  q {q} mean {fmt(mq)} abs_diff {fmt(abs(mq - base_mean))}")
    lines.append(
        f"raw_scale t0_base {fmt(t0_b)} t0_stretch {fmt(t0_s)} t0_expected {fmt(t0_hat)} "
        f"F0_base {fmt(F0_b)} F0_stretch {fmt(F0_s)} F0_expected {fmt(F0_hat)} "
        f"raw_changes {fmt(raw_moves)}"
    )
    lines.append(f"gate {gate}")
    lines.append(f"yielded {yielded}")
    lines.append("ALL UNIT-CHOICE CHECKS DONE")
    lines.append("")
    text = "\n".join(lines)
    out = {
        "candidate_mean": base_mean,
        "tol": tol,
        "unit_mean": unit_mean,
        "unit_move": unit_move,
        "fresh_move": record_move,
        "b_move": b_move,
        "mode_spread": mode_spread,
        "window_move": window_move,
        "q_move": q_move,
        "t0_base": t0_b,
        "t0_stretch": t0_s,
        "F0_base": F0_b,
        "F0_stretch": F0_s,
        "raw_changes": raw_moves,
        "gate": gate,
        "yielded": None if yielded == "none" else base_mean,
    }
    with open(os.path.join(HERE, "unit_choice_gate.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write("\n")
    with open(os.path.join(HERE, "unit_choice_gate.out"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
