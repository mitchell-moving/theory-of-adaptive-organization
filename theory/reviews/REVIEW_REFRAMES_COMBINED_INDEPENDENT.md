# Independent review of the combined T75/T76 head

Head `d117ca620f60c06feb63dc722a2887251eabb27c` on `forge-record-ratio-reframes`. Base is fork `main` at `0f3791890078161a1172277162df5ac13ebbff46`. Scope is the diff against that main, the five preregistration files, and `main`. `THEORY.md` is unchanged (blob `6caadae569116a94a74563398be94cebf6e99e9b`, the same object on `main`).

The merge `d117ca6` has parents `0598334` (T76 errata) and `21ab5f0` (T75 review). It adds one file, `theory/reviews/RECORD_RATIO_CONSISTENCY_REVIEW_1_2026-11-24.md`. That blob equals the blob at `21ab5f0`. The T75 memo blob equals the blob at `f795666`. No path present on either parent is absent at this head.

## Result

One locked pass scores a different instrument from the one named in `PREREG_QUANTUM.md`. The coherent rank-2 block is fixed by the projectors in the lock, so its disturbance is 0. The stored line `Q-coh PASS` is the entropy gap to the fully dephased diagonal state, `0.065406`. The memo, the answer section, and the T76 row repeat that number as a selection of ratio 0.

The other headline numbers that were recomputed match the stored digits. The five locks sit in their own commits before their grids, the sha256 sidecars match, and those blobs are unchanged at this head. Misses that the locks predicted are still present as `FAIL` lines. `DEVIATIONS.md` only grew.

## What was run

All three checkers from the repo root, exit 0.

- `python3 tools/check_consistency.py`. `RESULT: PASS`. `FAIL: 0`. `INFO (frozen records): 29`. Maintained docs scanned: 31; wording FAILs: 0. Frozen records scanned: 496. CLAIM_MAP section N: 68 rows (`N1`..`N68`); N references checked: 123; mismatches: 0. CLAIM_MAP rows counted: 392 (tally 392). Tables checked: 124. Process-rule FAILs: 0. Self-reviews found by header: 14. Appendix C and CLAIM_MAP section O: 74 and 74. Core-rule FAILs: 0. Soft length warnings: `THEORY.md` 11325 words, `README.md` 1857 words.
- `python3 tools/check_open_work.py`. `items.json` not-DONE: 62; `QUEUE.md` not-DONE: 90; union missing from `OPEN_WORK.md`: 0. `RESULT: PASS`.
- `python3 tools/check_fresh.py`. `STATUS.md` main is `d592662`; window `0f37918 d592662 f4ec246 341b7de b611a68`. `RESULT: PASS`.

Pytest, after installing NumPy 2.5.5, SciPy 1.18.1, SymPy 1.14.0, and pytest 9.2.0 for the run. Those packages are not added to the tree. `lake` is absent.

- `python3 -m pytest -q` from the repo root. Collection exit 2. `301 tests collected, 1 error in 1.51s`. The error is `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py`: `ModuleNotFoundError: No module named 'numba'`. That file is on `main`. Its import writes `test_result.json`. It was not executed.
- `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE`. **300 passed, 1 skipped, 386.29 s, exit 0.** The skip is `tools/test_lean.py:124`, `Lean 4 / lake is not installed`. Collection of `tools` alone is 301 tests. With that importer ignored, collection outside `tools` is empty. The executable suite is the `tools` suite.

An independent script, not committed, recomputed the channel, the closed form, the phase boundary, the Holevo fits, the rank-2 projectors, the unsharp Kraus maps, and the `n=256` count channel with SciPy's binomial pmf. It does not call the repository scripts.

## Locks

