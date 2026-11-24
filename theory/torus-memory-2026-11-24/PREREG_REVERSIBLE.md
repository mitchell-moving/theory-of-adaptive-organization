# T82b preregistration: a closed reversible torus

*24 November 2026 (UTC). A new lock. `PREREG.md` and `PREREG_COUPLED.md` are not edited. Written and committed, with `PREREG_REVERSIBLE.sha256` and the same hash in `RUN_LOG.md`, before `reversible_torus_checks.py` and before any scored orbit.*

## Why this approach

The coupled-loop score used a contracting map on a width menu. Its destruction rate sat at 1 or 9, and a tail-diameter test cannot see an invariant torus (`DEVIATIONS.md`, the reframe of 24 November 2026; `ARCHAEOLOGY.md`). In a closed reversible world the flow does not fall onto an attractor. Each initial condition stays on its own torus. The label of that torus is the memory. The E-pair gap is a candidate for that label, not a nuisance to be damped out.

The repo already knows that a rational ratio closes and an irrational ratio fills (`theory/TORUS.md:16`, commit `d57669d9`), and LOCK1 already failed the claim that the cost picks the golden mean (`tests/LOCK1/RESULTS.md:9-18`). This lock does not rerun those. It asks whether a measured return share, on a symplectic flow, can tell a resonant torus from a quasi-periodic one.

## Can it fail

Can it fail: yes. Equidistribution can make the return share blind to the value of the action. Damping the action can leave the angle memory of a rational orbit intact. A long irrational orbit can pass near its start. The damped flow can reproduce the circle-map tongue, or it can fail to lock at all.

Cheapest way to fail it: one orbit at frequency ratio \(3/2\) and one at \(\sqrt{2}\), both at zero action, zero coupling, and zero damping. The rational orbit is not periodic, or the irrational orbit is not quasi-periodic, under the rotation-number rule in §4.

## What can genuinely fail

I-rev and I-vol fail if the step is not reversible or not symplectic. P1 fails if distinct starts land on one terminal. P2 fails if the angle-averaged return does not move with the action, which equidistribution makes likely, or if it moves and is not smooth. P3 fails if the rational angle-gap does not halve on the timescale \(1/\gamma\). P4 fails if the golden-ratio shift is larger than the rational shift, if a plateau appears with no damping, or if damping creates no plateau. P-kc fails if there is no width to compare, or if the width matches \(\varepsilon/\pi\) within 5 percent. A pass of I-rev is a property of the integrator. It is not, by itself, evidence about memory.

## 1. The world

Coordinates \((\theta_1,I_1,\theta_2,I_2)\). Angles are real numbers; comparisons of angles use the principal value in \((-\pi,\pi]\).

\[
H=\omega_{10} I_1+\omega_{20} I_2+\frac{\beta}{2}(I_1^2+I_2^2)+\varepsilon\cos(\theta_1-\theta_2).
\]

\(\beta=0.25\). \(\omega_{10}=1\). Three families of \(\omega_{20}\): rational \(3/2\), irrational \(\sqrt{2}\), golden conjugate \((\sqrt{5}-1)/2\). Unperturbed frequencies \(\Omega_j=\omega_{j0}+\beta I_j\).

The destruction rate is \(\rho=\exp(I_1)\). It is continuous. There is no menu and no clamp.

Actions \(I_2=0\), \(I_1\in\{-0.4,-0.2,0,0.2,0.4\}\). Angles \(\theta_1=0\), \(\theta_2=2\pi k/8\) for \(k=0,\ldots,7\). Coupling \(\varepsilon\in\{0,0.05\}\). Damping \(\gamma\in\{0,0.02,0.05\}\).

## 2. Integrator

Separable Stormer–Verlet, step \(h=0.05\), \(n=2000\) steps. \(A\) is the quadratic part of \(H\) and \(V=\varepsilon\cos(\theta_1-\theta_2)\).

\[
\begin{aligned}
I&\leftarrow I-\frac{h}{2}\partial_\theta V,\\
\theta&\leftarrow \theta+h\,(\omega_0+\beta I),\\
I&\leftarrow I-\frac{h}{2}\partial_\theta V.
\end{aligned}
\]

