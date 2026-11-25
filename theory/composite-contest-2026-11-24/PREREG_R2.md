# PREREG R2: deviation before any scoring run

*Tuesday 24 November 2026. Committed after `theory/PREREG.md` (`e271ea971a10fbff4d58484cd2942c98dca12518`) and before any result-producing script is run. `theory/PREREG.md` is not edited. Original predictions P1–P8 stay in force. This file adds a checkpoint, a change of headline, and one control stake.*

## Checkpoint 1 (after the prereg commit, before any results)

**(a) Is this still the question that would show the ruin-capped cost forces quantum structure (local tomography, complex over real and classical)?**

Only in part. The question named in `PREREG.md` is whether that cost selects complex quantum theory over real quantum theory, a classical hidden-variable record, and a composite without local tomography, on one task with later local readouts. That is the question the single-system duel left open. It is the question that would show a forcing only if the task is not already the complex theory's own behavior. As locked, the target table is the singlet correlator and the headline slice demands exact agreement. That ranks named theories by the cost of copying that table. It does not show that the cost, starting from a task that does not mention the table, produces the table.

**(b) Is the setup quietly building the answer in, the way the time-symmetric mirror setup built in the conjugate?**

Yes, on the headline slice. Loss zero is the singlet. Lemma C of `PREREG.md` builds that state from a two-qubit unitary path. The menu contains `y` so the rebit rank bound applies, and the CHSH angles so the classical bound applies. Section 1 of `PREREG.md` adopts `λ ln K_AB` as the primary price because the mutual-information coordinate is identically zero on this protocol and cannot separate the loss-zero theories. Those choices place the headline WIN inside the premises. A code check of that slice checks an identity. It is the same pattern as the mirror numerics, which checked a conjugate the real, time-symmetric premises had already put in (`theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md` §2).

The loose-cap cells (`ε ≥ 0.05`, `λ > 0`) are not that identity. A cheaper theory with a positive loss can undercut `λ ln 16` there. No label was locked for them (P8).

**(c) Is there a cheaper or sharper test we're missing?**

Yes.

1. The identity itself does not need a search. Among the named theories with singlet loss 0, the dimensions are 16, 17 and 36, and 16 is the smallest. That one comparison is P1.
2. A classical-direction stake, defined below, uses the same price and the same cap on a world that is a classical axis. If the cost forced complex structure, the complex record would win there too. It does not, by the proof in this file.
3. A network with independent sources (Renou et al. 2021, doi 10.1038/s41586-021-04160-4, already verified for `PREREG.md` §11) separates real from complex quantum theory more sharply than one composite menu. It is not this contest, and it is not started here.

## Change of course

**Reason.** Checkpoint 1, answer (b). Keeping the ε = 0 slice as the headline would report an identity as evidence that the cost forces quantum structure.

**What changes.** The headline question is no longer "is every ε = 0, λ > 0 cell WIN?" Prediction P1 stays. A pass of P1 is a check of the identity, not that evidence. The headline is now the pair H1–H2 below.

**What does not change.** The menu, the contestants, the values of `K_AB`, the singlet loss, the grid, the tie tolerance, the classical search, the seesaws, and predictions P1–P8. No number in `PREREG.md` is rewritten.

## H1. Classical-direction control

Same price `J = λ ln K_AB + L`, same tolerance, same preparation rule.

**World.** `n` is uniform on the six poles `{±e1, ±e2, ±e3}`. The query `u` is uniform on `{e1, e2, e3}` and is drawn after the record is fixed. A pair `(n, u)` is scored only when `n · u ≠ 0`, that is when `n = ±u`. There are 18 pairs and 6 scored pairs. Both wings are scored. The loss is the mean, over scored pairs and over the two wings, of the 0-1 error of the wing's ±1 output against `sign(n · u)`.

**Classical record H.** Ontic state `n`, so `M = 6` and `K_AB = 6`. Both wings read `n` and output `sign(n · u)`. On every scored pair the output matches. `L = 0`. This record is reachable from a product under a permutation, by the same column-to-diagonal construction as `PREREG.md` §4 (H).

**Complex record C.** For each `n`, prepare the product `|n⟩ ⊗ |n⟩` and let each wing measure `σ · u`. On a scored pair the measurement is deterministic and equals `sign(n · u)`. `L = 0`. The theory's composite dimension is still `K_AB = 16`.

**Comparison.** At `λ = 0`, `J = 0` for both, so the cell is a TIE. At `λ > 0`, `J_H = λ ln 6` and `J_C = λ ln 16`, so `Δ = J_H − J_C = −λ ln(8/3) < 0`. Since `8/3 > 5/2`, `ln(8/3) > ln(5/2)`, and `ln(5/2) > 4/5` once `e^{4/5} < 5/2`. Let `x = 4/5`. The exponential terms through order 6 are `1`, `4/5`, `8/25`, `32/375`, `32/1875`, `128/46875`, `256/703125`. Their sum is `53/25 + 74176/703125`. The tail after order 6 is strictly smaller than `t6 · 4/31 = 1024/21796875`, because each later ratio is at most `x/7 = 4/35` and the geometric sum of those ratios multiplies `t6` by `4/31`. Over the denominator `21796875 = 31 · 703125` the three pieces are `46209375 + 2299456 + 1024 = 48509855`. Twice that numerator is `97019710`, and `5 · 21796875 = 108984375`. The first is smaller, so `e^{4/5} < 5/2` and `ln(8/3) > 4/5`. The tie band uses `0.01 ln 16 = 0.04 ln 2 < 0.04 · 7/10 = 0.028 < 4/5`. So `|Δ| > tol` for every grid `λ ≥ 10^{−4}`. **C LOSES to H on this control for every λ > 0, and TIES at λ = 0.**

**Real record.** A rebit's local Bloch vector lies in a plane. If that plane is `xz`, no state has `⟨Y⟩ = ±1`, so a Y measurement is not deterministic when `n = ±e2`. The control does not need a number for that loss. The code may report it. It is not part of H1.

**Information, reported, not the decision.** A perfect classical copy has `I(n; record) = ln 6`. The six product states `|n⟩ ⊗ |n⟩` live in a 4-dimensional space, so the Holevo quantity of the uniform ensemble is at most `ln 4 = 2 ln 2 < ln 6`. An information price and the dimension price disagree on this control: the dimension price favors the classical copy, and the Holevo upper bound is smaller than `ln 6`. The code prints the Holevo quantity. The decision on H1 uses `K_AB` only, the same primary price as `PREREG.md`.

## H2. What the singlet grid is evidence for

Run the grid in `PREREG.md` exactly. P1–P7 are checks. P1 passing means the identity survived the code, not that the cost forces quantum structure.

The part that can still fail is P8: the cells with `λ > 0` and `ε ≥ 0.05`, and the 24-cell `λ > 0` aggregate. **No label is locked.** The cost selects complex structure on the singlet menu, beyond the identity, only if those loose-cap cells are WIN. If they are MIXED, TIE, or LOSE, that is the result, and the memo states the scope: exact copying of the singlet table is an input of P1, and the tradeoff at a loose cap is the output.

## Deviation log

Logged here and, with the same text, in the memo's deviations. No result numbers exist yet, so none are recorded.

- D1. Headline moved from the ε = 0 slice to H1–H2. Reason: checkpoint 1 (b). `PREREG.md` unchanged. P1 retained as an identity check.
- D2. Classical-direction control added. Reason: checkpoint 1 (c). Same price, same cap, a world that is a classical axis.
