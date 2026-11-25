# Independent review 4: the maximal tensor product ties by copying the target (T72)

*24 November 2026. Fresh clone of `mitchell-moving/theory-of-adaptive-organization`, branch `forge-composite-contest`, head `71a4e30425803526e61c28549fff9e17d542a900`. Parents under review: prereg 4 `82a803dd5fc266c8778dfb80f35cbd1fe7c294d6` and the run log `c59741862619f9bfa2425b30658dd286dbc47a07`, both after review 3 at `1b8141c145d64c1fb9fb0a46f195fac101891cb1`. Draft PR https://github.com/mitchell-moving/theory-of-adaptive-organization/pull/1. Adversarial review. No file other than this review is edited. Environment: Python 3.12.3, numpy 2.5.5, scipy 1.18.1, sympy 1.14.0, numba 0.68.1. One thread for OpenMP and OpenBLAS.*

Rerun, from that clone, with `refs/heads/main` and `refs/remotes/origin/main` at `0f3791890078161a1172277162df5ac13ebbff46`: `python3 tools/check_consistency.py` (`FAIL: 0`, `RESULT: PASS`); `python3 theory/menu3_checks/run_menu3.py`; `python3 -m pytest -q` (288 passed, 1 skipped, 743.83s). The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). The menu3 stdout, the regenerated `decisions.out`, and the committed file are the same 7713 bytes, sha256 `a22aa42540ea1d9680f5745345a433f9345575fb6d2afa2e1269b17330448af8`, which is the lock in `theory/menu3_checks/SHA256SUMS`. Pytest reruns that script and the composite and pivot locks; those hashes held. `d592662` is the parent of upstream `main`, inside the five-commit window `tools/check_fresh.py` uses.

Every contestant row in `decisions.out` (40 rows) and every sensitivity row (25 rows) was recomputed from the printed loss and `K` with the script's `pair` rule. Zero mismatches. The new digits were also recomputed by separate code: the singlet trace, the real-plane Born rule, R4a's 16-atom Frank–Wolfe, Gmin from the fixed starts plus 40 random starts, and classical Frank–Wolfe at 2000 and 8000 steps. The memo's computed-contestant section quotes only numbers that appear in `decisions.out`.

## Findings

### HIGH

**Gmax is feasible at K = 16 and its loss is 0. Both are the inclusion of the singlet in the maximal tensor product, scored by returning the target. The positive-price TIE is that identity.**

The inclusion is real. A product effect on two Bloch balls is `(I + n·σ)/2` with `‖n‖ ≤ 1`. On the singlet its probability is `(1 − n·m)/4`, which is at least 0 for every such pair, and 0 when `n = m` is a unit vector. The quantum composite sits inside the maximal tensor product, in the same 16-dimensional real space of Hermitian 4×4 matrices. `theory/composite-contest-2026-11-24/PREREG.md:105` already prices that space at `K_AB = 16`, the same count as C. Under the state-space price, a behavior that reproduces `−u·v` has loss 0 and the same price as C, so the pair ties. Charging C's roundoff loss instead of exact 0 does not move the label: the gap is about `10^{−32}`, and the tie band is one percent of `λ ln 16`.

The code does not search that set. `theory/menu3_checks/contestants.py:154-164` returns `mean_loss(T)` and `T.copy()` when two gates pass, and otherwise returns loss `1` and a zero matrix. `mean_loss` (`:43-45`) is the mean square distance to `T`, so `mean_loss(T)` is 0. `T` is `-(MENU @ MENU.T)` (`:26`), the target the stake measures. Returning it is loss 0 for any contestant. The gates are tolerances around identities:

- `product_effect_min` (`:136-151`) evaluates the 100 signed menu effects, 5 directions times 5 times 4 outcomes. The printed minimum is `−8.3266726846886728e-17` (`decisions.out:7`), on the `yy` effect. The menu row `y` has float norm whose square is `1 + 2.22×10^{−16}`, so `(1 − y·y)/4` is a rounding of the probability 0. The gate is `≥ −10^{−9}` (`:161`). A value below that bound would mean this state was not the singlet.
- `max |T|` is `1 + 2.22×10^{−16}`. The same line allows `1 + 10^{−9}`. For unit menu rows, `|u·v| ≤ 1`.

