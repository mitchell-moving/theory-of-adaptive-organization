# T82e preregistration: one island in the lossless flow

*24 November 2026 (UTC). A new lock. No earlier preregistration is edited. Written and committed, with `PREREG_T82E.sha256` and the same hash in `RUN_LOG_T82E.md`, before any orbit of this scan.*

## Why this approach

The T82d islands were boundaries of the integer width menu. They moved when the floor moved, and they vanished when the floor was removed. That map also contracts. A resonance that is not a menu boundary has to be looked for where the vector field does not contract and the record has no width floor: the reversible flow of T82b, with the damping set to zero, and a record that is an average of a smooth function of the angle.

## Can it fail

Can it fail: yes. The width below is a pendulum reduction. Finite step size, a long period near the separatrix, or a wrong stable phase can put the measured width outside the band, or leave the center circulating. The loss average can be flat. A second rational can appear as a numerical island.

Cheapest way to fail it: one orbit at coupling \(0.04\), bare frequency \(1\), step \(0.05\), \(40000\) steps, start \((\theta_1,\theta_2)=(0,\pi)\), actions \(0\). If the rotation number is more than \(0.002\) from \(1\), the center is not on the island and the width prediction misses.

## What a miss changes

If the \(1/1\) width or the square-root scaling misses, the resonance thread on this toy is shelved. The next look is not another rational scan of this Hamiltonian. It is whether the continuous record is a smooth coordinate of the conserved actions, and that look needs its own preregistration.

If the \(1/1\) width and the scaling hit, and no rational with denominator \(2\) through \(5\) forms a plateau, stop. That is one island. It is not a staircase. No further tongue scan is opened on this coupling.

If a denominator from \(2\) to \(5\) does form a plateau, and the finer grid keeps it, that misses the one-harmonic prediction. The next step is a new preregistration that puts a second harmonic in the coupling. This file is not edited.

If the width hits and the cost gap misses, the island is in the rotation number and not in the cost. The cost is not used as a resonance detector for this toy.

## 1. The world

The flow is the T82b Hamiltonian with no damping. \(\beta=0.25\), \(\omega_1=1\), \(\gamma=0\). The coupling is \(\varepsilon\cos(\theta_1-\theta_2)\). The step is the Stormer–Verlet step already used for that flow, with the damping factor not applied. Time \(T=2000\). The coarse step is \(h=0.05\) (\(40000\) steps). The start is \(\theta=(0,\pi)\), \(I=(0,0)\), so the relative angle starts at the phase the reduction calls the center.

The scanned parameter is the bare second frequency \(\omega_2\), from \(0.50\) to \(1.50\) inclusive, step \(0.005\) (\(201\) values). Couplings \(\varepsilon\in\{0, 0.01, 0.04, 0.09\}\).

The cost stake \(w\) is not in the vector field. It enters only the averaged cost, at \(w=2\), \(\kappa=1\), and price \(1\). The predicted island width does not depend on \(w\).

There is no walk, no integer width, and no floor. The continuous record at a sample is the mean, over the steps, of

\[
J(\theta_2)=I(\theta_2)+P_D(\theta_2)+2\,L(\theta_2),
\]

with the same closed form used for the antenna at \(R=0.6\) and phase \(0\): binary entropy in nats, \(P_D=\tfrac12(h_b(\tfrac{1+R|\cos\theta_2|}{2})-h_b(\tfrac{1+R}{2}))\), information \(\tfrac12(\ln 2-h_b(\tfrac{1+R|\cos\theta_2|}{2}))\), and loss \(\tfrac12 R^2-(R^4\cos^2\theta_2)/4\).

## 2. How an island is detected

This is not a dissipative classifier. Nothing is tested for a fixed point of a contracting map.

The rotation number is the frequency ratio

\[
\nu=\frac{\theta_2(T)-\theta_2(0)}{\theta_1(T)-\theta_1(0)}.
\]

The same ratio is computed from the Poincaré samples taken when the unwrapped \(\theta_1\) crosses a multiple of \(2\pi\), as the advance of \(\theta_2\) per crossing divided by \(2\pi\). If the two ratios differ by more than \(10^{-3}\), the sample is `OTHER` and is not on an island.

The relative angle is \(\psi=\theta_1-\theta_2\). The sample librates if \(|\psi(T)-\psi(0)|<\pi\). It circulates otherwise.

A sample is on the \(1/1\) island only if it is not `OTHER`, \(|\nu-1|\le 0.002\), and it librates.

A plateau at a rational \(p/q\) is at least three consecutive grid values whose \(\nu\) is within \(0.002\) of that same \(p/q\). For \(1/1\), each of those samples must also be on the island as defined above. The measured width is the last grid value in the plateau minus the first, plus one grid step.

## 3. The scaling relation, the bands, and the odds

Reduce the relative angle. With \(\Delta=\omega_1-\omega_2\) and \(J=I_1-I_2\),

\[
\ddot\psi=2\beta\varepsilon\sin\psi.
\]

