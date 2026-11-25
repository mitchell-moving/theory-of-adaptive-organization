# PREREG 2: worst later-chosen question

*Tuesday 24 November 2026. Written after the mixed result of the first contest was committed (`99aff2732ad9b8ef0a8ae4ef5d3783e27d3a347a`), and before any script for this pivot is run. `theory/PREREG.md` and `theory/PREREG_R2.md` are not edited. Their predictions and the stored outputs are not patched.*

## Why this pivot

The first contest did not give a complex-quantum win on its headline. H1, the classical axis, is a loss for every positive dimension price (`control.out`). H2, the loose singlet cells, is MIXED: nine WIN and three LOSE (`decisions.out` line 278). The three LOSE cells are `λ = 0.1` and `ε ∈ {0.05, 0.2, 1}` (line 249).

**The assumption that blocked the win on those cells is the form of the ruin cap.** The cap is the mean, over the whole menu, of the squared correlator error. The rebit search returned loss `4.0000000000000098e-02`, the floor 1/25 proved in `PREREG.md` Lemma R. That mean passes `ε = 0.05`. At `λ = 0.1` the rebit's cost is `0.2702585092994047` and the complex record's cost is `0.2772588722239781` (`decisions.out` lines 250–251). The rebit's CHSH value on that same behavior is `-2.8284270928652244` (`decisions.out` line 2), so the residual is not a failure of the Bell part of the menu. It is the questions that need a third local direction. An average lets the record miss those questions and stay under the cap.

It is not the pricing rule by itself. The same price makes the holistic composite (`K = 17`) and the real doubling (`K = 36`) lose to the complex record on every positive-`λ` cell (P4). A smaller `K` wins at `λ = 0.1` only because the cap admits a loss of 1/25.

It is not the contestant set. The rebit is the equal-`N` real theory, and it is the one that wins those cells.

It is not the classical-axis control. That loss was proved in `PREREG_R2.md` before the run. A classical world is tracked more cheaply by a classical record. This pivot does not reopen it.

## Checkpoint

(a) The question is unchanged: does this cost force complex structure over real and classical records when the question is chosen after the record is set? The first cap did not ask that. It asked whether the average over questions the referee might not pick stays small.

(b) Cells with `ε` below every competitor's proved floor are an identity again, of the same kind as P1. They are a check that a win is possible. They are not the headline. The headline is the band where the rebit is still excluded and the classical record is not excluded by the proof.

(c) If that band is still a loss, the next assumption to change would be how an approximate record is priced, not a further tightening of this cap. That next change is not made here.

## The one change

Same menu, same contestants, same `K_AB`, same tie tolerance, same `λ` grid. The stake and the cap both become the worst later-chosen pair, not the mean.

`L_∞ = max_{a,b} (C_ab + u_a · u_b)^2`.

Feasible if and only if `L_∞ ≤ ε`. Cost `J = λ ln K_AB + L_∞` when feasible, and infinite otherwise.

A question chosen after the record is one question. The ruin event is that question. The record does not get to average it against questions it can answer.

## Floors (a win is possible)

**C, G, R4c.** The singlet, the same singlet at `η = 0`, and the real simulation of `PREREG.md` Lemma R4c have every correlator equal to `−u · v`, so `L_∞ = 0`.

**R.** On settings `x, y, z` the correlator block `A` has rank at most 2, so some unit `q` has `A q = 0`. The error matrix `M = A + I` then has `M q = q` and spectral norm at least 1. The spectral norm is at most the Frobenius norm, and the Frobenius norm of a 3×3 matrix is at most `3` times the largest absolute entry. So some absolute entry is at least `1/3`, and `L_∞ ≥ 1/9`.

**H and R4a.** Lemma B of `PREREG.md`: the four CHSH squared errors sum to at least `3 − 2√2`. The largest of them is at least `(3 − 2√2)/4`. Hence `L_∞ ≥ (3 − 2√2)/4`.

**Gmin and Gmax.** Lemma P: four squared errors on the `z, x` block sum to at least 1. The largest is at least `1/4`. Hence `L_∞ ≥ 1/4`.

**Where the floors sit relative to the grid.**

- `(3 − 2√2)/4 > 1/25`. Cross-multiply: `25(3 − 2√2) > 4` iff `71 > 50√2` iff `5041/2500 > 2` iff `5041 > 5000`.
- `(3 − 2√2)/4 > 1/50`, by the same steps with `73 > 50√2` and `5329 > 5000`.
- `(3 − 2√2)/4 < 1/20`. Cross-multiply: `5(3 − 2√2) < 1` iff `14 < 10√2` iff `196 < 200`.
- `1/9 > 1/10` and `1/9 > 1/20`.

So at `ε ∈ {0, 0.02, 0.04}` every one of R, H, R4a, Gmin and Gmax is infeasible, while C, G and R4c are feasible with `L_∞ = 0`. The gaps `ln(17/16)` and `ln(36/16)` clear the 1% tie band for every grid `λ ≥ 10^{−4}` by `PREREG.md` Lemma Tol, which does not use the shape of the loss, only that both losses are zero. **Every cell with `λ > 0` and `ε ∈ {0, 0.02, 0.04}` is WIN.** That is the proof that a win is possible. It is a check, labeled as one. At `λ = 0` those cells are TIE, because G and R4c match `L_∞ = 0`.

