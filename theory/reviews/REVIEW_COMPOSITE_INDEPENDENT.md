# Independent review

Head `b2ff239dc2b4dbac169c3d99fad65051dcb14ee8` (`mitchell-moving:forge-composite-contest`).
Base `04e9e5baef53ed1793116ea8e85468571ea08da5` (`upstream/main`).
Scope: the diff of that range, the preregistrations, and `main`. Working notes and chat context were not used.

The conditional headline survives the arithmetic. Under the hand-restricted orbit the four positive Hardy prices are WIN. Under `PREREG_4` they are TIE. The sensitivity row matches. One committed rewrite of the pre-run gate remains in the branch history, and one maintained ledger row now names the wrong preregistration.

## Checks

| Command | Result |
|---|---|
| `python3 tools/check_consistency.py` | exit 0. `FAIL: 0`. `INFO` 30. `RESULT: PASS`. Wording FAILs 0 on 31 maintained docs. Frozen records scanned 518. Section N: 68 rows, 0 mismatches. Process-rule FAILs 0. Core-rule FAILs 0. Advisory length warnings on `THEORY.md` (11325 words) and `README.md` (1857 words). |
| `python3 tools/check_fresh.py` | exit 0. `RESULT: PASS`. `STATUS.md` points at `3418781`, which is inside the last 5 first-parent commits of `upstream/main` `04e9e5b` (`04e9e5b 0e22302 3418781 26e1490 28db5ce`). |
| `python3 tools/check_open_work.py` | exit 0. `RESULT: PASS`. `items.json` not-DONE 62. `QUEUE.md` not-DONE 90. Union missing from `OPEN_WORK.md`: 0. |
| `python3 -m pytest -q` | exit 0. **295 passed, 1 skipped**, 817.33 s. The skip is `tools/test_lean.py:124` (Lean 4 / lake is not installed). |

The standing check scripts named `tools/check_*.py` are the three above. Pytest reruns the locked contest scripts (`run_all.py`, `run_menu3.py`, `run_pivot.py`) through `tools/test_composite_contest_checks.py`, `tools/test_menu3_checks.py`, and `tools/test_pivot_worst_checks.py`.

`tools/check_fresh.py` on this branch treats `origin/main` and `upstream/main` as alternative windows of width 5. This clone's `origin/main` is `0f379189`, whose window does not contain `3418781`. The pass uses the upstream window. The pointer is the third commit in that window.

Independent numerics used NumPy 2.5.5 and SciPy 1.18.1. They do not import the contest modules.

## DOIs

Every DOI added by the diff is one of the 15 works in `theory/composite-contest-2026-11-24/PREREG.md:215-229` (repeated from the memo and `PREREG_R2.md` / `PREREG_3.md`). Each returned HTTP 200 from `https://api.crossref.org/works/<doi>`. Title, author family names, and the Crossref issued year match the preregistration. Hardy and Wootters (`10.1007/s10701-011-9616-6`) is issued 2011, print 2012, as the prereg says. Wootters (`10.1007/s10701-010-9488-1`) is issued 2010, print 2012, as the prereg says. Cirel'son, Renou et al., and the other thirteen match on the first request or on a paced retry after Crossref returned 429. Hardy 2001 is still cited as having no Crossref DOI (`PREREG.md:231`).

## Independent math

Tilted menu, the one `contestants.py:16-25` scores: `z, x, p, m, y=(1,1,1)/√3`. Loss is the mean of 25 squared correlator errors. Feasible means loss `≤ 10^{-8}`. Tie band `0.01 · max(J, J') + 10^{-12}`.

**Orbit loss.** The quoted `1.6233664462791825e-01` is the Eckart–Young residual of the tilted target after its largest singular value, divided by 25. Recomputed singular-value residual: `1.62336644627918247341e-01`. Difference from the quoted float: 0. An alternating least-squares search over arbitrary factors in `[-1, 1]^5` reaches the same floor (`1.6233664462791830e-01`). A Fibonacci search over Bloch products `(n·u)(m·v)` reached `1.6234266855473820e-01`, six millionths above the floor; the author's Powell value sits on the floor, so a Bloch product attains it. On the orthogonal menu locked in `PREREG.md:35-41`, the same rank-1 floor is `0.2000000000000000`. Both numbers are far above `10^{-8}`, so both are infeasible at `ε = 0`. The WIN label does not depend on which of the two floors is used.

