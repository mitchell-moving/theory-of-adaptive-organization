# P1-S results, scored against the locked preregs, and a hostile self-review

*Thursday 26 November 2026, 22:56–23:20 EST. Local note; nothing committed, pushed, emailed or posted. Preregs: `PREREG_P1S_2026-11-26.md` (SHA-256 d31ab71d…, locked 22:56:05) and `PREREG_P1S2_2026-11-26.md` (924a2253…, locked 22:57:31). Model code `p1s_sim.py` (97e950e9…). Scores: `score.out`, `score2.out`. Post hoc: `posthoc_designed.py` → `.out`.*

**Labels:** results are **observed** (in-model simulation numbers). Interpretations are **hypothesis**. Nothing here derives quantum theory or any physics.

## 1. Scores (strict, as locked)

**P1-S (σ_f = 1.5, seeds 1–5): PRIMARY OPEN MISS.** Extinction in 17 of 25 runs: heredity-on 2/5, heredity-off 5/5, sieve-only 4/5, high price 5/5, fast drift 0/5. H-A 1/5 (dA_z 0.0051, 0.1024, 0.0182 in the surviving seeds); H-B 0/5; H-C 0/5 (only seed 3 comparable: ratio 1.71, the judge worse); H-D 0/5; H-E 1/5; H-F 0/5.

**P1-S2 (σ_f = 1.0, seeds 11–15): PRIMARY OPEN MISS.** No extinctions.

| prediction | threshold | observed (seeds 11–15) | score |
|---|---|---|---|
| H-A anticipation in the record | dA_z ≥ 0.05 | 0.0012, 0.0005, 0.0046, 0.0055, 0.0010 | FAIL 0/5 |
| H-B needs heredity | on − off ≥ 0.03 | 0.0012, 0.0004, 0.0045, 0.0054, 0.0010 | FAIL 0/5 |
| H-C judge beats sieve at equal prices | ruin ratio ≤ 0.7 | 0.546, 0.876, 0.810, 1.558, 1.068 | FAIL 1/5 |
| H-D heredity-off null loses | ratio ≥ 1.3 | 11.39, 10.36, 10.91, 8.62, 8.17 | **PASS 5/5** |
| H-E record heredity follows drift persistence | h(P) − h(U) ≥ 0.15 | −0.215, −0.047, −0.039, −0.123, −0.155 | FAIL 0/5 (wrong sign) |
| H-F zero-action limit | log k median ≤ −3 and abs(dA_z) < 0.05 | log k −2.96, −2.85, −3.01, −2.93, −3.11 | FAIL 2/5 (near the line) |

Other observed numbers (P1-S2): evolved reading at low price sat at log10 k ≈ −1.2 to −1.9; the ruin hazard was 0.0061–0.0076 with heredity on, 0.0616–0.0769 with heredity off, and 0.0049–0.0124 for the sieve-only arm.

## 2. What the numbers say (observed, in this model)
- Survival selection with heredity kept populations alive about 10× better than populations whose offspring got random designs (H-D). It **did not** build a memory that anticipates the force (dA_z ≤ 0.0055), and the reading population did **not** beat the no-reading population at the same prices.
- At high price, reading fell to about 1/1000 of its range (log k ≈ −3), so the high-price limit is close to the sieve, as the zero-action limit predicts, but 3 of 5 seeds sat just above the locked line.
- Record heredity did not follow drift persistence. It went the wrong way.

## 3. Post hoc diagnostic (not preregistered; changes no score)

`posthoc_designed.py` (one seed, T = 1500, no births). It puts in a **designed** judge (steady-state Kalman filter on x, p and f, with feedback that cancels the estimated force) next to a reflex controller (filter on x and p only) and no reading, in the same worlds.

| σ_f | design | best k | ruin hazard | net income (of 0.2) |
|---|---|---|---|---|
| 1.0 | sieve (no reading) | — | 0.00313 | 0.200 |
| 1.0 | reflex | 0.1 | 0.00216 | 0.185 |
| 1.0 | designed judge | 0.1 | **0.00095** | 0.184 |
| 1.5 | sieve | — | 0.08026 | 0.200 |
| 1.5 | reflex | 1.0 | 0.02307 | 0.145 |
| 1.5 | designed judge | 1.0 | **0.01374** | 0.153 |