| Lock | Commit | sha256 | Blob at the lock and at this head | First result commit |
|---|---|---|---|---|
| `PREREG.md` | `8563c91` | `8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8` | `01e6a499aa466bde0f8e9a82fa04e00d0a323de5`, same | `0c875c4` |
| `PREREG_FIXED_POINTS.md` | `c864603` | `82d58bdcefca97218ac4b7587a9246850994eedac1c6c372de8f50a75417017b` | `bcd4121ac432a49adeb50b3dd065c43614b3fc6e`, same | `a849170` |
| `PREREG_MHD.md` | `4ca0322` | `faf04d3d53de980141cbfd57a3dfb30f34af6e6f8d7efb5ce72f5a01e3dc25b6` | `87db4b1c9ba8459ce6d3c6139ce29a8cf10b30d8`, same | `c534798` |
| `PREREG_REPEAT_ASYMPTOTE.md` | `e0b411a` | `5b0846fa823e86d63c71133831ec966ac42f3f3a27f1cff9ec613c392adfa60a` | `8df0fcc1e56df405a222fadb767050a5e4dcb75e`, same | `c534798` |
| `PREREG_QUANTUM.md` | `dba140b` | `1ac92e314705b3378e3b6a1bd665d36ec6dc9f7f812760a20bc4556617b817d3` | `10c83a275222984fe456bc0daf89fcccaa3f7948`, same | `00e8dfa` |

Each lock commit adds only that file and its `.sha256` sidecar. Each sidecar's first token is the sha256 of the lock bytes. Parent links put every lock before its `.py` and `.out`: `0c875c4` follows `8563c91`, `a849170` follows `c864603`, `c534798` follows `e0b411a` which follows `4ca0322`, and `00e8dfa` follows `dba140b`. The MHD and repeated-record outputs share `c534798`, after both of those locks. No preregistration blob changes after its lock commit. No `.out` file has a second commit. The sidecar clock `15:46:38` on `PREREG.sha256` is nine seconds before the commit `8563c91` at `15:46:47` UTC. The digest matches either way.

`DEVIATIONS.md` is created in `80f9e7b` with D1 and D2, then `c534798` appends D3 and leaves D1 and D2 byte-identical. Later commits do not touch it. D1 and D3 are labeled post-hoc and do not change the `FAILS` counts (`FAILS 4` and `FAILS 2` remain). D2 records that G5 was scored against the symbol \(P_\chi(0)\), and the sentence was not rewritten. The stored G5 line is `FAIL` with `literal_miss=4.819e-02`.

## Merge

`git diff 0598334 d117ca6` is the T75 review file, 152 lines. `git diff 21ab5f0 d117ca6` is the T76 tree. The T75 memo and the T76 memo are both present once. `OPEN_WORK.md` has one T75 row and one T76 row. The stored stdout files each contain one line per check name. The errata `0598334` rewrites sentences in the memo, the T76 row, and `theory/README.md`. It does not duplicate a `FAIL` line and it does not delete the quantum paragraph from `OPEN_WORK.md` or from the memo.

`theory/README.md` is the stale index. At `00e8dfa` the quantum commit edits the T76 row and changes the words `two preregistrations` to `hash-locked checks`. The row still does not name the fifth lock, `FAILS 1`, or the coherent-block number. The errata edits the same row again, adding the two MHD next tests, and still does not name the fifth lock. `OPEN_WORK.md` and the memo do.

T75 and T76 agree on the claim that was scored: none of the readings forces \(\kappa_D/\kappa=1\). Route A’s gap \(\kappa_D P_D\), zero at every angle exactly at \(\kappa_D=0\), is the stock-price map in the fixed-point lock. The destruction charge that would zero the gap at ratio 1 is the charge named in the T75 memo and restated at review lines 50 and 152. The pins `theory/reviews/RECORD_RATIO_CONSISTENCY_REVIEW_1_2026-11-24.md:7`, `:50`, `:89`, `:90`, and `:152` land on those sentences in the merged file.

## Numbers recomputed

Antipodal complete dephasing, \(r=0.6\), \(\phi=0\). The Bloch evaluator and the closed form agree to \(5.55\times 10^{-17}\) on \(I\), \(P_D\), and \(L\) at the gate angles. \(P_\chi(0)=0.09637237851087865\), which prints as `0.096372378511`. The equator has \(I=0\), \(P_D\) equal to that same value, and \(L=r^2/2=0.18\). The ledger \(I+P_D\) is constant on the grid. \(w_\star=\ln((1+r)/(1-r))/(2r^3)=3.209014724814562\), which rounds to the printed `3.209014724815`. \(3\ln 2/r^2=5.7762265046662105\).

