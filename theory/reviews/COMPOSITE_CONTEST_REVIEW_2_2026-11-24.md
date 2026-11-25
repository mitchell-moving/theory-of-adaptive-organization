# Independent review 2: tilted menu after the errata (T72)

*24 November 2026. Reviewed branch `forge-composite-contest` at `77e6c5a20ed61e1adc25f39c979017bbeb274822`, from a fresh clone. Draft PR https://github.com/mitchell-moving/theory-of-adaptive-organization/pull/1. Adversarial review. The author's files are not edited. Environment: Python 3.12.3, numpy 2.5.5, scipy 1.18.1 (HiGHS), sympy 1.14.0, numba 0.68.1.*

## Summary

The locked scripts reproduce byte for byte, the preregistration order holds, all 15 added DOIs resolve, `THEORY.md` matches upstream `main`, and the wording rules hold. The new headline does not survive as a statement about the rebit.

`theory/COMPOSITE_CONTEST_2026-11-24.md:36` says the rebit minimum on the tilted menu is `2.1492408906328463e-03`. That number is the minimum of one family of single-strategy Powell runs. It is reproducible, and further single-strategy starts did not beat it. It is not the minimum over rebit behaviors. On the real singlet, mix two local readouts with one shared bit, weight `√(2/3)` on the sharp `xz` projections and the rest on `y → +I` for one wing and `−I` for the other. Mean loss is `2.3e-32`. The `3^5` list never builds that behavior: each pattern is one readout.

Priced as two rebits plus that bit (`K = 2 × 10 = 20`), the copy is feasible at `ε = 0` and still dearer than the complex record (`K = 16`) at every positive price. Priced as free shared randomness inside `K = 10`, every positive-price cell is LOSE, which is the first review's failure mode again. `theory/composite-contest-2026-11-24/PREREG.md:55` does not grant a correlated bit at the start, so contestant R as specified excludes the copy, and P-loss as a statement about the 243 runs still passes. The memo's "rebit minimum" drops that restriction.

Inside the implemented list the positive-price WIN is the identity `16 < 17 < 36` once `ε = 0` has made every positive loss infeasible. The mutual-information TIE is the same identity with the price term hardcoded to 0. Neither label uses the value `0.00215` except as a gate at `10^{-8}`.

## Problems, by severity

**1. High: a shared bit copies the tilted table, so the reported rebit minimum is the single-strategy search.**

`theory/composite-contest-2026-11-24/PREREG_3.md:33` argues from `⟨M⊗M⟩ = c² − |n|²` that a diagonal of `−1` forces a sharp planar readout and rules `±I` out. That identity is the same operator on both wings. Opposite signs are a second solution on the singlet: `⟨(+I)⊗(−I)⟩ = −1`. For any biases, a single pair of rebit observables on the singlet has the form `c_a c_b − n_a·n_b`. Matching `−u·v` would make `n_a·n_b` the Gram matrix `G + ccᵀ`. Both terms are positive semidefinite and `G` has rank 3, so the sum has rank at least 3 and cannot be a Gram matrix of planar vectors. No single readout on the singlet matches the table. The code's `±I` patterns miss the opposite-sign solution anyway: `run_menu3.py:88-92` and `:108-110` put the same operator on both wings, and the same sign on both wings gives diagonal `+1`.

One extra shared bit is enough. Let `p = √(2/3)`. Both branches prepare the real singlet.

- Branch 1, weight `p`: every setting is the sharp measurement along the normalized `(x, z)` part of the menu vector. For `y = (1,1,1)/√3` that direction is `(1,0,1)/√2`.
- Branch 2, weight `1−p`: the same four planar settings, and `y` is `+I` on one wing and `−I` on the other.

Pairs that avoid `y` match in both branches. The `yy` entry is `−1` in both. A planar setting `u = (u_x, 0, u_z)` correlates with branch 1 by `−(u_x+u_z)/√2` and with branch 2 by 0, so the mixture is `−(u_x+u_z)/√3 = −y·u`. Evaluated on the same operators as `run_menu3.py`, mean loss is `2.3045076783754708e-32` and the largest absolute entry error is `4.4e-16`.

Replacing the shared bit by the average observable `p M_planar + (1−p)(±I)`, which is one legal readout, gives mean loss `0.003591840513196231`. The bit is doing work that one operator cannot do. Convexity in the state at fixed measurements does not produce this table.

