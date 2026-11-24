# Results addendum: T84 observed in-model, consistency check

*Tuesday 24 November 2026, 16:31 ET. Appended after the review of fork PR #22 (comment on head `29ffc8b656f39fde1000fa8b9082b206882c374c`; write-up `theory/reviews/DEPHASING_CROSSOVER_REVIEW_2026-11-24.md` on `forge-dephasing-review`, fork PR #24). Vocabulary follows `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at upstream `652d936` (PR #261). This file does not edit `PREREG.md`, the lock `389f3bc`, the scored script, or the stored stdout. `THEORY.md` and `CORE.md` are unchanged. No prediction, bar, grid, or sign was patched.*

> The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment. (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. The qubit, the qutrit, and the dephasing channel remain inputs.

## Label going forward

The stored run still reads `HEADLINE CLUE_SPLIT`, `FAILS 0`, and `ALL T84 CHECKS PASS` (`theory/dephasing_crossover_checks/dephasing_crossover_checks.out:13-15`). `MEMO.md:23` calls the encoding crossover **PROVED (in-model)**. That sentence stays. Commit `853e5a2` already replaced those words on the T84 row of `OPEN_WORK.md:125` and added the identity reading at `STATUS.md:26` and `theory/README.md:52`. `MEMO.md:23` is superseded by this addendum.

Going forward the P1, P2, and crossover arithmetic is **observed in-model, consistency check**, and **NOT A TEST**. It is not an independent test of the cost. The label **PROVED** is not used for this run from this addendum on. The same rows are the ledger in `DEVIATIONS.md`.

Inside the locked cost, for \(\kappa=1\),

\[
J_P-J_H=\ln 2-\chi(r)-w\varepsilon=h(\varepsilon)-w\varepsilon,
\]

with \(\varepsilon=(1-r)/2\) and \(\chi(r)=\ln 2-h((1+r)/2)\), because \(h((1+r)/2)=h(\varepsilon)\) (`PREREG.md:70-80`). P1 is that identity (`PREREG.md:100-104`). `j_h` and `j_p` are the closed forms (`theory/dephasing_crossover_checks/dephasing_crossover_checks.py:94-99`). A hit on an identity of the chosen cost carries information \(\sim 0\) (`process/PROCESS.md` item 5 at `652d936`).

## Ledger

**Lock reference:** `forge-dephasing-crossover` `389f3bcbf7b05bd9811a62fb420a98009685395a`, sha256 `c6826685567aadeeb11ff1617b727a9dce69d8287688068f81429a859913203d`.

**Logged at (ET):** 2026-11-24 16:31 ET.

**Breach check:** `none`. The lock blob is unedited, no prediction was patched after the run, and this entry adds no private data.

Sign convention for a rival row: the miss is the rival gap minus the locked gap, in nats. The P-versus-H gap is \(J_P-J_H\). The Z-versus-H gap is \(J_Z-J_H\). A negative gap means the first design is cheaper. Gaps below are at \(\kappa=1\), rounded to six decimals from float64.

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
| PROCESS-LABEL | The results memo called the crossover PROVED (in-model) at `MEMO.md:23`. Commit `853e5a2` moved `OPEN_WORK.md:125`, `STATUS.md:26`, and `theory/README.md:52` to observed in-model. | P1, P2, and the crossover are identities of the locked cost. | Process miss: the memo treated a ~0-information identity as a test. No numeric residual. | process | high | PROVED at `MEMO.md:23` superseded by this file and `DEVIATIONS.md`. That sentence kept. Lock unedited. | none |
| RIVAL-A | Not a locked prediction. Carrier entropy at \(\gamma\tau=1\), \(w=1\): \(J_H=h(\varepsilon)+w\varepsilon\), \(J_P=0\). Locked P1 at that cell says the phase hold is cheaper. | \(J_P-J_H\) locked \(+0.307804\); rival \(-0.939924\) (\(J_H=0.939924\)). At \(\gamma\tau=0\), rival \(J_H=0\) against locked \(\ln 2\). | At \(\gamma\tau=1\), \(w=1\), miss on \(J_P-J_H\) is \(-1.247728\) nats. At \(\gamma\tau=0\), miss on \(J_H\) is \(-0.693147\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-B | Not a locked prediction. Linear leak \(J_H=(1-e^{-\gamma\tau})+w\varepsilon\), \(J_P=\ln 2\), same cell \(w=1\). | Threshold 0.193085 against locked 1.973877. \(J_P-J_H\) locked \(+0.307804\); rival \(-0.255034\). | Miss on \(J_P-J_H\) is \(-0.562837\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-C | Not a locked prediction. Squared Hamming \(L=\varepsilon^2\), cell \(\gamma\tau=1\), \(w=2\), where locked P1 says the pointer is cheaper. | Threshold 6.245254. \(J_H=0.269071\). \(J_P-J_H\) locked \(-0.008256\); rival \(+0.424076\). Fair-coin floor \(4\ln 2=2.772589\), not \(2\ln 2\). | Miss on \(J_P-J_H\) is \(+0.432332\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-D | Not a locked prediction. Coefficient \((1+w)\) on \(I\), same cell \(w=2\). | \(J_P-J_H\) locked \(-0.008256\); rival \(+1.239472\). | Miss on \(J_P-J_H\) is \(+1.247728\) nats. | model | high | none yet (locked cost unedited) | none |
| RIVAL-P2 | Not a locked prediction. \(q=0\), rent \(1-r\) instead of \(\chi\), cell \(\gamma\tau=1\), \(w=0.5\). Locked P2 threshold 0.376662 says the pinch is not cheaper. | Rival threshold 3.436564. \(J_Z=0.250\), \(J_H=0.790\). \(J_Z-J_H\) locked \(+0.022687\); rival \(-0.540151\). | Miss on \(J_Z-J_H\) is \(-0.562837\) nats. | model | high | none yet (locked cost unedited) | none |

## Scaled write-up

Low rows stop at the ledger. The blocks below are the high rows.

### 1. Process label

**Prediction and risk.** The lock did not state odds that the closed forms would miss. The forms are part of the model (`PREREG.md:70-80`), so a hit on them excludes no named rival cost. Information of that hit is \(\sim 0\).

**Miss and location.** Location is `process`. The write-up at `MEMO.md:23` attached **PROVED (in-model)** to an identity. The stored headline token remains on `dephasing_crossover_checks.out:13` and is not an independent test. These five checks compare a formula with itself:

- **C1** (`dephasing_crossover_checks.py:221`) subtracts `j_p()` from `j_h(r, w)` and compares the sign with \(w/\kappa-h(\varepsilon)/\varepsilon\).
- **C3** (`:281-282`) calls `j_h(r, w)` with no \(q\), so the span in \(q\) is zero by the signature.
- **C5** (`:308-309`) writes \(\kappa\ln 2+w\varepsilon\) against \(\kappa\ln 2\).
- **C10** (`:403-406`) compares \(h((1+\lvert r\sin\theta\rvert)/2)-h((1+r)/2)\) with the same expression in `pd_theta` (`:177-179`).
- **C11** (`:433-455`) builds the headline from the booleans and compares that string with the same boolean expression.

P2 is the same kind of identity, scored at `:251-266`. The headline label that requires the one-time-write sign for every \(w>0\) as soon as \(\gamma\tau>0\) (`PREREG.md:165`) stays out of reach while the closed forms stand: the grid contains \(w=1<2\ln 2\), and \(h(\varepsilon)/\varepsilon\) stays above \(2\ln 2\) at finite \(\tau\).

**Update.** The label going forward is observed in-model, consistency check, NOT A TEST. The original sentences stay visible. The lock is not edited.

### 2. Rival costs

**Prediction and risk.** RIVAL-A through RIVAL-D and RIVAL-P2 were not locked. They are rival notes at the cells named in the review. Each changes which design is cheaper at that cell.

**Miss and location.** Location is `model`. The signed misses are the ledger column. A negative miss on \(J_P-J_H\) moves the cell toward the pointer relative to the locked cost (RIVAL-A, RIVAL-B). A positive miss moves it toward the phase hold (RIVAL-C, RIVAL-D). The negative miss on \(J_Z-J_H\) moves the cell toward the pinch (RIVAL-P2). The headline rule requires P1 (`PREREG.md:164`), so a P1 sign change at the named cell would not leave the stored headline in place. These five rents were not scored by the locked script.

**Update.** None on the locked formulas. These notes do not replace \(J=\kappa I+q\kappa P_D+w L\). A comparison among cost forms was not locked in `389f3bc`, and none is adopted here.

### 3. Known comparison

\(w/\kappa>h(\varepsilon)/\varepsilon\) is the comparison of the endpoints of the binary Hamming rate-distortion function \(R(D)=\ln 2-h(D)\). With \(I_H=\ln 2-h(\varepsilon)\), \(L_H=\varepsilon\), \(I_P=\ln 2\), \(L_P=0\), and \(P_D=0\) on both eigenbasis records, the pointer is cheaper exactly when lossless storage at cost \(\kappa\ln 2\) beats a binary symmetric channel of crossover \(\varepsilon\) priced at \(\kappa(\ln 2-h(\varepsilon))+w\varepsilon\). Pure dephasing supplies only \(\varepsilon=(1-e^{-\gamma\tau})/2\). After the eigenbasis read the comparison is classical.

It is a different object from a quantum fault-tolerance threshold, which is a critical physical error rate. It is a different object from a scrubbing or refresh schedule, and from a dynamical-decoupling pulse schedule.

Crossref API, 24 November 2026, HTTP 200 on each DOI below. Titles, authors, and years are the fields returned. Where an abstract was returned, no sentence is quoted. The texts of Saleh, Serrano, and Patel and of Schroeder, Pinheiro, and Weber were not opened.

Rate-distortion endpoint. `10.1109/9780470544242.ch21`. Returned title: "Coding Theorems for a Discrete Source With a Fidelity CriterionInstitute of Radio Engineers, International Convention Record, vol. 7, 1959." Issued 2009. Container title "Claude E. Shannon". No author array and no abstract were returned.

Fault-tolerance thresholds. Knill, Laflamme, and Zurek, "Resilient Quantum Computation", *Science* 279:342-345 (1998), `10.1126/science.279.5349.342` (abstract returned). Aharonov and Ben-Or, "Fault-Tolerant Quantum Computation with Constant Error Rate", *SIAM Journal on Computing* 38:1207-1282 (2008), `10.1137/s0097539799359385` (abstract returned). Shor, "Scheme for reducing decoherence in quantum computer memory", *Physical Review A* 52:R2493-R2496 (1995), `10.1103/physreva.52.r2493`. Fowler, Mariantoni, Martinis, and Cleland, "Surface codes: Towards practical large-scale quantum computation", *Physical Review A* 86:032324 (2012), `10.1103/physreva.86.032324`. Terhal, "Quantum error correction for quantum memories", *Reviews of Modern Physics* 87:307-346 (2015), `10.1103/revmodphys.87.307`. Dennis, Kitaev, Landahl, and Preskill, "Topological quantum memory", *Journal of Mathematical Physics* 43:4452-4505 (2002), `10.1063/1.1499754` (abstract returned).

Scrubbing, refresh, and pulse schedules. Saleh, Serrano, and Patel, "Reliability of scrubbing recovery-techniques for memory systems", *IEEE Transactions on Reliability* 39:114-122 (1990), `10.1109/24.52622`. Schroeder, Pinheiro, and Weber, "DRAM errors in the wild" (2009), *Proceedings of the eleventh international joint conference on Measurement and modeling of computer systems*, 193-204, `10.1145/1555349.1555372`. Viola and Lloyd, "Dynamical suppression of decoherence in two-state quantum systems", *Physical Review A* 58:2733-2744 (1998), `10.1103/physreva.58.2733`.

### 4. State facts that stand

Q1, Q2, Q5, and the \(P_D=0\) half of Q3 are facts about the states and the projectors. They do not use the rent. The five rival costs leave them alone. They stand. The price half of Q3, P4, P5, and Q4 stay inside the consistency check, as the ledger says.

### 5. The \(2\ln 2\) floor, the stake exponent, and a flag for T84b

\(h\) is in nats and \(\varepsilon\) is a probability, so \(h(\varepsilon)/\varepsilon\) and \(2\ln 2\) are nats per unit Hamming error. \(2\ln 2=1.38629436111989\ldots\) prints as `1.386294361120`. The threshold depends on \(\gamma\) and the hold time \(T\) only through the product \(x=\gamma T\):

| \(\gamma T\) | \(w_\times/\kappa\) |
|---|---|
| \(0.01\) | \(6.300822\) |
| \(0.1\) | \(4.021138\) |
| \(1\) | \(1.973877\) |
| \(2\) | \(1.582026\) |
| \(5\) | \(1.395653\) |
| \(20\) | \(1.386294\) |
| \(\infty\) | \(2\ln 2\) |

\(\gamma=2\), \(T=1/2\) and \(\gamma=1/2\), \(T=2\) both give \(1.973877\). The floor \(2\ln 2\) does not move with \(\gamma\) or with \(T\) separately.

An elementary balance \((\kappa\ln 2)/T+w(\gamma T)/2\) has optimum cost \(\sqrt{2\kappa\ln 2\cdot w\cdot\gamma}\), proportional to \(w^{1/2}\). That balance is not what the locked script scores. On `389f3bc`, `git grep` for `exponent`, `scrub`, and `T_hold` in `theory/dephasing-crossover-2026-11-24/` and `theory/dephasing_crossover_checks/` is empty, and the preregistration does not lock a \(w^{1/2}\) prediction. None is credited. `CORE.md:91` and `theory/CLOCK_TERM_2026-11-23.md:55` already record a square-root cost for other questions. Those lines are not this note.

`theory/CLOCK_TERM_2026-11-23.md:125` says a clock first pays when the best clockless look carries more than \(4\kappa/\lambda\) nats. That threshold does not move with the stake. T84's long-hold floor is also a stake-independent nat threshold, \(2\ln 2\) nats per unit Hamming error. The two expressions differ, and the decisions differ: pay for a clock, or switch a static encoding. The kinship is flagged for a separate preregistration, T84b. It is not scored here. This note does not lock a claim that one floor is the other.

## What was not edited

`PREREG.md` at `389f3bc` is the same blob. Predictions P1 through P5 and Q1 through Q5 stay as locked. `dephasing_crossover_checks.py` and `dephasing_crossover_checks.out` stay as scored. `THEORY.md` and `CORE.md` are untouched. Breach check: none.
