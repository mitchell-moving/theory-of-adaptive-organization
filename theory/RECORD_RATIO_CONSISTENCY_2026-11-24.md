# Record-price ratio: four consistency readings, none forces 1

**G2: CONSISTENCY_CHECK.** Each route's value is hand-computable from the locked cost, or it is a known theorem. The note is not a test.

*24 November 2026 (UTC). Desk note. No script. Self-check, not an independent review. `THEORY.md` is unchanged. Open-work row T75. Status words are those at `CORE.md:169`. Nothing here derives general relativity, quantum mechanics, or holography. The qubit, the dephasing channel, and the two record functionals are inputs from draft #252.*

*T74 (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md` on `forge-quantum-record-price` at `1fb7b5b`) asked whether A1–A8 or the ruin cap fixes \(\kappa_D/\kappa\). They do not. The missing sentence named there is one shared coefficient on both record terms. On the antipodal ensemble the record cost is flat in \(\theta\) exactly at ratio 1 (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md` Route 5 and ERRATA E1 on that head; `theory/pointer-basis-stakes-2026-11-24/MEMO.md:64-68` at `e584d8b`). This note asks whether a consistency principle, rather than a further axiom, forces that sentence.*

## Answer

No. Four readings. None of them forces \(\kappa_D/\kappa=1\).

\[
J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L,
\]

with \(\kappa,\kappa_D\ge 0\), \(I(W;M)=P_\chi\), and \(P_D=\mathbb{E}[D(\rho\|\Phi_\theta(\rho))]\) as on draft #252 (`PREREG.md:28-34`, `MEMO.md:64-68` at `e584d8b`).

- **Route A** (no-arbitrage). Inside the menu of one projective measurement there is only one design per classical channel, so there is no cycle. Adding a pointer measurement followed by a classical garbling makes the same channel strictly cheaper by \(\kappa_D P_D(\theta)\) whenever \(\kappa_D>0\). The gap is zero for every \(\theta\) exactly when \(\kappa_D=0\). Ratio 1 leaves the gap equal to \(\kappa P_D(\theta)\). There is no reverse step, so there is no cycle at any ratio. **PROVED (in-model)** on the complete-dephasing antipodal ensemble. Does not force ratio 1.
- **Route B** (coarse-graining continuity). Full dephasing makes the state classical. At the pointer, \(P_D=0\), so the cost matches R1's price \(\kappa I(W;M)\) at every ratio. Off the pointer, \(P_D>0\), so matching R1 for every basis forces \(\kappa_D=0\). Continuity of the preorder (A1) is continuity in the resource coordinates, not in the decoherence parameter. **PROVED (in-model)** that neither reading forces ratio 1.
- **Route C** (thermodynamic exchange). Reeb and Wolf 2014 bound heat by a von Neumann entropy decrease, and they show the same bound does not pass to a change in mutual information. Adopting that entropy is **KNOWN**. The route stops. It does not set \(\kappa_D/\kappa\).
- **Route D** (entropy ledger, added here). For this measurement, \(I(W;M)+P_D=H(M)-\mathbb{E}[S(\rho)]\). Ratio 1 is the price that puts one coefficient on that balance and none on the split. The chain rule writes the entropy coefficient as 1. A price coefficient is the preorder's marginal rate (`theory/REPRESENTATION.md:120`). **PROVED (in-model)** as an identity. It does not force the price ratio.

The shared-coefficient sentence remains the missing sentence. The two strengthened readings that do fix a number fix the endpoint 0, which T74 already separated from that sentence (`theory/QUANTUM_RECORD_PRICE_2026-11-24.md` ERRATA E1 on that head).

## Where the ratio stands

On this main (`0f37918`):

