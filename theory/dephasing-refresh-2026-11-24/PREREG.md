# PREREG: refresh of a dephasing phase tracker

*Tuesday 24 November 2026 (UTC). Written and committed before any results script and before any stored output. Branch `forge-dephasing-refresh`, cut from `forge-dephasing-crossover` at `29ffc8b`. `THEORY.md` and `CORE.md` are not edited. This file is locked by the commit that adds it. A later change to a prediction, a bar, or a grid is a deviation and is appended in `DEVIATIONS.md`. Open-work id **T84b**. Self-check, not an independent review.*

Can it fail: the finite-hold threshold can tend to 16, the short-period elasticity can leave 1/2 inside \(\gamma\tau^*\le 0.5\), the Gaussian probe can keep exponent 1/2, and \(\Pi_c(\Theta)\) can equal the T84 threshold \(h(\varepsilon)/\varepsilon\).

Cheapest way to fail it: one qubit, time-averaged Hamming loss, heat linear in the number of refreshes, closed forms. No bath Hilbert space and no Monte Carlo.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. The qubit and the dephasing channel are inputs. A miss is a puzzle. The record price is a cost.

## 0. Question

Minimize the rate

\[
J=\dot Q+w\,\mathbb E[\mathrm{loss}]
\]

for a phase bit held over a window \(T_{\mathrm{hold}}\), under pure dephasing at rate \(\gamma\), stake \(w\), and heat \(A=\lambda kT\,I_0\) per refresh. The candidates, stated as unreviewed and not used as premises, were: \(\Pi=w\gamma T_{\mathrm{hold}}^2/A\); below \(\Pi_c\sim 16\) at small \(\gamma\tau\), an unrefreshed phase memory beats every periodic refresh; above \(\Pi_c\), periodic refresh wins at \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A\,w\,\gamma}\), so the stake exponent is \(0.50\pm 0.05\) against T68's \(w^{1/3}\); a T68 clock between refreshes lowers \(J^*\) only if the look carries more than \(4\kappa/\lambda\) nats (`theory/CLOCK_TERM_2026-11-23.md:125`). Two failure routes were named: \(1/f\) or other non-Markovian noise, and a nonzero unitary control heat. The last question is whether \(\Pi_c\) is T84's threshold \(w/\kappa>h(\varepsilon)/\varepsilon\) written in other variables (`theory/dephasing-crossover-2026-11-24/PREREG.md:100-104`).

## 1. Why this approach

The candidates were not reviewed. The rate above is not T84's stock \(\kappa I+q\kappa P_D+w L\). It is heat per unit time plus the stake on the time-averaged Hamming loss, the same time average T68 uses when a record is needed at a random moment inside an interval (`theory/CLOCK_TERM_2026-11-23.md:40`). Ruin stays outside the sum (`CORE.md:27`). Deriving the stationarity condition decides the threshold. The candidate \(16\) is then a reading to identify, not a number to fit.

## 2. Class RF

The bit starts pure at a refresh. Pure dephasing multiplies the coherence by \(e^{-\gamma t}\). The Hamming loss at age \(t\) is the T84 expression

\[
\varepsilon(t)=\frac{1-e^{-\gamma t}}{2}.
\]

The use time is uniform on the inter-refresh interval, so

\[
\bar L(u)=\frac12-\frac{1-e^{-u}}{2u},\qquad u=\gamma\tau>0,
\]

and \(\bar L(0)=0\). A refresh re-prepares the pure phase and costs heat \(A\). It is not T84's pointer encoding: that encoding has loss \(0\) for every later time (`theory/dephasing-crossover-2026-11-24/PREREG.md`), so repeating it on a static bit would be pure waste. Here the tracked phase keeps dephasing, and the refresh resets the age.

A hold of length \(T\) is split into \(n\ge 1\) equal intervals of length \(\tau=T/n\).

**Accounting A** (opening preparation charged to every policy, including \(n=1\)):

\[
J=\frac{A}{\tau}+w\,\bar L(\gamma\tau).
\]

**Accounting B** (the opening preparation is sunk, and only later refreshes are charged):

\[
J=\frac{(n-1)A}{T}+w\,\bar L(\gamma\tau)=A\Big(\frac1\tau-\frac1T\Big)+w\,\bar L(\gamma\tau).
\]

Unrefreshed means \(n=1\). In A its rate is \(A/T+w\bar L(\gamma T)\). In B its rate is \(w\bar L(\gamma T)\).

**Accounting C**, the candidate comparison, charges \(A/\tau\) on the refresh side and charges the unrefreshed side nothing, even though both start from a fresh state. That is recorded in §4. It is not the score of class RF.

Dimensionless groups: \(\Theta=\gamma T\), \(s=w/(\gamma A)\), \(\Pi=s\Theta^2=w\gamma T^2/A\). Rates below are in units of \(\gamma A\), written \(j\).

## 3. Derivation

For \(u>0\),

\[
\bar L'(u)=\frac{1-(1+u)e^{-u}}{2u^2}>0.
\]