\(\partial_{\theta_1}V=-\varepsilon\sin(\theta_1-\theta_2)\) and \(\partial_{\theta_2}V=+\varepsilon\sin(\theta_1-\theta_2)\). When \(\gamma>0\), after each full step, \(I\leftarrow I\,e^{-\gamma h}\). That factor is not symplectic. It is the dephasing. No file in this tree defines a T84 rate, so \(\gamma\) is not imported from a T84 result (`ARCHAEOLOGY.md`).

## 3. The return share

\(q\) is a measurement, not a term in \(H\). It uses T81's lazy path at commit `f625bb7`: \(N=32\), \(c=1\), contact into the agent, one excitation, the accumulated agent mass after \(T_{\mathrm{steps}}\) steps. Site \(s(\theta_2)=\lfloor N\,(\theta_2 \bmod 2\pi)/(2\pi)\rfloor\), and site 32 is site 0.

\[
T_{\mathrm{steps}}=\max\bigl(1,\mathrm{round}(80/\Omega_2)\bigr)
\]

at the initial \(\Omega_2\). Samples are the Poincaré crossings where the unwrapped \(\theta_1\) passes a multiple of \(2\pi\), with \(\theta_2\) and \(I_1\) interpolated linearly across the step. Then

\[
q=\frac{\sum_k \rho_k\,p\bigl(s(\theta_{2,k}),T_{\mathrm{steps}}\bigr)}{\sum_k \rho_k},\qquad \rho_k=\exp(I_{1,k}).
\]

No crossing makes \(q\) undefined and the orbit `OTHER`. This horizon is not T81's integer width. T81's width menu is not used.

## 4. Classifier

Frequency analysis only. The rotation number is

\[
\nu=\frac{\theta_2(T)-\theta_2(0)}{\theta_1(T)-\theta_1(0)}
\]

on the unwrapped angles. Distance to rationals: minimum of \(|\nu-a/b|\) for \(b=1,\ldots,B\) and \(a=0,\ldots,2b\).

- `PERIODIC` if that distance at \(B=8\) is at most \(10^{-4}\).
- `QUASIPERIODIC` if the distance at \(B=16\) is greater than \(10^{-3}\).
- `OTHER` otherwise.

The minimum return distance of \((\theta_1,\theta_2)\) over the second half of the steps is printed. It does not assign the class. The coupled-loop labels FIXED, CYCLE, and TORUS are not used.

## 5. Predictions

**I-rev.** \(\gamma=0\), \(\varepsilon\in\{0,0.05\}\), \(I=0\), \(\theta=0\), each family. Run \(n\) steps, then \(n\) steps of \(-h\). Every \(|\Delta I|\) and every principal \(|\Delta\theta|\) is at most \(10^{-4}\). Fails if any coordinate is larger.

**I-vol.** \(\varepsilon=0.05\), \(\gamma=0\), \(I=0\), \(\theta=0\), family \(\sqrt{2}\). Central-difference Jacobian, step \(10^{-6}\). \(|\det-1|\le 10^{-6}\) after one Verlet step and \(\le 10^{-3}\) after 50 steps. The damping factor is off. Fails if either bound misses.

**P1.** \(\gamma=0\), \(\varepsilon=0\), family \(\sqrt{2}\). The 40 states (5 actions, 8 angles) have pairwise distance at least \(10^{-4}\) at the end, with distance \(\sqrt{\mathrm{wrap}(\Delta\theta_1)^2+\mathrm{wrap}(\Delta\theta_2)^2+\Delta I_1^2+\Delta I_2^2}\). The five terminal \(I_1\) at \(\theta=0\), in order of the grid, stay within \(10^{-3}\) of the five starts. Fails if a pair collides or an action moves.

**P2.** \(\gamma=0\), \(\varepsilon=0\), families \(\sqrt{2}\) and golden. At each \(I_1\), the range of \(q\) across the 8 angles is at most \(0.02\). The range of the angle-averaged \(q\) across the five actions is at least \(0.02\). The maximum absolute second difference of that average is at most half the maximum absolute first difference. Fails if any clause misses. A flat average is a miss, not a pass.