- `CORE.md:52` and `theory/REPRESENTATION.md:58-60`: the memory coordinate is classical mutual information. R1 does not choose the coordinate list. A8 only signs coefficients.
- `theory/REPRESENTATION.md:177`: one common scale multiplies the whole sum. The ratios inside the sum are the preorder's marginal rates (`:120`, Cauchy at `:110-111`). No sentence equates two of them.
- `theory/REPRESENTATION.md:120`: Landauer and the learning-rate papers are floors. They do not produce the sum. Stacking a stock price and a second thermodynamic price double-counts a bound the Shannon note already refuses.
- `THEORY.md:36`: physics sets floors on prices, not exchange rates between systems. A dimensionless ratio inside one system is still a price ratio. The sentence does not set it.
- `theory/SELECTION_AXIOMS.md:23`: a design that cannot cover the named \(J\) shrinks. The axiom uses \(J\) as already defined and does not reopen the term list.
- `theory/INTERNAL_MODEL.md:66`: "no-arbitrage" there is the market reading that blind persistence in an efficient environment requires information. It is not a conversion between \(P_D\) and \(I(W;M)\).

Off this main, and not re-derived here:

- Draft #252, head `e584d8b`. Closed form at complete dephasing, `PREREG.md:64-72`. The sum \(P_D+P_\chi\) is independent of \(\theta\) on the antipodal ensemble, `MEMO.md:58-62`. At \(\kappa_D=\kappa\) the stake alone sets \(\theta\), `MEMO.md:68`. Off that ensemble the sum need not be constant, `MEMO.md:70`. The follow-up is locked and unscored, `PREREG_2.md`.
- T74, head `1fb7b5b`. Five routes. A1–A8 do not force the ratio. Flatness on this ensemble does, and flatness is not an axiom.
- Draft constants note, `forge-constants-exchange-rates`: \(k_B\) and \(\hbar\) as exchange rates once a physical energy and a physical time are given. That is a different ratio. It is not \(\kappa_D/\kappa\).

Repository grep on this main, before this file existed: `git grep -n -i -E 'κ_D|kappa_D|Reeb' -- '*.md'` has no hit on \(\kappa_D\) and no hit on Reeb and Wolf. The no-arbitrage hits are the market sentence above.

## The identity used below

**Scope.** The measurement in draft #252: one projective measurement of \(n(\theta)\cdot\sigma\) on a qubit. The post-measurement state \(\Phi_\theta(\rho)\) is diagonal in that basis with eigenvalues \(p(m\mid\rho)\). Its von Neumann entropy equals the Shannon entropy of the outcome. For an ensemble labeled by \(W\),

\[
H(M\mid W)=\mathbb{E}[S(\Phi_\theta(\rho))],
\]

so

\begin{align*}
I(W;M)&=H(M)-H(M\mid W)=H(M)-\mathbb{E}[S(\Phi_\theta(\rho))],\\
P_D&=\mathbb{E}[S(\Phi_\theta(\rho))-S(\rho)].
\end{align*}

Adding these,

\[
I(W;M)+P_D=H(M)-\mathbb{E}[S(\rho)].
\]

**ELEMENTARY.** \(\mathbb{E}[S(\rho)]\) does not depend on \(\theta\). \(H(M)\) does, except where the outcome is fair for every \(\theta\). On the antipodal ensemble at complete dephasing, \(P(M=+1)=1/2\) for every \(\theta\) (`MEMO.md` ERRATA E2 at `e584d8b`), and the right-hand side is the constant \(c\) already written at `MEMO.md:58-62`. Off that ensemble the identity still holds and the right-hand side need not be constant. That is why flatness at ratio 1 is special to this ensemble (T74; `MEMO.md:70`).

The record cost is then

\[
\kappa\,I(W;M)+\kappa_D\,P_D=\kappa\big(H(M)-\mathbb{E}[S(\rho)]\big)+(\kappa_D-\kappa)\,P_D.
\]

Ratio 1 drops the second term. It prices the balance and not the split. Any other ratio prices the created noise \(P_D=H(M\mid W)-\mathbb{E}[S(\rho)]\).

## Route A. No-arbitrage

**Question.** If a free operation converts \(P_D\) into \(I(W;M)\) or back, does every ratio other than 1 let a designer lower \(J\) for the same behavior by a cycle?

**Assumes.** The complete-dephasing antipodal ensemble and the closed form `PREREG.md:64-72` at `e584d8b`. The record that enters the action is the final classical outcome, which is the record draft #252 keeps (`MEMO.md:34`, `MEMO.md:68`: an unmeasured quantum record is a separate question). Ruin stays slack (`PREREG.md:36`).

**One measurement, one channel.** After complete dephasing the \(\pm x\) states are maximally mixed, so

