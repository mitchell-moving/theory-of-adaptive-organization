# Holographic memory and the cost of judgment

*Sunday 22 November 2026. Draft, revised the same day after the review of PR #186. A self-check, not an independent review. The hypothesis sentence is unchanged. The master equation in THEORY is unchanged. No locked preregistration file is edited. `THEORY.md`, `CORE.md`, and `README.md` are not edited. Checks: `theory/holographic_memory_checks/memory_checks.py`, run at `nice -n 19` (96 checks, FAILS 0). DOIs resolved on the Crossref API on 22 November 2026, and the abstracts used below, are listed in `theory/holographic_memory_checks/crossref.out`.*

Labels: **PROVED** (a proof is on this page, in the class named with it, and the arithmetic is in the checks), **PROVED (in-model)** (the same, at a stated parameter point the checks recompute), **KNOWN** (published, fetched this session, or already in this repository, and not claimed here), **CONJECTURE** (a measurement that has not been run), **FAILS** (a counterexample is on this page), **METAPHOR** (the name adds no prediction the cost equation does not already make). GTAO is the theory in this repository.

The sentence of the hypothesis is unchanged, byte for byte:

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

## 0. The answer

Sometimes. A shared memory minimizes the cost when the decision is a combination of many signals. It ties a local memory when every decision reads one signal on its own, and a memory that mixes those signals is then the more expensive one. Sparse features lower the cost when the readout names which few are active. Sparse queries do not: if a typical decision touches only a couple of items chosen from many, the high-stake costs of the two memories meet.

The alignment of the memory with the task is what any separable precision cost does on an isotropic Gaussian prior. A mutual-information price and the heat \(a(v-\sigma)/\sigma\) are two such costs, and both keep a direction when the stake times its weight clears a constant. The factor-\(s\) window between those thresholds is that counting shape. It is not, by itself, evidence for the heat. The heat is distinguished by the error, which falls as \(w^{-1/2}\) and rises as \(\sqrt{a}\), and by a minimized cost that grows like \(\sqrt{w}\). A price on nats falls as \(w^{-1}\), does not see the drift, and has minimized cost \((\kappa/2)(1+\log(2wV/\kappa))\). The factor by which \(K\) identical modes cost more heat when stored separately, at a matched sum-error, is already proved.

A cap on the chance of a large error does not, in this class, select a split of one precision budget. At the note's own heat and upkeep, two copies of one full memory meet the cap at cost \(5.12\), and the split meets it at seven units and cost \(7.700585\). That miss is an open question about the missing baseline, worked in §4. Under the accounting that charges every unit its own heat, a pool of the same units is at most as costly as the non-pooling copy, and a one-unit copy can meet the cap only when the unit can hold the whole precision. The inequalities are stated in that section before the costs the checks print.

The phone image does not follow. In the proved class the heat floor depends on the rank of the decision and on the drift of those modes, not on the dimension of the world. At a drift of one per second, \((v-\varepsilon)/\varepsilon=1\), temperature \(300\,\mathrm{K}\), and a billion modes, the floor is \(4.141947\times 10^{-12}\) W. A finite-rate memory sits above that floor. The figure is not a statement about whether a frontier model runs on a phone.

## 1. Already in the repository, and the other holographic draft

None of the following is a result of this note.

- The heat floor. For one exogenous equilibrium Ornstein–Uhlenbeck signal and a mean-squared decision loss, the infimum of the memory-bath heat is \(kT\,a(v-\varepsilon)/\varepsilon\) (`theory/INFO_PHYSICS_ATTAINABILITY.md`). For independent modes the per-mode loss adds those rates. On a sum loss the minimizer is one memory, gains \(g_k=1/(a_k+\mu)\), heat \(kT\mu\) (`theory/INFO_PHYSICS_GENERAL.md`). At rates \((1,100)\), variances \((1,1)\), and sum-error \(0.5\), that note has separate heat \(141\) against \(\mu=103.887732673340\). The checks here recompute both numbers. For \(K\) identical modes the separate heat is exactly \(K\) times the joint heat at every matched sum-error. The ratio of optimized costs tends to \(\sqrt{K}\).
- The shape \(\dot Q\ge kT\) times the learning rate is Horowitz and Esposito. This note uses it and does not re-prove it.
- The word superposition, where it already appears, is the world's linear mixture of sources (`reviews/night1/formal/AXIOMS.md`), not a memory code. Distributed, where it already appears, is a database or a firm, not a holographic store.
- Draft PR #184, branch `holographic-2026-11-22`, was read and is not edited. It tested the spacetime sense: boundary against bulk, area against volume, MERA. Inside the class it proved, the heat at fixed per-site error scales with the volume, and the sum-loss memory has one coordinate. That draft's conclusion stands for that sense. This note is the other sense: many items in one shared state, read by content, degrading when units are lost.

Kolmogorov's reverse water-filling and Sims's rational inattention are the \(\tfrac12\log\) allocation. Their work records were fetched this session. The water-filling description used below is the one already booked in `theory/INFO_PHYSICS_GENERAL.md`, not a new reading of either paper. Copies of an on/off layer under a ruin cap are already R1 and CT37 in `theory/ROBUSTNESS.md`. Section 4 uses that result and does not redo it.

## 2. Class

**M-X, M-E.** \(K\) independent exogenous equilibrium Ornstein–Uhlenbeck modes, \(dX_k=-a_k X_k\,dt+\sqrt{2 a_k v_k}\,dW_k\). Where the sentence says identical, every \(a_k=a\) and every \(v_k=v\). The signal bath's medium heat is zero, by the cancellation already proved. A memory that moves \(X\) is outside.

**M-B.** The memory is a bipartite Markov process. The action is a function of the current memory state. The checks set \(kT=1\) except in the watt conversion.

