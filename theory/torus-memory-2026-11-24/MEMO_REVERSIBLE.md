# T82b: a closed reversible torus

*24 November 2026 (UTC). Self-check, not an independent review. Locked in `PREREG_REVERSIBLE.md`, sha256 `84b5cd7fb8c4e843ae1f54e837cdca1fec603c57916f6d1787716ca6cf0988dc`, commit `7994066`, before the orbits. `PREREG.md` and `PREREG_COUPLED.md` were not edited. In-model only. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

**In-model.** The flow keeps its starts apart, and the rotation number is the frequency ratio: periodic at \(3/2\), quasi-periodic at \(\sqrt{2}\) and at the golden conjugate. The return share still depends on the starting angle in every family. Five locked bars miss. The misses are puzzles.

## Scores

| Item | Score | Number | Where |
|---|---|---|---|
| I-rev, round trip | PASS | max error \(1.687539\times 10^{-14}\) | `reversible_torus_checks.out:3` |
| I-vol, Jacobian | PASS | det errors \(4.585443\times 10^{-12}\), \(7.960037\times 10^{-10}\) | `:4` |
| P1, distinct starts | PASS | separation \(0.785398\), action error \(0\) | `:5` |
| P2, \(q\) against the actions | FAIL | \(\sqrt{2}\) angle range \(0.261857\), action range \(0.005019\); golden \(0.100407\), \(0.024067\) | `:6-8` |
| P3, damping time | FAIL | \(G(0)=0.332754\); the gap never halves | `:9-22` |
| P4, rational against irrational | FAIL | ranges \(0.332754\), \(0.076988\), \(0.055431\); shifts \(0.058311\), \(0.043644\) | `:23-28` |
| P4-tongue | FAIL | no plateau on any of the four runs | `:36`, `:44`, `:52`, `:60-61` |
| P-kc, width against \(\varepsilon/\pi\) | FAIL | no width | `:62` |
| Beyond Kuramoto | PASS | `NOT_BEYOND` | `:64` |

FAILS 5 (`:65-66`). The T81 port matches the E-pair \(0.239059227845\) and \(0.048343059332\) (`:2`).

## What the memory is

At zero coupling the actions are constant. The 40 starts on the \(\sqrt{2}\) family stay at least \(2\pi/8\) apart (`PREREG_REVERSIBLE.md:87`, `:5`). That separation is the torus label: an action and a phase, still distinct at the end.

The rotation number sits on the frequency ratio to about \(10^{-14}\) (`:23-25`). All eight angles at \(3/2\) are `PERIODIC`. All eight at \(\sqrt{2}\) and at \((\sqrt{5}-1)/2\) are `QUASIPERIODIC` (`PREREG_REVERSIBLE.md:95-96`). A rational ratio is a closed orbit. An irrational ratio winds. The golden conjugate moves less under the coupling \(\varepsilon=0.05\): the shift is \(0.043644\) against \(0.058311\) at \(3/2\) (`:26-27`, `PREREG_REVERSIBLE.md:98`).

The return share reads the starting angle. At zero action its range is \(0.332754\) on the rational orbit, \(0.076988\) on \(\sqrt{2}\), and \(0.055431\) on the golden conjugate (`:23-25`). The rational bar, above \(0.05\), holds. The golden range is the smaller of the two irrational ranges. The \(\sqrt{2}\) bar, below \(0.02\), misses, and that one miss fails P4. Across the action grid the angle ranges are larger still, \(0.261857\) and \(0.100407\) (`:6-7`). About fifteen Poincaré samples do not yet average the angle away. History is visible in \(q\) on every family, and it is largest on the resonant orbit.

**P4, one line.** The classes and the smaller golden shift hold; the miss is the \(\sqrt{2}\) angle range \(0.076988\) against the \(0.02\) bar. The puzzle is that an irrational orbit at this horizon still keeps a record of the start in \(q\).

