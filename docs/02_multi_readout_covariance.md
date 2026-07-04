# 02 — Multi-Readout Covariance

## 1. Multiple readouts

Tau Core allows several physically admissible readout projectors:

\[
\Pi_i,\quad i=1,\dots,N.
\]

Each must satisfy:

\[
\Pi_i^\dagger\eta_\tau\Pi_i\geq0.
\]

Two readouts can both be positive while noncommuting:

\[
[\Pi_i,\Pi_j]\neq0.
\]

This means they are not the same physical observable sector.

## 2. No double counting principle

Double counting would occur if:

\[
\Pi_i=\Pi_j
\]

and:

\[
\mathcal{A}_i=\mathcal{A}_j
\]

while treating the same observable as independent evidence.

Tau Core instead uses:

\[
\Pi_i\neq\Pi_j,
\]

\[
\mathcal{A}_i\neq\mathcal{A}_j,
\]

but:

\[
\Pi_i,\Pi_j,\mathcal{A}_i,\mathcal{A}_j
\leftarrow
\mathfrak{P}_\tau.
\]

Thus different channels are partially correlated projections, not duplicate measurements.

## 3. Residual model

A residual in readout channel \(i\) is:

\[
\delta_i(t)
=
M_i\Pi_iU_\tau(t)\delta\Psi_\tau(0)+n_i(t).
\]

Where:

- \(M_i\): measurement/response operator,
- \(\Pi_i\): readout projector,
- \(U_\tau(t)\): parent evolution,
- \(\delta\Psi_\tau(0)\): parent perturbation,
- \(n_i(t)\): noise/systematics.

## 4. Cross-readout covariance

Parent perturbation covariance:

\[
\Sigma_\tau
=
\langle
\delta\Psi_\tau(0)\delta\Psi_\tau^\dagger(0)
\rangle.
\]

Then:

\[
\boxed{
\mathrm{Cov}_{ij}(t,t')
=
M_i
\Pi_i
U_\tau(t)
\Sigma_\tau
U_\tau^\dagger(t')
\Pi_j^\dagger
M_j^\dagger
+
N_{ij}(t,t').
}
\]

This is the central empirical Tau Core equation.

## 5. Main prediction

Tau Core does not predict that residuals are identical:

\[
\delta_i\neq\delta_j.
\]

It predicts:

\[
\boxed{
\text{shared parent}
\Rightarrow
\text{structured cross-readout covariance}.
}
\]

## 6. Evidence hierarchy

A single anomaly:

\[
\delta_i\neq0
\]

is insufficient.

A candidate Tau Core signal requires:

\[
\mathrm{Cov}_{ij}^{obs}-N_{ij}\neq0
\]

with:

- surrogate survival,
- out-of-sample validation,
- parameter penalty,
- independent null controls.

## 7. Multi-axis diagnostic

The synthetic audits show that Tau Core should not be reduced to one scalar score.

Preferred diagnostic space:

\[
(Z_{\text{shared}},Z_{\text{orient}},\ldots).
\]

Primary:

\[
Z_{\text{shared}}.
\]

Secondary:

\[
Z_{\text{orient}}.
\]