**M-C.** A rank-at-most-\(D\) Gaussian channel. The conditional covariance is \(S=( \Sigma^{-1}+\Phi)^{-1}\) with \(\Phi\succeq 0\) and \(\operatorname{rank}\Phi\le D\). For identical modes \(\Sigma=vI\) and the diffusion matrix of the modes is \(av\,I\), so the learning rate is \(av\,\operatorname{tr}\Phi\). The heat floor is \(kT\) times that rate. Two fast linear springs, rate \(10^5\), on three modes, approach the static learning rate of their channel: heat \(5.39980915\) against \(5.40000000\). One static coordinate at noise \(0.25\) on a unit mode has error \(0.2\) and learning rate \(4\), the scalar floor.

**M-L.** The loss is a mean square of linear functionals of \(X\), written \(\operatorname{tr}(U S)\), with stake \(w\). The cost is heat plus \(w\) times that loss. A loss that is not a mean square, and a conditional that is not Gaussian, stay outside.

**Local** means \(\Phi\) is diagonal in the item basis: each stored direction is one item, and at most \(D\) diagonal entries are nonzero. **Aligned** means \(\Phi\) is diagonal in the eigenbasis of \(U\). **Random** means the image of \(\Phi\) is a subspace drawn without regard to \(U\).

## 3. Shared or local

**Proposition M-item (PROVED, under M-X through M-L, identical modes).** For a per-item loss \(\sum_k c_k S_{kk}\) with \(c_k>0\), an optimum exists with \(\Phi\) diagonal in the item basis. At a fixed diagonal of the precision, a nonzero off-diagonal entry weakly raises every marginal variance and does not lower the heat.

*Proof.* The marginal variance is at least the conditional variance given the other coordinates, and that conditional variance is \(1/P_{kk}\). So \(S_{kk}\ge 1/P_{kk}\), with equality when row \(k\) of the precision has no off-diagonal entry. The heat sees only \(\sum_k\Phi_{kk}\). Zeroing the off-diagonal entries holds the heat fixed and weakly lowers every \(S_{kk}\). At precision diagonal \((2,2)\) and off-diagonal \(0.2\), \(0.5\), and \(0.8\), the trace gaps are \(0.010101\), \(0.066667\), and \(0.190476\).

If the \(c_k\) are equal, every orthonormal basis with the same precision eigenvalues has the same cost: the per-item task is isotropic, and aligned and local tie. The off-diagonal step has no rank cap: a rank-\(D\) matrix can have more than \(D\) positive diagonal entries, so zeroing off-diagonal entries can raise the rank. With a cap of two slots the ordering is the one in Proposition M-task, applied to the diagonal weights. At weights \((4,3,0.2,0.1)\) and stake \(1\), the item-aligned cost is \(5.764102\). The best precision on the all-ones axis costs \(7.176852\). The best precision on the two heavy items, \(u=(1,1,0,0)/\sqrt{2}\), costs \(2\sqrt{3.5}+2.8=6.541657\). Both shared axes are above the item-aligned cost. ∎

**Proposition M-sum (PROVED; the case \(s=K\) is the merged identical-mode theorem).** Let \(Z=\sum_{k=1}^{s} X_k\) for \(s\) identical modes, and let the loss be the mean square of an estimate of \(Z\). One aligned coordinate has heat \(kT\,a(sv-\varepsilon)/\varepsilon\) at sum-error \(\varepsilon\). \(s\) local memories have heat \(s\) times that, at every \(\varepsilon\in(0,sv)\). The optimized costs are

\[
J_{\mathrm{shared}}=
\begin{cases}
w\,sv & w\le kT a/(sv)\\
2\sqrt{kT\,a\,s\,v\,w}-kT a & w\ge kT a/(sv)
\end{cases}
\qquad
J_{\mathrm{local}}=
\begin{cases}
w\,sv & w\le kT a/v\\
s\bigl(2\sqrt{kT\,a\,v\,w}-kT a\bigr) & w\ge kT a/v.
\end{cases}
\]

For \(s\ge 2\) and \(w>kT a/(sv)\), the shared cost is strictly smaller. As \(w\to\infty\) the ratio of the costs tends to \(\sqrt{s}\). The matched-error heat ratio is \(s\) at every error.

*Proof.* The sum of \(s\) identical modes is the scalar equilibrium Ornstein–Uhlenbeck signal of rate \(a\) and variance \(sv\), by the same addition used for \(K\) modes in the merged note. The scalar frontier applies. Local errors add, because a diagonal conditional leaves the items uncorrelated, and the symmetric point \(s_k=\varepsilon/s\) is feasible. Its heat is \(s\) times the joint heat. The scalar threshold \(kT a/V\) becomes \(kT a/(sv)\) for the sum and \(kT a/v\) for each item. Between those stakes the shared memory tracks and every local item is blind. The high-stake ratio tends to \(s/\sqrt{s}=\sqrt{s}\). The checks recompute the merged points: joints \(1.5\), \(1.727272727273\), \(7\) at \((K,\varepsilon)=(2,0.8)\), \((3,1.1)\), \((4,0.5)\), and separate heats \(3\), \(5.181818181818\), \(28\). ∎

The factor \(s\) is that argument on a subset. It is recorded so the boundary can be stated. It is not a new technique. The merged case is \(s=K\).

On four identical modes the shared threshold is \(1/4\) and the local threshold is \(1\). Both are blind at stake \(0.1\), cost \(0.4\). At stake \(0.5\) the shared cost is \(1.828427124746\) and the local cost is \(2\). At stake \(4\) the costs are \(7\) and \(12\). At stake \(100\) they are \(39\) and \(76\), ratio \(1.948718\), toward \(2\). One shared coordinate beats a local memory of \(1\), \(2\), \(3\), or \(4\) slots at stake \(4\): costs \(7\) against \(15\), \(14\), \(13\), and \(12\).

**Proposition M-task (PROVED, identical modes).** Let \(U\) have eigenvalues \(\lambda_i\). The heat-optimal \(\Phi\) of rank at most \(D\) puts its precision on the \(D\) largest eigenvalues that clear \(w\lambda>kT a/v\), and nowhere else. Direction \(\lambda\) contributes the scalar frontier at stake \(w\lambda\). A direction that does not clear the threshold is left at the prior and spends no dimension.

