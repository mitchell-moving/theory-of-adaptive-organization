# Run log

## Computed contestants on the tilted menu

No new prediction, and no new preregistration. `theory/composite-contest-2026-11-24/PREREG_3.md` already required these four to be computed. Ace locked the headline price at Hardy `ln K_AB` (`theory/composite-contest-2026-11-24/PREREG.md:27`) and said not to open another contest.

(a) The positive-price win disappears if the computed holistic loss is not the singlet's local loss, or if Gmin or Gmax, from its own model, reaches loss at most `10^{-8}` at `K = 16`. Either one moves the `K = 17` row or puts a rival inside the gate at `K ≤ 16`.

(b) This is the cheapest check: 25 product traces, one two-point momentum mirror, and two product fits, from fixed starts, before any new menu. If the win disappears, re-read that row and stop.

## Maximal tensor product, written before the run

`theory/composite-contest-2026-11-24/PREREG_4.md` is the preregistration. The locked files are not edited.

(a) The positive-price win disappears if Gmax, the maximal tensor product, is feasible at `K = 16`. It also disappears if the real-plane record or the four-point phase space is feasible at `K ≤ 16`.

(b) The cheapest check is the rank of the product Paulis and the 25 product-effect probabilities of the singlet. If that already puts a loss-0 behavior at `K = 16`, stop and write the puzzle. Do not put the local-rotation restriction back.

After the run, 24 November 2026. Line (b) above is the pre-run text from `c597418`. The code evaluates 100 signed menu effects, not 25. The Gmax loss 0 follows from the singlet being in the maximal tensor product. The membership check `gmax_fit` returns the target table when the gates pass (`theory/menu3_checks/contestants.py:162`). It is not a search. The printed minimum `-8.3266726846886728e-17` is float error on a probability that is 0.

After the run, 24 November 2026, errata on the independent review of `b2ff239`. Commit `c539110` replaced the pre-run clause "the 25 product-effect probabilities of the singlet" with "the 100 signed menu effects of the singlet". Commit `4514d39` restored the bytes from `c597418`. The rewrite is still reachable in branch history and was not hidden.

After the run, 24 November 2026, location relabel. D12 named location `measurement/code`. That location is not used for the unfired arms: no MV gate fired, and neither arm at `run_menu3.py:416` ran. D12a records location `process`. The scored file is unchanged: `P-gmax PASS` at `decisions.out:65`, `P-win FAIL` at `:61`, headline TIE at `:105`.

After the merge of `9ed7298`, 24 November 2026. That commit appended a row that leaves the location unassigned. The row stays. D12a is the location row: `process`.