`theory/composite-contest-2026-11-24/PREREG_3.md:43-51` defines the official loss as 243 singlet evaluations plus 243 Powell runs, one state and one readout pattern per run, at most 40 iterations. That search cannot return the mixture. Its minimum, `2.1492408906328463e-03`, matches `theory/menu3_checks/decisions.out:4` and a fresh rerun byte for byte. From the prereg's own start, Powell hits the iteration cap (`success` false) at that printed value; allowing more iterations stops at iteration 55 with `2.1492408103896432e-03`. Twenty-four further starts, five opposite-identity starts, and a polish all land on that value or higher. The best single strategy found is `2.1492408103896432e-03`, above `10^{-4}` and above the feasibility gate `10^{-8}`. This is a search, not a certificate that no single state and one observable per setting does better.

`theory/composite-contest-2026-11-24/PREREG.md:55-60` withholds correlated shared randomness at the start and allows only what one reversible interaction creates from local product noise. One orthogonal conjugation on two rebits does not add a classical bit. Contestant R, as locked, excludes the copy, and P-loss as locked ("the search returns a smaller value", `theory/composite-contest-2026-11-24/PREREG_3.md:51,55`) passes. Hardy dimension of the bit together with two rebits, under local tomography across that cut, is `K = 20`. Then `J = λ ln 20` against `λ ln 16`, a gap of `0.223λ` against a tie band of about `0.030λ`, so the complex record still wins that pair at every `λ > 0`. If the bit is not charged and the behavior is entered at `K = 10`, `ΔJ = λ ln(10/16) ≈ −0.470λ` and every positive-price cell is LOSE.

`theory/COMPOSITE_CONTEST_2026-11-24.md:36`, `theory/README.md:50`, and `OPEN_WORK.md:120` state the search value as the rebit minimum. There is no `theory/menu3_checks/DEVIATIONS.md` recording that the minimum is over one readout per setting.

**2. High: under the implemented list, the positive-price WIN is the price, and the mutual-information TIE is an identity.**

At `ε = 0` a contestant is feasible only if its loss is at most `10^{-8}` (`run_menu3.py:314-320`). The single-strategy rebit loss `0.00215`, the classical worst-pair loss `0.04289`, and the product loss `0.162` all fail that gate. The feasible set that remains is C at `K = 16`, G at `K = 17`, and R4c at `K = 36`, each with loss about `10^{-32}` (`theory/menu3_checks/decisions.out:2,6`). For every `λ > 0`, Hardy order is strict because `16 < 17 < 36`. At `λ = 0` the dimension term drops out and those three tie. No cell in the grid is close: the rebit's `0.00215` is never added into `J`, because infeasible costs are infinite (`run_menu3.py:329-332`).

The mutual-information cells do not read a mutual information. `run_menu3.py:302` stores `I_A6` and the Holevo quantity as the constants `0`. `run_menu3.py:341-348` then sets every feasible contestant's information cost to 0 and every infeasible cost to infinity. G and R4c are feasible, so each information cell is TIE, and P-tie passes (`:357`). The failure condition in `theory/composite-contest-2026-11-24/PREREG_3.md:57` ("if their mutual information with the settings is not 0") is not implemented: a nonzero stored `I_A6` would leave P-tie passing. Lemma I0 already says this mutual information is 0 for every record fixed before the settings (`theory/composite-contest-2026-11-24/PREREG.md:21-23,185`). The TIE is that lemma plus two perfect copies, not a computed score.

`theory/composite-contest-2026-11-24/PREREG_3.md:56` says P-win fails if any implemented contestant has loss below `10^{-8}` at `K ≤ 16`. C itself meets that sentence. The code scores rivals only. Read as written, the failure condition is tripped by the complex record; read as the code runs, P-win is the identity above.

So the label flips with the price and with nothing else on this grid. Hardy gives WIN at every positive price. Mutual information gives TIE at every price. That is what `decisions.out:20-59` prints, and it is what the prereg's own "why a win is possible" paragraph (`theory/composite-contest-2026-11-24/PREREG_3.md:37`) reduces to once the single-strategy rebit stays above the gate.

**3. High: G, R4a, and the information coordinates are constants in the new script, and that is not logged.**

