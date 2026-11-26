#!/usr/bin/env python3
"""Layer-counting rule for real systems (T15; measurement/LAYER_COUNT_RULE.md).

Two sides, kept separate:

  Observation (K_obs).  From a measured response kernel, count distinct in-band
  memory time constants by degree (a rhythm = a complex pole pair = 2).  Step 1
  never sees prices, argmin J, or the world's spectrum.

  Prediction (K*).  From a measured (or modelled) excess-error curve ε_K and the
  stake ratio R, return the cheapest layer count.  This is always argmin_K J,
  which equals the lower-convex-hull increment test (KEYSTONE_NOTE §4).  On a
  finite domain, the from-0 count K*_0(R) = #{K >= 1 : R d_K > 1} equals the
  leftmost argmin for all R >= 0 if the decrements of ε_K are non-increasing
  (Fox 1966; L1 / N64 in PR #145); the converse holds under positive,
  pairwise distinct decrements (distinctness with the threshold decrement
  positive is enough; see theory/LAYER_CONVEXITY.md; d = (-2, -1) is a
  counterexample to a bare iff).
  When S/N has a peak, convexity can fail: use the hull, not the adjacent count.

  Comparison (for a later N56 test).  A raw K_obs ≠ K* is not by itself a miss.
  The observed design lies in the predicted band iff J_obs ≤ (1+ε+δ_meas) J*
  (THEORY §3).  The functions here implement that band; they do not score a
  real system.

Run a short synthetic check:  nice -n 19 python3 tools/layer_count_rule.py
"""
from __future__ import annotations

import json, math, os, sys, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
from scipy.optimize import least_squares

BIC_GATE = 10.0          # precommitted penalty choice (numerical scale from Kass & Raftery 1995)
K_MAX = 5                # default max degree fitted
RESOLUTION = 3.0         # precommitted default merge / relay factor
MAX_FIT_PTS = 800        # decimation cap for variable projection and BIC
PENCIL_MAX_PTS = 1500    # decimation cap for matrix pencil
PENCIL_RATE_BOUNDS = (0.05, 3.0)   # (a/T, b/dt) pencil rate clip
VARPRO_RATE_BOUNDS = (0.02, 4.0)   # (a/T, b/dt) variable-projection rate bounds
PAIR_SEED_DECAY_MULT = 3.0         # default decay rate 3/T for one-pair candidate seed
PAIR_SEED_PERIOD_DIV = 5.0         # default period T/5 for one-pair candidate seed


# --------------------------------------------------------------------------------------
# Model: g(t) = sum_i c_i e^{-b_i t}  +  sum_j e^{-d_j t}(c_{j1} cos ω_j t + c_{j2} sin ω_j t)
# A structure is (n_real, n_pair); its degree is n_real + 2 n_pair.
# Nonlinear parameters theta: log b (n_real), then (log d, log ω) per pair.
# --------------------------------------------------------------------------------------

def _basis(t, theta, nr, npair):
    cols = []
    for i in range(nr):
        cols.append(np.exp(-np.exp(theta[i]) * t))
    for j in range(npair):
        d = np.exp(theta[nr + 2 * j]); w = np.exp(theta[nr + 2 * j + 1])
        e = np.exp(-d * t)
        cols += [e * np.cos(w * t), e * np.sin(w * t)]
    if not cols:
        return np.zeros((len(t), 0))
    return np.column_stack(cols)


def _lin(Phi, y):
    if Phi.shape[1] == 0:
        return np.zeros(0), y.copy()
    c, *_ = np.linalg.lstsq(Phi, y, rcond=None)
    return c, y - Phi @ c


def _downsample(t, y, max_pts=MAX_FIT_PTS):
    n = len(t)
    if n <= max_pts:
        return t, y
    step = int(np.ceil(n / max_pts))
    return t[::step], y[::step]


def _pencil_poles(t, y, K, max_pts=PENCIL_MAX_PTS):
    """Continuous-time poles of a degree-K matrix-pencil fit (Hua & Sarkar 1990)."""
    dt0 = t[1] - t[0]
    step = max(1, int(np.ceil(len(t) / max_pts)))
    ys = y[::step]; dt = dt0 * step
    n = len(ys); L = n // 3
    if K == 0 or L <= K:
        return np.zeros(0, complex)
    H = np.lib.stride_tricks.sliding_window_view(ys, L + 1)
    _U, _s, Vt = np.linalg.svd(H, full_matrices=False)
    V = Vt[:K].T
    V1, V2 = V[:-1], V[1:]
    z = np.linalg.eigvals(np.linalg.pinv(V1) @ V2)
    with np.errstate(all="ignore"):
        p = np.log(z.astype(complex)) / dt
    return p