The ten phase cells match the lock. Interior roots: \(0.704255\) at \((q,w)=(0,3)\) and at \((0.5,1.5)\), grid angle `0.704677`; \(0.634866\) at \((0.67,1)\), grid `0.634864`. At \(\gamma=1/2\), \(q=0\), \(w=3\), the minimizer is the pointer and the complete-dephasing root is \(0.704255\). On the fifty-point mesh, \(w_{\mathrm{crit}}/|\delta|\) falls from `3.208789` to `2.777911`. Endpoint slopes at step \(10^{-4}\): the interior cell \((0.5,1.5)\) has quotients \(-3.386\times 10^{-7}\) and \(+3.600\times 10^{-7}\), under the bar \(10^{-6}\), with the signs the phase asks for. The \((0,1)\) and \((0,10)\) quotients clear the bar. G4’s gap is `0.464694` rad.

G5’s minimized costs differ by \(0.048186189255\) at every listed stake, which is half of \(P_\chi(0)\). The designs agree. The symbol in the lock is the full \(P_\chi(0)\). The `FAIL` is the right score for that symbol. The second difference of \(J\) in \(q\) is \(2.776\times 10^{-17}\). At \(w=1\), \(J^\star(0.5)-J^\star(0)=0.048186189255\).

Off the antipodal pair, equal mixture of post-dephasing \(+z\) and \(+x\) at \(r=0.6\). \(H(M)\) is `0.6474466390`, `0.6544700058`, `0.6931471806` at \(\theta\in\{0,0.4,\pi/2\}\). Ratio-1 record costs are `0.0506718370`, `0.0576952038`, `0.0963723785`. The ratio that levels \(\theta=0\) against \(0.4\) is `0.54871389`. The ratio that levels \(\theta=0\) against \(\pi/2\) is `0.52579212`. The printed `0.549` and `0.526` are those values to three decimals. They are not one ratio.

Biased Holevo fit, no intercept, 721 angles: \(\max|I+P_D-\chi|=0.06627772\), \(\chi=0.126467034034\), Gram determinant `38.3585506`, least-squares weights `(1.003331915670976, 0.6581687266183737)`, max residual `0.00042137749256`. The fit to \(I\) is `(1, 0)` with residual 0. The two-copy affine fit is `(-8.9823415, -5.02910136, 1.35482532)`, slope ratio `0.55988757`, max residual `2.07878\times 10^{-5}`. The range of \(I_2+2P_D\) on the antipodal grid is `0.01628863`. The biased record-cost sum \(R(\delta)+R(-\delta)\) ranges by `0.13255545`.

Repeated records, SciPy binomial, not the repository `lgamma` path. At \(\theta=0\), \(n=16\), \(I_{16}=0.713026221429\) and \(H(C\mid K)=0.326694549411\). They sum to \(\tfrac32\ln 2=1.039720770840\). At \(n=256\), \(q=0\): \(w=1\) is the unique equator; \(w=4\) is grid index 673, \(\theta=673\pi/1440=1.468258233240\), \(J=0.680024647\), \(I=0.196940909\), \(L=0.120770935\); \(w=10\) is index 461, \(\theta=1.005745981462\), \(J=1.039457661\). The truncated literal `1.468258` has \(I=0.196941645\), which rounds to `0.196942`. A 201-point window of two grid steps moves the \(w=4\) angle by \(+5.24\times 10^{-4}\) rad and the \(w=10\) angle by \(-3.93\times 10^{-4}\) rad. At \(n=256\), \(I(0)=1.039720337\), \(L(0)\approx 0\); \(I(\pi/4)=1.038833279\), \(L(\pi/4)=0.000084745\); \(I(\pi/2)=0\), \(L(\pi/2)=0.180000\). Ratios \(0.5\), \(1\), and \(2\) at \(w=1\) are the unique pointer.

Unsharp menu, \(\eta=1/2\), Kraus operators as the square roots of \(E_\pm=(I\pm\eta n\cdot\sigma)/2\). The Frobenius norm of \([E_+(z),E_+(x)]\) is `0.1767766952966368`, and \(\eta^2/\sqrt{2}\) is the same value. Ensemble entropy disturbance on the 721-grid runs from `0.025449577` to `0.025714241`, and the endpoints equal the minimum. Trace distance on the \(+x\) label is `0.300`. The unsharp \(x\) probability is `0.65`. Conditional information of unsharp \(z\) then unsharp \(x\) is `0.017070163`. The two disturbances sum to `0.084895536`.