`K` is the literal 16 in the same dictionary as C (`theory/menu3_checks/run_menu3.py:329`). At each positive `λ`, Gmax's `J` is `λ ln 16 + 0` and the comparator uses `λ ln 16` (`:317`, `:338`). The difference is 0 (`decisions.out:29`, `:39`, `:49`, `:59`). `cell` (`contestants.py:325-331`) returns TIE when any rival ties and none loses. Infeasible rivals are labeled WIN. G and R4c are WIN by `λ ln(17/16)` and `λ ln(36/16)`. The cell TIE is the Gmax pair (`decisions.out:21`, `:31`, `:41`, `:51`, `:105`).

`theory/composite-contest-2026-11-24/PREREG_4.md:29` states the success branch in advance: nonnegative product probabilities, hence loss at most `10^{−8}` at `K = 16`, hence the positive-price cell is TIE. The failure branch is a product probability below `−10^{−9}`. On a correct singlet that branch does not fire. `PREREG_4.md:13` is explicit that this drops the local-rotation restriction in `PREREG.md:105`, which was what put Gmax under Lemma P (`PREREG.md:154`) and under Theorem W (`PREREG.md:166`). The run log's clause (a) (`theory/menu3_checks/RUN_LOG.md:15`) says the win disappears if this Gmax is feasible at `K = 16`. The computation shows that feasibility by copying the target.

**Model implication.** Conditional on pricing the state space at Hardy `λ ln K_AB`, the positive-price cell ties, and the count `16 < 17 < 36` does not decide it. Conditional on the orbit restriction in `PREREG.md:105`, Gmax remains a product and Lemma P keeps it out. The memo already separates those readings (`theory/COMPOSITE_CONTEST_2026-11-24.md:63-65`). This run does not choose between them.

### MEDIUM

**H's printed loss and K are one Frank–Wolfe run, not the minimizing local model.** The stake is now the mean of squares, which answers review 3's objection to the squared worst entry. `PREREG_4.md` defines H as this run: uniform start, step `2/(k+2)`, 2000 iterations. The print matches that definition: loss `1.4463870270106627e-02`, `yy` `−9.8694952523738211e-01`, marginal supports 8 and 9, product `K = 72` (`decisions.out:4`, `:6`). An independent 2000-step run reproduced those digits. The same run has 11 atoms above `10^{−8}`, not 72. `PREREG.md:95` prices H by the number of ontic atoms. Continuing the same trajectory to 8000 steps reaches `1.4462260503519455e-02`, lower by `1.609766587172×10^{−6}`.

The cell does not use these digits. The first four menu directions are still the CHSH block: the signed sum of the target entries is `−2√2`. Lemma B therefore still floors every local mean loss by `(3−2√2)/25 = 6.8629150101523883×10^{−3}`. The stored squared worst entry `4.2893218813452497×10^{−2}` differs from `(3−2√2)/4` by `6.94×10^{−17}` (`decisions.out:4`, `:10`). Every local model, including the true minimum and R4a's polytope, stays above `10^{−8}`. H is infeasible either way, and an infeasible rival is a WIN for C (`run_menu3.py:335-342`). The memo's table presents `K = 72` and `1.4463870270106627×10^{−2}` as the contestant (`theory/COMPOSITE_CONTEST_2026-11-24.md:50`). Those are the locked run. They are not a certified minimum, and the infeasibility is the Bell floor.

### LOW

**Mutual information and Holevo are still identically 0.** The separation claim is dropped (`PREREG_4.md:23`, `decisions.out:8`, `:20`), so this no longer decides a cell. The code that remains builds the product of the 25 uniform settings with a one-point record (`contestants.py:250-252`). Its mutual information is `ln 25 + 0 − ln 25 = 0`. Holevo of one state is the state's eigenvalue entropy minus itself (`:270-272`). `P-mi` asks for a number at most `10^{−12}` (`PREREG_4.md:35`, `run_menu3.py:373`). The stored value cannot be anything else. `P-tie` passes because the information price is this constant (`decisions.out:62`).

**Lemma L7 is still the two-point identity.** `theory/composite_contest_checks/lemmas.py:247-251` sets `momenta` to `{+1, −1}`, mirrors them by a sign change, and checks that the weighted product equals `−1`. The same arithmetic on `{+2.5, −2.5}` returns `−6.25`. The menu witness is no longer this number. D4 says so (`theory/menu3_checks/DEVIATIONS.md:8`).

