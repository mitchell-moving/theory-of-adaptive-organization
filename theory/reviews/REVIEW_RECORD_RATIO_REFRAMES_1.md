# Independent review 1: record-ratio reframes

*24 November 2026 (UTC). Independent review of draft PR #8, branch `forge-record-ratio-reframes`, head `c5347986407a9f53784d75ff0371a8d1657d0bb3`. The memo is `theory/RECORD_RATIO_REFRAMES_2026-11-24.md`. This file is the review. It does not edit the memo, the locks, `THEORY.md`, `OPEN_WORK.md`, or `theory/README.md`.*

## Result

No HIGH finding. No MEDIUM finding. Three LOW findings. The numeric claims that were attacked reproduce. The H1 and H2 write-ups name a precise break. The argument that joint minimization never goes below \(J^\star(0)\) is sound on \(q\ge 0\). The repeated-record preregistration predates its grid, and its sha256 matches.

## What was run

Tree `c534798` on `forge-record-ratio-reframes`. `origin/main` is `0f3791890078161a1172277162df5ac13ebbff46`. `origin/forge-record-ratio-consistency` is `21ab5f03ac0b32daf4796ad65a61cb3b94a84e10`. Merge base of this head with that base is `f795666`.

- `python3 tools/check_consistency.py`. Exit 0. `RESULT: PASS`. Wording FAILs 0 on 31 maintained docs. Process-rule FAILs 0. Core-rule FAILs 0.
- `python3 -m pytest -q tools`. **297 passed, 1 skipped**, 385.15 s, exit 0. The skip is `tools/test_lean.py:124`, `Lean 4 / lake is not installed` (`lake` is absent from `PATH`). Pytest, NumPy, SciPy, and SymPy were installed in this environment before the run; the first collection stopped on the missing modules.
- The five scripts the memo cites, each compared byte for byte with the stored stdout: `mhd_analogy_checks.py`, `repeat_asymptote_checks.py`, `fixed_point_checks.py`, `record_ratio_reframes_checks.py`, `posthoc_windows.py`. All five match. `repeat_asymptote_checks.out` still ends `FAILS 2`. `mhd_analogy_checks.out` still ends `FAILS 0`.
- Throwaway stdlib script, not committed. It recomputes the post-dephasing pinch, the single-shot cost, the binomial count channel by a ratio recurrence (not `math.lgamma`), and the \(n=256\) grid. The numbers below are from that script unless a line says the author's function was printed for a digit check.

## Locks

| Lock | Commit | Author and committer time (UTC) | sha256 | Blob at the lock commit and at HEAD |
|---|---|---|---|---|
| `PREREG.md` | `8563c91` | 15:46:47 | `8e495b7b97bbf254429dc4ed0aeb153944579db9f2230eae769937e98b43fce8` | same |
| `PREREG_FIXED_POINTS.md` | `c864603` | 16:07:39 | `82d58bdcefca97218ac4b7587a9246850994eedac1c6c372de8f50a75417017b` | same |
| `PREREG_MHD.md` | `4ca0322` | 16:24:05 | `faf04d3d53de980141cbfd57a3dfb30f34af6e6f8d7efb5ce72f5a01e3dc25b6` | same |
| `PREREG_REPEAT_ASYMPTOTE.md` | `e0b411a` | 16:30:08 | `5b0846fa823e86d63c71133831ec966ac42f3f3a27f1cff9ec613c392adfa60a` | same |

Each sha256 file's first token equals the digest of the lock bytes. Each lock commit is an ancestor of `c534798`, and the parent links put the lock before the script: `repeat_asymptote_checks.py` and `repeat_asymptote_checks.out` are absent from `e0b411a`; `mhd_analogy_checks.py` is absent from `4ca0322`; `fixed_point_checks.py` is absent from `c864603`; `record_ratio_reframes_checks.py` is absent from `8563c91`. The memo at `e0b411a` does not contain `1.468258`, `1.005746`, `0.326695`, `5.776226504666`, or `2.776e-17`. Git records the order. It does not show a wall clock outside the commits. Author date and committer date agree on each of these four commits.

`PREREG.sha256` says 15:46:38. The commit is 15:46:47. The digest matches either way.

## Numeric claims