Reading (hypothesis): when designed, anticipation does pay in **ruin**. The judge's hazard is 2–3× below the reflex's, and below the sieve's. **In fitness terms, at σ_f = 1.0 it probably does not pay.** The judge saves about 0.002 deaths per agent per unit time. Its reading and acting cost about 8% of income, which slows reproduction by roughly 0.13 × 0.08 ≈ 0.010 per agent per unit time (birth rate from P1-S2 births: about 118,000 over 3000 time units for 300 agents). So the cost is about 5× the benefit. GTAO's own switch-on condition (SCALE_ENDS SE7: "a per-nat cost below the marginal value of the first nat") was then **not met in fitness units** in the world where populations survived. At σ_f = 1.5, where judging would pay, shared-force excursions ended most runs.

## 4. Hostile self-review (fixes appended; locked files untouched)
1. **The test was miscalibrated (main finding).** The prereg never checked that a designed judge is fitness-positive in its own world. In P1-S2 it probably was not (§3), so H-A failing is close to what the theory itself predicts there. The miss is open, but it is weak evidence about judgment-first. **Fix:** a calibration gate before any lock. In the locked world, a designed judge must beat the sieve in fitness (net growth), by a stated margin, computed with designed controllers only and no evolution.
2. **Selection was weak.** Random culls at the population cap caused about 95% of deaths; ruin caused a few percent. Mostly, the run measured mutation and drift. **Fix:** lower turnover (income), or make ruin a larger share of mortality, stated before the run.
3. **Shared-force confound.** The arms do not share the force path (different random draws), and with one common force, between-arm hazards are dominated by that path. Pairing by seed did not pair the worlds. **Fix:** use common random numbers for f across arms.
4. **Record heredity was built wrong.** The memory z carries the parent's body state, but the offspring is born at the origin, so inheriting z hands it a stale, mismatched state. H-E's wrong sign is plausibly this artifact. **Fix:** split body memory from world memory, or give offspring the parent's body state.
5. **H-D passing says little.** Heredity versus random designs is a search with versus without accumulation, which is W13 territory: selection with heredity is an optimizer. It is not evidence for the heredity clause beyond that.
6. **dA_z is pooled across different genomes,** which can hide anticipation held in differently scaled memories. dA_u (from actions) was also ≤ 0.012, so the conclusion is unlikely to flip. A per-lineage fit would be fairer.
7. **The pilot was too short.** T = 100 could not show the extinctions that appeared at T ≈ 100–2300. **Fix:** run a full-length pilot for extinction only.
8. **Nothing quantum was tested.** The quantum content is coherent-state births and the imprecision–backaction product. At these noise levels a classical model with the same noises gives the same dynamics. This is a test at the decohered (Gaussian) level, which is where the P1 note put the sieve-to-judge boundary, and it is said plainly.
9. **Walls.** W12: the prices are imposed (accepted; not tested). W13: the capacity to judge (a linear memory wired from the record to the force) is given; what selection had to find was its use. W10: the drift premise held. The internal-model principle (Francis & Wonham 1976, Automatica 12, doi 10.1016/0005-1098(76)90006-6) says rejecting a persistent force needs an internal model of it, so the designed judge's advantage is known in kind.
10. **No third force size was tried,** as P1-S2 stated before its run.

## 5. Meaning for the judgment-first hypothesis (plain words; hypothesis)
- In this toy world, being able to read and remember did not, by itself, turn into foresight under survival selection. Judgment did not appear by itself here.
- The likely reason is the theory's own: foresight has to pay for itself in survival and offspring, and in the world where populations lasted it cost about five times what it saved. Where it would have paid, shared catastrophes wiped populations out first. So this run does **not** count against judgment-first. It does show that "judgment emerges from below" is a claim about **when** foresight pays, not a given.
- What held: heredity is what let populations persist (10×), and pricing reading pushed it toward zero, the sieve end. The sieve end and the heredity requirement behaved as the theory says. The anticipation step, the part that makes a judge, was not shown.

## 6. Recommendation (by the same rule)
P1-S3, with fixes 1–4 and 7, and a calibration gate (a designed judge must be fitness-positive by a stated margin) before the lock. About 2 h. My p (a result that can fail and is not known) rises from 0.40 to about 0.5, because the main failure mode is now visible. EIV ≈ 0.5·0.48 + 0.5·0.05 ≈ 0.27 bits over 2 h ≈ 0.13 bits/h, well above the hold price. It is the best next step on this line. Not run in this session.
