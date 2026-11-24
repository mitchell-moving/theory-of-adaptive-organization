# Deviations

`PREREG.md` is unchanged after commit `389f3bc` (sha256 `c6826685567aadeeb11ff1617b727a9dce69d8287688068f81429a859913203d`). No prediction, bar, grid, or sign was edited after the run. No deviation.

## Ledger after the independent review

**Lock reference:** `389f3bc` on `forge-dephasing-crossover`. The preregistration is unedited.  
**Logged at (ET):** 2026-11-24 16:32 ET  
**Breach check:** `none`

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| INDEX-LABEL | index states the scored sign as proved in-model | review comment `7144884461`: the sign is an identity, so the run is a consistency check, observed in-model | overclaim: the label was stronger than an identity; no numeric residual | process | medium | index sentences and an appended errata in `MEMO.md`; the lock is unchanged | none |

## Addendum, 24 November 2026, 16:31 ET

The paragraph above stands for the lock. No prediction was patched. The reading of the scored labels is logged here. Vocabulary follows `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at upstream `652d936` (PR #261). The scaled write-up, the Crossref fields, and the product table are in `RESULTS_ADDENDUM.md`. `THEORY.md` and `CORE.md` are unchanged.

> The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment. (`CORE.md:7`)

**Lock reference:** `389f3bcbf7b05bd9811a62fb420a98009685395a`, sha256 `c6826685567aadeeb11ff1617b727a9dce69d8287688068f81429a859913203d`.

**Logged at (ET):** 2026-11-24 16:31 ET.

**Breach check:** `none`. Lock unedited. No post-hoc prediction patch. No private data in this entry.

### Label

Struck, as of this addendum: **PROVED (in-model)** on the P1 crossover at `MEMO.md:23`. That sentence stays visible. Commit `853e5a2` already replaced those words on the T84 row of `OPEN_WORK.md:125` and added the identity reading at `STATUS.md:26` and `theory/README.md:52`. The label going forward, including for `MEMO.md:23`, is observed in-model, consistency check, and NOT A TEST.

Going forward the P1, P2, and crossover results are **observed in-model, consistency check**, and **NOT A TEST**. The stored stdout still prints `HEADLINE CLUE_SPLIT`, `FAILS 0`, and `ALL T84 CHECKS PASS` (`theory/dephasing_crossover_checks/dephasing_crossover_checks.out:13-15`). Those bytes stay. Inside the locked cost, \(J_P-J_H=h(\varepsilon)-w\varepsilon\) (`PREREG.md:70-80`, `:100-104`; `dephasing_crossover_checks.py:94-99`). A hit on that identity carries information \(\sim 0\).

### Self-comparisons

These five checks compare a formula with itself. C1 subtracts the closed forms (`dephasing_crossover_checks.py:221`). C3 calls `j_h(r, w)` with no \(q\) (`:281-282`). C5 writes \(\kappa\ln 2+w\varepsilon\) against \(\kappa\ln 2\) (`:308-309`). C10 compares \(h((1+\lvert r\sin\theta\rvert)/2)-h((1+r)/2)\) with the same expression (`:403-406`; `pd_theta` at `:177-179`). C11 builds the headline from the booleans and compares that string with the same boolean expression (`:433-455`). P2 is the same kind of identity, scored at `:251-266`.

### Rival notes

Not locked predictions. Location `model`. Miss = rival gap minus locked gap, in nats, at \(\kappa=1\). The P-versus-H gap is \(J_P-J_H\). The Z-versus-H gap is \(J_Z-J_H\). A negative gap means the first design is cheaper. Six-decimal rounding from float64.

- **RIVAL-A**, carrier entropy \(J_H=h(\varepsilon)+w\varepsilon\), \(J_P=0\), cell \(\gamma\tau=1\), \(w=1\). Locked gap \(+0.307804\) (phase hold cheaper). Rival gap \(-0.939924\). Miss \(-1.247728\) nats. At \(\gamma\tau=0\), rival \(J_H=0\) against locked \(\ln 2\); miss on \(J_H\) is \(-0.693147\) nats.
- **RIVAL-B**, linear leak \(J_H=(1-e^{-\gamma\tau})+w\varepsilon\), \(J_P=\ln 2\), same cell. Threshold 0.193085 against locked 1.973877. Rival gap \(-0.255034\). Miss \(-0.562837\) nats.
- **RIVAL-C**, squared Hamming \(L=\varepsilon^2\), cell \(\gamma\tau=1\), \(w=2\). Locked gap \(-0.008256\) (pointer cheaper). Rival gap \(+0.424076\) (\(J_H=0.269071\); threshold 6.245254). Miss \(+0.432332\) nats. Fair-coin floor \(4\ln 2=2.772589\), not \(2\ln 2\).
- **RIVAL-D**, coefficient \((1+w)\) on \(I\), same cell. Rival gap \(+1.239472\). Miss \(+1.247728\) nats.
- **RIVAL-P2**, \(q=0\), rent \(1-r\) instead of \(\chi\), cell \(\gamma\tau=1\), \(w=0.5\). Locked P2 threshold 0.376662 says the pinch is not cheaper. Rival threshold 3.436564, \(J_Z=0.250\), \(J_H=0.790\), gap \(-0.540151\) against locked \(+0.022687\). Miss \(-0.562837\) nats.

The headline rule requires P1 (`PREREG.md:164`), so a P1 sign change at the named cell would not leave the stored headline in place. No rival cost is adopted. The locked \(J\) stays. A comparison among cost forms was not locked in `389f3bc`.

### Known comparison

\(w/\kappa>h(\varepsilon)/\varepsilon\) is the endpoint comparison of \(R(D)=\ln 2-h(D)\) for a binary symmetric channel under Hamming loss. Dephasing supplies only \(\varepsilon=(1-e^{-\gamma\tau})/2\). After the eigenbasis read the comparison is classical. It is a different object from a fault-tolerance threshold and from a scrubbing or refresh schedule.

Crossref HTTP 200 on 24 November 2026, fields as returned, no abstract sentence quoted. Rate-distortion: `10.1109/9780470544242.ch21` (container "Claude E. Shannon", issued 2009; the returned title names the 1959 fidelity-criterion chapter; no author array). Fault-tolerance: Knill, Laflamme, and Zurek 1998, `10.1126/science.279.5349.342`; Aharonov and Ben-Or 2008, `10.1137/s0097539799359385`; Shor 1995, `10.1103/physreva.52.r2493`; Fowler, Mariantoni, Martinis, and Cleland 2012, `10.1103/physreva.86.032324`; Terhal 2015, `10.1103/revmodphys.87.307`; Dennis, Kitaev, Landahl, and Preskill 2002, `10.1063/1.1499754`. Scrubbing and schedules: Saleh, Serrano, and Patel 1990, `10.1109/24.52622`; Schroeder, Pinheiro, and Weber 2009, `10.1145/1555349.1555372`; Viola and Lloyd 1998, `10.1103/physreva.58.2733` (dynamical suppression). Bibliographic detail is in `RESULTS_ADDENDUM.md`.

### State facts that stand

Q1, Q2, Q5, and \(P_D=0\) on the respecting read stand. They do not use the rent, and the five rival costs leave them alone.

### Floor, exponent, and T84b

The floor \(2\ln 2\) depends on \(\gamma\) and the hold time \(T\) only through the product \(\gamma T\). It does not move with \(\gamma\) or with \(T\) separately. \(\gamma=2\), \(T=1/2\) and \(\gamma=1/2\), \(T=2\) both give 1.973877. Units are nats per unit Hamming error.

No \(w^{1/2}\) prediction was locked, so none is credited. On `389f3bc`, `git grep` for `exponent`, `scrub`, and `T_hold` in the T84 preregistration and check directory is empty. The elementary balance \((\kappa\ln 2)/T+w(\gamma T)/2\) is proportional to \(w^{1/2}\) and is not what the locked script scores. `CORE.md:91` and `theory/CLOCK_TERM_2026-11-23.md:55` are other notes, not this one.

`theory/CLOCK_TERM_2026-11-23.md:125` is a stake-independent onset at \(4\kappa/\lambda\) nats. T84's long-hold floor is \(2\ln 2\) nats per unit Hamming error. The expressions differ, and the decisions differ. Kinship is flagged for a separate preregistration, T84b. Not scored here.

### Ledger

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| P1 | For \(\varepsilon>0\), P is strictly cheaper than H iff \(w/\kappa>h(\varepsilon)/\varepsilon\). Tie at \(\gamma\tau=0\). Odds not locked. `PREREG.md:100-106` | Grid signs match the closed form (`dephasing_crossover_checks.out:2`, bad_cells=0). At \(\gamma\tau=1\) the threshold is 1.973877. | HIT; information ~0. Identity \(J_P-J_H=h(\varepsilon)-w\varepsilon\). NOT A TEST / consistency check. | model | low | none on the formula | none |
| P1-shape | \(t(\varepsilon)=h(\varepsilon)/\varepsilon\) strictly decreasing on the locked sample; \(t(10^{-4})>8\); \(t(1/2)=2\ln 2\) within \(10^{-12}\). Odds not locked. `PREREG.md:108-114` | Stored \(t(10^{-4})=10.210290\) and \(t(1/2)=1.386294361120\). The finite threshold depends on \(\gamma\) and \(T\) only through \(\gamma T\). | HIT; information ~0. Property of binary entropy. NOT A TEST / consistency check. | model | low | none on the formula | none |
| P2 | For \(q<1\), Z is strictly cheaper than H iff \(w/\kappa<2(1-q)\chi(r)/r\). For \(q\ge 1\), Z is not strictly cheaper. Odds not locked. `PREREG.md:116-122` | Grid signs match (`dephasing_crossover_checks.out:3`, bad_cells=0). At \(q=0\), \(\gamma\tau=1\) the threshold is 0.376662. | HIT; information ~0. Identity of \(J_Z-J_H\) inside the locked cost. NOT A TEST / consistency check. | model | low | none on the formula | none |
| P2-shape | \(\chi(r)/r\) strictly increasing on the locked sample, from below 0.03 at \(r=0.05\) to \(\ln 2\) at \(r=1\). Odds not locked. `PREREG.md:124` | Stored \(\chi(0.05)/0.05=0.025010\) and \(\chi(1)=0.693147180560\). | HIT; information ~0. NOT A TEST / consistency check. | model | low | none on the formula | none |
| P3 | \(J_H\) and \(J_P\) do not move with \(q\), by at least \(10^{-12}\). Odds not locked. `PREREG.md:126` | Both spans are 0 (`dephasing_crossover_checks.out:4`). | HIT; information ~0. `j_h` and `j_p` take no \(q\) (`dephasing_crossover_checks.py:94-99`; C3 at `:281-282`). NOT A TEST / consistency check. | model | low | none on the formula | none |
| P4 | \(J_H=\kappa\chi(e^{-\gamma\tau})+w(1-e^{-\gamma\tau})/2\), and \(\Delta=w\varepsilon-\kappa h(\varepsilon)\). Odds not locked. `PREREG.md:128-134` | Max absolute mismatch \(8.882\times 10^{-16}\) (`dephasing_crossover_checks.out:5`). At \(\gamma\tau=1\), \(w=2\), \(\Delta=0.008256\). | HIT; information ~0. Same algebra as P1. NOT A TEST / consistency check. | model | low | none on the formula | none |
| P5 | One-time write: \(J_H=\kappa\ln 2+w\varepsilon\), \(J_P=\kappa\ln 2\). For every \(w>0\) and \(\gamma\tau>0\), P is strictly cheaper; tie if \(w=0\) or \(\gamma\tau=0\). Odds not locked. `PREREG.md:136` | bad_cells=0 (`dephasing_crossover_checks.out:6`). | HIT; information ~0. C5 writes those two expressions against each other (`dephasing_crossover_checks.py:308-309`). NOT A TEST / consistency check. | model | low | none on the formula | none |
| Q1 | Respecting projectors fix \(\rho(c)\); \(P_D=0\) and \(J=0\) within \(10^{-12}\). Odds not locked. `PREREG.md:138` | Max absolute residual 0 (`dephasing_crossover_checks.out:7`). | HIT; state fact stands. Does not use the rent. | model | low | none | none |
| Q2 | At \(c=1/8\), \(P_D\) rises as \(\alpha\) falls, and the absolute gap from `0.065406` is at most \(5\times 10^{-7}\). \(P_D(c)\) at \(\alpha=0\) rises in \(c\). Odds not locked. `PREREG.md:140-146` | \(P_D=0.06540602\), gap \(+1.797\times 10^{-8}\) (`dephasing_crossover_checks.out:8`). | HIT; state fact stands. Gap is inside the locked band. Does not use the rent. | model | low | none | none |
| Q3 | On design H, \(P_D=0\) at every locked cell, and \(J_H=\kappa\ln 2\) at \(\gamma\tau=0\). Odds not locked. `PREREG.md:148` | \(P_D=0\) on the grid. \(J_H\) at \(\gamma\tau=0\) is 0.693147180560 (`dephasing_crossover_checks.out:9`). | \(P_D=0\) HIT, state fact stands. Price half HIT, information ~0, NOT A TEST / consistency check. | model | low | none on the formula | none |
| Q4 | \(S(\rho(\tau))+P_{D,Z}(\tau)=\ln 2\) within \(10^{-12}\). Odds not locked. `PREREG.md:150-156` | Max absolute error \(3.469\times 10^{-17}\) (`dephasing_crossover_checks.out:10`). | HIT; information ~0. Entropy identity of this qubit. NOT A TEST / consistency check. | model | low | none on the formula | none |
| Q5 | \(P_D(\theta)\) matches the closed form within \(10^{-12}\), is 0 at \(\theta=\pi/2\), and falls in \(\lvert\sin\theta\rvert\). Odds not locked. `PREREG.md:158` | form_err=0 (`dephasing_crossover_checks.out:11`). | HIT; state fact stands. C10 compares the closed form with itself (`dephasing_crossover_checks.py:403-406`), so that check is NOT A TEST / consistency check, information ~0. | model | low | none on the formula | none |
| HEADLINE | The locked table's first label when P1, Q1, Q2, Q3, Q4, and P5 hold. Odds not locked. `PREREG.md:160-168` | Stored lines `dephasing_crossover_checks.out:12-15` print that label, `FAILS 0`, and `ALL T84 CHECKS PASS`. | HIT; information ~0. C11 compares the boolean label with itself (`dephasing_crossover_checks.py:433-455`). NOT A TEST / consistency check. Stdout bytes stay. Reading going forward: observed in-model, consistency check. | model | low | reading superseded in PROCESS-LABEL | none |
| PROCESS-LABEL | The results memo called the crossover PROVED (in-model) at `MEMO.md:23`. Commit `853e5a2` moved `OPEN_WORK.md:125`, `STATUS.md:26`, and `theory/README.md:52` to observed in-model. | P1, P2, and the crossover are identities of the locked cost. | Process miss: the memo treated a ~0-information identity as a test. No numeric residual. | process | high | PROVED at `MEMO.md:23` superseded by this entry and `RESULTS_ADDENDUM.md`. That sentence kept. Lock unedited. | none |
| RIVAL-A | Not a locked prediction. Carrier entropy at \(\gamma\tau=1\), \(w=1\): \(J_H=h(\varepsilon)+w\varepsilon\), \(J_P=0\). Locked P1 at that cell says the phase hold is cheaper. | \(J_P-J_H\) locked \(+0.307804\); rival \(-0.939924\) (\(J_H=0.939924\)). At \(\gamma\tau=0\), rival \(J_H=0\) against locked \(\ln 2\). | At \(\gamma\tau=1\), \(w=1\), miss on \(J_P-J_H\) is \(-1.247728\) nats. At \(\gamma\tau=0\), miss on \(J_H\) is \(-0.693147\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-B | Not a locked prediction. Linear leak \(J_H=(1-e^{-\gamma\tau})+w\varepsilon\), \(J_P=\ln 2\), same cell \(w=1\). | Threshold 0.193085 against locked 1.973877. \(J_P-J_H\) locked \(+0.307804\); rival \(-0.255034\). | Miss on \(J_P-J_H\) is \(-0.562837\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-C | Not a locked prediction. Squared Hamming \(L=\varepsilon^2\), cell \(\gamma\tau=1\), \(w=2\), where locked P1 says the pointer is cheaper. | Threshold 6.245254. \(J_H=0.269071\). \(J_P-J_H\) locked \(-0.008256\); rival \(+0.424076\). Fair-coin floor \(4\ln 2=2.772589\), not \(2\ln 2\). | Miss on \(J_P-J_H\) is \(+0.432332\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-D | Not a locked prediction. Coefficient \((1+w)\) on \(I\), same cell \(w=2\). | \(J_P-J_H\) locked \(-0.008256\); rival \(+1.239472\). | Miss on \(J_P-J_H\) is \(+1.247728\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-P2 | Not a locked prediction. \(q=0\), rent \(1-r\) instead of \(\chi\), cell \(\gamma\tau=1\), \(w=0.5\). Locked P2 threshold 0.376662 says the pinch is not cheaper. | Rival threshold 3.436564. \(J_Z=0.250\), \(J_H=0.790\). \(J_Z-J_H\) locked \(+0.022687\); rival \(-0.540151\). | Miss on \(J_Z-J_H\) is \(-0.562837\) nats. | model | high | none yet (locked cost unedited) | none |

High rows, one block each, per the template. Low rows stop at the table.

**PROCESS-LABEL.** The lock named no rival the closed forms could miss, so the hit's information is \(\sim 0\). The miss sits in `process`: `MEMO.md:23` called an identity PROVED (in-model). Update: this entry supersedes that label. The formulas do not change.

**RIVAL-A through RIVAL-P2.** Each named cell changes which design is cheaper. The signed sizes are the miss column. Update: none yet. The locked cost is not replaced, and no cost-form comparison was locked.