Rank-2 projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\). On \(\mathrm{diag}(1/2,1/4,1/4)\) the channel is the identity, \(P_D=0\), \(I=0\), and \(|H(M)-S(\rho)|=\tfrac12\ln 2=0.346573590280\). On the coherent block with off-diagonal \(1/8\), the same projectors also leave the matrix fixed, so \(P_D=0\). The gap from that state to \(\mathrm{diag}(1/2,1/4,1/4)\) is `0.06540601797`.

## Crossref

Fetched 24 November 2026 from `api.crossref.org/works/{doi}`.

- `10.1088/1367-2630/16/10/103011`. Type `journal-article`. Title "An improved Landauer principle with finite-size corrections." Authors David Reeb and Michael M. Wolf. Container *New Journal of Physics*, volume 16, issue 10, page `103011`. `issued` and `published-online` are 8 October 2014. Matches the T75 memo and the review.
- `10.1002/j.1538-7305.1956.tb03809.x`. Type `journal-article`. Title "A New Interpretation of Information Rate." Author given name `J. L.`, family `Kelly`. Container *Bell System Technical Journal*, volume 35, issue 4, pages `917-926`. `issued` and `published-print` are July 1956. Matches the title, container, volume, pages, and year in `PREREG.md` and the memo. The preregistration also prints the suffix `Jr.`, which this Crossref author field does not carry.
- `10.1115/1.3625105`. Type `journal-article`. Title "Engineering Magnetohydrodynamics." Container *Journal of Applied Mechanics*, volume 33, issue 2, page `478-478`. `issued` is 1 June 1966. Authors on the record: G. W. Sutton, A. Sherman, and Ira M. Cohen. A one-page item. The memo calls this DOI a 1966 notice of the McGraw-Hill book, volume 33, page 478, and not a page of the derivation. That reading fits the page span. The notice’s author list has the third name.
- `10.1017/9781316672853`. Type `monograph`. Title "Introduction to Magnetohydrodynamics." Author P. A. Davidson. Publisher Cambridge University Press. Edition 2. `issued` and `published-print` are 22 December 2016. `published-online` is 9 February 2017. The memo and `PREREG_MHD.md` print the year as 2017.
- `10.1147/rd.53.0183`. Type `journal-article`. Title "Irreversibility and Heat Generation in the Computing Process." Author R. Landauer. Container *IBM Journal of Research and Development*, volume 5, issue 3, pages `183-191`. `issued` July 1961. This is the DOI already printed at `theory/REPRESENTATION.md:120`. The T75 review adds no page.

Sharma is cited as arXiv `1306.3791v2` with no DOI. No DOI was checked for it.

## Classical-record assumptions

The information coordinate in every scored menu, including `PREREG_QUANTUM.md`, is Shannon mutual information of a classical outcome. The lock says so. Joint minimization over \(q\ge 0\) then sits at 0 whenever the scored disturbance is positive, because \(J\) is linear in \(q\) with that slope. The unsharp grid checks the sign of that slope. It does not replace the Shannon coordinate with a quantum mutual information.

On the unsharp channel the lock’s \(P_D=\mathbb{E}[S(\Phi(\rho))-S(\rho)]\) is not the Umegaki divergence that T75’s projective pinch uses. Across the 721 angles and the four antipodal states, the largest absolute gap between those two functionals is `0.04628655`, at \(\theta=0\) on the \(+x\) state: Umegaki `0.00461260`, entropy increase `0.05089915`. Both are nonnegative on that grid. The ensemble entropy increase stays between `0.025450` and `0.025714`. The memo and the T76 row carry the symbol \(P_D\) from T75 into this menu without stating the gap.

Sequential remeasurement in the fixed-point lock is a rank-1 projective pinch. After that pinch the conditional state is a basis vector, the conditional mutual information is numerical zero (`5.55\times 10^{-17}`), and a same-basis second disturbance is 0. The answer’s first bullet states that sequential remeasurement fixes every ratio. The fifth lock’s unsharp pair is a different composition: the conditional information is `0.017070`, and the cost at \(q=1\) exceeds the cost at \(q=0\) by the disturbance `0.084896`. Ratio 0 is the minimum of that pair. The other ratios are not fixed points of it.

