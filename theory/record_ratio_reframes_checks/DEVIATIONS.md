# Deviations

`PREREG.md` and `PREREG.sha256` are unchanged. No prediction, bar, stake list, or ensemble was edited after the run.

## D1. Post-hoc window, not a rescore

The locked run is `record_ratio_reframes_checks.out` (FAILS 4). C1 returned no interior stake and C2 returned one. After that output existed, `posthoc_windows.py` was written to locate the stake band those lists skipped and to repeat the locked inversion inside that band only. Its stdout is `posthoc_windows.out`. It does not change FAILS. It does not replace C1 or C2. The stakes `{0.2, 0.3}` named in `PREREG.md` as the next C1 step were evaluated there and left at the corner; they were not added to the locked list.

## D2. How G5 was scored

`PREREG.md` G5 says the minimized costs differ by \(P_\chi(0)\) within \(10^{-9}\), and the same sentence's parenthesis says the difference is the added coefficient times the constant ledger. Those two descriptions are not the same number. The locked check uses the symbol \(P_\chi(0)\). The parenthesis is printed as `DIAGNOSTIC` and is not a locked check. The sentence was not rewritten.

## D3. Post-hoc readout of the repeated-record miss, not a rescore

`PREREG_REPEAT_ASYMPTOTE.md` is unchanged. The locked run is `repeat_asymptote_checks.out` (FAILS 2). R-low and R-high miss. After that output existed, `repeated` was evaluated at \(n=256\) on \(\theta=0\), \(\pi/4\), \(\pi/2\), and on the two reported minimizers \(1.468258\) and \(1.005746\), to see which term carries the cost. This readout does not change FAILS and does not replace R-low or R-high.

At \(\theta=0\), \(I=1.039720\) and \(L=0\). At \(\pi/4\), \(I=1.038833\) and \(L=0.000085\). At \(\pi/2\), \(I=0\) and \(L=0.180000\). At \(1.468258\), \(I=0.196942\) and \(L=0.120771\). At \(1.005746\), \(I=1.022569\) and \(L=0.001689\). With \(q=0\), the \(w=4\) minimizer costs \(0.680025\), against \(0.720000\) at the equator and \(1.039720\) at the pointer. The \(w=10\) minimizer costs \(1.039458\), against \(1.039720\) at the pointer.

## D4. Q-coh used the dephased diagonal, not the named projectors

`PREREG_QUANTUM.md` is unchanged. The coherent block is the review instrument, projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\), on the state with off-diagonal \(1/8\) inside that block. Those projectors fix the state, so \(P_D=0\) and the costs at \(q=0\) and \(q=1\) agree. The prediction \(P_D>0.01\) fails.

The run stored at `00e8dfa` did not apply those projectors. It subtracted the entropy of eigenvalues \((1/2,1/4,1/4)\) from the entropy of \((1/2,3/8,1/8)\) and printed `Q-coh PASS PD=0.065406 cost_gap=0.065406`, with `FAILS 1`. That number is the gap to the fully dephased diagonal. It is not the disturbance of the locked instrument. This commit replaces `quantum_record_checks.out`. The corrected line is `Q-coh FAIL PD=0.000000 cost_gap=0.000000`, and the file ends `FAILS 2`. No prediction was edited.

## D5. Original Q-coh run log restored and appended, 24 November 2026

`PREREG_QUANTUM.md` is unchanged. D4 records that commit `9284624` replaced `quantum_record_checks.out` with the re-scored line. The original nine lines from `00e8dfa`, including `Q-coh PASS PD=0.065406 cost_gap=0.065406` and `FAILS 1`, are now restored at the top of that file and are not edited. The re-score `Q-coh FAIL PD=0.000000 cost_gap=0.000000` and `FAILS 2` is appended below a dated note, 24 November 2026 (America/New_York). The live script stdout is the appended block. No prediction was edited.

## D6. D4 names the old subtraction in the reverse order

`PREREG_QUANTUM.md` is unchanged. D4 and D5 are left as written. The return stored at `00e8dfa` is the dephased entropy minus the coherent-state entropy, \(S(1/2,1/4,1/4)-S(1/2,3/8,1/8)=+0.065406\). D4 says that run subtracted the entropy of \((1/2,1/4,1/4)\) from the entropy of \((1/2,3/8,1/8)\), which is the negative of that difference. The printed gap is still the gap to the dephased diagonal, and the re-score remains \(P_D=0\). No prediction was edited.

