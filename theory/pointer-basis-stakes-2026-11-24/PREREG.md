# PREREG: does a stake move the record basis off the dephasing axis?

*Tuesday 24 November 2026, America/New_York. Written and committed before the scored derivation and before any results script. Branch `forge-pointer-basis-stakes`, cut from upstream `main` `0f3791890078161a1172277162df5ac13ebbff46`. `THEORY.md` is not edited. No pull request. This file is locked by that commit. Anything computed after it, and any change to the criteria below, is a deviation and is logged in `MEMO.md`.*

Open-work id reserved here, assigned when the row is written: **T70**. T69 is already used, for four different items, on `origin/forge-composite-contest`, `origin/forge-constants-exchange-rates`, `origin/forge-info-causality`, and `origin/forge-layer-fixed-point`. No open branch examined carries T70.

## 0. Question

A qubit undergoes pure dephasing. The memory chooses a record basis at an angle \(\theta\) from the dephasing axis and carries a stake \(w\) on an observable. Two questions, scored separately:

- **(A)** At complete dephasing, is every cost-minimizing \(\theta\) the sieve basis \(\theta=0\), for every stake and every observable angle on the grid?
- **(B)** At partial dephasing, does a stake on an observable that does not commute with the dephasing axis move the minimizing \(\theta\)?

This is a comparison with the predictability sieve and with quantum Darwinism. It is not the record-count headwind in `WALLS_REVIEW.md:65` on upstream branch `ace-probe-memos-2026-11-23` (commit `e3e0e70116fc9cabce11af7e1c25d93d18405b0b`). That line is a count of real parameters, \(K=N^2\) against \(N\), at one Holevo cap. This note does not vary dimension and does not use that count.

Already known, and not scored as a result: with relative entropy as the price of a non-commuting change, a qubit of Bloch radius \(0.6\) pays more than the squared-radius accuracy returns. The identity is
\[
D=\frac{r}{2}\ln\frac{1+r}{1-r}\Big|_{r=0.6},\qquad r^2=0.36.
\]
At three decimals \(D\) is \(0.416\). There is no stake grid and no dephasing channel in that comparison. The script may print the identity as a label. It is not (A) or (B).

## 1. Why the quantum record price is a modeling choice

Theorem R1 (`CORE.md:52`) fixes the memory coordinate as mutual information in the sense of A6: finite-law Shannon information on finite alphabets, and, when the mutual information is finite, the Gelfand–Yaglom–Dobrushin supremum of discrete mutual informations. That is a classical record. It does not fix the price of a quantum record. A8, in the same sentence, requires the prices that do enter the sum to be nonnegative. It does not choose which nonnegative quantum price is the memory coordinate.

The duel on that same upstream branch priced the quantum record by Holevo \(\chi\) (`theory/probes-2026-11-23/duel/PREREG.md:27`, P-info). This note does not adopt that price as the default. It states a different one, and it scores Holevo beside it. If (A) or (B) changes truth value when the price is swapped, the outcome is a pricing artifact: the grid did not decide the question, the choice of price did.

**Chosen price \(P_D\).** The mean Umegaki relative entropy of the record-making pinch on the post-dephasing state,
\[
P_D(\theta)=\mathbb{E}\big[S(\Phi_\theta(\rho))-S(\rho)\big]= \mathbb{E}\big[D(\rho\,\|\,\Phi_\theta(\rho))\big].
\]
For a pinching map the two expressions are equal. \(P_D\ge 0\), so the choice sits inside A8. Reason: the predictability sieve's own score is entropy produced under the environment, and the classical learning-rate floor is a flux of Kullback–Leibler divergences (Horowitz and Esposito 2014, doi `10.1103/PhysRevX.4.031015`, already the floor at `CORE.md:70`). \(P_D\) is that divergence for the map that writes the record. It is a modeling choice, not a theorem, and it is not Holevo \(\chi\).

**Holevo price \(P_\chi\).** The record kept is the classical outcome \(M\). Its Holevo quantity equals the Shannon mutual information \(I(W;M_\theta)\), which is nonnegative. This is the duel's P-info applied to a record that the measurement has already made classical. The Holevo quantity of the ensemble *before* the measurement does not depend on \(\theta\) and is not used: it does not price the basis the memory chose.

**Cost.** \(\kappa=1\). Ruin is slack and is not in the sum. For each price \(P\in\{P_D,P_\chi\}\),
\[
J_P(\theta)= P(\theta)+ w\, L(\theta).
\]
\(L\) is defined in §2. The currency of \(w\) is the currency of \(P\). Nothing here sets \(w\) from temperature.

