# Independent review: pointer-basis stakes (T73)

*Reviewer: independent. I did not write the preregistration, the memo, or the script. Tuesday 24 November 2026. Fresh clone of `forge-pointer-basis-stakes` at `13623ec`. `THEORY.md` was not edited by that branch or by this review. No pull request.*

**Findings.** The γ = 0 closed forms, the printed gap `0.096372378511`, the endpoint thresholds, and the grid minimizer `0.449422` are right. The headline `PRICING_ARTIFACT` was not at risk: predicate (A) flips by the closed forms already locked in `PREREG.md:66–72`, and the scoring rule returns that label on P4 alone. On this ensemble the two prices are affine complements at every dephasing I checked, so the partial-dephasing "both move" comparison at w = 100 is two signs of one curve sliding toward the same loss minimum. The Holevo thresholds are the stakes where the endpoints cross, not the stakes where θ = 0 becomes the minimizer. The sieve citation fixes a wrong title and then overshoots: PRL 70:1187 uses the name. Wording, the logged T70 → T73 deviation, the walls distinction, and the DOI table hold.

## What was rerun

Fresh clone of `mitchell-moving/theory-of-adaptive-organization`, branch `forge-pointer-basis-stakes`, head `13623ece9ea4b711715439b0de579eacc95ec4e2`.

| Check | Result |
|---|---|
| `pointer_basis_stakes_checks.py` against `pointer_basis_stakes_checks.out` | Byte-identical. sha256 `9c5ddf753822d0cc413829df506eb2206481873118d5dce1a645a82914a62f46` |
| `python3 tools/check_consistency.py` | Exit 0. `RESULT: PASS`. Wording FAILs 0. 29 INFO hits, all in older frozen records |
| `python3 tools/check_open_work.py` | Exit 0. `RESULT: PASS` |
| `python3 -m pytest -q tools` | 286 passed, 1 skipped, 378 s. The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). `tools/test_pointer_basis_stakes.py` passed |

The script uses the standard library only. The density-matrix check below does not import it. It rebuilds the four states, the dephasing channel, the projectors, the von Neumann entropies, the Umegaki divergence, and the conditional-mean loss from the Pauli matrices.

Upstream `Chad-Mitchell/theory-of-adaptive-organization` `main` is still `0f3791890078161a1172277162df5ac13ebbff46`. `git diff 0f37918 HEAD -- THEORY.md` is empty.

## What holds

**Closed forms at γ = 0.** For this ensemble, after complete dephasing, the ±x states are maximally mixed and the ±z states have Bloch length r. A projective measurement along n(θ) has outcome probabilities (1 ± r cos θ)/2 on ±z and 1/2 on ±x. Binary entropy is symmetric, H(M) = ln 2 by the antipodal pairing, and the mean squared error of the conditional mean is r²/2 − (r⁴ cos²φ cos²θ)/4. That is `PREREG.md:68–70`. A density-matrix evaluation of S(Φ(ρ)) − S(ρ), of D(ρ ‖ Φ(ρ)), of I(W; M), and of the loss agrees with those three formulas to 2 × 10⁻¹⁶ on a stride through the 721-point grid. The pinching identity D(ρ ‖ Φ(ρ)) = S(Φ(ρ)) − S(ρ) holds to 4 × 10⁻¹⁶. P_D and P_χ are the right functionals for the definitions in `PREREG.md:29–34`.

**P_D is uniquely minimized at θ = 0.** h((1 + u)/2) is strictly decreasing in u ∈ [0, 1], so P_D(θ) is strictly increasing on [0, π/2] and zero only at θ = 0. The loss excess is (r⁴ cos²φ / 4) sin²θ ≥ 0 (`MEMO.md:30`). Both terms of J_D are minimized at the dephasing axis, and the first is strict, for every w ≥ 0 and every φ. The memo's proof at `MEMO.md:30–34` is correct. The first grid step, θ = π/1440 ≈ 0.002182, already costs P_D = 4.95 × 10⁻⁷, which is far above the 10⁻⁹ tie, so uniqueness is not an artifact of `TIE` at `pointer_basis_stakes_checks.py:11`.

