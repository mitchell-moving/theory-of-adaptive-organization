# Independent review of the horizon scan and the resonance scan

*24 November 2026, 16:35 ET. Head `46f8bdc51debcbb05db6e08bbc378abc67c2eda5` on `forge-torus-memory`. This review is a new branch, `forge-resonance-review`. It does not edit that branch, `THEORY.md`, or `CORE.md`. Wording follows `process/PROCESS.md` and `process/MISS_LOG_TEMPLATE.md` at upstream `652d936`. Historical memos, locked preregistrations, run logs, and deviation paragraphs are not rewritten.*

**Lock reference:** horizon `af44b86`, sha256 `abb56169340490e2a420d47f5c0cb556e90e86caf720a2a86d5423a4c5ee85d9`; resonance `c496962`, sha256 `3a37da80f100480efa7442a372fc94aa449541ea4b04b39a8b03ec0db5ad4a39`.

**Breach check:** none. Both preregistration blobs are identical from the locking commit through `46f8bdc`. Each file is touched by one commit. The score commits do not edit them. No locked number was patched after the run.

## Checks

| Check | Result |
|---|---|
| Resonance lock before score | `c496962` (2026-11-24 21:04:11Z) is an ancestor of `46f8bdc` (21:10:03Z). The lock commit adds the preregistration, the sidecar, a run-log stub, and one appended deviations paragraph. |
| Horizon lock before score | `af44b86` (2026-11-24 20:55:39Z) is an ancestor of `cee6440` (21:07:03Z) and of `46f8bdc`. |
| Sidecars | Both sha256 files match the blobs at the lock and at the head. |
| Re-run | `resonance_checks.py` and `horizon_checks.py` reprint the committed `.out` files with no diff. |
| Independent recomputation | `theory/reviews/REVIEW_RESONANCE_checks/attack.py`, output `attack.out`. It does not import the score scripts. |
| `python3 tools/check_consistency.py` | Exit 0. Wording count on maintained docs is 0. `RESULT: PASS`. |
| `python3 -m pytest -q` | 295 passed, 1 skipped, exit 0, 645 s. |
| Crossref, this review, DOI `10.1007/978-3-642-01742-1_10` | Title "Small denominators. I. Mapping of the circumference onto itself." Author field empty. Container Collected Works. Pages 152–223. Issued 2009. Same record as `PREREG.md:75` and the deviations paragraph. No author was added. |

The run logs still open with the sentence that the scored script has not been run, and the score sentence is appended under it. `DEVIATIONS.md` grows only by added paragraphs. Every scored miss on the two scoreboards is named in the matching run log. Those lines are prose, not the eight-field ledger. That is a template gap for the next append, not a reason to rewrite the lines that are already there.

## Eight-field ledger

No preregistration in this packet names MV1–MV8. A recomputation of the locked map matches the printed islands, the port levels, and the fine-gain periods. The width floor is the menu the lock wrote down. It is not a disagreement between the code and the lock. Under `process/PROCESS.md` item 6, a `measurement/code` location is therefore not admissible for these rows, including the width floor. Every row below is `model`. Odds were not locked.

