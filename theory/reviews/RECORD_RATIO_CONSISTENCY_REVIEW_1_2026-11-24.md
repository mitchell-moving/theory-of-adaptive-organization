# Independent review 1: record-price ratio

*24 November 2026 (UTC). Independent review of draft PR #7, branch `forge-record-ratio-consistency`, head `f79566695f8b1dc85125b41afa0235c873b1a3f5`. The memo is `theory/RECORD_RATIO_CONSISTENCY_2026-11-24.md`. This file is the review. It does not edit the memo, `THEORY.md`, `OPEN_WORK.md`, or `theory/README.md`.*

## Result

No HIGH finding. No MEDIUM finding. Two LOW findings, both line pins. The four readings do what the memo says. None forces \(\kappa_D/\kappa=1\). The strengthened readings of Routes A and B fix the endpoint \(\kappa_D=0\). Route C stops on a published entropy bound. The ledger identity in Route D holds for this rank-1 measurement, and the identity leaves the price ratio free.

## What was run

Fresh clone of `forge-record-ratio-consistency` at `f795666`, with `origin/main` fetched at `0f3791890078161a1172277162df5ac13ebbff46` (the main the memo names). `python` is not on `PATH` in this environment (`command not found`). The checker's own usage line is `python3`.

- `python3 tools/check_consistency.py` on that clone. Exit 0. `RESULT: PASS`. Wording FAILs 0 on 31 maintained docs. Process-rule FAILs 0. Core-rule FAILs 0. `THEORY.md` main text is present: `## Appendix A.` is at `THEORY.md:201`, and the checker counts 11325 words before it (advisory length warning, same class as the README warning; both are soft). CLAIM_MAP tally 392. The freshness check passes: STATUS's stated main `d592662` sits inside the first-parent window of `origin/main`. The same command, run again on the tree that contains this review, exits 0 with the same counts.
- `python3 -m pytest -q tools` on that clone. **285 passed, 1 skipped**, 376.37 s, exit 0. The skip is `tools/test_lean.py:124`, `Lean 4 / lake is not installed`.
- A root `python3 -m pytest` also collects `reviews/night2/CAUSAL_NULL_INVARIANCE/run_test.py`. That file has no `def test_`. Importing it runs a locked historical simulation. Collection stopped with exit 2 because `numba` was absent. That file is on `main` and is outside the maintained suite. It was left un-run, so the locked script did not write `test_result.json`.
- Throwaway stdlib script, not committed, run once with `python3`. It recomputed the channel, the closed form, the loss, a non-antipodal ensemble, a rank-2 instrument, and three candidate reverse maps. The numbers below are from that script.

`git grep -n -i -E 'κ_D|kappa_D|Reeb' 0f37918 -- '*.md'` returns no hit. The no-arbitrage hits on that main are the market sentence at `theory/INTERNAL_MODEL.md:66` and the same sentence in `history/2026-11-18_CURRENT_BRIEF.md:125`, `reference/THEORY_v1.4.29.md:152`, and `theory/INTERNAL_MODEL.md:245`.

## LOW

**L1. The closed-contour sentence is `theory/REPRESENTATION.md:108`.** The memo at line 128 cites `:102` for "Debreu's continuity is closed contour sets in that product topology." Line 102 opens proof step 2, Debreu's additive representation. The sentence "Continuity in the citation is closed upper and lower contour sets in the product topology" is line 108. A1 at `theory/REPRESENTATION.md:43`, which the memo also cites, states the closed contour sets of the preorder. Route B's reading of A1 is the reading on line 43 and line 108. The pin is the defect.

**L2. `MEMO.md:34` at `e584d8b` is the cost-gap display.** The memo at line 78 cites `MEMO.md:34` and `MEMO.md:68` for the claim that draft #252 keeps the final classical outcome, with the unmeasured quantum record set aside. Line 68 does say that an unmeasured record is a separate question. Line 34 is the display \(J_D(\theta)-J_D(0)=P_D(\theta)+w(L(\theta)-L(0))\). The kept-record sentence on that head is `MEMO.md:9` and `MEMO.md:56` ("The record kept here is \(M\)"), and `PREREG.md:34` ("The record kept is the classical outcome \(M\)"). The modeling assumption Route A uses is in those lines. The `:34` pin does not contain it.

