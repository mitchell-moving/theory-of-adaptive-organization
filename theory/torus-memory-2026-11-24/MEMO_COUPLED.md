# T82 addition: the coupled flow-ratio loop

*24 November 2026 (UTC). Self-check, not an independent review. Separate lock `PREREG_COUPLED.md`, sha256 `0ff192a126020f647447a9511386944bcdda6d3de7ef55b0a7b16b2129f9c560`, commit `0352de5`, before the orbits. `PREREG.md` was not edited. T81's files were not edited. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

**In-model.** The destruction rate and the return share phase-lock. They do not cycle, and they do not wind on a torus. The walk's start selects which number they lock to. On the E-pair horizon the two locked returns are \(0.246706007043\) and \(0.067235517163\).

## Scores

| Item | Score | Where |
|---|---|---|
| I-port, T81 E-pair reproduced | PASS | `coupled_loop_checks.out:2` |
| H-settle, every orbit FIXED | PASS | `:3` |
| H-history, the two starts differ by more than 0.05 | PASS | `:4`, `:7` |
| H-init, map initial conditions agree | PASS | `:5` |

144 orbits. FIXED 144, CYCLE 0, TORUS 0, OTHER 0 (`:6`). FAILS 0 (`:33`).

The port matches T81's unscored E-pair at width 1 and \(T=415\): \(0.239059227845\) and \(0.048343059332\), absolute gaps \(1.515\times 10^{-13}\) and \(1.297\times 10^{-13}\) (`:2`).

## What the classes are

FIXED means both variables have stopped: one number, the phase-locked reading. CYCLE would have been a limit cycle, one frequency. TORUS would have been quasi-periodic winding, two frequencies. T81's prediction that the loop settles on one number holds for this lag map. The cycle and the winding did not appear, so there is no puzzle of that kind on this grid, and no coupling to compare with \(K_c=2/(\pi g(0))\).

The number is not unique across histories. On m3-b, every gain and every initial condition gives the same pair (`:7-18`):

| Start | Locked \(q\) | Locked destruction rate |
|---|---|---|
| midpoint | \(0.246706007043\) | 9 |
| far end | \(0.067235517163\) | 9 |

The gap is \(0.179470489880\). The one-shot E-pair gap at width 1 is \(0.190716168513\). Letting the width move does not merge the two histories.

The midpoint terminals reproduce T81's `POINT` values: \(0.106409485164\), \(0.246706007043\), \(0.422916079022\), \(0.246706007043\), \(0.000005868622\), \(0.866153244874\) (`:19-30`). That column is a relabel of T81's one-step map. The far-start column is not. It runs from \(0\) at the short horizon m3-e to \(0.817269719222\) at m3-f.

The destruction rate locks at an endpoint of the width menu, 1 or 9, on every cell (`:19-30`). Interior rates do not occur. On m3-c the midpoint locks at rate 1 and the far start locks at rate 9.

## Deviation

Gain \(\alpha=1.5\) leaves \([1,9]\) during the transient. Those 950 evaluations hold the endpoint return (`:32`; `DEVIATIONS_COUPLED.md`). The terminal is the same at the gains that stay inside. The hold does not choose it.

## Model implication

Inside this lag map, with T81's walk and T81's cost, feedback phase-locks the destruction rate and the return. History of the walk chooses the locked return. It does not produce a limit cycle or a torus on the locked grid.