def _theta_from_poles(p, T, dt):
    """Split pencil poles into reals and pairs; return (nr, npair, theta).

    The pencil rate clip [a/T, b/Δt] is applied to both nonlinear parameters:
    the decay and, for a complex pair, the angular frequency.
    """
    rmin, rmax = PENCIL_RATE_BOUNDS[0] / T, PENCIL_RATE_BOUNDS[1] / dt
    reals, pairs, used = [], [], np.zeros(len(p), bool)
    for i, pi in enumerate(p):
        if used[i]:
            continue
        used[i] = True
        if abs(pi.imag) > 1e-6 * max(abs(pi.real), 1e-12) and abs(pi.imag) * dt < np.pi * 0.98:
            j = None
            for k in range(len(p)):
                if not used[k] and abs(p[k] - np.conj(pi)) < 1e-3 * abs(pi) + 1e-9:
                    j = k; break
            if j is not None:
                used[j] = True
                pairs.append((np.clip(-pi.real, rmin, rmax), np.clip(abs(pi.imag), rmin, rmax)))
                continue
        reals.append(np.clip(-pi.real if np.isfinite(pi.real) else rmin, rmin, rmax))
    theta = [np.log(b) for b in reals]
    for d, w in pairs:
        theta += [np.log(d), np.log(w)]
    return len(reals), len(pairs), np.array(theta, float)


def fit_structure(t, y, nr, npair, theta0):
    dt = t[1] - t[0]; T = t[-1] - t[0] + dt
    # The same variable-projection bounds [a/T, b/Δt] apply to both nonlinear
    # parameters (log decay and, for a pair, log angular frequency).
    lo = np.full(max(len(theta0), 1), np.log(VARPRO_RATE_BOUNDS[0] / T))[:len(theta0)]
    hi = np.full(max(len(theta0), 1), np.log(VARPRO_RATE_BOUNDS[1] / dt))[:len(theta0)]
    if len(theta0) == 0:
        c, r = _lin(np.zeros((len(t), 0)), y)
        return dict(nr=0, npair=0, theta=theta0, c=c, rss=float(r @ r))
    theta0 = np.clip(theta0, lo + 1e-9, hi - 1e-9)
    fun = lambda th: _lin(_basis(t, th, nr, npair), y)[1]
    try:
        sol = least_squares(fun, theta0, bounds=(lo, hi), method="trf", x_scale="jac",
                            max_nfev=30 * (len(theta0) + 1), ftol=1e-10, xtol=1e-10, gtol=1e-8)
        th = sol.x
    except Exception:
        th = theta0
    c, r = _lin(_basis(t, th, nr, npair), y)
    return dict(nr=nr, npair=npair, theta=th, c=c, rss=float(r @ r))


def fit_degree(t, y, K):
    """Deterministic best degree-K fit: matrix-pencil start, plus an all-real grid and one pair start."""
    dt = t[1] - t[0]; T = t[-1] - t[0] + dt
    if K == 0:
        return fit_structure(t, y, 0, 0, np.zeros(0))
    cands = []
    p = _pencil_poles(t, y, K)
    if len(p) == K:
        nr, npair, th = _theta_from_poles(p, T, dt)
        if nr + 2 * npair == K:
            cands.append((nr, npair, th))
    grid = np.linspace(np.log(1.0 / T), np.log(1.0 / dt), K + 2)[1:-1]
    cands.append((K, 0, grid.copy()))
    if K >= 2:
        g1 = np.linspace(np.log(1.0 / T), np.log(1.0 / dt), K + 1)[1:-1]
        th = np.concatenate([
            g1[: K - 2],
            [np.log(PAIR_SEED_DECAY_MULT / T), np.log(2 * np.pi * PAIR_SEED_PERIOD_DIV / T)],
        ])
        cands.append((K - 2, 1, th))
    best = None
    for nr, npair, th in cands:
        f = fit_structure(t, y, nr, npair, th)
        if best is None or f["rss"] < best["rss"]:
            best = f
    return best


def states(fit):
    """List of fitted states: dicts with kind, degree, rate(s), time scales."""
    out = []
    th = fit["theta"]; nr, npair = fit["nr"], fit["npair"]
    for i in range(nr):
        b = np.exp(th[i]); out.append(dict(kind="real", degree=1, tau=1 / b, period=None))
    for j in range(npair):
        d = np.exp(th[nr + 2 * j]); w = np.exp(th[nr + 2 * j + 1])
        out.append(dict(kind="pair", degree=2, tau=1 / d, period=2 * np.pi / w))
    return out


def in_band(s, band):
    """Real pole: tau in [lo, hi]. Complex pair: both decay time tau and period in [lo, hi]."""
    lo, hi = band
    if s["period"] is None:
        return lo <= s["tau"] <= hi
    return (lo <= s["tau"] <= hi) and (lo <= s["period"] <= hi)


