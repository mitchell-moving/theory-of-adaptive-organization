# T82 addition: the coupled flow-ratio loop

*24 November 2026 (UTC). A separate lock. `PREREG.md` in this directory is not edited. Written and committed, with `PREREG_COUPLED.sha256`, before `coupled_loop_checks.py` and before any scored orbit. Chad's hypothesis, continued: behavior changes the returning flow, and the flow changes behavior.*

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every statement about what the loop does is a model implication, in-model.

## Why this approach

T81 (fork branch `forge-record-ratio-measured`, commit `f625bb74c2702a6a9b1f7d5b8afff922f90cf8b3`, fork PR #15) measures the return share and then composes it with the cost in one step: the width jumps to the minimizer, and the next \(q\) is the return at that width. Its locked prediction for that map is one number. The interior cells came back `POINT`.

The same commit leaves an unscored E-pair. At \(N=32\), \(c=1\), horizon \(T=415\), width 1, the midpoint start returns \(0.239059227845\) and the far-end start returns \(0.048343059332\). Same clock, two histories. A classification that uses one start rule would throw that difference away.

This lock therefore runs a two-variable lag map. The destruction rate chases the width the current return asks for. The return chases the flow the current destruction rate produces. Neither jump is the whole step. Both of T81's start rules are in the grid.

## Can it fail

Can it fail: yes. A gain can overshoot and the orbit can cycle or wind, and the two start rules can lock to one shared number once the width is free to move.

Cheapest way: cell m3-b, gain \((\alpha,\beta)=(1.5,0.5)\), one initial condition, one start rule, with the tail range of \(q\) above \(10^{-3}\).

## 0. What is reused, and what is labeled as an extension

Reused from T81's `measured_checks.py` and from `closed_form_ant` in `record_ratio_reframes_checks.py` at that same commit. \(R=0.6\). Binary entropy in nats. \(\gamma=0\), \(\phi=0\).

\[
J(\theta;q)=I(\theta)+q\,P_D(\theta)+w\,L(\theta),
\]

with \((I,P_D,L)\) from `closed_form_ant`. Angle grid \(\theta_j=j\cdot(\pi/2)/180\), \(j=0,\ldots,180\). A tie is any grid angle whose \(J\) is within \(10^{-9}\) of the minimum. Packet widths of the tied angles,

\[
W=1+\left\lfloor 8\cdot\frac{P_D(\theta)}{P_D(\pi/2)}+10^{-15}\right\rfloor,
\]

clamped into \(\{1,\ldots,9\}\) only if a value falls outside, and a clamp is a deviation.

The walk is T81's lazy path. \(N=32\), \(c=1\), contact into the agent. Integer width \(W\) under the midpoint rule uses T81's centered block. The return is the accumulated agent mass after \(T\) steps, averaged over the sites in the block.

Horizons are the integers T81 printed, not a fresh eigenvalue: m3-a \(T=208\), \(w=2\); m3-b \(T=415\), \(w=2\); m3-c \(T=831\), \(w=2\); m3-d \(T=415\), \(w=1\); m3-e \(T=21\), \(w=2\); m3-f \(T=3323\), \(w=2\).

**EXT-far, labeled.** The far start rule uses a block of the same length as the midpoint block for that width, shifted so it ends at site \(31\). At width 1 this is the site \(31\) of the E-pair. T81 did not put this block inside \(\Phi\).

**EXT-rate, labeled.** The destruction rate \(\rho\) is a real number in the role of the packet width. T81's \(W\) is an integer. For integer \(k\), \(Q_s(k)\) is the walk return under start rule \(s\). For \(\rho\in[1,9]\),

\[
Q_s(\rho)=(1-f)\,Q_s(k)+f\,Q_s(k+1),\qquad k=\lfloor\rho\rfloor,\ f=\rho-k,
\]

and \(Q_s(9)\) when \(\rho=9\). This interpolation is not in T81.

**EXT-target, labeled.** \(R^\star(q)\) is the arithmetic mean of the tied widths at that \(q\). T81 averaged the returns of the tied widths. The lag map needs one rate, so the target is the mean width.

## 1. The coupled map

State \((\rho,q)\). Start rules \(s\in\{\mathrm{mid},\mathrm{far}\}\). Gains \((\alpha,\beta)\) from the locked list. One step, using only the previous state:

\[
\rho\leftarrow \rho+\alpha\bigl(R^\star(q)-\rho\bigr),\qquad
q\leftarrow q+\beta\bigl(Q_s(\rho)-q\bigr).
\]

No clamp after the step. Four hundred steps. The tail is steps 200 through 399.

Gains: \((1,1)\), \((0.5,0.5)\), \((1.5,0.5)\), \((0.5,1.5)\).

Initial conditions of the map, distinct from the walk's start: \((1,0)\), \((5,0.5)\), \((9,1)\).

Cells: the six horizons and stakes above, \(\phi=0\).

## 2. Classifier, locked

Applied to the tail. Euclidean distance in \((\rho,q)\).

1. **FIXED** if the range of \(\rho\) and the range of \(q\) are both at most \(10^{-3}\). This is one number: phase locking, in the sense that both variables have stopped. It is the reading T81's `POINT` gave its one-dimensional map.
2. Else **DIVERGE**, reported as **OTHER**, if any tail point has \(|q|>2\) or \(\rho<0\) or \(\rho>12\).
3. Else **CYCLE** if the smallest \(p\in\{2,\ldots,32\}\) satisfies \(\|x_{i+p}-x_i\|\le 10^{-3}\) for every tail index \(i\) with \(i+p\) still in the tail. A repeating section is a limit cycle: one frequency.
4. Else the rotation number about the tail's centroid. Radius \(r_i\). Mean radius \(\bar r\). Thickness \(\max r-\min r\). Angle \(\mathrm{atan2}(q-\bar q,\ \rho-\bar\rho)\), unwrapped so consecutive jumps lie in \((-\pi,\pi]\). \(\omega\) is the mean step divided by \(2\pi\), reduced to \([0,1)\). Distance to the rationals is the minimum, over denominators \(b=1,\ldots,32\) and numerators \(a=0,\ldots,b\), of the distance on the circle \(\mathbb{R}/\mathbb{Z}\).
   - **TORUS** if \(\bar r>10^{-3}\), the thickness is at most \(0.05\,\bar r\), and the distance to those rationals is greater than \(10^{-3}\). Quasi-periodic motion on a curve. For this two-dimensional map that curve is the section of a torus: two frequencies, the winding and the discrete step.
   - **CYCLE** if \(\bar r>10^{-3}\), the thickness is at most \(0.05\,\bar r\), and the distance is at most \(10^{-3}\). Rational winding, still one frequency.
   - **OTHER** otherwise.

A finite-time Lyapunov number is printed and does not change the class. At the first tail point, a second orbit starts at \(q+10^{-6}\) and both run 40 steps. \(\lambda=(1/40)\log(d_{40}/10^{-6})\), or \(-10^{9}\) if \(d_{40}=0\). \(W\) jumps, so this slope is not the classifier.

Kuramoto vocabulary, locked before the counts. FIXED is the locked state, one relative condition, as Adler's phase difference sits at a fixed point. CYCLE is a limit cycle, one frequency. TORUS is the unlocked winding, two incommensurate frequencies. This grid does not estimate \(K_c=2/(\pi g(0))\). A class is not a coupling constant.

## 3. Predictions

**I-port.** The port of the walk at \(T=415\), width 1, matches T81's E-pair to an absolute error of \(10^{-9}\): midpoint \(0.239059227845\), far end \(0.048343059332\). Fails if either gap is larger. A match says the port is the same walk. It is not evidence about the loop.

**H-settle.** Every orbit on the grid is FIXED. This is T81's "one number," asked of the lag map, under both start rules, every gain, and every initial condition. Fails if any orbit is CYCLE, TORUS, or OTHER. A cycle or a winding is the finding, stated in the terms of §2. The map, the grid, and the classifier are not changed to remove it. T81's files are not edited.

**H-history.** On m3-b, for every gain and every initial condition, both start rules are FIXED and their tail-mean \(q\) values differ by more than \(0.05\). Fails if any of those twelve pairs misses either condition. The E-pair gap is why \(0.05\) is the bar: the one-shot gap is \(0.190716168513\), and \(0.05\) is below that gap and above the FIXED tolerance.

**H-init.** Inside one cell, one start rule, and one gain, the three initial conditions share a class. If that class is FIXED, their tail-mean \(q\) values differ by at most \(0.02\). Fails if a class splits, or if a FIXED triple spreads by more than \(0.02\).

## 4. What this file does not do

It does not score the orbits. It does not edit `PREREG.md`, `THEORY.md`, `CORE.md`, or any T81 file. It does not add a return edge, a clamp, or a gain after the classes are known. Deviations, if any, are appended to `DEVIATIONS_COUPLED.md`. This file is not edited after the locking commit.