\[
P(M=+1\mid W)=\frac{1+z_W\cos\theta}{2},
\]

with \(z_W=\pm r\) on the \(\pm z\) labels and \(z_W=0\) on the \(\pm x\) labels. For \(r\in(0,1)\) and \(\theta\in[0,\pi/2]\) this determines \(\theta\). A menu of single projective measurements has one design per classical channel. There is no second path and no cycle. **ELEMENTARY** from the closed form.

**The operation that was asked for.** Measure at the pointer \(\theta=0\), then pass the outcome through a binary symmetric channel with crossover \(\varepsilon=(1-\cos\theta)/2\). For a state whose Bloch \(z\)-component is \(z\),

\[
(1-\varepsilon)\frac{1+z}{2}+\varepsilon\frac{1-z}{2}=\frac{1+z\cos\theta}{2}.
\]

Applied to the four labels, the garbling reproduces \(P(M\mid W)\) of the direct \(\theta\)-measurement. The stake observable is a function of \(W\) (`PREREG.md:55-56`), so the same channel gives the same loss \(L\) at every \(\phi\), not only at the complementary angle. The final mutual information equals \(P_\chi(\theta)\).

The quantum pinch on the garbling path is the pointer pinch. \(P_D(0)=0\) (`PREREG.md:72`). Classical post-processing is not a second pinch. The record cost of the garbling path is \(\kappa P_\chi(\theta)\).

The direct measurement pays \(\kappa P_\chi(\theta)+\kappa_D P_D(\theta)\). From the closed form, \(P_\chi(0)-P_\chi(\theta)=P_D(\theta)\), and \(P_D(\theta)>0\) for \(\theta\in(0,\pi/2]\) and \(r\in(0,1)\) (`PREREG.md:72`: \(P_D\) increases with \(|\theta|\)).

**Gap.** Same classical channel, same \(L\), same slack ruin:

\[
\big(\kappa P_\chi+\kappa_D P_D\big)-\kappa P_\chi=\kappa_D\,P_D(\theta).
\]

The gap vanishes for every \(\theta\) if and only if \(\kappa_D=0\). At ratio 1 the direct cost equals \(\kappa c\) and the garbling cost equals \(\kappa(c-P_D(\theta))\), so the gap equals \(\kappa P_D(\theta)\). Ratio 1 does not stop the designer from lowering the record cost of this channel. The lowering is one way: the data-processing inequality says a classical channel cannot raise \(I(W;M)\). Nothing in the model refunds a pinch. A cycle that returns to the same design does not exist at any ratio. A money pump does not exist at any ratio.

**What would force ratio 1, and is not here.** A reverse free map, one nat of \(I(W;M)\) per nat of \(P_D\), returning to the same design. Or a charge of \(\kappa\) per nat of mutual information destroyed by the garbling, added on top of the stock. R1 prices the stock that is held (`theory/REPRESENTATION.md:60`, the gross stock \(I_{\mathrm{mem}}\)). It does not add a second charge for destroying it. On this ensemble \(H(M)=\ln 2\) at every \(\theta\) (fair outcome, `MEMO.md` ERRATA E2), so a charge on the Shannon entropy of the outcome does not see the garbling either. The information the garbling destroys is an increase of \(H(M\mid W)\), equal to \(P_D(\theta)\), not an increase of \(H(M)\).

**Not one nat booked twice.** The environment's dephasing, before the memory measures, produces entropy only on the \(\pm x\) states: each goes from Bloch radius \(r\) to the maximally mixed state, an increase \(\ln 2-h((1+r)/2)\) with \(h\) the binary entropy in nats from that closed form. Those two labels have total weight \(1/2\), so the mean increase equals \(P_\chi(0)\). The pointer information \(P_\chi(0)\) is carried by the \(\pm z\) labels, which the \(z\)-dephasing does not touch. The two equal numbers come from different labels. Measuring in the pointer basis does not convert the dephasing entropy into the classical mutual information. The numerical match is the equal weight of the two pairs. **ELEMENTARY** from the closed form and the Bloch radius in `PREREG.md` §2.

**Status. PROVED (in-model).** The same-channel gap equals \(\kappa_D P_D(\theta)\). No cycle forces the ratio, and the one-way gap is zero for every \(\theta\) only at the endpoint \(\kappa_D=0\). That endpoint is the refusal of the second coefficient, which T74 separated from the shared-coefficient sentence.

