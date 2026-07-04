# 01 — Tau Core Readout Positivity and Parent Formalism

## 1. Parent state system

Tau Core uses a parent system:

\[
\mathfrak{P}_\tau
=
(\mathcal{P}_\tau,\eta_\tau,H_\tau,\mathcal{A}_\tau,\Sigma_\tau).
\]

Where:

- \(\mathcal{P}_\tau\): parent state space,
- \(\eta_\tau\): parent pairing / metric,
- \(H_\tau\): parent generator,
- \(\mathcal{A}_\tau\): parent observable algebra,
- \(\Sigma_\tau\): parent perturbation covariance.

The parent space is not required to be a positive Hilbert space.

A minimal indefinite toy metric is:

\[
\eta_\tau =
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

For:

\[
\Psi_\tau =
\begin{pmatrix}
\psi_+\\
\psi_-
\end{pmatrix},
\]

the parent norm is:

\[
\langle\Psi_\tau|\Psi_\tau\rangle_\eta
=
|\psi_+|^2-|\psi_-|^2.
\]

This can be positive, null, or negative.

Tau Core claim:

\[
\boxed{
\text{Parent-level indefiniteness is not physical pathology unless it survives the readout as negative observable norm/probability.}
}
\]

## 2. Readout projector

A physical readout is represented by a projector:

\[
\Pi_i:\mathcal{P}_\tau\rightarrow\mathcal{P}_\tau.
\]

The induced readout metric is:

\[
\eta_i
=
\Pi_i^\dagger\eta_\tau\Pi_i.
\]

The admissibility condition is:

\[
\boxed{
\Pi_i^\dagger\eta_\tau\Pi_i\geq0.
}
\]

This is the **Tau Core Readout Positivity Principle**.

## 3. Positive readout cone

\[
\mathcal{C}_\tau^+
=
\{
\Psi_\tau:
\langle\Psi_\tau|\Psi_\tau\rangle_{\eta_\tau}\geq0
\}.
\]

A readout is allowed when:

\[
\operatorname{Im}(\Pi_i)\subseteq\mathcal{C}_\tau^+.
\]

In the two-component model:

\[
v(r)=
\begin{pmatrix}
1\\
r
\end{pmatrix},
\]

\[
v(r)^\dagger\eta_\tau v(r)=1-r^2.
\]

So:

- \(|r|<1\): positive readout,
- \(|r|=1\): null readout,
- \(|r|>1\): ghost-dominant nonphysical readout.

## 4. Parent dynamics

Parent dynamics:

\[
i\frac{d}{dt}\Psi_\tau=H_\tau\Psi_\tau.
\]

For indefinite metric, the stability condition is pseudo-Hermiticity:

\[
\boxed{
H_\tau^\dagger\eta_\tau=\eta_\tau H_\tau.
}
\]

Then:

\[
U_\tau^\dagger(t)\eta_\tau U_\tau(t)=\eta_\tau.
\]

A minimal two-component generator:

\[
H_\tau
=
\begin{pmatrix}
a&b\\
-b^*&d
\end{pmatrix},
\quad
a,d\in\mathbb{R}.
\]

For real \(b\), the eigenvalues are:

\[
\lambda_\pm
=
\frac{a+d}{2}
\pm
\sqrt{
\left(\frac{a-d}{2}\right)^2-b^2
}.
\]

Stable regime:

\[
|b|\leq\left|\frac{a-d}{2}\right|.
\]

Define:

\[
\epsilon_\tau
=
\frac{|b|}
{
\left|\frac{a-d}{2}\right|
}.
\]

Then:

\[
\epsilon_\tau\leq1
\]

is the minimal toy stability condition.

## 5. Readout algebra

The parent observable algebra is:

\[
\mathcal{A}_\tau.
\]

A readout algebra is:

\[
\boxed{
\mathcal{A}_i=
\Pi_i^\dagger\mathcal{A}_\tau\Pi_i.
}
\]

Thus:

\[
\boxed{
\text{A physical observable is a readout-projected parent observable.}
}
\]

Two readouts can share the same parent but have different observable algebras:

\[
\mathcal{A}_i\neq\mathcal{A}_j,
\quad
\mathcal{A}_i,\mathcal{A}_j\leftarrow\mathcal{A}_\tau.
\]

This prevents double-counting when different channels are treated as separate readouts.