A third pin is one line off and does not get its own finding. The memo at line 94 says the stake observable is a function of \(W\) at `PREREG.md:55-56`. Those lines are the loss display \(L=\mathbb{E}[(y-\hat a(M))^2]\). The target \(y_W=r\,n_A\cdot u_W\) is the previous line, `PREREG.md:54`. The same-channel loss identity uses that target, and the identity holds (below).

## Route A. No-arbitrage

The BSC crossover is right. For \(\varepsilon=(1-\cos\theta)/2\),

\[
(1-\varepsilon)\frac{1+z}{2}+\varepsilon\frac{1-z}{2}=\frac{1+z\cos\theta}{2},
\]

because \(1-2\varepsilon=\cos\theta\). On a grid of \(z\in\{0,\pm 0.2,\pm 0.6,\pm 1,0.999\}\) and \(\theta\) every degree from 0 to 90, the absolute error is at most \(2.22\times 10^{-16}\). Applied to the four labels after complete dephasing, the garbling reproduces \(P(M\mid W)\) of the direct \(\theta\)-measurement. For \(r\in(0,1)\) and \(\theta\in[0,\pi/2]\), \(P(M=+1\mid +z)=(1+r\cos\theta)/2\) recovers \(\theta\). The script's recovery error is at most \(8.1\times 10^{-15}\).

The closed form at `PREREG.md:68-69` matches an explicit average over the four post-dephasing states, \(r=0.6\), all 721 angles in \([0,\pi/2]\). Max absolute error on \(P_D\) and on \(P_\chi\) is \(5.55\times 10^{-17}\). \(P_D(0)=0\). \(P_\chi(0)=0.096372378511\), the value printed at `MEMO.md:42` on `e584d8b`. \(P(M=+1)=1/2\) and \(H(M)=\ln 2\) at every angle, which is ERRATA E2. \(P_\chi(0)-P_\chi(\theta)=P_D(\theta)\) to \(1.11\times 10^{-16}\). \(P_D(\theta)>0\) on \((0,\pi/2]\).

The loss match is the whole channel. Direct measurement and pointer-plus-BSC give the same mean squared error at \(\phi\in\{0,\pi/4,\pi/2,1\}\), every 5 degrees of \(\theta\), and both match the closed form \(L=r^2/2-r^4\cos^2\phi\cos^2\theta/4\) at `PREREG.md:70`. Max absolute error \(5.55\times 10^{-17}\). The match is the joint law of \((W,M)\). It holds at every \(\phi\), including the complementary angle where \(L\) is already flat.

The gap algebra is the one in the memo. With the final stock priced, the direct record cost is \(\kappa P_\chi(\theta)+\kappa_D P_D(\theta)\) and the garbling cost is \(\kappa P_\chi(\theta)\). The difference is \(\kappa_D P_D(\theta)\). It is zero at every \(\theta\) exactly when \(\kappa_D=0\). At ratio 1 the direct cost equals \(\kappa c\) with \(c=P_\chi(0)\), the garbling cost equals \(\kappa(c-P_D(\theta))\), and the gap equals \(\kappa P_D(\theta)\). Checked at \(\theta\in\{0.3,\pi/4,\pi/2\}\) with \(\kappa=\kappa_D=1\): gaps \(0.009012\), \(0.049915\), \(0.096372\).

The one-way claim survives three reverse attempts.

- Re-preparation of the Lüders state does nothing. A rank-1 projective measurement leaves \(|m\rangle\langle m|\). Preparing \(|m\rangle\) from the outcome is that same state. The pinch entropy is still there.
- The Petz recovery of complete \(z\)-dephasing, relative to the maximally mixed state, is the dephasing map. An equatorial pure state has fidelity \(1/2\) with its dephased state. Coherence does not come back.
- Keeping the BSC noise bits does not lower the stock. For the \(\pm z\) pair at \(r=0.6\) and \(\theta=\pi/3\), \(I(W;M_{\mathrm{pointer}})=I(W;M_{\mathrm{garbled}},\mathrm{noise})=0.192745\). A reversible garbling holds the pointer information. The cheap path is the one that discards the noise. Data processing blocks the return.