**P3.** Family \(3/2\), \(\varepsilon=0\), \(I_1=0\). \(G(\gamma)\) is the range of \(q\) across the 8 angles. \(G(0)>0.05\). For \(\gamma\in\{0.02,0.05\}\), stop at times \(t=20,40,60,80,100\) and let \(t_{1/2}\) be the first of these with \(G\le G(0)/2\). \(|\gamma t_{1/2}/\ln 2-1|\le 0.5\). Fails if \(G(0)\) is too small, if the gap never halves, or if the half-time misses the window. No T84 formula is used.

**P4.** \(\varepsilon=0\), \(\gamma=0\), \(I=0\).
- \(\nu\) is within \(10^{-6}\) of \(\omega_{20}/\omega_{10}\) on every angle of every family.
- All 8 rational angles are `PERIODIC`. All 8 angles of \(\sqrt{2}\) and of the golden conjugate are `QUASIPERIODIC`.
- The rational range of \(q\) exceeds \(0.05\). The \(\sqrt{2}\) range is below \(0.02\). The golden range is at most the \(\sqrt{2}\) range.
- At \(\varepsilon=0.05\), \(\gamma=0\), \(I=0\), \(\theta=0\), the absolute shift of \(\nu\) from its \(\varepsilon=0\) value is no larger for the golden conjugate than for \(3/2\).

Fails if any clause misses. This is not LOCK1: nothing here minimizes a cost over ratios.

**P4-tongue.** Detuning \(\delta\in\{-0.15,-0.10,-0.05,0,0.05,0.10,0.15\}\) added to \(\omega_{20}=3/2\), \(I=0\), \(\theta=0\). A plateau is three consecutive \(\delta\) with \(|\nu-3/2|\le 10^{-3}\). No plateau at \(\gamma=0\), for \(\varepsilon=0\) and for \(\varepsilon=0.05\). A plateau at \(\varepsilon=0.05\), \(\gamma=0.05\). Fails if a conservative run plateaus, or if the damped run does not.

**P-kc.** If the damped plateau exists, its half-width is half the span of \(\delta\) in the longest run. Compare with \(\varepsilon/\pi\). `DIFFER` if the relative gap exceeds \(0.05\), `MATCH` otherwise. The prediction is `DIFFER`. Fails if there is no plateau, or if the gap is at most \(0.05\).

**Beyond Kuramoto.** \(K_c=2/(\pi g(0))\) and the 0:1 width \(K/\pi\) are the known circle-map facts (`theory/TORUS.md:17`). This run is beyond them only if all three hold: the half-width differs from both \(\varepsilon\) and \(\varepsilon/\pi\) by more than 5 percent; the half-width at \(\gamma=0.02\) and at \(\gamma=0.05\), same \(\varepsilon\), differs by more than 5 percent; and the ratio of half-width to \(\gamma\) is not constant within 5 percent. Otherwise `NOT BEYOND`. The prediction is `NOT BEYOND`. Fails if the three conditions all hold.

## 6. What a pass would mean

In-model only. If P4 holds and P2's action range fails, the return share reads the rational-versus-irrational class, and the angle of a rational orbit, and it does not read the value of \(I\). The phase-space memory is still the torus, because P1 keeps the actions apart. The share \(q\) is a coarser record. The names "revival" and "filling" are the same split. They are not a Talbot carpet. This tree has no T83 result (`ARCHAEOLOGY.md`).

## 7. Prior art

Crossref on 24 November 2026, the same queries as `PREREG.md` §3. Kuramoto, DOI `10.1007/BFb0013365` (issued field empty; symposium volume `10.1007/BFb0013294`, 1975) and `10.1007/978-3-642-69689-3` (1984). Strogatz 2000, `10.1016/S0167-2789(00)00094-4`. Acebrón, Bonilla, Pérez Vicente, Ritort, and Spigler 2005, `10.1103/RevModPhys.77.137`. Circle-map reprint, `10.1007/978-3-642-01742-1_10`, author list empty. No 1961 DOI is cited. Greene 1979 and Shenker 1982 are named by `tests/LOCK1/RESULTS.md:24` and are not given a DOI here.

## 8. What this file does not do

It does not score. It does not edit `PREREG.md`, `PREREG_COUPLED.md`, either scoreboard, `THEORY.md`, or `CORE.md`. Deviations after this commit go to `DEVIATIONS.md`, appended. This file is not edited after the locking commit.