## 2. Model (class PB)

One qubit. Pure dephasing in the \(z\) basis multiplies the \(x\) and \(y\) Bloch components by \(\gamma\in\{0,1/2\}\) and leaves \(z\) alone. \(\gamma=0\) is complete dephasing, the sieve's long-time limit. \(\gamma=1/2\) is partial: a transverse component survives, so a move in \(\theta\) is not closed by the channel. \(\gamma=1\) is out of scope. With no dephasing, the sieve has nothing to select.

**World.** \(W\) is uniform on four labels \(\{+z,-z,+x,-x\}\). Pre-dephasing Bloch vectors, radius \(r=0.6\):
\[
+r\hat z,\; -r\hat z,\; +r\hat x,\; -r\hat x.
\]
The radius is the radius of the excluded comparison in §0, so this note does not introduce a second one.

**Record.** The memory chooses \(\theta\in[0,\pi/2]\) and measures \(n(\theta)\cdot\sigma\) with \(n(\theta)=(\sin\theta,\,0,\,\cos\theta)\). One projective shot. Outcome \(M\in\{+1,-1\}\). The dephasing axis is \(\theta=0\).

**Stake.** Observable \(A(\phi)=\sin\phi\,\sigma_x+\cos\phi\,\sigma_z\). The target on label \(W\) is the pre-dephasing expectation \(y_W=r\, n_A\cdot u_W\). The action \(\hat a(M)\) is the conditional mean \(\mathbb{E}[y\mid M]\). The loss is the mean squared error
\[
L(\theta)=\mathbb{E}\big[(y-\hat a(M))^2\big].
\]
\(\phi=0\) commutes with the dephasing axis. \(\phi=\pi/4\) and \(\phi=\pi/2\) do not. \(\phi=\pi/2\) is fully complementary.

**Grid.** \(\phi\in\{0,\pi/4,\pi/2\}\), \(w\in\{0,10^{-2},10^{-1},1,10,100\}\), both prices, both \(\gamma\). Angle grid: \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\), \(j=0,\ldots,720\). Deterministic. No random numbers. The script sets `SEED = 20261124` and does not draw from it.

**Minimizer.** A grid point is minimal when its cost is within \(10^{-9}\) of the smallest cost on that grid. "\(\theta=0\) is the unique minimizer" means \(\theta_0\) is minimal and no other grid point is.

### Closed form at \(\gamma=0\) (part of the model, checked by C0)

After complete dephasing the \(\pm x\) states are maximally mixed and the \(\pm z\) states have Bloch length \(r\). With \(h\) the binary entropy in nats and \(h(0)=h(1)=0\),
\begin{align*}
P_D(\theta)&=\tfrac12\Big[h\big(\tfrac{1+r|\cos\theta|}{2}\big)-h\big(\tfrac{1+r}{2}\big)\Big],\\
P_\chi(\theta)&=\tfrac12\Big[\ln 2-h\big(\tfrac{1+r|\cos\theta|}{2}\big)\Big],\\
L(\theta)&=\tfrac{r^2}{2}-\tfrac{r^4\cos^2\phi\cos^2\theta}{4}.
\end{align*}
\(P_D\) is zero only at \(\theta=0\) on \([0,\pi/2]\) and increases with \(|\theta|\). \(P_\chi\) is largest at \(\theta=0\) and is zero at \(\theta=\pi/2\). \(L\) decreases in \(|\cos\theta|\) when \(\cos\phi\neq 0\), and does not depend on \(\theta\) when \(\cos\phi=0\).

## 3. Predictions, and an input that fails each one

Each prediction is a statement about the grid in §2. The failing input is a cell, or a pair of cells, on which the statement is false. The script does not drop a cell.

**P1.** At \(\gamma=0\) and price \(P_D\), \(\theta=0\) is the unique minimizer for every \((w,\phi)\) on the grid. *Fails if* any one of those \(18\) cells has a minimizer at \(\theta\ge 0.02\), or a second grid point within \(10^{-9}\) of the minimum.

**P2.** At \(\gamma=1/2\), \(\phi=\pi/4\), price \(P_D\), the minimizing angles at \(w=0\) and at \(w=100\) differ by at least \(0.2\) rad, and the cost at \(\theta=0\) for \(w=100\) exceeds the minimum by at least \(10^{-4}\). *Fails if* those two angles differ by less than \(0.2\), or the cost gap is below \(10^{-4}\).

**P3.** At \(\gamma=1/2\), \(\phi=0\), price \(P_D\), \(\theta=0\) is the unique minimizer for every \(w\) on the grid. *Fails if* any of those six stakes has a minimizer at \(\theta\ge 0.05\).

