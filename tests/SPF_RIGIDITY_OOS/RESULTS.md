# SPF-RIGIDITY-OOS — MV10 power gate: GATE NOT MET (no prereg locked, no outcome computed)

Executor `queue-pick20` (for Ace; Chad t1914), Sunday 15 Nov 2026, about 4:50–5:15 PM ET (America/New_York). Queue protocol v2,
post-protocol pick 20, UNIFORM slot (ledger 96 unaided order, 97 rule_rank, 98 pick; outcome entry in `tests/SG_RANK/LEDGER.jsonl`).
THEORY.md not edited. **No CLAIM_MAP status changes; N13 stays OPEN; vigilance stays OPEN.**

## The item
From SPF-NOISE-PROXY S-1 (POST HOC): with the validated nowcast-noise proxy K_L0w, the consensus CG coefficients of UNEMP,
HOUSING, TBILL and RSLGOV exceed the optimal noisy-filter β^G by 2.5–6×. Lock "β̂ > β^G(K_L0w)" and its size on unseen data,
power first. Required standard (dispatch): a locked prereg that passes FRAMEWORK MV10 (`tools/power_gate.py`) before any outcome.

## What was done (pre-outcome only)
1. **Unseen data chosen:** the nine SPF variables whose CG β̂ has never been computed in this repo and that have ≥ 80 survey
   pairs before 2020 (LFK gate E1): NGDP, PGDP, CPROF, RGDP, RCONSUM, RNRESIN, RRESINV, RFEDGOV, CPI. Same window as the seen
   analysis (targets ≤ 2019Q4). Their LFK environment fits (`../LFK_SPF/results/env.json`, environment stage only) failed LFK's
   E2/E3 (α̂ at the bound 6, or corner at the 5,000-quarter bound); those gates were for estimating τ_E, which this item does not
   need: β^G needs only the fitted spectrum. Exposure: no actual-minus-forecast error and no CG regression was computed for any
   of the nine (the consensus files `../LFK_SPF/data/spf_*.csv` were not read). Literature exposure: CG regressions on SPF
   inflation are published (Coibion & Gorodnichenko 2015, as recalled, not re-opened); not used.
2. **Noise and prediction** (`prelock.py` → `results/prelock.{json,out}`; microdata `build_micro_oos.py` → `data/`):
   K_L0w by the SPF-NOISE-PROXY instrument; population β^G = model.moments(S, K_L0w, h=3, nf); its expectation and sampling sd at
   the planned n by simulating the optimal consensus in the fitted world (2,000 panels each); β^G uncertainty from 200 parametric
   environment re-fits × block bootstrap of the nowcast dispersion. Premise stated: Gaussian world, white sensing noise, best
   linear (= Bayes, under that premise) noisy filter (TELEGRAPH-LINEAR-PREMISE audit).
3. **Independent numerical check of the simulator:** at n = 20,000 the simulated mean β̂ matches the closed form within 0–12%
   for all nine (e.g. RNRESIN 0.348 vs 0.354; PGDP 1.340 vs 1.306; RGDP 0.182 vs 0.162). Calibration on SEEN variables
   (`calib_seen.py` → `results/calib_seen.out`): model sampling sd vs the published real NW SE is UNEMP 0.133 vs 0.230,
   HOUSING 0.167 vs 0.286, TBILL 0.150 vs 0.179, RSLGOV 0.561 vs 0.473. The simulator mostly **understates** real noise, so
   the power below is, if anything, optimistic.
4. **Planned statistic** (the design that would have been locked; `power.py`): pooled multiple
   c = Σ w_v (β̂_v − bias_v) β^G_v / Σ w_v (β^G_v)², w_v = 1/sd_v², bias_v = model finite-sample bias of the CG regression;
   percentile cluster bootstrap over variables. H_R (item, lower end of the post hoc size): c = 2.5. H_0 (theory: measured-input
   optimum of the Gaussian noisy filter): c = 1. PASS iff c_lo > 1; FAIL iff c_hi < 2.5 (MV10 form, κ = 1).

