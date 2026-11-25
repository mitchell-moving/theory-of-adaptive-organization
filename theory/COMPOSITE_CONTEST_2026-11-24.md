# Composite contest: two records, later local readouts

*Tuesday 24 November 2026. Branch `forge-composite-contest`. Preregistration `theory/composite-contest-2026-11-24/PREREG.md`, committed before any scoring run. Deviation `theory/composite-contest-2026-11-24/PREREG_R2.md`, also before any scoring run. `THEORY.md` is unchanged. Nothing here derives quantum theory. Labels: **PROVED (in-model)**, **KNOWN**, **ELEMENTARY**, **NUMERICAL**.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

## Errata

Checked `theory/reviews/composite_contest_review_checks/rebit0.py` after `c2a2a92`. Mean loss `1.101e-32`, worst-pair loss `4.930e-32`. Confirmed. A real singlet, with `y` read out as `+I` on one wing and `−I` on the other, matches the target. `theory/composite-contest-2026-11-24/PREREG.md` allows those readouts. The search and Lemma R kept only traceless effects, and the pivot hard-coded `1/9`.

Corrected labels, rebit loss 0 at `K = 10`, same tie band. The stored outputs are unchanged.

| Contest | Cells | Code output | Corrected |
|---|---|---|---|
| First, `λ > 0` | 24 | 21 WIN, 3 LOSE | 24 LOSE |
| Pivot headline, `λ > 0`, `ε ∈ {0.05, 0.1}` | 8 | 6 WIN, 2 LOSE | 8 LOSE |
| `λ = 0` | 6 and 8 | TIE | TIE |

`ΔJ = λ ln(10/16)` is about `−0.470λ`, past a tie band of about `0.028λ`.

The cause is one restricted search, shared with the lemma. The `y` setting is orthogonal to the other four, so its target row is zero off the diagonal. Opposite constants produce that row.

Other review items:

2. Classical `K` was the number of atoms in one behavior, not `K_A K_B`. Under the product rule the review's `lt.py` finds no local model with `K ≤ 10` inside the worst-pair cap at 0.05 or 0.1. Logged. It does not change the corrected labels.
3. A shared sign bit (`M = 2`) has loss 0 on the classical-axis control (`rescore.py`). The loss for C there stands. The information-versus-dimension split was about the 6-state copy only. Holevo of that ensemble is `ln 3`, and the printed value `1.0986122886681096` matches it.
4. Logged as deviations, not previously: no `pinfo` or `orbit` grid, `I_A6` hard-coded, G and R4c entered as constants, R4a copied from H, and `search_results.json`, `grid_results.json`, script hashes, and the pivot `envelope.txt` were not written.
5. `PREREG_2` changed the stake, the `ε` grid, and the search, not only the cap.
6. Mean-loss minimum is `2(3−2√2)/25`. The bound `(3−2√2)/25` is not what the search attains. Wording above is corrected.
7. Three figures above are corrected to `decisions.out`: `I_wings` `1.3862943611198841`, CHSH `−2.8284270928652249`, and `J_H` `3.4520245437103150e-02`.

**Diagnosis.** The menu builds in a real shortcut. Because `y` is orthogonal to every other setting, perfect anticorrelation on `y` is free for a rebit: constants, not a third direction. That is the menu, not the cap and not the price. `CORE.md:52` prices mutual information. On this protocol that price is 0 for every record set before the settings, so every loss-0 record ties, and with the rebit at loss 0 the dimension price makes every positive-`λ` cell a loss. The cap form never got to decide.

## ERRATA_2

Checked the shared-bit strategy in `theory/reviews/COMPOSITE_CONTEST_REVIEW_2_2026-11-24.md` (commit `4f04415`) on the operators in `run_menu3.py`. On the real singlet, mix sharp `xz` projections, weight `√(2/3)`, with `y → +I` on one wing and `−I` on the other. Mean loss `2.3045076783754708e-32`. Largest absolute entry error `4.4408920985006262e-16`. Averaging those two branches into one readout, `√(2/3) M + (1−√(2/3))(±I)` on `y`, gives mean loss `3.5918405131962310e-03`.