*Proof.* The heat \(kT\,av\,\operatorname{tr}\Phi\) depends on \(\Phi\) only through its eigenvalues. For fixed eigenvalues, \(\operatorname{tr}(U S)\) is minimized by placing the smallest posterior variances on the largest eigenvalues of \(U\): the trace of a product is minimized when the eigenvalues are oppositely ordered. Each direction then separates. Activating \(\lambda\) saves \(w\lambda v-2\sqrt{kT\,a\,v\,w\,\lambda}+kT a\) against leaving it blind, and that saving is increasing in \(\lambda\) once \(\lambda\) is above the threshold, because its derivative \(wv\bigl(1-\sqrt{kT a/(v w\lambda)}\bigr)\) is positive there. The \(D\) largest qualifying eigenvalues are the ones to keep. ∎

**Proposition M-groups (PROVED).** \(m\) disjoint sums of \(s\) identical modes each, loss the sum of the \(m\) mean squares. A shared memory of dimension \(m\), one coordinate on each sum, attains the uncapped optimum. The high-stake cost ratio against a full local memory tends to \(\sqrt{s}\).

At \(m=3\), \(s=4\), the ratio at stake \(10^8\) is \(1.999950\). At stake \(1\) the costs are \(9\) and \(12\). At stake \(0.2\), below the shared threshold \(1/4\), both are blind, cost \(2.4\).

**The random-subset query.** A uniform random subset of size \(s\), loss the mean square of the sum of that subset, has task operator \(U=\mathbb{E}[1_\Omega 1_\Omega^\top]\). Its eigenvalues are one spike \(s^2/K\) and \(K-1\) copies of \((s/K)(K-s)/(K-1)\), checked against the matrix for \((K,s)\) in \(\{(12,1),(12,2),(12,6),(12,12),(8,3)\}\). The spike is tracked when \(w>(kT a/v)\,K/s^2\). A local item, whose diagonal weight is \(s/K\), is tracked when \(w>(kT a/v)\,K/s\). The ratio of those stakes is \(s\).

At \(K=12\), in units \(kT a/v=1\):

| \(s\) | shared threshold | local threshold | window | high-stake cost ratio |
|---|---|---|---|---|
| 1 | 12 | 12 | 1 | 1.000000 |
| 2 | 3 | 6 | 2 | 1.008218 |
| 4 | 0.75 | 3 | 4 | 1.054454 |
| 6 | 0.333333 | 2 | 6 | 1.135018 |
| 12 | 0.083333 | 1 | 12 | 3.462869 |

For \(s=1\) the task is a multiple of the identity and the memories tie at every stake. For \(s=12\) the task is the pure sum and the high-stake ratio tends to \(\sqrt{12}\). For a small subset the high-stake ratio is already \(1.008\) at \(s=2\). The window is real and narrow. Sparse queries are not the regime in which a shared memory wins by a large factor.

**Proposition M-random (PROVED for the expectation; the finite-heat gap is in-model).** A Haar subspace of dimension \(D\) captures expected energy \(D\) of the all-ones vector in \(\mathbb{R}^K\). The expected residual variance of the sum, at infinite precision, is \(v(K-D)\), the same residual as perfectly tracking \(D\) items and dropping the rest. On \(K=20\), \(D=5\), \(2000\) draws, the mean captured energy is \(5.0458\) (standard error \(0.0583\)), against the exact expectation \(D=5\). At heat \(4\), one aligned coordinate holds the sum-error at \(4\). A uniform unit vector \(g\) has \(\mathbb{E}[(1\cdot g)^2]=1\), so the expected sum-error of one random coordinate at that heat is \(K-4/5=19.2\). The mean of \(400\) draws at seed \(2\) is \(19.2291\), standard error about \(0.05\). The expectation is the claim. The seed-\(2\) mean is the sample.

Random projections are not the optimum for a decision that is known when the memory is built. They match local storage in the infinite-precision residual and lose once the aligned coordinate is available at finite heat. Plate's construction and Kanerva's title use random high-dimensional vectors because the query is not a single known functional. That is a different design problem. Candès and Tao, and Donoho, title the recovery of a signal from random projections. Their bounds are not restated: the abstracts were not in the records fetched. The comparison this note proves is the known-decision gap above, not their measurement count.

**Known support, a different sparsity.** The world has \(K\) possible items and a support of size \(s\) known to the readout and unknown when the slots are chosen. Inactive items are absent, so they add no drive. A local code of \(D\) fixed slots pays the heat budget on those slots whether or not they are active. A Gaussian codebook of \(D\) projections is scaled, on the revealed support, so that its heat equals the same budget.

At \(K=32\), \(s=4\), \(D=8\), heat \(16\), the ideal of \(s\) dedicated sensors has summed error \(0.8\). The fixed slots have expected error \(3.333333\), because they capture one active item on average. The random codebook, \(300\) supports, seed \(3\), has mean error \(1.204911\). It beats the fixed slots and does not reach the ideal: a random \(8\times 4\) matrix is not an isometry, and the gap is the conditioning. At \(K=s=D=8\), same heat, the local code stores every item and has error \(2.666667\). Seed \(4\) is one Gaussian matrix, error \(3.942262\). Across \(2000\) independent codebooks the mean error is \(4.079182\) (standard error \(0.004528\)). The local error sits below that mean. When the support is the whole space, random projections do not beat item storage.

**Drift.** For a pure sum of \(K\) identical modes the two thresholds are \(kT a/(Kv)\) and \(kT a/v\). Their ratio is \(K\) at every \(a\). Raising \(a\) raises both stakes and the heat. It does not change which memory wins. On unequal rates, at sum-error \(0.5\) and variances \(1\), the matched-heat ratio is \(2\) at rate ratio \(1\), \(1.919669\) at rate ratio \(4\), and \(1.357234\) at rate ratio \(100\). The last pair is the merged anchor. Separating the rates shrinks the ratio and does not reverse it on this grid.