def eval_fit(t, fit):
    c = fit["c"]
    return _basis(t, fit["theta"], fit["nr"], fit["npair"]) @ c if len(c) else np.zeros_like(t)


def hankel_rank(y, sigma, max_pts=PENCIL_MAX_PTS):
    """Cross-check: Hankel singular values above the Gavish–Donoho 2014 hard threshold,
    applied heuristically (Hankel noise entries are not independent).  Not used as K_obs."""
    step = max(1, int(np.ceil(len(y) / max_pts)))
    ys = y[::step]
    n = len(ys); L = n // 3
    H = np.lib.stride_tricks.sliding_window_view(ys, L + 1)
    s = np.linalg.svd(H, compute_uv=False)
    m, k = H.shape
    beta = min(m, k) / max(m, k)
    lam = np.sqrt(2 * (beta + 1) + 8 * beta / ((beta + 1) + np.sqrt(beta ** 2 + 14 * beta + 1)))
    thr = lam * np.sqrt(max(m, k)) * sigma
    return int(np.sum(s > thr)), s[:10].tolist(), float(thr)


RSS_REL_FLOOR = 1e-10  # residual RMS below 1e-10 of the record peak counts as an exact fit


def bic_score(rss, n, n_params):
    return n * np.log(max(rss, 1e-300) / n) + n_params * np.log(n)


def select_bic_degree(bic, gate=BIC_GATE):
    """Fit degrees 0..K_max. Degree 0 is always eligible. Accept degree K > 0
    only if it lowers BIC by at least `gate` against every lower degree j < K,
    and select the largest such degree (a rhythm may enter as a jump of 2).
    """
    bic = np.asarray(bic, float)
    ksel = 0
    for K in range(1, len(bic)):
        if np.all(bic[K] <= bic[:K] - gate):
            ksel = K
    return int(ksel)


def detect(t, y, band, k_max=K_MAX, seed=0, merge_factor=RESOLUTION):
    """Observation step 1.  Fits degrees 0..k_max on a (possibly downsampled) record;
    degree 0 is always eligible, degree K > 0 is accepted only if it lowers BIC by
    at least BIC_GATE against every lower degree, and the largest such degree is
    selected.  Drops out-of-band poles and merges same-kind in-band time constants
    closer than merge_factor (used only for single-record detection; `count_layers`
    classifies `states_in_band` before merging when `unit_records` are supplied).
    `seed` is accepted for API compatibility (fitting is deterministic).

    Returns the selected fit, K_det (in-band degree after the merge), and the BIC path.
    Takes only the record, the band and fit settings: no prices, no argmin J, no spectrum.
    """
    t = np.asarray(t, float); y = np.asarray(y, float)
    tf, yf = _downsample(t, y)
    n = len(yf)
    fits, bic = [], []
    # Residuals below floating-point resolution carry no information. Without
    # this floor, BIC differences on a noiseless record are roundoff and depend
    # on the BLAS thread count (sweep, 22 Nov 2026).
    rss_floor = n * (RSS_REL_FLOOR * max(float(np.max(np.abs(yf))), 1e-300)) ** 2
    for K in range(k_max + 1):
        f = fit_degree(tf, yf, K)
        # Re-evaluate RSS on the (downsampled) record used for the BIC, already in f["rss"].
        fits.append(f)
        bic.append(bic_score(max(f["rss"], rss_floor), n, 2 * K))
    bic = np.array(bic)
    Ksel = select_bic_degree(bic, BIC_GATE)
    f = fits[Ksel]
    st = states(f)
    st_in = [s for s in st if in_band(s, band)]
    st_merged = merge_close_states(st_in, merge_factor)
    k_det = sum(s["degree"] for s in st_merged)
    sigma_hat = np.sqrt(f["rss"] / max(n - 2 * Ksel - 1, 1))
    return dict(fit=f, K_total=Ksel, K_det=k_det, states=st, states_in_band=st_in,
                states_merged=st_merged, bic=bic.tolist(), sigma_hat=float(sigma_hat))


def _within_factor(a, b, factor):
    """True if same-kind states lie within `factor` on every time constant
    the rule uses: tau for a real pole; both tau and period for a pair.

    The comparison is strict (`ratio < factor`), so a ratio of exactly `factor`
    is not a match or a merge (it counts as a move of at least the factor).
    """
    if a["kind"] != b["kind"]:
        return False
    tau_ratio = max(a["tau"] / b["tau"], b["tau"] / a["tau"])
    if tau_ratio >= factor:
        return False
    if a["kind"] == "pair":
        pa, pb = a.get("period"), b.get("period")
        if pa is None or pb is None:
            return False
        if max(pa / pb, pb / pa) >= factor:
            return False
    return True


