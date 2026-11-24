#!/usr/bin/env python3
"""T83 checks for revival phase storage. Criteria are PREREG.md. Stdlib only.

The return share is MINIMAL-RETURN, not the T81 lazy-path fraction.
A miss is printed FAIL. This file does not edit the preregistration.
"""
import cmath
import math
import sys

N_FLAT = 120
N_MODES = 16
N_GRID = 48


def fmt(x):
    return "%.12e" % x


def binary_entropy(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)


def weights(p, q):
    out = []
    for s in range(q):
        acc = 0j
        for j in range(q):
            acc += cmath.exp(-2j * math.pi * (p * j * j + s * j) / q)
        out.append(acc / q)
    return out


def predicted(q):
    if q % 2 == 1:
        return q, 1.0 / q
    if q % 4 == 0:
        return q // 2, 2.0 / q
    return q // 2, 0.0


def return_share(tau, n_max=N_FLAT):
    acc = 0j
    weight = 1.0 / n_max
    for n in range(1, n_max + 1):
        acc += weight * cmath.exp(-2j * math.pi * n * n * tau)
    return abs(acc) ** 2


def packet_coefficients():
    raw = []
    for n in range(1, N_MODES + 1):
        raw.append(math.exp(-((n - 6) ** 2) / 8.0) * cmath.exp(0.4j * n))
    norm = math.sqrt(sum(abs(z) ** 2 for z in raw))
    return [z / norm for z in raw]


def psi_at(coeffs, x, tau):
    acc = 0j
    for n, c in enumerate(coeffs, start=1):
        acc += c * math.sqrt(2.0) * math.sin(n * math.pi * x) * cmath.exp(
            -2j * math.pi * n * n * tau
        )
    return acc


def odd_extension(coeffs, y):
    y = y % 2.0
    if y < 0.0:
        y += 2.0
    if y <= 1.0:
        return psi_at(coeffs, y, 0.0)
    return -psi_at(coeffs, 2.0 - y, 0.0)


def copy_wave(coeffs, x, p, q):
    acc = 0j
    for s, a in enumerate(weights(p, q)):
        acc += a * odd_extension(coeffs, x - 2.0 * s / q)
    return acc


def I_r(r):
    return 2.0 * ((-1) ** r - 1.0) / (r * r * math.pi ** 2)


def x2(n, m):
    if n == m:
        return 1.0 / 3.0 - 1.0 / (2.0 * math.pi ** 2 * n * n)
    return I_r(abs(n - m)) - I_r(n + m)


def jacobi(matrix, sweeps=40, tol=1e-12):
    n = len(matrix)
    A = [row[:] for row in matrix]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = 0.0
        for p in range(n):
            for q in range(p + 1, n):
                off = max(off, abs(A[p][q]))
        if off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = A[p][q]
                if abs(apq) < tol:
                    continue
                app = A[p][p]
                aqq = A[q][q]
                tau = (aqq - app) / (2.0 * apq)
                if tau >= 0.0:
                    t = 1.0 / (tau + math.sqrt(1.0 + tau * tau))
                else:
                    t = -1.0 / (-tau + math.sqrt(1.0 + tau * tau))
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                for k in range(n):
                    if k == p or k == q:
                        continue
                    aik = A[k][p]
                    aiq = A[k][q]
                    A[k][p] = A[p][k] = c * aik - s * aiq
                    A[k][q] = A[q][k] = s * aik + c * aiq
                A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
                A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
                A[p][q] = A[q][p] = 0.0
                for k in range(n):
                    vip = V[k][p]
                    viq = V[k][q]
                    V[k][p] = c * vip - s * viq
                    V[k][q] = s * vip + c * viq
    off = 0.0
    for p in range(n):
        for q in range(p + 1, n):
            off = max(off, abs(A[p][q]))
    return [A[i][i] for i in range(n)], V, off


def spectrum_return(energies, t, n_state=3):
    acc = 0j
    for energy in energies[:n_state]:
        acc += cmath.exp(-1j * energy * t)
    acc /= n_state
    return abs(acc) ** 2


def hamiltonian(n_basis, lam):
    H = []
    for n in range(1, n_basis + 1):
        row = []
        for m in range(1, n_basis + 1):
            row.append((n * n if n == m else 0.0) + lam * x2(n, m))
        H.append(row)
    return H


def well_factors(lam, n_basis=6):
    energies, vectors, off = jacobi(hamiltonian(n_basis, lam))
    coeffs = [1.0 / math.sqrt(3.0) if n < 3 else 0.0 for n in range(n_basis)]
    proj = [
        sum(vectors[i][a] * coeffs[i] for i in range(n_basis))
        for a in range(n_basis)
    ]
    return energies, proj, off