## D7. K2 net minimum was overwritten by the least-squares residual

`PREREG.md` is unchanged. No prediction, bar, stake list, or ensemble was edited. The stored run `record_ratio_reframes_checks.out` lines 1–19 are unchanged. The corrected block is appended under the note dated 24 November 2026 (America/New_York).

The least-squares block wrote its residual into `net_min` whenever that residual was smaller than the grid minimum. The printed line `net_min=0.0004213774925606595 at=(1.0033319156709788, 0.6581687266183737)` is the least-squares point. It is not a point of the net \(\alpha,\beta\in\{-2,-1.95,\ldots,4\}\). The 121 by 121 minimum is `0.0014997828907532262` at `(1.0, 0.65)`. The script now prints those two numbers in separate fields. Both are below the locked bar `0.005`, so K2's bound clause still misses. The run remains `FAILS 4`.

The overwritten field is a measurement/code miss. The bound-clause miss is a model miss, and it is unchanged. The ledger below records both, and it records every other locked hit and miss on this branch.

## Ledger

**Lock reference:** `PREREG.md` sha256 `8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8`; `PREREG_FIXED_POINTS.md` sha256 `82d58bdcefca97218ac4b7587a9246850994eedac1c6c372de8f50a75417017b`; `PREREG_MHD.md` sha256 `faf04d3d53de980141cbfd57a3dfb30f34af6e6f8d7efb5ce72f5a01e3dc25b6`; `PREREG_REPEAT_ASYMPTOTE.md` sha256 `5b0846fa823e86d63c71133831ec966ac42f3f3a27f1cff9ec613c392adfa60a`; `PREREG_QUANTUM.md` sha256 `1ac92e314705b3378e3b6a1bd665d36ec6dc9f7f812760a20bc4556617b817d3`. None of these files was edited.
**Logged at (ET):** 2026-11-24 17:50 ET
**Breach check:** none

