# Deviations, composite contest

`theory/composite-contest-2026-11-24/PREREG.md` is unchanged. Predictions P1–P8 were not edited after the run.

- **D1.** Headline moved off the ε = 0 slice. Reason: checkpoint 1 in `theory/composite-contest-2026-11-24/PREREG_R2.md`, committed before any scoring run. P1 stays as a check of an identity.
- **D2.** Classical-direction control added, same price. Reason: the same checkpoint. Proved there, then checked in `control.out`.
- **D3.** Implementation, after the run was already specified. The rebit state step uses the analytic gradient of the loss on the Cholesky factor and a golden-section line search, and it stops when the factor stops moving, instead of a fixed 2000 finite-difference steps. The loss it returned equals 1/25 on the traceless effect set only (`decisions.out` line 2). See the memo errata: `±I` readouts reach loss 0.
- **D4.** Logged after the review, not a change of any stored output. Not produced: `pinfo` and `orbit` grids, `search_results.json`, `grid_results.json`, and hashes of the scripts. `I_A6` is hard-coded 0. G and R4c are constants in the grid. R4a copies H. The pivot `envelope.txt` was not written.