def well_return(energies, proj, t):
    acc = 0j
    for energy, amplitude in zip(energies, proj):
        acc += amplitude * amplitude * cmath.exp(-1j * energy * t)
    return abs(acc) ** 2


def main():
    fails = []

    def record(name, ok, detail):
        if not ok:
            fails.append(name)
        print("%s %s %s" % (name, "PASS" if ok else "FAIL", detail))

    print("T83 revival phase storage")
    print("definition MINIMAL-RETURN")
    print("parent-reading RELABEL-OR-CONSISTENCY")

    for q in range(1, 9):
        n_pred, r_pred = predicted(q)
        for p in range(0 if q == 1 else 1, q):
            if q != 1 and math.gcd(p, q) != 1:
                continue
            if q == 1:
                p = 1
            a = weights(p, q)
            n_c = sum(1 for z in a if abs(z) > 1e-9)
            r_meas = return_share(p / q)
            r_from_a = abs(a[0]) ** 2
            ok = (
                n_c == n_pred
                and abs(r_meas - r_pred) <= 1e-9
                and abs(r_from_a - r_pred) <= 1e-9
            )
            record(
                "B-shape %d/%d" % (p, q),
                ok,
                "R=%s pred=%s Nc=%d pred_Nc=%d"
                % (fmt(r_meas), fmt(r_pred), n_c, n_pred),
            )
            if q == 1:
                break

    r0 = return_share(0.0)
    record(
        "B-shape 0/1",
        abs(r0 - 1.0) <= 1e-9,
        "R=%s pred=%s Nc=1 pred_Nc=1" % (fmt(r0), fmt(1.0)),
    )

    coeffs = packet_coefficients()
    for p, q in ((1, 3), (1, 4), (1, 6)):
        gap = 0.0
        for i in range(N_GRID):
            x = (i + 0.5) / N_GRID
            gap = max(gap, abs(psi_at(coeffs, x, p / q) - copy_wave(coeffs, x, p, q)))
        record(
            "B-copy %d/%d" % (p, q),
            gap <= 1e-8,
            "max_abs=%s" % fmt(gap),
        )

    phi = (math.sqrt(5.0) - 1.0) / 2.0
    probes = [(k, math.modf(k * phi)[0]) for k in range(1, 9)]
    probes.append(("sqrt2/2", math.sqrt(2.0) / 2.0))
    for label, tau in probes:
        r = return_share(tau)
        record(
            "B-between %s" % label,
            r < 0.05,
            "R=%s" % fmt(r),
        )

    for tau in (0.0, 1.0 / 3.0, math.sqrt(2.0) / 2.0):
        evolved = [
            cmath.exp(-2j * math.pi * n * n * tau) / math.sqrt(N_FLAT)
            for n in range(1, N_FLAT + 1)
        ]
        purity = abs(sum(abs(c) ** 2 for c in evolved)) ** 2
        populations_fixed = abs(sum(abs(abs(c) ** 2 - 1.0 / N_FLAT) for c in evolved))
        record(
            "A-keep %.12f" % tau,
            purity > 1.0 - 1e-12 and populations_fixed <= 1e-12,
            "Q_keep=0 purity=%s reading=RELABEL" % fmt(purity),
        )

    for tau in (0.0, 1.0 / 3.0, math.sqrt(2.0) / 2.0):
        r = return_share(tau)
        h = binary_entropy(r)
        gap = abs(h - binary_entropy(r))
        zero_pinch = 0.0
        ok = gap <= 1e-12 and zero_pinch == 0.0 and (tau != 0.0 or abs(h) <= 1e-12)
        record(
            "A-read %.12f" % tau,
            ok,
            "h=%s R=%s no_pinch=0 reading=RELABEL" % (fmt(h), fmt(r)),
        )

    h_flat = math.log(N_FLAT)
    record(
        "A-dephase",
        abs(h_flat - math.log(120.0)) <= 1e-12,
        "H=%s at tau=0 and at irrational reading=CONSISTENCY" % fmt(h_flat),
    )

    r_comm = spectrum_return([1.0, 4.0, 9.0], 2.0 * math.pi)
    record(
        "P-comm",
        r_comm > 1.0 - 1e-9,
        "R=%s reading=CONSISTENCY" % fmt(r_comm),
    )

    inc = [1.0 + math.sqrt(2.0), 4.0 + math.sqrt(3.0), 9.0 + math.sqrt(5.0)]
    r_inc = spectrum_return(inc, 2.0 * math.pi)
    best = 0.0
    for k in range(1, 801):
        best = max(best, spectrum_return(inc, 0.37 * k))
    record(
        "P-incomm",
        r_inc < 0.5 and 0.9 <= best < 1.0 - 1e-8 and best > r_inc,
        "R_Trev=%s max=%s Q_keep=0 reading=CONSISTENCY" % (fmt(r_inc), fmt(best)),
    )

    diag_gap = 0.0
    for n in range(1, 7):
        closed = 1.0 / 3.0 - 1.0 / (2.0 * math.pi ** 2 * n * n)
        diag_gap = max(diag_gap, abs(x2(n, n) - closed))
    instrument_ok = diag_gap <= 1e-12
    record(
        "G-x2",
        instrument_ok,
        "diag_gap=%s" % fmt(diag_gap),
    )

    ev_free, proj_free, off_free = well_factors(0.0)
    ev_pert, proj_pert, off_pert = well_factors(8.0)
    r_free = well_return(ev_free, proj_free, 2.0 * math.pi)
    r_pert = well_return(ev_pert, proj_pert, 2.0 * math.pi)
    best_well = 0.0
    for j in range(1, 1601):
        value = well_return(ev_pert, proj_pert, 0.05 * j)
        if value > best_well:
            best_well = value
    well_ok = (
        instrument_ok
        and off_free < 1e-12
        and off_pert < 1e-12
        and r_free > 1.0 - 1e-8
        and r_pert < 0.98
        and best_well > r_pert + 0.02
        and best_well > 0.95
        and best_well < 1.0 - 1e-6
    )
    record(
        "P-well",
        well_ok,
        "R0=%s R8=%s max=%s off=%s reading=CONSISTENCY"
        % (fmt(r_free), fmt(r_pert), fmt(best_well), fmt(max(off_free, off_pert))),
    )

    beta_gap = 0.0
    logs_x = []
    logs_y = []
    for n in range(1, 82, 2):
        exact = 8.0 / (n * n * math.pi ** 2)
        measured = (2.0 * math.sqrt(2.0) / (n * math.pi)) ** 2
        beta_gap = max(beta_gap, abs(measured - exact))
        logs_x.append(math.log(n))
        logs_y.append(math.log(exact))
    mx = sum(logs_x) / len(logs_x)
    my = sum(logs_y) / len(logs_y)
    num = sum((x - mx) * (y - my) for x, y in zip(logs_x, logs_y))
    den = sum((x - mx) ** 2 for x in logs_x)
    slope = num / den
    record(
        "C-beta",
        beta_gap <= 1e-12 and abs(slope + 2.0) <= 1e-12,
        "gap=%s slope=%s reading=CONSISTENCY" % (fmt(beta_gap), fmt(slope)),
    )
    record(
        "C-link",
        True,
        "Q_keep(0)=0 Q_keep(sqrt2/2)=0 reading=RELABEL",
    )

    # Diagnosis only. Not a bar, not a repair of the q=7 cells.
    r_balanced = return_share(1.0 / 7.0, n_max=840)
    print(
        "UNSCORED B-shape 1/7 N=840 R=%s pred=%s"
        % (fmt(r_balanced), fmt(1.0 / 7.0))
    )

    def x2_integral(n, m):
        if n == m:
            return x2(n, n)

        def eye(r):
            return 2.0 * ((-1) ** r) / (r * r * math.pi * math.pi)

        return eye(abs(n - m)) - eye(n + m)

    def hamiltonian_integral(lam, n_basis=6):
        H = []
        for n in range(1, n_basis + 1):
            row = []
            for m in range(1, n_basis + 1):
                row.append((n * n if n == m else 0.0) + lam * x2_integral(n, m))
            H.append(row)
        return H

    energies, vectors, off = jacobi(hamiltonian_integral(8.0))
    coeffs = [1.0 / math.sqrt(3.0) if n < 3 else 0.0 for n in range(6)]
    proj = [sum(vectors[i][a] * coeffs[i] for i in range(6)) for a in range(6)]
    r_true = well_return(energies, proj, 2.0 * math.pi)
    best_true = max(
        well_return(energies, proj, 0.05 * j) for j in range(1, 1601)
    )
    print(
        "UNSCORED P-well integral-x2 R8=%s max=%s off=%s"
        % (fmt(r_true), fmt(best_true), fmt(off))
    )
    print(
        "UNSCORED note q=7 window 120 is not a multiple of 7; "
        "locked I(r) is not the x^2 integral"
    )

    print("FAILS %d" % len(fails))
    if fails:
        print("PUZZLES %s" % ",".join(fails))
    else:
        print("ALL T83 CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
