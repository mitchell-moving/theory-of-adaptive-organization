# T84: the price of holding a phase, and when the pointer record is cheaper

*Tuesday 24 November 2026. Self-check, not an independent review. Preregistered in `PREREG.md` (commit `389f3bc`, sha256 `c6826685567aadeeb11ff1617b727a9dce69d8287688068f81429a859913203d`) before this run. `THEORY.md` and `CORE.md` are unchanged. The qubit, the qutrit, and the dephasing channel are inputs. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

## Why this approach

The cost in the question is \(J=\kappa I+q\kappa P_D+w L\) (`theory/pointer-basis-stakes-2026-11-24/MEMO.md:64-68`; `theory/QUANTUM_RECORD_PRICE_2026-11-24.md:11-13`), with ruin outside the sum (`CORE.md:27`). Draft #257, at `40c4060`, scored the same projectors two ways (`theory/record_ratio_reframes_checks/PREREG_QUANTUM.md:31-35`, `:67`; `quantum_record_checks.py:281-283`; `DEVIATIONS.md:19-23`; `quantum_record_checks.out:8`, `:24`). A split that respects the coherent block has \(P_D=0\). A split that deletes the off-diagonal costs \(0.065406\). This note asks whether dephasing at rate \(\gamma\) over a horizon \(\tau\) is that distinction, and whether the stake then makes a pointer record cheaper than holding the phase. The one-time-write reading (`CORE.md:78`) is scored beside it as the plain-decoherence null (`PREREG.md:136`).

## Results

Headline `CLUE_SPLIT` (`dephasing_crossover_checks.out:13`). `FAILS 0` (`:14`). Checks C0–C11 pass. \(\kappa=1\). The numbers below are the locked expressions at locked grid points. C1 and C2 scored every sign on that grid (`bad_cells=0`).

**C0. PASS.** Matrix \(I\), \(P_D\), and \(L\) match the three closed forms. Max absolute error \(5.551\times 10^{-17}\) (`dephasing_crossover_checks.out:1`).

**P1. PASS. Encoding crossover, not the null.** Design P, the stable pointer encoding, is strictly cheaper than design H, the phase hold, if and only if

\[
\frac{w}{\kappa}>\frac{h(\varepsilon)}{\varepsilon},\qquad \varepsilon=\frac{1-e^{-\gamma\tau}}{2}
\]

(`PREREG.md:100-104`). The threshold falls with \(\gamma\tau\). At \(\varepsilon=10^{-4}\) it is \(10.210290\). At \(\varepsilon=1/2\) it is \(1.386294361120\), which is \(2\ln 2\) (`:2`). A stake at or below \(2\ln 2\) never makes the pointer encoding strictly cheaper at a finite \(\tau\).

Locked evaluations, signs already inside C1: at \(\gamma\tau=0.1\) the threshold is \(4.021138\); at \(\gamma\tau=1\) it is \(1.973877\); at \(\gamma\tau=5\) it is \(1.395653\). At \(\gamma\tau=1\) and stake \(2\), \(J_P=\ln 2=0.693147180560\) and \(J_H=0.701404\), so the pointer encoding is cheaper. At stake \(1\), which is below \(1.973877\), the phase hold is cheaper. **PROVED (in-model)** as the closed form, confirmed on the grid.

**P2. PASS. Pointer pinch.** Design Z, the T73 \(\sigma_z\) pinch of the phase state, is strictly cheaper than H only when \(q<1\) and

\[
\frac{w}{\kappa}<\frac{2(1-q)\,\chi(e^{-\gamma\tau})}{e^{-\gamma\tau}}
\]

(`PREREG.md:116-120`). \(\chi(r)/r\) rises from \(0.025010\) at \(r=0.05\) to \(\ln 2\) at \(r=1\) (`:3`). The threshold therefore falls as the phase decoheres. At \(q=0\) and \(\gamma\tau=1\) it is \(0.376662\): stake \(0\) prefers the pinch, and stake \(0.5\) prefers the phase hold. For every \(q\ge 1\) on the grid, Z is not strictly cheaper. Longer holding shrinks the set of stakes on which the pinch wins. It does not enlarge that set.