## Pre-lock numbers (`results/prelock.out`)
| Var | n | K_L0w [95% CI] | β^G pop [95% CI] | β^G at planned n | planned sd(β̂) | horizon G (diagnostic) |
|---|---|---|---|---|---|---|
| NGDP | 195 | 0.078 [0.006, 0.22] | 0.129 [0.038, 0.20] | 0.064 | 0.47 | +4.97 |
| PGDP | 195 | 0.020 [0.0007, 4.3] | 1.31 [0.063, 6.0] | 1.29 | 0.46 | −0.22 |
| CPROF | 195 | 0.27 [0.15, 0.68] | 0.25 [0.13, 0.61] | −0.04 | 4.00 | +1.30 |
| RGDP | 195 | 0.16 [0.089, 0.27] | 0.162 [0.083, 0.27] | 0.054 | 0.66 | +2.08 |
| RCONSUM | 149 | 0.16 [0.10, 0.25] | 0.159 [0.098, 0.24] | 0.082 | 0.51 | +2.22 |
| RNRESIN | 149 | 0.27 [0.16, 0.51] | 0.354 [0.22, 0.59] | 0.290 | 0.46 | +1.54 |
| RRESINV | 149 | 0.17 [0.085, 0.37] | 0.218 [0.11, 0.46] | 0.134 | 0.59 | +1.61 |
| RFEDGOV | 149 | 1.0 (above noise max: K not identified) | 0.81 [0.44, 1.19] | 0.649 | 1.16 | +0.86 |
| CPI | 149 | 0.015 [0.0008, 0.21] | 0.193 [0.026, 0.33] | 0.149 | 0.30 | +0.65 |

Plain reading: for quarterly growth and inflation series the optimal three-quarter-ahead forecast barely revises, so the CG
regression is nearly all noise (planned sd 1.3–16× the predicted β^G), and the one variable with a large β^G (PGDP) has a noise
measurement spanning four orders of magnitude.

## MV10 gate (`results/power.out`, 2,000 simulated studies × 1,000 bootstrap each; `results/power_sd08.out`)
| Variable set | heterogeneity τ of ln c | P(PASS \| c = 2.5) | P(FAIL \| c = 1) | gate (both ≥ 0.8) |
|---|---|---|---|---|
| A: all 8 with K identified (PGDP carries 85% of the information) | 0 | 0.62 | 0.60 | NOT MET |
| A | 0.4 | 0.56 | 0.55 | NOT MET |
| B: A minus variables whose β^G CI spans > ×10 (drops PGDP, CPI) | 0 | 0.39 | 0.37 | NOT MET |
| B | 0.4 | 0.40 | 0.33 | NOT MET |
| A, planned sd × 0.8 (optimistic, against the calibration) | 0 | 0.71 | 0.72 | NOT MET |
| A minus PGDP, sd × 0.8 | 0 | 0.57 | 0.57 | NOT MET |

**Verdict: GATE NOT MET.** No prereg was locked and no outcome statistic was computed for any unseen variable. Not a pass or a
fail of anything; the rigidity pattern stays POST HOC, N13 stays OPEN.

## Other unseen sources named in the item (not run; reasons)
- **Post-2019 data for the seen variables:** about 24 survey pairs each. Even the full 1968–2019 sample of the four seen variables
  carries information Σ(β^G/SE)² ≈ 3.9 (UNEMP 2.0, HOUSING 1.5, TBILL 0.28, RSLGOV 0.10; published SEs), sampling-only se(c) ≈ 0.51,
  just under the 0.54 the gate needs before any heterogeneity; a 24-pair sample has roughly 1/8 of that (se(c) ≈ 1.4). Not reachable.
- **Other horizons of the seen variables:** not independent of the seen h = 3 result (same series and forecasters); not out-of-sample.
- **SPF variables with short samples** (EMP 61 pairs, CORECPI/PCE/COREPCE 48, BAABOND 23): less information than the set above.
- **Livingston Survey, ECB SPF:** public, but need a new noise instrument for their designs (semiannual, 6/12-month horizons;
  ECB rolling and calendar-year horizons) validated on synthetic truth before any power claim. Queued as SPF-RIGIDITY-LIVINGSTON.

## Surprises (QUEUE rule 4)
- **weak:** the SPF's own unused variables cannot power the test: quarterly growth and inflation series are close to white at the
  3-quarter horizon, so the optimal filter's CG coefficient is small (0.13–0.35) against planned sd 0.3–0.7 (CPROF 4.0). The level
  series that produced the post hoc pattern are the only SPF series with usable CG precision.
- Horizon diagnostic G is large for NGDP (+4.97) and the real-activity series (+1.5 to +2.2): dispersion contamination growing with
  horizon, as SPF-NOISE-PROXY found for 6 of 7 seen variables (diagnostic only; no test).

## Validity
MV1 yes. MV2 partial (K_L0w validated on synthetic truth for the seven seen environments only; RFEDGOV not identified). MV7 in-model
check passed (closed form vs simulation). MV8/MV10: **failed** by the pre-lock power simulation, which is this item's result. MV9: code,
seeds (20261115+98, +99, +148), microdata sha256 in `data/SHA256.txt`; raw SPFmicrodata.xlsx sha256 in `../LFK_SPF/data/RAW_SHA256.txt`.

## Files
`build_micro_oos.py`, `prelock.py`, `power.py`, `calib_seen.py`, `data/micro_*.csv`, `results/prelock.{json,out,log}`,
`results/power.{json,out}`, `results/power_sd08.out`, `results/calib_seen.out`.
