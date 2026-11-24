# T83 deviations

The preregistration was not edited. The six `B-shape` fails stay fails.

1. **Window.** `PREREG.md:69` says \(N=120\) is a multiple of every \(q\le 8\). \(7\) does not divide \(120\). The residue classes are not equal, so \(R\) is not exactly \(1/7\). Copy count \(N_c=7\) still matches. `revival_phase_checks.out:52` is an unscored sum at \(N=840\), where \(7\) divides the window and \(R\) matches \(1/7\) to \(10^{-13}\). That line is not a score and does not clear `out:16`–`:21`.

2. **Off-diagonal.** `PREREG.md:141` writes \(I(r)=2\bigl((-1)^r-1\bigr)/(r^2\pi^2)\) and calls it \(\langle n|x^2|m\rangle\). The boundary term in that antiderivative dropped a factor of \(x\). Quadrature of \(\int_0^1 2\sin(n\pi x)\sin(m\pi x)\,x^2\,dx\) gives \(\langle 1|x^2|2\rangle=-0.180126548697\). The printed \(I(r)\) gives \(-0.360253097395\). The diagonal formula matches the integral, and `G-x2` checks only the diagonal (`out:48`). The scored `P-well` (`out:49`) is the matrix as printed. It passes its bars. `out:53` is the same bars on the integral, unscored: \(R(2\pi)=0.929538906895\), later maximum \(0.989130295842\). Same side of every locked bar. Not a rescore.