**Second difference \(2.776\times 10^{-17}\).** At \(\theta\in\{0,\pi/4,\pi/2\}\), \(q\in\{0.25,0.5,0.75,1\}\), step \(1/4\), \(w=1\), the largest absolute second difference is \(2.7755575615628914\times 10^{-17}\), which prints as `2.776e-17`. That is the residue of an algebraic zero. At fixed \(\theta\), \(J=\kappa I+q\kappa P_D+w L\) and \((I,P_D,L)\) do not depend on \(q\) (`mhd_analogy_checks.py:37-39`). A product \(q(1-q)\) would have second difference \(-\kappa P_D/8\), about \(-0.012\) at the equator, not \(10^{-17}\). The linearity claim holds.

**Half-ratio excess \(0.048186\) at stake 1.** Both unique minimizers on the 721-point grid are the equator. \(J^\star(0.5)-J^\star(0)=0.048186189255439354=P_D(\pi/2)/2\), with \(P_D(\pi/2)=0.09637237851087871\). Six-digit rounding is `0.048186`. At \(w=10\), \(q=0\) and \(q=0.5\) are both the unique pointer and the costs agree.

**\(I_{16}\) and \(H(C\mid K)\).** Independent count entropy at \(\theta=0\), \(n=16\): \(I_{16}=0.713026221429\), \(H(C\mid K)=0.326694549411\). They print as `0.713026` and `0.326695`. Their sum equals \(\tfrac32\ln 2=1.039720770840\) to \(2.22\times 10^{-16}\) on the normalized recurrence. The author's `lgamma` path, rerun here, still prints `identity_gap=8.882e-16` (`repeat_asymptote_checks.out:1`). The identity holds.

**Stake-4 and stake-10 minimizers.** On the locked grid, \(q=0\), \(n=256\):

- \(w=4\): index 673, \(\theta=673\pi/1440=1.4682582332402296\), unique, \(J=0.680024647\). Prints as `1.468258`.
- \(w=10\): index 461, \(\theta=1.0057459814617324\), unique, \(J=1.039457661\). Prints as `1.005746`.

The stored stdout matches. A 201-point refinement on a window of two grid steps moves the \(w=4\) angle by \(+5.24\times 10^{-4}\) rad, to about \(1.46878\), and lowers \(J\) by \(2.7\times 10^{-6}\). It moves the \(w=10\) angle by \(-3.93\times 10^{-4}\) rad, to about \(1.00535\), and lowers \(J\) by about \(5\times 10^{-9}\). Both refined points sit inside the window. The sixth printed digit is the grid node. The design claims survive: neither angle is the pointer, the \(w=4\) record is unresolved, and the \(w=10\) cost stays a few ten-thousandths under the ceiling. See L1.

The post-hoc \(I=0.196942\) at `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:68` is the mutual information at the truncated literal \(1.468258\) (`0.196941645`, which rounds to `0.196942`). The exact grid node has \(I=0.196940909\), which rounds to `0.196941`. \(L\) rounds to `0.120771` either way, and \(J=0.680025\) is the grid-node cost.

**Threshold \(3\ln 2/r^2=5.776226504666\).** With \(r=0.6\), \(3\ln 2/r^2=5.776226504666210\), which rounds to the printed twelve decimals. At that stake the equator's cost \(w r^2/2\) equals the pointer ceiling \(\tfrac32\ln 2\) exactly. Below it, \(\tfrac32\ln 2>w r^2/2\).

**Equator's cost \(w r^2/2\).** At \(\gamma=0\), \(\theta=\pi/2\), \(\phi=0\), every world has outcome probability \(1/2\), so \(I=0\) and the conditional mean of \(y\) is the prior mean. Prior variance of \(y\) is \(r^2/2=0.18\). The \(n=256\) evaluation returns \(I=0\) and \(L=0.18000000000000002\). The cost at ratio 0 is \(w r^2/2\) at this \(n\), and the same \(I\) and \(L\) hold at \(n=1\).

**Equatorial copy at \(n=256\).** Post-dephasing Bloch vectors are \((0,0,\pm r)\) and \((0,0,0)\). The equatorial axis is \((1,0,0)\). All four dots are 0, so each copy is a fair coin and is independent of \(W\). The count is \(\mathrm{Binomial}(256,1/2)\) for every world. \(I_{256}(\pi/2)=0\). The same four probabilities are \(1/2\) at every \(n\), which is the sentence at `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:64` and `:199`. The pre-dephasing rates in `PREREG_REPEAT_ASYMPTOTE.md:26` are not the rates in `fixed_point_checks.py:101-104`. That diagnosis of R-low and R-high is right. At \(\theta=\pi/4\) the post-dephasing probabilities are about \(0.712\), \(0.288\), \(0.5\), \(0.5\): no sign-pair collision.

