# Independent review 067c485dd86517f7ffaad01486cbd696f690842b

*Reviewer: independent. I did not write the preregistrations, the memo, or the scored scripts. Tuesday 24 November 2026. Fork PR #26, pinned head `067c485dd86517f7ffaad01486cbd696f690842b`, branch `forge-dephasing-refresh`, base `forge-dephasing-crossover` `853e5a2f76a269df048854f8a593921eca3011ab`. This review does not edit `THEORY.md` or `CORE.md`, and it does not edit that branch.*

**Result label: observed in-model.** This review does not clear it. The arithmetic of the locked costs holds. Inside those costs the scored bars are identities. The short-period stake exponent is a consistency check of the square-root balance already labeled KNOWN in this repository.

A later lock, if one is added on `forge-dephasing-refresh` after this head, that tests whether the symmetric threshold near 4 is the fixed-price Poisson onset \(c^*=4\kappa kT\) (`theory/CLOCK_TERM_2026-11-23.md:126`, the \(a=1\), \(b=2\) branch) is outside this review. It is not scored.

The locks contain the hypothesis sentence of `CORE.md:7`: "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment."

## Findings

### High

**H1. Inside the locked refresh cost the scored bars cannot miss. They are NOT A TEST.** The closed forms are part of the lock (`theory/dephasing-refresh-2026-11-24/PREREG.md:66-106`), committed at `612b82e` before any scoring script. For \(\Theta=\gamma T\),

\[
\Pi_c(\Theta)=\frac{2\Theta^2}{1-(1+\Theta)e^{-\Theta}}.
\]