Signed size is outcome minus the locked value. A hit records the margin to the locked bar.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT plus margin) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T82d-P-port | Stake 2: \(T=415\) period 1 at \(0.246706007043\); \(T=500\) period 2 at \(0.288952\) and \(0.291620\) within \(5\times 10^{-7}\); \(T=831\) period 1 at \(0.422916079022\); \(T=550\) rate 6 and return \(0.313065981732\). Odds not locked. | Recomputed: periods 1, 2, 1; levels \(0.288951536270\), \(0.291620058685\); means \(0.246706007043\) and \(0.422916079022\); \(T=550\) return \(0.313065981732\). | HIT. Level residuals \(-4.64\times 10^{-7}\) and \(+5.87\times 10^{-8}\), inside the band. | model | low | none yet | none |
| T82d-P-band | One period-2 plateau, length at least 3, containing 500, and no other period-2 horizon. Odds not locked. | Four blocks: 500–505, 555–558, 613–615, 674. | \(+3\) blocks. | model | high | none yet. Do not retarget a clock. The blocks are the four menu boundaries below. | none |
| T82d-P-where | That one plateau lies strictly between 415 and 831. Odds not locked. | No single plateau. All four blocks lie in \((415,831)\). | Placement residual 0. The item misses because the unique plateau is absent (\(+3\) blocks). | model | medium | none yet | none |
| T82d-P-align | The one center \(C\) satisfies \(\lvert C/(r\tau)-1\rvert>0.05\) for every \(r\) in \(\{1/2,1,5/4,4/3,3/2,2\}\). \(\tau=1/\sin^2(\pi/64)\). Odds not locked. | No unique \(C\). Recomputed \(\tau=415.345062231902\). | The locked residual is the missing center (\(+3\) blocks). The post-score ratio residuals are in Attacks tried; they are not this row's locked residual. | model | high | none yet. The 5 percent reading does not clear the chance baseline below. | none |
| T82d-P-stair | Every horizon at stake 2 has period 1 or 2. Odds not locked. | Period above 2: 0 horizons, on the recomputed scan and on the re-run. | HIT. Count residual 0. | model | low | none yet | none |
| T82d-P-single | Each of stakes 1, 2, 4 has at most one period-2 block. Odds not locked. | Stakes 1 and 4 have 0. Stake 2 has 4. | Stake 2: \(+3\) blocks. Stakes 1 and 4: HIT, count 0. | model | medium | none yet | none |
| T82d-P-gain-interior | \(N(1.5,1.5)-N(0.5,0.5)\le 2\). Odds not locked. | Scoreboard re-run: 184 and 148. | HIT. Signed difference \(-36\), which is 38 under the cap of \(+2\). The interior set shrinks. | model | medium | none yet | none |
| T82d-P-gain-differ | Horizons whose period changes between gains \((0.5,0.5)\) and \((1.5,1.5)\): at most 2. Odds not locked. | Scoreboard re-run: 51. | \(+49\) horizons. | model | high | none yet. See the gain section: the period changes on a contraction. | none |
| T82d-P-gain-fine | The seven equal gains at \(T=500\) share one period. Odds not locked. | Recomputed periods 16, 9, 12, 4, 3, 3, 5. | \(+6\) gains differ from the first. | model | high | none yet | none |
| T82d-P-null | Six runs are period 1: \(T=500\), \(T=550\), and the integer nearest the unique center, each on 181 and 2881 angles, with the floor removed. Odds not locked. | The four named runs are period 1. There is no unique center, so two runs are not executed. | \(-2\) runs not executed. The four executed runs have period residual 0. | model | high | none yet. The floor comparison is the locked null, not a code bug. | none |
| T82c-P-port | \(T=500\) is a period-2 cycle at those levels, step \(2.668522\times 10^{-3}\), widths 7 and 8. Odds not locked. | Re-run and recomputation agree: levels \(0.288951536270\), \(0.291620058685\); widths 7 and 8. | HIT. Same level residuals as T82d-P-port. | model | low | none yet | none |
| T82c-P-res | One period-2 block containing 500, length at most 207, with a stopped horizon on each side. Odds not locked. | Re-run: 4 blocks, 14 cycle horizons, 401 point, 0 set. Longest block length 6. | \(+3\) blocks. The length cap is not crossed (6 versus 207). | model | medium | none yet | none |
| T82c-H-label | End separation at least half the start separation. Odds not locked. | Re-run ratio \(1\). | HIT. Margin \(+0.5\) above the bar of \(1/2\). | model | low | none yet | none |
| T82c-H-flow | For each family, the smallest gap on \(t=20,\ldots,100\) is at least half the largest, and the rational gap stays at least the \(\sqrt{2}\) gap. Odds not locked. | Re-run. Rational smallest \(0.193568186357\) is above half of \(0.332754439250\). \(\sqrt{2}\) smallest \(0.047911800530\). Golden smallest \(0.055431257067\). | \(\sqrt{2}\): \(-0.066878241365\) against half of its maximum. Golden: below its own half as well. Rational clause: HIT. | model | medium | none yet | none |
| T82c-H-walk | At \(T=83069\), each family keeps at least half of its \(T=415\) gap. Odds not locked. | Re-run: both gaps are 0. | Rational \(-0.145933501381\). \(\sqrt{2}\) \(-0.042608989184\). | model | medium | none yet | none |
| T82c-H-gamma | A sample on the locked grid reaches half of \(G_0=0.076988268821\), and the half-time sits in the locked window of \(\ln 2/\gamma\). Odds not locked. | Re-run: no sample reaches the half. Last values \(0.078924958230\) and \(0.064446909176\). | \(+0.040430823820\) and \(+0.025952774766\) above the half line. The gap stays larger than the locked half. | model | medium | none yet | none |