**P4.** Let \(Q(P)\) be the predicate "at \(\gamma=0\), \(\theta=0\) is the unique minimizer for every \((w,\phi)\)". Then \(Q(P_D)\) is true and \(Q(P_\chi)\) is false. *Fails if* the two truth values are equal.

**P5.** At \(\gamma=1/2\), \(\phi=\pi/2\), price \(P_D\), the minimizer at \(w=0\) is \(\theta=0\), and the minimizer at \(w=100\) has \(\theta\ge 1.0\) rad. *Fails if* the \(w=0\) minimizer has \(\theta\ge 0.05\), or the \(w=100\) minimizer has \(\theta<1.0\).

**P6.** At \(\gamma=1/2\), \(\phi=\pi/4\), price \(P_\chi\), the minimizing angles at \(w=0\) and at \(w=100\) differ by at least \(0.2\) rad. *Fails if* they differ by less than \(0.2\). This asks whether the tilt boolean in P2 flips under Holevo. It is not required for the headline rule, and it is scored.

**Effect size this grid is built to resolve.** A basis move smaller than \(0.2\) rad (about \(11.5^\circ\), about \(46\) grid steps) does not count, and a cost gap below \(10^{-4}\) does not count. A gap of that size is a different record basis, not a tie on a flat cost.

### Headline rule (code-scored)

| Predicates | Label |
|---|---|
| P4's flip is observed (\(Q\) differs by price) | `PRICING_ARTIFACT` |
| P4 does not flip, P1 holds, and P2 does not | `RELABEL` |
| P4 does not flip, P1 holds, P2 holds, and P6 holds | `TILT` |
| anything else | `UNRESOLVED` |

`PRICING_ARTIFACT` and `RELABEL` are the two failure modes named for this question. Both are results. `UNRESOLVED` is a puzzle to diagnose, not a dropped question. The predicted label, written before the scored run, is **`PRICING_ARTIFACT`**: P1–P6 all hold, and the headline follows from P4.

What would make that prediction false is the failing input of P4, or a failure of P1–P3 or P5–P6 if those are needed to read the table. The script prints the label from the table only. It does not overwrite a mismatch with the predicted word.

## 4. Code-scored checks

Script `theory/pointer_basis_stakes_checks/pointer_basis_stakes_checks.py`, standard library only. It prints one line per check, then `HEADLINE <label>`, then `FAILS <n>`, and `ALL T70 CHECKS PASS` only when \(n=0\).

| Check | Scores | Pass |
|---|---|---|
| C0 | \(\gamma=0\) grid against the three closed forms, every grid \(\theta\), every \(\phi\), absolute error | max error \(\le 10^{-12}\) |
| C1 | P1 | P1 true |
| C2 | P2 | P2 true |
| C3 | P3 | P3 true |
| C4 | P4 | P4 true |
| C5 | P5 | P5 true |
| C6 | P6 | P6 true |
| C7 | headline | the table's label equals the label implied by C1–C6, and a mismatch of any of P1–P6 does not print the predicted word in place of the table |

C0–C7 failing means the preregistered prediction or the closed form is wrong. That is reported as a puzzle in the memo. The script is not edited to make a check pass, except for a bug that does not change a criterion; any such edit is a deviation.

A stored stdout, `pointer_basis_stakes_checks.out`, is compared byte for byte by `tools/test_pointer_basis_stakes.py`.

## 5. Prior-art log (done before the scored run)

### 5.1 Repository grep

On this branch, which is upstream `main` `0f37918`, before any results file existed:

```
git grep -n -i -E 'predictability sieve|pointer basis|quantum Darwinism|einselection' -- '*.md' '*.py'
```

No matches.

```
git grep -n -i Holevo -- '*.md'
```

The maintained hit that bears on a quantum memory coordinate is `theory/DIRECTIONS_2026-11-22.md:58`: a conjecture that the frontier form carries over with a Holevo bound. It names no dephasing model and no stake on a basis. It is not this test.

On `upstream/ace-probe-memos-2026-11-23` (`e3e0e70`), the same sieve pattern matches one line: `theory/probes-2026-11-23/WALLS_MEMO.md:188`, which calls quantum Darwinism a record-count economy. The phrases "predictability sieve", "pointer basis", and "einselection" do not occur there. The two citations this note is required to keep in view, and not to build on, are:

- `theory/probes-2026-11-23/reviews/WALLS_REVIEW.md:65` — the \(K=N^2\) headwind at a Holevo cap.
- `theory/probes-2026-11-23/duel/PREREG.md:27` — Holevo \(\chi\) as the quantum stand-in for the memory coordinate.