Pointer readout at \(n=256\): \(I(0)=1.039720337\), \(L(0)=4.02\times 10^{-8}\). Six digits are `1.039720` and `0`. At \(\pi/4\), \(I=1.038833279\) and \(L=0.000084745\), which print as the memo's `1.038833` and `0.000085`.

## H1 and H2

**H1 names the break.** `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:40`: "The break is the step from current times field to a product." The channel power is proportional to \(K(1-K)\). This \(J\) is linear in \(q\). The second difference on the locked mesh is the roundoff above, and \(P_D(\pi/2)/2=0.048186\) is a cost increase at the half ratio, not a power maximum. The break is that algebraic step.

**The joint-minimum argument is sound.** For \(\kappa>0\), \(q\ge 0\), and \(P_D(\theta)\ge 0\),

\[
J(\theta,q)=J(\theta,0)+q\kappa P_D(\theta)\ge J(\theta,0)\ge J^\star(0).
\]

Hence \(J^\star(q)\ge J^\star(0)\) for every real \(q\ge 0\), and in particular on \(\{0,0.25,0.5,0.75,1,2\}\). On this ensemble \(P_D=\tfrac12\big[h((1+r|\cos\theta|)/2)-h((1+r)/2)\big]\ge 0\), with equality only at \(\theta=0\). A 10001-point mesh has minimum \(P_D=0\) and no negative value. The closed form matches the explicit four-state average to \(1.11\times 10^{-16}\) on all 721 angles. An extended probe at stakes \(\{0.01,0.5,1,2,100\}\) and ratios \(\{0,0.01,0.25,0.5,0.75,1,2,7\}\) found no undershoot. At \(q=-0.1\) the same probe undershoots, so the sign of \(q\) is necessary. The memo's set is nonnegative (`theory/RECORD_RATIO_REFRAMES_2026-11-24.md:40`). The repeated-record cost adds \(q\, n P_D\) with the same \(P_D\ge 0\), so the same bound is why no ratio in \(\{0,0.5,1,2\}\) beats \(q=0\) at \(n=256\).

**H2 names the break.** `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:46`: "The break is the assumption of one ratio of two terms." The cell is specific. At \(w/\kappa=1\), \(q=0\) is the unique equator and \(q=1\) is the unique pointer, gap \(\pi/2\). At \(q=0\) and \(w/\kappa=2\) the unique minimizer is still the equator. At \(q=0.7\), \(w=1\) is the unique pointer and \(w=0.5\) is the unique equator. Those three cells were recomputed. One number near 1 does not select the design. The ratio of the two thresholds is \(\ln((1+r)/(1-r))/(2r)\). At \(r=0.6\) that is \(1.155245300933\), and \(w_\star=3.209014724815\), \(1/r^2=2.777777777778\).

The header on each of those sections is **Puzzle**, and both locked checks pass (`FAILS 0`). The glossary at `CORE.md:169` asks a puzzle to carry a next test. The memo says neither break is worth a further lock (`:36`). H1 stops at a different objective (`:42`). H2 says a further grid does not make the boundary one number (`:48`). That is L2. It does not blur the break points. <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->

## DOIs

Fetched from `api.crossref.org` on 24 November 2026.

- `10.1002/j.1538-7305.1956.tb03809.x`. Type `journal-article`. Title "A New Interpretation of Information Rate." Author J. L. Kelly, Jr. Container *Bell System Technical Journal*, volume 35, pages 917–926, issued July 1956. Matches `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:213` and `PREREG.md:39`.
- `10.1017/9781316672853`. Type `monograph`. Title "Introduction to Magnetohydrodynamics." Author P. A. Davidson. Publisher Cambridge University Press. Edition 2. `published-print` and `issued` are 22 December 2016. `published-online` is 9 February 2017. The memo's "2017" is the online date (`theory/RECORD_RATIO_REFRAMES_2026-11-24.md:36`, `PREREG_MHD.md:19`).
- `10.1115/1.3625105`. Type `journal-article`. Title "Engineering Magnetohydrodynamics." Container *Journal of Applied Mechanics*, volume 33, page 478–478, issued 1 June 1966. Authors on the record: G. W. Sutton, A. Sherman, and Ira M. Cohen. A one-page item. The memo calls this DOI a journal notice of the McGraw-Hill book and not a page of the derivation (`theory/RECORD_RATIO_REFRAMES_2026-11-24.md:36`, `PREREG_MHD.md:15`). That reading fits the page span. Crossref does not label the type `book-review`.

