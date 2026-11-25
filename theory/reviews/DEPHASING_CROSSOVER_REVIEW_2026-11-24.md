# Independent review: dephasing crossover (T84)

*Reviewer: independent. I did not write the preregistration, the memo, or the scored script. Tuesday 24 November 2026. Fork PR #22, head `29ffc8b656f39fde1000fa8b9082b206882c374c`, base `main` `d2aeb8100e22870dc5aee2529356de970c82a820`. Lock `389f3bcbf7b05bd9811a62fb420a98009685395a`. This review does not edit `THEORY.md` or `CORE.md`, and it does not edit the PR branch.*

**Result label: observed in-model.** This review does not clear it. The arithmetic of the chosen cost holds. The run is a consistency check of that cost. The crossover \(w/\kappa>h(\varepsilon)/\varepsilon\) is the binary rate-distortion comparison with \(\varepsilon\) taken from pure dephasing. Nearby costs flip the locked signs. No stake-exponent prediction was locked.

## Findings

### High

**H1. Inside the locked cost the headline cannot come out any other way, and nearby costs flip it.** The closed forms are part of the model (`PREREG.md:70-80`). For \(\kappa=1\),

\[
J_P-J_H=\ln 2-\chi(r)-w\varepsilon=h(\varepsilon)-w\varepsilon,
\]