**Where this sits against the published geometry. KNOWN as algebra, not as support for the heat.**

On an isotropic prior the loss \(\operatorname{tr}(U S)\) is minimized, at fixed eigenvalues of \(\Phi\), by aligning the smallest posterior variances with the largest eigenvalues of \(U\). Any cost that is an increasing separable function of those precisions has the same alignment and the same threshold shape. Kolmogorov's \(\tfrac12\log\) and the heat \(a(v-\sigma)/\sigma\) are two such costs. The merged sum-loss theorem had already aligned a memory with the all-ones task. Elhage and coauthors, on the arXiv record fetched, obtain polysemanticity by storing extra sparse features in superposition, and they report a phase change. That phase change is not this window: §6 keeps the identification as **FAILS**. Hopfield's abstract gives a content-addressable memory that returns a whole pattern from a sufficient part. Plate's abstract uses a fixed-width vector for bindings. None of those papers contains this heat.

A direction of weight \(\lambda\) is tracked when \(w\lambda\) clears a constant. For the heat the constant is \(kT a/v\). For the nat price \(\kappa\cdot\tfrac12\log(v/\sigma)+w\lambda\sigma\) the constant is \(\kappa/(2v)\). The ratio of the local threshold to the spike threshold is \(s\) for both, because both constants sit in front of \(1/\lambda\). The factor-\(s\) window is that shared counting shape. What separates the prices is the error and the cost: heat-optimal error \(\sqrt{kT a V/w}\), cost \(2\sqrt{kT a V w}-kT a\); nat-priced error \(\kappa/(2w)\), cost \((\kappa/2)(1+\log(2wV/\kappa))\). The slopes and the factor \(\sqrt{a}\) are in §5.

**What is new on this page.** The table in which the shared window does not become a large high-stake gap. The random-versus-aligned gap at equal heat, expectation \(19.2\) against \(4\). The known-support comparison, \(3.333\) against \(1.205\) against \(0.800\). The scaling comparison in §5. The degradation identity in §4. The copy baseline next to that identity, which reverses the selection reading. The capacity-cap comparison that follows it.

**What fails.**

- "A shared memory always costs less." **FAILS.** On a per-item loss with unequal weights, the all-ones axis costs \(7.177\) and the two-heavy axis costs \(6.542\), against \(5.764\) for the item-aligned slots. On an isotropic per-item loss the two memories tie.
- "Sparse queries favor a shared memory." **FAILS** as a high-stake claim. At \(K=12\), \(s=2\), the high-stake ratio is \(1.008218\). The window has width \(2\) and the costs above it meet.
- "Random distributed storage is the holographic optimum." **FAILS** for a known sum. The aligned coordinate is the optimum. The expected error of a random coordinate at the same heat is \(19.2\), against \(4\).
- "A single stored coordinate degrades gracefully." **FAILS.** Graceful degradation, in the sense of the identity below, is a property of a split across units (§4). One coordinate is either up or down.

**What to try next.** Not a lock and not a preregistration. Rebuild a sparse-feature toy model of the Elhage kind with the heat \(kT a(v-\varepsilon)/\varepsilon\) as the width cost, and with a nat-price control \(\kappa\cdot\tfrac12\log(v/\varepsilon)\) on the same draws. Sweep stake and drift. The measurement that separates the prices is the slope of error against stake, and the slope against drift. The factor-\(s\) window is predicted by both prices, so a window of that width would not separate them. If the error scales as \(1/w\) and ignores the drift, the heat functional has added nothing in that model.

## 4. Graceful degradation, and the cap

**Proposition M-split (PROVED).** Split a total precision evenly across units that all observe the same sum, of prior variance \(V\), held at error \(\varepsilon\) when every unit is up. After a fraction \(f\) of the units fail, the error is

\[
\varepsilon_{\mathrm{split}}(f)=\frac{V\varepsilon}{(1-f)V+f\varepsilon}.
\]

A local code whose failed items revert to the prior, and whose surviving items keep error \(\varepsilon\) in the sum, has

\[
\varepsilon_{\mathrm{item}}(f)=(1-f)\varepsilon+f V.
\]

For \(f\in(0,1)\) and \(\varepsilon\in(0,V)\),

\[
\varepsilon_{\mathrm{item}}-\varepsilon_{\mathrm{split}}=\frac{f(1-f)(V-\varepsilon)^2}{(1-f)V+f\varepsilon}>0.
\]

The derivative at \(f=0\) is \(V-\varepsilon\) for item erasure and \(\varepsilon(V-\varepsilon)/V\) for the split. The split slope is the item slope times \(\varepsilon/V\).

*Proof.* Remaining precision fraction \(\rho=1-f\) gives \(\varepsilon_{\mathrm{split}}=V\varepsilon/(\varepsilon+\rho(V-\varepsilon))\), which is the display. The difference is the algebra in the checks. At \(V=4\), \(\varepsilon=1\), \(f=1/4\), the errors are \(16/13=1.230769230769\) and \(7/4=1.75\), gap \(0.519230769231\). The slopes at \(f=0\) are \(3/4\) and \(3\). The gap is zero at \(f=0\) and at \(f=1\). Both curves are strictly increasing in \(f\) on \((0,1)\). ∎

Both curves increase in \(f\). Inside M-C and M-L, removing a unit subtracts a positive semidefinite update from \(\Phi\). The posterior covariance rises in the Loewner order, and \(\operatorname{tr}(U S)\) does not fall for a positive semidefinite loss \(U\). Re-optimizing the decoder on the remaining channel cannot undercut the error the larger channel had already achieved. An error that falls when a part is lost is **CONJECTURE**, and it sits outside this class. The checks confirm the two curves rise, and that deleting one positive semidefinite piece of a \(2\times 2\) precision raises \(\operatorname{tr}(S)\).