`theory/composite-contest-2026-11-24/PREREG.md:55` does not grant that bit, so it is not an R contestant. If it is admitted, the count used here is `K = 40`: each wing holds the bit, `m_A m_B = 4`, times the rebit record `10`. `K = 20` is the other count, the bit as one system. Both sit above 16. Uncharged, `K = 10`. The numbers are the sensitivity in Computed contestants, not the lock label.

`theory/composite-contest-2026-11-24/PREREG_3.md:29` leaves the singular-value formula unfinished. The svd value is `3.3673504811214609e-02` (`theory/menu3_checks/decisions.out:1`). That formula is not used.

## Computed contestants

`theory/composite-contest-2026-11-24/PREREG_4.md`, committed before this run. The rebit search number is unchanged.

| Id | K | Loss | Leaves its lemma? |
|---|---|---|---|
| C | 16 | `1.1898287380433425e-32` | singlet, `decisions.out:2` |
| R | 10 | `2.1492408906328463e-03` | one readout per setting, `:3`; infeasible |
| H | 72 | `1.4463870270106627e-02` | mean of squares, `run_menu3.py:209`; the squared worst entry `4.2893218813452497e-02` is on `:4`, and `:10` is the Bell check |
| G | 17 | `1.9786896432643543e-32` | no: product Paulis span rank 16 and `eta_gap` is 0, `contestants.py:55`, `:5` |
| R4a | 7 | `1.8885627596701121e-01` | yes: its own phase space, `contestants.py:167`, `:7`; `yy` is `-5.9487425149700646e-01` |
| R4c | 36 | `6.8737752773862176e-32` | the real plane, `contestants.py:227`; feasible, and alone it is still `λ ln(36/16)` |
| Gmin | 16 | `1.6233664462791825e-01` | no: it is the product in Lemma P, `contestants.py:117` |
| Gmax, orbit | 16 | `1.6233664462791825e-01` | `PREREG.md:105`: local rotations plus swap, the same bound as Gmin. That number is the Gmin product (`:7`). Infeasible | 
| Gmax, state space | 16 | `0` | `PREREG_4`: membership check, not a fit. The singlet is in the set, so `gmax_fit` returns the target (`contestants.py:162`). `-8.3266726846886728e-17` on `:7` is float error |

The witnesses are the models' own `yy` entries (`contestants.py:84`, `decisions.out:6`). R, H, R4a, and Gmin are not `−1`. C, G, R4c, and Gmax are.

**Model implication.** Under `PREREG.md` as locked: WIN, resting on a hand-restricted Gmax. Under `PREREG_4`: TIE. Both are conditional on the Hardy price `λ ln K_AB` (`theory/composite-contest-2026-11-24/PREREG.md:27`).

Under `PREREG.md:105` the orbit row's loss is the Gmin product number `1.6233664462791825e-01` (`decisions.out:7`), infeasible at `ε = 0`. G at `K = 17` and R4c at `K = 36` are feasible and dearer, so the positive-price cell is WIN. That group was granted by hand.

Under `PREREG_4` the positive-price WIN does not hold. The membership check returns the target table, loss 0 at `K = 16`, because the singlet is in the set (`contestants.py:162`, `decisions.out:29`, `:105`). `-8.3266726846886728e-17` is float error. `PREREG_4` is a new lock, written after the first result. At price 0 the feasible loss-0 records tie with C (`:11`). `I_A6` and Holevo are identically 0 (`contestants.py:262`, `:272`, `decisions.out:8`). Those identities cannot fail, and the claim that they separate contestants is dropped.