## Can these rows use the ledger

Yes, with two empty cells the locks themselves left empty. The value, the outcome, the signed residual, the location, the stake, the update, and the breach check can all be filled, as above. The odds cell is "not locked" on every row: neither preregistration states a rival probability or an MV10 power. That does not block the ledger. It means a hit here is a reproduction or an in-model clause, and its information is the margin to the bar, not a surprise against a stated prior.

The location cell cannot honestly be switched to `measurement/code` for the width floor. Two conditions would allow that, and neither holds.

- A pre-declared MV1–MV8 gate fired. No preregistration in `theory/torus-memory-2026-11-24/` names an MV gate. Nothing in that set fired.
- A reproducible bug: the code does something other than the lock. The independent scan reproduces the four islands, the port levels to the printed digits, the stake split, and the seven fine-gain periods. The floor formula is the one the resonance preregistration writes down.

The period-1 map with the floor removed is the locked null, item T82d-P-null. Its executed runs hit. The item misses because the unique center the lock also required is absent. Recording that as an instrument bug would be the relocation the admissibility rule bars.

## Attacks tried

Independent code: `theory/reviews/REVIEW_RESONANCE_checks/attack.py`. The walk is the lazy step (stay \(1/2\), neighbors \(1/4\), the near end absorbed, \(c=1\)). The angle cost is the closed form at `f625bb7`. The menu is \(1+\lfloor 8 P_D(\theta^\star)/P_D(\pi/2)\rfloor\) on the angle grid, with ties averaged, which is the locked floor.

### (a) Ratio match against chance

Recomputed centers of the blocks of length at least 1, and of the three plateaus of length at least 3:

| Block | Center | Nearest locked ratio | Signed \((C/(r\tau)-1)\) |
|---|---|---|---|
| 500–505 | 502.5 | \(5/4\) | \(-0.032130\) |
| 555–558 | 556.5 | \(4/3\) | \(+0.004887\) |
| 613–615 | 614 | \(3/2\) | \(-0.014474\) |
| 674 | 674 | \(3/2\) on the locked list; \(5/3\) on all \(p/q\) with \(q\le 4\) | \(+0.081831\) against \(3/2\); \(-0.026352\) against \(5/3\) |

The memo's three residuals match. Two further comparisons the memo does not use also match the arithmetic: the first center is closer to \(6/5\) once \(q\le 5\) is allowed (signed \(+0.008198\)), and the length-1 horizon 674 lies inside 5 percent of \(5/3\).

Chance model, as asked: three independent centers uniform on \([416,830]\), length 414. The family is every \(p/q\) with \(1\le q\le 4\) whose 5 percent window meets that interval. The targets are \(1\), \(5/4\), \(4/3\), \(3/2\), \(5/3\), \(7/4\), and \(2\), times \(\tau\).

The 5 percent windows cover fraction \(0.765909\) of the interval. The probability that all three centers land within 5 percent of some such ratio is \(0.765909^3=0.449\). On the integer grid 416 through 830 the same fraction is \(319/415=0.769\). A 5 percent match to some simple ratio is the usual case, not a rare one.

Using the three observed absolute residuals \(0.004887\), \(0.014474\), and \(0.032130\) as the tolerances, and asking that the ordered nearest-ratio gaps of three random centers are at most those three numbers, the probability is \(0.0442\). About one draw in 23. If the three ratios had been locked in advance for three named centers, the product of the three specific windows would be \(4.59\times 10^{-5}\). The look-elsewhere factor, from that product up to the ordered-gap probability, is about \(10^3\). The post-score reading searched the family and then kept the nearest hit.