`theory/composite-contest-2026-11-24/PREREG_3.md:64-66` says each contestant is computed, including G's local correlators, the odd-momentum witness, separate Gmin and Gmax fits, and the mutual information and Holevo quantity.

- G's loss is C's loss (`run_menu3.py:300`, `G_loss {fmt(L_c)}`). No holistic coordinate is built. For a singlet at `η = 0` the local correlators do match C, so the number is the right one, and it is not a recomputation.
- R4a is the classical loss plus `witness()` (`run_menu3.py:239-240`), which returns `0.5 * ((−1)·1 + 1·(−1))`. That expression is `−1`. It is not computed from a phase-space model. The original control was defined to be `−1` (`theory/composite-contest-2026-11-24/PREREG.md:99`); "recomputed" (`theory/composite-contest-2026-11-24/PREREG_3.md:66`) overstates what the function does.
- Gmin and Gmax are one function, `product_loss` (`run_menu3.py:194-213,298-299`).
- `I_A6` and Holevo are literals (`run_menu3.py:301-302`).

The first contest logged this class of gap as D4 (`theory/composite_contest_checks/DEVIATIONS.md:8`). The tilted menu has no deviation file. P-win and P-tie are decided by these constants together with the rebit search and the classical linear program.

**4. Medium: the errata answers the first review at the top of the memo, and leaves the false floor standing below it.**

Checked against `theory/reviews/COMPOSITE_CONTEST_REVIEW_2026-11-24.md`.

| First-review item | Where it stands after `43c2e8d` and `77e6c5a` |
|---|---|
| 1. Rebit loss 0, both positive-price grids LOSE | Confirmed again with `rebit0.py`: mean loss `1.1011504292824115e-32`, worst-pair `4.930380657631324e-32`. The errata table (`COMPOSITE_CONTEST_2026-11-24.md:13-17`) matches that correction. `theory/pivot_worst_checks/DEVIATIONS.md:6` still says a search cannot put a rebit below `1/9`, and that this floor makes C win at every positive price. `COMPOSITE_CONTEST_2026-11-24.md:160` still says the rebit stays infeasible below `1/9` and that the headline is six WIN and two LOSE. |
| 2. Classical `K` was an atom count | Stated in the errata (`:25`). On the tilted menu the code charges `m_A m_B`. See the low item below: that product is 16, and 16 is the minimum at the Bell floor. It does not move the `ε = 0` label. |
| 3. The information-versus-dimension puzzle was the 6-state copy | Errata item 3 (`:26`) says so. The puzzle section (`:138-140`) still presents the opposition for that 6-state copy without the two-state record beside it. Holevo `1.0986122886681096` matches `ln 3` and `control.out`. | <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->
| 4. Missing outputs and hardcoded contestants | D4 logs them for the first contest. The tilted menu repeats the shortcuts (item 3 of this review) and does not log them. |
| 5. `PREREG_2` changed more than the cap | Stated in the errata (`:28`). The pivot section was not rewritten. |
| 6. Classical mean-loss minimum is `2(3−2√2)/25` | The memo (`:102`) now says so. `qp.py` gives `0.0137258300203048`. `qp2.py` gives a Frank–Wolfe dual gap of `−1.6e-15` and the same value. `theory/composite_contest_checks/decisions.out:198` has `J_H = 3.4520245437103150e-02`. `OPEN_WORK.md:120` still says the classical loss for three or more ontic states is a search upper bound. |
| 7. Three transcribed figures | `I_wings` for the rebit is `1.3862943611198841` (`theory/composite_contest_checks/decisions.out:5` and the memo table). CHSH `−2.8284270928652249` is `theory/composite_contest_checks/decisions.out:2`. `J_H` is line 198, as above. |

`OPEN_WORK.md:120` is the T72 row, and the same identifier is in `theory/README.md:50` and the three test module docstrings. Upstream `main` (`0f37918`) has T68 and no T69, T70, or T71; the commit message of `77e6c5a` says the branch's T69 row was renumbered to T72. The row text is three headlines in one cell: the pre-errata MIXED result with rebit loss `1/25`, the errata's 24/24 and 8/8 LOSE, and the tilted-menu WIN. Its file list names the memo, `composite_contest_checks/`, and `pivot_worst_checks/`. It does not name `theory/composite-contest-2026-11-24/PREREG_3.md` or `theory/menu3_checks/`. The README line does name `menu3_checks/` and states the errata and the tilted-menu label.