Free classical post-processing, the stake read from the pre-dephasing Bloch vector, and \(P_{D,n}=n P_D\) for product copies are written in the locks. The repeated-record miss is the \(\gamma=0\) case of the stake and the dephasing: section 3 of `PREREG_REPEAT_ASYMPTOTE.md` writes the pre-dephasing probabilities \((1\pm r\cos\theta)/2\) and \((1\pm r\sin\theta)/2\), and the code dots \(n(\theta)\) with the post-dephasing state. R-low and R-high are `FAIL`. The memo says so. The replacement comparison \(3\ln 2/r^2\) matches the equator cost \(w r^2/2\) against the pointer ceiling \(\tfrac32\ln 2\). At \(w=4\), which is below that stake, the \(n=256\) minimizer is still the interior grid node above, cheaper than both the equator (`0.72`) and the pointer (`1.039720`).

## Wording

Scanned the diff’s new prose, the five locks, the check scripts, `OPEN_WORK.md`’s new rows, and `theory/README.md`’s new rows.

- No phrase `theory of everything`.
- `solved` occurs only inside `will not say that the ratio has been solved` and the same refusal for the analogies (`PREREG.md:129`, `PREREG_FIXED_POINTS.md:148`, `PREREG_MHD.md:65`, `PREREG_REPEAT_ASYMPTOTE.md:69`, `PREREG_QUANTUM.md:73`).
- No word `bill`.
- `kill` in the new code is the comment `Φ kills the coherence` at `quantum_record_checks.py:281`. The T75 review and the earlier T76 review quote `kill` and `verdict` to say those words are absent from the memo. No new sentence uses either word as a status of a result.
- `law` inside the hypothesis quotation `The law of adaptive organization (hypothesis)` at `CORE.md:7`, copied into each lock. Outside that quotation, the new prose uses `outcome law` (`RECORD_RATIO_REFRAMES_2026-11-24.md:87`, `PREREG_QUANTUM.md:53`), `unsharp x law` in the T76 row of `OPEN_WORK.md`, and `joint law` in the T75 review at line 40. Those are probability-law uses. They do not name the hypothesis.
- The sentences that mention general relativity, quantum mechanics, holography, or gravity say that nothing here derives them. No sentence claims a derivation of any of those.

`ELEMENTARY` and `NUMERICAL` are used beside the status words at `CORE.md:169`. The route and miss labels that carry a status use `PROVED (in-model)`, `KNOWN`, `Puzzle`, and `OPEN`.

## Attacks tried

- Replayed the parent chain of all five locks and hashed each blob at the lock commit and at this head.
- Diffed both merge parents against `d117ca6` and compared the T75 memo blob with `f795666`.
- Walked `DEVIATIONS.md` commit by commit and checked that each `.out` has a single introducing commit.
- Re-derived the antipodal closed form, the loss, the phase boundary, and the G5 shift from the Bloch channel. The G5 cost moves by half the ledger.
- Re-fit the biased Holevo quantity and the two-copy span by least squares.
- Rebuilt the `n=16` and `n=256` count channels with SciPy, including a local refinement around the two reported minimizers, and checked the literal `1.468258` against grid index 673.
- Applied the rank-2 projectors to both the diagonal state and the coherent block, and compared that \(P_D\) with the dephasing gap the code prints.
- Built the unsharp effects and Kraus operators, the commutator norm, the trace distance, and the conditional information of the two-axis sequence.
- Compared Umegaki’s divergence with the entropy increase on all 721 angles and all four states.
- Solved the off-ensemble levelers to more digits than the three printed decimals.
- Fetched each DOI above from Crossref and checked title, authors, container, and dates against the sentences that cite them.
- Grepped the diff for the banned tokens listed above.
- Read `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py` far enough to see that import writes `test_result.json`, and left it un-run.
- Checked the post-hoc stake band against `posthoc_windows.out`. The printed \(\delta\) values sit on unique interior stakes. The prose endpoint \(w=1.60\), \(\theta=0.127\), is the row `w=1.60 theta=0.126536 ntie=2`.

## Findings

### BLOCKING

**B1. `Q-coh` scores a dephasing map. The projectors named in the lock fix the coherent block.** `PREREG_QUANTUM.md` defines the review instrument as the projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\), then says the coherent block uses the same instrument, with \(P_D=S(\Phi(\rho))-S(\rho)\). Those projectors satisfy \(\Phi(\rho)=\rho\) for