def _log_ratio_cost(a, b):
    """Sum of log time-constant ratios (tau, and period for a pair)."""
    cost = math.log(max(a["tau"] / b["tau"], b["tau"] / a["tau"]))
    if a["kind"] == "pair" and a.get("period") and b.get("period"):
        cost += math.log(max(a["period"] / b["period"], b["period"] / a["period"]))
    return cost


def max_cardinality_match(pooled, unit, factor=RESOLUTION):
    """Maximum-cardinality matching of same-kind poles under the factor.

    An edge exists only when `_within_factor` holds (for a complex pair, both
    the decay time and the period must lie within the factor). Among maximum-
    cardinality matchings, the rule takes the one with the smallest sum of
    log-ratios; remaining ties are broken by the lexicographically smaller
    tuple of matched pooled decay times, then by the sorted periods (a real
    pole has no period and sorts before any positive period).

    Returns the set of matched pooled indices. The graphs are tiny (degree at
    most K_max), so the matchings are enumerated.
    """
    n = len(pooled)
    m = len(unit)

    def rec(ia, used_b, chosen):
        if ia == n:
            return [list(chosen)]
        opts = rec(ia + 1, used_b, chosen)
        for ib in range(m):
            if ib in used_b:
                continue
            if not _within_factor(pooled[ia], unit[ib], factor):
                continue
            opts.extend(rec(ia + 1, used_b | {ib},
                            chosen + [(ia, ib, _log_ratio_cost(pooled[ia], unit[ib]))]))
        return opts

    matchings = rec(0, set(), [])

    def _period_sort_value(state):
        # A real pole has no period and sorts before any positive period.
        p = state.get("period")
        return (0,) if p is None else (1, float(p))

    def key(matching):
        card = len(matching)
        sum_log = sum(c for _, _, c in matching)
        taus = tuple(sorted(pooled[ia]["tau"] for ia, _, _ in matching))
        periods = tuple(sorted(_period_sort_value(pooled[ia]) for ia, _, _ in matching))
        return (-card, sum_log, taus, periods)

    best = min(matchings, key=key)
    return {ia for ia, _, _ in best}


def merge_close_states(state_list, factor=RESOLUTION):
    """Merge same-kind states whose time constants differ by less than `factor`.
    Two close real poles count as one (degree 1); two close pairs count as one
    rhythm (degree 2) only when both the decay time and the period lie within
    the factor.  States of different kinds are never merged.  Local vs shared
    is applied by the caller before this function (pass one class at a time,
    and only poles the unit records matched to the same partners).
    """
    if factor <= 1 or len(state_list) <= 1:
        return list(state_list)
    out = []
    for kind, degree in (("real", 1), ("pair", 2)):
        group = sorted((s for s in state_list if s["kind"] == kind), key=lambda s: s["tau"])
        if not group:
            continue
        cur = dict(group[0])
        for s in group[1:]:
            if _within_factor(s, cur, factor):
                # geometric mid-point; keep the kind and degree of one representative
                cur = dict(cur)
                cur["tau"] = np.sqrt(cur["tau"] * s["tau"])
                if cur.get("period") is not None and s.get("period") is not None:
                    cur["period"] = np.sqrt(cur["period"] * s["period"])
            else:
                out.append(cur); cur = dict(s)
        out.append(cur)
    # other kinds, if any, pass through
    for s in state_list:
        if s["kind"] not in ("real", "pair"):
            out.append(s)
    return out


def merge_classified(classified, factor=RESOLUTION):
    """Merge only within a class, and only among poles that the unit records
    matched to the same partners (the same set of matching unit indices).
    Two pooled poles stay unmerged when different units match them to
    different partners, even if both are labelled shared and their time
    constants lie within the factor.
    """
    groups = {}
    for s in classified:
        key = (s.get("class"), tuple(s.get("matched_units") or []))
        groups.setdefault(key, []).append(s)
    merged = []
    for group in groups.values():
        merged.extend(merge_close_states(group, factor))
    return merged


def classify_local_shared(unit_states, pooled_states, factor=RESOLUTION):
    """Classify poles as local (present in isolated-unit responses) or shared
    (present only in the pooled response).  `unit_states` is a list of state-lists,
    one per isolated unit (or per-unit response to a unit-specific drive).

    Within each unit, same-kind poles are matched by `max_cardinality_match`
    (maximum cardinality under the factor; then minimum total log-ratio; then
    the sorted pooled decay times, then the sorted periods). A pooled pole is
    local iff it matches in every unit; otherwise it is shared. The set of
    matching unit indices is
    stored as `matched_units` so a later within-class merge can keep poles
    unmerged when different units match them to different partners.
    """
    matched_per_unit = [max_cardinality_match(pooled_states, u, factor) for u in unit_states]
    out = []
    for i, s in enumerate(pooled_states):
        units_hit = [u for u, m in enumerate(matched_per_unit) if i in m]
        local = bool(unit_states) and len(units_hit) == len(unit_states)
        d = dict(s)
        d["class"] = "local" if local else "shared"
        d["matched_units"] = units_hit
        out.append(d)
    return out


