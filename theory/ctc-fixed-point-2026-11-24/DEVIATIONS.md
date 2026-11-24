# T85 deviations

Append only. The preregistration was not edited.

No deviation has been appended. `ctc_fixed_point_checks.out:18` reports `FAILS 0`. The bars in `PREREG.md` were not moved.

## Appended 2026-11-24 after the independent review

The paragraph above is the score-commit record. It stays. This section is the later add. `PREREG.md` is still unedited. Lock `forge-ctc-fixed-point` `f18721fc852f83a6154aa50186cbbdb876fe0ad9`, scored at `3e1fcf9e0e4ac1aecb05a76306c675883b3f6d45`. Logged at 2026-11-24 16:54 ET. Breach check: none.

The ten locked bars hit. P1a, P2-bound, P3-phase, P3-contraction, and P4-cycle are **NOT A TEST** / consistency checks, as in the review. The route A identification is a miss. It was not a locked numeric bar.

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| P1a | \(\lvert\Delta S(\rho_{CTC})\rvert\le 10^{-9}\) on the accepted list; 0 rejections. No odds locked | max \(5.551\times 10^{-16}\); \(n=149\); rejections 0 | HIT, residual \(+5.551\times 10^{-16}\) inside the band. **NOT A TEST** / consistency check of the fixed-point definition | model | low | none yet | none |
| P1b-named | non-unique \(\{I,\mathrm{CNOT}_{CR},\mathrm{CNOT}_C,\mathrm{CZ},\mathrm{DISC}\}\); unique \(\{\mathrm{SWAP},\mathrm{DCNOT}\}\) at \(I/2\). No odds locked | that split (`out:4`) | HIT. The split could have missed. It is not an identity | model | low | none yet | none |
| P1b-grid | exactly 20/64; non-unique singular value \(<10^{-8}\); unique \(>0.2\). No odds locked | 20/64; non-unique max \(5.551\times 10^{-16}\); unique min \(0.292893218813=1-1/\sqrt{2}\) | HIT. Margin of the unique floor above 0.2 is \(+0.092893218813\). Exact on the locked angle set. The count moves when the angle set moves | model | medium | note appended in `MEMO.md`; the locked count was not moved | none |
| P2-bound | \(\Delta S(\rho_{CR})\ge -10^{-9}\) on the accepted list. No odds locked | minimum 0 (`out:8`) | HIT. The minimum sits on 0, \(+10^{-9}\) above the floor. **NOT A TEST** / consistency check of unitarity, a product input, subadditivity, and the fixed point | model | low | none yet | none |
| P2-illicit | mixture difference \(-\ln 2\) within \(10^{-9}\); selector change \(+\ln 2\) within \(10^{-9}\); not one process. No odds locked | \(-0.693147180560\) and \(+0.693147180560\) (`out:10`) | HIT, residual 0 at twelve digits. The mixture is outside the product fixed-point equation | model | medium | none yet. Scope already marked `not-a-process` | none |
| P3-gap | unique \(I/2\); gap \(h((2+\sqrt{2})/4)\) within \(10^{-8}\) and \(>0.1\); \(I=\ln 2-h(3/4)\) within \(10^{-8}\); five \(\gamma\). No odds locked | \(0.416495530700\) and \(0.130812035941\) at all five \(\gamma\) (`out:11`) | HIT. Margin above 0.1 is \(+0.316495530700\). Flatness in \(\gamma\) is **NOT A TEST**. The value of the gap could have missed | model | medium | none yet | none |
| P3-phase | both pure points fixed within trace distance \(10^{-9}\); gap 0 within \(10^{-9}\). No odds locked | distances 0 and \(1.110\times 10^{-16}\); gap \(1.110\times 10^{-16}\) (`out:13`) | HIT. **NOT A TEST** / consistency check of the locked columns and of phase damping on a diagonal state | model | low | none yet | none |
| P3-contraction | nullity at least 1 at \(\gamma=0\); nullity 0 at \(\gamma=10^{-6}\). No odds locked | 1, then 0 (`out:14`) | HIT. **NOT A TEST** of the contraction. The small singular value equals the depolarizing strength | model | low | none yet | none |
| P4-cycle | absolute energy sum, net learning, and trace distance each \(\le 10^{-12}\). No odds locked | 0, 0, 0 (`out:15`) | HIT. **NOT A TEST** / consistency check that CNOT twice and SWAP twice are the identity. The CTC qubit is not in the circuit | model | low | none yet | none |
| P4-half | open-prefix sum \(-1/2\) within \(10^{-12}\). No odds locked | \(-1/2\) (`out:16`) | HIT, residual 0. The sign is \(H_B=Z/2\) with \(\lvert 0\rangle\) the excited state | model | low | none yet | none |
| route-A-id | prose claim that the scored gap is route A's same-channel gap and is not undercut. Not a locked numeric bar. The route A minimized slope is 0. No odds locked | one-design slope \(0.416495530700\) | miss \(+0.416495530700\) nats per unit \(\kappa_D\), against slope 0 | model | high | identification withdrawn below the original sentences in `MEMO.md`, in the T85 row of `OPEN_WORK.md`, and in `theory/README.md`. `PREREG.md` not edited | none |

### P1b-grid

The locked prediction is 20 non-unique gates out of 64, cutoff \(10^{-8}\), unique singular value above 0.2. The outcome is 20/64, and the smallest unique singular value is \(1-1/\sqrt{2}\). The count is exact on \(\{0,\pi/4,\pi/2,\pi\}^3\). It is not a property of every angle set: the same cutoff gives 10, 20, 10, and 10 on the four other four-angle grids named in the memo. Update: that note. The bar stays.

### P2-illicit

The locked numbers are \(-\ln 2\) for the label-dependent mixture and \(+\ln 2\) for the maximum-entropy selector on each input. Both hit at twelve digits. Each pure branch has entropy change 0. The negative number is \(S(\mathbb{E}\rho')-S(\mathbb{E}\rho)\) for a CTC state that depends on a classical label. The product fixed-point equation does not contain that preparation. No update.

### P3-gap

The locked gap is the binary entropy \(h((2+\sqrt{2})/4)\) and the mutual information is \(\ln 2-h(3/4)\), at five depolarizing strengths, and the gap is above 0.1. Both closed forms hit. Independence of \(\gamma\) follows from \(r=0\) being the only solution of the contraction for \(\gamma>0\), so that flatness is a consistency check. The numerical value is the part that could have missed. No update.

### route-A-id

The withdrawn sentence said the scored gap is route A's gap \(\kappa_D P_D\) and is not undercut. Route A `:103` subtracts two designs of one classical channel. Route A `:116` says the minimized cost of that channel has slope 0 in \(\kappa_D\). The score is one DISC design, slope \(0.416495530700\). The difference of the slopes is the miss \(+0.416495530700\). Location `model`: the two objects are different, not a swapped sign in a printout. Update: the identification is withdrawn in the places named in the ledger. The ten locked bars stay. The negative statement that remains is narrower: \(\Delta S(\rho_{CTC})=0\) is not the reverse leg route A says is missing, and this score does not recompute `:103`.