**The printed Holevo gap.** P_χ(0) = ½(ln 2 − h((1 + r)/2)) at r = 0.6 is 0.09637237851088…. Rounded to twelve digits it is `0.096372378511` (`MEMO.md:40`). The endpoint gaps w > P_χ(0) / (r⁴ cos²φ / 4) are 2.974456126879 at φ = 0 and 5.948912253758 at φ = π/4, again after correct rounding. At φ = π/2 the loss does not depend on θ, P_χ is strictly decreasing in θ, and θ = π/2 is the unique minimizer at every w. The cells at w ∈ {1, 10} sit on the predicted side of both endpoint crossings (`pointer_basis_stakes_checks.out:10–15` and `:22–27`).

**The partial-dephasing grid point.** At γ = 1/2, φ = π/4, w = 100, price P_D, the 721-point minimizer is index 206, θ = 206 π/1440 = 0.44942228…, which prints as `0.449422`. Neighbors 205 and 207 are more expensive. The same check puts the Holevo minimizer at index 220, printing `0.479966`. Those two cells in the stored output are the right grid points.

**Walls, duel, and the repository grep.** On upstream `ace-probe-memos-2026-11-23` at `e3e0e70`, `theory/probes-2026-11-23/reviews/WALLS_REVIEW.md:65` is the record-count headwind: at equal readable information (ln N, a Holevo cap) a quantum record has K = N² parameters against N classically. This note does not vary dimension and does not use that count. The distinction in `PREREG.md:13` and `MEMO.md:7` is accurate. `theory/probes-2026-11-23/duel/PREREG.md:27` is P-info, λ per nat of record–world mutual information, quantum case Holevo χ, and it is marked secondary there. Citing it as P-info is fair. On `0f37918` the sieve pattern has no matches, and the only Holevo hit in `*.md` is `theory/DIRECTIONS_2026-11-22.md:58`. On the probes branch the same sieve pattern matches only `WALLS_MEMO.md:188`.

**DOIs.** Direct Crossref lookups on 24 November 2026, with one retry after HTTP 429, match the table at `PREREG.md:154–160` and the two follow-up rows at `:166–167`: title, authors, issue date, container, volume, issue, and page or empty page field. `10.1143/PTP.89.281` resolves to the registered DOI `10.1143/ptp/89.2.281`. The bibliographic query `predictability sieve Zurek`, `rows=5`, again returned `total-results` 29702, and the first three items were the same three DOIs in the same order. `10.1103/PhysRevX.4.031015` is Horowitz and Esposito, "Thermodynamics with Continuous Information Flow", *Physical Review X* 4, 031015 (28 July 2014). The calibration (r/2) ln((1 + r)/(1 − r)) at r = 0.6 is 0.415888308336, which rounds to the prereg's `0.416` (`PREREG.md:19`, `MEMO.md:9`).

**Deviation log and wording of the memo.** `PREREG.md` is blob `d9806821` in both `6418237` and `13623ec`. `RUN_LOG.md` is blob `ad562daa` in both `bfd88ab` and `13623ec`. Commit `6418237` adds only the preregistration. The scored digits `0.449422`, `0.096372378511`, `2.974`, `5.949`, and `0.479966` are not in that file or in the run log. The pass-line change and the id change are the deviation at `MEMO.md:56–58`. Sibling rows on this fork are T69 (layer fixed point), T70 (constants, reassigned onto the id this prereg had reserved), T71 (information causality), and T72 (composite). T73 does not collide with those. The memo labels the γ = 0 slices **PROVED (in-model)** and the γ = 1/2 slices **NUMERICAL**, marks the model sentence as conditional on P_D, calls the open price a puzzle, and marks the last paragraph a conjecture. It does not call the hypothesis a law, does not say the question is finished, calls the record price a cost, and does not claim to derive quantum mechanics. Dephasing and the qubit stay inputs (`MEMO.md:3`, `PREREG.md:180`).

## Findings

### High