\[
\rho=\begin{pmatrix}1/2&0&0\\0&1/4&1/8\\0&1/8&1/4\end{pmatrix},
\]

so \(P_D=0\). The two costs at \(q=0\) and \(q=1\) agree. Ratio 0 is not selected. `qutrit_coherent` instead subtracts the entropy of eigenvalues `(0.5, 0.375, 0.125)` from the entropy of `(0.5, 0.25, 0.25)`. That gap is `0.06540601797`, the stored `Q-coh PASS PD=0.065406`. The comment on that function says the channel kills the coherence. The diagonal block is handled consistently with the projectors (`Q-rank`, \(P_D=0\)). The coherent block is not. `DEVIATIONS.md` does not record the substitution. The memo at lines 85–87, the sentence "On the unsharp menu and on the coherent block the disturbance is positive", and the T76 row’s "A coherent state in that block has \(P_D=0.065406\) and selects ratio 0" all repeat the dephasing number. `tools/test_quantum_record_checks.py` byte-compares the stored stdout, so the suite passes while the locked instrument would fail `Q-coh`.

### HIGH

None.

### MEDIUM

**M1. `theory/README.md` drops the fifth lock.** The T76 index row, after the quantum commit and again after the errata, does not mention `PREREG_QUANTUM.md`, `FAILS 1`, or the coherent-block claim. `OPEN_WORK.md` and the memo do. The quantum commit’s only change to that row is the replacement of `two preregistrations` by `hash-locked checks`.

**M2. The quantum \(P_D\) is the entropy increase, and on this channel that is not T75’s divergence.** The lock states \(\mathbb{E}[S(\Phi)-S(\rho)]\). On the unsharp grid the gap to the Umegaki divergence reaches `0.046287` nat, larger than the ensemble entropy increase at the pointer (`0.025450`). The memo’s quantum section and the T76 row use \(P_D\) for both menus.

**M3. The answer’s first bullet is wider than the map that was scored.** "Sequential remeasurement, and a product of independent worlds. Every ratio is a fixed point" is the projective F-seq result. The unsharp pair in the same answer list changes the cost by `0.084896` at \(q=1\). That composition selects ratio 0. It does not fix every ratio.

### LOW

**L1. The T75 contour pin is still line 102.** The memo at line 128 cites `theory/REPRESENTATION.md:102` for Debreu’s closed contour sets. Line 102 opens the Debreu step. The contour sentence is line 108. The merged review already records this. The memo was not edited.

**L2. The Davidson year is the online date.** DOI `10.1017/9781316672853` has `issued` and `published-print` on 22 December 2016, and `published-online` on 9 February 2017. `PREREG_MHD.md` and the memo print "2nd ed. (Cambridge, 2017)".

**L3. One H2 sentence is in the memo twice.** "A coherence lifetime is not a coordinate of this menu. \(\gamma\) is a dephasing factor already used." Line 47 carries it, with the following clause that \(\gamma\) was not reintroduced as a lifetime. Line 49 ends on the same two sentences again.

**L4. "The same three rates" overstates the large-\(n\) tie.** At \(\gamma=0\) the probabilities of \(\pm z\) are \((1\pm r\cos\theta)/2\) and both \(x\)-labels stay at \(1/2\). Those values depend on \(\theta\). What is shared for every \(\theta<\pi/2\) is the ceiling \(I_\infty=\tfrac32\ln 2\) and \(L_\infty=0\), because the \(x\)-pair stays unresolved and \(y=0\) on that pair. The cost comparison in the memo uses that ceiling. The rate values are not the same.

**L5. The post-hoc endpoint \(w=1.60\) is a tie.** `posthoc_windows.out` has `w=1.60 theta=0.126536 ntie=2 interior=False`. The memo’s "to \(w=1.60\) (\(\theta=0.127\))" is the smaller tied angle, rounded to three decimals. The \(\delta\) values it prints are the unique interior stakes, and those match the file.

**L6. Probability-law wording.** `outcome law`, `unsharp x law`, and `joint law` sit outside the hypothesis quotation. They are not a name for the hypothesis. The maintained-doc checker reports wording FAILs 0. `OPEN_WORK.md` is outside that maintained list.

Blockers remaining: 1