**Singlet and membership.** Singlet loss on the tilted menu: `1.1898287380433425e-32`, matching `theory/menu3_checks/decisions.out:2`. Real-plane Born loss: `6.8737752773862176e-32`, matching `decisions.out:7`. Product-effect probabilities of the singlet are `(1 - s_a s_b u·v)/4`, which are nonnegative because `|u·v| ≤ 1`. The float minimum I get is `-8.3266726846886728e-17`, the same digits as `decisions.out:7`. That value is a structural zero (`u = v` and equal outcome signs). No menu probability is below `-10^{-12}`.

**Bell floor.** On `z, x` against `p, m` the target signed sum is `-2√2`. Every local deterministic behavior has absolute sum at most 2, so the mean loss is at least `(3 - 2√2)/25 = 6.8629150101523918e-03`. H and R4a are local, so both are infeasible at `ε = 0` without using the Frank–Wolfe or phase-space search values.

**Rebit.** Forty-three L-BFGS starts on a mixed real state, with an independent biased planar observable on each wing, reached `2.3366452234256916e-03`. That equals the rank-at-most-2 Eckart–Young floor `2.3366446279183386e-03`. The published search minimum `2.1492408906328463e-03` (`decisions.out:3`) is lower, so a bias term beats a purely planar correlator, and this search did not find that basin. Both figures are above `10^{-4}` and above `10^{-8}`. The rebit stays infeasible at `ε = 0`.

**Shared bit.** The mixture at weight `√(2/3)` has loss `2.3045076783754708e-32`, matching `decisions.out:72`. A uniform grid in the weight is lowest next to that exact weight.

**Labels, recomputed.** Losses used: C and G at the singlet loss, R at `2.149e-03` (the smaller published figure), H and R4a at the Bell floor, R4c at the real-plane loss, Gmin and the orbit Gmax at `1.6233664462791825e-01`, membership Gmax at 0. Dimensions 16, 10, 72, 17, 7, 36, 16, 16.

| Price | `λ = 10^{-4}` | `10^{-3}` | `10^{-2}` | `10^{-1}` |
|---|---|---|---|---|
| Orbit Gmax (`PREREG.md:105` on this menu) | WIN | WIN | WIN | WIN |
| Membership Gmax (`PREREG_4`) | TIE | TIE | TIE | TIE |

The orbit WIN is C winning every pair: R, H, R4a, Gmin, and orbit Gmax infeasible; G at `K = 17` and R4c at `K = 36` feasible and dearer than the 1% band. The membership TIE is that same list with Gmax feasible at loss 0 and `K = 16`, so `Δ = 0`. At `λ = 0` the orbit cell is TIE, because G and R4c match C. The headline is about the positive prices.

**Sensitivity**, shared-bit loss, C at `K = 16`, every positive `λ`:

| Count | Label |
|---|---|
| charged `K = 40` | WIN |
| charged `K = 20` | WIN |
| `K = 16` | TIE |
| `K = 15` | LOSE |
| uncharged `K = 10` | LOSE |

That is `decisions.out:99-103`.

The gap that keeps G a WIN is `ln(17/16) / ln(17) = 0.02140`. The locked tie fraction is 0.01. The K=15 LOSE clears `ln(16/15) / ln(16) = 0.02328`. Neither label is a float-edge accident. `λ` cancels in these ratios; multiplying every locked `λ` by a positive constant leaves the labels in place. The additive `10^{-12}` is below the slack at `λ = 10^{-4}`.

## Preregistrations and the run log

Each preregistration is added in its own commit, the blob at that commit equals the blob at the head, and the commit is earlier than the result commit that scores it.

