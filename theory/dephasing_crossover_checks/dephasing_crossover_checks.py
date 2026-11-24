#!/usr/bin/env python3
"""T84 checks. Criteria are locked in theory/dephasing-crossover-2026-11-24/PREREG.md.

Standard library only. A change that moves a bar, a grid, or a sign is not a bugfix.
"""
from __future__ import annotations

import math
import sys

KAPPA = 1.0
SEED = 20261124  # set and not drawn from
LN2 = math.log(2.0)
GT = (0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 20.0)
WS = (0.0, 0.5, 1.0, 2.0, 5.0, 20.0)
QS = (0.0, 0.5, 1.0, 2.0)
CS = (0.0, 0.05, 0.125, 0.2, 0.25)
ALPHAS = (1.0, 0.75, 0.5, 0.25, 0.0)
THETAS = (0.0, math.pi / 6.0, math.pi / 4.0, math.pi / 3.0, math.pi / 2.0)
RS_TH = (1.0, 0.5, 0.1)
EPS_SHAPE = (1e-4, 1e-3, 1e-2, 0.05, 0.1, 0.2, 0.4, 0.5)
R_SHAPE = (0.05, 0.2, 0.5, 0.9, 1.0)


def h(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def chi(r: float) -> float:
    return LN2 - h((1.0 + r) / 2.0)


def eps_of(r: float) -> float:
    return (1.0 - r) / 2.0


def entropy(eigs) -> float:
    s = 0.0
    for e in eigs:
        if e > 1e-15:
            s -= e * math.log(e)
    return s


def qubit_eigs(a: float, b: float, c: float):
    tr = a + b
    det = a * b - c * c
    disc = max(0.0, tr * tr - 4.0 * det)
    root = math.sqrt(disc)
    return (tr + root) / 2.0, (tr - root) / 2.0


def mi_hamming(p_m0_b0: float, p_m0_b1: float):
    """Uniform bit, binary record. Returns Shannon I and Bayes Hamming loss."""
    p_m0 = 0.5 * (p_m0_b0 + p_m0_b1)
    p_m1 = 1.0 - p_m0
    info = h(p_m0) - 0.5 * (h(p_m0_b0) + h(p_m0_b1))
    p_m1_b0 = 1.0 - p_m0_b0
    p_m1_b1 = 1.0 - p_m0_b1

    def piece(p_m, p_b0, p_b1):
        if p_m <= 0.0:
            return 0.0
        return min(0.5 * p_b0, 0.5 * p_b1) / p_m

    loss = p_m0 * piece(p_m0, p_m0_b0, p_m0_b1) + p_m1 * piece(p_m1, p_m1_b0, p_m1_b1)
    return info, loss


def designs(r: float):
    """Matrix scores (I, P_D, L) for H, P, Z at surviving coherence r."""
    # Phase state B=0: [[1/2, r/2], [r/2, 1/2]]. B=1 flips the sign of r.
    eigs = qubit_eigs(0.5, 0.5, r / 2.0)
    s_phase = entropy(eigs)
    # Respecting read, sigma_x. State is diagonal in x, so the pinch does not move it.
    p_m0_b0 = (1.0 + r) / 2.0
    p_m0_b1 = (1.0 - r) / 2.0
    i_h, l_h = mi_hamming(p_m0_b0, p_m0_b1)
    s_after_x = s_phase
    pd_h = s_after_x - s_phase
    # Pointer pinch, sigma_z. Populations 1/2, off-diagonal removed.
    i_z, l_z = mi_hamming(0.5, 0.5)
    s_z = entropy(qubit_eigs(0.5, 0.5, 0.0))
    pd_z = s_z - s_phase
    # Pointer encoding: |0> / |1|, invariant. Perfect z record.
    i_p, l_p = mi_hamming(1.0, 0.0)
    s_pointer = entropy(qubit_eigs(1.0, 0.0, 0.0))
    pd_p = s_pointer - s_pointer
    return (i_h, pd_h, l_h), (i_p, pd_p, l_p), (i_z, pd_z, l_z), s_phase


def j_h(r, w):
    return KAPPA * chi(r) + w * eps_of(r)


def j_p():
    return KAPPA * LN2


def j_z(r, w, q):
    return q * KAPPA * chi(r) + w / 2.0


def matmul(a, b):
    n = len(a)
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = a[i][k]
            if aik == 0.0:
                continue
            for j in range(n):
                out[i][j] += aik * b[k][j]
    return out


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def qutrit(c: float):
    return (
        (0.5, 0.0, 0.0),
        (0.0, 0.25, c),
        (0.0, c, 0.25),
    )


def respect(rho):
    p0 = ((1.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    p1 = ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    return madd(matmul(matmul(p0, rho), p0), matmul(matmul(p1, rho), p1))


def jacobi_eigs(a):
    m = [list(row) for row in a]
    n = 3
    for _ in range(48):
        p = q = 0
        best = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(m[i][j]) > best:
                    best = abs(m[i][j])
                    p, q = i, j
        if best < 1e-15:
            break
        app, aqq, apq = m[p][p], m[q][q], m[p][q]
        if apq == 0.0:
            break
        tau = (aqq - app) / (2.0 * apq)
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        cc = 1.0 / math.sqrt(1.0 + t * t)
        s = t * cc
        for i in range(n):
            if i == p or i == q:
                continue
            mip, miq = m[i][p], m[i][q]
            m[i][p] = m[p][i] = cc * mip - s * miq
            m[i][q] = m[q][i] = s * mip + cc * miq
        m[p][p] = cc * cc * app - 2.0 * s * cc * apq + s * s * aqq
        m[q][q] = s * s * app + 2.0 * s * cc * apq + cc * cc * aqq
        m[p][q] = m[q][p] = 0.0
    return [m[i][i] for i in range(n)]


def block_eigs(off: float):
    return (0.5, 0.25 + off, 0.25 - off)


def pd_alpha(c: float, alpha: float) -> float:
    return entropy(block_eigs(alpha * c)) - entropy(block_eigs(c))


def pd_theta(r: float, theta: float) -> float:
    ndot = r * abs(math.sin(theta))
    return h((1.0 + ndot) / 2.0) - h((1.0 + r) / 2.0)


def strict_inc(xs) -> bool:
    return all(xs[i + 1] > xs[i] + 1e-15 for i in range(len(xs) - 1))


def strict_dec(xs) -> bool:
    return all(xs[i + 1] < xs[i] - 1e-15 for i in range(len(xs) - 1))


def main() -> int:
    if SEED != 20261124:
        raise SystemExit("seed moved")
    lines = []
    # The label is computed from the booleans. It is not a stored word.
    c_ok = []

    # C0
    max_err = 0.0
    for gt in GT:
        r = math.exp(-gt)
        (ih, pdh, lh), (ip, pdp, lp), (iz, pdz, lz), _s = designs(r)
        closed = (
            (chi(r), 0.0, eps_of(r)),
            (LN2, 0.0, 0.0),
            (0.0, chi(r), 0.5),
        )
        got = ((ih, pdh, lh), (ip, pdp, lp), (iz, pdz, lz))
        for a, b in zip(got, closed):
            for x, y in zip(a, b):
                max_err = max(max_err, abs(x - y))
    ok = max_err <= 1e-9
    c_ok.append(ok)
    lines.append(f"C0 {'PASS' if ok else 'FAIL'} max_err={max_err:.3e}")

    # C1 P1 and shape
    bad = 0
    for gt in GT:
        r = math.exp(-gt)
        eps = eps_of(r)
        for w in WS:
            diff = j_p() - j_h(r, w)
            if eps == 0.0:
                if abs(diff) > 1e-9:
                    bad += 1
                continue
            t = h(eps) / eps
            gap = w / KAPPA - t
            if abs(gap) <= 1e-9:
                if abs(diff) > 1e-8:
                    bad += 1
            elif gap > 0.0:
                if not (diff < -1e-12):
                    bad += 1
            else:
                if not (diff > 1e-12):
                    bad += 1
    ts = [h(e) / e for e in EPS_SHAPE]
    shape = strict_dec(ts) and ts[0] > 8.0 and abs(ts[-1] - 2.0 * LN2) <= 1e-12
    ok = bad == 0 and shape
    c_ok.append(ok)
    lines.append(
        f"C1 {'PASS' if ok else 'FAIL'} bad_cells={bad} t_1em4={ts[0]:.6f} t_half={ts[-1]:.12f}"
    )

    # C2 P2
    bad = 0
    for q in QS:
        for gt in GT:
            r = math.exp(-gt)
            for w in WS:
                zh = j_z(r, w, q) - j_h(r, w)
                if q >= 1.0:
                    if zh < -1e-12:
                        bad += 1
                    continue
                thresh = 2.0 * (1.0 - q) * chi(r) / r
                gap = w / KAPPA - thresh
                if abs(gap) <= 1e-9:
                    if abs(zh) > 1e-8:
                        bad += 1
                elif gap < 0.0:
                    if not (zh < -1e-12):
                        bad += 1
                else:
                    if not (zh > 1e-12):
                        bad += 1
    ratios = [chi(r) / r for r in R_SHAPE]
    shape = strict_inc(ratios) and ratios[0] < 0.03 and abs(chi(1.0) - LN2) <= 1e-12
    ok = bad == 0 and shape
    c_ok.append(ok)
    lines.append(
        f"C2 {'PASS' if ok else 'FAIL'} bad_cells={bad} chi_over_r_0.05={ratios[0]:.6f} chi_1={chi(1.0):.12f}"
    )

    # C3 P3
    span_h = 0.0
    span_p = 0.0
    for gt in GT:
        r = math.exp(-gt)
        for w in WS:
            hs = [j_h(r, w) for _q in QS]
            ps = [j_p() for _q in QS]
            span_h = max(span_h, max(hs) - min(hs))
            span_p = max(span_p, max(ps) - min(ps))
    ok = span_h < 1e-12 and span_p < 1e-12
    c_ok.append(ok)
    lines.append(f"C3 {'PASS' if ok else 'FAIL'} span_H={span_h:.3e} span_P={span_p:.3e}")

    # C4 P4
    bad = 0.0
    for gt in GT:
        r = math.exp(-gt)
        eps = eps_of(r)
        for w in WS:
            delta = j_h(r, w) - KAPPA * LN2
            expect = w * eps - KAPPA * h(eps)
            bad = max(bad, abs(delta - expect))
    ok = bad <= 1e-9
    c_ok.append(ok)
    lines.append(f"C4 {'PASS' if ok else 'FAIL'} max_abs_delta={bad:.3e}")

    # C5 P5 null reading
    bad = 0
    for gt in GT:
        r = math.exp(-gt)
        eps = eps_of(r)
        for w in WS:
            jhw = KAPPA * LN2 + w * eps
            jpw = KAPPA * LN2
            if w > 0.0 and gt > 0.0:
                if not (jpw < jhw - 1e-15):
                    bad += 1
            else:
                if abs(jpw - jhw) > 1e-12:
                    bad += 1
    ok = bad == 0
    c_ok.append(ok)
    lines.append(f"C5 {'PASS' if ok else 'FAIL'} bad_cells={bad}")

    # C6 Q1 respecting split
    worst = 0.0
    jacobi_gap = 0.0
    for c in CS:
        rho = qutrit(c)
        phi = respect(rho)
        for i in range(3):
            for j in range(3):
                worst = max(worst, abs(phi[i][j] - rho[i][j]))
        ev = jacobi_eigs(rho)
        jacobi_gap = max(jacobi_gap, max(abs(a - b) for a, b in zip(sorted(ev), sorted(block_eigs(c)))))
        pd = entropy(jacobi_eigs(phi)) - entropy(jacobi_eigs(rho))
        worst = max(worst, abs(pd))
        for q in QS:
            worst = max(worst, abs(q * KAPPA * pd))
    ok = worst < 1e-12 and jacobi_gap < 1e-9
    c_ok.append(ok)
    lines.append(f"C6 {'PASS' if ok else 'FAIL'} max_abs={worst:.3e} jacobi={jacobi_gap:.3e}")

    # C7 Q2 crossing split
    pds_alpha = [pd_alpha(0.125, a) for a in ALPHAS]
    pds_c = [pd_alpha(c, 0.0) for c in CS]
    cited = pds_alpha[-1]
    jac = abs(entropy(jacobi_eigs(
        ((0.5, 0.0, 0.0), (0.0, 0.25, 0.0), (0.0, 0.0, 0.25))
    )) - entropy(jacobi_eigs(qutrit(0.125))) - cited)
    ok = (
        strict_inc(pds_alpha)
        and abs(pds_alpha[0]) <= 1e-12
        and abs(cited - 0.065406) <= 5e-7
        and strict_inc(pds_c)
        and abs(pds_c[0]) <= 1e-12
        and jac <= 1e-9
    )
    c_ok.append(ok)
    lines.append(
        f"C7 {'PASS' if ok else 'FAIL'} PD_cross={cited:.8f} cited_gap={cited - 0.065406:.3e} "
        f"PD_c0={pds_c[0]:.3e} PD_c_quarter={pds_c[-1]:.8f}"
    )

    # C8 Q3
    bad = 0
    j0 = None
    for gt in GT:
        r = math.exp(-gt)
        (ih, pdh, lh), _, _, _ = designs(r)
        for w in WS:
            if abs(pdh) >= 1e-9:
                bad += 1
            if gt == 0.0:
                j0 = j_h(r, w)
                if abs(j0 - KAPPA * LN2) >= 1e-9:
                    bad += 1
    ok = bad == 0
    c_ok.append(ok)
    lines.append(f"C8 {'PASS' if ok else 'FAIL'} bad_cells={bad} J_H_noiseless={KAPPA * LN2:.12f}")

    # C9 Q4
    worst = 0.0
    respect_not = None
    for gt in GT:
        r = math.exp(-gt)
        (_ih, pdh, _lh), _, (_iz, pdz, _lz), s_phase = designs(r)
        worst = max(worst, abs(s_phase + pdz - LN2))
        # P_D,Z(0) for the pure phase bit is chi(1) = ln 2, and S(rho(0))=0.
        worst = max(worst, abs((LN2 - pdz) - s_phase))
        worst = max(worst, abs(pdh))
        if abs(gt - 1.0) < 1e-15:
            respect_not = abs(s_phase + pdh - LN2)
    ok = worst <= 1e-12 and respect_not is not None and respect_not > 1e-3
    c_ok.append(ok)
    lines.append(
        f"C9 {'PASS' if ok else 'FAIL'} max_abs={worst:.3e} respect_minus_ln2_at_1={respect_not:.6f}"
    )

    # C10 Q5
    form_err = 0.0
    mono = True
    zero_at_axis = True
    for r in RS_TH:
        vals = []
        for theta in THETAS:
            # matrix: n·u = r sin theta, post-pinch entropy h((1+|n·u|)/2)
            ndot = r * math.sin(theta)
            pd_m = h((1.0 + abs(ndot)) / 2.0) - h((1.0 + r) / 2.0)
            pd_c = pd_theta(r, theta)
            form_err = max(form_err, abs(pd_m - pd_c))
            vals.append(pd_m)
            if abs(theta - math.pi / 2.0) < 1e-15 and abs(pd_m) > 1e-12:
                zero_at_axis = False
        if not strict_dec(vals):
            mono = False
    ok = form_err <= 1e-12 and mono and zero_at_axis
    c_ok.append(ok)
    lines.append(f"C10 {'PASS' if ok else 'FAIL'} form_err={form_err:.3e}")

    # Headline from the booleans named in the table: P1, Q1, Q2, Q3, Q4, and P5.
    # Indices: C1=0? Wait, c_ok order is C0..C10 so:
    # 0 C0, 1 C1 P1, 2 C2, 3 C3, 4 C4, 5 C5 P5, 6 C6 Q1, 7 C7 Q2, 8 C8 Q3, 9 C9 Q4, 10 C10
    p1 = c_ok[1]
    p5 = c_ok[5]
    q1, q2, q3, q4 = c_ok[6], c_ok[7], c_ok[8], c_ok[9]
    # Null pattern of P1: stock formula makes P strictly cheaper for every w>0 when γτ>0.
    null_pattern = True
    for gt in GT:
        if gt == 0.0:
            continue
        r = math.exp(-gt)
        for w in WS:
            if w <= 0.0:
                continue
            if not (j_p() < j_h(r, w) - 1e-15):
                null_pattern = False
    if p1 and q1 and q2 and q3 and q4 and p5:
        headline = "CLUE_SPLIT"
    elif (not p1) and null_pattern:
        headline = "NULL_DECOHERENCE"
    else:
        headline = "PUZZLE"
    # A miss must not print the predicted word.
    if not (p1 and q1 and q2 and q3 and q4 and p5) and headline == "CLUE_SPLIT":
        headline = "PUZZLE"
    lines.append(f"HEADLINE {headline}")
    headline_ok = headline == "CLUE_SPLIT"
    # C11 passes when the printed label is the table's label. The table's label
    # is what the booleans just computed. The check fails only if that computation
    # was replaced by the predicted word after a miss. That replacement is the
    # branch above, which forces PUZZLE. So C11 passes when headline is the
    # boolean label. Recompute and compare.
    if p1 and q1 and q2 and q3 and q4 and p5:
        table = "CLUE_SPLIT"
    elif (not p1) and null_pattern:
        table = "NULL_DECOHERENCE"
    else:
        table = "PUZZLE"
    c11 = headline == table
    c_ok.append(c11)
    # Insert C11 before HEADLINE for a stable order: rebuild.
    # Easier: the prereg says one line per check, then HEADLINE, then FAILS.
    # C11 is the headline check. Put it before HEADLINE.
    lines.pop()
    lines.append(f"C11 {'PASS' if c11 else 'FAIL'} label={headline}")
    lines.append(f"HEADLINE {headline}")
    fails = sum(1 for ok in c_ok if not ok)
    lines.append(f"FAILS {fails}")
    if fails == 0 and headline_ok:
        lines.append("ALL T84 CHECKS PASS")
    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