**Errata, 24 November 2026, after the independent review of `b2ff239`.** The script-checked headline is TIE (`theory/menu3_checks/decisions.out:105`). The orbit WIN is a recomputed prose substitution at lines 60-62 of this file, not a line the scorer prints. The number tied to `PREREG.md:105`, `1.6233664462791825e-01`, is the tilted menu's rank-1 floor. The menu in `PREREG.md:35-41` gives `0.2`. At `ε = 0` the label is the same for both.

**Outside the lock.** The shared bit is a sensitivity (`decisions.out:72-103`). The count used is `K = 40`. Charged at 40 or at 20, that pair is WIN. At `K = 16` it is TIE. At `K = 15`, and uncharged at `K = 10`, it is LOSE (`:99-103`).

## Open miss

Under `PREREG.md` as locked the cell is WIN, and that WIN rests on a hand-restricted Gmax. Under `PREREG_4` the loss 0 follows from the singlet being in the maximal tensor product. The membership check returns the target table (`theory/menu3_checks/contestants.py:162`). It is not a search. The menu also cannot see a coordinate that product effects ignore (`contestants.py:81`). No next contest lock. The state-space reading stays a sensitivity, distinct from the reachable-orbit lock. Neither the classical information coordinate nor the present cost chooses which preparations are available. An orbit lock needs each contestant's full reversible group, and for Gmax that group was chosen by hand. Do not open another contest on this menu. `I_A6` and Holevo are identically 0 and cannot fail (`contestants.py:262`, `:272`). L7 is the same kind of identity (`theory/composite_contest_checks/lemmas.py:247-251`). Mutual information does not answer the record-price question on this protocol.

## Menu without that axis

`theory/composite-contest-2026-11-24/PREREG_3.md`, committed before its script. `y = (1,1,1)/√3` is not orthogonal to every other setting. The locked search is `3^5` patterns, one readout per setting. Its minimum is `2.1492408906328463e-03` (`theory/menu3_checks/decisions.out:3`). That number is the search, not the minimum over rebit behaviors. The lock label is the computed-contestant section above. `theory/composite-contest-2026-11-24/PREREG_3.md:29` leaves the smallest singular value unfinished, and it is not cited as a finished bound.

## Why this approach

The single-system duel ties, because one generator uses a thin section of the quantum state space and a blurred classical rotor matches every readout on that section (`theory/probes-2026-11-23/reviews/DUEL_REVIEW.md` §6, on `upstream/ace-probe-memos-2026-11-23`). The review named the next question: two records that interact, or a question chosen only after the record is set. That is where complex quantum theory, real quantum theory, a classical hidden-variable model, and a composite without local tomography can come apart. Müller and Masanes (doi 10.1088/1367-2630/15/5/053040) already show that single-system postulates give a ball in every dimension, and that local tomography plus a continuous reversible interaction is what forces the qubit. The mirror review asked that R4a and R4c be controls in this contest, not a separate simulation (`theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md` §4).

The price is `λ ln K_AB`, the same Hardy dimension for every theory, because that is the record-size price the walls memo and the duel used. The memory coordinate at `CORE.md:52` is mutual information. On a protocol whose settings are drawn after the record, that coordinate is zero for every contestant (`theory/composite-contest-2026-11-24/PREREG.md` Lemma I0). It is reported. It is not the price that can separate the loss-zero theories.

## Checkpoints

### After the prereg commit, before any results

Full text: `theory/composite-contest-2026-11-24/PREREG_R2.md`, commit `18a36c0ee9610fb8ef8fef20e07b7c83ab0c2656`, after `theory/composite-contest-2026-11-24/PREREG.md` at `e271ea971a10fbff4d58484cd2942c98dca12518`.

(a) Only in part. Copying the singlet table ranks theories by the cost of that table. It does not show that the cost produces the table.

(b) Yes, on the ε = 0 headline. Loss zero is the singlet, the menu was built so the rebit rank bound and the classical Bell bound apply, and the dimension price was chosen because mutual information cannot separate the loss-zero theories. A pass of that slice checks an identity, in the same way the mirror numerics checked a conjugate the premises had already put in.