| File | Introduced | Blob | Result commit after it |
|---|---|---|---|
| `PREREG.md` | `e271ea971a10` 03:59Z | `bf5e401041f4eb219c9222d69b7126ac540332c7` | `99aff2732ad9` 04:17Z |
| `PREREG_R2.md` | `18a36c0ee961` 04:06Z | `1b557869af563f0e73b7d201f9f19a93e66a3924` | `99aff2732ad9` 04:17Z |
| `PREREG_2.md` | `e1d8af844d76` 04:18Z | `d1080764b95ec38ef50a4cee64adb3a95034458c` | `d30f65ab3ad0` 04:24Z |
| `PREREG_3.md` | `f8af0787beaa` 05:00Z | `c9f3dc6b9b3fdd06c3c53c98fd772cd6f820a016` | `77e6c5a20ed6` 05:22Z |
| `PREREG_4.md` | `82a803dd5fc2` 14:21:50Z | `6f97e49b0f0d4674726c5558e967903636d24905` | `71a4e3042580` 14:41Z |

`f774ca3509f6` renames the first four with similarity 100. No later commit changes those blobs.

Misses that are logged, and where:

- Orthogonal-menu positive-price cells, corrected from the stored print to 24 LOSE, and the rebit loss 0 that falsifies Lemma R: `theory/COMPOSITE_CONTEST_2026-11-24.md:9-16`, `theory/composite_contest_checks/DEVIATIONS.md` D3.
- Pivot stored print six WIN and two LOSE, corrected to eight LOSE: memo `:199`, `theory/pivot_worst_checks/DEVIATIONS.md`.
- `P-win` FAIL once Gmax is the maximal tensor product: `decisions.out:61`, `theory/menu3_checks/DEVIATIONS.md` D10.
- Shared bit outside the 243-pattern list: `DEVIATIONS.md` D1, memo `:34-38`.
- `I_A6` and Holevo identically 0, separation claim dropped: D6.
- Unfinished singular-value formula at `PREREG_3.md:29`: D7.
- `pinfo` and `orbit` grids, script hashes, and the hard-coded information coordinate on the first run: `theory/composite_contest_checks/DEVIATIONS.md` D4.

No prediction in `PREREG.md`, `PREREG_R2.md`, `PREREG_2.md`, `PREREG_3.md`, or `PREREG_4.md` comes back failed without a deviation or an errata paragraph. The stored `theory/composite_contest_checks/decisions.out` still prints the original P1 WIN. The memo says those bytes stay, and the corrected label is the errata. `tools/test_composite_contest_checks.py:41` still requires `P1 PASS`.

**Run log.** At the head, `theory/menu3_checks/RUN_LOG.md` begins with the exact bytes of `c59741862619` (1400 bytes). Both `(b)` lines are byte-identical to that commit, including line 17: "The cheapest check is the rank of the product Paulis and the 25 product-effect probabilities of the singlet." The correction is appended at line 19. It was not appended that way in every commit. See the blocking finding.

## Classical assumptions inside the quantum claims

**Commuting measurements.** The membership table violates the CHSH bound (`S = -2√2`). A single joint distribution over all five settings on each wing, the commuting or noncontextual record, cannot match it. The mean-loss floor above is the obstruction. `gmax_fit` (`theory/menu3_checks/contestants.py:154-163`) never builds that joint. It evaluates one product effect at a time on the singlet and, if the gate passes, returns the target. The TIE is the maximal-tensor-product reading. A commuting-record reading of the same menu is the Bell floor, and that cell would be WIN.

**Maximal tensor product versus the quantum product.** The singlet is a quantum state, and every quantum state is positive on product effects, so it lies in the maximal tensor product of the two Bloch balls. The linear space of that tensor product is 16-dimensional, the same Hardy count as two qubits. `gmax_fit` shows that this one quantum behavior is an admissible maximal-tensor-product behavior. It does not exhibit a post-quantum box, and it does not apply the preparation rule in `PREREG.md:53-60`. `PREREG.md:105` grants only `SO(3)×SO(3)` and the swap, which keep a product state a product and put the correlator on the rank-1 floor. `PREREG_4.md:13` drops that group and scores membership. Those are two different questions. The two headlines are the answers to those two questions. The code's printed headline (`decisions.out:105`, `run_menu3.py:416-421`) is only the membership TIE. The orbit WIN is the hand substitution of the Gmin loss into that cell rule. The substitution recomputes to WIN at every positive locked price.