No other DOI appears in the memo or the four locks. Sharma is arXiv `1306.3791v2`, title "A gambling interpretation of some quantum information-theoretic quantities." A Crossref bibliographic query and a title-plus-author query do not put that paper on the first page. No DOI was returned for it. The memo's sentence at `:214` stands.

The review citations checked against `21ab5f0`: `:7` is "No HIGH finding. No MEDIUM finding." `:42` is the stock gap \(\kappa_D P_D\). `:50` is the destruction charge \((\kappa_D-\kappa)P_D\), zero at every \(\theta\) exactly at ratio 1, and the start of the R1 sentence. `:89` has \(H(M)\) `0.647447`, `0.654470`, `0.693147`, record costs `0.050672`, `0.057695`, `0.096372`, and levelings `0.549` and `0.526`. `:90` is the mixed rank-2 block, sides separated by \(\tfrac12\ln 2\). `:152` says the destruction charge is outside R1.

## Wording, THEORY.md, personal data

Added lines from `f795666..HEAD` in `theory/` and `OPEN_WORK.md`:

- No added sentence contains the phrase theory of everything.
- "law": only the quotation "The law of adaptive organization (hypothesis)" in the four locks (`PREREG.md:5` and the same line in the other three). The word is inside the hypothesis label.
- "solved": only "will not say that the ratio has been solved" / "will not say the ratio has been solved" / "will not say that either analogy has been solved" (`PREREG.md:129`, `PREREG_FIXED_POINTS.md:148`, `PREREG_MHD.md:65`, `PREREG_REPEAT_ASYMPTOTE.md:69`).
- "bill", "kill", "verdict": no hit.
- "general relativity", "quantum mechanics", "holography": only the sentence that nothing here derives them, in the memo header, the four locks, and the T76 row of `OPEN_WORK.md:120`.
- "derive": those denials, plus "do not re-derive" (`PREREG.md:43`) and "checked rather than re-derived" (`theory/RECORD_RATIO_REFRAMES_2026-11-24.md:167`).

Eight of the nine **Model implication** paragraphs carry a status word. The paragraph at `:32` does not. That is L3.

`git rev-parse HEAD:THEORY.md` and `git rev-parse main:THEORY.md` are both `6caadae569116a94a74563398be94cebf6e99e9b`. `git diff main -- THEORY.md` is empty. `main` and `origin/main` are the same commit.

The added file text has no email address, no telephone number, and no government-id pattern. The commit identity on this branch is the existing author line. It is not new personal data in the diff.

## LOW

**L1. The six-digit stake-4 and stake-10 angles are grid nodes.** `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:62` and `:68` report the minimizers `1.468258` and `1.005746`. Those are index 673 and index 461 of the 721-point grid, spacing \(\pi/1440\approx 0.002182\). A local refinement moves them by \(5.24\times 10^{-4}\) and \(3.93\times 10^{-4}\) rad. The fourth decimal changes. The locked prediction was a grid argmin (`PREREG_REPEAT_ASYMPTOTE.md:55`), and the qualitative sentences (not the pointer, unresolved, still under the ceiling) survive. The post-hoc \(I=0.196942\) at `:68` is the value at the truncated literal, one unit in the sixth digit above the exact grid node.

**L2. H1 and H2 are labeled Puzzle, and the next test is declined.** `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:38` and `:44`. `CORE.md:169`, which the memo cites at `:3`, says a puzzle is a miss with a diagnosis and a next test. Both sections name the break (`:40`, `:46`). The memo then says neither break is worth a further lock (`:36`). H1 stops at a different objective (`:42`). H2 says a further grid does not make the boundary one number (`:48`). The model implication at `:50` labels the same paragraphs **NUMERICAL** and **Analogy, hypothesis**. The locked script reports `FAILS 0` (`mhd_analogy_checks.out:7`). The break points are precise. The status word is the defect. <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->

**L3. One model implication has no status word.** `theory/RECORD_RATIO_REFRAMES_2026-11-24.md:32` states four conditionals about the menu, the ensemble, and the rank-2 block, and it does not attach a word from `CORE.md:169`. The eight later model implications do (`:50`, `:72`, `:94`, `:112`, `:127`, `:147`, `:167`, `:189`). The closing sentence of `:32` says none of the four is a derivation of the coefficient. The paragraph is still unlabeled.