**P3. PASS.** \(J_H\) and \(J_P\) do not move with \(q\). Both spans are \(0\) (`:4`). The eigenbasis records have \(P_D=0\), so the free ratio (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md:15`) does not enter this comparison.

**P4. PASS. Price of holding.** 

\[
J_H=\kappa\,\chi(e^{-\gamma\tau})+w\,(1-e^{-\gamma\tau})/2.
\]

The excess over the noiseless box is \(\Delta=w\varepsilon-\kappa h(\varepsilon)\). Max absolute mismatch \(8.882\times 10^{-16}\) (`:5`). At \(\gamma\tau=0\), \(J_H=\kappa\ln 2\). At \(\gamma\tau=1\) and stake \(2\), \(\Delta=0.008256\). Below the P1 threshold the excess is negative: the leaked information reduces the rent by more than the stake charges for the error.

**P5. PASS. The null, kept separate.** Under the one-time write \(\kappa\ln 2\) plus the stake only, the pointer encoding is strictly cheaper for every \(w>0\) as soon as \(\gamma\tau>0\), and the costs tie if \(w=0\) or \(\gamma\tau=0\) (`:6`). The strict winner does not depend on the size of a positive stake. That is the plain-decoherence restatement. It does not make P1 a pass (`PREREG.md:136`).

**Q1. PASS.** On the #257 block, projectors \(P_0=|0\rangle\langle 0|\) and \(P_1=|1\rangle\langle 1|+|2\rangle\langle 2|\) fix \(\rho(c)\) for every locked \(c\). \(P_D=0\) and, because this instrument has one state and no stake coordinate, \(J=0\). Max absolute residual \(0\). Jacobi eigenvalues match the block formula to \(1.110\times 10^{-16}\) (`:7`).

**Q2. PASS.** The crossing family, damping the off-diagonal by \(\alpha\), has \(P_D\) strictly increasing as \(\alpha\) falls. At \(\alpha=0\) and \(c=1/8\), \(P_D=0.06540602\), which is within \(1.797\times 10^{-8}\) of the stored six digits `0.065406` (`:8`; `quantum_record_checks.out:8` on `40c4060`). At \(c=0\), \(P_D=0\). At \(c=1/4\), \(P_D=0.34657359\). At \(q=1\), \(J=P_D\) on this block.

**Q3. PASS. Clue, not a vanishing price.** On the phase hold, \(P_D=0\) at every locked cell, and \(J_H=\ln 2=0.693147180560\) at \(\gamma\tau=0\) (`:9`). Destruction is zero. The price is not. The parenthetical in the #257 clue, that the whole price vanishes whenever the split respects the subspace, is false for a phase bit that still carries information.

**Q4. PASS.** For the pure phase bit, \(S(\rho(\tau))+P_{D,Z}(\tau)=\ln 2\) at every locked \(\gamma\tau\), max absolute error \(3.469\times 10^{-17}\) (`:10`). The entropy gained while holding equals the drop in the pointer-pinch destruction, and both are functions of \(e^{-\gamma\tau}\) only. At \(\gamma\tau=1\) the respecting record's \(S+P_D\) misses \(\ln 2\) by \(0.069283\), which is the remaining pointer destruction \(\chi(e^{-1})\). The partition belongs to the split that crosses the coherence.

**Q5. PASS.** \(P_D(\theta)\) matches the closed form (error \(0\)) and falls as \(|\sin\theta|\) rises, from the pointer axis to the state's own axis (`:11`).

## What is new, and what is the null

Plain decoherence says the off-diagonal decays as \(e^{-\gamma\tau}\) and that the pointer basis is the one the interaction leaves alone (Zurek, *Progress of Theoretical Physics* 89:281, 1993, doi `10.1143/ptp/89.2.281`; Zurek, Habib, and Paz, *Physical Review Letters* 70:1187, 1993, doi `10.1103/PhysRevLett.70.1187`; the sieve as read at `theory/pointer-basis-stakes-2026-11-24/MEMO.md:9`). Landauer's erasure bound, as this repo states it, is at least \(kT\ln 2\) per bit (`theory/SCALE_ENDS.md:23`; doi `10.1147/rd.53.0183`). Neither states a stake threshold that moves with \(\gamma\tau\).

P5 is that restatement, inside the frozen-record reading: any positive stake, and any \(\gamma\tau>0\), and the pointer encoding wins. P1 is not. Its critical stake falls from \(+\infty\) at \(\gamma\tau\to 0\) to \(2\kappa\ln 2\), and a stake below \(2\kappa\ln 2\) keeps the degraded phase cheaper than a perfect pointer bit because the rent has fallen. P2 is not a restatement either, and it points the other way: the pinch of a phase state wins only at low stake, only for \(q<1\), and on a set that shrinks as \(\gamma\tau\) grows.

**Model implication.** Conditional on the stock formula and on design P versus design H: the pointer encoding becomes cheaper only above \(h(\varepsilon)/\varepsilon\), a decreasing function of \(\gamma\tau\). Conditional on design Z versus design H and on \(q\ge 1\): the pointer pinch is never strictly cheaper. Conditional on the #257 projectors: \(P_D=0\) on the coherent block, and the crossing destruction at \(c=1/8\) is the stored \(0.065406\). Conditional on a pure phase bit: holding entropy and remaining pointer destruction partition \(\ln 2\), and the respecting record does not pay the destruction term. The full price of that record is still \(\kappa I+w L\).

## Deviations

None. `PREREG.md` was not edited after `389f3bc`. The script does not change a bar, a grid, or a sign.