**`gmax_fit` returns the target by construction.** If the minimum product probability is at least `-10^{-9}` and every target entry is inside `[-1, 1]`, the function returns `mean_loss(T), worst, T.copy()` (`contestants.py:162-163`). For the singlet the gate is an identity, as the probability formula above shows. The printed minimum is float error on a probability that is 0. The memo (`theory/COMPOSITE_CONTEST_2026-11-24.md:64`), `RUN_LOG.md:19`, and `DEVIATIONS.md` D5 say this. The check cannot fail on this state, and it is not a search. `I_A6` and Holevo (`contestants.py:250-272`) are the same kind of identity: the joint is built as a product of the settings with a one-point record, and Holevo subtracts a state's entropy from itself. L7 (`theory/composite_contest_checks/lemmas.py:247-251`) sets the mirrored momenta to the negations of `{+1, -1}` and sums `p * (-p)`. That sum is `-1` for any weights that add to 1. The memo says these identities cannot fail.

## Wording

The hypothesis sentence in `theory/COMPOSITE_CONTEST_2026-11-24.md:5` and `theory/composite-contest-2026-11-24/PREREG.md:7` is byte-for-byte the sentence in `CORE.md:7`, inside the quotation marks: `The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.`

`THEORY.md` at the head and at `upstream/main` is blob `6caadae569116a94a74563398be94cebf6e99e9b`.

Added lines do not say "theory of everything". They do not say "solved". They do not use "bill" as a cost. They do not call a miss a kill. "Puzzle, not a verdict" (`theory/COMPOSITE_CONTEST_2026-11-24.md:178`) refuses that word. `PREREG.md:17` and `PREREG_4.md:3` say this work does not derive quantum theory. The added lines do not claim a derivation of general relativity, quantum mechanics, or holography. The headline is marked **Model implication** at `theory/COMPOSITE_CONTEST_2026-11-24.md:60`, in the `theory/README.md` index row, and at `OPEN_WORK.md:123`. The diff adds no email address, phone number, or credential. The new open-work cell ends with the ledger token `needs Chad`, the same token the file already uses.

`PREREG.md:15` says "readout law" for the one-system generator. That use of "law" sits outside the hypothesis sentence. `check_consistency.py` reports it only as frozen-record INFO, because the preregistration is not a maintained document.

The headline, read with the sentence in front of it, is accurate. `theory/README.md` says the orthogonal-y grids are LOSE, then states the WIN under the hand-restricted Gmax and the TIE under `PREREG_4`. The errata at `theory/COMPOSITE_CONTEST_2026-11-24.md:14-16` is the orthogonal-menu result. The WIN sentence is the tilted cell with the group from `PREREG.md:105` substituted for membership. Detached from those sentences, "Under PREREG.md as locked: WIN" names the preregistration whose own menu the errata scores LOSE.

## Attacks tried

1. **Different Gmax lock.** Three scorings of the same losses. Orbit group, loss `1.6233664462791825e-01`, `K = 16`: WIN at all four positive prices. Maximal-tensor-product membership, loss 0, `K = 16`: TIE at all four. Membership with the dimension charged as 17, as if the larger set added a coordinate: the pair becomes the G pair, and the positive cell is WIN. The TIE requires the Hardy count to stay 16. That count is the dimension of the tensor product of two 4-dimensional state spaces. The attack reproduces the headline's split. It does not produce a third label inside either lock.

2. **Perturbed price.** The orbit WIN against G flips when the tie fraction exceeds `0.02140`. At the locked `0.01` it holds at every positive `λ`. At `0.03` G ties and the orbit cell becomes TIE. Replacing `λ ln K` by `λ K` leaves the orbit cell WIN (`Δ = λ` against a band of `0.17 λ` on `K = 17`). Replacing the price by the orbit dimension of one prepared state makes every loss-0 record pay the same, and the positive cell is TIE. That price is the one `PREREG.md:25` and `PREREG.md:70` already set aside. Scaling every locked `λ` by a positive constant does not move a label. The headline is stable under small price noise and unstable under a tie band a little above 2%, or under the orbit price the preregistration rejected.