The series \(4+(8/3)\Theta+(7/9)\Theta^2+O(\Theta^3)\) is the expansion of that quotient. An independent expansion agrees, and \(\Pi_c(10^{-6})-4=2.666667\times 10^{-6}\), the first correction \((8/3)\times 10^{-6}\). So \(\Pi_c\to 4\). Accountings A and B differ by the constant \(-A/T\), so they share that boundary (`PREREG.md:84-89`). The stake elasticity equals the loss share, \(e=\bar L/(\bar L+u\bar L')\), which tends to \(1/2\) with the linear loss \(\bar L\sim u/4\).

The script scores those identities against themselves.

- R0 compares the closed derivative with a centered difference of the same function (`dephasing_refresh_checks.py:84-97`).
- R2 compares \(\Pi_c(0.01)\) with the series of the same \(\Pi_c\) (`:132-136`).
- R3 compares the optimum of that function with its own leading term (`:138-145`).
- R6 substitutes \(u=(3/s)^{1/3}\) into \(A/\tau+w\gamma^2\tau^2/6\) (`:167-175`). The loss share is \(1/3\) for every \(s\). The Gaussian envelope \(e^{-(\gamma t)^2}\) is not evaluated.
- R7 compares \(2\Pi_c(0.01)\) with twice the same series (`:177-181`).
- R8 adds \(0\) and a positive constant to a hardcoded rate \(1.0\), and sets the onset to \(2\cdot 1\cdot 2/1\) (`:183-195`).

The headline branch that would fire if the finite-hold limit were 16 compares the series of this \(\Pi_c\) with a window around 4 (`PREREG.md:156`). That branch is unreachable while the script implements the formula. The parent rows R0–R9 are a consistency check. Observed in-model.

The same holds for the review fold-in, whose formulas sit in `ADDENDUM_REVIEW_PREREG.md` at `6fb397b`. \(t(\gamma,T)\) depends on \(\gamma T\) because \(\varepsilon=(1-e^{-\gamma T})/2\), so \(t(2,1/2)=t(1/2,2)\) by definition. The printed-cell elasticity \(w\varepsilon/J_H\) at \(\gamma\tau=1\), \(w=2\) is the definition of an affine cost; an independent value is \(0.9012221936\). Squared Hamming on the refresh rate has short-time average \(u^2/12\), stationarity \(s=6/u^3\), loss share \(1/3\), and critical \(\Pi=6/(\gamma T)\). At \(\gamma T=0.01\) that is \(600\) exactly (`dephasing_refresh_review_checks.py:63-73`). Those bars are NOT A TEST. The general one-interval balance \(A/\tau+\beta\tau^p\) has loss share \(1/(p+1)\). Linear loss is \(p=1\), share \(1/2\). Quadratic loss is \(p=2\), share \(1/3\).

**H2. Accounting C, which reproduces 16, charges the opening preparation on one side.** Both policies start from a fresh state (`PREREG.md:59`). Accounting A charges that opening to both. Accounting B charges it to neither. Both give \(\Pi_c\to 4\). Accounting C charges \(A/\tau\) on the refresh side and charges the unrefreshed side nothing (`PREREG.md:120`).

In the linear loss \(\bar L\sim u/4\), the unrefreshed rate in units of \(\gamma A\) is \(s\Theta/4\) and the refreshed minimum is \(\sqrt s\). They tie at \(s=16/\Theta^2\), so \(\Pi=16\). An independent solution of \(\bar L(\Theta)=\bar L(u)+u\bar L'(u)\) gives \(16.00160009\) at \(u=10^{-4}\) and \(16.16089276\) at \(u=0.01\), which round to the printed \(16.001600\) and \(16.160893\).

At the short-period boundary of A, the opening heat \(A/T\) equals the loss term. Removing it from the hold side leaves that side half as large. The refresh cost scales as the square root of the stake and the hold cost scales linearly, so the tie moves from 4 to 16. The reading in which the opening is already paid, and the decision is whether to refresh again, is accounting B, whose limit is 4. Reproducing 16 is the identity of the one-sided charge. It is NOT A TEST of a second threshold. The memo already separates C from A and B (`MEMO.md:29`). That separation is the part that holds.

**H3. The square-root stake scaling is a consistency check of the slow-drift case already labeled KNOWN.** It is not a new exponent, and it is not the general throughput exponent.

The short-period refresh cost is one fixed heat \(A\) per reset plus a loss linear in the inter-refresh interval, \(\bar L\sim\gamma\tau/4\):

\[
J=\frac{A}{\tau}+w\frac{\gamma\tau}{4},\qquad
\tau^*\sim 2\sqrt{\frac{A}{w\gamma}},\qquad
J^*\sim\sqrt{A\,w\,\gamma}.
\]

That is the one-interval form of the square-root/EOQ balance. In this repository the information rate on a drifting world scales as \(Q^{\min(1/2,1/\beta)}\), and for spectrum exponent \(\beta\le 2\) the slow modes follow the square-root/EOQ case (`theory/INTERNAL_MODEL.md:45`). The slow-mode rate \(\sqrt{q/\theta}/(2\ln 2)\) is that same case, labeled KNOWN (`theory/INTERNAL_MODEL.md:180`). The same stake exponent \(w^{1/2}\), with loss share \(1/2\), is what `theory/CLOCK_TERM_2026-11-23.md:55` records for continuous diffusive tracking and points to `CORE.md:91`. The deterministic-drift branch, loss proportional to \(1/f^2\), has \(w^{1/3}\) and loss share \(1/3\) (`theory/CLOCK_TERM_2026-11-23.md:40-47`, `:55`).

Class of this model: one reset, loss linear in the gap, no clock rate. That is the slow-drift square-root/EOQ case, the same exponent as continuous diffusive tracking. It is not class CK. It is not the deterministic-drift branch. The general statement in `INTERNAL_MODEL.md:45` is \(\min(1/2,1/\beta)\); the exponent \(1/2\) is only the slow-drift branch. A quadratic gap, the squared-Hamming balance or the short-time Gaussian monomial, sits on the \(1/3\) branch already stated at `CLOCK_TERM:55`. Consistency check, in both powers.

Crossref, queried for this review on 24 November 2026, HTTP 200:

- Harris, reprinted as Operations Research 38:947 (1990), `10.1287/opre.38.6.947`. The abstract says setup cost and capital tied up in stock determine the lot. No formula is quoted from it.
- Erlenkotter, Operations Research 38:937 (1990), `10.1287/opre.38.6.937`. The abstract says Harris presented the economic-order-quantity model in 1913. No formula is quoted from it.
- Arrow, Harris, and Marschak, Econometrica 19:250 (1951), `10.2307/1906813`, title "Optimal Inventory Policy". No abstract was returned, so no formula is taken from it. The replenishment interval of the deterministic lot is the same Harris balance.
- Saleh, Serrano, and Patel, IEEE Trans. Reliability 39:114 (1990), `10.1109/24.52622`, title on scrubbing recovery. No abstract was returned.
- Schroeder, Pinheiro, and Weber, "DRAM errors in the wild" (2009), `10.1145/1555349.1555372`. No abstract was returned.

No DOI for the 1934 Wilson essay was used. The verified lot-size record is Harris, identified as the economic-order-quantity model by Erlenkotter. Saleh and Schroeder identify a scrubbing literature and a DRAM-error literature by title. Their abstracts were absent, so this review does not attribute a square-root scrub interval to either paper. The exponent's classical home is the economic-order-quantity balance.

End-of-interval loss \(\sim\gamma\tau/2\) gives \(J^*\sim\sqrt{2A w\gamma}\). The time average \(\sim\gamma\tau/4\) gives \(J^*\sim\sqrt{A w\gamma}\). Both are the same square root. The prefactor is the part that follows the choice of average. The fold-in states that split (`MEMO.md:61`). Independent algebra agrees. At \(u=0.01\) the exact period is longer than \(2\sqrt{A/(w\gamma)}\) by the factor \(1.00333750\), and the exact rate is shorter than \(\sqrt{A w\gamma}\) by the factor \(0.99833749\). Those are the printed ratios. They are the remainder of the expansion, a consistency check.

Shannon's fidelity-criterion paper, Crossref HTTP 200, `10.1109/9780470544242.ch21` (collected volume, 2009; no abstract, so no sentence is quoted) remains the record behind the binary rate-distortion endpoint \(R(D)=\ln 2-h(D)\). The T84 sign is that comparison. The fold-in already says so. NOT A TEST.

**H4. The clock-floor bars cannot miss, and the alternatives cannot pass.** `theory/CLOCK_TERM_2026-11-23.md:125` states that a clock first pays when the best clockless look carries more than \(4\kappa/\lambda\) nats. Line 126 says this is the fixed-price Poisson onset \(c^*=4\kappa kT\) on the \(a=1\), \(b=2\) branch. The addendum sets the stock floor to \(F=\kappa\ln 2\), computed from \(\chi(1)=\ln 2-h(1)\) (`ADDENDUM_PREREG.md:21-39`).

At \(\kappa=\lambda=kT=1\), \(F=\ln 2=0.693147180559945\) and the onset is 4. The gap is \(4-\ln 2=3.306852819440055\), which prints as \(3.306853\). Bar B1 forces \(F\) onto \(\ln 2\) within \(10^{-12}\). Bar B2 is \(|F-4|\ge 3\), and the margin under that identity is \(0.30685281944\). Bar B3 is \(|\ln 2-0|\ge 0.5\). Once B1 holds, B2 and B3 are facts about \(\ln 2\). The alt-onset form is defined as 4, so \(|4-4|\ge 3\) is false. The alt-frozen form is defined as 0, and the clock at rest is defined as 0, so \(|0-0|\ge 0.5\) is false (`dephasing_refresh_addendum_checks.py:46-64`). The script branch that would mark the bars as failing to separate the forms is unreachable. The memo's sentence that this headline is not a consistency check (`MEMO.md:51`) does not hold. The comparison is NOT A TEST.

\(F=\kappa\ln 2\) is a stock cost. The onset at lines 125–126 is an information threshold for paying for a clock. Setting \(\kappa=\lambda=kT=1\) makes both pure numbers so they can be subtracted. This review scores that subtraction, which is the addendum present at this head. It does not score whether \(\Pi_c\to 4\) equals \(c^*=4\kappa kT\).

### Medium

**M1. The named Gaussian probe is not the function the script evaluates.** R6 scores the monomial \(w\gamma^2\tau^2/6\). An independent Simpson quadrature of the Hamming loss under coherence \(e^{-(\gamma t)^2}\), minimized over the period, gives elasticity \(0.354802\) at stake parameter \(s=20\) (signed \(+0.021469\) from \(1/3\)) and \(0.333633\) at \(s=10^4\) (signed \(+0.000299\) from \(1/3\)). The short-time limit is \(1/3\). The finite envelope is closer to \(1/3\) than to \(1/2\), and it is not the quantity inside the locked tolerance \(10^{-12}\). Location: measurement/code. The lock's own bar remains the monomial identity.

**M2. Several fold-in clauses are constants compared with constants.** `dephasing_refresh_review_checks.py:93` checks the literal `0.376662 < 0.4` and does not compute that threshold. The fair-coin clause \(|4\ln 2-2\ln 2|>1\) is \(|2\ln 2|>1\). The carrier at \(\gamma\tau=0\) is assigned `0.0` and then compared with \(\ln 2\). Those clauses cannot miss. The five magnitudes that are computed match an independent evaluation at \(\gamma\tau=1\): carrier \(0.93992434\), leak threshold \(0.19308539\), squared one-shot \(0.26907132\), rent gap \(1.23947163\), coherence threshold \(3.43656366\). They are the alternatives already computed in the T84 review. They show that those one-shot signs belong to the chosen cost. They are not a test inside the locked refresh cost.

**M3. Classical assumptions that fix the exponent.** After the eigenbasis read, pure dephasing supplies the crossover \((1-e^{-\gamma t})/2\) of a classical bit, and the cost is Hamming on that bit. The heat \(A\) does not depend on the age or on the entropy erased; that fixed setup heat is the economic-order-quantity assumption, and a heat that grew with the mixedness of the state would be a different balance. The use time is uniform on the interval; scoring at the end of the interval changes the prefactor by \(\sqrt 2\) and leaves the exponent. The first preparation costs the same \(A\) as each later refresh; a different opening heat would split accounting A from accounting B. The ruin cap is slack, the period is continuous, and the model is one bit. Short-time Markovian loss is linear in age. A coherence even in \(t\) is the quadratic case, whose share is the known \(1/3\).

### Low

**L1. Locks, order, wording, and the untouched core files.** The three sha256 values match the blobs, and the blobs at `067c485` are the same:

| Lock | Commit | sha256 | Scoring script |
|---|---|---|---|
| Parent rate | `612b82e` at `2026-11-24T21:11:32Z` | `b2e96d76234da1e4a2521b990bb9cf456ca1c9c60a334ebf475f49b159dcab8f` | absent until `9c1b0f3` |
| Clock addendum | `9619565` at `2026-11-24T21:19:52Z` | `62871c9de3ad1d29046d2f73162139b5f0ae4d897a3204ca05859f3a9c5e63b2` | absent until `9c1b0f3` |
| Review fold-in | `6fb397b` at `2026-11-24T21:27:21Z` | `fc82c94bcf0ff3e639d6512475d8060228164b27c0a8f973dc4adc0b1f371dfd` | absent until `9c1b0f3` |

Author date equals committer date on each lock and on `9c1b0f3` (`2026-11-24T21:28:20Z`), which is the commit that adds all three scripts and their stored stdout. No later commit edits the three files. `THEORY.md` and `CORE.md` are absent from `612b82e^..067c485`. Git does not show whether an uncommitted draft of a script existed before the lock. The closed forms inside the locks already fix the bars, so an earlier draft would not have made an independent test.

The new ledger avoids the disallowed outcome words. The three locks still contain the older outcome sentence the upstream process retired, and the headline token for a miss. The process rule on upstream `652d936` leaves locked preregistrations unrewritten. That is not a breach. The diff against `29ffc8b` has no email address and no phone number. `theory/dephasing-crossover-2026-11-24/PREREG.md` contains neither `w^{1/2}` nor `T_hold`.

## Ledger

**Lock reference:** `067c485dd86517f7ffaad01486cbd696f690842b` on `forge-dephasing-refresh`, reviewing locks `612b82e`, `9619565`, `6fb397b`
**Logged at (ET):** 2026-11-24 16:45 ET
**Breach check:** `none` (the three locks are the blobs named above; this review does not patch them)

Rules: `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` on upstream `652d936`. Signed size is independent value minus the printed value.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| HASH | three sha256 values, each file unedited, each lock before `9c1b0f3` | all three match; scripts born in `9c1b0f3` | HIT, residual 0 | process | low | none yet | none |
| PI4 | \(\Pi_c(0.01)=4.02674456\), series gap \(1.186\times 10^{-7}\), limit 4 | \(4.02674456303\), gap \(1.185863\times 10^{-7}\) | NOT A TEST; residuals \(+3.0\times 10^{-9}\) and \(-1.4\times 10^{-11}\) | model | low | none yet | none |
| ACCT-C | 16.001600 at \(10^{-4}\); 16.160893 at 0.01 | 16.00160009; 16.16089276 | NOT A TEST; residuals \(+8.9\times 10^{-8}\) and \(-2.4\times 10^{-7}\). One-sided opening charge | model | medium | none yet | none |
| EOQ | \(\tau^*\) ratio 1.003338; \(J^*\) ratio 0.998337; exponent \(1/2\) | 1.00333750; 0.99833749 | NOT A TEST; residuals \(-5.0\times 10^{-7}\) and \(+4.9\times 10^{-7}\). Consistency check of the KNOWN slow-drift case | model | medium | none yet | none |
| SQ | share \(1/3\); critical \(\Pi=600\) at \(\gamma T=0.01\) | share \(1/3\) exactly; \(\Pi=6/0.01=600\) | NOT A TEST; residuals 0 and 0 | model | low | none yet | none |
| CLOCK | \(F=\ln 2\); gap to 4 nats is 3.306853; bars separate the forms | gap \(3.30685281944\) | NOT A TEST; residual \(-1.8\times 10^{-7}\). B2 margin \(+0.30685\) under an identity; alternatives cannot pass | model | high | none yet | none |
| ELAS | elasticity 0.901222 at \(\gamma\tau=1\), \(w=2\) | 0.9012221936 | NOT A TEST; residual \(+1.9\times 10^{-7}\) | model | low | none yet | none |
| GAUSS | short-time monomial share \(1/3\) stands in for the Gaussian envelope | envelope elasticity 0.354802 at \(s=20\) | signed \(+0.021469\) from \(1/3\); the script does not evaluate the envelope | measurement/code | medium | none yet | none |

### Scaled notes (medium and high)

1. **CLOCK.** The locked bars are \(|F-\ln 2|\le 10^{-12}\), \(|F-4|\ge 3\), and \(|F|\ge 0.5\), with \(F\) defined as \(\ln 2\). The outcome sits on \(\ln 2\) because that is the definition. The two alternatives are the constants 4 and 0, and the bars measure distance from those same constants. Location is the model. No formula was changed. The update that would make a separation test is a later lock with a bar that can miss. This review does not score that lock.
2. **ACCT-C and EOQ.** The candidate 16 is the one-sided opening charge. The symmetric charges give 4. The exponent \(1/2\) is the slow-drift square-root/EOQ case at `theory/INTERNAL_MODEL.md:45` and `:180`, the same exponent as `theory/CLOCK_TERM_2026-11-23.md:55` and `CORE.md:91`. Location is the model. No update to a formula is warranted. The label is a consistency check.
3. **GAUSS.** The locked tolerance is on the monomial. The envelope the prose names differs from \(1/3\) by \(+0.021469\) at \(s=20\). That is a measurement/code gap between the name and the script, inside the short-time reading the lock actually scores. No update yet.

## What was rerun

Head `067c485dd86517f7ffaad01486cbd696f690842b`. The recomputation does not import the scored scripts. It is `theory/reviews/dephasing_refresh_review_checks/recompute.py` on `forge-refresh-review`.

| Check | Result |
|---|---|
| Parent blob at `612b82e` and at `067c485` | `b2e96d76234da1e4a2521b990bb9cf456ca1c9c60a334ebf475f49b159dcab8f`, unedited |
| Clock-addendum blob at `9619565` and at `067c485` | `62871c9de3ad1d29046d2f73162139b5f0ae4d897a3204ca05859f3a9c5e63b2`, unedited |
| Review-fold blob at `6fb397b` and at `067c485` | `fc82c94bcf0ff3e639d6512475d8060228164b27c0a8f973dc4adc0b1f371dfd`, unedited |
| Script and stored stdout present in a lock | absent from `612b82e`, `9619565`, and `6fb397b`; born together in `9c1b0f3` |
| Rerun of the three scoring scripts | stdout matches the stored `.out` files; fail count 0 |
| `python3 tools/check_consistency.py` | `RESULT: PASS`. Wording FAILs 0. 29 INFO hits on frozen records |
| `python3 tools/check_fresh.py` | `RESULT: PASS`. `origin/main` is `d2aeb81`; `31aa997` is inside the window |
| `python3 tools/check_open_work.py` | `RESULT: PASS` |
| `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` | 294 passed, 1 skipped, 375.21s, exit 0 |

`numba` is not installed. `reviews/night2/CAUSAL_NULL_INVARIANCE/core.py` imports it, so that path is ignored. Pytest itself was absent at the start of this review and was installed in the user site (pytest 9.2.0, NumPy 2.5.5, SciPy 1.18.1). The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed).

## What holds

The printed digits match a 50-place recomputation to the last printed place: \(\Pi_c(0.01)=4.02674456\), the series gap \(1.186\times 10^{-7}\), accounting C at \(16.001600\) and \(16.160893\), the short-period ratios \(1.003338\) and \(0.998337\), elasticities \(0.50083\), \(0.54149\), and \(0.58198\), \(\ln 2=0.693147180560\), the gap \(3.306853\), \(t(0.01)=6.300822\), \(t(1)=1.973877\), \(\Pi_c(1)=7.568845\), and the printed-cell elasticity \(0.901222\). The derivative of \(\Pi_c\) has the sign of \(2-(2+2\Theta+\Theta^2)e^{-\Theta}\), which is positive for \(\Theta>0\) because that function is 0 at 0 and its derivative is \(\Theta^2 e^{-\Theta}\). The channel and the dephasing map are inputs. The hash, the commit order, and the three locks preceding the scripts all hold.

## Attacks tried

1. Hash and order. Each stated sha256 matches the lock blob and the blob at `067c485`. The three scoring scripts and their stored stdout are absent from the locks and appear together in `9c1b0f3`. Author dates equal committer dates. `THEORY.md` and `CORE.md` are untouched.
2. Identity attack, as in the T84 review. Expanded \(\Pi_c\), the series, the shared boundary of A and B, the elasticity identity, R6 for every \(s\), R7 as twice R2, and R8 as adding a positive constant. Those bars are NOT A TEST.
3. Accounting C. Recomputed the one-sided boundary. The limit 16 is that one-sided opening charge. The symmetric charges give 4.
4. Square-root class. Placed the one-interval linear-gap balance in the slow-drift square-root/EOQ case (`INTERNAL_MODEL.md:45`, `:180`, KNOWN), the same exponent as continuous diffusive tracking (`CLOCK_TERM:55`, `CORE.md:91`), and off the deterministic-drift \(w^{1/3}\) branch (`CLOCK_TERM:40-47`, `:55`). Labeled a consistency check. Crossref on Harris, Erlenkotter, Arrow–Harris–Marschak, Saleh, Schroeder, and Shannon. No Wilson DOI was used. No scrubbing abstract stated a square-root interval, so none is attributed.
5. Clock bars. Evaluated \(4-\ln 2\) and the three bars. The stock floor cannot miss and the two alternatives cannot pass. Did not score a comparison of \(\Pi_c\to 4\) with \(c^*=4\kappa kT\).
6. Gaussian envelope, integrated independently. The script's monomial is exactly \(1/3\). The envelope at \(s=20\) is \(0.354802\).
7. Fold-in digits and the constant clauses, including the pasted `0.376662 < 0.4`.
8. Wording, personal data, and the hypothesis sentence against `CORE.md:7`.
9. Consistency, freshness, open-work, and the full pytest with the numba path ignored.

The blocker is that no bar scored at this head can miss while the closed forms in the three locks stand. The run stays a consistency check.

Blockers remaining: 1