The charge that would force ratio 1 is the one the memo names at lines 108–109: \(\kappa\) per nat destroyed by the garbling, added on top of the final stock. Destroyed information on this ensemble equals \(P_D(\theta)\). The garbling cost becomes \(\kappa P_\chi(\theta)+\kappa P_D(\theta)=\kappa c\), the direct cost is \(\kappa c+(\kappa_D-\kappa)P_D(\theta)\), and the gap is \((\kappa_D-\kappa)P_D(\theta)\). That gap is zero for every \(\theta\) exactly at ratio 1. The same algebra is peak-stock pricing, because the pointer stock plus the nats the garbling destroys is the peak. R1 prices the gross stock that is held (`theory/REPRESENTATION.md:60`, \(I_{\mathrm{mem}}=I(M_t;X^t)\)). It does not add a second charge for destroying it. Landauer and the learning-rate papers are floors at `theory/REPRESENTATION.md:120`. The memo's disappearance paragraph (lines 114–115) already withdraws the gap if post-processing is priced as something other than the final stock. That route is named, and it is outside A1–A8.

The dephasing paragraph at memo line 110 is right and is two different labels. Each \(\pm x\) state goes from entropy \(h((1+r)/2)\) to \(\ln 2\). Weight \(1/2\), so the mean increase is \(\tfrac12(\ln 2-h((1+r)/2))=P_\chi(0)\). Splitting \(W\) into a pair bit and a sign bit, \(I(\mathrm{pair};M)=0\) at the pointer (both pairs are unbiased), and \(I(\mathrm{sign};M\mid\mathrm{pair})\) is entirely the \(z\) pair: \(\tfrac12(\ln 2-h((1+r)/2))\). The equal numbers are the equal weights. Measuring at the pointer does not turn the \(\pm x\) entropy into the \(\pm z\) mutual information.

No cycle, and no ratio other than the disclosed destruction charge, came out of these attempts. Route A's **PROVED (in-model)** status matches the menu it states.

## Route B. Coarse-graining continuity

At \(\theta=0\), \(P_D=0\), so \(\kappa P_\chi(0)+\kappa_D P_D(0)\) equals \(\kappa P_\chi(0)\) at every \(\kappa_D\ge 0\). Matching R1 at the pointer leaves the ratio free.

Off the pointer the state is \(z\)-diagonal and \(P_D(\theta)>0\). The two-term cost exceeds \(\kappa I(W;M)\) by \(\kappa_D P_D(\theta)\). Equality at every \(\theta\in(0,\pi/2]\) holds exactly when \(\kappa_D=0\). At ratio 1 the excess is \(\kappa P_D(\theta)\). Continuity in \(\theta\) makes both the two-term cost and the R1 price continuous. They agree at \(\theta=0\) for every ratio. Agreement on the whole interval is a further demand, and that demand fixes 0.

A1 is the continuous preorder on the product of resource coordinates (`theory/REPRESENTATION.md:43`), with Debreu's closed contour sets in that product topology (`theory/REPRESENTATION.md:108`). The decoherence parameter is not one of those coordinates. Nothing in A1 equates the two record prices. Route B does not force ratio 1.

## Route C. Reeb and Wolf 2014

Crossref, fetched 24 November 2026, DOI `10.1088/1367-2630/16/10/103011`. Title "An improved Landauer principle with finite-size corrections." Authors David Reeb and Michael M. Wolf. Container *New Journal of Physics*, volume 16, page 103011. `issued` and `published-online` are 8 October 2014. The arXiv record `1306.4352v3` (11 October 2014) is marked "published version" and carries journal reference *New J. Phys.* 16 (2014) 103011, with the same DOI. The text below is `ar5iv.labs.arxiv.org/html/1306.4352v3`.