Shifting the floor, which the next section does, moves the centers and they still fall near the same comb. At floor offset \(0.75\) the first center is 521, signed \(+0.003503\) from \(5/4\,\tau\), closer than the locked floor's \(-0.032130\). At offset \(0.50\) the horizon 691 is signed \(-0.001794\) from \(5/3\,\tau\). The comb is dense relative to a 5 percent bar. Landing on it does not identify \(5/4\), \(4/3\), and \(3/2\).

### (b) Floor values and angle grids

The integer menu has five distinct blocks, not nine widths. Widths 2 and 3 share sites 15–17, widths 4 and 5 share 14–18, widths 6 and 7 share 13–19, and widths 8 and 9 share 12–20. Width 1 is site 16 alone. A 2-cycle needs two widths with different returns. The recomputed cycles use exactly the four boundaries between those five blocks:

| Horizons | Widths in the cycle | Coupled mean rate at gain \((1,1)\) |
|---|---|---|
| 500–505 | 8 and 7 | 7.5, period 4 |
| 555–558 | 6 and 5 | 5.5, period 4 |
| 613–615 | 4 and 3 | 3.5, period 4 |
| 674 | 2 and 1 | 1.5, period 4 |

Same-site pairs do not cycle, because they return the same number.

Floor offset is the constant added inside the floor, with span 8 held fixed. Each offset moves all four islands.

| Offset | Period-2 blocks at stake 2 |
|---|---|
| 0 (locked) | 500–505, 555–558, 613–615, 674 |
| 0.25 | 507–511, 562–565, 621–622, 682–683 |
| 0.50, and rounding to the nearest integer | 512–516, 568–571, 626–628, 691 |
| 0.75 | 519–523, 575–578, 634–636, 698–699 |
| span 4, offset 0 | 534–535, 644 |
| span 16, offset 0 | 590–595, 622–625, 657–659, 691 |

With the floor removed, the 181-point grid has no plateau. It has ten length-1 period-2 horizons: 501, 505, 508, 511, 514, 522, 529, 569, 571, 573. \(T=500\) and \(T=550\) are period 1, which is the executed half of T82d-P-null. A full scan at 361 angles, and probe scans at 721, 1441, and 2881 angles, show no period-2 horizon once the floor is removed.

With the floor kept, finer grids do not remove the islands. At 2881 angles the probe still has 500–505, 555–558, 613–615, and 675. Edges move by at most one horizon. The plateaus are the integer menu. They are not the coarseness of the 181-point angle grid.

### (c) Gain and the period list 16, 9, 12, 4, 3, 3, 5

At \(T=500\) the seven equal gains recompute to those periods on all three initial conditions. The tail closes with error 0, or at most \(2\times 10^{-15}\) at gain 1.5. The largest step inside the tail is \(0.25\) to \(3.87\), so the detector is not promoting a slow drift. These are closed orbits of the piecewise-linear lag map.

Inside a cell where the target width is constant, the coupled step has Jacobian eigenvalues \(1-\alpha\) and \(1-\beta\). For a gain in \((0,2)\) both have absolute value below 1. At gain \(0.25\), two starts separated by \(10^{-6}\) in \(q\) give a 40-step exponent \(-0.2877\), against \(\log 0.75=-0.287682\). At the other six fine gains the separation has collapsed by step 40. The exponent is negative. This is not sensitive dependence on initial conditions.

A gain grid from \(0.05\) to \(1.95\) at \(T=500\), one start, is mostly short: many periods last one step of \(0.05\). The long flat piece is period 3 from gain \(1.15\) to \(1.70\). The sequence is not a period-doubling cascade, and it is not monotone (the locked list jumps from 9 to 12). Across horizons, gain \(1\) puts period 4 on 6, 4, and 3 horizons in the windows around 500, 556, and 614. Gain \(1.5\) puts period 3 on 9, 7, and 5 horizons in those same windows. The non-fixed set changes its period as the gain rises. An Arnold tongue would hold one rotation number and widen. This map changes the period. The interior-count clause already hit in the direction of a smaller interior set, not a wider one.

What the gain scan supports: the lag map is a contraction onto a cycle whose length is set by how large a step is taken toward the two-width menu. What it does not support: chaos, or a tongue of fixed rotation number.

### (d) Classical and dissipative structure