The value of the action is a weak coordinate of \(q\). On \(\sqrt{2}\) the angle-averaged share moves by \(0.005019\), under the \(0.02\) bar. On the golden conjugate it moves by \(0.024067\). Neither curve is as smooth as the lock asked (`PREREG_REVERSIBLE.md:89`).

**P2, one line.** At this sample length \(q\) still changes with the starting angle (\(\sqrt{2}\) range \(0.261857\)) and barely changes with the action (range \(0.005019\)). The puzzle is that \(q\) is not a smooth coordinate of the torus label.

## Damping and locking

\(G\) at \(\gamma=0.02\) equals \(G\) at \(\gamma=0.05\) at every listed time (`:10-20`). The start is \(I=0\) and \(\varepsilon=0\), so \(I\leftarrow I e^{-\gamma h}\) stays at zero and the angles are untouched (`PREREG_REVERSIBLE.md:91`, `:43-45`). The smallest gap on the list is \(0.193568\) at \(t=40\), still above half of \(0.332754\). There is no half-time. This tree has no T84 result to import (`ARCHAEOLOGY.md`).

The detuning grid has no run of three rotation numbers within \(10^{-3}\) of \(3/2\). With \(\varepsilon=0\) the rotation number is the detuned ratio exactly (`:29-35`). With \(\varepsilon=0.05\) it follows the detuning, shifted upward, and damping pulls it back toward that line without pinning it (`:37-59`). At \(\delta=0\), \(\gamma=0.05\), \(\nu=1.508071\). No width, so there is nothing to compare with \(\varepsilon/\pi\), and the three beyond-Kuramoto conditions do not hold (`theory/TORUS.md:17`).

**P-kc, one line.** There is no plateau, so there is no width beside \(\varepsilon/\pi\). The puzzle is that coupling plus action damping on this grid does not mode-lock, and the circle-map comparison does not get a number.

A probe beside the locked P3 fail, not a new score: at \(I_1=0.4\), \(I_2=0\), \(\varepsilon=0\), the action decays to \(0.054134113295\) at \(\gamma=0.02\) and to \(0.002695178800\) at \(\gamma=0.05\), matching \(0.4\exp(-\gamma\cdot 100)\), while \(\theta_2\) stays \(150.30000000000004\) because \(q\) reads \(\theta_2\) (`DEVIATIONS.md`). The identical series at \(I=0\) are the locked experiment.

## Prior work and Lean

`ARCHAEOLOGY.md` records the earlier claims. `theory/TORUS.md:16-20` already states that a rational ratio closes and a badly approximable torus is the last to break, and the circle-map tongue width was checked there. LOCK1 already failed the claim that a cost minimum selects the golden mean (`tests/LOCK1/RESULTS.md:9-18`). This run does not rescore either.

`formal/lean/` has no torus, rotation-number, or KAM lemma. The class split above is a numerical instance of one natural target: a constant-frequency flow on \(T^2\) is periodic exactly when the frequency ratio is rational. Two others are already named in the archaeology and are not formalized: the rank of a frequency vector over \(\mathbb{Q}\), and the 0:1 tongue width \(K/\pi\).

The names "revival" and "filling" are this same split (`PREREG_REVERSIBLE.md:107-109`). The classifier matches it. The return share on the irrational orbits still depends on the angle, so the share is a coarse record of the start at this horizon. This tree has no T83 note and no Talbot carpet.

## Contrast: the coupled map forgets

The width-9 gap between the two coupled-loop starts is \(0.179470489880\) at \(T=415\) and \(0.000896617534\) at \(T=10000\) (review comment 7144237250; recomputed with the locked step). In that dissipative menu the history is a transient. The reversible score is the contrast: at zero coupling and zero damping the actions stay at their starts (`reversible_torus_checks.out:5`) and the return share still depends on the angle at the locked horizon (`:23-25`). Whether that dependence survives a long walk horizon is locked separately in `PREREG_HORIZON.md` and is not a rescore of these lines.