def _matched(s, pool, factor):
    """True if `s` has a same-kind partner in `pool` within the factor
    (for a pair, both decay time and period). Ratio >= factor is a move."""
    return any(_within_factor(s, b, factor) for b in pool)


def relay_class(baseline_states, bypass_states, factor=RESOLUTION):
    """Intervene on one candidate level (bypass it, or replace it with a pure delay).

    The candidate is a layer iff the in-band pole set changes: some pole disappears
    or moves by at least `factor` (ratio >= factor).  If the pole set is unchanged
    (only a delay disappeared), it is a relay (CT16).  The caller passes in-band
    states only.
    """
    disappeared = [s for s in baseline_states if not _matched(s, bypass_states, factor)]
    appeared = [s for s in bypass_states if not _matched(s, baseline_states, factor)]
    return "layer" if (disappeared or appeared) else "relay"


def relay_test(baseline_states, bypass_states, factor=RESOLUTION):
    """Per-state labels after a `relay_class` on the same pair of records.

    If the intervention shows a layer, every unmatched baseline pole is a layer
    and matched poles stay layers (they were not the thing removed).  If it shows
    a relay, unmatched baseline poles are relays (only a delay disappeared) and
    matched poles stay layers.
    """
    outcome = relay_class(baseline_states, bypass_states, factor)
    out = []
    for s in baseline_states:
        d = dict(s)
        if _matched(s, bypass_states, factor):
            d["role"] = "layer"
        else:
            d["role"] = "layer" if outcome == "layer" else "relay"
        out.append(d)
    d0 = dict(classification=outcome)
    return out, d0