**Where this disappears.** If the menu is only one projective measurement, the second path is not there and the gap is not a comparison the designer can make. If the behavior includes the post-measurement qubit, the paths differ: the direct measurement leaves the state diagonal in the \(\theta\) basis, and the pointer measurement leaves it diagonal in \(z\). If classical post-processing is priced as something other than the final stock, the garbling cost changes. Any of those withdraws the gap. The thing to do then is to price the operation that replaced it, not to set the ratio to 1 by hand.

**Model implication.** Conditional on free classical post-processing being allowed, and on the kept record being the final outcome: every \(\kappa_D>0\) makes a direct angled measurement strictly dearer than pointer-plus-garbling for the same channel. The minimized record cost of a channel does not depend on \(\kappa_D\). The ratio stays unidentified. This is the same conclusion as T74's minimum, reached by a dominance inside one channel rather than by a tie of endpoints across channels.

## Route B. Coarse-graining continuity

**Question.** A quantum record that fully decoheres is a classical record. R1 prices a classical record by mutual information (`CORE.md:52`). Must the price be continuous across that limit, and does the match pin \(\kappa_D/\kappa\)?

**Assumes.** Complete dephasing is the classical end of the channel (`PREREG.md` §2: \(\gamma=0\) is the sieve's long-time limit). The cost on the quantum side is the two-term record cost. The classical price of the resulting channel is \(\kappa I(W;M)+w L\), because A6 names that mutual information and does not name a pinch (`theory/REPRESENTATION.md:114`, `CORE.md:52`).

**Pointer record.** At \(\theta=0\), \(P_D(0)=0\). The two-term cost equals \(\kappa P_\chi(0)+w L(0)\) for every \(\kappa_D\). The match with R1 holds at every ratio. Continuity at the record R1 prices does not see \(\kappa_D\).

**Every basis.** At \(\theta\in(0,\pi/2]\), the state is already diagonal in \(z\), and \(P_D(\theta)>0\). The two-term cost exceeds the R1 price of that same classical channel by \(\kappa_D P_D(\theta)\). Equality for every \(\theta\) holds if and only if \(\kappa_D=0\).

**What A1 actually says.** A1 is a continuous preorder on the product of resource coordinates (`theory/REPRESENTATION.md:43`). It is not a requirement that the cost be continuous in a decoherence parameter, and it is not a requirement that a quantum extension agree with R1 off the pointer. Debreu's continuity is closed contour sets in that product topology (`theory/REPRESENTATION.md:108`). The decoherence limit is not one of those coordinates.

**Status. PROVED (in-model).** Matching R1 at the pointer leaves every ratio. Matching R1 for every basis of the fully decohered state forces the endpoint \(\kappa_D=0\). Neither is ratio 1. At ratio 1 the excess over R1, off the pointer, is \(\kappa P_D(\theta)\).

**Where this disappears.** If the classical limit is required only for pointer records, \(\kappa_D\) drops out and the route stops with no constraint. If a classical theory itself charged the disturbance of measuring a \(z\)-diagonal state in another basis, R1 would not be the comparison price. R1 does not contain that charge (`CORE.md:52`: the coordinate list is not chosen, and the coordinate that is named is mutual information). Adding it would be the missing sentence, not a consequence of continuity.

**Model implication.** Conditional on the fully decohered cost equaling R1 for every measurement basis: \(\kappa_D=0\), and the record term is the classical mutual information alone. Conditional on the match only at the pointer: the ratio is unconstrained by this limit. Neither conditional is ratio 1.

## Route C. Thermodynamic exchange

**Question.** Does the Landauer exchange between a classical record and a quantum record set \(\kappa_D/\kappa\)?

**Stop. KNOWN.** The route would set the ratio only by adopting a known entropy as the priced functional, and the paper that was asked for does not carry the ratio even after that adoption.

Crossref, direct lookup on 24 November 2026, DOI `10.1088/1367-2630/16/10/103011`. Title: "An improved Landauer principle with finite-size corrections." Authors: David Reeb, Michael M. Wolf. *New Journal of Physics* 16 (2014), article 103011, issued 8 October 2014. The same title, authors, and journal reference are the arXiv record `1306.4352v3`. The text below is that paper, not a restatement from memory.

- The entropy in the bound is the von Neumann entropy \(S(\rho)=-\mathrm{tr}[\rho\log\rho]\) (their section 2.3).
- Theorem 3 is an equality, \(\beta\Delta Q=\Delta S+I(S':R')+D(\rho'_R\|\rho_R)\), for a unitary on a system and an initially thermal reservoir that start as a product. Landauer's bound \(\beta\Delta Q\ge\Delta S\) is what remains after the mutual information and the relative entropy are dropped.
- Corollary 4: equality in that bound holds if and only if the process is unitary on the system and leaves the reservoir untouched. A process with a nonzero entropy decrease does not sit on the bound.
- Section 5.2 asks whether the bound can be written on a change in mutual information, the information an agent has about the system, instead of on the entropy in the system. A swap against a reservoir of the same size violates the tentative inequality \(\beta\Delta Q\ge\Delta I\) whenever the memory starts with perfect knowledge of a mixed state. A reversed inequality fails as well. They write that other tentative correlation forms can be dismissed the same way. Complete erasure of the correlation, in their sense, need not dissipate heat.

Adopting the von Neumann entropy, or the Umegaki relative entropy, is the step T74 already marked **KNOWN**. It chooses a functional up to a scale. It does not choose to price both \(I(W;M)\) and \(P_D\), and it does not set the ratio of those prices.

What blocks an exchange-rate reading, even after that adoption:

- The bound is on an entropy decrease of the system. \(P_D\) is an entropy increase under a pinch. \(I(W;M)\) is a mutual information. Section 5.2 is a published obstruction to replacing the entropy decrease by the mutual information.
- The bound is an inequality. Equality is the trivial process (Corollary 4). A floor under one coefficient, or under both, does not force the coefficients to be equal. `theory/REPRESENTATION.md:120` already says these floors do not produce the sum. `THEORY.md:36` already says the floor is not an exchange rate. A niche price may sit above the floor; the distance to the floor is a measured number per system (`THEORY.md:36`).
- On a state that is diagonal in an orthonormal basis, the von Neumann entropy equals the Shannon entropy of the eigenvalues. That is one functional with one scale, restricted to classical states. It is not a ratio between the mutual information of an outcome and the entropy produced by a pinch.

No value of \(\kappa_D/\kappa\) is computed from this paper. The route stops.

## Route D. One ledger, two prices

**Question.** The identity says \(I(W;M)\) and \(P_D\) are the two pieces of one entropy balance. Does pricing entropy, once, force the pieces to share a coefficient?

**Assumes.** The identity in the section above, for this rank-1 projective measurement. A5 as written: cost adds over successive durations and over independent copies (`theory/REPRESENTATION.md:53-56`). The Cauchy step makes each concatenating coordinate linear (`:110-111`). It does not set two slopes equal (`:120`).

**What the identity fixes.** The sum of the two record functionals equals \(H(M)-\mathbb{E}[S(\rho)]\), with coefficient 1 in the entropy arithmetic. That coefficient is not a price. Writing the record cost as \(\kappa\) times the balance is the shared-coefficient sentence. Writing it as \(\kappa I+\kappa_D P_D\) is the two-price sentence. Both are linear prices on the same ledger. The identity says they differ by \((\kappa_D-\kappa)P_D\). It does not say the difference is zero.

**Why A5 does not fire.** A measurement followed by a classical garbling is one record, then a degradation of that record. The mutual informations do not add. The costs of two independent copies would add. These are not independent copies. Concatenation over time prices a duration at a fixed rate. It does not identify the coefficient of a stock with the coefficient of a disturbance.

**Status. Open miss.** The identity is **PROVED (in-model)** in the scope above. The price reading is the missing sentence, not a consequence of it. A1–A8 do not contain the sentence (`theory/REPRESENTATION.md:177`, `:120`, `:114`).

**Model implication.** Conditional on the shared-coefficient sentence: the record cost equals \(\kappa(H(M)-\mathbb{E}[S(\rho)])\). On the antipodal complete-dephasing ensemble that expression is independent of \(\theta\), and the stake alone sets \(\theta\) (`MEMO.md:68`). Off that ensemble \(H(M)\) can depend on \(\theta\), so ratio 1 need not flatten the record cost. What it does to the minimizing \(\theta\) there is **OPEN**, and it is the unscored lock in `PREREG_2.md` on draft #252. This note does not score it.

## Why there is no script

Routes A, B, and D are algebra on the closed form already locked and checked on draft #252 (`PREREG.md:64-72`, C0 in that preregistration). A new grid would re-check that form. It would not decide whether a second path is on the menu, whether the post-measurement qubit is part of the behavior, or whether a known entropy bound is an exchange rate. Route C is a published theorem. None of the four fails by a draw from a seed. No preregistration and no run.

If the closed form on draft #252 were withdrawn, the gap in Route A and the pointer match in Route B would be withdrawn with it. The thing to do then is to re-derive the channel identity from whatever closed form replaces it, not to keep the ratio claim. The ledger identity in Route D does not use the antipodal closed form. It uses only that a rank-1 projective measurement leaves a diagonal state whose entropy is the outcome entropy. That step would survive a change of ensemble.

## Open miss

Route A has no cycle. The one-way replacement lowers the cost of a channel by \(\kappa_D P_D\), including at ratio 1, and it is available only if classical post-processing is on the menu and the kept record is the final outcome. Route B's continuity either misses \(\kappa_D\), at the pointer, or sets \(\kappa_D=0\), off the pointer. Route C is a known entropy bound on a different functional, and the paper shows the bound does not pass to mutual information. Route D writes the missing sentence as "do not price the split" and does not derive it. A1–A8, the ruin cap, and these four readings do not force \(\kappa_D/\kappa=1\). The shared-coefficient sentence is still missing. The endpoint 0 is what two strengthened readings would say instead, and those strengthenings are not in the axioms either.

## Prior art

Checked on 24 November 2026, and used above only where the text was read:

- Reeb and Wolf, doi `10.1088/1367-2630/16/10/103011`, as in Route C. Crossref returned the title, authors, container, volume, article number, and issue date. The theorem statements are from the published text (arXiv `1306.4352v3`, journal reference New J. Phys. 16 (2014) 103011).
- Landauer 1961 is the bound their Theorem 3 sharpens. The repository already records that DOI at `theory/REPRESENTATION.md:120`. No page claim is added here.
- A Crossref query `Fundamental energy cost for quantum measurement` with author Reeb, 24 November 2026, returned 41 works. The first page did not contain a paper of that title. That miss is not a claim that no such paper exists.

No claim is made that a consistency principle of some other kind is absent from the literature. The claim is the one in the answer: these four readings do not force the ratio.

## Ledger

**Lock reference:** no preregistration. Desk note. The closed form it uses is draft #252, head `e584d8b`. `THEORY.md` blob `6caadae569116a94a74563398be94cebf6e99e9b`.
**Logged at (ET):** 2026-11-24 17:50 ET
**Breach check:** none

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size and direction, or HIT + info) | location | stake_x_info | update | breach_check |
|---|---|---|---|---|---|---|---|
| T75-A | the same-channel gap is \(\kappa_D P_D(\theta)\), and it is zero for every \(\theta\) only at \(\kappa_D=0\) | that identity, on the complete-dephasing antipodal ensemble | HIT; information about 0 (hand computation from the locked closed form) | model | low | none yet | none |
| T75-B | matching R1 off the pointer forces \(\kappa_D=0\); at the pointer the costs match at every ratio | that split | HIT; information about 0 | model | low | none yet | none |
| T75-C | Reeb and Wolf 2014 bound heat by a von Neumann entropy decrease and do not pass the bound to mutual information | the cited theorem (Theorem 3, Corollary 4, section 5.2) | HIT; information about 0 (known theorem; it does not set the ratio) | model | low | none yet | none |
| T75-D | \(I(W;M)+P_D=H(M)-\mathbb{E}[S(\rho)]\) for this rank-1 measurement | that identity; the chain-rule coefficient is not a price | HIT; information about 0 | model | low | none yet; the shared-coefficient sentence stays missing | none |
| T75-ratio | a consistency reading forces \(\kappa_D/\kappa=1\) | none of the four readings does | HIT on the question as asked; information about 0, because each reading was fixed before a run | model | low | none yet | none |