A search for the token `0.416` on the remote branches hits numeric dumps in older keystone and bridge outputs. None of those files is a qubit dephasing model. The excluded comparison in §0 is not a stored result of this repository.

### 5.2 Crossref (API, 24 November 2026)

Direct work lookups. User-Agent `theory-repo-prereg/1.0`. All six returned HTTP 200 and the bibliographic fields below.

| DOI | Crossref title | Author, issued, container |
|---|---|---|
| `10.1103/PhysRevLett.70.1187` | Coherent states via decoherence | Zurek, Habib, Paz. 1 March 1993. *Physical Review Letters* 70(9), 1187–1190 |
| `10.1143/ptp/89.2.281` | Preferred States, Predictability, Classicality and the Environment-Induced Decoherence | Zurek. 1 February 1993. *Progress of Theoretical Physics* 89(2), 281–312 |
| `10.1038/nphys1202` | Quantum Darwinism | Zurek. March 2009. *Nature Physics* 5(3), 181–188 |
| `10.1103/PhysRevLett.93.220401` | Objective Properties from Subjective Quantum States: Environment as a Witness | Ollivier, Poulin, Zurek. 22 November 2004. *Physical Review Letters* 93(22). Page field empty; the article number is the DOI suffix |
| `10.1103/PhysRevA.72.042113` | Environment as a witness: Selective proliferation of information and emergence of objectivity in a quantum universe | Ollivier, Poulin, Zurek. 31 October 2005. *Physical Review A* 72(4). Page field empty; article number in the DOI |
| `10.1038/ncomms8908` | Generic emergence of classical features in quantum Darwinism | Brandão, Piani, Horodecki. 12 August 2015. *Nature Communications* 6(1). Page field empty |

The DOI `10.1143/PTP.89.281` resolves to the same PTP paper as `10.1143/ptp/89.2.281`.

Bibliographic query `predictability sieve Zurek`, `rows=5`, returned `total-results` 29702 (a broad query, not a hit count). The first three items were:

- `10.1103/physreva.72.062101`, "Predictability sieve, pointer states, and the classicality of quantum trajectories", December 2005, *Physical Review A*. Confirmed on a direct lookup: D. A. R. Dalvit, J. Dziarmaga, W. H. Zurek, *Phys. Rev. A* 72(6), issued 1 December 2005. Page field empty.
- `10.1103/physrevd.53.7327`, "Decoherence of quantum fields: Pointer states and predictability", 15 June 1996, *Physical Review D*. Confirmed: J. R. Anglin, W. H. Zurek, *Phys. Rev. D* 53(12), 7327–7335.
- `10.1143/ptp/89.2.281`, the PTP paper above.

PRL 70:1187 was not in those five items. An earlier bibliographic attempt returned HTTP 429 and was retried once; the retry is the query recorded here. No further pages were fetched.

**What the check changes in the citation.** The pointer given for this question was "Zurek's predictability sieve (PRL 70:1187, 1993)". Crossref does not support that title for that DOI. PRL 70:1187 is Zurek, Habib, and Paz, "Coherent states via decoherence": states are selected by minimal entropy increase under an environment. The paper that names the predictability sieve is Zurek, *Progress of Theoretical Physics* 89:281 (1993). Both are used below under those titles. Quantum Darwinism, as a named account of redundant records, is Zurek, *Nature Physics* 5:181 (2009). The witness papers (Ollivier, Poulin, Zurek 2004 and 2005) and the generic-emergence theorem (Brandão, Piani, Horodecki 2015) are the published statements that the classical record is fixed by the interaction and is redundant for the pointer observable. None of those abstracts, as returned by the title lookup, states a stake \(w\) on a non-commuting observable inside a priced sum \(P+wL\). No claim is made that a stake-dependent basis is absent from the literature beyond this query and the repository grep. A miss in a five-row query is not a novelty proof.

### 5.3 Scratch used to choose the ensemble

While fixing the four-point ensemble, a scratch evaluation of \(J\) on a coarse \(\theta\) grid was run in an ephemeral interpreter. It was not kept, it is not a result, and no number from it is a criterion above. It was used only to reject an encoding in which every price is a function of one correlation, so that \(\theta\) cannot move except as a relabeling of how much information is bought. The scored run is the script in §4.

## 6. What this note will not say

It will not edit `THEORY.md`. It will not say that quantum mechanics, general relativity, or holography has been derived. Dephasing and the qubit are inputs. It will not call the hypothesis a law, and it will not say the question is solved. A miss is a puzzle. The record price is a cost. The walls headwind is not an input.