\(\bar L''<0\) on \((0,\infty)\): the script checks the sign of a centered difference on the locked grid, and the closed form of \(\bar L'\) is the object it differentiates. Stationarity of accounting A,

\[
\frac{d}{du}\Big(\frac1u+s\bar L(u)\Big)=0,
\]

is

\[
s=s_*(u)=\frac{2}{1-(1+u)e^{-u}}\qquad(u>0).
\]

\(s_*(u)\) falls from \(+\infty\) at \(u\to 0\) to \(2\) at \(u\to\infty\). For \(s\le 2\) the derivative of \(j\) is strictly negative, so the rate keeps falling as the period grows and the infimum is the saturated loss \(s/2\), with no finite refresh. For \(s>2\) there is one critical point, a minimum, at the unique \(u_*\) with \(s_*(u_*)=s\).

On a finite hold the critical point lies inside \((0,\Theta)\) if and only if \(s>s_*(\Theta)\). At \(s=s_*(\Theta)\) it sits at \(\tau=T\), which is \(n=1\). For \(s>s_*(\Theta)\) the interior minimum is strictly below the value at \(\tau=T\), in both A and B, because B differs from A by the constant \(-1/\Theta\) and the unrefreshed value in B differs from the unrefreshed value in A by the same constant. So A and B name the same boundary:

\[
\Pi_c(\Theta)=s_*(\Theta)\,\Theta^2=\frac{2\Theta^2}{1-(1+\Theta)e^{-\Theta}}.
\]

Below it, every \(n\ge 2\) is strictly worse than \(n=1\). Above it, the interior period wins.

Small \(\Theta\): \(1-(1+\Theta)e^{-\Theta}=\Theta^2/2-\Theta^3/3+\Theta^4/8+O(\Theta^5)\), so

\[
\Pi_c(\Theta)=4+\frac83\Theta+\frac79\Theta^2+O(\Theta^3).
\]

Thus \(\Pi_c\to 4\) as \(\gamma T\to 0\). The candidate \(\sim 16\) is not this limit.

At that same limit, \(s_*(u)\sim 4/u^2\), so

\[
\gamma\tau_*=u_*\sim 2\sqrt{\frac{\gamma A}{w}}=2\gamma\sqrt{\frac{A}{w\gamma}},\qquad
\frac{J^*}{\sqrt{A\,w\,\gamma}}\to 1.
\]

The candidate expressions for \(\tau^*\) and \(J^*\) are this leading term. The exact period is \(u_*\), not the square root, once \(\gamma\tau_*\) is finite.

The stake elasticity at the minimum equals the loss share, by the envelope theorem:

\[
e(u_*)=\frac{\partial\ln J^*}{\partial\ln w}=\frac{s\bar L(u_*)}{1/u_*+s\bar L(u_*)}.
\]

As \(u_*\to 0\), \(e\to 1/2\) from above. T68's no-clock branch scales as \(w^{1/3}\) because a deterministic lag grows as \(1/f^2\) (`theory/CLOCK_TERM_2026-11-23.md:53-55`). Short-time dephasing loss grows as one power of the age, and the time average keeps that power, so the balance of \(A/\tau\) against \(w\tau\) is a square root. The worked-class OU minimum is also a square root above its stake, with an extra \(-kTa\) (`CORE.md:91`). That subtracted term is not derived here.

## 4. Where this differs from the candidates

1. **\(\Pi_c\to 4\), not \(\sim 16\).** Accounting C compares \(w\bar L(\gamma T)\) with \(\min_\tau(A/\tau+w\bar L(\gamma\tau))\) and drops \(A/T\) on one side only. In the linear loss \(\bar L(u)\sim u/4\) that comparison ties at \(\Pi=16\). Its exact boundary pairs a period \(u\) with a hold \(\Theta\) by \(\bar L(\Theta)=\bar L(u)+u\bar L'(u)\), and sets \(\Pi=s_*(u)\,\Theta^2\). The script computes that pair and labels it C. A pass of C does not make 16 the threshold of A or B.
2. **The band \(0.50\pm 0.05\) is the short-period side only.** \(e(u)\) is increasing in \(u\). The lock is \(e(0.5)<0.55\) and \(e(1)>0.55\). At \(\gamma\tau_*=1\) the exact elasticity is outside the candidate band.
3. **A T68 clock does not lower this \(J^*\).** \(\bar L\) does not depend on a clock rate. The TUR term \(\kappa kT\,\omega'^2/D\) (`theory/CLOCK_TERM_2026-11-23.md:19-21`) is nonnegative, and it is zero at \(\omega'=0\). The minimum over the clock leaves \(J^*\) unchanged at every \(I_0\), including on both sides of \(4\kappa/\lambda\). Inside T68's class CK, with Poisson time-averaged loss coefficients \(a=1\), \(b=2\), the fixed-price onset is \(c^*=2\kappa kT\,b/a=4\kappa kT\) (`theory/CLOCK_TERM_2026-11-23.md:45`). With \(c=\lambda kT\,I_0\) that is \(I_0=4\kappa/\lambda\) (`theory/CLOCK_TERM_2026-11-23.md:125`). That onset is a theorem of class CK. It is not a threshold of class RF.
4. **\(\Pi_c\) is not T84's \(h(\varepsilon)/\varepsilon\).** T84 compares one stock cost at one horizon. RF compares rates of repeated preparation. As functions of the same \(\Theta=\gamma T\), \(t(\Theta)=h(\varepsilon)/\varepsilon\) with \(\varepsilon=(1-e^{-\Theta})/2\) falls, and \(\Pi_c(\Theta)\) rises, on the locked grid. They are not the same boundary in other variables.

## 5. Failure routes, locked as predictions

**F1. Non-Markovian probe.** Replace the coherence \(e^{-\gamma t}\) by the Gaussian envelope \(e^{-(\gamma t)^2}\). This is the probe for the named \(1/f\) / non-Markovian route. It is not a fitted spectrum. At short time the Hamming loss is \((\gamma t)^2/2\) and the time average is \((\gamma\tau)^2/6\). Then

\[
J=\frac{A}{\tau}+w\frac{\gamma^2\tau^2}{6},\qquad
\tau^3=\frac{3A}{w\gamma^2},\qquad
\frac{\partial\ln J^*}{\partial\ln w}=\frac13.
\]

The exponent \(1/2\) fails on this probe. The \(1/3\) is the same power T68 gets from a quadratic lag, from a different loss.

**F2. Unitary control heat.** Add a heat \(H_u>0\) on every refresh, and keep defining \(\Pi\) with the Landauer piece \(A\) alone. The true heat per refresh is \(A+H_u\), so the threshold in that \(\Pi\) is \(\Pi_c(\Theta)\,(1+H_u/A)\). The locked case is \(H_u=A\): the small-\(\Theta\) limit is \(8\), not \(4\). A quote of \(4\) that ignores \(H_u\) is wrong on this route.

## 6. What is locked

Grid \(\Theta\in\{0.01,0.1,0.5,1,2\}\) and \(u\in\{0.01,0.1,0.5,1,2\}\). Tolerances: closed forms \(10^{-9}\); series at \(\Theta=0.01\), absolute gap \(10^{-6}\); square-root ratios at \(u=0.01\), absolute gap \(5\times 10^{-3}\). \(\kappa=\lambda=1\) only in the clock probes \(I_0\in\{1,4,10\}\). No seed. Stdlib only.

| id | lock |
| --- | --- |
| R0 | \(\bar L\), \(\bar L'\), and \(s_*\) match the formulas in §3, and \(\bar L''<0\) on the \(u\) grid |
| R1 | A and B share \(\Pi_c(\Theta)\). Below it every split \(n\ge 2\) loses; above it an interior period wins. Checked at \(s=s_*/2\) and \(s=3s_*/2\) on the \(\Theta\) grid |
| R2 | \(\Pi_c(0.01)\) matches \(4+(8/3)(0.01)+(7/9)(0.01)^2\) within \(10^{-6}\), and \(\Pi_c(0.01)<4.05\). The limit named by the series is 4 |
| R3 | At \(u=0.01\), \(\lvert u\sqrt{s_*(u)}/2-1\rvert<5\times 10^{-3}\) and \(\lvert j/\sqrt{s_*(u)}-1\rvert<5\times 10^{-3}\) |
| R4 | \(e(0.01)<0.505\), \(e(0.5)<0.55\), \(e(1)>0.55\), and \(e(2)>e(1)\) |
| R5 | Accounting C at its own boundary tends to 16: at \(u=10^{-4}\), \(\lvert\Pi-16\rvert<5\times 10^{-3}\); at \(u=0.01\), \(\Pi\in(16.1,16.2)\). This is not R1 |
| R6 | F1: the quadratic balance has elasticity \(1/3\) within \(10^{-12}\) |
| R7 | F2 at \(H_u=A\): small-\(\Theta\) threshold in the Landauer \(\Pi\) is 8. The script checks \(2\,\Pi_c(0.01)\) against \(8+(16/3)(0.01)+(14/9)(0.01)^2\) within \(2\times 10^{-6}\) |
| R8 | Adding a nonnegative clock heat does not lower \(j\) at \(I_0\in\{1,4,10\}\). The CK arithmetic \(2\kappa kT\cdot b/a\) with \(a=1\), \(b=2\) equals \(4\kappa kT\) |
| R9 | On the \(\Theta\) grid, \(t(\Theta)\) strictly falls, \(\Pi_c(\Theta)\) strictly rises, \(\Pi_c-t\) is negative at \(0.01\) and positive at \(1\) |

Headline `CLUE_REFRESH` if R0–R9 all hold. If R2 fails because the finite-hold limit is 16, the headline is `PUZZLE`, including if R5 holds. The script computes the label from the booleans and does not print `CLUE_REFRESH` after a miss.

## 7. Prior art already in the repo

Landauer's bound, as this repo states it, is at least \(kT\ln 2\) per bit (`theory/SCALE_ENDS.md:23`). T68's onset and its \(w^{1/3}\) are the citations in §4. T84's threshold is `theory/dephasing-crossover-2026-11-24/PREREG.md:100-104`. No new DOI is introduced. The Gaussian envelope is a defined probe, not a claim that a published \(1/f\) spectrum equals \(e^{-(\gamma t)^2}\).