The repository's antifragility reading in `theory/ROBUSTNESS.md` uses a cost concave in the stressor. The split's cost \(J(f)=(1-f)\mu+w V/(1+(1-f)\mu)\) has second derivative \(2w V\mu^2/(1+(1-f)\mu)^3\), which is positive. Under that reading the split is fragile to variation in \(f\). This note does not recompute the variance-scale stressor of that file. A mild loss of units can lower one draw's cost when the installed \(\mu\) sits past the minimizer of heat plus stake: the cap bought extra precision for the tail, and shedding it is surplus heat coming off. The error on that draw still rises. At stake weight \(1.5\) and \(V=4\) the healthy minimizer is \(\mu=\sqrt{6}-1=1.449490\), cost \(2\sqrt{6}-1=3.898979\).

A memory that is one unit does not have an interior \(f\). Losing it sends the error from \(\varepsilon\) to \(V\) in one step. "Every part carries the whole" is true of the split, because each unit observes the same functional, and it is false of a single coordinate. The optical-storage title of van Heerden and the digital store of Heanue, Bashaw, and Hesselink are the engineering literature of this picture. Heanue's abstract adds error-correcting encoding for bit-error rate. Neither abstract contains the identity above. Hopfield's abstract already says the collective properties are only weakly sensitive to the failure of individual devices. The identity is the heat-floor version of that sentence for this channel, not a replacement of it.

**The split against a coarser split, and the baseline that was missing.** Units fail independently with probability \(0.2\). Total precision is fixed, so the heat floor does not rise when the same precision is split more finely. At \(V=4\), design error \(1\), and cap level \(1.5\), the remaining fraction must exceed \(5/9\). The chance of falling short is \(0.200000\) at \(1\) unit, \(0.180800\) at \(4\), \(0.033344\) at \(7\), \(0.056282\) at \(8\), and \(7.003561\times 10^{-3}\) at \(16\). The chance is not monotone in the number of units. A reader who steps only through powers of two will think \(8\) is the first count under \(0.05\), and \(8\) misses the cap. The cheapest split on \(D=1,\ldots,20\) with upkeep \(0.5\), stake \(1\), and heat \(3\) is \(D=7\), cost \(7.700585\).

That comparison is a fine split against a coarse split of one budget. It is not the copy already in R1. Put the same installed precision \(\mu=3\) on \(n\) units, charge that heat once, and charge upkeep \(h=0.5\) per unit, which is the accounting of the paragraph above. A copy keeps the whole precision whenever at least one unit is up:

\[
\varepsilon_{\mathrm{copy}}(i)=
\begin{cases}
V/(1+\mu) & i\ge 1,\\
V & i=0,
\end{cases}
\qquad
\varepsilon_{\mathrm{split}}(i)=\frac{V}{1+(i/n)\mu}.
\]

For \(1\le i\le n\) the split's surviving precision is at most \(\mu\), so its error is at least the copy's. The two agree at \(i=0\) and at \(i=n\). The same \(n\), the same \(\mu\), the same failure probability, the same upkeep, and the same stake therefore give the copy a cost at most the split's, on every draw and in expectation. The checks confirm the pathwise bound on a grid of failure probabilities, counts, and precisions. No point on that grid reverses it.

At the worked cap the copy meets \(P\le 0.05\) at \(n=2\), because \(0.2^2=0.04\). Expected error \(1.120000\), cost \(5.120000\). Seven copies of the same memory have chance \(1.280\times 10^{-5}\), expected error \(1.000038\), and cost \(7.500038\), still below the split's \(7.700585\). R1's own expected-cost test does not buy the second copy: \(w(V-\varepsilon)p(1-p)=0.48<h=0.5\), so the cap is what lifts the count from \(1\) to \(2\). That is the copy result already proved. The split is a more expensive way to buy a tail the copy already buys.

Charging every copy its own floor, which is more heat than that accounting charges, still leaves the copy ahead at this point. The smallest precision whose up-state clears error \(1.5\) is \(\mu=5/3\). Two such trackers have total heat \(10/3\), expected error \(1.600000\), and cost \(5.933333\).

On the heat grid \(D\in\{1,2,4,8,16\}\) and \(\mu=0.5\times 1.12^{n}\) for \(n=0,\ldots,47\), stake weight \(1.5\), the split's uncapped minimum has heat \(1.391420\) and the split's capped minimum has heat \(2.189426\). Those two numbers are a minimum over splits only. A copy on the same heat rule, expected heat \(\mu(1-p^n)\), meets the cap at \(n=2\) and \(\mu=5/3\) with expected heat \(1.600000\) and cost \(4\). The cap does not raise that design's heat from \(1.391\) to \(2.189\).

**The reading that the cap selects a distributed split. FAILS** in this class, at this heat and this upkeep. The degradation identity stays **PROVED**. The open miss is why the split looked cheaper: the comparison never included a replica that keeps the whole precision. Fragments that do not pool are a different object. A reader who keeps one survivor and throws the rest away cannot meet this cap for \(n\ge 2\), because one fragment of \(\mu=3\) has error at least \(4/(1+3/2)=1.6\). Beating that reader is not beating a copy. Item erasure is not a local memory plus spare copies of the decision.

**Capacity-limited units, stated before the numbers.** The copy advantage uses a unit that can hold the full precision. The class below drops that.

Each unit installs a precision \(\varphi\in(0,c]\) and pays that precision as heat, plus upkeep \(h\). Units fail independently with probability \(p\). A common shock of probability \(\beta\) downs every unit and otherwise leaves the independent failures. The cost is heat plus upkeep plus \(w\) times expected error. The cap is \(P(\mathrm{error}>\varepsilon_{\mathrm{cap}})\le\varepsilon_r\). A copy reader uses the best surviving unit and does not add precisions. A pool adds the precisions of the survivors.