**H1. Predicate (A) was decided by the preregistration, and the headline rule cannot refuse it.** `PREREG.md:11` asks whether, at complete dephasing, every cost-minimizing θ is the sieve basis, for every stake. `PREREG.md:72`, in the locked model, already says P_D is zero only at θ = 0 and increases with |θ|, while P_χ is largest at θ = 0 and zero at θ = π/2, and the loss decreases in |cos θ| or does not depend on θ. At w = 0 the cost is the price. The minimizer of P_D is θ = 0. The minimizer of P_χ is θ = π/2. Q(P_D) is true and Q(P_χ) is false before any grid is scored. P4 (`PREREG.md:84`) restates that pair of truth values. The headline table (`PREREG.md:96`) returns `PRICING_ARTIFACT` when P4's flip is observed, and the code does that first:

```217:219:theory/pointer_basis_stakes_checks/pointer_basis_stakes_checks.py
    def rule(p1_ok, p2_ok, p4_ok, p6_ok):
        if p4_ok:
            return "PRICING_ARTIFACT"
```

P2, P3, P5, and P6 do not enter once P4 is true. A partial-dephasing miss would still print the predicted label. The stake is not what flips (A): the flip is present at w = 0. It is also not special to the four-point set. After complete dephasing every state is diagonal in z, so an x-measurement gives a fair coin for every state and I(W; M) = 0, while any z-contrast makes I(W; M) > 0 at θ = 0. P_D is zero only for a z-measurement whenever some state has a nonzero z component. Q flips for every such ensemble.

The same lock makes P1 unreachable. Its failing condition (`PREREG.md:78`) is a minimizer at θ ≥ 0.02 or a second grid point within 10⁻⁹. The closed form forbids both, and the first-step gap 4.95 × 10⁻⁷ confirms the tie tolerance is not doing the work. P4's failing condition ("the two truth values are equal", `PREREG.md:84`) names no input on which they are equal. P2, P3, P5, and P6 do name a cell outcome that would fail them. Those four do not control the headline.

C7 does not guard this. The preregistration (`PREREG.md:117`) says C7 checks that the table's label equals the label implied by C1–C6, and that a mismatch does not print the predicted word in place of the table. The implementation compares the rule to itself:

```226:227:theory/pointer_basis_stakes_checks/pointer_basis_stakes_checks.py
    label = rule(p1, p2, p4, p6)
    report("C7", label == rule(p1, p2, p4, p6), f"HEADLINE_RULE {label}")
```

That comparison is true for every boolean assignment. `tools/test_pointer_basis_stakes.py:19` then asserts the string `HEADLINE PRICING_ARTIFACT`. The stored output can still catch an edit, because the test also requires a byte match (`:22`). It does not test the counterfactual the preregistration described.

The preregistration was committed before the scored script. It was not committed before any derivation. `6418237` (05:19:13Z) contains only `PREREG.md`. `bfd88ab` (05:19:19Z) adds `RUN_LOG.md` and nothing else. The run log has no digits. The six seconds are not a hidden results dump. The derivation that fixes the headline is the closed-form paragraph inside the preregistration, plus the scratch evaluation admitted at `PREREG.md:174–176`, which was used to choose the ensemble and was not kept. The predicted word `PRICING_ARTIFACT` is in the lock (`PREREG.md:101`). What is absent, and this part of the timing claim holds, is the scored grid.

### Medium

**M1. On this ensemble the two prices are one function with opposite signs. The 0.2 rad bar does not separate them.** The definitions are the right ones for what they name. P_D is the mean entropy produced by the pinch, and it equals the mean Umegaki divergence. P_χ is I(W; M), which is the Holevo quantity of the classical outcome. They are not two prices of one coordinate. Theorem R1 (`CORE.md:52`) fixes the memory coordinate of a classical record as mutual information. The record in this note is the classical outcome M (`PREREG.md:34`, `PREREG.md:52`), so that coordinate is P_χ. A8, in the same sentence, only requires the coefficient to be nonnegative. P_D is the entropy produced by writing, a different term. `RUN_LOG.md:1` reads a flip as "Theorem R1 has not fixed the quantum record price". The flip shows that a different functional selects a different basis. It does not show that R1 is silent about the classical record this model keeps.

There is a sharper redundancy. The four states are two antipodal pairs, equally likely, so P(M = +1) = 1/2 for every θ and every γ. Then

