# T80 preregistration: the ratio as a normal cone at a corner

*Tuesday 24 November 2026 (UTC). Written and committed before `corner_checks.py` and before any scored grid. Branch `forge-record-ratio-corners`, cut from `forge-record-ratio-bicausal` at `2df1925d96f7992b29eb2905fd32b1db36c9e6d8`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`, same commit. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md` and in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\). Ratio \(1\) means \(\kappa_D=\kappa\). Every statement about what an equilibrium does is a model implication, in-model.

## Why this approach

The independent review of T79 (`theory/reviews/REVIEW_BICAUSAL_INDEPENDENT.md` on `forge-bicausal-review` at `619983c`; fork PR #12) found no blocker and three limits under the headline. The one continuous pin, the singleton \(\{0.30\}\), has width \(1.65\times 10^{-4}\). That is near a point. The wide rationalizing sets are the equator-end formula \(R=[0,\ 1-w r^2]\). The parent's continuous best reply is \(0.6\) wherever \(P_D>0\).

**H-corner, Forge's hypothesis, not an axiom and not a result.** The ratio \(q=\kappa_D/\kappa\) is a Lagrange multiplier, a shadow price, of the record constraint \(\min(I+s L)\) at a fixed disturbance. Where the cost is smooth and the action menu is fine, the observed angle identifies \(q\) as a point. \(q\) opens into an interval only at a kink or a corner: a binding cap at the end of the disturbance range, the flat equator \(\phi=\pi/2\) (T77: the shadow price there is \(1\), and the ledger subdifferential is an interval), or a coarse action menu. On this reading the T79 set is the normal cone at a corner, not fundamental slack. The parent's \(0.6\) is not an input here. There is no return channel and no time-symmetric rate table.

P4 is a separate reading, from Chad: weight the same cells three ways and see whether a peak is shared. It is secondary. It is open to course-correction, as is H-corner.

## Can it fail

Can it fail: yes. A smooth interior cell can keep a wide rationalizing set on the finest grid, or a corner's set can miss the normal cone.

Cheapest way: one interior angle on the 513-point grid whose rationalizing width stays above \(5\times 10^{-3}\).

## 1. Objects

Reuse the antipodal closed form in `theory/record_ratio_reframes_checks/record_ratio_reframes_checks.py` (`closed_form_ant`), \(\gamma=0\), \(r=0.6\), \(\kappa=1\). Stake \(s=w/\kappa\). Angle \(\theta\in[0,\pi/2]\). Write \(u=\cos\theta\), \(\Lambda(u)=\ln\frac{1+ru}{1-ru}\), and

\[
A(\theta)=I(\theta)+s\,L(\theta),\qquad B(\theta)=P_D(\theta).
\]

Charged cost \(J(\theta;q)=A(\theta)+q\,B(\theta)\). Report window \(Q=[0,2]\). `SEED = 20261124` is set and not drawn from. The script imports no random module. No parent cost, no return share, no delay, no binary-entropy channel, and no reverse-rate copy of a forward rate.

**Grids.** Point counts \(N\in\{9,33,129,513\}\), endpoints included,

\[
\theta_j=j\cdot(\pi/2)/(N-1),\qquad j=0,\ldots,N-1.
\]

**Rationalizing set.** On a menu \(\{\theta_k\}\), action \(k\) is optimal at \(q\) when \(J(\theta_k;q)\le J(\theta_j;q)\) for every \(j\). With \(dB=B_k-B_j\) and \(dA=A_j-A_k\): if \(|dB|\le 10^{-15}\) and \(A_k>A_j+10^{-12}\), the set is empty; if \(|dB|\le 10^{-15}\) and \(A_k\le A_j+10^{-12}\), action \(j\) does not cut; if \(dB>0\), then \(q\le dA/dB\); if \(dB<0\), then \(q\ge dA/dB\). Intersect with \([0,2]\). \(R\) is that intersection. Width \(w=h-l\) when \(R=[l,h]\) is nonempty. A point has width \(0\). An empty set fails the cell.

**Independent multiplier, not read off \(R\).** For \(u\in(0,1)\),

\[
\lambda(u)=1-s\cdot\frac{2 r^3\cos^2\phi\cdot u}{\Lambda(u)}.
\]

Endpoint formulas, the same closed form at its limits:

\[
q_{\mathrm{eq}}=1-s r^2\cos^2\phi,\qquad q_{\mathrm{ptr}}=1-s\cdot\frac{2 r^3\cos^2\phi}{\ln\frac{1+r}{1-r}}.
\]

Normal cones scored inside \([0,2]\), an upper-cap multiplier taken nonnegative:

- equator \(\theta=\pi/2\), not flat: \([0,\ \min(2,\max(q_{\mathrm{eq}},0))]\).
- pointer \(\theta=0\), not flat: \([\max(q_{\mathrm{ptr}},0),\ 2]\).
- flat equator, \(|\cos\phi|\le 10^{-12}\) and \(\theta=\pi/2\): \([0,1]\).
- flat pointer, \(|\cos\phi|\le 10^{-12}\) and \(\theta=0\): \([1,2]\).
- flat interior, \(|\cos\phi|\le 10^{-12}\) and \(\theta\in(0,\pi/2)\): \(\{1\}\).

The T77 ceiling \(1-1/w_\star\) with \(w_\star=\ln\frac{1+r}{1-r}/(2r^3)\) is \(q_{\mathrm{ptr}}\) at \(\phi=0\), \(s=1\). The printed value `0.688377871168` is the comparison target. \(q_{\mathrm{eq}}(0,1)=1-r^2=0.64\).

## 2. Classifier

Applied to the installed angle and the menu. It does not read the width.

- `corner` if the installed angle is an endpoint of its menu (\(\theta=0\) or \(\theta=\pi/2\) on an interval grid; either end of the coarse menu), or the cell is one of the three coarse-menu actions. The equator endpoint is the binding cap: \(P_D\) is maximal there, and the cone above is the subdifferential of \(P_D\le P_D(\pi/2)\).
- `tie-point` if \(|\cos\phi|\le 10^{-12}\) and the installed angle is strictly inside \((0,\pi/2)\). Not smooth and not a corner.
- `smooth` otherwise: interior angle, \(|\cos\phi|>10^{-12}\), refinable interval menu.

An interior binding cap stays `smooth`. The cap selects the angle. It does not by itself open an interval.

## 3. Cells

Interval menu unless a row says coarse. \(\phi\) and \(s\) as written. The installed angle on grid \(N\) is the grid point nearest the target (absolute distance in \(\theta\); a tie takes the smaller \(\theta\)).

| family | how the angle is chosen | classifier the lock expects |
|---|---|---|
| smooth | \(\phi\in\{0,\pi/6,\pi/3\}\), \(s\in\{0.5,1,2\}\), target \(u\in\{0.3,0.7\}\), \(\theta=\arccos u\) | smooth, 18 cells |
| pin | \(\phi=0\), \(s=2\), target \(\theta=1.075559\) (the T79 singleton's angle) | smooth, 1 cell |
| cap | \(\phi=0\), \(s=1\), \(D\in\{0.02,0.05,0.08\}\). Feasible points have \(P_D\le D+10^{-12}\). Among them, minimize \(A\). Tie: smaller \(\theta\) | smooth, 3 cells |
| equator | \(\phi\in\{0,\pi/6,\pi/3\}\), \(s\in\{0.5,1,2\}\), \(\theta=\pi/2\) | corner, 9 cells |
| pointer | same \(\phi\), \(s\), \(\theta=0\) | corner, 9 cells |
| flat-equator | \(\phi=\pi/2\), \(s=1\), \(\theta=\pi/2\) | corner, 1 cell |
| flat-pointer | \(\phi=\pi/2\), \(s=1\), \(\theta=0\) | corner, 1 cell |
| flat-interior | \(\phi=\pi/2\), \(s=1\), \(\theta=\pi/4\) | tie-point, 1 cell |
| coarse | menu exactly \(\{0,\pi/4,\pi/2\}\), not refined, \(\phi=0\), \(s=1\), one cell per action | corner, 3 cells |

45 cells. If a cap or a smooth target lands on an endpoint, the classifier's rule wins over the expected column, and the cell is scored as what the rule says. That reclassification is a miss of the expected column and is printed. It is not a reason to edit this table.

## 4. Predictions

**G-form.** On \(\theta\in\{0,0.5,1,\pi/2\}\) and \(\phi\in\{0,\pi/2\}\), `closed_form_ant` and `functionals("ANT", 0, θ, φ)` differ by \(<10^{-9}\) in \(I\), \(P_D\), and \(L\).

*Fails if* any gap is \(\ge 10^{-9}\). Then this lock is not on the repo's menu. Do not replace the closed form.

**G-cone.** \(|q_{\mathrm{eq}}(0,1)-0.64|<10^{-15}\) and \(|q_{\mathrm{ptr}}(0,1)-0.688377871168|<10^{-9}\).

*Fails if* either gap is at least that tolerance. Do not refit \(r\).

**G-dyn.** On every cell, all 17 starts in §5 land on the same action.

*Fails if* any cell splits. A split means the discrete score has a basin the continuous score does not. Print the cell and the two landing indices.

**P1. Refinement.** On every cell the classifier marks `smooth`, with \(w_N\) the width of \(R\) on grid \(N\):

- \(w_{33}\le 1.25\,w_9\), \(w_{129}\le 1.25\,w_{33}\), \(w_{513}\le 1.25\,w_{129}\);
- \(w_{513}\le w_9/8\);
- \(w_{513}\le 5\times 10^{-3}\).

The floor is \(5\times 10^{-3}\). The overall shrink is a factor \(8\). A single step may rise by at most a quarter.

*Fails if* any smooth cell breaks one of those three lines. The falsifier named for this prediction is a smooth width on the 513-grid above \(5\times 10^{-3}\). Report the cell, the four widths, and the installed angles. A miss means the set did not close under refinement. The clue is whether the classifier's smooth mark is sitting on a kink the rule missed.

**P2. Corners.** Wide means width \(\ge 0.01\). On a refinable cell the width is \(w_{513}\). On a coarse cell it is the width of the one menu.

- every `smooth` cell has \(w_{513}<0.01\);
- every `corner` cell is wide;
- every `tie-point` cell has width \(\le 10^{-6}\).

*Fails if* a smooth cell is wide, a corner cell is not wide, or a tie-point is wider than \(10^{-6}\). The falsifier named for this prediction is a wide \(R\) in a cell the classifier marks smooth. The other two clauses are the converse the word "exactly" asks for. Report the cell, the mark, and the width.

**P3. Multiplier match.** Tolerance \(10^{-3}\). Compare \(R\) to the independent cone, on grid \(513\) for refinable cells and on the three-point menu for coarse cells.

- `smooth`: the midpoint of \(R\) and \(\lambda(u)\) at the installed grid angle differ by \(\le 10^{-3}\).
- `corner`: each endpoint of \(R\) and the matching endpoint of the cone in §1 differ by \(\le 10^{-3}\).
- `tie-point`: the midpoint and \(1\) differ by \(\le 10^{-6}\), already bounded by P2's width.
- coarse: \(R\) for this comparison is recomputed by a direct scan, \(q_i=i\cdot 10^{-4}\) for \(i=0,\ldots,20000\), action \(k\) kept when its cost is within \(10^{-12}\) of the minimum. The scan's min and max and the crossing endpoints differ by \(\le 10^{-3}\). The scan is not used for P1 or P2.

*Fails if* any cell exceeds its tolerance, or \(R\) is empty. Report the cell, both ends, and the gap. A miss means the set that rationalizes the angle is not the multiplier of the constraint.

**P4. Ensemble, secondary.** Chad's reading. Three schemes, one histogram each. None is fit to a T79 width, and none uses \(0.6\) as a center, a target, or a weight. Bins: 25 bins of width \(0.08\) on \([0,2]\), edges \(k\cdot 0.08\). A bin is left-closed and right-open, except the last, which is closed. A point sitting on an interior edge goes to the higher bin. Masses are normalized to sum to \(1\).

A bin is a **peak** when its mass is \(\ge 0.10\), it is at least each adjacent bin, and it is at least \(1.5\) times the mean of its existing neighbors. The **expected number** of peaks per scheme is \(2\). The pass band is the integers \(\{1,2,3,4\}\). A count of \(0\) or of \(5\) or more fails that scheme. **Concentration:** the scheme is concentrated when its heaviest bin has mass \(\ge 0.20\), and diffuse otherwise. Concentration is printed. It is not a pass-fail clause. A peak **counts** only when all three schemes find it, within the agreement rule below. Multimodal histograms are allowed.

Corner values, for the optional clause only: \(0\), \(1\), \(2\), and \(q_{\mathrm{eq}}(\phi,s)\), \(q_{\mathrm{ptr}}(\phi,s)\) at \(\phi\in\{0,\pi/6,\pi/3,\pi/2\}\) and \(s\in\{0.5,1,2\}\).

**(a) Equal weight.** For each cell, spread mass \(1\) uniformly on \(R\) (a point puts mass \(1\) in its bin). Sum over the 45 cells. This is the maximum-entropy weight on each set.

**(b) Dynamics.** Score \(C=I+s L\). No \(q\) in the score. Grid: the 33-point grid for interval cells; the three-point menu for coarse cells. Starts, asymmetric, quadratic, not mirrored about \(\pi/4\):

\[
\theta^{(k)}=(\pi/2)\,(k/16)^2,\qquad k=0,\ldots,16.
\]

Seventeen starts. On the coarse menu, snap each start to the nearest menu angle; a distance tie takes the smaller angle. From the current index, move to the neighbor with strictly smaller \(C\). Stop when neither neighbor is smaller by more than \(10^{-12}\), or after \(64\) steps. A neighbor tie within \(10^{-12}\) moves to the lower index. The recorded price is \(q_{\mathrm{eq}}\) if the landing is the equator end, \(q_{\mathrm{ptr}}\) if it is the pointer end, and \(\lambda\) at the landed angle otherwise, then clipped to \([0,2]\). Each cell contributes mass \(1\), split across its landings by the share of starts if a cell splits. `G-dyn` is the no-split gate. This scheme does not read \(R\).

**(c) Robustness.** Probes, quadratic, equally spaced in the square, not centered on a parent root:

\[
q_i=2\,(i/20)^2,\qquad i=0,\ldots,20.
\]

Twenty-one probes. For each distinct \((\phi,s)\) in the cell list, and each probe, the reference action minimizes \(J\) on the 129-point grid (tie: smaller \(\theta\)). Nine perturbations: \(\delta\phi\in\{-0.05,0,0.05\}\) with \(\phi'\) clipped to \([0,\pi/2]\), and \(\delta s\in\{-0.1,0,0.1\}\) (every locked \(s\) stays positive). A perturbation survives when the new minimizer is within two grid steps of the reference. Survival is the fraction of the nine. A probe's Voronoi weight is half the gap to each neighbor; the end probes use their one gap. A cell inherits the survival curve of its \((\phi,s)\). The histogram adds, for each cell and each probe, Voronoi weight times survival, into the probe's bin. This scheme does not read \(R\).

**Agreement.** Peak-index sets \(S_a,S_b,S_c\). An index \(i\in S_a\) is matched when some \(j\in S_b\) and some \(k\in S_c\) have pairwise absolute gaps at most \(1\). The representative is the median of \((i,j,k)\). Distinct medians are the agreed peaks. Pass when there is at least one.

**P4-corner, optional under H-corner.** Every agreed peak's bin center (left edge plus \(0.04\)) lies within \(0.08\) of a corner value. *Fails if* there is no agreed peak, or any representative is farther than \(0.08\) from every corner value. A miss means a shared peak is not sitting on a corner of this menu.

*P4 fails a scheme if* its peak count is outside \(\{1,2,3,4\}\). *P4-agree fails if* the matched count is \(0\). Report the three peak lists, the masses of those bins, the agreed medians, and whether each scheme is concentrated or diffuse. A miss is a puzzle about the weighting, not a reason to retune a threshold.

## 5. What a miss points to

P1: the discrete set did not close. If the cell is interior and the width stays put, the set is not a grid artifact.

P2: either a smooth cell is wide, so the classifier missed a kink, or a marked corner is narrow, so that corner does not open a cone of the size this menu produces.

P3: the rationalizing set and the multiplier of the constraint are not the same object on that cell.

P4: the three weights do not share a mode inside the locked band. The optional clause misses when a shared mode is away from the corner values. Neither miss removes H-corner or the distributional reading. Both stay open to course-correction.

## 6. What this run will not say

It will not edit `THEORY.md` or the T79 locks. It will not say that a value of the ratio has been obtained as a final answer. It will not treat a pass as a derivation of general relativity, quantum mechanics, holography, or gravity. It will not put the parent's \(0.6\) into a scheme after seeing the histogram. It will not add a cell, a grid, a threshold, or a start after seeing the output.

## 7. Output

One line per named check, `PASS` or `FAIL`, then `FAILS` and a count. Then one `CELL` line per cell: family, classifier mark, four widths or the coarse width, cone ends, midpoint gap. Stdout is stored and byte-compared by the test. `PREREG.md` is not read for numbers. `RUN_LOG.md` records every deviation and, if there is none, says so. `DEVIATIONS.md` is the same list, append-only. The memo uses the labels PROVED (in-model), NUMERICAL, and PUZZLE. The memo has an errata section. This file is not rewritten to absorb an erratum.