*Prediction, fixed before the search in the checks.* On the same units, the pool's precision is at least the best single survivor's, so the pool's error is at most the copy's on every draw, and the heat and the upkeep match. The pool's cost is therefore at most the copy's. A copy made of one unit is feasible only when \(c\ge\mu_\star=V/\varepsilon_{\mathrm{cap}}-1\). Below that, no number of non-pooling copies meets the cap, and a pool can. A common shock with \(\beta>\varepsilon_r\) leaves both designs infeasible, because every design of these units is down on the shock. On a sum of \(K>1\) items, the same total precision aimed at the sum has error \(K/(1+\Phi)\), and the same precision spread across items has error \(K^2/(K+\Phi)\). The aimed sum is the smaller one.

*What the checks find.* The pathwise bound holds on the grid of caps, counts, stakes, and a shock of probability \(0.02\) that was written into the checker with the prediction. At \(V=4\), \(\varphi=5/3\), two units, \(p=0.2\), \(h=0.5\), \(w=1\), the copy costs \(5.933333\) and the pool of those same two units costs \(5.564103\). The boundary for a feasible one-unit copy is \(c=\mu_\star=5/3\): at \(c=1/2\) the up-state error is \(8/3>1.5\), so copies of one unit miss the cap at every count. Under this accounting the pool does not lose to copies. Copies are the cheaper instrument only in the accounting of the previous subsection, where a replica carries the whole precision and the heat is charged once, and that accounting needs \(c\ge\mu_\star\).

For the sum of four items, cap level \(2\), and \(c=1/2\), an item-diagonal code has all-up error \(16/(4+N/2)\). That is at most \(2\) only for \(N\ge 8\), so every feasible item design pays heat plus upkeep at least \(8\). The aligned pool meets the cap at \(4\) units, chance \(0.027200\), expected error \(1.583360\), cost \(5.583360\), which is already below that floor. The symmetric search, four units on each item, meets the cap at cost \(17.583360\), chance \(0.012412\), and the same expected error, because each item was given as many units as the whole pool. The cap does not reverse the ordering.

**What fails, restated.** "The cap selects distribution." **FAILS** when a unit can hold the decision's precision and a replica pays upkeep rather than a second heat. "Copies still win once units are capacity-limited, at equal heat and upkeep." **FAILS** by the pathwise bound: the pool of those units is at least as cheap, and it is the only feasible design when \(c<\mu_\star\). "Losing a unit can lower the error, inside this class." **FAILS**. The conjecture that some other code gains when a part is lost stays outside M-C and M-L.

**What to try next.** Not a lock. The capacity bound \(c\) is the piece this class can state and a circuit can measure. If a neuron, a worker, or a cell can be shown to hold the whole decision at the precision the cap requires, the copy is the design this accounting selects, and a split needs a different reason. If each unit's precision saturates below \(\mu_\star\), the pool is the design that can meet the cap, and the measurement is whether the survivors' precisions add. Silence a fraction \(f\) and fit the error to the two formulas. A curve that falls as \(f\) rises would be the conjecture outside this class, and it would be worth a model that is not a mean-square Gaussian channel.

## 5. The phone image

**Proposition M-rank (PROVED, identical modes).** Let \(U\) have rank \(r\). The number of modes the heat-optimal memory tracks is the number of eigenvalues above \(kT a/(vw)\), which is at most \(r\), at every ambient dimension \(K\ge r\). The cost does not depend on \(K\) beyond those eigenvalues. At \(K=100\), two eigenvalues equal to \(1\), and the rest \(0\), stake \(4\), the memory uses \(2\) directions and the cost is \(6\), equal to the cost of those two modes alone.

At matched error \(\varepsilon\) on each of \(r\) orthonormal readouts of identical modes, the heat floor is \(r\,kT\,a(v-\varepsilon)/\varepsilon\). A local code that holds all \(K\) items at that same marginal error, for a tight task of rank \(r\), pays \(K/r\) times that heat. The ratio is the one in §3.

**Proposition M-scale (PROVED, one scalar signal of variance \(V\)).** The heat-optimal error is \(\sqrt{kT\,a\,V/w}\) when that lies below \(V\), and \(V\) otherwise. A mutual-information price \(\kappa\cdot\tfrac12\log(V/\varepsilon)+w\varepsilon\) has error \(\kappa/(2w)\) when that lies below \(V\). On stakes \(2,4,8,16,32\) the log-log slopes are \(-1/2\) and \(-1\). At stake \(4\) and \(\kappa=kT=1\), raising the drift from \(1\) to \(5\) multiplies the heat-optimal error by \(\sqrt{5}=2.236068\) and leaves the nat-priced error unchanged.

**Unit conversion, not a measurement of a phone.** Boltzmann's constant times \(300\,\mathrm{K}\) is \(1.380649\times 10^{-23}\times 300=4.141947\times 10^{-21}\,\mathrm{J}\). At drift \(1\) per second and \((v-\varepsilon)/\varepsilon=1\), a billion decision modes have floor \(4.141947\times 10^{-12}\,\mathrm{W}\). The assumptions that license that figure are the memory-bath floor, the fast-memory infimum, equilibrium cancellation of the signal bath, drift one per second, rank \(10^9\), and temperature \(300\,\mathrm{K}\). The two springs at rate \(10^5\) sit above their static rate, heat \(5.39980915\) against \(5.40000000\), so a finite-rate memory is not on the floor. Replacing the drift by \(10^9\) per second and the rank by \(10^{12}\) produces \(4.141947\,\mathrm{W}\). That second figure treats \(a\) as a clock and the rank as a parallel width. The theorem does not. The drift in the floor is the drift of the world signal. A static map, \(a\to 0\), has floor \(0\) at every rank, by the equilibrium cancellation already proved. Compression is not what makes a frozen map cheap. Drift is what makes a live one expensive, and only on the modes the decision uses.

**What this does not show.**