P_D(θ) + P_χ(θ) = ln 2 − E[S(ρ)],

and the right-hand side does not depend on θ. A density-matrix scan gives a θ-spread below 4 × 10⁻¹⁶ at γ ∈ {0, 1/2, 0.8}. At γ = 0 the constant is P_χ(0) itself: P_χ = P_χ(0) − P_D. Minimizing one price is maximizing the other. The headline comparison is a sign.

At γ = 1/2 and φ = π/4 the loss alone is minimized at θ ≈ 0.4638. At w = 100 the two priced minimizers sit on either side of that angle: P_D at 0.4485 on a fine grid (the reported grid point 0.449422 is the coarser cell), P_χ at 0.4795. Each is about 0.015 rad from the loss minimum. The 0.2 rad bar (`PREREG.md:90`) is about 92 grid steps, so it is not a tie rule in disguise. It is crossed, for P_D, only once w ≳ 5 (θ = 0.196 at w = 3, θ = 0.262 at w = 5). At w = 1, where the stake term and the price are the same order, θ = 0.085 and P2 would fail. P2 and P6 compare w = 0 with w = 100 (`PREREG.md:80`, `:88`). At w = 100 the price is a small shift of the loss minimum, and the two w = 0 endpoints are opposite ends of the same curve, so both separations clear 0.2 together. "Both prices move θ" is true on the locked cells. It is not evidence that two independent prices agree about a tilt.

P2's code also demands uniqueness at both ends (`pointer_basis_stakes_checks.py:161–166`). The fail sentence in `PREREG.md:80` does not. On this run both minimizers are unique, so the extra demand did not manufacture the pass.

**M2. The Holevo thresholds are endpoint crossings. θ = 0 is selected later, and the minimizer in between is interior.** The formula at `MEMO.md:37–40` is the gap J_χ(0) − J_χ(π/2). The digits are right, and "the sieve endpoint wins" is the right description of that gap. It is not the stake at which θ = 0 becomes the minimizer. J_χ as a function of cos²θ is not linear in the price term. Just above each quoted threshold an interior angle is strictly cheaper than both endpoints:

| φ | Quoted endpoint crossing | Global minimizer there | Cheaper than either endpoint by | θ = 0 becomes the unique minimizer |
|---|---|---|---|---|
| 0 | w > 2.974456126879 | θ ≈ 0.763 | 0.00173 | w ≈ 3.209 |
| π/4 | w > 5.948912253758 | θ ≈ 0.763 | 0.00173 | w ≈ 6.418 |

The second stake is twice the first, as cos²(π/4) = 1/2 requires. The grid never samples this window: its stakes jump from 1 to 10, and on those cells the minimizer really is an endpoint (`MEMO.md:18` is right about the grid). A twelve-digit threshold that is not the selection threshold should say so. At φ = π/2 there is no such window; the memo's claim there is the full minimizer, and it checks.

**M3. The sieve title correction is right. "Not the paper that names the sieve" is not.** Crossref does not title `10.1103/PhysRevLett.70.1187` as the predictability sieve. The title is "Coherent states via decoherence", Zurek, Habib, and Paz, *Physical Review Letters* 70, 1187–1190 (1 March 1993). The criterion in that paper is least entropy increase: the abstract quantifies stability by the rate of increase of linear or statistical entropy, and says coherent states produce the least entropy for a weakly damped oscillator. That part of `PREREG.md:172` and `MEMO.md:7` is accurate, and it is an oscillator result, not this qubit.

The naming sentence is too exclusive. The PRL uses "predictability sieve" for the procedure, including "this procedure has been referred to as the predictability sieve", and applies it. Its reference [10] is Zurek's chapter in the 1993 Halliwell, Pérez-Mercader, and Zurek volume, together with "Theor. Phys. (to be published)", which is the PTP paper. PTP 89:281 (1 February 1993) is a naming source. It is not the only paper in this pair that uses the name, and the PRL points at the book chapter as well. `PREREG.md:172` and `MEMO.md:7` should say that the PRL applies the sieve and attributes the name to those two then-forthcoming expositions. The rest of the prior-art hedge is in good shape: empty Crossref abstracts do not state a stake, the five-row query is not offered as a novelty proof (`PREREG.md:172`), and the query reproduces.