def count_layers(t, y, band, n_boot=0, seed=0, k_max=K_MAX, merge_factor=RESOLUTION,
                 unit_records=None, bypass=None):
    """The observation rule.  K_obs is the in-band, within-class-merged degree.

    unit_records: optional list of (t, y) isolated-unit records, used to classify
    in-band poles as local vs shared *before* merging, then merge only within a
    class and only among poles the unit records matched to the same partners.
    bypass: optional (t, y) record after bypassing a candidate level or replacing it
    with a pure delay; classifies the candidate level as 'layer' or 'relay' without
    changing K_obs (a relay holds no pole of its own).

    A parametric bootstrap, when requested, resamples the pooled record and each
    unit record and percentiles the same classify-then-merge count (not detect's
    merged degree).
    """
    d = detect(t, y, band, k_max=k_max, seed=seed, merge_factor=merge_factor)
    k_hsv, _sv, _thr = hankel_rank(y if len(y) <= 4000 else y[::max(1, len(y)//2000)], d["sigma_hat"])
    classified = None
    unit_detects = []
    if unit_records:
        unit_states = []
        for tu, yu in unit_records:
            du = detect(tu, yu, band, k_max=k_max, seed=seed, merge_factor=merge_factor)
            unit_detects.append((tu, du))
            unit_states.append(du["states_in_band"])
        classified = classify_local_shared(unit_states, d["states_in_band"], merge_factor)
        merged = merge_classified(classified, merge_factor)
    else:
        merged = d["states_merged"]
    roles = None
    relay_classification = None
    if bypass is not None:
        tb, yb = bypass
        db = detect(tb, yb, band, k_max=k_max, seed=seed, merge_factor=merge_factor)
        roles, relay_meta = relay_test(merged, db["states_in_band"], merge_factor)
        relay_classification = relay_meta["classification"]
    k_obs = sum(s["degree"] for s in merged)
    out = dict(K_obs=k_obs, K_det=k_obs, K_hsv=k_hsv, K_total=d["K_total"],
               sigma_hat=d["sigma_hat"], bic=d["bic"],
               states=[{k: (float(v) if isinstance(v, (float, np.floating)) else v)
                        for k, v in s.items()} for s in merged],
               classified=classified, roles=roles,
               relay_classification=relay_classification)
    lo = hi = k_obs
    if n_boot:
        rng = np.random.default_rng(seed + 1)
        g = eval_fit(t, d["fit"])
        ks = []
        for b in range(n_boot):
            yb = g + rng.normal(0, d["sigma_hat"], len(t))
            boot_units = None
            if unit_records:
                boot_units = []
                for tu, du in unit_detects:
                    gu = eval_fit(tu, du["fit"])
                    yub = gu + rng.normal(0, du["sigma_hat"], len(tu))
                    boot_units.append((tu, yub))
            ks.append(count_layers(
                t, yb, band, n_boot=0, seed=seed + 100 + b, k_max=k_max,
                merge_factor=merge_factor, unit_records=boot_units, bypass=None,
            )["K_obs"])
        ks = np.array(ks)
        lo = int(np.percentile(ks, 5, method="lower"))
        hi = int(np.percentile(ks, 95, method="higher"))
        vals, cnt = np.unique(ks, return_counts=True)
        out.update(boot=ks.tolist(), K_mode=int(vals[np.argmax(cnt)]), K_lo=lo, K_hi=hi,
                   boot_agree=float(np.mean(ks == k_obs)))
    out["interval"] = [lo, hi]
    return out


# --------------------------------------------------------------------------------------
# Prediction side: K* from an excess-error curve.  No fitting.
# --------------------------------------------------------------------------------------

def decrements(eps):
    eps = np.asarray(eps, float)
    return eps[:-1] - eps[1:]


def is_convex(eps, tol=0.0):
    """True iff the decrements are non-increasing, up to `tol` (L1's premise)."""
    d = decrements(eps)
    return bool(np.all(d[1:] <= d[:-1] + tol))


def n60_from(eps, R, k0=0):
    """N60-from-k0: k0 + #{K > k0 : R (ε_{K-1} − ε_K) > 1}."""
    d = decrements(eps)
    return int(k0 + sum(1 for K, dk in enumerate(d, start=1) if K > k0 and R * dk > 1))


def n60_as_written(eps, R):
    """N60 as written, starting at 1: 1 + #{k ≥ 2 : R (ε_{k−1} − ε_k) > 1}.
    This has the known K* = 0 hole: when the first increment does not pay, the
    formula still returns 1.  Prefer n60_from(..., k0=0) when K = 0 is allowed.
    """
    d = decrements(eps)
    return int(1 + sum(1 for K, dk in enumerate(d, start=1) if K >= 2 and R * dk > 1))


def J_of_K(eps, R, K):
    return K + R * (1.0 + float(eps[K]))


def argmin_J(eps, R, leftmost=True):
    Js = [J_of_K(eps, R, K) for K in range(len(eps))]
    m = min(Js)
    # leftmost on a numerical tie
    for K, j in enumerate(Js):
        if j <= m + 1e-15:
            return K if leftmost else max(k for k, jj in enumerate(Js) if jj <= m + 1e-15)
    return int(np.argmin(Js))


def lower_hull(eps):
    """Lower convex hull vertices of {(K, ε_K)}, as a list of (K, ε_K)."""
    hull = []
    for k, e in enumerate(np.asarray(eps, float)):
        while len(hull) >= 2:
            k1, e1 = hull[-2]; k2, e2 = hull[-1]
            if (k2 - k1) * (e - e1) <= (k - k1) * (e2 - e1) + 1e-15:
                hull.pop()
            else:
                break
        hull.append((int(k), float(e)))
    return hull


def hull_increment(eps, R):
    """Leftmost minimizer of J by the lower-convex-hull increment test (KEYSTONE_NOTE §4).
    Walk hull vertices k_i and jump to k_{i+1} iff R (ε_{k_i} − ε_{k_{i+1}}) > (k_{i+1} − k_i).
    An identity for any real sequence ε_K: equals the leftmost argmin of J.
    """
    h = lower_hull(eps)
    k_star = h[0][0]
    for (k1, e1), (k2, e2) in zip(h, h[1:]):
        if R * (e1 - e2) > (k2 - k1):
            k_star = k2
        else:
            break
    return int(k_star)


def predict_count(eps, R, tol=1e-12):
    """Predicted K* and the method used.

    Always reports the leftmost argmin and the hull increment (they must agree).
    If the decrements are non-increasing, the adjacent N60-from-0 count is exact
    and is the method recorded; otherwise the method is the lower-convex-hull
    test, which is the rule for peaked (rhythmic) ε curves.
    """
    eps = np.asarray(eps, float)
    convex = is_convex(eps, tol)
    k_arg = argmin_J(eps, R)
    k_hull = hull_increment(eps, R)
    k_n60 = n60_from(eps, R, k0=0)
    k_written = n60_as_written(eps, R)
    method = "n60-from-0" if convex else "lower-convex-hull"
    k = int(k_n60 if convex else k_hull)
    return dict(K_star=k, method=method, convex=bool(convex),
                K_argmin=int(k_arg), K_hull=int(k_hull),
                K_n60=int(k_n60), K_n60_as_written=int(k_written))


def cost_band(J_by_K, eps, delta_meas=0.0):
    """Counts whose reduced cost lies in the THEORY §3 band:
    {K : J(K) ≤ (1 + ε + δ_meas) J*}.  This is the prediction-side band, never
    computed inside count_layers.
    """
    J = {int(k): float(v) for k, v in J_by_K.items()}
    jmin = min(J.values())
    cap = (1.0 + eps + delta_meas) * jmin
    return sorted(k for k, v in J.items() if v <= cap)


def in_cost_band(J_obs, J_star, eps, delta_meas=0.0):
    """True iff the observed design's cost lies in the predicted band."""
    return float(J_obs) <= (1.0 + eps + delta_meas) * float(J_star)


# --------------------------------------------------------------------------------------
# Synthetic testbed: OU-sum world in white noise (Model S).  Used only in checks.
# J(design) = h * degree + w * MSE(kernel; world).  κ, A, L omitted in this testbed.
# --------------------------------------------------------------------------------------

def _transfer_basis(fit, w):
    th = fit["theta"]; nr, npair = fit["nr"], fit["npair"]
    s = 1j * w
    cols = []
    for i in range(nr):
        cols.append(1.0 / (s + np.exp(th[i])))
    for j in range(npair):
        d = np.exp(th[nr + 2 * j]); om = np.exp(th[nr + 2 * j + 1])
        den = (s + d) ** 2 + om ** 2
        cols += [(s + d) / den, om / den]
    return np.column_stack(cols) if cols else np.zeros((len(w), 0), complex)


def _wgrid(fit, a, n_w=6000):
    th = fit["theta"]
    rates = np.exp(th) if len(th) else np.array([1.0])
    lo = min(np.min(a), rates.min()) * 1e-4; hi = max(np.max(a), rates.max()) * 1e4
    return np.exp(np.linspace(np.log(lo), np.log(hi), n_w))


def _spec(a, v, w):
    return (v[None, :] * 2 * a[None, :] / (a[None, :] ** 2 + w[:, None] ** 2)).sum(1)


def mse_kernel(fit, a, v, N, n_w=6000):
    """MSE of the causal filter with kernel `fit` on s = sum OU(a_j, v_j), y = s + white(N)."""
    a = np.asarray(a, float); v = np.asarray(v, float)
    w = _wgrid(fit, a, n_w)
    Phi = _transfer_basis(fit, w)
    G = Phi @ fit["c"] if Phi.shape[1] else np.zeros(len(w), complex)
    S = _spec(a, v, w)
    integrand = np.abs(1 - G) ** 2 * S + np.abs(G) ** 2 * N
    return float(np.trapezoid(integrand * w, np.log(w)) / np.pi)


def kernel_from_stores(b, g):
    """Fit dict for the K-store design of theory/layers_checks/stores.py:
    H = sum g_k b_k/(b_k + i ω), i.e. kernel sum g_k b_k e^{-b_k t}."""
    b = np.asarray(b, float); g = np.asarray(g, float)
    return dict(nr=len(b), npair=0, theta=np.log(b), c=g * b, rss=0.0)


def J_factory(a, v, N, h, w, band):
    def J_of(fit):
        deg = sum(s["degree"] for s in states(fit) if in_band(s, band))
        return h * deg + w * mse_kernel(fit, a, v, N)
    return J_of


# Default short grid for unit tests and the self-check (dt=0.5, T=400).
T_GRID = np.arange(800) * 0.5
BAND = (1.0, 300.0)


def _kernel_from_taus(nr_taus, pair=None):
    th, c = [], []
    for tau, amp in nr_taus:
        th.append(-np.log(tau)); c.append(amp / tau)
    npair = 0
    if pair is not None:
        tau, period, amp = pair
        th += [-np.log(tau), np.log(2 * np.pi / period)]; c += [amp / tau, 0.0]; npair = 1
    return dict(nr=len(nr_taus), npair=npair, theta=np.array(th, float), c=np.array(c, float), rss=0.0)


def tautology_worlds():
    """Worlds where the system is deliberately not at argmin J."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                    "theory", "layers_checks"))
    import stores
    cases = []
    a = np.array([1 / 5.0, 1 / 200.0]); v = np.array([1.0, 1.0]); N = 5.0
    rng = np.random.default_rng(3)
    E, designs = {}, {}
    for K in (1, 2, 3):
        mse, lb = stores.E_K(a, v, N, K, starts=8, rng=rng)
        b = np.exp(np.sort(lb)) if lb is not None else None
        _, g = stores.mse_given_b(a, v, b, N)
        E[K] = mse; designs[K] = (b, g)
    E0 = float(np.sum(v))
    for (h, w) in [(0.01, 1.0), (0.1, 1.0)]:
        Js = {0: w * E0}
        Js.update({K: h * K + w * E[K] for K in (1, 2, 3)})
        kstar = min(Js, key=Js.get)
        b1, g1 = designs[1]; b2, g2 = designs[2]
        over = kernel_from_stores(np.concatenate([b2, [1 / 200.0]]), np.concatenate([g2, [0.5]]))
        for name, f, ktrue in (("underbuilt", kernel_from_stores(b1, g1), 1),
                               ("at_K2", kernel_from_stores(b2, g2), 2),
                               ("overbuilt", over, 3)):
            cases.append(dict(name=name, h=h, w=w, a=a.tolist(), v=v.tolist(), N=N,
                              K_true=ktrue, K_star=int(kstar),
                              J_by_K={int(k): float(x) for k, x in Js.items()}, fit=f))
    return cases


def run_tautology(eps=0.01, noise=1e-3, seed=0):
    """Observation recovers the system's degree; the cost-band comparison does not
    force agreement with K* when the system is under- or over-built.
    """
    out = []
    rng = np.random.default_rng(seed)
    for c in tautology_worlds():
        g = eval_fit(T_GRID, c["fit"])
        y = g + rng.normal(0, noise * np.max(np.abs(g)), len(g))
        r = count_layers(T_GRID, y, BAND, seed=seed)
        J_of = J_factory(c["a"], c["v"], c["N"], c["h"], c["w"], BAND)
        J_obs = J_of(c["fit"])
        J_star = c["J_by_K"][c["K_star"]]
        band = cost_band(c["J_by_K"], eps)
        inside = in_cost_band(J_obs, J_star, eps)
        out.append(dict(name=c["name"], h=c["h"], K_true=c["K_true"], K_star=c["K_star"],
                        K_star_band=band, K_obs=r["K_obs"],
                        J_obs=float(J_obs), J_star=float(J_star), in_band=bool(inside)))
    return out


def main():
    t0 = time.time()
    res = {"prediction_identities": _prediction_selfcheck(), "tautology": {}}
    for e in (0.01, 0.05):
        res["tautology"]["eps%g" % e] = run_tautology(eps=e)
    res["runtime_s"] = round(time.time() - t0, 1)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "measurement", "layer_count", "RESULTS.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(json.dumps({k: res[k] for k in ("prediction_identities", "runtime_s")}, indent=1))


def _prediction_selfcheck():
    """Elementary identities used in the note; also run as pytest."""
    out = {}
    # Convex decreasing: N60-from-0, hull and argmin agree for every R.
    eps = [1.0, 0.4, 0.15, 0.05, 0.0]
    agree = all(predict_count(eps, R)["K_star"] == argmin_J(eps, R) == hull_increment(eps, R)
                == n60_from(eps, R, 0) for R in np.logspace(-2, 3, 250))
    out["convex_n60_equals_argmin"] = bool(agree)
    # K* = 0 hole: N60 as written returns 1 when the first increment does not pay.
    # At R = 0.5, d_1 = 0.6, R d_1 = 0.3 < 1, true argmin is 0; as-written returns 1.
    out["k0_hole_as_written"] = (n60_as_written(eps, 0.5) == 1 and n60_from(eps, 0.5, 0) == 0
                                 and argmin_J(eps, 0.5) == 0)
    # Peaked example of PR #145 (W = (0,1,0), weights (2,1,1)): E_inf = 0, so
    # excess E_K - E_inf = (1, 2/3, 0) with decrements 1/3 then 2/3 and multiplier w/h = 3.
    peaked_excess = [1.0, 2.0 / 3.0, 0.0]
    out["peaked_not_convex"] = (not is_convex(peaked_excess))
    p = predict_count(peaked_excess, 3.0)
    out["peaked_wh_3"] = dict(K_star=p["K_star"], method=p["method"],
                              K_n60=p["K_n60"], K_argmin=p["K_argmin"])
    out["peaked_hull_recovers_argmin"] = (p["K_star"] == 2 and p["K_n60"] == 1
                                          and p["method"] == "lower-convex-hull")
    # Converse of L1 (positive, pairwise distinct decrements): an ascent makes the
    # adjacent count miss the argmin on an open interval of the multiplier.
    out["l1_converse"] = (p["K_n60"] != p["K_argmin"])
    # Counterexample to a bare iff (N64 / L1): d = (-2, -1), seq = (-3, -1, 0).
    cex = [-3.0, -1.0, 0.0]
    out["l1_bare_iff_counterexample"] = (
        not is_convex(cex)
        and all(n60_from(cex, R, 0) == argmin_J(cex, R) == 0 for R in (0.0, 0.5, 2.0, 10.0))
    )
    # Exclusivity of the converse is false: d = (1, 2, -1), seq = (2, 1, -1, 0).
    # At R = 0.75 the from-0 count is 1 and the argmin is 2.
    excl = [2.0, 1.0, -1.0, 0.0]
    out["l1_converse_not_only_positive"] = (
        not is_convex(excl)
        and n60_from(excl, 0.75, 0) == 1 and argmin_J(excl, 0.75) == 2
        and n60_from(excl, 0.6, 0) == 1 and argmin_J(excl, 0.6) == 0
    )
    return out


if __name__ == "__main__":
    main()