- It does not show that a frontier model fits in a phone's memory or within a phone's power.
- It does not bound a parameter count, a training run, or a weight matrix. The floor is a heat rate for holding a conditional law, not a stock of bits. The Gaussian stock of one mode is \(\tfrac12\log(v/\varepsilon)\), which is Kolmogorov's object. The heat is \(kT a(e^{2I}-1)\) once that stock is \(I\). A small stock can sit next to a large path rate; the fast spring in the attainability note already has path rate \(999.503\) at heat \(4.000020\).
- It does not say that the decisions of a real model are low-rank, or that its world is an equilibrium Ornstein–Uhlenbeck signal.
- A watt figure obtained by calling \(a\) a clock rate is not an application of the floor.

The sentence "a holographic memory lets a frontier model run on a phone" is **METAPHOR**. The proved substitute is the rank bound and the watt conversion under a stated drift.

**What to try next.** Not a lock. For one task whose decision rank and whose drift can be estimated independently of the model that serves it, compare power, not parameter count, to \(kT\sum_i a_i(v-\varepsilon_i)/\varepsilon_i\) while the drift is varied and the error is held fixed. Power linear in that drift, and insensitive to ambient dimension once the rank is fixed, would match the floor. Power tracking the parameter count, or independent of the drift, would not. A phone-battery comparison is not that measurement.

## 6. Predictions, and where they can still diverge

Each claim is something a measurement could refute. Agreement with a published coding result is recorded as convergence. The follow-up uses the heat, the drift, the stake, or the cap, which that result does not price. Nothing here is a preregistration.

**Place cells and grid cells.**

Mathis, Herz, and Stemmler, abstract fetched, take place cells as spiking at one location and grid cells as spiking on a hexagonal lattice, and they find that an optimized grid code has higher spatial resolution than a place code under Fisher information, with a tradeoff against range. Hafting and coauthors, abstract fetched, report the lattice, the shared orientation, and the differing phases. O'Keefe and Dostrovsky are cited for the title of the spatial-map paper; no abstract was in the records fetched, and no sentence about one location is taken from them. Sreenivasan and Fiete, abstract fetched, read the grid as an analog error-correcting code whose accuracy under noise sits outside the class of the sensory and motor population codes they compare.

*Claim, as a heat statement.* Where the decision is position, a low-dimensional quantity, a periodic code has a lower heat than one slot per place at the same position error, and the ratio grows with the number of places the local code keeps. The error at the optimum scales as \(\sqrt{a/w}\).

*What would refute it.* At matched position error, a place-only population with a lower measured heat than a grid population, on a task that is only the position estimate. Or an error-versus-stake slope of \(-1\), with no change when the environment's rate of change is varied.

*Convergence.* The resolution ranking is already Mathis, Herz, and Stemmler. The robustness reading is already Sreenivasan and Fiete. That agreement is support. It does not distinguish GTAO from efficient coding or from an error-correcting-code account. Label for the ranking: **KNOWN**.

*Where a divergence can be looked for.* Fisher information has no drift \(a\) and no stake power \(-\tfrac12\). Metabolic power linear in the speed of environmental change, at fixed position error, would match the heat floor. Power independent of that speed would match a nat price or a pure resolution objective. Label for that power law: **CONJECTURE**.

*What to try next.* A power measurement on grid and place populations at matched position error, with the animal's or the world's rate of change varied. The slope against that rate is the discriminator. The existence of both codes is not: §3 already says a per-item question (is the animal at this place?) keeps a local code, and a position estimate keeps a shared one. A dataset that cannot separate those two decisions cannot separate the memories.

**The fly mushroom body.**

Caron, Ruta, Abbott, and Axel, abstract fetched: Kenyon cells encode odours as sparse distributed patterns, and each traced cell integrates an apparently random combination of glomeruli, with no organization by tuning, anatomy, or origin. Dasgupta, Stevens, and Navlakha, abstract fetched: the circuit solves similarity search by a variant of locality-sensitive hashing. The abstract does not list the three strategies it mentions.

*Claim.* In the class of §3, random projections beat fixed slots when a few features are active and the readout names them (\(1.205\) against \(3.333\) at the worked point), and they lose when every coordinate is active (\(3.942\) against \(2.667\)). A Kenyon-cell expansion that does not change the conditional law of the odour given the decision does not add heat at the floor: an equilibrium coordinate the action ignores has heat \(0\), which is the cancellation already proved.

*What would refute it.* A complete, non-random glomerular map onto Kenyon cells, against Caron's report. Or a metabolic cost of the Kenyon-cell layer that scales with the cell count at fixed identification error and fixed odour drift.

*Convergence.* The random convergence and the hashing reading are already those two papers. Label: **KNOWN**. The heat sentence is the floor applied to a coordinate the decision ignores. Calling that sentence a new discovery about the fly is **METAPHOR** until the power measurement exists.

*Where a divergence can be looked for.* A cost per spike charges the expansion whether or not the odour world is drifting. The heat floor charges the learning rate, which tracks the drift. Olshausen and Field, abstract fetched, obtain localized fields by maximizing sparseness, for statistical independence. Their objective is not this heat. A layer whose metabolic rate is large at zero drift fits a per-spike cost and the sparse-code objective better than the floor.

*What to try next.* Power of the Kenyon-cell layer against the rate of change of the odour, at fixed identification error. Linear in that rate favors the floor. Flat in that rate, and proportional to cell count, favors a per-cell cost.

**Ant colonies.**

A Europe PMC search on 22 November 2026 for "ant colony distributed memory" did not return a title that states a distributed colony memory of the kind in the question. No ant paper is cited. No numerical claim about ants is made.

*Claim, as a proposal.* If the colony's decision is one sum, and workers fail, a split in which every worker carries a weak copy of that sum should follow the smooth curve of §4. A specialist for each site should lose sites outright.

*What would refute it.* Ablating a fraction of workers erases particular sites and leaves others intact, on a decision that is a single sum. Or the error falls smoothly, on a decision that requires every site separately, with no failures.

*Overlap.* If the observation is only that more workers are used when failure is likely, that is CT37, **KNOWN** in this repository, and the holographic name is **METAPHOR** for that observation. The discriminator is the shape of the error curve, which is **PROVED** as an identity and **CONJECTURE** as a description of a colony.