with \(\varepsilon=(1-r)/2\) and \(\chi(r)=\ln 2-h((1+r)/2)\), because \(h((1+r)/2)=h(\varepsilon)\). P1 is that identity. The numerator of \((h(\varepsilon)/\varepsilon)'\) is \(\ln(1-\varepsilon)<0\) on \((0,1)\), so the threshold falls from \(+\infty\) to \(h(1/2)/(1/2)=2\ln 2\). A stake at or below \(2\ln 2\) stays on the phase-hold side of a strict inequality at every finite \(\tau\). P2, P4, P5, and the price half of Q3 are the same algebra. Q4 is \(S+\chi=\ln 2\) for a qubit whose average state is maximally mixed.

The script scores those identities against themselves. `j_h` and `j_p` are the closed forms (`dephasing_crossover_checks.py:94-99`). C1 subtracts them (`:221`). C3 calls `j_h(r, w)` with no \(q\) (`:281-282`), so the span in \(q\) is zero by the signature. C5 writes \(\kappa\ln 2+w\varepsilon\) against \(\kappa\ln 2\) (`:308-309`). C10 compares \(h((1+|r\sin\theta|)/2)-h((1+r)/2)\) with the same expression (`:403-406`). C11 builds the headline from the booleans and compares that string with the same boolean expression (`:433-455`). `NULL_DECOHERENCE` needs P strictly cheaper for every \(w>0\) as soon as \(\gamma\tau>0\). The grid contains \(w=1<2\ln 2\), and the identity keeps the threshold above \(2\ln 2\) at finite \(\tau\), so that label is unreachable while the closed forms stand.

The same predicates fail as soon as the rent or the readout changes. \(\kappa=1\), \(\gamma\tau=1\), where the locked threshold is \(1.973877\), the memo’s cell says stake \(2\) prefers the pointer and stake \(1\) prefers the phase hold.

| Alternative | What is charged | Locked cell | What the alternative does |
|---|---|---|---|
| A. Carrier entropy | \(J_H=h(\varepsilon)+w\varepsilon\), \(J_P=0\) (pure pointer) | \(w=1\) | Pointer is cheaper (\(J_H=0.939924\)). Locked P1 says the phase hold. At \(\gamma\tau=0\), \(J_H=0\). Locked Q3 wants \(\ln 2\). |
| B. Linear leak | \(J_H=(1-e^{-\gamma\tau})+w\varepsilon\), \(J_P=\ln 2\) | \(w=1\) | Threshold \(0.193085\). Stake \(1\) prefers the pointer. Locked P1 says the phase hold. |
| C. Squared Hamming | \(L=\varepsilon^2\) | \(w=2\) | Threshold \(6.245254\). \(J_H=0.269071<J_P\). The phase hold is cheaper. Locked P1 says the pointer. The fair-coin floor is \(4\ln 2=2.772589\), not \(2\ln 2\). |
| D. Stake-dependent rent | coefficient \((1+w)\) on \(I\) | \(w=2\) | \(J_P-J_H=+1.239472\). The phase hold is cheaper. Locked P1 says the pointer. |
| P2, linear coherence | \(q=0\), rent \(1-r\) instead of \(\chi\) | \(w=0.5\) | Threshold \(3.436564\). The pinch is cheaper (\(J_Z=0.250\), \(J_H=0.790\)). Locked P2 threshold is \(0.376662\), so the pinch is not cheaper. |

Q1, Q2, Q5, and the \(P_D=0\) half of Q3 are facts about the states and the projectors. They do not use the rent, so these four alternatives leave them alone. The headline rule requires P1, so under each alternative the label is no longer `CLUE_SPLIT`.

The scored run never built these alternatives. Given the chosen \(J\), the passes cannot miss. Record the run as a consistency check of that \(J\). The result stays **observed in-model**.

**H2. \(w/\kappa>h(\varepsilon)/\varepsilon\) is a restatement of the binary rate-distortion comparison.** With \(I_H=\ln 2-h(\varepsilon)\), \(L_H=\varepsilon\), \(I_P=\ln 2\), \(L_P=0\), and \(P_D=0\) on both eigenbasis records, the pointer is cheaper exactly when lossless storage at cost \(\kappa\ln 2\) beats a binary symmetric channel of crossover \(\varepsilon\) priced at \(\kappa(\ln 2-h(\varepsilon))+w\varepsilon\). That is the comparison of the endpoints of the binary Hamming rate-distortion function \(R(D)=\ln 2-h(D)\). Crossref HTTP 200 on 24 November 2026 identifies Shannon’s 1959 fidelity-criterion paper as `10.1109/9780470544242.ch21` (collected-papers chapter, issued 2009, container title “Claude E. Shannon”; the record has no abstract, so no sentence is quoted from it). Pure dephasing supplies only \(\varepsilon=(1-e^{-\gamma\tau})/2\). After the eigenbasis read the comparison is classical.

It is a different object from a quantum fault-tolerance threshold, which is a critical physical error rate. Crossref HTTP 200: Knill, Laflamme, and Zurek, Science 279:342 (1998), `10.1126/science.279.5349.342`; Aharonov and Ben-Or, SIAM J. Comput. 38:1207 (2008), `10.1137/s0097539799359385`; Shor, Phys. Rev. A 52:R2493 (1995), `10.1103/physreva.52.r2493`; Fowler, Mariantoni, Martinis, and Cleland, Phys. Rev. A 86:032324 (2012), `10.1103/physreva.86.032324`; Terhal, Rev. Mod. Phys. 87:307 (2015), `10.1103/revmodphys.87.307`; Dennis, Kitaev, Landahl, and Preskill, J. Math. Phys. 43:4452 (2002), `10.1063/1.1499754`.

It is a different object from a scrubbing or refresh schedule. Crossref HTTP 200: Saleh, Serrano, and Patel, IEEE Trans. Reliability 39:114 (1990), `10.1109/24.52622`; Schroeder, Pinheiro, and Weber, “DRAM errors in the wild” (2009), `10.1145/1555349.1555372`; Viola and Lloyd, Phys. Rev. A 58:2733 (1998), `10.1103/physreva.58.2733`. An elementary balance \((\kappa\ln 2)/T+w(\gamma T)/2\) has optimum cost \(\sqrt{2\kappa\ln 2\cdot w\cdot\gamma}\), proportional to \(w^{1/2}\). That balance is not what the locked script scores. The texts of Saleh and of Schroeder were not opened; the DOIs and titles were.

Landauer (`10.1147/rd.53.0183`) and Zurek (`10.1143/ptp/89.2.281`; with Habib and Paz, `10.1103/physrevlett.70.1187`) do not, by their Crossref titles, state this stake threshold. Crossref returned no abstracts for those three. The prereg already says a title is not a novelty proof (`PREREG.md:226`). That narrow sentence can stand. It leaves P1 a restatement of the rate-distortion comparison. Bennett, Int. J. Theor. Phys. 21:905 (1982), `10.1007/bf02084158`; Sagawa and Ueda, Phys. Rev. Lett. 102:250602 (2009), `10.1103/physrevlett.102.250602`; Faist, Dupuis, Oppenheim, and Renner, Nat. Commun. 6:7669 (2015), `10.1038/ncomms8669` (abstract: the minimal work is the entropy of the discarded information conditional on the output); Sartori and Pigolotti, Phys. Rev. X 5:041039 (2015), `10.1103/physrevx.5.041039`. Those price erasure, measurement, or the dissipation of keeping an error small. The chosen \(J_H\) charges the information that remains, \(\chi=\ln 2-S\), which falls as the bit decoheres. Lostaglio, Jennings, and Rudolph, Nat. Commun. 6:6383 (2015), `10.1038/ncomms7383`, abstract: free-energy relations do not describe quantum coherence. The headline comparison has \(P_D=0\), so coherence destruction is not in \(J_H\) or \(J_P\).

### Medium

**M1. The maintained index states the crossover as the price.** `STATUS.md` gives \(J_H\) and \(w/\kappa>h(\varepsilon)/\varepsilon\) as the T84 sentence. `theory/README.md` says a stable pointer encoding becomes cheaper only above a stake threshold that falls to \(2\ln 2\). The T73 row in that same table says the printed headline is fixed by the closed forms. The T84 row does not. `OPEN_WORK.md` says **PROVED (in-model)**. This review’s label is observed in-model.

**M2. At \(w=0\) and \(q=0\) the pinch “wins” because nothing is charged.** \(I_Z=0\), \(L_Z=1/2\), and \(q=0\), so \(J_Z=0\) while \(J_H=\chi>0\). The memo’s “stake 0 prefers the pinch” is the zero-information record. The formula is doing what it says.

### Low

**L1. Wording, personal data, and the derivation sentences.** On the added lines of `d2aeb81..29ffc8b` the only `law` is the hypothesis sentence, which matches the words of `CORE.md:7`. No universal-theory phrasing, no finished-question wording, no billing wording, and no phone or email address. `THEORY.md` and `CORE.md` are absent from the diff. The new sentences say the qubit, the qutrit, and the channel are inputs.

**L2. C9 adds a \(10^{-3}\) separation at \(\gamma\tau=1\).** The value is \(\chi(e^{-1})=0.069283\). The prereg’s Q4 fail sentence does not name \(10^{-3}\). The extra cut is met and does not manufacture the identity \(S+P_{D,Z}=\ln 2\).

## 1. Circularity

Covered by H1. The passes that flip under a plausible alternative are P1, P2, P4 (its sign rule is the same secant as P1), P5’s tie at \(w=0\) under the carrier-entropy cost (the pointer is strictly cheaper at stake 0), and the price half of Q3. The passes that do not flip are the state facts Q1, Q2, Q5, and \(P_{D,H}=0\). Because the headline needs P1, the headline flips with the cost. The scored script only evaluates the chosen \(J\), inside which those signs are identities. Consistency check. Observed in-model.

## 2. Literature beyond plain decoherence

Covered by H2. Plain statement: \(w/\kappa>h(\varepsilon)/\varepsilon\) is a restatement of the known comparison between lossless storage and a binary symmetric channel under linear Hamming loss. It is not a restatement of the quantum threshold theorem, of a DRAM scrubbing interval, or of a dynamical-decoupling pulse schedule. Every DOI named in H2 returned HTTP 200 from the Crossref API on 24 November 2026, with the title, authors, and year used above. The ten DOIs in `PREREG.md:213-224` were fetched the same day and match that table’s titles. `10.1109/24.52613` was fetched and is a different paper (Gandini, reliability sensitivity); it is not cited.

## 3. Units and scaling of the \(2\ln 2\) floor

\(h\) is in nats and \(\varepsilon\) is a probability, so \(h(\varepsilon)/\varepsilon\) and \(2\ln 2\) are nats per unit Hamming error. \(2\ln 2=1.38629436111989\ldots\) prints as `1.386294361120`. In bits the same floor is \(2\): a fully decohered bit saves one bit of rent and pays a stake on an error of \(1/2\), so the pointer is cheaper when \(w/2>\kappa\ln 2\).

The threshold depends on \(\gamma\) and the hold time \(T\) only through the product \(x=\gamma T\):

| \(\gamma T\) | \(w_\times/\kappa\) |
|---|---|
| \(0.01\) | \(6.300822\) |
| \(0.1\) | \(4.021138\) |
| \(1\) | \(1.973877\) |
| \(2\) | \(1.582026\) |
| \(5\) | \(1.395653\) |
| \(20\) | \(1.386294\) |
| \(\infty\) | \(2\ln 2\) |

\(\gamma=2\), \(T=1/2\) and \(\gamma=1/2\), \(T=2\) give the same \(1.973877\). The floor \(2\ln 2\) does not move with \(\gamma\) or \(T\). The finite threshold falls as the product grows. At a fixed stake above the floor the crossover time scales as \(1/\gamma\). There is no temperature in the scored units (\(\kappa=1\)). If the rent were \(kT\) per nat, the floor would be the stake \(w=2kT\ln 2\).

The cost that was scored is affine in \(w\). At the printed cell \(\gamma\tau=1\), \(w=2\), the stake elasticity \(w\partial J_H/\partial w\big/J_H\) is \(0.901222\).

Ace’s square-root candidate is already in the repository, and it is not this note. `CORE.md:91` gives the minimizing cost \(2\sqrt{kT\,a\,v\,w}-kT\,a\) above the stake \(kT a/v\). `theory/CLOCK_TERM_2026-11-23.md:55` records \(J^*\propto w^{1/2}\) for continuous diffusive tracking. The elementary scrub balance above is the same square root. `git grep` on `389f3bc` for `exponent`, `w^{1/2}`, `T_hold`, and `scrub` in the T84 preregistration and run log is empty. The results commit does not add an exponent in the T84 files. A \(w^{1/2}\) prediction is not credited here.

## 4. Flag only: the T68 clock term

`theory/CLOCK_TERM_2026-11-23.md:125` says a clock first pays when the best clockless look carries more than \(4\kappa/\lambda\) nats. That threshold does not move with the stake. T84’s long-hold floor is also a stake-independent nat threshold, \(2\ln 2\) nats per unit Hamming error, and it does not move with \(\gamma\) or \(T\) separately. The two expressions differ, and the decisions differ: pay for a clock, or switch a static encoding. This review flags the kinship. It does not test it. A separate preregistration would have to lock any claim that one floor is the other.

## What was rerun

Head `29ffc8b656f39fde1000fa8b9082b206882c374c` on `forge-dephasing-crossover`. The recomputation below does not import the scored script. It is `theory/reviews/dephasing_crossover_review_checks/recompute.py` on `forge-dephasing-review`.

| Check | Result |
|---|---|
| Prereg blob sha256 at `389f3bc` | `c6826685567aadeeb11ff1617b727a9dce69d8287688068f81429a859913203d` |
| Same blob at `29ffc8b` | unchanged |
| Lock time, then results time | `2026-11-24T20:48:53Z`, then `2026-11-24T20:59:40Z`. Author date equals committer date on both. Parent of the lock is `d2aeb81`. |
| Q1–Q5 inside the hashed file | five prediction headings, including the \(0.065406\) bar |
| `40c4060` `quantum_record_checks.out` | line 8 is `Q-coh PASS PD=0.065406 cost_gap=0.065406`; the errata line is `Q-coh FAIL PD=0.000000 cost_gap=0.000000` |
| Scored script against the stored stdout | byte match |
| `python3 tools/check_consistency.py` | `RESULT: PASS`. Wording FAILs 0. 29 INFO hits on frozen records. A first run missed freshness because this VM’s `origin/main` was still `0f37918`. After `git fetch origin main` the tip is `d2aeb81`, and `31aa997` is inside the five-commit window. |
| `python3 tools/check_fresh.py` | `RESULT: PASS` |
| `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` | 291 successes, 1 skip, 371.40s. The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). `numba` is not installed; `reviews/night2/CAUSAL_NULL_INVARIANCE/core.py` imports it. |

