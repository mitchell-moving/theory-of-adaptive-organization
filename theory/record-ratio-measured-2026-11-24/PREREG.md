# T81 preregistration: the record ratio as a measured return flow

*Tuesday 24 November 2026 (UTC). Written and committed before `measured_checks.py` and before any scored run. Branch `forge-record-ratio-measured`, cut from `forge-record-ratio-corners` at `eb372973a565840a1536211d1b4d1a0a60403ef3`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Locked by sha256 in `PREREG.sha256`, same commit. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md` and in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every statement about what the chain or the fixed point does is a model implication, in-model.

## Why this approach

T74 through T80 inferred the ratio \(q=\kappa_D/\kappa\) from behavior: the set of \(q\) that rationalizes a choice. A price read off a choice is generically a set. Ties, corners, and linearity of \(J\) in \(q\) are why those locks kept returning ranges.

That approach dropped the original definition. **Chad's framing, a hypothesis, not an axiom and not a result.** \(q\) is the share of destruction that comes back to cost whoever did it. That is a flow. It can be measured in a dynamics. It is not a preference fitted to an angle.

**Forge's pivot of that framing, open to course-correction.** Measure the flow. Do not infer \(q\) from which angle minimizes \(J\). T78's reading that \(q=0\) when destruction stays gone is the open-sink limit of this same flow. This lock keeps that limit. It does not discard it.

## Can it fail

Can it fail: yes. The collapse onto \(x=T/\tau_{\mathrm{mix}}\) can miss, the continuum shape between 0 and 1 can miss, the fixed-point iteration can cycle or split, and the closedness histogram can miss the curve implied by that collapse.

Cheapest way: two reservoirs at one nominal \(x\) whose measured returns differ by more than \(0.08\), or one interior fixed-point cell whose five starts do not land together.

## Circularity and what could fail

In a finite closed conserving world, a walker that can reach the agent reaches it with probability 1. A graph with no edge into the agent returns nothing. Those two limits are the ends of M1. They are checked, and a match is not evidence. The classes below are locked. The memo repeats them. It does not regrade a construction check as evidence after the run.

| Check | Could the locked bar have failed? | If it matches |
|---|---|---|
| M1-closed | No, given the closed graph below: finite path, both directions open inside, the far end reflects, the contact end is reachable. The probability of an eventual hit is 1. | holds by construction, not evidence |
| M1-sink | No, given the sink graph: the contact step is removed, so the agent counter stays at 0. | holds by construction, not evidence |
| M1-scale | Yes. At fixed horizon the hit probability need not fall with \(N\). | evidence |
| M2-collapse | Yes. Two pairs with the same nominal \(x\) can differ by more than \(0.08\). | evidence |
| M2-shape | Yes. The Fourier series is a continuum approximation, not an identity of the lazy chain. | evidence |
| M2-interior | Yes. The return at \(x=0.5\) and at \(x=1\) can sit near 0 or near 1. | evidence |
| M3-conv | Yes. Undamped iteration of a stepwise map can cycle, and five starts can split. | evidence |
| M3-corner | Yes. A corner cell can cycle and then it has not reached a fixed point. | evidence |
| M4 | Yes. Closedness can change how much ever returns, not only the clock \(x\). | evidence |
| E-pair | Not scored. | report only |

Existence of at least one root of \(\Phi(q)-q\), when \(\Phi\) is a continuous single-valued map of \([0,1]\) into itself, is the intermediate-value theorem. It is not evidence. M3 scores uniqueness and convergence only. The map below is stepwise, so that existence remark does not by itself supply a root of the iteration.

Monotonicity of a hitting probability in \(T\) is not scored. It holds by construction for the closed kernel.

## 1. Prior art

Checked on the Crossref API on 24 November 2026, HTTP 200, before this commit. No number is taken from these works. No page of a book is claimed.

- Landauer, R. Irreversibility and Heat Generation in the Computing Process. IBM Journal of Research and Development 5:183–191 (1961). doi `10.1147/rd.53.0183`. Erasing a record displaces entropy into the surroundings. That is why a destroyed record is placed in the environment as an excitation. The doi does not set \(q\).
- Kac, M. On the notion of recurrence in discrete stochastic processes. Bulletin of the American Mathematical Society 53:1002–1010 (1947). doi `10.1090/s0002-9904-1947-08927-8`. In a finite recurrent chain a state is visited again. That is the reason the closed-world limit of a cumulative hit is 1, and it is why that limit is marked construction rather than evidence.
- Poincaré, H. Chapitre II. Théorie des invariants intégraux. Acta Mathematica 13:46–88 (1890). doi `10.1007/bf02392508`. Classical source for recurrence of a measure-preserving flow. No page inside the chapter is claimed.
- Levin, D., Peres, Y., and Wilmer, E. Markov Chains and Mixing Times. American Mathematical Society, 2008. doi `10.1090/mbk/058`. The relaxation time \(1/(1-\lambda_2)\) and total-variation mixing are the vocabulary for \(\tau_{\mathrm{mix}}\). The gap below is computed on the decoupled environment, not copied from a table in the book.

## 2. World

A finite path. Agent region: sites \(0,1,\ldots,A-1\) with \(A=4\). Environment: \(N\) sites \(A,A+1,\ldots,A+N-1\). The path reflects at site \(0\) and at site \(A+N-1\). There is no second copy of any edge and no edge that skips a neighbor.

**Dynamics.** One excitation. Discrete-time lazy simple random walk. From an interior site, stay with probability \(1/2\), step to either neighbor with probability \(1/4\). A step that would leave an endpoint is held at that endpoint, so each endpoint stays with probability \(3/4\) and moves inward with probability \(1/4\). The transition matrix on the full path is symmetric and stochastic. The uniform measure is invariant. The walk is reversible. The excitation count is conserved. This is a finite Markov system with a conserved total. It is not a cellular automaton. The same kernel on \(W\) labeled excitations, run independently, is the product chain. The product still preserves the product of the uniform measures.

**No added return edge.** The only way an excitation enters the agent is the neighbor step from site \(A\) to site \(A-1\). That step is the contact already in the path. It is not a channel added so that \(q\) comes out at a chosen value.

**Start.** One site, or a block, in the environment. Index inside the environment \(j\in\{0,\ldots,N-1\}\), site \(A+j\). Reference site \(j_0=N//2\) (integer division). The start is a point mass on that site when \(W=1\). It is not the uniform measure. It is not the stationary distribution of the reversible chain. The forward kernel is not copied into a reverse table. This is the avoidance of the time-symmetric start: the mirror circularity in T79 `PREREG_3.md` (a real reference, symmetric looks, and the turn \(\tau=it\)), which put the conjugate in by the start. `SEED = 20261124` is set and not drawn from. The script imports no random module.

**Destruction.** Erasing a record of width \(W\) places \(W\) excitations on the contiguous environment sites centered at \(j_0\),

\[
j\in\{j_0-\lfloor W/2\rfloor,\ldots,j_0+\lfloor W/2\rfloor\}.
\]

On the locked grids this block lies inside \(\{0,\ldots,N-1\}\). If a site ever falls outside, it is dropped, the denominator is the number kept, and the drop is a deviation. Displaced cost \(C_{\mathrm{disp}}\) is the number of excitations placed, one unit each.

**Return, and the future record cost.** The blank record is the agent region with no excitation in it. An excitation that occupies an agent site has to be removed before the blank record is back. That removal costs one unit for that excitation. \(q(T)\) counts an excitation once, at its first entrance into the agent, because that is the moment the future reset cost rises by one unit. Excitations still in the environment have not raised that cost.

\[
q(T)=\frac{\#\{\text{excitations that have entered the agent by step }T\}}{C_{\mathrm{disp}}}.
\]

At \(T=0\), before any step, \(q=0\). Steps are \(1,\ldots,T\).

For independent excitations this is the average of the hitting probabilities of the starts. The underlying walk is the measure-preserving path. First-entrance probabilities may be computed by restricting the mass that has not yet hit: that restriction is an accounting identity for the same path, not a second world. `G-equiv` checks the identity on one small cell.

**Open sink.** The contact step from environment index \(0\) into the agent is removed. The outward quarter from that site goes to a sink counter and is not counted as a return. The agent counter stays at 0. This is T78's "destruction stays gone", kept as the open-sink control.

**Closedness \(c\in[0,1]\).** A property of the far end of the environment, not of the contact. From environment index \(N-1\), the outward quarter \(1/4\) is split: fraction \(c\) reflects (added to the stay), fraction \(1-c\) goes to the sink and is not a return. \(c=1\) is the closed path. \(c=0\) is a far-end hole. The contact step is unchanged by \(c\).

**Decoupled environment, used only for \(\tau\).** The agent sites are deleted. Both ends of the \(N\)-site path reflect, except that closedness, when it is not 1, leaks at the far end and the near end stays reflecting. This matrix does not contain an agent state and does not count hits. \(\tau_{\mathrm{mix}}(N)\) is computed only at \(c=1\) on this decoupled path.

## 3. Clocks, measured apart from the return

**Relaxation time.** Let \(P^{\mathrm{dec}}(N)\) be the decoupled reflecting matrix at \(c=1\). It is symmetric. Let \(\lambda_2\) be its second-largest eigenvalue. 

\[
\tau_{\mathrm{mix}}(N)=\frac{1}{1-\lambda_2}.
\]

This is the relaxation time in the sense of the mixing-time monograph cited above. It is not a hitting time. The return code is not an input.

**Closedness clock.** Let \(M(N,c)\) be the decoupled matrix with far-end leak \(1-c\) and a reflecting near end. It is symmetric. Let \(\rho(c)\) be its largest eigenvalue if \(c<1\), and its second-largest eigenvalue if \(c=1\).

\[
\tau(c)=\frac{1}{1-\rho(c)}.
\]

At \(c=1\), \(\tau(1)=\tau_{\mathrm{mix}}(N)\). The agent is not in \(M\). If the largest absolute entrywise difference between \(P^{\mathrm{dec}}\) and the return restriction at the same \(N\) is at most \(0.2\), `G-decouple` fails and the dependence is a puzzle in `DEVIATIONS.md`.

**Horizon.** For a nominal \(x>0\),

\[
T=\lfloor x\,\tau_{\mathrm{mix}}(N)+1/2\rfloor,
\]

and \(T\) is at least 1. Ties round half away from zero. A cell is unpaired when \(|T/\tau_{\mathrm{mix}}(N)-x|>0.02\). Unpaired cells are printed and left out of the collapse range and the shape range.

**Eigenvalues.** Jacobi rotations on the symmetric matrix, at most 80 sweeps, stop when the off-diagonal Frobenius norm is below \(10^{-12}\). A second estimate is the Rayleigh quotient of power iteration on the subspace orthogonal to the all-ones vector, 4000 steps, start vector \(v_i=\cos(\pi i/(N-1))\). `G-gap` fails if the two \(\tau_{\mathrm{mix}}\) values differ by more than \(10^{-8}\) on any locked \(N\), or if either method fails to finish.

## 4. Return kernel

Environment mass \(p_0,\ldots,p_{N-1}\). One step, closedness \(c\):

- Interior \(0<j<N-1\): stay \(1/2\), each neighbor \(1/4\).
- At \(j=0\): stay \(1/2\), move to \(1\) with \(1/4\), and \(1/4\) enters the agent (return) on the closed and closedness kernels. On the sink kernel that quarter enters the sink instead.
- At \(j=N-1\): move to \(N-2\) with \(1/4\), stay with \(1/2+c/4\), and \((1-c)/4\) enters the sink.

\(q\) after \(T\) steps is the accumulated agent mass, divided by the number of starts (each start is mass 1). The sink mass is not added.

Reference geometry for M1-scale, M2, and M3: \(c=1\).

## 5. Continuum shape, no free parameter

Not fitted. Diffusivity \(D=1/4\), from a per-step position variance \(1/2\) and the Fokker–Planck coefficient \(\sigma^2/2\). Barriers: absorbing at coordinate \(-1\), reflecting at coordinate \(N\). Length \(L=N+1\). Start coordinate of site \(j_0\) measured from the absorbing barrier: \(y=j_0+1\). Forty terms, \(n=0,\ldots,39\),

\[
S=\sum_{n=0}^{39}\frac{2}{(n+\tfrac12)\pi}\sin\!\left(\frac{(n+\tfrac12)\pi y}{L}\right)\exp\!\left(-D\frac{(n+\tfrac12)^2\pi^2 T}{L^2}\right).
\]

\(q_{\mathrm{pred}}=1-S\), clipped only for printing into \([-0.01,1.01]\). A clip that moves the raw value by more than \(10^{-6}\) is a deviation. The comparison uses the raw value.

## 6. Agent, and the fixed-point map

Reuse `closed_form_ant` in `theory/record_ratio_reframes_checks/record_ratio_reframes_checks.py`. \(\gamma=0\), \(r=0.6\), \(\kappa=1\). Angle grid \(\theta_j=j\cdot(\pi/2)/180\) for \(j=0,\ldots,180\).

\[
J(\theta;q)=I(\theta)+q\,P_D(\theta)+w\,L(\theta).
\]

A tie is any grid angle whose \(J\) is within \(10^{-9}\) of the minimum. Packet width

\[
W(\theta)=1+\left\lfloor 8\cdot\frac{P_D(\theta)}{P_D(\pi/2)}+10^{-15}\right\rfloor.
\]

\(W\) is an integer in \(\{1,\ldots,9\}\) on this menu because \(P_D\) runs from 0 at the pointer to \(P_D(\pi/2)\) at the equator. If a computed \(W\) falls outside that set, clamp it and log a deviation.

\(\Phi(q)\) is the set of returns \(q(T)\) at the distinct widths of the tied angles, one copy of each width. The iteration uses the arithmetic mean of that set. Starts \(q\in\{0,1/4,1/2,3/4,1\}\). At most 40 updates. Stop when the absolute step is at most \(10^{-4}\).

- `POINT` if every start stops, the terminals differ by at most \(0.02\), and at the mean terminal the width of \(\Phi\) is at most \(0.02\).
- `SET` if every start stops and `POINT` fails.
- `CYCLE` if any start has not stopped.

A boundary corner of \(x\) is nominal \(x\le 0.05\) or nominal \(x\ge 8\).

Locked cells, \(N=32\), \(c=1\):

| cell | \(x\) | \(\phi\) | \(w\) | corner | required |
|---|---|---|---|---|---|
| m3-a | 0.5 | 0 | 2 | no | POINT |
| m3-b | 1 | 0 | 2 | no | POINT |
| m3-c | 2 | 0 | 2 | no | POINT |
| m3-d | 1 | 0 | 1 | no | POINT |
| m3-e | 0.05 | 0 | 2 | yes | POINT or SET |
| m3-f | 8 | 0 | 2 | yes | POINT or SET |

`CYCLE` fails the cell it sits on, corner or not.

## 7. Locked predictions

Reservoirs \(N\in\{12,16,24,32,48\}\). Nominal \(x\in\{0.05,0.1,0.25,0.5,1,2,4,8\}\). Reference width \(W=1\), start \(j_0\), \(c=1\), unless a line says otherwise.

**M1-closed.** Eventual hit probability on the closed kernel, computed as the agent mass at step \(T_{\infty}=\lfloor 200\,\tau_{\mathrm{mix}}(N)+1/2\rfloor\) for \(N=12\) and for \(N=48\), \(W=1\). Bar: both are at least \(1-10^{-9}\). A match is holds by construction.

**M1-sink.** Same horizons, sink kernel. Bar: both agent masses are at most \(10^{-9}\). A match is holds by construction.

**M1-scale.** Closed kernel, \(W=1\), horizon \(T=32\) fixed, every locked \(N\). The five returns are strictly decreasing by at least \(10^{-4}\) at each step, the \(N=12\) return is at least \(0.01\), and the \(N=48\) return is at most \(0.20\). *Fails if* any of those three misses. This is the \(N\to\infty\) reading at a horizon that does not grow. It is evidence.

**M2-collapse.** At each nominal \(x\), the range of \(q\) across paired \(N\). Metric \(\rho\) is the maximum of those ranges. A nominal \(x\) with fewer than 4 paired reservoirs is dropped and printed. *Fails if* fewer than 6 nominal values remain, or \(\rho>0.08\). Falsifier, same object: two paired \((T,N)\) at one nominal \(x\) with \(|q_1-q_2|>0.08\).

**M2-shape.** On paired cells with nominal \(x\in\{0.25,0.5,1,2\}\) and every locked \(N\), \(W=1\), the maximum of \(|q-q_{\mathrm{pred}}|\). *Fails if* fewer than 12 such cells are paired, or the maximum exceeds \(0.08\). This is the curve between 0 and 1. The endpoints are not this check.

**M2-interior.** At \(N=32\), \(W=1\), \(c=1\), both \(q(x=0.5)\) and \(q(x=1)\) lie in \((0.05,0.95)\). *Fails if* either falls outside. A collapse that only compares endpoints does not pass this line.

**M3-conv.** Cells m3-a through m3-d are `POINT`. *Fails if* any is `SET` or `CYCLE`.

**M3-corner.** Cells m3-e and m3-f are `POINT` or `SET`. *Fails if* either is `CYCLE`.

**M4, secondary, Chad's idea.** Closedness values \(c=k/10\) for \(k=0,\ldots,10\), at \(N=32\). Reference horizon \(T_{\mathrm{ref}}=\lfloor \tau_{\mathrm{mix}}(32)+1/2\rfloor\), at least 1. The curve \(f\) is the mean, over paired reservoirs, of the M2 returns at each nominal \(x\) that M2-collapse did not drop. Linear interpolation in \(x\). Outside \([0.05,8]\), clamp to the nearer endpoint and count a clamp. \(x(c)=T_{\mathrm{ref}}/\tau(c)\), with \(\tau(c)\) from the decoupled clock.

Predicted returns: \(f(x(c))\), eleven numbers. Measured returns: the fixed-point iteration of §6 at \(\phi=0\), \(w=2\), horizon \(T_{\mathrm{ref}}\), using the closedness-\(c\) kernel. The measured summary is the mean terminal if every start stops, otherwise the mean of the last iterates. Bins on \([0,1]\): edges \(0,0.2,0.4,0.6,0.8,1\). Left-closed, right-open, except the last bin, which is closed. A point on an interior edge goes to the higher bin.

Total variation is half the \(\ell_1\) distance of the two bin-mass vectors, each normalized to sum to 1. *Fails if* the distance exceeds \(0.20\).

The predicted masses are printed, including the tag `PREDICT`, before any measured \(q^\star\) is computed. The script builds \(f\) and the prediction from M2 returns and from \(\tau(c)\) only.

**E-pair, exploratory, not scored.** Locked here, before the run, not added after a result. Two closed worlds, \(c=1\), \(N=32\), \(W=1\), the same \(T_{\mathrm{ref}}\), hence the same \(x\). World A starts at \(j_0\). World B starts at \(N-1\). Both use the closed kernel. Print both returns and the absolute difference. They are not in the fail count. This is the explicit same-\(x\) comparison of two equally closed worlds. M2-collapse remains the scored version of that comparison inside one family.

**Report, not scored.** For each of m3-a through m3-d, the mean terminal, its absolute distance to \(0.30\), and its absolute distance to \(0.6\). The \(0.30\) figure is the T79 singleton's ratio. The \(0.6\) figure is the parent's root at equal kappas. Neither is a target. Neither is a bin center. Neither enters \(f\).

## 8. Instrument checks

- `G-rev`. On the full path with \(A=4\), \(N=12\), the lazy matrix is symmetric to \(10^{-15}\) and every row sums to 1 within \(10^{-12}\).
- `G-cons`. Twenty steps of that chain from the reference start keep total mass within \(10^{-12}\) of 1.
- `G-start`. Total variation of that start from the uniform measure is at least \(0.5\). The start entropy is 0. The uniform entropy \(\ln(A+N)\) exceeds 1.
- `G-decouple`. As in §3. Also the decoupled matrix is \(N\times N\) and stochastic at \(c=1\), while the closed return restriction has row sum at most \(0.75\) at environment index 0.
- `G-gap`. As in §3.
- `G-equiv`. \(N=12\), \(A=4\), \(T=5\), \(c=1\), start \(j_0\). First-entrance probability on the full path, tracked with a hit flag, equals the return kernel within \(10^{-12}\).
- `G-form`. `closed_form_ant` and `functionals` at \(\phi=0\), \(\gamma=0\), angles \(0,\pi/6,\pi/4,\pi/3,\pi/2\). Maximum absolute difference of \(I\), \(P_D\), and \(L\) at most \(10^{-9}\).

## 9. What this run will not do

It will not edit `THEORY.md`, `CORE.md`, or this file. It will not add a return edge after seeing \(q\). It will not set a reverse rate equal to a forward rate. It will not start from the uniform measure. It will not fit \(D\), the tolerances, the bins, or the interpolation to the measured returns. It will not treat a construction match as evidence. It will not say that a value of the ratio has been obtained as a final answer. It will not treat a pass as a derivation of general relativity, quantum mechanics, holography, or gravity. It will not put \(0.30\) or \(0.6\) into the cost, the curve, or the histogram.

## 10. Output

One line per named check, `PASS` or `FAIL`. Construction matches that meet the bar are `PASS holds-by-construction`. Then `FAILS` and a count of lines whose result is `FAIL`. `E-pair` and `REPORT` lines are not checks. `CLASS` lines repeat the locked evidence tag and are not checks. `DIAG` lines carry the numbers. `PREDICT` lines are printed before the measured M4 returns. Stdout is stored and byte-compared by the test. This file is not read for numbers that the script could edit into a pass. `RUN_LOG.md` records every deviation and, if there is none, says so. `DEVIATIONS.md` is the same list, append-only. The memo uses the labels PROVED (in-model), NUMERICAL, and PUZZLE, and it has a section headed `Circularity and what could fail`.