*What to try next.* An ablation curve. Fit it to the two formulas in §4 before any stronger claim.

**Superposition in trained networks.**

Elhage and coauthors, abstract fetched: polysemanticity arises from storing additional sparse features in superposition, and there is a phase change. The abstract does not give the location of the phase change, and none is imported.

*Claim.* The linear-Gaussian calculation does not reproduce that phase change from sparse queries. At \(K=12\), a subset of size \(2\) has high-stake cost ratio \(1.008218\). The known-support calculation does cut the error, from \(3.333\) to \(1.205\), when the readout names four active items out of \(32\). The two uses of "sparse" are different objects. Treating them as one phrase was the confusion, and the calculation is what separates them.

*What would refute the divergence.* In a heat-priced toy model, sweeping stake and drift leaves the superposition boundary where a hard width constraint puts it, and the error scales as \(1/w\).

*Labels.* Their phase change, as stated in the abstract: **KNOWN**. The identity of that phase change with the stake window of §3: **FAILS**. The square-root scaling: **PROVED** in the Gaussian class. Whether a trained network shows it: **CONJECTURE**.

*What to try next.* The toy-model sweep in §3. Report the error against stake on a log-log plot, and against drift at fixed stake, for the heat price and for the nat price on the same features. The slopes are the result. A boundary that moves only with sparsity and width, and not with those slopes, would say the heat price is idle in that model.

## 7. What this note does not do

It does not edit `THEORY.md`, `CORE.md`, `README.md`, or the hypothesis sentence. It does not adopt \(J_{\mathrm{phys}}\) into the master equation. It does not close the open rows of the heat notes. It does not rerun the spacetime draft or T20. It does not import a compressed-sensing measurement count, a Hopfield capacity, or a \(0.14N\) figure: Amit, Gutfreund, and Sompolinsky were fetched, the abstract was empty, and the title's "infinite numbers" is not that figure, so the paper is not cited as a capacity theorem. It does not score a fly, a rat, an ant, or a network. Those are the follow-ups above, and they are not locks.

## 8. Checks

`theory/holographic_memory_checks/memory_checks.py`. 96 checks, FAILS 0. The numbers in §§3–5 are the numbers it prints.

## 9. References

Fetched this session. Abstracts from Europe PMC unless the line says otherwise. Crossref HTTP 200 for every DOI.

Volume and page are omitted. The locator is the DOI that Crossref returned.

van Heerden, P. J. 1963. Theory of optical information storage in solids. *Applied Optics*. doi 10.1364/AO.2.000393. No abstract in the Crossref record. Cited for the title.

Plate, T. A. 1995. Holographic reduced representations. *IEEE Transactions on Neural Networks*. doi 10.1109/72.377968.

Kanerva, P. 2009. Hyperdimensional computing: an introduction to computing in distributed representation with high-dimensional random vectors. *Cognitive Computation*. doi 10.1007/s12559-009-9009-8. No abstract in the Crossref record. Cited for the title.

Hopfield, J. J. 1982. Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*. doi 10.1073/pnas.79.8.2554.

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., and Olah, C. 2022. Toy models of superposition. arXiv:2209.10652. Abstract and these sixteen names from the arXiv API. Crossref returned HTTP 404 for doi 10.48550/arXiv.2209.10652 on 22 November 2026. Not cited as that DOI.

Candès, E. J., and Tao, T. 2006. Near-optimal signal recovery from random projections: universal encoding strategies? *IEEE Transactions on Information Theory*. doi 10.1109/TIT.2006.885507. No abstract in the Crossref record. The recovery bound is not restated.

Donoho, D. L. 2006. Compressed sensing. *IEEE Transactions on Information Theory*. doi 10.1109/TIT.2006.871582. No abstract in the Crossref record. The measurement count is not restated.

Caron, S. J. C., Ruta, V., Abbott, L. F., and Axel, R. 2013. Random convergence of olfactory inputs in the Drosophila mushroom body. *Nature*. doi 10.1038/nature12063.

Dasgupta, S., Stevens, C. F., and Navlakha, S. 2017. A neural algorithm for a fundamental computing problem. *Science*. doi 10.1126/science.aam9868.

Hafting, T., Fyhn, M., Molden, S., Moser, M.-B., and Moser, E. I. 2005. Microstructure of a spatial map in the entorhinal cortex. *Nature*. doi 10.1038/nature03721.

O'Keefe, J., and Dostrovsky, J. 1971. The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. *Brain Research*. doi 10.1016/0006-8993(71)90358-1. Cited for the title. No abstract was fetched.

Sreenivasan, S., and Fiete, I. 2011. Grid cells generate an analog error-correcting code for singularly precise neural computation. *Nature Neuroscience*. doi 10.1038/nn.2901.

Mathis, A., Herz, A. V. M., and Stemmler, M. 2012. Optimal population codes for space: grid cells outperform place cells. *Neural Computation*. doi 10.1162/NECO_a_00319.

Olshausen, B. A., and Field, D. J. 1996. Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*. doi 10.1038/381607a0.

Heanue, J. F., Bashaw, M. C., and Hesselink, L. 1994. Volume holographic storage and retrieval of digital data. *Science*. doi 10.1126/science.265.5173.749.

Kolmogorov, A. N. 1956. On the Shannon theory of information transmission in the case of continuous signals. *IRE Transactions on Information Theory*. doi 10.1109/TIT.1956.1056823.

Sims, C. A. 2003. Implications of rational inattention. *Journal of Monetary Economics*. doi 10.1016/S0304-3932(03)00029-1.

Horowitz, J. M., and Esposito, M. 2014. Thermodynamics with continuous information flow. *Physical Review X*. doi 10.1103/PhysRevX.4.031015.

Gabor, D. 1948. A new microscopic principle. *Nature*. doi 10.1038/161777a0. Fetched. Not used as a memory result.