(c) Yes. The identity is a one-line comparison of 16, 17 and 36. A classical-axis stake can go the other way. A network with independent sources is sharper and was not started.

Change of course, logged before the run: the headline is H1–H2 in `theory/composite-contest-2026-11-24/PREREG_R2.md`. P1–P8 were not rewritten.

### After the first results

(a) Yes, for the question H1–H2 actually ask. The run answers it. The cost does not force complex structure on these two stakes. On a classical axis, the classical record wins whenever `λ > 0`. On the singlet menu, complex theory wins the identity slice and loses once the cap lets a cheaper record pay a small loss at a high dimension price.

(b) The identity was named and demoted before these numbers existed. The three LOSE cells at `λ = 0.1` were not built in: P8 locked no label. They come from the rebit loss sitting on the floor 1/25 and from the classical search, neither of which was given a numerical value in the prereg.

(c) Still open, and not a reason to rerun the headline. A certified minimum for the classical loss, below the search value 0.0137, could move a near cell. It cannot repair the LOSE cells, because those already lose to the rebit at the proved floor. The Renou network is a sharper real-versus-complex test and is a different experiment.

### Before finishing

(a) The question that would show a forcing is the one that was run after the deviation. On this task the answer is no.

(b) No remaining built-in headline. P1 is labeled as a check. H1 was proved in the opposite direction before the run. H2 was unlabeled and came back MIXED, with three LOSE cells.

(c) Two sharper tests were not run, on purpose. A branch-and-bound certificate that the classical loss cannot fall below the value that would flip a WIN cell, and the three-party network of Renou et al. 2021 (doi 10.1038/s41586-021-04160-4). The nested-layer fixed-point conjecture was not started. It would have been a second preregistration on another branch, and it would have delayed this contest.

## What was scored

Two stakes, one price. `J = λ ln K_AB + L`, tie band `0.01 · max(J, J') + 10^{−12}` (`theory/composite-contest-2026-11-24/PREREG.md` §6).

**Singlet menu.** Five directions, loss the mean squared gap of the correlator from `−u · v`. Grid `λ ∈ {0, 10^{−4}, 10^{−3}, 10^{−2}, 10^{−1}}`, `ε ∈ {0, 10^{−3}, 10^{−2}, 0.05, 0.2, 1}`.

**Classical axis (H1).** `n` uniform on the six poles, query a coordinate axis, score only the aligned pairs, loss the 0-1 error. Same `λ`.

Contestants and coordinates. `I_A6` is the mutual information between the later settings and the record. On the singlet menu it is 0 for every contestant, by the protocol (`decisions.out` lines 4–5). `I_wings` is the quantum mutual information of the prepared state. `K_hv` is the ontic cardinality of a local hidden-variable model, or `inf` when the CHSH sub-block exceeds 2.

| Contestant | K_AB | K_hv | I_A6 | I_wings | Loss on the singlet menu |
|---|---|---|---|---|---|
| C complex two qubits | 16 | inf | 0 | 2 ln 2 = 1.3862943611198906 | 0 |
| R two rebits | 10 | inf | 0 | 1.3862943611198841 | 0.040000000000000098 |
| H classical search | 1 through 8, chosen per cell | same M | 0 | depends on the mixture; not one state | envelope below |
| G holistic | 17 | inf | 0 | same singlet at η = 0 | 0 |
| R4a velocity-flip | same models as H | same M | 0 | same as H | same as H; witness −1 (`lemmas.out` L7) |
| R4c real doubling | 36 | inf | 0 | the simulated singlet | 0 |
| Gmin, Gmax | 16 | a product needs no shared variable | 0 | 0 for a pure product | 0.2000000000000000 |

The rebit loss in that restricted search equals 1/25. The CHSH value of that behavior is −2.8284270928652249 (`decisions.out` line 2). See the errata: this is not the rebit's minimum.