**Three deviation citations are one step off, and the preamble is stale.** The D1–D6 lines now land on the current files; the review-3 citations to `continue` and to the old information loop are gone. What remains: the preamble says `decisions.out` is not edited (`DEVIATIONS.md:3`), in the commit that regenerates it. D10 does record the previous sha256 `e6d331b13b7b87d836c56dbe62823a010c2a89c3f3caa5782efafb055db1686d`, which matches `f774ca3`. D3 cites `contestants.py:67` for G's loss (`DEVIATIONS.md:7`); that line is `def g_model`, and the return is `:81`. D10 cites `decisions.out:10` for the squared worst entry (`DEVIATIONS.md:14`); line 10 is `P-bell PASS`, and the number `4.2893218813452497e-02` is on line 4. The run log says "25 product-effect probabilities" (`RUN_LOG.md:17`); the code evaluates 100 signed menu effects.

**The unused failure branch would print WIN.** `PREREG_4.md:38` says that if P-gmax fails, the headline is withdrawn and the cell is re-read. `run_menu3.py:416` prints TIE only when P-gmax passes and P-win fails; otherwise it prints WIN whenever P-win passes. A failed gate makes Gmax infeasible, which the cell counts as a WIN for C, so P-win can pass and the headline would read WIN. This run took the success branch. The mismatch is not logged in `DEVIATIONS.md`.

**Two status lines state the tie without the model-implication label.** The memo labels it (`theory/COMPOSITE_CONTEST_2026-11-24.md:59`) and so does the headline string (`decisions.out:105`). `theory/README.md:50` and `OPEN_WORK.md:120` state the positive-price TIE as the status of the row. `OPEN_WORK.md:120` does call the G comparison a puzzle and names the condition `λ ln K_AB`. <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->

## What review 3 flagged

| Item | Status |
|---|---|
| G scored as C | Remains, and is now stated. `g_model` (`contestants.py:67-81`) traces the singlet on product Paulis. The joint effect moves from `0.5` to `1` to `0` with `η` and is not scored. `eta_gap` is 0 and the Pauli rank is 16 (`decisions.out:5`). G's loss `1.9786896432643543e-32` is the trace evaluation; C's `1.1898287380433425e-32` is the `vdot` evaluation of the same vector. The gap `7.8886090522101182e-33` is the printed `G_minus_C`. The largest entry gap between the trace correlator and `T` is `2.22×10^{−16}`. The memo's table says this does not leave Lemma G (`theory/COMPOSITE_CONTEST_2026-11-24.md:51`). P-blind predicts the match (`PREREG_4.md:28`). The WIN against G alone is still `λ ln(17/16)`. |
| Witness literal `−1` at `lemmas.py:248` | Menu witness fixed. Each model reports its own `yy` (`contestants.py:84-86`, `run_menu3.py:287-298`). R is `−8.2419079699618347e-01`, H is `−9.8694952523738211e-01`, R4a is `−5.9487425149700646e-01`, Gmin is `−8.3113308872951464e-01` (`decisions.out:6`). The H, R4a, and Gmin figures were reproduced by the separate runs. C, G, R4c, and Gmax still report `−1`, because their correlators are the target. L7 remains the identity above. |
| R4a reuses H's loss | Fixed. R4a's 16 joint atoms and 500 Frank–Wolfe steps give loss `1.8885627596701121e-01` at `K = 7` (`contestants.py:167-194`, `decisions.out:7`). An independent reimplementation matched the loss, the support 7, and the `yy` entry. H's loss is the other number. The responses are local ±1 functions, so Lemma B already keeps R4a above `10^{−8}`. The new loss leaves the copied-variable identity. It does not leave the local floor. |
| Gmin and Gmax share one fit | Fixed as a shared objective. Gmin is still the rank-1 Bloch product. The locked `gmin_fit` returns `1.6233664462791825e-01` (`contestants.py:117-133`). Forty extra normal starts did not go lower. Lemma P's floor is `1/25`. Gmax is no longer that product; it is the inclusion test in the high finding. The memo says Gmin does not leave Lemma P (`theory/COMPOSITE_CONTEST_2026-11-24.md:54`). |
| H's loss was the squared worst entry | Fixed as the stake. The mean is the Frank–Wolfe value; the squared worst entry is the Bell check. The medium finding is what remains: the mean is not certified, and `K = 72` is the product of the marginal supports. |
| `I_A6` and Holevo constant 0 | The claim that they separate contestants is dropped. The stored numbers are still the constant, as in the low finding. |
| No `K = 15` or `K = 16` sensitivity row | Fixed. Both are printed at every `λ` (`decisions.out:74-98`). Positive-price summaries (`:99-103`): `K = 40` WIN, `K = 20` WIN, `K = 16` TIE, `K = 15` LOSE, `K = 10` LOSE. The shared-bit loss `2.3045076783754708e-32` matches `shared_bit_loss`. Recomputing `pair` at those five counts reproduces every label. |
| Stale D1–D6 line numbers, and D1 in the present tense | The items were rewritten onto this file. D1 now says the shared-bit pair is not the cell (`DEVIATIONS.md:5`). The residual citation nits are the low finding. |