3. **Alternative contestant, and an independent rederivation.** An independent rebit, mixed state, separate biases and angles on each wing, 43 starts, 269985 evaluations: loss `2.3366452234256916e-03`. Still infeasible. The cell stays WIN under the orbit lock and TIE under membership. Arbitrary rank-1 factors in the box attain the same loss as the Bloch product, so reading `f(u) g(v)` as a table rather than a Bloch product does not admit Gmin or the orbit Gmax at `ε = 0`. Putting the shared-bit behavior in as contestant R at `K = 10` makes every positive cell LOSE under both locks. That is the row `decisions.out:103`. The lock prices that bit at 40, or shows 20 beside it, and both of those are WIN. The attack breaks the headline only by admitting a record the preregistration and the deviation leave outside the cell.

The rank-1 floor, the Bell floor, the singlet probabilities, the real-plane loss, the shared-bit loss, and the four decision rows were rederived in a separate script. They match the quoted figures and the labels above.

## Findings

### BLOCKING

1. **Gate line (b) was rewritten in a commit that is still on the branch.** `c59741862619` locks `theory/menu3_checks/RUN_LOG.md` with the sentence "the 25 product-effect probabilities of the singlet." Commit `c539110acd8a` replaces that clause with "the 100 signed menu effects of the singlet" and appends a shorter after-the-run note. Commit `4514d39c8f96` restores the `c597418` bytes and appends the correction that is now `RUN_LOG.md:19`. At the head, line 17 matches `c597418` and the correction sits below it. The rewritten line remains reachable at `c539110`. A rewritten committed log line is blocking. The five preregistration blobs were not rewritten.

### HIGH

2. **`OPEN_WORK.md:96` now names this contest's preregistration for a different task.** The T45 row used to say the acting-memory hash lock had the same `PREREG.md` sha256, and that T43's preregistration commit was `40232f6`. Both occurrences were replaced by `theory/composite-contest-2026-11-24/PREREG.md`. That file was introduced in `e271ea971a10`. It is not commit `40232f6`, and it is not the acting-memory preregistration. The T72 row at `OPEN_WORK.md:123` is the contest row. The T45 sentence is a false citation, left behind by the path edit in the move.

### MEDIUM

None.

### LOW

3. **`PREREG.md:15` says "readout law"** for the one-system generator. The word sits outside the hypothesis sentence. The consistency check does not fail the file, because the preregistration is frozen history.

4. **The machine-checked headline is the TIE.** `decisions.out:105` and `tools/test_menu3_checks.py:25` lock "TIE". The orbit WIN is the prose substitution at `theory/COMPOSITE_CONTEST_2026-11-24.md:60-62`. The substitution recomputes to WIN. It is not a line the scorer prints.

5. **`tools/test_composite_contest_checks.py:41` requires `P1 PASS`.** That is the orthogonal-menu identity the errata corrects to LOSE. The memo says the stored output is unchanged. The test protects those bytes.

6. **The number attached to `PREREG.md:105` is the tilted-menu floor.** A recomputation on the menu in `PREREG.md:35-41` returns `0.2`. The quoted `1.6233664462791825e-01` is the tilted target's rank-1 floor, which `decisions.out:7` is. At `ε = 0` the label is the same for both floors.

7. **Freshness accepts either main window.** `tools/check_fresh.py:79-100` passes when the STATUS pointer lies in the last 5 first-parent commits of `origin/main` or of `upstream/main`. A pointer that has fallen out of the upstream window can still pass through a stale `origin/main`. The pointer on this branch is inside the upstream window, so this pass does not use that side.

## What holds

On the tilted menu, at `ε = 0`, with the locked 1% band and Hardy `λ ln K`:

- Hand-restricted Gmax, the rank-1 orbit: WIN at `λ ∈ {10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}}`.
- Maximal tensor product, membership, `K = 16`: TIE at those four prices, because the singlet behavior is in the set and the dimension matches C.
- Shared bit: WIN at 40 and at 20, TIE at 16, LOSE at 15 and at uncharged 10.

The orthogonal-y contest is the errata: LOSE at every positive price. Nothing here derives quantum theory.

Blockers remaining: 1
