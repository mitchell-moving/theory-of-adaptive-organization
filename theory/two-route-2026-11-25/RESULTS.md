# Results ledger: two-route prereg

**Lock reference:** `theory/two-route-2026-11-25/PREREG.md`, sha256 `9e42fe0a581a271f5c09a6dd7064304f8aaab43dd21ed7d509feaad13cd29e54`, lock commit `b159d0f`  
**Logged at (ET):** 2026-11-25 09:05 ET  
**Breach check:** `none` (the prereg hashes to its lock value; no prediction was edited; no data was used)

Rows are added as bars are scored. Bars not listed (A-C3, A-T1, A-T3, all of Route B) are not scored yet.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| A-C1 (CONSISTENCY_CHECK) | At \(g=0\) the world-bath heat is 0 at every memory design (T61 passive plant) | max \(|\dot Q_X|=0\) over 9 designs | HIT, information about 0 (identity) | model | low | none | none |
| A-C2 (CONSISTENCY_CHECK) | Stability determinant of W2 is \(a\gamma(1-gc)\) (F3 input) | \(\det A=a\gamma(1-gc)\) by inspection of the drift matrix in `checks/route_a_w2.py` | HIT, information about 0 (identity) | model | low | none | none |
| A-T2 | \(\rho=\dot Q_M^*(0.5)/\dot Q_M^*(0)\le0.9\); RI predicts \(\rho=1\); odds of a miss 0.5 | \(\rho=1.0453\) (\(\dot Q_M^*=2.2042\) at \(g=0.5\), \(2.1086\) at \(g=0\)); tolerance check 1.0453 | **miss, \(+0.145\)** (memory heat rises with the world's copy gain instead of falling). RI's value 1 is also off, by \(+0.045\), smaller than the locked bar's error | model (no MV gate or bug fired; JP-heat \(\dot Q_M\ge kT_M l_M\) held at 2,000 random designs; A-C1 held) | medium | none yet (open miss, `CORE.md:169`) | none |

## A-T2, scaled write-up (medium)

1. **Prediction and risk.** Locked: a world that copies the memory (gain \(g=0.5\)) lowers the optimal memory heat by at least 10% at \(w=10\). RI, which treats the world as exogenous, predicts no change. Odds of a miss were set at 0.5.
2. **Miss and location.** \(\rho-0.9=+0.145\), location `model`. The cost does fall with \(g\) (\(J^*=6.281\) at \(g=0\), \(6.052\) at \(0.5\), \(5.851\) at \(0.9\)), but not through the memory bath: the world-bath heat turns negative (\(\dot Q_X^*=-0.278\) at \(g=0.5\)), the memory relaxes more slowly and copies more (\(\gamma^*\) 6.88 to 5.24, \(c^*\) 0.59 to 0.76), and the memory heat rises by 4.5%. The learning rate barely moves (1.453 to 1.448). Total heat stays positive (1.926 at \(g=0.5\)), as the second law requires at equal temperatures. All numbers: `checks/route_a_w2.out`.
3. **Update.** None yet. Diagnosis: in W2 the responding world's gain shows up as a shift of heat between the two baths, not as a free ride on the memory's heat, and RI's exogenous reading is closer than the locked bar (+0.045 against +0.145). Next test: A-T1 asks whether the two-bath account and the design-level chain are one object; the sign of \(\dot Q_X^*\) is the cross term the two-one-way null sets to 0, and it is not 0 here (reported, not a scored bar). Per the prereg's G5, the free-ride line stops here.

## Notes appended after the gate read (2026-11-25 09:29 ET; the lines above are unchanged)

- **A-T2 status:** run without a gate check (see `DEVIATIONS.md`, process miss `FORGE-GATE-1`). The miss against the locked bar stands: \(+0.145\), location model.
- **RI correction:** RI's held design gives \(\rho_{\mathrm{RI}}=0.8774\), inside the hit band, not 1. The sentence above saying RI's value 1 "is also off, by +0.045" is withdrawn. A-T2 did not discriminate against RI. Calculation in `DEVIATIONS.md`.
- **Stamp:** the header's "09:05 ET" should read 08:53 ET (commit `9967b5d`, 08:53:38 ET).
- **Wording:** "second law" in the write-up is the physics name (`process/PROCESS.md:39` allows physics names). It is kept.
- **v2:** A-T1, A-T3, B-T1 and B-T2 are superseded by `PREREG_2.md`. No v2 bar has been run.
- **v3:** The v2 gate read found 1 blocker on A-T1′ (`gc = 0.95` margin). A-T1′ (only) and the §6/Gate wording items are superseded by `PREREG_3.md` (lock `78ff15a`), which awaits a fresh gate read. No v2 or v3 bar has been run.
- **v4:** The v3 gate read found 1 blocker on A-T1″ (`J_m` lacked the confinement term, letting memory best replies reach `gc = 0.999`). A-T1″ (only) is superseded by `PREREG_4.md` (lock `b9a2710`, shared `w_x E[x^2]` modeling choice with `w_x in {0.5, 1, 2}` robustness rule), which awaits a fresh gate read. No v2, v3, or v4 bar has been run.

## Results under `PREREG_4.md` + `PREREG_4a.md` (appended 2026-11-25 11:33 ET; the lines above are unchanged)

**Lock references:** `PREREG_4.md` sha256 `b16b3c2b814122f0e180045cbbffb634b761fafb907225a3d2b7803e0f14914c`, commit `b9a2710`; `PREREG_4a.md` sha256 `c9fb4fb9610d1128e39d64f291f32fc9d51009917459c823c41dc9874d24c937`, commit `6580fb0`. Gate: v4 independent gate read, GATE PASS (0 blocking). Scripts and outputs: `checks/route_a_t1ppp.py` / `.out`, `checks/route_b_t2p.py` / `.out`. Every number below is OBSERVED in-model (toy W2 world and random 3×3 landscapes). Nothing is a field result. The hypothesis sentence is untouched.
**Breach check:** `none` (all four prereg files hash to their locks; no prediction was edited; no data was used).

| prediction_id | locked_prediction (value/band; odds) | outcome (OBSERVED) | miss (signed size & direction, or HIT + info) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| A-T1‴ | HYPOTHESIS \(G\ge0.10\) at all three \(w_x\in\{0.5,1,2\}\); weak rival \(G=0\); hit odds 0.20, boundary-hit odds 0.01 | \(w_x=0.5\): Nash on the box edge \(\ln\gamma=5\) (\(\gamma=148.41,\ c=0.0205,\ g=1.4497\)); undamped 200 rounds did not stop, damped stopped at round 24; \(G=0.488\) at the edge, not scored. \(w_x=1\): same edge (\(g=1.3763\)), damped round 32, \(G=0.356\) at the edge, not scored. \(w_x=2\): interior, undamped round 19 (\(\gamma=6.500,\ c=0.5448,\ g=0.7682,\ gc=0.419\)), \(G=0.0654\). Joint minima interior at all three (\(J^*=14.0087,\ 16.1186,\ 19.2769\)). Half-tolerance reruns: identical \(G\) | **open miss, `boundary-hit`**, size undefined. The interior point alone (\(w_x=2\)) would be below the bar by \(-0.035\) | model: off the box, \(J_m\) keeps falling as \(\gamma\to\infty,\ c\to0\) (\(10.5035\) at \(\ln\gamma=5\), \(10.50004\) at \(\ln\gamma=9\), limit \(10+w_x\) at \(w_x=0.5\)). At world gain about 1.4 the memory's best reply is to stop copying (\(m\to0\)), a limit the box cannot reach. The paper bracket \(g\in[0.5,1.1]\) did not cover this path (gate read v4 NB5) | medium | none yet (open miss, `CORE.md:169`) | none |
| B-T2′ | HYPOTHESIS \(f\in[0.10,0.35]\); rivals \(f=0.5\) (random basin) and weak \(f=0\); odds of a miss 0.45 | 12,093 of 20,000 draws qualify (0 SP ties); 2,844 select the worse Nash point: \(f=0.2352\), SE 0.0039. Edmonds equals brute force on the first 200 qualifying draws (max diff \(4\times10^{-16}\)). SP minimizer is a local minimum in every draw. CPU 104 s | **HIT**, inside the band (0.135 above the lower edge, 0.115 below the upper). \(\lvert f-0.5\rvert=0.265>4\,\mathrm{SE}=0.015\): resolved | — | medium | F6 gets a size on this landscape family: with strengths \(c=(1,3)\), about 24% of two-basin draws settle in the worse basin | none |
| B-C3 (CONSISTENCY_CHECK, code gate) | At \(c=(1,1)\), \(f=0\) on the same draws | \(f=0\) on all 12,093 qualifying draws (0 ties) | HIT, information about 0 (identity); gate passed, so B-T2′ is scored | measurement/code | low | none | none |
| A-C3, A-C4, A-C5, B-C1, B-C2, B-C4 (CONSISTENCY_CHECK) | Identities per `PREREG_4.md` Gate (A-C5 with its heat-formula caveat) | Not run, as locked ("Logged only") | information about 0 | — | low | none | none |

**§6 score (`PREREG_3.md` §2.2 as amended by `PREREG_4a.md`; provisional until the independent review round of `PREREG_2.md` §5).**

- Route A: scope rows BICAUSAL and CL11 changed after independent review: 0 (no review yet; no status change is claimed). A-T1‴ resolved: 0 (`boundary-hit` scores 0). **\(S_A=0\).**
- Route B: scope rows CX2 and F6 changed after independent review: 0 (no review yet; F6 stays proved-in-model, CX2 stays open). B-T2′ resolved: 1. **\(S_B=1\).**
- Route B moved the core claim further on this score. The scope-row points (up to 4 per route) wait on the review round.

**A-T1‴, short write-up (medium).** (1) Locked bet: a sized Nash gap \(G\ge0.10\) at all three \(w_x\), with boundary-hit odds put at 0.01. (2) Outcome: at \(w_x=0.5\) and \(1\) the alternating best replies end on the \(\ln\gamma=5\) box edge, so the bar is a `boundary-hit` open miss and is not scored. The paper's 0.01 was wrong: it rested on a memory-reply bracket that stopped at \(g=1.1\), and the Nash path went to \(g\approx1.4\). (3) Diagnosis, not an update: in W2 with this shared excursion cost, a world that copies strongly enough makes "stop copying" the memory's best reply, which no finite design attains. That is a property of the model, seen in the solver. Next test, not locked: a prereg whose memory design set includes that limit (for example \(c=0\), \(m\) fixed) as an attainable point, so a Nash point there can be scored.