The rebit line is unchanged from `f774ca3` and is inside the byte-identical rerun: exact `5.3877607697943204e-03`, Powell `2.1492408906328463e-03` (`decisions.out:3`). P-loss and P-bell stay PASS.

## Preregistration

`PREREG_4.md` was introduced in `82a803d` at 2026-11-24T14:21:50Z. Author and committer timestamps match. Its blob `6f97e49b0f0d4674726c5558e967903636d24905` is unchanged at `71a4e30`. The results commit does not touch it. The run-log clause was added in `c597418` at 2026-11-24T14:21:54Z, blob `8f0856e89ff10da90cb3f83d75b651bd165b4d8c`. `git diff c597418 71a4e30` on `RUN_LOG.md` and on `PREREG_4.md` is empty. The results commit is `71a4e30` at 2026-11-24T14:41:11Z. The prereg and the failure clause contain thresholds and no printed result digit.

The four earlier preregistration blobs are the ones review 3 recorded, still at `theory/composite-contest-2026-11-24/`, and none of them changes in `82a803d..71a4e30`:

| File | Blob | Introduced |
|---|---|---|
| `PREREG.md` | `bf5e401041f4eb219c9222d69b7126ac540332c7` | `e271ea9` |
| `PREREG_R2.md` | `1b557869af563f0e73b7d201f9f19a93e66a3924` | `18a36c0` |
| `PREREG_2.md` | `d1080764b95ec38ef50a4cee64adb3a95034458c` | `e1d8af8` |
| `PREREG_3.md` | `c9f3dc6b9b3fdd06c3c53c98fd772cd6f820a016` | `f8af078` |
| `PREREG_4.md` | `6f97e49b0f0d4674726c5558e967903636d24905` | `82a803d` |

D10 is the deviation for this run. The failure branch of the headline, noted above, is the deviation that is not in that file. `THEORY.md` is not in the diff `1b8141c..71a4e30`.

## Wording

The lines added in these three commits do not say "theory of everything", "solved", or "bill". They do not call a miss a kill or a verdict. `PREREG_4.md:3` says this addendum does not derive quantum theory. The new memo section is titled Puzzle and does not claim a derivation of quantum theory, gravitation, or holography. The headline in the memo is labeled **Model implication** and is conditional on the Hardy price (`theory/COMPOSITE_CONTEST_2026-11-24.md:59`). The older sentence "Puzzle, not a verdict" is still at `:173`. `check_consistency.py` reports 0 wording failures on the maintained documents. The status-line label gap is the low finding. The added sentences contain no personal details. <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->

## DOIs

No new DOI appears in `82a803d..71a4e30`. The 15 works in `theory/composite-contest-2026-11-24/PREREG.md:215-229` each returned HTTP 200 from `https://api.crossref.org/works/<doi>` on 24 November 2026, on the first request, with the year and first authors named in the prereg: Müller and Masanes 2013 (`10.1088/1367-2630/15/5/053040`), Masanes and Müller 2011 (`10.1088/1367-2630/13/6/063001`), Chiribella, D’Ariano, and Perinotti 2011 (`10.1103/PhysRevA.84.012311`), Hardy and Wootters 2011 (`10.1007/s10701-011-9616-6`), Barnum and Wilce 2014 (`10.1007/s10701-014-9777-1`), McKague, Mosca, and Gisin 2009 (`10.1103/PhysRevLett.102.020505`), Aleksandrova, Borish, and Wootters 2013 (`10.1103/PhysRevA.87.052106`), Wootters 2010 (`10.1007/s10701-010-9488-1`), Renou, Trillo, Weilenmann, and Le 2021 (`10.1038/s41586-021-04160-4`), Barrett 2007 (`10.1103/PhysRevA.75.032304`), Gross, Müller, Colbeck, and Dahlsten 2010 (`10.1103/PhysRevLett.104.080402`), Cirel’son 1980 (`10.1007/BF00417500`), Popescu and Rohrlich 1994 (`10.1007/BF02058098`), Hardy 2004 (`10.1016/j.shpsb.2003.12.001`), Montina 2008 (`10.1103/PhysRevA.77.022104`). Hardy 2001 is still described as having no Crossref DOI (`PREREG.md:231`). The Renou DOI is the only one cited again outside that list, in the memo and in `PREREG_R2.md`, and it is the same work.