Classical envelope, loss against ontic cardinality (`decisions.out` line 3; `envelope.txt`):

| M | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| L | 0.7337258300203047 | 0.2537258300203047 | 0.0937258300203048 | 0.0480115443060191 | 0.0312868056300609 | 0.0260335223279971 | 0.0217258300203048 | 0.0137258300203048 |

The value at M = 8 is the certified minimum of the mean loss, `2(3 − 2√2)/25 = 0.0137258300203048` (review `qp.py`, `qp2.py`). Lemma B's bound `(3 − 2√2)/25` is not attained. The worst-pair floor `(3 − 2√2)/4` is a different quantity, and the pivot did hit it.

## Results

**H1, classical axis.** C loses to H at every `λ > 0`, and ties at `λ = 0` (`control.out` lines 5–10). Both have loss 0. `K_H = 6`, `K_C = 16`. At `λ = 0.1`, `J_C = 0.2772588722239781` and `J_H = 0.1791759469228055`. The axis measurement on the matching spin state is deterministic (`control.out` line 2, defect 0). This matches the proof in `theory/composite-contest-2026-11-24/PREREG_R2.md`. **PROVED (in-model)**, code check PASS.

Holevo quantity of the six product states: 1.0986122886681096, below `ln 4 = 1.3862943611198906` and below `ln 6 = 1.7917594692280550` (`control.out` lines 4, 11–12). **NUMERICAL**, inside the bound that was proved before the run.

**H2, singlet grid.**

| Slice | Cells | Label | Where |
|---|---|---|---|
| ε = 0, λ > 0 (P1, the identity) | 4 | WIN | `decisions.out` line 277 |
| λ = 0 | 6 | TIE | line 279 |
| λ > 0 and ε ≥ 0.05 | 12 | MIXED: 9 WIN, then 3 LOSE | line 278 |
| all λ > 0 | 24 | MIXED | line 276 |

P1 through P5 pass (`decisions.out` lines 280–284). P6 and P7 hold as stated: `I_A6 = 0`, and each loss-zero protocol prepares one state.

The three LOSE cells are `λ = 0.1` and `ε ∈ {0.05, 0.2, 1}`. At `ε = 0.05` (`decisions.out` lines 249–257):

- C: `J = 0.2772588722239781`, loss 0, `K = 16`.
- R: `J = 0.2702585092994047`, loss 0.04, `K = 10`. C loses to R.
- H and R4a: `J = 0.1866409804180081`, loss 0.0480115443060191, `K = 4`. C loses to both.
- G: `J = 0.2833213344056216`, `K = 17`. C beats G.
- R4c: `J = 0.3583518938456110`, `K = 36`. C beats R4c.
- Gmin and Gmax stay infeasible at `ε = 0.05` (loss 0.2).

At `λ ≤ 0.01` the same loose caps are WIN. The stake gap is larger than the dimension gap.

## What this is, and what it is not

**Model implication.** On these two stakes, with this price, the ruin cap does not force complex quantum theory, and it does not force local tomography.

On a classical axis the cheapest feasible record in the named list is classical. Demanding the singlet table instead makes complex theory cheapest only while the cap excludes everyone who cannot copy that table, or while `λ` is small enough that a loss of 1/25 still costs more than `λ ln(16/10)`. At `λ = 0.1` the rebit, which does not have local tomography (`K_AB = 10 > 9`), undercuts the complex record. One extra holistic coordinate (`K = 17`) never helps a local readout and loses on the dimension price whenever `λ > 0` (P4). That is the price of an unused coordinate, not a derivation that composites in nature are locally tomographic.

**The information coordinate disagrees with the dimension price on the classical axis.** A perfect classical copy holds `ln 6` nats about `n`. The quantum ensemble's Holevo quantity is about 1.099 nats, under `ln 6`. Charging mutual information would rank that ensemble cheaper. Charging Hardy dimension ranks it dearer, because the theory's state space is 16-dimensional whether or not the protocol visits all of it. `theory/composite-contest-2026-11-24/PREREG_R2.md` stated this split before the run. The number 1.0986122886681096 is the check.