### Minimal ledger

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT + info) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| G0 | closed form of \(P_D\), \(I\), \(L\) within \(10^{-10}\) | max abs \(5.551\times 10^{-17}\) | HIT; margin \(10^{-10}-5.551\times 10^{-17}\) | model | low | none yet | none |
| G0b | \(\lvert P(M=+1)-1/2\rvert<10^{-12}\) on the grid | max abs \(5.551\times 10^{-17}\) | HIT; margin about \(10^{-12}\) | model | low | none yet | none |
| K1-ledger | \(\max\lvert I+P_D-\chi\rvert<10^{-9}\) on ANT | \(5.551\times 10^{-17}\) | HIT; information about 0 (antipodal identity) | model | low | none yet | none |
| K1-fit-I | fit to \(I\) within \(10^{-8}\) of \((1,0)\), residual \(<10^{-9}\) | \((1,0)\), residual 0 | HIT; information about 0 | model | low | none yet | none |
| K1-fit-chi | fit to \(\chi\) within \(10^{-8}\) of \((1,1)\), residual \(<10^{-9}\) | \((1,1)\), residual \(8.327\times 10^{-17}\) | HIT; information about 0 | model | low | none yet | none |
| K2-ledger | \(\max\lvert I+P_D-\chi\rvert>0.02\) on BIAS | \(0.066278\) | HIT; \(+0.046278\) nat above the bar | model | low | none yet | none |
| K2-gram | Gram determinant \(>10^{-6}\) | \(3.835855\times 10^{1}\) | HIT | model | low | none yet | none |
| K2-fit-I | fit to \(I\) within \(10^{-8}\) of \((1,0)\) | \((1,0)\), residual 0 | HIT | model | low | none yet | none |
| K2-bound-weight | \(f>0.005\) at the least-squares fit of \(\chi\) and at every net pair | least-squares \(f=0.0004213774925606595\) at \((1.0033319156709788,\ 0.6581687266183737)\); net minimum \(f=0.0014997828907532262\) at \((1.0,\ 0.65)\) | least-squares \(-0.0045786225074393405\) nat; net \(-0.0035002171092467738\) nat | model | medium | report both numbers; do not declare ratio 1 (`PREREG.md:80`) | none |
| K2-print | the printed net minimum is the minimum on the 121 by 121 net | the stored field was the least-squares residual \(0.0004213774925606595\) | \(-0.0010784053981925667\) nat (printed minus the net minimum \(0.0014997828907532262\)) | measurement/code | medium | script prints the two fields separately; D7; original log kept | none |
| G1 | nine cells, unique \(\theta=0\), cost span \(<10^{-9}\) | no bad cell; cost span 0 | HIT | model | low | none yet | none |
| G2 | ratio 1 range \(<10^{-9}\); ratio 2 unique \(\theta=0\) and endpoint gap \(>0.01\) | range \(8.327\times 10^{-17}\); \(\theta=0\); gap \(0.096372\) | HIT | model | low | none yet | none |
| G3 | \(w=1\) gives \(\theta^\star>0.2\); \(w=10\) gives unique \(\theta=0\) | \(1.570796\); \(0\) | HIT | model | low | none yet | none |
| G4 | \(\lvert\theta_1-\theta_{100}\rvert\ge 0.2\) | gap \(0.464694\) rad | HIT; margin \(+0.264694\) rad | model | low | none yet | none |
| G5 | minimized costs differ by \(P_\chi(0)=0.096372378511\) within \(10^{-9}\) | cost gap \(0.048186189255\); angles agree | \(-0.048186189256\) nat | model | medium | literal miss stands; the parenthesis is not the criterion (D2) | none |
| C1 | at least one interior stake in \(\{0.5,1,2,4,8\}\) | 0 interior stakes | \(-1\) interior stake | model | medium | none yet; a later lock would name a search rule, not these stakes | none |
| C2 | at least two interior stakes, recovering both coefficients within \(0.02\) | 1 interior stake | \(-1\) interior stake | model | medium | none yet | none |
| C3 | ratio 0 above \(\pi/2-0.02\); ratio 1 below \(0.02\) | \(1.570796\); \(0\) | HIT | model | low | none yet | none |
| T-mono | \(w_{\mathrm{crit}}/\lvert\delta\rvert\) strictly decreasing on fifty angles | \(3.208789\) down to \(2.777911\) | HIT | model | low | none yet | none |
| T-cells | ten listed cells in the locked phase, interior within one grid step of the root | all ten match | HIT | model | low | none yet | none |
| T-slope | endpoint quotients have the phase sign and absolute value \(>10^{-6}\) | signs match; interior quotients \(-3.386036\times 10^{-7}\) and \(+3.600020\times 10^{-7}\) | magnitude short by \(-6.614\times 10^{-7}\) and \(-6.400\times 10^{-7}\) | model | medium | none yet; a finer grid would be a new preregistration | none |
| T-gamma | \(\gamma=0\) root and \(\gamma=1/2\) minimizer differ by \(\ge 0.1\) rad | gap \(0.704255\) rad | HIT; margin \(+0.604255\) rad | model | low | none yet | none |
| T-lambda | five reuse fractions in the locked phase | all five match | HIT | model | low | none yet | none |
| F-seq | conditional information \(<10^{-9}\); same-basis disturbance \(<10^{-9}\); right-angle disturbance \(>0.05\); added cost \(<10^{-9}\) | \(5.551\times 10^{-17}\); \(0\); \(0.693147\); \(0\) | HIT | model | low | none yet | none |
| F-prod | product cost equals \(2J\) within \(10^{-9}\); minimizers agree within one step | max gap \(2.220\times 10^{-16}\); angles agree | HIT | model | low | none yet | none |
| F-menu | channel match within \(10^{-12}\); gap equals \(\kappa_D P_D\) within \(10^{-12}\); \(P_D(\pi/2)>0.05\) | max channel \(2.220\times 10^{-16}\); gap miss \(1.110\times 10^{-16}\); \(P_D(\pi/2)=0.096372\) | HIT; information about 0 (Route A identity on this grid) | model | low | none yet | none |
| F-rep | \(\lvert I_{16}-\tfrac32\ln 2\rvert<0.02\), and the listed minimizers | \(I_{16}=0.713026\) against \(1.039721\); the listed minimizers match | \(-0.326695\) nat; the other clauses hit | model | medium | the \(n=256\) readout is D3; the prediction was not edited | none |
| F-span | two-copy residual \(>0.01\) | residual \(2.078781\times 10^{-5}\); slope ratio \(0.559888\) | \(-0.009979\) nat | model | medium | report the pair; do not declare a flow (`PREREG_FIXED_POINTS.md`) | none |
| D-value | antipodal ranges \(<10^{-9}\); biased range \(>0.02\) | antipodal about \(10^{-16}\); biased \(0.132555\) | HIT; antipodal part is an identity | model | low | none yet | none |
| D-argmin | ratio-0 and ratio-1 angles differ by \(\ge 1\) rad; ratio 2 matches ratio 1 | gap \(1.570796\); gap \(0\) | HIT | model | low | none yet | none |
| H1-lin | absolute second difference in \(q\) \(<10^{-9}\) | \(2.776\times 10^{-17}\) | HIT; information about 0 (\(J\) is linear in the ratio) | model | low | none yet | none |
| H1-joint | \(J^\star(q)\ge J^\star(0)-10^{-9}\) | holds on the listed pairs | HIT | model | low | none yet | none |
| H1-half | half-ratio gap at \(w=1\) is \(>0.01\); at \(w=10\) both sit at \(\theta=0\) within \(10^{-9}\) | \(0.048186\); \(0\) | HIT | model | low | none yet | none |
| H2-split | at \(w=1\), ratio 0 is the equator and ratio 1 is the pointer, gap \(\ge 1\) rad | gap \(1.570796\) | HIT | model | low | none yet | none |
| H2-below | at \(w=2\), ratio 0, unique \(\theta=\pi/2\) | \(1.570796\) | HIT | model | low | none yet | none |
| H2-move | \(\lambda=0.7\) is the pointer at \(w=1\) and the equator at \(w=0.5\) | \(0\); \(1.570796\) | HIT | model | low | none yet | none |
| R-class | \(I_{16}=\tfrac32\ln 2-H(C\mid K)\) within \(10^{-9}\), and \(H>0.2\) | identity gap \(8.882\times 10^{-16}\); \(H=0.326695\) | HIT; information about 0 (the three-rate identity) | model | low | none yet | none |
| R-low | unique minimizer within \(0.15\) rad of \(\pi/4\), and that angle beats both ends by \(>0.05\) | \(\theta=1.570796\) | \(+0.785398\) rad (equator minus \(\pi/4\)) | model | medium | the collision angle used the pre-dephasing vector; prediction not edited | none |
| R-high | unique \(\theta=0\) at \(w=4\) and at \(w=10\) | \(1.468258\); \(1.005746\) | \(+1.468258\) rad; \(+1.005746\) rad | model | medium | reported as grid nodes; prediction not edited | none |
| R-pos | at \(n=256\), \(w=1\), ratio \(1\) and ratio \(0.5\) are unique \(\theta=0\) | both \(0\) | HIT | model | low | none yet | none |
| R-ratio | no listed ratio beats \(q=0\); second difference in \(q\) within \(10^{-9}\) | second difference \(-1.776\times 10^{-15}\) | HIT | model | low | none yet | none |
| Q-comm | Frobenius norm \(0.176776695297\) within \(10^{-9}\), and \(>0.1\) | \(0.176776695297\) | HIT | model | low | none yet | none |
| Q-slope | every entropy disturbance \(>0.02\) | min \(0.025450\) | HIT | model | low | none yet | none |
| Q-pointer | \(P_D(0)>0.02\) and \(P_D(\pi/2)>0.02\) | both \(0.025450\) | HIT | model | low | none yet | none |
| Q-garble | every label gap \(>0.1\) | min gap \(0.150000\) | HIT | model | low | none yet | none |
| Q-state | trace distance \(>0.2\) | \(0.300000\) | HIT | model | low | none yet | none |
| Q-reuse | conditional information \(>0.05\); disturbance sum \(>0.02\); \(q=1\) and \(q=2\) exceed \(q=0\) by \(>0.01\) | \(I=0.017070\); disturbance \(0.084896\); gaps \(0.084896\) and \(0.169791\) | \(-0.032930\) nat on the information bar; the other two clauses hit | model | medium | none yet; the cost still selects ratio 0 | none |
| Q-rank | \(\lvert P_D\rvert<10^{-12}\), \(\lvert I\rvert<10^{-12}\), ledger gap equals \(\tfrac12\ln 2\) within \(10^{-9}\) | \(0\); \(0\); \(0.346573590280\) | HIT; information about 0 (rank-2 ledger) | model | low | none yet | none |
| Q-coh | \(P_D>0.01\) and the cost gap \(>0.01\), under the projectors named in the lock | \(P_D=0\); cost gap \(0\) | \(-0.01\) nat on each bar | model | medium | re-score appended; original line kept (D4, D5) | none |
| Q-coh-script | the stored disturbance is the disturbance of the locked projectors | the `00e8dfa` line was \(0.065406\), the gap to \(\mathrm{diag}(1/2,1/4,1/4)\) | \(+0.065406\) nat relative to the locked instrument's \(0\) | measurement/code | medium | D4–D6; preregistration not edited | none |