- Section 2.3, equation (13): \(S(\rho):=-\mathrm{tr}[\rho\log\rho]\), natural log, nats.
- Theorem 3, equation (22): \(\beta\Delta Q=\Delta S+I(S':R')+D(\rho'_R\|\rho_R)\), for a unitary on a product of the system and an initially thermal reservoir. The bound \(\beta\Delta Q\ge\Delta S\) is what remains after the mutual information and the relative entropy are dropped. The proof says so in the last line.
- Corollary 4: equality in \(\beta\Delta Q\ge\Delta S\) holds if and only if the final state is a product, the system map is unitary, and the reservoir is untouched. Equivalently \(\Delta S=\Delta Q=0\). The paper's own gloss: a process with nonzero entropy decrease sits strictly above the bound.
- Section 5.2, "A Landauer Principle for correlations rather than entropies?": the entropy is the information in the system; \(I(S:M)\) is the information an agent has about the system. A swap against a reservoir of the same size, with \(\rho_R=\rho_S\) thermal at \(\beta=1\), gives \(\beta\Delta Q=0\) and \(\Delta I=I(S:M)\), so \(\beta\Delta Q\ge\Delta I\) fails whenever \(I(S:M)>0\), including perfect knowledge of a non-pure state. A reversed inequality \(\beta\Delta Q\le\Delta I\) fails as well (the paragraph after equation (64)). "Other tentative notions of a Landauer Principle for correlations can be dismissed similarly." Complete erasure in their sense (65) is a swap and "does not require any heat dissipation."

The paper bounds an entropy decrease. \(P_D\) is an entropy increase under a pinch. \(I(W;M)\) is a mutual information, and section 5.2 is an obstruction to moving the bound onto that change. Equality in the bound is the trivial process. No value of \(\kappa_D/\kappa\) is in the paper. The **KNOWN** stop is the right status. The Landauer DOI `10.1147/rd.53.0183` is the one already printed at `theory/REPRESENTATION.md:120` and again at `:360`. The memo adds no page.

The Crossref query in the memo reproduces. `query=Fundamental energy cost for quantum measurement` with `query.author=Reeb` returns `total-results` 41. The first 20 titles contain no paper of that title. (A `query.bibliographic` variant returned 37. The count 41 is the free-query form.) Item 12 of that first page is the Landauer paper above, which is a different title.

## Route D. The ledger identity

For a rank-1 projective measurement and a conditional state \(\rho_W\), the post-measurement state is diagonal with eigenvalues \(p(m\mid\rho_W)\), so \(S(\Phi(\rho_W))=H(M\mid W=w)\). Then

\[
I(W;M)=H(M)-\mathbb{E}[S(\Phi)],\qquad D(\rho\|\Phi(\rho))=S(\Phi(\rho))-S(\rho),
\]

and the sum is \(H(M)-\mathbb{E}[S(\rho)]\). The relative-entropy step is the pinching identity: \(\log\Phi(\rho)\) is diagonal in the measurement basis, so \(\mathrm{tr}(\rho\log\Phi)=\mathrm{tr}(\Phi\log\Phi)\). `PREREG.md:30-31` at `e584d8b` states the equality. On a grid of qubit states and angles the absolute gap between \(D(\rho\|\Phi)\) and \(S(\Phi)-S(\rho)\) is 0. On the antipodal ensemble the identity holds to \(1.11\times 10^{-16}\), and the right-hand side is constant because \(H(M)=\ln 2\).

The identity is wider than the four-label ensemble and narrower than an arbitrary instrument.

- It holds off the antipodal ensemble. Equal mixture of post-dephasing \(+z\) and \(+x\) at \(r=0.6\): the identity error is at most \(1.11\times 10^{-16}\) at \(\theta\in\{0,0.4,\pi/2\}\), while \(H(M)\) runs \(0.647447\), \(0.654470\), \(0.693147\). At ratio 1 the record cost is that \(H(M)-\mathbb{E}[S(\rho)]\), so it runs \(0.050672\), \(0.057695\), \(0.096372\). Ratio 1 does not flatten this ensemble. No single ratio flattens it either: the ratio that levels \(\theta=0\) against \(0.4\) is \(0.549\), and the ratio that levels \(\theta=0\) against \(\pi/2\) is \(0.526\). Flatness at ratio 1 is special to the fair antipodal ensemble, as the memo says at lines 64 and 171. `MEMO.md:70` poses that off-ensemble question and points at `PREREG_2.md`. The sentence that the sum depends on \(\theta\) is `PREREG_2.md:13` and `:21`. The identity section of this memo already proves the right-hand side moves when \(H(M)\) moves.
- It fails for a higher-rank Lüders instrument with leftover entropy. Qutrit projectors \(|0\rangle\langle 0|\) and \(|1\rangle\langle 1|+|2\rangle\langle 2|\), state \(\mathrm{diag}(1/2,1/4,1/4)\). Then \(P_D=0\), \(I(W;M)=0\), \(H(M)=\ln 2\), \(S(\rho)=\tfrac32\ln 2\), and the two sides differ by \(\tfrac12\ln 2\approx 0.346574\). The rank-1 scope is load-bearing for the mutual-information half.
- Rank-1 is a sufficient condition the proof uses. A rank-2 block whose conditional state is pure has residual entropy 0, and the same arithmetic goes through. The memo's sentence at line 177 ("uses only that a rank-1 projective measurement leaves a diagonal state whose entropy is the outcome entropy") describes the hypothesis of this proof. The qubit measurement in draft #252 is rank-1 (`PREREG.md:52`).

A5 (`theory/REPRESENTATION.md:53-56`) adds costs over successive durations and over independent copies. A measurement followed by a garbling is one record and then a degradation of it. The Cauchy step (`:110`; line 111 is blank) makes each concatenating coordinate linear. Line 120 says the ratios inside the sum are the preorder's marginal rates. Line 177 fixes the price vector up to one common scale. None of those sentences sets \(\kappa_D=\kappa\). The coefficient 1 in \(I+P_D=H(M)-\mathbb{E}[S(\rho)]\) is the chain rule. The record cost at a general ratio differs from \(\kappa\) times that balance by \((\kappa_D-\kappa)P_D\), which is memo line 69. The identity says the difference has that form. It does not set the difference to zero.

T74 at `1fb7b5b` matches the citations. Five routes are listed (Route 1, A, B, C, and Route 5). Route 5 and ERRATA E1 separate the shared coefficient, which sets ratio 1 and keeps both terms, from the refusal of the second coefficient, which is the endpoint 0. Flatness on the antipodal ensemble forces ratio 1, and E1 says that condition is outside A1–A8. The constants note on `forge-constants-exchange-rates` (`theory/constants-exchange-2026-11-24/MEMO.md:5` and the T70 row) asks whether \(k_B\) and \(\hbar\) enter as unit conversions once an energy and a time are given. That is a different ratio.

## Citation audit

Pins on this main (`0f37918`, unchanged by the commit except the three added files):

| Pin | What is there | Check |
|---|---|---|
| `CORE.md:169` | PROVED, KNOWN, OPEN, and a puzzle as a miss with a diagnosis and a next test | Holds | <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->
| `CORE.md:52` | R1 does not choose the coordinate list; the named coordinate is mutual information; A8 makes prices nonnegative | Holds |
| `theory/REPRESENTATION.md:43` | A1, closed contour sets on the product of resource coordinates | Holds |
| `theory/REPRESENTATION.md:53-56` | A5, additivity over durations and over independent copies | Holds |
| `theory/REPRESENTATION.md:58-60` | A6, Shannon mutual information; the gross stock \(I_{\mathrm{mem}}\) is on line 60 | Holds |
| `theory/REPRESENTATION.md:102` | Opening of the Debreu step | **L1.** The contour sentence is `:108` |
| `theory/REPRESENTATION.md:110-111` | Cauchy linearity on line 110; line 111 is blank | Holds |
| `theory/REPRESENTATION.md:114` | The memory coordinate is Shannon mutual information in nats | Holds |
| `theory/REPRESENTATION.md:120` | Price ratios from the Cauchy equation; Landauer doi `10.1147/rd.53.0183` is a floor and does not produce the sum | Holds |
| `theory/REPRESENTATION.md:177` | "R1 fixes a price vector up to one common scale." | Holds |
| `THEORY.md:36` | Floors on prices, and the exchange-rate clause is between systems | Holds |
| `theory/SELECTION_AXIOMS.md:23` | A design that cannot cover \(J\) shrinks; the note uses \(J\) as already defined | Holds |
| `theory/INTERNAL_MODEL.md:66` | Market no-arbitrage: blind persistence in an efficient environment requires information | Holds |

Pins on `e584d8b` (`forge-pointer-basis-stakes`):

| Pin | What is there | Check |
|---|---|---|
| `PREREG.md:28-34` | \(P_D=\mathbb{E}[D(\rho\|\Phi_\theta(\rho))]=\mathbb{E}[S(\Phi)-S(\rho)]\); line 34 starts \(P_\chi=I(W;M_\theta)\) | Holds |
| `PREREG.md:36` | Ruin is slack | Holds |
| `PREREG.md:55-56` | The loss display | One line off; the target \(y_W\) is `:54`. The loss identity holds |
| `PREREG.md:64-72` | Closed form; \(P_D\) increases with \(\lvert\theta\rvert\) | Holds. Recomputed above |
| `PREREG.md` §2, line 44 | \(\gamma=0\) is complete dephasing, the sieve's long-time limit | Holds |
| `MEMO.md:34` | The \(J_D\) gap display | **L2** |
| `MEMO.md:58-62` | \(P_D+P_\chi=\ln 2-\mathbb{E}[S(\rho)]\), independent of \(\theta\) | Holds |
| `MEMO.md:64-68` | \(J=\kappa I(W;M)+\kappa_D P_D+w L\); at \(\kappa_D=\kappa\) the stake alone sets \(\theta\); unmeasured record set aside | Holds |
| `MEMO.md:68` | Same paragraph, the flat-ratio sentence and the unmeasured-record sentence | Holds |
| `MEMO.md:70` | The off-ensemble question, locked unscored in `PREREG_2.md` | Holds as a pointer. The dependence itself is `PREREG_2.md:13`, `:21`, and this memo's identity |
| `MEMO.md` ERRATA E2, line 86 | \(P(M=+1)=1/2\) at every \(\theta\) | Holds. Recomputed |
| `PREREG_2.md` | Locked, and the header says it is committed before any scoring script | Holds |

`theory/QUANTUM_RECORD_PRICE_2026-11-24.md` at `1fb7b5b`: Route 5 is lines 133–151, ERRATA E1 is lines 172–180. Both separate ratio 1 from the endpoint 0.

## Wording

Scanned the memo, the new T75 row in `OPEN_WORK.md`, and the new row in `theory/README.md`.

- No "theory of everything." The memo header, the T75 row, and `theory/README.md:50` say the note derives neither general relativity, nor quantum mechanics, nor holography. `THEORY.md` is not in the diff. The hypothesis sentence at `THEORY.md:41` is untouched.
- No "law" in the new prose. The maintained-doc checker reports wording FAILs 0.
- No "solved." No "bill." The word used for the objective is "cost."
- No "kill" and no "verdict" in the new prose. The literature-search sentence at memo line 189 calls a missing title a miss and says that miss is not a claim that no such paper exists. Route D and the closing section are labeled **Puzzle**. The off-ensemble angle question is labeled **OPEN**, with the next test named as the unscored lock in `PREREG_2.md`. <!-- banned-ok: review record; quotes the memo wording at the reviewed head -->
- Model implications are labeled, at memo lines 116, 134, and 171, each conditional on the demand that would be added.
- In-model claims are labeled **PROVED (in-model)** or **ELEMENTARY**. The Reeb and Wolf reading is labeled **KNOWN**. The Crossref lookups are dated 24 November 2026. `ELEMENTARY` is not one of the status words at `CORE.md:169`. It is used for three algebraic steps (memo lines 64, 86, and 110), the same way T74 uses it, and the route statuses themselves are words from that list. Left as an observation.
- No personal information about Chad in the new prose.

The T75 row and `theory/README.md:50` match the memo: self-check, four readings, ratio 1 unforced, endpoint 0 only under the strengthened demands, Landauer stopped, ledger identity not a derivation.

## Conclusion

Routes A and B, under the demands that make them fix a number, fix \(\kappa_D=0\). Route C publishes an entropy bound and an obstruction to moving that bound onto mutual information, and it stops. Route D proves \(I(W;M)+P_D=H(M)-\mathbb{E}[S(\rho)]\) for this rank-1 measurement and shows that the chain-rule coefficient is not a price. The destruction charge that would force ratio 1 is named in the memo and is outside R1. L1 and L2 are line pins. They do not move a route.