The center is \(\psi=\pi\). Set \(\phi=\psi-\pi\). Then \(\ddot\phi=-(2\beta\varepsilon)\sin\phi\). The separatrix energy, started from \(J=0\) at the center, confines the orbit when \(|\Delta|<2\sqrt{2\beta\varepsilon}\). With \(\beta=0.25\) the full width in \(\omega_2\) is

\[
W(\varepsilon)=2\sqrt{2}\,\sqrt{\varepsilon}.
\]

This is the area-preserving island width for a first harmonic, proportional to \(\varepsilon^{1/2}\). The dissipative circle-map relation for a tongue of order \(q\) is a width proportional to \(\varepsilon^{q}\). For \(q=1\) that rival is linear in \(\varepsilon\). It is not the prediction.

The Hamiltonian has no higher harmonic. For every rational with denominator \(q\) from \(2\) to \(5\), the predicted width is \(0\).

| Coupling | Ratio | Center | Predicted full width | Band |
|---|---|---|---|---|
| \(0.01\) | \(1/1\) | \(\omega_2=1\) | \(0.282842712475\) | within \(30\) percent |
| \(0.04\) | \(1/1\) | \(\omega_2=1\) | \(0.565685424949\) | within \(30\) percent |
| \(0.09\) | \(1/1\) | \(\omega_2=1\) | \(0.848528137424\) | within \(30\) percent |
| any of the three | \(q=2,3,4,5\) | none | \(0\) | plateau count \(0\) |

The scaling check is \(W(0.04)/W(0.01)=2\), accepted in \([1.4, 2.6]\). The linear rival gives \(4\), which lies outside that interval.

Odds, locked before the orbits. The null is \(\nu=\omega_2+\xi\) with \(|\xi|\le 0.002\). Three consecutive grid values span \(0.010\). A shift of at most \(0.002\) still leaves them outside a window of half-width \(0.002\) around one rational, because \(0.010>0.008\). The null probability of a three-point plateau at any \(p/q\) is \(0\). A single grid value lying within \(0.002\) of some reduced \(p/q\) with \(q\le 5\) and \(p/q\in[0.5,1.5]\) is not a plateau. There are \(11\) such rationals, and \(11\) of the \(201\) grid values meet one of them, fraction \(11/201=0.054726368159\). That single-value fraction is the look-elsewhere baseline. It is not evidence.

## 4. Predictions

**P-width.** At each of \(\varepsilon=0.01\), \(0.04\), and \(0.09\), the \(1/1\) samples form one plateau that contains the grid value \(\omega_2=1\), and the measured width is within \(30\) percent of the predicted width. Misses if any coupling has no such plateau, or if \(|W_{\mathrm{meas}}/W(\varepsilon)-1|>0.30\). Signed size: \(W_{\mathrm{meas}}-W(\varepsilon)\), in the frequency \(\omega_2\).

**P-scale.** \(W(0.04)/W(0.01)\) lies in \([1.4, 2.6]\). Misses if the ratio is outside that interval, or if either width is undefined. Signed size: the ratio minus \(2\). The linear rival \(4\) is outside the interval, so a hit of this row is not a hit of the circle-map exponent.

**P-higher.** At each positive coupling, the number of plateaus at rationals with denominator \(2\), \(3\), \(4\), or \(5\) is \(0\). Misses if the count is positive. Signed size: the count, minus \(0\).

**P-eps0.** At \(\varepsilon=0\), the number of grid values with \(|\nu-1|\le 0.002\) is at most \(1\). Misses if the count is \(2\) or more. Signed size: the count minus \(1\), and a count of \(0\) or \(1\) is a hit with margin \(1\) minus the count.

**P-record.** At \(\varepsilon=0.04\) and stake \(w=2\), let \(J_{\mathrm{in}}\) be the continuous record at the grid value \(\omega_2=1\), and let \(J_{\mathrm{out}}\) be the mean of the records at the first grid values strictly outside the two ends of the \(1/1\) plateau. \(|J_{\mathrm{in}}-J_{\mathrm{out}}|\ge 0.002\). Misses if the gap is smaller, or if the plateau is missing. Signed size: the absolute gap minus \(0.002\). No prior frequency is claimed for this bar. The bar is \(0.002\), about half a percent of the circulating cost scale near \(0.42\).

**P-refine.** At \(\varepsilon=0.04\), repeat the scan with \(h=0.025\) (\(80000\) steps, the same time \(T=2000\)) and grid step \(0.0025\) on \([0.70, 1.30]\). The \(1/1\) plateau still contains \(\omega_2=1\), and its width is within \(30\) percent of the coarse width at the same coupling. Misses if the fine plateau is absent or \(|W_{\mathrm{fine}}/W_{\mathrm{coarse}}-1|>0.30\). Signed size: \(W_{\mathrm{fine}}-W_{\mathrm{coarse}}\).

## 5. What this file does not do

It does not score. It does not edit a locked preregistration, `THEORY.md`, or `CORE.md`. The flow is a toy. Nothing here is a claim about a physical pendulum, a fluid, or a celestial resonance. Deviations after this commit are appended. This file is not edited after the locking commit.
