#!/usr/bin/env python3
"""CT34 dyadic nesting operator. Reads criteria.json. No randomness.

The argmin in the operator's definition is global. A dense scan brackets it
and a golden section polishes that bracket. A pure golden section on the
whole bracket is also computed; a disagreement is recorded and the global
argmin is the one that enters rho.
"""
import cmath
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_criteria():
    with open(os.path.join(HERE, "criteria.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _exp(x):
    if isinstance(x, complex):
        return cmath.exp(x)
    return math.exp(x)


def _log(x):
    if isinstance(x, complex):
        return cmath.log(x)
    return math.log(x)


def f_star(t):
    return t + 1.0 / t


def phi_of(kind, t):
    if kind == 1:
        return t ** 3 + t ** (-3)
    if kind == 2:
        return t ** 5 + t ** (-5)
    if kind == 3:
        z = _log(t)
        return _exp(-z * z)
    raise ValueError(kind)


def f_of(kind, s, t):
    return f_star(t) + s * phi_of(kind, t)


def family_f(A, B, t):
    return A * t + B / t


def V_pair(b, t):
    tb = t / b
    return (4.0 / 3.0) * (t ** 3 + tb ** 3)


def golden_on(func, lo, hi, tol):
    """Minimize func on [lo, hi]. Returns the midpoint of the final bracket."""
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = func(c), func(d)
    while (b - a) > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = func(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = func(d)
    return 0.5 * (a + b)


def scan_min(func, lo, hi, nscan):
    best_v = None
    best_z = None
    step = (hi - lo) / (nscan - 1)
    for i in range(nscan):
        z = lo + i * step
        v = func(z)
        if best_v is None or v < best_v:
            best_v = v
            best_z = z
    return best_z, best_v, step


def newton_polish(func, z):
    """Finish an argmin by Newton on the derivative.

    Comparing function values cannot locate this minimum to 1e-12: near the
    minimum the curvature sits below double precision. A complex-step
    derivative has no cancellation, so Newton computes the same critical
    point to rounding error. func must accept a complex argument.
    """
    h = 1e-20
    hh = 1e-4
    for _ in range(12):
        fp = func(z + 1j * h).imag / h
        fpp = (func(z + hh).real - 2.0 * func(z).real + func(z - hh).real) / (hh * hh)
        if fpp == 0.0:
            break
        step = fp / fpp
        if abs(step) > 0.5:
            step = math.copysign(0.5, step)
        z = z - step
        if abs(step) < 1e-15:
            break
    return z


def global_log_argmin(func, lo, hi, tol):
    """Global argmin of func(log t): dense scan, golden polish, then Newton."""
    nscan = 8001
    z_scan, _, step = scan_min(func, lo, hi, nscan)
    pure = golden_on(func, lo, hi, tol)
    half = 4.0 * step
    z_lo = max(lo, z_scan - half)
    z_hi = min(hi, z_scan + half)
    polished = golden_on(func, z_lo, z_hi, tol)
    polished = newton_polish(func, polished)
    return polished, pure


def slack_maps(f, b, bracket, tol):
    def F_log(z):
        t = _exp(z)
        return f(t) + f(t / b)

    z0, z_pure = global_log_argmin(F_log, -bracket, bracket, tol)
    t0 = math.exp(z0)
    F0 = F_log(z0)

    def Tf(u):
        return 2.0 * F_log(math.log(t0 * u)) / F0

    return Tf, t0, F0, abs(z0 - z_pure)


def binding_maps(f, b, q, yhat, bracket, tol):
    """Minimizer of F on the feasible set.

    A golden section on a bracket that crosses the feasible boundary can
    walk into the infeasible side and stay there, because both samples are
    then equal at the sentinel. The scan finds the feasible run, and the
    golden section is restricted to that run. That is the argmin the
    operator names.
    """

    def F_of_t(t):
        return f(t) + f(t / b)

    def feasible(t):
        F = F_of_t(t)
        if not (F < yhat):
            return False
        theta = 2.0 * (yhat - F) / V_pair(b, t)
        return theta >= q - 1e-12

    nscan = 8001
    step = (2.0 * bracket) / (nscan - 1)
    best_v = None
    best_i = None
    flags = []
    for i in range(nscan):
        t = math.exp(-bracket + i * step)
        ok = feasible(t)
        flags.append(ok)
        if ok:
            v = F_of_t(t)
            if best_v is None or v < best_v:
                best_v = v
                best_i = i
    if best_i is None:
        return None
    i_lo = best_i
    while i_lo > 0 and flags[i_lo - 1]:
        i_lo -= 1
    i_hi = best_i
    while i_hi < nscan - 1 and flags[i_hi + 1]:
        i_hi += 1
    z_lo = -bracket + i_lo * step
    z_hi = -bracket + i_hi * step
    if i_hi == i_lo:
        z0 = z_lo
    else:
        z0 = golden_on(lambda z: F_of_t(math.exp(z)), z_lo, z_hi, tol)
        z_try = newton_polish(lambda z: F_of_t(_exp(z)), z0)
        if z_lo <= z_try <= z_hi and feasible(math.exp(z_try)):
            z0 = z_try
        elif not feasible(math.exp(z0)):
            z0 = -bracket + best_i * step
    t0 = math.exp(z0)
    F0 = F_of_t(t0)

    def Tf(u):
        return 2.0 * F_of_t(t0 * u) / F0

    return Tf, t0, F0, 0.0


def grid(Z, N):
    if N == 1:
        return [0.0], [1.0]
    dz = (2.0 * Z) / (N - 1)
    zs = [-Z + i * dz for i in range(N)]
    # Trapezoid weights on a uniform grid. The common dz cancels in rho,
    # but the end half-weights do not, so they are kept.
    w = [dz] * N
    w[0] *= 0.5
    w[-1] *= 0.5
    return zs, w


def rayleigh(Tf, kind, s, Z, N):
    zs, w = grid(Z, N)
    num = 0.0
    den = 0.0
    max_gap = 0.0
    for z, wi in zip(zs, w):
        u = math.exp(z)
        phi = phi_of(kind, u)
        gap = Tf(u) - f_star(u)
        num += wi * gap * phi
        den += wi * phi * phi
        if abs(gap) > max_gap:
            max_gap = abs(gap)
    rho = num / (s * den)
    return rho, max_gap


def second_derivative_phi1(t, s):
    # f = t + 1/t + s (t^3 + t^{-3})
    return 2.0 / t ** 3 + s * (6.0 * t + 12.0 / t ** 5)


def convex_ok(Z, N, s):
    zs, _ = grid(Z, N)
    worst = min(second_derivative_phi1(math.exp(z), s) for z in zs)
    return worst > 0.0, worst


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs)


def score(rec, crit):
    tol = crit["stable_tol"]
    expanding = crit["expanding_min"]
    if not rec["S1"] or not rec["S2"]:
        return "BROKEN"
    if not rec["convex_ok"]:
        return "NONCONVEX"
    slack = rec["slack_primary_window"]
    rhos = [slack[k] for k in ("1", "2", "3")]
    m = mean(rhos)
    m2 = mean(rec["slack_refine_window"][k] for k in ("1", "2", "3"))
    m_fd = mean(rec["slack_fd_window"][k] for k in ("1", "2", "3"))
    if abs(m - m2) > tol or abs(m - m_fd) > tol:
        return "CUTOFF"
    if max(rhos) - min(rhos) > tol:
        return "MODE_DEPENDENT"
    if all(abs(r) < expanding for r in rhos):
        return "CONTRACTING"
    # Slack half of SUPPORT holds only when the three agree with the mean
    # and the mean is expanding. The order above already returns when they
    # differ by more than tol, which is the locked MODE_DEPENDENT test.
    if max(abs(r - m) for r in rhos) > tol or abs(m) < expanding:
        return "CONTRACTING"
    for q, block in rec["binding_primary_window"].items():
        mq = mean(block[k] for k in ("1", "2", "3"))
        if abs(mq - m) > tol:
            return "CAP_DEPENDENT"
    return "SUPPORT"


def family_and_fixed(crit, bracket, tol):
    b = crit["b_primary"]
    window = crit["windows"][0]
    zs, _ = grid(window["Z"], window["N"])
    Tf, t0, F0, gold_gap = slack_maps(f_star, b, bracket, tol)
    s1_gap = 0.0
    for z in zs:
        u = math.exp(z)
        s1_gap = max(s1_gap, abs(Tf(u) - f_star(u)))
    s1 = s1_gap < crit["fixed_point_tol"]
    residuals = []
    for A, B in crit["family_points"]:
        Tfam, _, _, _ = slack_maps(lambda t, A=A, B=B: family_f(A, B, t), b, bracket, tol)
        gap = 0.0
        for z in zs:
            u = math.exp(z)
            gap = max(gap, abs(Tfam(u) - f_star(u)))
        residuals.append({"A": A, "B": B, "max_abs": gap})
    s2_family = all(row["max_abs"] < crit["family_tol"] for row in residuals)
    # Lemma B, b = 2, A = B = 1. F0 = 2(1+b)/sqrt(b) = 3*sqrt(2).
    Tf2, _, F0_b2, _ = slack_maps(f_star, 2, bracket, tol)
    target = 3.0 * math.sqrt(2.0)
    lemma_b = abs(F0_b2 - target) < crit["family_tol"]
    s2 = s2_family and lemma_b
    return {
        "S1": s1,
        "S1_max_abs": s1_gap,
        "S1_t0": t0,
        "S1_golden_log_gap": gold_gap,
        "S2": s2,
        "S2_family": residuals,
        "S2_F0_b2": F0_b2,
        "S2_F0_target": target,
        "S2_lemma_b": lemma_b,
    }


def rhos_for(kind_list, s, b, Z, N, bracket, tol, binding):
    out = {}
    gaps = {}
    gold = {}
    for kind in kind_list:
        def f(t, kind=kind, s=s):
            return f_of(kind, s, t)

        if binding is None:
            Tf, _, _, ggap = slack_maps(f, b, bracket, tol)
        else:
            q, yhat = binding
            got = binding_maps(f, b, q, yhat, bracket, tol)
            if got is None:
                out[str(kind)] = None
                continue
            Tf, _, _, ggap = got
        rho, gap = rayleigh(Tf, kind, s, Z, N)
        out[str(kind)] = rho
        gaps[str(kind)] = gap
        gold[str(kind)] = ggap
    return out, gaps, gold


def marginal_yhat(b, q, bracket, tol):
    Tf, t_c, F_c, _ = slack_maps(f_star, b, bracket, tol)
    yhat = F_c + 0.5 * q * V_pair(b, t_c)
    return yhat, t_c, F_c


def run():
    crit = load_criteria()
    bracket = crit["golden_log_bracket"]
    tol = crit["golden_tol"]
    kinds = (1, 2, 3)
    base = family_and_fixed(crit, bracket, tol)
    conv, conv_worst = convex_ok(crit["windows"][0]["Z"], crit["windows"][0]["N"], crit["convex_s"])

    def pack(b, s, window, binding):
        rh, gaps, gold = rhos_for(kinds, s, b, window["Z"], window["N"], bracket, tol, binding)
        return rh, {"max_abs_Tf_minus_f": gaps, "golden_log_gap": gold}

    rec = dict(base)
    rec["convex_ok"] = conv
    rec["convex_worst_second"] = conv_worst

    w0 = crit["windows"][0]
    w1 = crit["windows"][1]
    b = crit["b_primary"]
    s = crit["s_primary"]
    s2 = crit["s_check"]

    rec["slack_primary_window"], extra0 = pack(b, s, w0, None)
    rec["slack_refine_window"], extra1 = pack(b, s, w1, None)
    rec["slack_fd_window"], extra_fd = pack(b, s2, w0, None)
    rec["slack_diagnostics"] = {"primary": extra0, "refine": extra1, "fd": extra_fd}

    side, _ = pack(crit["b_side"], s, w0, None)
    rec["slack_b_side"] = side

    binding = {}
    binding_side = {}
    yhat_rows = {}
    for q in crit["q_values"]:
        yhat, t_c, F_c = marginal_yhat(b, q, bracket, tol)
        key = format(q, ".1f")
        yhat_rows[key] = {"yhat": yhat, "t_c": t_c, "F_c": F_c}
        binding[key], _ = pack(b, s, w0, (q, yhat))
        yhat_b, _, _ = marginal_yhat(crit["b_side"], q, bracket, tol)
        binding_side[key], _ = pack(crit["b_side"], s, w0, (q, yhat_b))
    rec["binding_primary_window"] = binding
    rec["binding_b_side"] = binding_side
    rec["marginal_income"] = yhat_rows

    # Amplitude gauge: currency rescaling must be removed by T. Code check.
    def f_amp(t):
        return (1.0 + s) * f_star(t)

    Tf_amp, _, _, _ = slack_maps(f_amp, b, bracket, tol)
    zs, w = grid(w0["Z"], w0["N"])
    num = 0.0
    den = 0.0
    for z, wi in zip(zs, w):
        u = math.exp(z)
        phi = f_star(u)
        gap = Tf_amp(u) - f_star(u)
        num += wi * gap * phi
        den += wi * phi * phi
    rec["amplitude_gauge_rho"] = num / (s * den)

    rec["cell"] = score(rec, crit)
    rec["criteria_echo"] = {
        "stable_tol": crit["stable_tol"],
        "expanding_min": crit["expanding_min"],
        "q_values": crit["q_values"],
        "windows": crit["windows"],
        "s_primary": crit["s_primary"],
        "s_check": crit["s_check"],
    }
    return rec


def fmt(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, float):
        return f"{x:.12g}"
    return str(x)


def render(rec):
    lines = []
    lines.append("CT34 nesting operator, slack and marginal-cap Rayleigh quotients")
    lines.append(f"cell {rec['cell']}")
    lines.append(f"S1 {fmt(rec['S1'])} max_abs {fmt(rec['S1_max_abs'])} t0 {fmt(rec['S1_t0'])}")
    lines.append(
        f"S2 {fmt(rec['S2'])} lemma_b {fmt(rec['S2_lemma_b'])} "
        f"F0 {fmt(rec['S2_F0_b2'])} target {fmt(rec['S2_F0_target'])}"
    )
    for row in rec["S2_family"]:
        lines.append(f"  family A {fmt(row['A'])} B {fmt(row['B'])} max_abs {fmt(row['max_abs'])}")
    lines.append(
        f"convex_ok {fmt(rec['convex_ok'])} worst_fsecond {fmt(rec['convex_worst_second'])}"
    )
    lines.append(f"amplitude_gauge_rho {fmt(rec['amplitude_gauge_rho'])}")

    def block(title, rh):
        lines.append(title)
        for k in ("1", "2", "3"):
            lines.append(f"  phi{k} {fmt(rh[k])}")
        vals = [rh[k] for k in ("1", "2", "3")]
        lines.append(f"  mean {fmt(mean(vals))} spread {fmt(max(vals) - min(vals))}")

    block("slack b=2 window Z=2 N=64 s=1e-4", rec["slack_primary_window"])
    block("slack b=2 window Z=3 N=96 s=1e-4", rec["slack_refine_window"])
    block("slack b=2 window Z=2 N=64 s=1e-5", rec["slack_fd_window"])
    block("slack b=3 window Z=2 N=64 s=1e-4", rec["slack_b_side"])
    for q, rh in rec["binding_primary_window"].items():
        y = rec["marginal_income"][q]
        lines.append(
            f"binding b=2 q={q} yhat {fmt(y['yhat'])} t_c {fmt(y['t_c'])} F_c {fmt(y['F_c'])}"
        )
        block(f"binding b=2 q={q} window Z=2 N=64", rh)
    for q, rh in rec["binding_b_side"].items():
        block(f"binding b=3 q={q} window Z=2 N=64", rh)
    lines.append("ALL LAYER-FP CHECKS DONE")
    lines.append("")
    return "\n".join(lines)


def main():
    rec = run()
    text = render(rec)
    with open(os.path.join(HERE, "nest_map.json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=2, sort_keys=True)
        fh.write("\n")
    with open(os.path.join(HERE, "nest_map.out"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
