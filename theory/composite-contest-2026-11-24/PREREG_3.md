# PREREG 3: menu without an all-orthogonal axis

*Tuesday 24 November 2026. Committed before any script for this menu. `PREREG.md`, `PREREG_R2.md`, `PREREG_2.md` and the stored outputs are not edited.*

## Run log

(a) Yes. The rebit minimum on this menu can come out above `10^{-4}` or not. Above it, the orthogonal-`y` shortcut was what decided the loss, and exact match is a win for the complex record under the dimension price. Below it, that story is incomplete and the complex record loses on dimension at every positive price.

(b) Yes. One menu. The identity readout is a discrete choice, enumerated in full. Angles and the state are optimized from one deterministic start per pattern, not from a random sweep. The gap to resolve is about `0.001` in mean loss (`σ_min^2 / 25` of the `{x, z, y}` block, below). A return below `10^{-4}` is a clear miss of that gap. No `λ` sweep is required to learn it.

## Price, as a choice

`CORE.md:52` fixes the memory coordinate as mutual information. On a record set before the settings, that mutual information is 0, so under it every loss-0 record ties. A strict win is then not available while G or R4c can copy the table. The cell rule that can come out WIN or LOSE uses Hardy `ln K_AB`, each contestant priced by the dimension of its two-wing state space (`K_A K_B` when the composite is a product). Both numbers are computed. This choice is not a claim that the mutual-information price is wrong.

## Menu

Same four settings as the CHSH block, and `y` tilted so it is not orthogonal to all of them.

- `z = (0, 0, 1)`
- `x = (1, 0, 0)`
- `p = (1/√2, 0, 1/√2)`
- `m = (−1/√2, 0, 1/√2)`
- `y = (1, 1, 1)/√3`

Target `T_ab = −u_a · u_b`. Mean loss as in `PREREG.md`. Cap `ε = 0` only. `λ ∈ {0, 10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}}`. Tie band unchanged.

Dots that are strictly between 0 and 1: `z·p`, `z·m`, `z·y`, `x·p`, `|x·m|`, `x·y`, `p·y` are `1/√2` or `1/√3` or `√(2/3)`. So each of the five settings has such a partner. `y·m = 0` and `x·z = 0` and `p·m = 0`, but none of those settings is orthogonal to every other one.

The `{x, z, y}` block of `T` has singular values `√3/√ something` computed as the roots of that Gram matrix. Its smallest singular value squares to `(√3 − √(4/3)? )` — the code prints the value from `numpy.linalg.svd` and checks it lies in `(0.03, 0.04)`. Call it `σ_min^2`. A rank-at-most-2 block is at least `σ_min^2` away in the sum of nine squares. Mean loss is then at least `σ_min^2 / 25`, which is about `0.00135`.

## Why a win is possible

A rebit ±1 readout has expectation operator `M = c I + n_x X + n_z Z` with `|c| + |n| ≤ 1`. On the singlet, `⟨M⊗M⟩ = c^2 − |n|^2`. The diagonal target is `−1`. Combined with `|c| + |n| ≤ 1`, equality holds only at `c = 0`, `|n| = 1`. So on the singlet every setting is a sharp planar measurement, and `±I` is out. Those planar correlators on `{x, z, y}` have rank at most 2, and the target block does not. Loss on the singlet is therefore at least `σ_min^2 / 25 > 0`.

The same four CHSH settings are in the menu, with the same target as before, so a local hidden-variable behavior has mean loss at least `(3 − 2√2)/25 > 0` on those four entries alone, and is infeasible at `ε = 0`.

G and R4c copy the singlet table and have `K = 17` and `K = 36`. Gmin and Gmax only reach product correlators; the `{x, z, y}` block is not rank 1. At `ε = 0` and `λ > 0`, under Hardy `K`, C is feasible and every other contestant is infeasible or strictly dearer, **if** no real state beats the singlet bound down to 0. That last clause is the prediction the search can falsify.

## Search

Deterministic. No random seed.

For each of the `3^5 = 243` patterns in `{+I, −I, planar}`:

- Build the real singlet.
- A `±I` slot is that multiple of the identity.
- A planar slot starts at the normalized `(x, z)` part of the menu vector (`y`'s start is `(1, 1)/√2`).
- Record the exact mean loss.
- Then one Powell run, at most 40 iterations, on the Cholesky factor of the state and on the free angles and biases of the planar slots, from that start.

The official rebit loss is the minimum over these 243 exact singlet values and the 243 Powell values. Prediction **P-loss** fails if that minimum is `< 10^{-4}`.

## Predictions, and the input that fails each one

- **P-loss.** Rebit minimum `≥ 10^{-4}`. Fails if the search returns a smaller value.
- **P-win.** If P-loss holds: every `λ > 0`, `ε = 0` cell is WIN under Hardy `K`. Fails if P-loss fails, or if any implemented contestant has loss `< 10^{-8}` at `K ≤ 16`.
- **P-tie.** Every `λ = 0` cell is TIE under Hardy `K`, and every `λ` cell is TIE under mutual information, because G and R4c match the table at information 0. Fails if G or R4c has loss `> 10^{-8}`, or if their mutual information with the settings is not 0.
- **P-bell.** The local-polytope worst-pair loss on this menu is at least `(3 − 2√2)/4`. Fails if the linear program returns a smaller value.

## Prior art

No new Crossref query. The readout algebra is the one in `PREREG.md` §4. The shortcut being removed is the review's `rebit0.py`. Hardy and Wootters, doi `10.1007/s10701-011-9616-6`, is already in `theory/composite_contest_checks/crossref.out`.

## Contestants, each computed

C: singlet correlators with `u·σ`. R: the search above, `K = 10`. H: linear program over the 1024 deterministic behaviors; `K = m_A m_B` for a minimum-support realization, not the atom count alone. G: the singlet state plus a holistic coordinate fixed at 0, local correlators recomputed, `K = 17`. R4a: the odd-momentum witness recomputed, and the same polytope loss as H, priced as `m_A m_B`. R4c: the real encoding of the singlet, Born probabilities recomputed, `K = 36`. Gmin and Gmax: product-correlator fits, separate functions, `K = 16`. Mutual information with the settings, and Holevo of a one-state record, are computed and stored.