**5. Low: the classical product dimension on this menu is 16, the singular-value formula was left unfinished, and H's stored loss is the worst pair.**

A MILP at the Bell deviation `(√2−1)/2` is feasible for `m_A = m_B = 4` (`K = 16`) and infeasible for `1×32`, `2×8`, `3×5`, `4×3`, and `5×3`. Any rectangle with a smaller product is smaller in at least one wing than one of those infeasible caps, so 16 is the minimum `m_A m_B` at this worst-pair loss. `theory/menu3_checks/decisions.out:5` reports `K_atoms 4` and `K_prod 16`. The code gets that product by minimizing the number of atoms and then multiplying the response sets in that solution (`run_menu3.py:185-191`). On this menu the two procedures agree. H is infeasible at `ε = 0` because the loss is the Bell floor `4.2893218813452497e-02`, far above `10^{-8}`. The number stored as H's loss is that worst-pair value (`classical_minimax` returns `s*s`). `theory/composite-contest-2026-11-24/PREREG_3.md:27` defines the stake as the mean loss. Both quantities clear the gate, so the cell label is unchanged.

`theory/composite-contest-2026-11-24/PREREG_3.md:29` leaves the smallest singular value as `(√3 − √(4/3)?)` and asks the code to check the interval `(0.03, 0.04)`. The rerun prints `3.3673504811214609e-02`, inside the interval. The block bound `σ_min²/25 = 1.3469401924485844e-03` is the rank-at-most-2 floor used in the prereg. The single-strategy value sits above it. The mixture beats it, because a mixture of two readouts is not a rank-2 correlator.

## What held

**Reproduction.** Fresh clone of `forge-composite-contest` at `77e6c5a`. Outputs rewritten under `PYTHONHASHSEED=0`, `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, then compared with `cmp`.

- `theory/composite_contest_checks/run_all.py`: `lemmas.out`, `envelope.txt`, `decisions.out`, `control.out`, `crossref.out`, and `SHA256SUMS` match. `sha256sum -c` reports 5/5.
- `theory/pivot_worst_checks/run_pivot.py`: `decisions.out` matches. `sha256sum -c` reports OK.
- `theory/menu3_checks/run_menu3.py`: `decisions.out` and `SHA256SUMS` match. Runtime 273 s. P-loss, P-win, P-bell, and P-tie print PASS.
- `python3 tools/check_consistency.py` with `origin/main` at fork `main` `0f37918`: `RESULT: PASS`, `FAIL: 0`. The freshness check uses `origin/main` when that ref exists (`tools/check_fresh.py`). Judged against the feature HEAD it fails, because `STATUS.md` still names `d592662`; that SHA is the second first-parent commit of `main`, so the check passes in the setup the script describes.
- `python3 -m pytest -q`: 288 passed, 1 skipped, 764 s. The first review's count was 287 passed and 1 skipped, before `tools/test_menu3_checks.py`.

`rebit0.py`, `qp.py`, `qp2.py`, `lt.py`, and `piv.py` were rerun. The first review's numerical claims that were rechecked here still hold, including no local model with product dimension at most 10 inside the pivot caps 0.05 and 0.1.

**Preregistration order.** Author and committer timestamps are equal on all ten commits.

| Commit | Committer time | What landed |
|---|---|---|
| `e271ea9` | 03:59:25Z | `theory/composite-contest-2026-11-24/PREREG.md` only |
| `18a36c0` | 04:06:49Z | `theory/composite-contest-2026-11-24/PREREG_R2.md` only |
| `99aff27` | 04:17:20Z | first scripts and outputs |
| `e1d8af8` | 04:18:16Z | `theory/composite-contest-2026-11-24/PREREG_2.md` only |
| `eb84314` | 04:21:46Z | pivot run log and D1 |
| `d30f65a` | 04:24:20Z | pivot script and output |
| `c2a2a92` | 04:48:28Z | first review |
| `43c2e8d` | 04:54:53Z | errata in the memo, D4, OPEN_WORK |
| `f8af078` | 05:00:31Z | `theory/composite-contest-2026-11-24/PREREG_3.md` only |
| `77e6c5a` | 05:22:47Z | `run_menu3.py`, `decisions.out`, the minimum in the memo |

`git log --follow` shows each of `theory/composite-contest-2026-11-24/PREREG.md`, `theory/composite-contest-2026-11-24/PREREG_R2.md`, `theory/composite-contest-2026-11-24/PREREG_2.md`, and `theory/composite-contest-2026-11-24/PREREG_3.md` in exactly one commit. `git log -S 2.1492408906328463` finds that string first in `77e6c5a`. It is not in `theory/composite-contest-2026-11-24/PREREG_3.md`. The run log in `theory/composite-contest-2026-11-24/PREREG_3.md:7` says the minimum can come out above `10^{-4}` or not. The tilt `y = (1,1,1)/√3` is the symmetric unit vector; the out-of-plane component is what keeps the five settings from lying in the `xz` plane, where a rebit would match the table exactly. Git timestamps are the committer's clock. The 22 minutes between `f8af078` and `77e6c5a` cover writing `run_menu3.py` and one run of about 273 s. Nothing in the tree shows the result was written back into the prereg.

**DOIs.** The 15 DOIs on added lines were fetched from `https://api.crossref.org/works/<doi>`. All 15 returned a record. Year, first authors, and title match the citations: Müller–Masanes 2013, Renou et al. 2021, Gross–Müller–Colbeck–Dahlsten 2010, Masanes–Müller 2011, Chiribella–D'Ariano–Perinotti 2011, Hardy–Wootters 2011, Barnum–Wilce 2014, McKague–Mosca–Gisin 2009, Aleksandrova–Borish–Wootters 2013, Wootters 2010, Barrett 2007, Cirel'son 1980, Popescu–Rohrlich 1994, Hardy 2004, Montina 2008. `theory/composite-contest-2026-11-24/PREREG_3.md` adds no new DOI. Hardy 2001 is still not given a DOI.