### Scaled write-up

- **K2-bound-weight (medium).** The lock required \(f>0.005\) at the least-squares fit and on the whole net, against the rival that some fixed pair reproduces the Holevo bound on this ensemble. Both numbers fall short, by \(-0.0045786225074393405\) nat and \(-0.0035002171092467738\) nat. The location is the model: the bound is an affine image of \((I,P_D)\) here. The update is the one the lock already named: report the pair and do not declare ratio 1.
- **K2-print (medium).** The printed net field was the least-squares residual, low by \(-0.001078\) nat. The location is measurement/code: the assignment after the fit overwrote the grid minimum, and the same script reproduces it. The update is D7. It is not a rescue of the bound clause, which still misses on the corrected number.
- **G5 (medium).** The lock's symbol is a gap of \(P_\chi(0)\). The outcome is half of that, short by \(-0.048186\) nat, while the angles agree. The location is the model: the sentence named the full Holevo value where the shift is half a ledger. The update is D2. The parenthesis was not adopted as the criterion.
- **C1 and C2 (medium).** C1 asked for at least one interior stake and got zero (\(-1\)). C2 asked for two and got one (\(-1\)). The location is the model: those stake lists sit on the corners. The update is none in this file. A later lock would name a search rule that does not use the post-hoc angles.
- **T-slope (medium).** The interior quotients have the locked signs and miss the magnitude bar by \(-6.614\times 10^{-7}\) and \(-6.400\times 10^{-7}\). The location is the model, on one interior cell. The update is none yet. The endpoint cells hit.
- **F-rep (medium).** \(I_{16}\) is short of \(\tfrac32\ln 2\) by \(-0.326695\) nat. The other listed minimizers hit. The location is the model: \(n=16\) has not reached the saturated count. The update is the readout in D3. The prediction was not edited.
- **F-span (medium).** The residual is short of \(0.01\) by \(-0.009979\) nat, so the two-copy cost stays an affine image of the single-shot pair at this tolerance. The location is the model. The update is the locked one: report \(\alpha\), \(\beta\), and the slope ratio \(0.559888\), and do not declare a flow.
- **R-low (medium).** The minimizer is the equator, \(+0.785398\) rad from \(\pi/4\). The location is the model: the collision angle was computed from the pre-dephasing Bloch vector, and at \(\gamma=0\) an equatorial copy is a fair coin. The prediction was not edited.
- **R-high (medium).** The minimizers sit \(+1.468258\) rad and \(+1.005746\) rad off the pointer. The location is the model: \(n=256\) has not reached the pointer at those stakes. The angles are grid nodes. The prediction was not edited.
- **Q-reuse (medium).** Conditional information is short of \(0.05\) by \(-0.032930\) nat. The disturbance sum and the cost gaps hit, and the cost still selects ratio 0. The location is the model. The update is none yet.
- **Q-coh (medium).** Under the locked projectors the disturbance and the cost gap are \(0\), each short of its bar by \(-0.01\) nat. The location is the model: those projectors fix the coherent block. The update is the appended re-score.
- **Q-coh-script (medium).** The first stored line was \(+0.065406\) nat above the locked instrument. The location is measurement/code: that line used a different map, and D4–D6 record the order and the restore. The preregistration was not edited.
