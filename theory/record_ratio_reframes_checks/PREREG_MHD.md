# T76 preregistration: MHD analogy, two hypotheses

*Tuesday 24 November 2026 (UTC). Written and committed before any MHD script and before any MHD grid. Branch `forge-record-ratio-reframes`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. Earlier locks `PREREG.md` and `PREREG_FIXED_POINTS.md` are not edited. Locked by sha256 in `PREREG_MHD.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This lock file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. A miss is a puzzle. The record price is a cost. Both readings below are **analogy, hypothesis**. They are not sentences of A1–A8. The MHD formulas are the standard channel facts named in the question. No page of either textbook was re-read for this lock. No post from X is a source.

## 0. Question

Does the record ratio \(q=\kappa_D/\kappa\) behave like an MHD load factor, and is there one dimensionless model quantity, with a crossover near 1, that selects the ratio-\(0\) design or the ratio-\(1\) design?

## 1. Analogy, hypothesis, not an axiom

**H1, load factor.** In a Faraday channel the load factor is \(K=E/(uB)\). \(K=0\) is a short circuit, \(K=1\) is an open circuit, \(0<K<1\) is a generator, and \(K>1\) is an accelerator. The ideal current density is \(\sigma u B(1-K)\) and the electrical power density is \(\sigma u^2 B^2 K(1-K)\), maximal at \(K=1/2\). Local efficiency of that ideal channel equals \(K\). The book that carries this channel theory is Sutton and Sherman, *Engineering Magnetohydrodynamics* (McGraw-Hill, 1965). A journal notice of that book is doi `10.1115/1.3625105`. The notice is not the derivation. No page is claimed.

The hypothesis inside the model: when \(J\) is minimized jointly over the design \(\theta\) and over an admissible ratio, the selected ratio is interior, and the value of the record has a product shape in the ratio, as \(K(1-K)\) does.

**H2, regime number.** The magnetic Reynolds number is \(\mathrm{Rm}=\mu_0\sigma u L\), the ratio of advection to diffusion in the induction equation. Large \(\mathrm{Rm}\) is the frozen-in regime. Small \(\mathrm{Rm}\) is the diffusive regime. The two terms are comparable when \(\mathrm{Rm}\) is of order 1. The book is P. A. Davidson, *Introduction to Magnetohydrodynamics*, 2nd ed. (Cambridge, 2017), doi `10.1017/9781316672853`. No page is claimed.

The hypothesis inside the model: one dimensionless quantity, \(w/\kappa\) or the reuse fraction \(\lambda\), selects the equator or the pointer, with a crossover near 1.

A coherence lifetime is not a coordinate of this static menu. \(\gamma\) is a dephasing factor already used. It is not reintroduced here as a lifetime. That sentence is not a scored check.

A regime number defined as \(w/(|\kappa_D-\kappa|\,w_\star)\) sits at 1 only by inserting \(w_\star\). It is not scored.

## 2. Prior exposure

The phase boundary on ANT, \(\gamma=0\), \(\phi=0\), is already scored (`PREREG_FIXED_POINTS.md` §3, `fixed_point_checks.out:2`). \(w_\star=3.209014724815\) at \(r=0.6\). \(P_\chi(0)=0.096372378511\). \(J\) is linear in \(q\) at fixed \(\theta\) by the definition \(J=\kappa I+q\kappa P_D+w L\), for \(\kappa>0\). That linearity is a check, not a new forecast. A hand evaluation, not a grid, at \(w=1\), \(q=0.5\), using the equator values \(I=0\) and \(P_D=P_\chi(0)\), puts \(J(0.5)-J(0)\) near \(0.048\). The locked bar is \(0.01\).

## 3. Model

Same objects as `PREREG.md` §3. ANT, \(\gamma=0\), \(\phi=0\), \(\kappa=1\), \(r=0.6\). Grid \(721\) points. Tie \(10^{-9}\). `SEED = 20261124` is set and not drawn from. \(J^\star(q,w)=\min_\theta J\). Ratio \(q\) means \(\kappa_D=q\).

## 4. H1 — predictions

**H1-lin.** At \(\theta\in\{0,\pi/4,\pi/2\}\) and at \(q\in\{0.25,0.5,0.75,1\}\), with step \(0.25\) in \(q\), the second difference \(J(q+\tfrac14)-2J(q)+J(q-\tfrac14)\) has absolute value \(<10^{-9}\). The stake in this line is \(w=1\).

*Fails if* any absolute second difference is \(\ge 10^{-9}\). Then \(J\) is not linear in the ratio at fixed design, and a product curvature is possible. Report the cell. Do not fit \(K(1-K)\).

**H1-joint.** Stakes \(w\in\{0.5,1,2,4,10\}\). Ratios \(q\in\{0,0.25,0.5,0.75,1,2\}\). For every pair, \(J^\star(q,w)\ge J^\star(0,w)-10^{-9}\).

*Fails if* any pair undershoots \(J^\star(0)\) by \(\ge 10^{-9}\). Then a ratio above \(0\) lowers the minimized cost. Report the pair. Do not declare an interior load factor.

**H1-half.** At \(w=1\), \(J^\star(0.5)-J^\star(0)>0.01\). At \(w=10\), both minimizers are the unique grid point \(\theta=0\) and \(|J^\star(0.5)-J^\star(0)|<10^{-9}\).

*Fails if* the \(w=1\) gap is \(\le 0.01\), or \(w=10\) is not uniquely the pointer at either ratio, or the \(w=10\) costs differ by \(\ge 10^{-9}\). A small gap at \(w=1\) means the half-ratio is not costlier than the endpoint on this stake. Report the gap.

## 5. H2 — predictions

**H2-split.** At \(w=1\), \(q=0\) has unique minimizer \(\theta=\pi/2\), and \(q=1\) has unique minimizer \(\theta=0\). The two angles differ by \(\ge 1\) rad.

*Fails if* either cell is not unique, or the gap is \(<1\). Then \(w/\kappa=1\) may select one design for both ratios.

**H2-below.** At \(w=2\), \(q=0\), the unique minimizer is \(\theta=\pi/2\).

*Fails if* the minimizer is not uniquely the equator. Then the crossover of \(w/\kappa\) at ratio \(0\) sits at or below \(2\).

**H2-move.** Nominal ratio \(1\), charged coefficient \(\lambda\), which is \(q=\lambda\). At \(\lambda=0.7\), \(w=1\), the unique minimizer is \(\theta=0\). At \(\lambda=0.7\), \(w=0.5\), the unique minimizer is \(\theta=\pi/2\).

*Fails if* either cell misses its end, or either cell ties. Then the same reuse fraction selects the same regime at both stakes, and \(\lambda\) may be acting as a single regime number at \(0.7\).

## 6. What this run will not say

It will not edit `THEORY.md`, the earlier locks, or the T75 review. It will not say that either analogy has been solved, and it will not say that a miss removes the analogy from further work. A fit that is only partial stays a puzzle. The MHD formulas are not prices in \(J\).

## 7. Output

The script prints one line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test.