**Wording.** On added lines: the hypothesis appears as the quoted "law of adaptive organization (hypothesis)"; the pivot deviation now says "computed by HiGHS"; the memo and `theory/composite-contest-2026-11-24/PREREG.md:17` say this work does not derive quantum theory. No "theory of everything", and no "bill" used as the cost. `tools/check_consistency.py` reports 0 wording failures. The miss on the first menu is still labeled "Puzzle, not a verdict" (`COMPOSITE_CONTEST_2026-11-24.md:140`).

**`THEORY.md`.** `git diff --stat 0f37918 HEAD -- THEORY.md` is empty. Upstream `main` of `Chad-Mitchell/theory-of-adaptive-organization` is `0f3791890078161a1172277162df5ac13ebbff46`, the same commit as fork `main`, and the blob is unchanged.

## Findings per new claim

| Claim | Finding |
|---|---|
| Rebit minimum `2.1492408906328463e-03` | **Problem.** True of the locked single-strategy search, reproduced byte for byte. False of rebit behaviors: one shared bit gives loss `2.3e-32` (problem 1) |
| P-loss PASS | Holds for the search the prereg defined. The search is not the full readout family |
| WIN under Hardy dimension at every `λ > 0`, `ε = 0` | Holds for the implemented contestants, as the identity `16 < 17 < 36` after the `10^{-8}` gate (problem 2). A shared bit at `K = 20` does not take the win. The same behavior at `K = 10` makes every positive cell LOSE |
| TIE under mutual information | **Problem** as a computed result. True as an identity: feasible copies are given price 0 (problem 2) |
| `3^5` enumerates the identity readouts | The 243 patterns are 243 single readouts. Opposite signs are not what the `±I` symbol does. The shared bit is outside the list (problem 1) |
| Classical model priced by `m_A m_B` | Confirmed for this menu. Minimum product at the Bell floor is 16, which is what the code stores (problem 5). Infeasible at `ε = 0` either way |
| G, R4a, R4c, Gmin, Gmax, mutual information computed | R4c's Born rule is computed (`run_menu3.py:216-236`) and matches. The others in this list are constants or a shared product fit (problem 3) |
| `PREREG_3` committed before its result | Confirmed by commit contents and timestamps, with the usual limit of a self-reported clock |
| Errata answers the first review | The label correction and items 2, 5, 6, and 7 are in the errata. The `1/9` floor and the old MIXED headline remain in force in the pivot deviation, the pivot section, and the T72 row (problem 4) |