**M4. The partial-dephasing move needs this ensemble. The headline does not.** Dropping the ±x states and keeping ±z, at γ = 1/2, φ = π/4, and w = 100, leaves the P_D minimizer at θ = 0. A non-commuting stake does not move the basis when no transverse Bloch component is left in the prior. The ±x states are what γ = 1/2 fails to erase, and they are also what makes H(M) independent of θ (M1). r = 0.6 is borrowed from the excluded comparison so the note does not introduce a second radius (`PREREG.md:50`). That is a reason. It is not a derivation of the four-point set. `PREREG.md:174–176` says a scratch evaluation on a coarse grid was used to reject an encoding in which θ cannot move, and that the scratch was not kept. No number from it is a locked criterion. A reviewer cannot see how close the 0.2 rad bar and w = 100 sat to that scratch. The complete-dephasing flip does not depend on this choice (H1). The sentence at `MEMO.md:50` that a stake moves θ only while a transverse component survives is the right scope for the channel. It is a statement about this prior, and the memo already confines the numerical claim to this grid.

### Low

**L1. The maintained index states the result without the memo's label.** `theory/README.md:50` says the relative-entropy minimizer is the dephasing axis for every stake, the Holevo minimizer is not, and a non-commuting stake moves θ at partial dephasing. The memo marks the first two **PROVED (in-model)** and the third **NUMERICAL**. The index line says "Self-check, not an independent review" and does not repeat those labels. `OPEN_WORK.md:120` does.

**L2. The reported 0.449422 is a grid coordinate.** It is the right cell. A 4001-point scan puts the continuous P_D minimizer at 0.4485, half a locked grid step away (step π/1440 ≈ 0.002182). The six printed decimals are the format `theta={theta:.6f}` at `pointer_basis_stakes_checks.py:140`, not a claim that the minimum is known to 10⁻⁶. Same remark for `0.479966`.

**L3. Nothing else in the wording scan failed.** `tools/check_consistency.py` reports 0 wording FAILs on the maintained documents. The new memo and preregistration are frozen records. They do not contain the universal-theory phrase, do not call the hypothesis a law (`finite-law Shannon` at `PREREG.md:23` is the term already at `CORE.md:52`), and the one use of a finished-question wording is the refusal at `PREREG.md:180`. `UNRESOLVED` is called a puzzle (`PREREG.md:101`). The record price is a cost.

## Answers to the review questions

1. **Rerun.** The script matches the stored output byte for byte. Consistency and open-work checks pass. The `tools/` pytest is 286 passed and 1 skipped.
2. **Preregistration.** The file at `6418237` is unchanged afterward and contains no scored grid digit. It does contain the derivation that fixes (A), the predicted label, and a disclosed unkept scratch. The run gate, six seconds later, contains no digits. The only logged deviation is T70 → T73, including the pass line, and that allocation matches the other open branches. P1 and P4 do not name an input that can make them fail inside the locked model. P2, P3, P5, and P6 name a failing cell outcome. The headline predicate was defined so that the flip was guaranteed.
3. **Math.** P_D's unique minimizer at θ = 0 is proved by the closed form. The gap and both endpoint thresholds match to the printed digits. They are not the stakes at which θ = 0 is selected (M2). The γ = 1/2 figure 0.449422 is the correct grid cell; the continuous minimizer is 0.4485. P_D and P_χ are defined correctly and, on this ensemble, are not independent (M1). The 0.2 rad bar is a real angular cut and a weak test at w = 100. The ensemble is inessential for (A) and essential for (B).
4. **Prior art.** The walls line is a different question (confirmed at `WALLS_REVIEW.md:65`). The DOI table matches Crossref, including the repeated bibliographic query. The sieve criterion is right; the claim that PRL 70:1187 does not name the sieve is not (M3).
5. **Wording and `THEORY.md`.** The memo meets the wording rules. The index line is missing the in-model label (L1). `THEORY.md` is byte-identical to upstream `main` `0f37918`.