At `ε ∈ {0.05, 0.1}` the rebit is still infeasible (`ε < 1/9`) and the classical record is not proved infeasible (`(3 − 2√2)/4 < 0.05`). **No label is locked on this band.** This is the headline. The old LOSE cell `λ = 0.1`, `ε = 0.05` sits in it.

## Grid and rule

`λ ∈ {0, 10^{−4}, 10^{−3}, 10^{−2}, 10^{−1}}`.

`ε ∈ {0, 0.02, 0.04, 0.05, 0.1, 0.12, 0.25, 1}`.

Cell rule and the 90% aggregate over `λ > 0`, same definitions as `PREREG.md` §6. `λ = 0` reported separately.

**Headline.** The eight cells with `λ > 0` and `ε ∈ {0.05, 0.1}`. The pivot succeeds only if every one of them is WIN. No such label is predicted.

**Check, not headline.** The twelve cells with `λ > 0` and `ε ∈ {0, 0.02, 0.04}` are WIN.

## Search (locked)

Deterministic. No seed. Same 1024 local vertices as `PREREG.md` §5, in the same index order.

The classical objective is `s(p) = max_{a,b} |corr_ab(p) + u_a · u_b|`, and `L_∞ = s^2`.

1. **M = 1.** Minimum of `s` over the 1024 vertices.
2. **M = 2.** For each unordered pair, `s` along the segment is the maximum of 25 absolute linear functions. Candidate steps are the endpoints, each zero of a linear function, and each point where two absolute values are equal. Keep the candidates in `[0, 1]`. Ties: lower index.
3. **Frank–Wolfe, 4000 iterations.** Start uniform. Step `2/(k+2)`. The linear oracle uses the subgradient of `s` at the worst menu pair, lowest index on a tie, and minimizes that coordinate's signed correlator over vertices, lowest vertex index on a tie. Exact line search on the segment by the same candidate list as in step 2.
4. **Support.** Weights above `10^{−10}`. Reoptimize with 2000 Frank–Wolfe iterations on that face, same line search.
5. **Backward elimination.** Drop the atom whose removal gives the smallest `s` after a fresh 2000-iteration reoptimization. Ties: lowest index. The curve used for the price is the lower envelope of steps 1, 2 and 5, in the `L_∞ = s^2` units.

For `M ≥ 3` the returned `L_∞` is an upper bound on the true minimum. A cell where C loses to this H is a loss against a concrete model. A cell where C beats this H is a win against this search. Cells where the floor already makes H infeasible do not depend on the search.

**Rebit.** Any behavior has `L_∞ ≥ 1/9`, so the search cannot create feasibility below that floor. Above it, minimize `L_∞` by alternating, for 40 rounds or until `L_∞` improves by less than `10^{−15}`: (i) each wing's effect in the `xz` disk, over 180 equally spaced angles and radii `{1, 1/2}`, keeping the best; (ii) 500 subgradient steps on the Cholesky factor, step length `1/(t+1)`, subgradient the worst menu pair, lowest index on a tie. Five starts, the same five pure states and initial angles as `PREREG.md` §9. Take the best `L_∞`.

**Product.** Alternate 200 rounds from the top singular vector of `T` and from the constant vector, each coordinate clipped to `[−1, 1]` to minimize that row or column's max absolute error. Take the best `L_∞`. The floor `1/4` does not depend on the search.

## Predictions

- **Q1.** Every cell with `λ > 0` and `ε ∈ {0, 0.02, 0.04}` is WIN. Check of the floors, not the headline.
- **Q2.** Every `λ = 0` cell with `ε ∈ {0, 0.02, 0.04}` is TIE.
- **Q3.** R is infeasible at every `ε ∈ {0, 0.02, 0.04, 0.05, 0.1}`, whatever the rebit search returns.
- **Q4.** H and R4a are infeasible at every `ε ∈ {0, 0.02, 0.04}`.
- **Q5.** Gmin and Gmax are infeasible at every `ε < 1/4`, that is every grid `ε` except `0.25` and `1`. At `ε = 0.25` the floor does not decide.
- **Q6.** For every `λ > 0`, C beats G and C beats R4c whenever both are feasible. Same gaps as Lemma Tol.
- **Q7.** No label is locked for `λ > 0` and `ε ∈ {0.05, 0.1}`, nor for the full `λ > 0` aggregate. That band is the measurement.

## Outputs

New directory `theory/pivot_worst_checks/`. Do not rewrite `theory/composite_contest_checks/`. Scripts write `decisions.out`, `envelope.txt`, and `SHA256SUMS`. A test reruns them and compares bytes. Deviations from this file go in the memo or in `theory/pivot_worst_checks/DEVIATIONS.md`, not by editing this file.
