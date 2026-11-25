# Quantum record price: five routes, none names it

*24 November 2026 (UTC). Desk note. No script. Self-check through the third pass; the ERRATA answers the independent review at `theory/reviews/QUANTUM_RECORD_PRICE_REVIEW_2026-11-24.md` (commit `1e2f7f5`). `THEORY.md` is unchanged. Open-work row T74. Status words are those at `CORE.md:169`. Nothing here derives general relativity, quantum mechanics, or holography.*

*Each route below states what it assumes, where it stops, and a status label. A route that would name a price only by adopting a known entropy theorem is marked KNOWN and is not counted as a derivation.*

## Answer

No unique quantum-record price. Five routes, each a different question. One concrete form, from draft #252 at head `e584d8b` (`theory/pointer-basis-stakes-2026-11-24/MEMO.md:64-68`), is what fixes the ratio \(\kappa_D/\kappa\) in

\[
J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L,
\]

or why nothing does. Both coefficients are nonnegative, \(P_D\) is the relative entropy to the pinched state, and \(I(W;M)\) is the mutual information of the classical outcome. The two prices scored on that branch are the endpoints of the ratio, \(0\) and \(\infty\). Routes 1 through 4 do not fix the ratio. On this antipodal ensemble, requiring the record cost to be independent of the record angle does fix it at 1 (Route 5). That condition is not in A1–A8.