## What holds

The printed digits match an 80-place recomputation: \(10.210290\), \(1.386294361120\), \(4.021138\), \(1.973877\), \(1.395653\), \(J_P=0.693147180560\), \(J_H=0.701404\), \(\Delta=0.008256\), \(\chi(0.05)/0.05=0.025010\), the \(q=0\) pinch threshold \(0.376662\), \(P_D(c=1/8)=0.06540601797\ldots\) (gap \(1.797\times 10^{-8}\) from `0.065406`), \(P_D(c=1/4)=\tfrac12\ln 2=0.34657359\), and the respecting gap \(0.069283=\chi(e^{-1})\). An independent \(2\times 2\) projector calculation of \(P_D(\theta)\) matches the closed form to \(2.2\times 10^{-16}\). The hash, the commit order, and the presence of Q1–Q5 in the hashed file all hold. The channel, the qutrit block, and the dephasing map are inputs.

## Attacks tried

1. Hash and order. The lock blob matches the stated sha256. The preregistration is the same blob in the results commit. The script and the stored output are absent from `389f3bc`. Q1–Q5 are inside the hashed bytes. Git does not show whether an uncommitted draft of the script existed before the lock. The closed forms inside the lock already fix the signs, so an earlier draft would not have made an independent test.
2. Identity attack. Expanded \(J_P-J_H\) and \(J_Z-J_H\). Proved \((h/\varepsilon)'\) has the sign of \(\ln(1-\varepsilon)\), and checked \(r\chi'(r)-\chi(r)>0\). The fair-coin floor is exactly \(2\ln 2\).
3. Self-comparison attack on C1, C3, C5, C10, and C11, as in H1. The other two headline labels are unreachable inside the locked model.
4. Alternative costs A–D and the linear P2 penalty, at the locked cells. P1, P2, and the price half of Q3 flip. The headline flips with them.
5. Independent digits, the qutrit gap, and a projector build for \(P_D(\theta)\). No printed digit missed.
6. Literature. Crossref on the preregistration’s ten DOIs and on the rate-distortion, erasure, fault-tolerance, scrubbing, and decoupling records in H2. One guessed DOI (`10.1109/24.52613`) resolved to a different paper and was dropped. The inequality is the rate-distortion comparison. The Zurek and Landauer titles do not state it.
7. Units. The floor is nats per unit error, equal to 2 bits. It moves only with \(\gamma T\). The elasticity at the printed cell is \(0.901222\). `CORE.md:91` and the clock note’s \(w^{1/2}\) were not locked in `389f3bc` and are not credited.
8. Clock-term flag, not a test. Line 125 of the clock note is \(4\kappa/\lambda\) nats. The T84 floor is \(2\ln 2\). Kinship flagged. No claim tested.
9. Wording, personal data, and the untouched `THEORY.md` and `CORE.md`.
10. Consistency, freshness, and the full pytest with the numba path ignored.

Blockers remaining: 1