**Open miss (`CORE.md:169`), no update yet.** The two coordinates are both in the theory's own vocabulary, and they rank one and the same control in opposite directions. The likely cause is the one just named: dimension charges the state space of the theory, and mutual information charges only what that state holds about the world variable. Nothing here chooses which charge is the one a selected system pays. The singlet menu does not resolve it either, because there `I_A6 = 0` for every contestant and the coordinate is silent (`CORE.md:52`).

**KNOWN, not new.** The singlet correlator, the Bell bound, the failure of local tomography for real quantum theory, and the real simulation of complex quantum theory are in the references of `theory/composite-contest-2026-11-24/PREREG.md` §11. All 15 DOIs resolved again (`crossref.out`, FAILS 0). Hardy 2001 has no Crossref DOI and is not cited as a verified reference.

**Search limit.** The mean-loss minimum is certified, so it is not an open gap under the restricted readout set. At `λ = 0.01`, `ε = 0.05`, `J_H = 3.4520245437103150e-02` at `K = 8` against `J_C = 2.7725887222397813e-02` (`decisions.out` lines 195–198). The errata supersedes these labels.

## Files

- `theory/composite-contest-2026-11-24/` holds `PREREG.md`, `PREREG_R2.md`, `PREREG_2.md`, and `PREREG_3.md` (moved by `git mv`; bytes unchanged), and `PREREG_4.md`
- `theory/composite_contest_checks/lemmas.py`, `search.py`, `decide.py`, `run_all.py`, `crossref_check.py`, `common.py`
- Outputs: `lemmas.out`, `envelope.txt`, `decisions.out`, `control.out`, `crossref.out`, `SHA256SUMS`
- `theory/composite_contest_checks/DEVIATIONS.md`
- `theory/composite-contest-2026-11-24/PREREG_3.md`, `theory/menu3_checks/DEVIATIONS.md`
- Test: `tools/test_composite_contest_checks.py` reruns `run_all.py` and checks the locked hashes

Read-first files, all found on `upstream/ace-probe-memos-2026-11-23`: `theory/probes-2026-11-23/README.md`, `reviews/DUEL_REVIEW.md`, `duel/DUEL_MEMO.md`, `WALLS_MEMO.md`, `reviews/WALLS_REVIEW.md`, `MIRROR_MEMO.md`, `reviews/MIRROR_REVIEW.md`. On this main: `CORE.md` (the priced sum and the memory coordinate at line 52; the heat floor at line 70) and `theory/CLOCK_TERM_2026-11-23.md`. The clock term is not charged. This contest is one preparation and one later readout.

## Pivot: the cap is the worst question

The loose cells lost because the cap was a mean. On the traceless search the rebit's mean error is 1/25, which passes 0.05, and at `λ = 0.1` that is cheaper than a perfect complex record (`decisions.out` lines 249–251). `theory/composite-contest-2026-11-24/PREREG_2.md` changes only the cap: ruin is the worst menu pair, `L_∞ = max (C_ab + u·v)^2`. One linear program, not a sweep (`theory/pivot_worst_checks/RUN_LOG.md`). The minimum classical support at that error is 6, not the solver's first support of 11 (`DEVIATIONS.md` D2).

The classical worst-question loss is `4.2893218813467290e-02`, on the Bell floor, at `K = 6` (`theory/pivot_worst_checks/decisions.out` line 1). The stored print is six WIN and two LOSE (`theory/pivot_worst_checks/decisions.out` line 364). That print is superseded. A rebit with opposite constants on `y` has loss 0, so the headline is eight LOSE (errata above). The rebit is not stuck below `1/9`.

**What was learned.** The stored cells are the code output. The corrected headline is the errata, eight LOSE, because the constant readout was outside the search. No further variant on this menu.