The resonance preregistration defines the rotation number as \(0\) at period 1 and \(1/p\) at period \(p\). That is a label of the discrete period. It is not the frequency ratio of a Hamiltonian flow. The coupled step is a linear relaxation toward the menu. On \((0,2)\) it damps. T82d is not a conservative torus, and the memo already says it does not estimate \(K_c\).

The formula \(\tau=1/\sin^2(\pi/64)\) recomputes as \(415.345062231902\). The largest-magnitude eigenvalue of the same 32-site lazy step is \(0.999416113416\). One over one minus that eigenvalue is \(1712.66\), not \(415.35\). This review does not assign the formula a derivation beyond the lock. It does record that the formula is not the decay constant of this walk. Rational multiples of it are not revival times of this step. The lock predicted that the single center would sit off those multiples. The score misses for lack of one center. The later reading, that three centers line up with \(5/4\), \(4/3\), and \(3/2\), is the commensurability step, and section (a) is why it does not support an update.

### The P3 note in `DEVIATIONS.md`

The historical paragraph is kept. The mechanism it states recomputes, and one printed angle does not, from the inputs the paragraph lists.

The separable step multiplies the action by \(e^{-\gamma h}\) after the kick when \(\gamma\neq 0\). At \(I=(0,0)\), \(\varepsilon=0\), and \(\omega=(1,3/2)\), the angles at \(\gamma=0\), \(0.02\), and \(0.05\) differ by 0. The action stays 0. A probe at \(I_1=0.4\), \(I_2=0\), \(\varepsilon=0\), \(n=2000\), \(h=0.05\), \(\theta(0)=(0,0)\) gives \(I_1=0.054134113295\) at \(\gamma=0.02\) (gap to \(0.4 e^{-2}\) of \(+3.2\times 10^{-15}\)) and \(I_1=0.002695178800\) at \(\gamma=0.05\) (gap \(-2.0\times 10^{-16}\)). Both sit inside the stated \(4\times 10^{-15}\). \(\theta_2\) is \(150.00000000000009\), not \(150.30000000000004\).

The printed angle is what the same step returns from \(\theta_2(0)=0.3\). That start is not stated in the note, and it is not one of the eight locked angles \(2\pi k/8\). The score script does not print the digit. This is not a bug in the scored orbit. It is an incomplete probe record. Stake is low. Update: append the reproduced value; do not rewrite the paragraph; do not open a corrected scoreboard.

### `ARCHAEOLOGY.md` against the files

The header dates the search to the tree at `e03b5f0`. Checked against the files, not against the prose summary alone:

- `theory/TORUS.md:16-20` says an irrational ratio fills \(T^2\), a rational ratio closes, the 0:1 tongue has width \(K/\pi\), and badly approximable tori survive as textbook. `circle_map.out` has widths \(0.0798\), \(0.1593\), \(0.2387\), \(0.3182\).
- `theory/TORUS.md:45-51` is the N45 plateau claim, and `:53-66` is the N49 price map, including continuity when \(\lvert\mu\rvert\le\sigma\).
- `independent_review_checks.out` has local exponents \(1.99\), \(1.95\) and \(2.92\), \(2.90\). "About 2" and "about 3" matches that file.
- `theory/THEOREMS.md:215` labels the link an untested analogy. `:218-219` is the dense winding and the Diophantine survival sentence.
- `tests/LOCK1/RESULTS.md:9-18` includes the B3 miss and the statement that the golden mean is not selected. The fuller citation `:3-18` also includes B1. `reviews/shannon_2026-11-21/REVIEW.md:227` is the B2 row.
- `PREREG.md:57` names the pairs \((1,\sqrt{2})\) and \((1,3/2)\). `:75` is the 2009 reprint, and the Crossref query above matches it. `:89-101` is P2 through P6.
- `formal/lean/` has 23 `.lean` files. The only `quasi` hits are `CT22.lean:29` and `Equipartition.lean:190`. No lean file in that tree names a torus, a rotation number, or KAM.
- A search of the tree at `e03b5f0` finds no file containing T83, T84, or Talbot. The Berry hits there are Palmer, Marre, Berry, and Bialek 2015.

Two limits, both small, both left in the historical file:

- `theory/theorems-checks/check_all.py:206` says the identical-frequency flow collapses to a point. The archaeology sentence adds "or a cycle," which that line does not say.
- `PREREG_COUPLED.md:77-84` is the rotation-number branch. The fixed-point clause is line 74 and the period search is line 76. The claim about the classifier is in the section; the cited range starts at the rotation clause.
- On this clone, `git log --all --grep=T83` is not empty. The commits are on `forge-revival-phase-storage`, `forge-revival-review`, and `forge-dephasing-crossover`. They are not ancestors of `e03b5f0`. The file-level claim about that tree holds. The sentence that the full ref list is empty does not hold on this clone, and later files on this branch name T84 as an absence. Do not rewrite the search note.

## What remains, and what does not support an update

Remains, as model facts on the locked menu:

- Stake 2 has four period-2 islands, 500–505, 555–558, 613–615, and 674. Stakes 1 and 4 have none. No horizon on the stake-2 scan has period above 2.
- Those islands are the four boundaries between the five distinct blocks. The coupled map at gain \((1,1)\) is period 4 there, with mean rates 7.5, 5.5, 3.5, and 1.5.
- The islands stay under finer angle grids and move when the floor offset or the menu span changes. Removing the floor removes the plateaus. From 361 angles upward it removes the leftover length-1 points as well.
- The gain changes the length of a contracting cycle. The interior count goes from 184 to 148. That clause hit. The period-count clauses miss, with signed sizes \(+49\) horizons and \(+6\) gains.

Does not support an update:

- Reading the three plateau centers as \(5/4\), \(4/3\), and \(3/2\) times the gap clock. Three random centers in \([416,830]\) fall within 5 percent of some \(p/q\) with \(q\le 4\) with probability \(0.449\). The tighter ordered-gap event has probability \(0.044\). The \(5/4\) label moves to \(6/5\) at the next denominator. The length-1 island is inside 5 percent of \(5/3\). Other floor offsets land even closer to the same comb.
- Reading the period list as chaos, or as an Arnold tongue. The orbits close, the separation exponent is negative and matches \(1-g\), and the period is not held fixed while a band widens.
- Reading \(\tau\) as the decay time of this walk. The eigenvalue gap is \(1712.66\), not \(415.35\).
- Putting the width floor in `measurement/code`. No MV gate was declared, and the code matches the lock.

The useful model statement is the smaller one: on this menu, period 2 is the chatter across a block boundary, and the boundaries move with the floor. That statement is already the content of the executed half of T82d-P-null. It does not need a new ratio.

## Note for the builder

Historical paragraphs stay. The next append, not a rewrite, should use the eight fields in `process/MISS_LOG_TEMPLATE.md`.

- `theory/torus-memory-2026-11-24/DEVIATIONS.md`. The next paragraph should be a ledger row, not another prose gloss. The low-stake row worth appending is the P3 angle: reproduced \(\theta_2(0)=0\) gives \(150.00000000000009\); the printed \(150.30000000000004\) is the unstated start \(0.3\). A second row, only if an update is actually made, would record the block-boundary reading of the four islands as `model`, with update "none to the lock or the scoreboard."
- `RUN_LOG_RESONANCE.md` and `RUN_LOG_HORIZON.md`. Future score lines should be ledger rows for every hit and every miss, including the hits that the present sentences only name in passing. Do not backfill the lines already there.
- Do not append a `measurement/code` location for the width floor unless a later lock declares an MV gate and that gate fires, or a later run shows the code leaving the lock.

Index of the checks above:

- Recomputed \(\tau\), the four islands, the plateau centers, and the signed residuals against \(5/4\), \(4/3\), and \(3/2\).
- Estimated the chance that three centers in \([416,830]\) land within those gaps of some \(p/q\) with \(q\le 4\), including the 5 percent coverage and the ordered-gap probability.
- Moved the floor offset, the menu span, and the angle-grid size, and removed the floor.
- Recomputed the seven fine-gain periods, the closure error, the separation exponent, and the period-versus-gain runs at \(T=500\).
- Compared \(\tau\) with the largest eigenvalue of the lazy step.
- Re-ran the P3 probe from the stated inputs and from the unstated angle that prints the logged digit.
- Checked the archaeology citations, the lean tree, the T83/T84 refs on this clone, and the one DOI on Crossref.
- Re-ran both score scripts and `tools/check_consistency.py`.

Blockers remaining: 0