- **Route 1** stops at A6's naming step. It does not fix \(\kappa_D/\kappa\). **PROVED (in-model).**
- **Route 2** (minimum over admissible prices) stops on a tie, including a tie of the two endpoints and a tie with the zero price A8 allows. It does not fix \(\kappa_D/\kappa\). **PROVED (in-model).**
- **Route 3** (selection under the ruin cap) has two readings. If the cap does not depend on the price, it removes nothing. If a reserve must cover the named \(J\), a reserve between the two minima keeps the pinch and drops mutual information, and still ties the pinch with charging nothing. Neither reading fixes an interior ratio. **PROVED (in-model).**
- **Route 4** (R1's axioms on a GPT state space) is closed as a **KNOWN** stop. Measurement entropy and mixing entropy coincide in quantum theory with no extra assumption there, and they differ on a general probabilistic theory. Adopting von Neumann entropy or Umegaki relative entropy is also **KNOWN**, and it still does not choose the record contraction or the ratio.
- **Route 5** (one scale on both record terms) does not force \(\kappa_D/\kappa=1\). The one-scale sentence multiplies the whole sum. It does not equate the coefficients. **Open question.** The missing sentence is named in that section.

## Where a quantum price is already assumed

On the main this note was first written against (`0f37918`), and still true after the merge of `04e9e5b`:

- `CORE.md:52` and `theory/REPRESENTATION.md:58` name the memory coordinate as Shannon mutual information, or the Gelfand–Yaglom–Dobrushin supremum when that mutual information is finite. Both are classical. `theory/REPRESENTATION.md:60` says the Aczél–Forte–Ng uniqueness is not extended to differential entropy.
- `theory/DIRECTIONS_2026-11-22.md:58` parks a conjecture that the frontier carries over with a Holevo bound, quantum channel capacities, and a quantum Landauer cost, with a different price on copying. That sentence assumes those floors. It does not derive which functional the record pays. The file says its references are to be checked before any canonical use, so they are not cited here.
- `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:114` is the two-dimensional quantum bullet. The three-dimensional repair heat is left open at `:115` and `:174`, and at `theory/PHYSICS_CHAIN_2026-11-23.md:18`. Those lines do not choose among mutual information, a pinch divergence, and dimension.

Brought in by the merge of `04e9e5b` (upstream PR #252, locked head `e584d8b`):

- The locked preregistration is unchanged: A6 does not fix a quantum price (`theory/pointer-basis-stakes-2026-11-24/PREREG.md:24`), the pinch score is \(P_D=\mathbb{E}[D(\rho\|\Phi_\theta(\rho))]\) (`PREREG.md:28`), \(P_\chi=I(W;M_\theta)\) is the Shannon mutual information of the classical outcome (`PREREG.md:34`), and ruin is slack (`PREREG.md:36`). The memo writes both terms (`MEMO.md:64-68`). The open number there is \(\kappa_D/\kappa\). This ratio is the one in that T73 memo. It is not the constants question in T70.

Still off this branch:

- Draft PR #253, head `fd69ec3`. `theory/COMPOSITE_CONTEST_2026-11-24.md:46` names the choice of headline price and does not make it. `:56` sets that price to \(\lambda\ln K_{AB}\). On a protocol whose settings are drawn after the record, the A6 coordinate is 0 for every contestant (`:56`, `:96`, `:154`). Mutual information and the dimension price rank one control in opposite directions (`:154`).

DOIs below were resolved on the Crossref API on 24 November 2026. Title, authors, and pages match. A DOI is printed only in that case.

## The ratio

Draft #252 at `e584d8b` states the cost with both record terms named (`MEMO.md:64-68`). On its antipodal ensemble, \(P_D(\theta)+P_\chi(\theta)\) does not depend on \(\theta\) (`MEMO.md:58-62`). Call that constant \(c\). The closed form at `PREREG.md:64` gives \(P_D(0)=0\) and \(P_\chi(\pi/2)=0\), so \(c=P_\chi(0)=P_D(\pi/2)\). For Bloch radius \(r\in(0,1)\), \(h((1+r)/2)<\ln 2\), so \(c>0\). **ELEMENTARY** from that closed form and their identity. No new grid.

A ratio needs a scale. On the simplex \(\kappa+\kappa_D=1\) with both coefficients nonnegative, write \(t=\kappa_D\). Then \(t=0\) is mutual information and \(t=1\) is the pinch, and

\[
(1-t)P_\chi+t\,P_D=(1-t)\,c+(2t-1)\,P_D.
\]

The record part vanishes at an endpoint of \(\theta\) only. At \(\theta=0\) it equals \((1-t)c\), which is 0 only at \(t=1\). At \(\theta=\pi/2\) it equals \(tc\), which is 0 only at \(t=0\). For \(t\in(0,1)\) both prices are positive on the open interval of \(\theta\), and each endpoint still carries the other price, so the record part is positive at every \(\theta\).

**PROVED (in-model).** Three comparisons, using \(L(\theta)-L(0)=(r^4\cos^2\phi/4)\sin^2\theta\ge 0\) from the same closed form.

- At stake 0 both endpoints attain cost 0. Every interior \(t\) attains \(c\cdot\min(t,1-t)>0\). The minimum ties the two scored endpoints.
- When \(\cos\phi=0\), the loss does not depend on \(\theta\). Both endpoints attain \(wL\) at every \(w\ge 0\), and every interior \(t\) pays a positive record part on top. The tie holds at every stake.
- When \(w>0\) and \(\cos\phi\neq 0\), the pure pinch attains \(w L(0)\) at \(\theta=0\). The cost of pure mutual information at \(\theta=\pi/2\) is \(w L(\pi/2)\). That number is the minimum only while the minimizer stays at \(\pi/2\). Draft #252 already separates the two (`MEMO.md:42-46`): at \(r=0.6\) and \(\phi=0\), the unique \(\theta=0\) minimizer of \(P_\chi\) starts at \(w_\star=3.209014724815\). Checked from the closed form at the locked point \(r=0.6\), \(\phi=0\), \(w=10\). With \(r=3/5\), \(L(0)=r^2/2-r^4/4=0.1476\) and \(L(\pi/2)=r^2/2=0.18\), so \(w L(0)=1.476\) and \(w L(\pi/2)=1.800\). And \(P_\chi(0)=\tfrac12[\ln 2-h(4/5)]\), with \(h(4/5)=- (4/5)\ln(4/5)-(1/5)\ln(1/5)\), equals \(0.096372378511\), so the pure-MI cost at \(\theta=0\) is \(1.572372\) at six decimals. That is the minimum at this point, and it is lower than \(1.800\) by \(0.227628\) at those decimals. The pinch stays the unique minimizer on the simplex: \(P_\chi\) and \(L-L(0)\) are nonnegative and are never zero at the same \(\theta\), and every interior \(t\) pays a positive record part at every \(\theta\), so every rival sits strictly above \(w L(0)\).

The flat ratio \(t=1/2\) is \(\kappa_D=\kappa\). One scale on both terms keeps both terms and sets this ratio. Its record part equals \(c/2\) at every \(\theta\). At stake 0 that is strictly above both endpoints, so the minimum does not select it. Flatness does: the record cost is independent of \(\theta\) exactly when the ratio is 1 (Route 5).

Without the simplex, the A8 orthant allows every pair with \(\kappa=0\). Each of them attains \(w L(0)\) at \(\theta=0\), because \(P_D(0)=0\). The pair \((0,0)\) leaves the ratio undefined. Every pair \((0,\kappa_D)\) with \(\kappa_D>0\) is the endpoint \(\infty\). Those pairs tie. The endpoint \(0\), which is \(\kappa_D=0\) with \(\kappa>0\), ties that cost when \(w=0\) or \(\cos\phi=0\), and is strictly dearer when \(w>0\) and \(\cos\phi\neq 0\). Any pair with both coefficients positive is strictly dearer at the minimum.

## Route 1. The representation minimum

**Route.** Ask whether the minimum of a cost under A1–A8, subject to the ruin cap, names one quantum-record functional, in the way R1 names the classical memory coordinate.

**Assumes.** A1–A8 as stated in `theory/REPRESENTATION.md:39-64`. The ruin cap is the feasible-set restriction in A2.

**Where it stops.** A6 names the coordinate before any minimum is taken. The minimum then returns a design, not a functional.

**Status. PROVED (in-model).** Under A1–A7, on at least three essential intervals, a continuous cost is \(C=a\sum_i p_i z_i+b\) with one \(a>0\) (`theory/REPRESENTATION.md:84-92`). Step 4 puts Shannon mutual information, in A6's scope, into the memory slot (`:114`). `CORE.md:52` says R1 does not choose the coordinate list. On a menu that does not depend on the numerical cost, \(C\mapsto aC+b\) preserves the argmin (`theory/REPRESENTATION.md:126`). Theorem S3 (`CORE.md:48`) runs the other way: on a convex feasible set, an undominated design is a minimizer at some nonzero nonnegative prices. A6's input is a finite alphabet, or a pair of classical random variables on standard Borel spaces with finite mutual information (`theory/REPRESENTATION.md:58-60`). A state on a Hilbert space is not that pair, so A6 does not fill the memory slot. The Cauchy step (`theory/REPRESENTATION.md:110-111`) makes a concatenating interval coordinate linear once that coordinate is in the sum. It does not choose which additive functional is placed there. A8 only signs a coefficient already in the sum (`:64`). The ruin cap is not produced by the representation (`:96`).

The candidates are not one coordinate up to \(a>0\). On one fixed classical alphabet, a non-degenerate perfect copy has \(I(W;M)>0\) and a pinch in that basis has \(D(\rho\|\Phi(\rho))=0\). An independent record has both equal to 0. No \(a>0\) carries one pair of values onto the other. Dimension \(\lambda\ln K\) is constant on that menu and is not essential (`theory/REPRESENTATION.md:80`, Lemma M). The Holevo quantity of an already classical outcome equals \(I(W;M)\). **ELEMENTARY**, from \(S(\rho)=-\mathrm{Tr}\,\rho\ln\rho\) on a diagonal state. That is A6's coordinate. The pre-measurement Holevo quantity is a different functional, and draft #252 does not use it (`PREREG.md:34`).

**Ratio.** This route does not fix \(\kappa_D/\kappa\). A6 names \(I(W;M)\) and does not name \(P_D\), so \(\kappa_D\) is not a coefficient in the sum. R1 fixes the prices of coordinates already on the list up to one common scale (`theory/REPRESENTATION.md:118`, `:177`). The sentence is `:177`. `:176` is the blank line above it. Class L is `:184`. The representation reports a ratio the preorder already carries. It does not derive the number, and it does not put the second coordinate on the list.

## Route 2. Minimum over admissible prices

**Route.** Treat the price functional as chosen with the design. Minimize the cost over the set of admissible quantum record prices, and over the record.

**Assumes.** The cost at a named price \(P\) and a record \(x\) is \(J(P,x)=P(x)+w L(x)\), with \(w\ge 0\) and \(L\) the decision loss. "Admissible" is either every nonnegative functional (the A8 orthant, `theory/REPRESENTATION.md:120`) or the two-element menu \(\{P_D,P_\chi\}\) from draft #252. The comparison that uses that menu takes the locked complete-dephasing form (`PREREG.md:64`): for Bloch radius \(r\in(0,1)\) and angle \(\theta\in[0,\pi/2]\),

\[
P_D(\theta)=\tfrac12\Big[h\Big(\tfrac{1+r|\cos\theta|}{2}\Big)-h\Big(\tfrac{1+r}{2}\Big)\Big],\qquad
P_\chi(\theta)=\tfrac12\Big[\ln 2-h\Big(\tfrac{1+r|\cos\theta|}{2}\Big)\Big],
\]

\[
L(\theta)=\tfrac{r^2}{2}-\tfrac{r^4\cos^2\phi\,\cos^2\theta}{4},
\]

with \(h\) the binary entropy in nats. No new grid is run. The monotonicity used below is the derivative \(h'(p)=\ln((1-p)/p)\), which is negative for \(p>1/2\) and zero only at \(p=1/2\). **ELEMENTARY.**

**Where it stops.** The minimum is not a single price.

**Status. PROVED (in-model).** Three stops, in order.

1. **The support function takes the prices as given.** Theorem S2 (`CORE.md:48`) says the minimum cost is the support function of the feasible set. The argument of a support function is a price vector in a coordinate space that has already been named. Changing the coordinates changes the argument. The minimum does not choose the coordinates.

2. **The A8 orthant minimizes at zero, tied with anything that vanishes.** A8 makes each concatenating coordinate a bad (`theory/REPRESENTATION.md:64`). Under A8 the price on that coordinate is nonnegative (`:92`), and a coordinate that is not essential has price zero (`:80`, Lemma M). The zero functional meets both. At stake \(w\), it scores \(w\min L\) on a loss-minimizing record. Any admissible price that is zero on that same record scores the same number. On the menu of stop 3 the pinch is zero at the loss minimizer, so its minimized cost equals the zero price at every stake. The copy-versus-noise pair in Route 1 shows that this pinch is not \(I(W;M)\). The minimum therefore does not separate "charge the pinch" from "charge nothing." Charging nothing is not a quantum record price.

3. **On the hand-listed menu the minimum ties on a large set.** Restrict, by hand, to \(\{P_D,P_\chi\}\) and the closed form above. Then \(P_D(0)=0\), \(P_D(\theta)>0\) for \(\theta\in(0,\pi/2]\), and \(P_\chi(\pi/2)=0\), \(P_\chi(\theta)>0\) otherwise. Also \(L(\theta)-L(0)=(r^4\cos^2\phi/4)\sin^2\theta\ge 0\). Hence \(\min_\theta J(P_D,\cdot)=w L(0)\), attained at \(\theta=0\). And \(\min_\theta J(P_\chi,\cdot)=w L(0)\) if and only if \(w=0\) or \(\cos\phi=0\), because equality needs \(P_\chi(\theta)=0\) and \(L(\theta)=L(0)\) together, which is \(\theta=\pi/2\) and \(\cos\phi=0\) when \(w>0\). So at stake 0, and for every stake when the observable is fully complementary, both prices attain the same minimum. The price is not unique. When \(w>0\) and \(\cos\phi\neq 0\), this two-element menu does pick \(P_D\). That pick is a fact about a menu that excluded the zero price. Stop 2 puts the zero price back, and the pick ties again.

**Ratio.** This route does not fix \(\kappa_D/\kappa\). On the simplex the minimum ties the endpoints \(0\) and \(\infty\) at stake 0 and at every stake when the observable is fully complementary. On the part of the menu where \(w>0\) and \(\cos\phi\neq 0\), the simplex picks the pure pinch. That pick excludes the zero functional. On the A8 orthant every pair with \(\kappa=0\) attains the same minimum, so the undefined ratio and the endpoint \(\infty\) tie. The endpoint \(0\) ties them when \(w=0\) or \(\cos\phi=0\). The flat value \(\kappa_D=\kappa\) is strictly dearer than both endpoints at stake 0.

**KNOWN, not a derivation.** If "admissible" is strengthened by the four axioms of Wilming, Gallego, and Eisert, *Entropy* 19:241 (2017), doi `10.3390/e19060241`, the functional of a pair with full-rank second argument is a positive multiple of Umegaki \(D(\rho\|\sigma)\). They state that no subset of the four axioms is enough, and that Rényi divergences meet the first three. The stopping rule applies: that uniqueness is adopted, not derived from the minimum. It still does not choose the second argument, and a single positive multiple of \(D\) is a scale for \(P_D\), not a value of \(\kappa_D/\kappa\). The pinch sets the second argument to \(\Phi(\rho)\). Holevo information of an ensemble averages \(D(\rho_x\|\bar\rho)\) to the barycenter. A Gibbs reference is their free-energy reading. Three contractions, one divergence.

## Route 3. Selection under the ruin cap

**Route.** Let lineages carry different quantum record prices. Eliminate a price when the design that minimizes it misses the ruin cap. Ask whether one price remains.

**Assumes.** Copying favors lower cost once a cost is named (`theory/SELECTION_AXIOMS.md:23-27`): a design that cannot cover the named \(J\) shrinks or is eliminated, and A2-L is the map \(m=m_0-\alpha J\) for that same \(J\). The ruin cap is \(P(\mathrm{ruin})\le\varepsilon\), outside the sum (`theory/REPRESENTATION.md:96`). Ruin, when it is a tail of the currency reserve, depends on the loss and the reserve. It does not depend on which information functional is written beside the loss.

**Where it stops.** The cap removes designs. It does not rank the functionals those designs were minimizing.

**Status. PROVED (in-model).** If the feasible set \(F=\{x:P(\mathrm{ruin})(x)\le\varepsilon\}\) does not depend on the price, and \(F\) is nonempty, then every price whose minimizer over \(F\) exists is still feasible. Nothing has been eliminated. Draft #252 sets the cap slack (`PREREG.md:36`), so neither \(P_D\) nor \(P_\chi\) is removed there. A second reading lets the cap see the named cost. `theory/SELECTION_AXIOMS.md:23` eliminates a design that cannot cover that \(J\). `theory/REPRESENTATION.md:152` says a reserve that pays the numerical cost changes the feasible set when the cost changes. At the locked point \(r=0.6\), \(\phi=0\), \(w=10\), the pinch minimum is \(1.476\) and the mutual-information minimum is \(1.572372\). A reserve strictly between them, for example \(1.50\), keeps the pinch and drops mutual information. The figure \(1.50\) is a deterministic coverage sensitivity, not a computed stochastic ruin probability. With the zero functional admitted, the same reserve still ties the pinch with charging nothing, because both attain \(w L(0)=1.476\). That reading ranks the hand-listed pair and does not fix an interior ratio. Both readings stay conditional. Draft #252 leaves the cap slack, and that locked model is not changed here. A cap separates the two named costs only when each is the actual outflow in one currency and a reserve model is stated. It does not show which functional is the true outflow by giving the same physical record a new name. Selection among the survivors needs a common \(J\). `theory/SELECTION_AXIOMS.md:23` uses \(J\) as already defined and does not reopen the term list. Two functionals are two maps \(m=m_0-\alpha P\). There is no shared \(\alpha\) until one of them is the currency. Revealed costs recover price ratios of an observed design (`theory/REVEALED_PRICES_2026-11-21.md:7-8`). A ratio is a ratio of coordinates the cost already contains. It does not name a coordinate that was never in the sum. Theorem R2 is the same shape of obstruction, already proved for classical objectives: Kelly growth and the Lundberg objective both stay solvent, and their argmins differ (`theory/REPRESENTATION.md:157-162`). A solvency filter does not leave one objective.

Forcing a common currency and then dropping the price with the higher minimized cost is Route 2 again. Route 2 ties.

**Ratio.** This route does not fix an interior value of \(\kappa_D/\kappa\). If the cap does not depend on the price, it does not read the ratio. If a reserve must cover the named \(J\), the locked point above keeps the pinch, drops mutual information, and still ties the pinch with charging nothing. Ranking the survivors by minimized cost is the simplex comparison above, which ties the endpoints \(0\) and \(\infty\) on a large set. Revealed costs recover a ratio of coordinates the cost already contains (`theory/REVEALED_PRICES_2026-11-21.md:7-8`). That is a reading of an observed design, not a derivation of this number.

## Route 4. R1's axioms on a GPT state space

**Route.** Replace the classical sample space in A6 by a general probabilistic theory, and take the operational limit of the same axioms: the entropy defined by measurements, the entropy defined by decompositions into pure states, and the large-copy properties (additivity, subadditivity) that A5 and A6 use.

**Assumes.** A1–A5, A7, and A8 are unchanged. A6's classical hypotheses are dropped, and the state is a GPT state. No quantum entropy is added as an axiom at the start.

**Where it stops.** The operational constructions do not return one functional. The step that would make the entropy unique inside quantum theory is a known theorem, and it still does not name the record price.

**Status. Closed as a KNOWN stop.** Barnum, Barrett, Clark, Leifer, Spekkens, Stepanik, Wilce, and Wilke, *New Journal of Physics* 12:033024 (2010), doi `10.1088/1367-2630/12/3/033024`: measurement entropy is the minimum Shannon entropy over fine-grained (maximal) tests; mixing entropy is the infimum of Shannon entropies over decompositions into pure states. In classical theory both equal Shannon entropy, and in quantum theory both equal von Neumann entropy, respectively, with no extra assumption inside quantum theory. They differ in general. In their firefly example, counted in bits, a pure state has mixing entropy 0 and measurement entropy 1, and a mixture has mixing entropy 1 and measurement entropy 0. Equality of the two (their word: monoentropic) is a strong constraint on a general theory; classical and quantum theory satisfy it. Short and Wehner, *New Journal of Physics* 12:033023 (2010), doi `10.1088/1367-2630/12/3/033023`, give one measure that reduces to Shannon entropy and to von Neumann entropy, and show that in a theory with non-local boxes no conditional entropy that is reasonable in their sense is subadditive. Off quantum theory the large-copy properties do not all carry over: in box world strong subadditivity fails, and Short and Wehner show no reasonable conditional entropy is subadditive. Plain subadditivity of measurement entropy survives. Quantum theory itself keeps the large-copy properties. Debreu still needs the coordinates to be intervals before it prices them (`theory/REPRESENTATION.md:84`). A GPT state does not supply those intervals.

**KNOWN, not a derivation.** Restricting the GPT to quantum theory and adopting Ochs, *Reports on Mathematical Physics* 8:109–120 (1975), doi `10.1016/0034-4877(75)90022-1`, fixes von Neumann entropy up to scale as a measure of dispersion. The publisher abstract says the postulates have no direct bearing on information theory. The postulate list inside the article was not re-read. Adopting Wilming, Gallego, and Eisert, cited in Route 2, fixes Umegaki relative entropy of a pair. The stopping rule applies to both: they are adopted axioms, not a consequence of R1. After either adoption the record contraction is still open, by the copy-versus-noise pair in Route 1. Shannon's classical uniqueness, the one A6 uses, remains Aczél, Forte, and Ng (doi `10.2307/1426210`, re-checked on Crossref this date; `theory/REPRESENTATION.md:58`). It is a theorem about finite alphabets.

**Ratio.** This route does not fix \(\kappa_D/\kappa\). One scale applied to both entropy differences keeps both terms and sets the ratio to 1. Refusing a second coefficient is the endpoint 0, or the undefined ratio at the origin. A8 does not refuse the second coefficient (`theory/REPRESENTATION.md:64`, `:92`), and nothing in this route equates the two. Wilming, Gallego, and Eisert fix a positive multiple of \(D(\rho\|\sigma)\), which is a scale for the pinch and not a scale for \(I(W;M)\). Adopting either theorem remains **KNOWN** and is not a derivation of the ratio. Whether one common scale forces the ratio is Route 5.

## Route 5. One scale on both record terms

**Route.** Does the one-scale sentence, or anything else already in A1–A8 and R1, force a single scale across \(I(W;M)\) and \(P_D\), and so force \(\kappa_D/\kappa=1\)?

**Assumes.** Both terms are already written in the cost, as draft #252 writes them (`MEMO.md:64-68` at `e584d8b`). The one-scale sentence is "R1 fixes a price vector up to one common scale" (`theory/REPRESENTATION.md:177`). In the proof the common scale is the single \(a>0\) in \(C=a\sum_i p_i z_i+b\) (`:84-92`, step 6 at `:118`).

**Where it stops.** That \(a\) multiplies the whole sum. It does not set the coefficients inside the sum equal. `theory/REPRESENTATION.md:120` says the price ratios are fixed by the Cauchy equation: each concatenating coordinate is linear (`:110-111`), so each ratio is some constant. The constant is the preorder's marginal rate. The equation does not set it to 1. A6 absorbs one positive constant into the coefficient of the one memory coordinate it names (`:114`). A8 requires each coefficient nonnegative (`:64`, `:92`). No sentence in A1–A8 or R1 equates \(\kappa_D\) with \(\kappa\).

**Status. Open question.** The route does not force \(\kappa_D/\kappa=1\). The missing sentence is: both record terms are in the sum, and they carry one shared coefficient, the entropy scale used on both differences. One scale used that way keeps both terms and sets the ratio to 1. It is not the refusal of a second coefficient. Refusing the second coefficient is the endpoint 0, or the undefined ratio at \((0,0)\).

**PROVED (in-model), and not a consequence of this route.** On the antipodal ensemble \(P_\chi=c-P_D\), and \(P_D\) is not constant in \(\theta\) for \(r\in(0,1)\) (`MEMO.md:58-62`, and the sign of \(h'\) above). Then

\[
\kappa P_\chi+\kappa_D P_D=\kappa c+(\kappa_D-\kappa)P_D.
\]

The record cost is independent of \(\theta\) exactly when \(\kappa_D=\kappa\), for every pair with positive scale. Flatness selects that ray. The minimum over nonnegative combinations selects the endpoints, or the undefined ratio, as Route 2 records.

**Model implication.** Conditional on the ratio being 1: on this ensemble the record terms are flat in \(\theta\), and the stake alone sets \(\theta\) (`MEMO.md:68`). Off this ensemble the sum \(P_D+P_\chi\) need not be constant (`theory/pointer-basis-stakes-2026-11-24/PREREG_2.md:13`, `:21`). What the ratio 1 does to \(\theta\) there is **OPEN**. That test is locked and unscored in the same file. `MEMO.md:70` says the scored grid does not answer the question once the sum depends on \(\theta\).

## Model implications

- **Model implication.** If a quantum coordinate is required to extend A6, then on classical diagonal records it matches \(I(W;M)\) up to one scale \(a>0\). The pinch and a pure dimension price fail that match. A pinch term can still sit beside the mutual information. Whether it is in the sum is the coordinate-list choice R1 does not make (`CORE.md:52`).
- **Model implication.** On draft #252's complete-dephasing menu, the simplex \(\kappa+\kappa_D=1\) picks the endpoint \(\kappa_D/\kappa=\infty\) when \(w>0\) and \(\cos\phi\neq 0\). At stake 0, and at every stake when \(\cos\phi=0\), that minimum ties the endpoints \(0\) and \(\infty\). On the A8 orthant the undefined ratio ties the endpoint \(\infty\), and the endpoint \(0\) ties them on that same set. The minimum does not identify the ratio. Conditional on the ratio already being 1, the antipodal record terms are flat and the stake alone sets \(\theta\) (`MEMO.md:68` on that branch). Off this ensemble the sum need not be constant (`theory/pointer-basis-stakes-2026-11-24/PREREG_2.md:13`, `:21`), so what ratio 1 does to \(\theta\) there is **OPEN**.
- **Model implication.** For a classical-quantum state \(\rho_{XB}=\sum_x p_x |x\rangle\langle x|\otimes\rho_x\), the quantum mutual information built from von Neumann entropy equals the Holevo quantity of the ensemble. **ELEMENTARY** given \(S\). It is not a consequence of A1–A8. Draft #252's \(P_\chi\) is the mutual information after the measurement (`PREREG.md:34`).
- **Model implication.** On draft #253's singlet menu the A6 coordinate is identically zero (`theory/COMPOSITE_CONTEST_2026-11-24.md:56` on that branch). Selection under a slack or silent cap cannot see it (Route 3). Charging \(\lambda\ln K\) would add a coordinate that is essential only on a menu that ranges over theories. On a single-theory menu it is constant, and Lemma M prices a constant coordinate at 0 (`theory/REPRESENTATION.md:80`). R1 does not choose to add it. The list stays open.

## Why there is no script

Route 2's comparison, including the comparison of \(\kappa_D/\kappa\), is the sign of \(h'\) and the identity \(P_D+P_\chi=c\) already written on draft #252 (`MEMO.md:58-62`, `PREREG.md:64`). A grid would re-check that sign. It would not define the admissible set, and it would not turn the tie of the endpoints into one ratio. The locked-point costs \(1.476\), \(1.800\), and \(1.572372\) are that same closed form at one published \((r,\phi,w)\). Route 3's reserve comparison uses those two minima. Route 5 is a reading of one sentence in `theory/REPRESENTATION.md`. Route 4 is the published separation of two GPT entropies. None of these fails by a draw from a seed. No preregistration and no run.

## Open question

Route 1 is missing a naming axiom, and with only \(I(W;M)\) named there is no ratio \(\kappa_D/\kappa\) to fix. Route 2 is missing a definition of "admissible" that excludes the zero price without already naming the functional; on the simplex that remains, the minimum ties the endpoints \(0\) and \(\infty\) on a large set, and the natural strengthening (Wilming's four axioms) is KNOWN and still leaves the ratio open. Route 3 is missing a fitness that is not the disputed functional. Route 4 is closed: on a general probabilistic theory the two entropies are not one functional, and in quantum theory they coincide without an extra assumption. A known entropy scale is not an exchange rate. Route 5 is missing the sentence that puts both record terms in the sum under one shared coefficient. A1–A8 and the ruin cap do not state any of those missing sentences. Flatness of the antipodal record cost fixes the ratio at 1, and that condition is not one of the axioms.

## ERRATA

*After `theory/reviews/QUANTUM_RECORD_PRICE_REVIEW_2026-11-24.md` (commit `1e2f7f5`), which reviewed head `a0fd117`. Five routes. Routes 1 through 4 stand as claims about those questions. Route 5 is the one-scale reading. Each finding is answered here. Ace's answers on upstream #254 are applied below where they change a sentence.*

**E1. HIGH. Ratio 1 keeps both terms.** The earlier sentence said that \(\kappa_D/\kappa=1\) is what you get by refusing a second coefficient. That is wrong. From \(P_\chi=c-P_D\),

\[
\kappa P_\chi+\kappa_D P_D=\kappa c+(\kappa_D-\kappa)P_D.
\]

\(P_D\) is not constant in \(\theta\) for \(r\in(0,1)\). The record cost is independent of \(\theta\) exactly when \(\kappa_D=\kappa\). One scale on both terms keeps both terms and sets the ratio to 1. Refusing the second coefficient is the endpoint 0, or the undefined ratio at the origin. The corrected sentences are in Route 4's ratio paragraph and in Route 5. Route 5, in that section and not repeated here, asks whether `theory/REPRESENTATION.md:177` forces one scale across the two record terms. It does not. The common scale is one \(a>0\) in front of the whole sum. The internal ratios stay the preorder's marginal rates. Nothing sets one of them to 1. The ratio stays a free nonnegative price. The shared-coefficient sentence is not added. Flatness on this ensemble would pick the ratio by a symmetry demand, and that demand is not an axiom. Conditional on the ratio already being 1, the stake alone sets \(\theta\) (`MEMO.md:68`). Off this ensemble the sum need not be constant (`theory/pointer-basis-stakes-2026-11-24/PREREG_2.md:13`, `:21`), and what ratio 1 does to \(\theta\) there is **OPEN**.

**E2. MEDIUM. The pure-MI cost is not \(w L(\pi/2)\).** The third simplex bullet said the endpoint \(t=0\) attains \(w L(\pi/2)\) as its comparison value whenever \(w>0\) and \(\cos\phi\neq 0\). That number is the cost at \(\theta=\pi/2\). It is the minimum only while the minimizer stays there. Checked from the closed form, not copied: at \(r=3/5\), \(\phi=0\), \(w=10\), \(w L(0)=1.476\), \(w L(\pi/2)=1.800\), and \(P_\chi(0)+w L(0)=1.572372\) at six decimals at \(\theta=0\), which is lower than \(1.800\) by \(0.227628\) at those decimals. Draft #252 already places this point past \(w_\star=3.209014724815\) (`MEMO.md:42-46`). The pure pinch remains the unique simplex minimizer, by the nonnegativity argument now written in that bullet. No new grid.

**E3. MEDIUM. A reserve can see \(J\).** `theory/SELECTION_AXIOMS.md:23` eliminates a design that cannot cover the named \(J\). At the same locked point the pinch minimum is \(1.476\) and the mutual-information minimum is \(1.572372\). A reserve strictly between them, for example \(1.50\), keeps the pinch and drops mutual information. That \(1.50\) is a deterministic coverage sensitivity, not a computed stochastic ruin probability. With the zero functional admitted, both the pinch and charging nothing attain \(1.476\), so the reserve ties them. The reading does not fix an interior ratio. Draft #252's slack cap (`PREREG.md:36`) is the other reading, and it removes neither price. Both readings are now in Route 3.

**E4. LOW. Line pins.** `theory/RECORD_REPAIR_FLOOR_2026-11-23.md:114` is the two-dimensional quantum bullet. The three-dimensional repair heat is open at `:115` and `:174`, and at `theory/PHYSICS_CHAIN_2026-11-23.md:18`. The one-scale sentence is `theory/REPRESENTATION.md:177`. The review's pin `:176` is the blank line above that sentence, and Class L is `:184`, so the cite keeps `:118` and `:177`. Theorem S3 is restated with the convex feasible set (`CORE.md:48`). The clause "the linearity step does not fire" is withdrawn. The Cauchy step (`theory/REPRESENTATION.md:110-111`) applies once a concatenating interval coordinate is in the sum, and it does not choose which functional is placed there.

**E5. LOW. Four questions.** The nine earlier questions for Ace are superseded by four, posted on the draft after this errata: the coordinate list, including whether \(\lambda\ln K\) is a new essential coordinate; the ruin-cap reading; the GPT reading; and the ratio, including the zero functional, the conditional pinch pick, and Route 5. The Wilming question and the Ochs question are not restated. The current paragraphs already say the cited theorem does not choose the second argument, and that Ochs is used from the publisher abstract.

**E6. LOW. Four pins from the review of head `a3e82ac`.** No blocker. The Route 2 cell in `OPEN_WORK.md` now says the undefined ratio on the A8 orthant ties the endpoint \(\infty\), as Route 2's ratio paragraph already says. Barnum et al. are cited with their "respectively": classical theory, Shannon entropy; quantum theory, von Neumann entropy. The sentence that the sum need not be constant off the antipodal ensemble is pinned to `theory/pointer-basis-stakes-2026-11-24/PREREG_2.md:13` and `:21`. `MEMO.md:70` says the scored grid does not answer the question once that sum depends on \(\theta\). No preregistration and no run log was edited.
