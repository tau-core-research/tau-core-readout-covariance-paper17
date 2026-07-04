# Tau Core v12 Synthetic Validation Report
## Multi-axis diagnostic strategy for parent-readout covariance

**Status:** synthetic-methodology report
**Scope:** controlled toy simulations, not empirical cosmological evidence
**Date:** 2026-07-03

---

## 0. Executive summary

The Tau Core v8–v11 synthetic programme tested whether a hidden shared parent field can be detected through cross-readout residual covariance.

The core result is:

\[
\boxed{
\text{Shared-parent covariance is robustly detectable in synthetic controls.}
}
\]

However, the audits also show that morphology/orientation evidence must be treated as a **secondary diagnostic**, not as a primary detector.

The final v11 classifier supports a two-axis Tau Core diagnostic space:

\[
\boxed{
(Z_{\text{shared}}, Z_{\text{orient}})
}
\]

where:

- \(Z_{\text{shared}}\) measures shared-parent cross-readout covariance,
- \(Z_{\text{orient}}\) measures morphology/orientation-like structure.

The correct hierarchy is:

\[
\boxed{
\text{Shared-parent evidence first; morphology/orientation only as conditional reinforcement.}
}
\]

---

## 1. Background

The Tau Core parent-readout formalism proposes:

\[
\mathfrak{P}_\tau
=
(\mathcal{P}_\tau,\eta_\tau,H_\tau,\mathcal{A}_\tau,\Sigma_\tau)
\]

as a deeper parent system, with physical readouts:

\[
\mathcal{R}_i
=
(\Pi_i,\eta_i,\mathcal{A}_i,M_i).
\]

A residual in channel \(i\) is modeled as:

\[
\delta_i(t)
=
M_i\Pi_iU_\tau(t)\delta\Psi_\tau(0)+n_i(t).
\]

The predicted cross-readout covariance is:

\[
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
\]

The first synthetic test focuses on:

\[
\delta_L \times \delta_F
\]

where:

- \(\delta_L\): lensing-like residual,
- \(\delta_F\): filament/morphology-like residual.

---

## 2. Synthetic world design

Two worlds were tested.

### 2.1 Tau-like shared-parent world

\[
P_\tau \rightarrow \delta_L
\]

\[
P_\tau \rightarrow \delta_F
\]

Both residuals are generated from the same hidden parent field.

Expected:

\[
Z_{\text{shared}}>3.
\]

If the parent is strongly anisotropic, morphology/orientation diagnostics may also appear:

\[
Z_{\text{orient}}>2.
\]

### 2.2 Null independent-parent world

\[
P_L \rightarrow \delta_L
\]

\[
P_F \rightarrow \delta_F
\]

with:

\[
P_L\perp P_F.
\]

Expected:

\[
Z_{\text{shared}}\leq3.
\]

Any orientation-like signal without shared-parent support is treated as insufficient.

---

## 3. v8: Shared-parent strength detector

### 3.1 Method

v8 used a cross-correlation strength score:

\[
S_{\text{shared}}
=
\sum_{\Delta}
|C_\parallel(\Delta)|
+
\sum_{\Delta}
|C_\perp(\Delta)|.
\]

The surrogate score was computed using rotation, phase randomization, and shuffle controls:

\[
Z_{\text{shared}}
=
\frac{
S_{\text{true}}-\mu(S_{\text{sur}})
}{
\sigma(S_{\text{sur}})
}.
\]

### 3.2 Result

v8 found:

\[
\text{NullWorld no-false-positive pass rate}=100\%.
\]

TauWorld recovery under a strict combined strength+anisotropy rule was only:

\[
25.2\%.
\]

But the shared-parent strength itself was very strong:

\[
Z_{\text{shared}}\approx6\text{--}7
\]

in TauWorld, and near zero in NullWorld.

### 3.3 Verdict

\[
\boxed{
\text{v8 shared-parent strength detector: KEEP}
}
\]

Reason:

- strong TauWorld recovery on the shared-parent axis,
- zero shared-parent false positives in NullWorld.

---

## 4. v9: Matched-filter anisotropy

### 4.1 Method

v9 attempted to replace the rough anisotropy score with a matched-filter profile:

\[
A_{LF}^{matched}
=
\frac{
\langle C_{LF},K_\parallel\rangle
}{
\langle C_{LF},K_\perp\rangle
}.
\]

### 4.2 Result

v9 degraded performance:

\[
\text{TauWorld pass rate}=1.48\%.
\]

\[
\text{NullWorld no-false-positive pass rate}=75.6\%.
\]

### 4.3 Diagnosis

The matched filter was too specific. It assumed:

\[
K_\tau
\approx
C_{LF}.
\]

But in Tau Core, readout maps are not identity maps:

\[
\text{parent kernel}
\rightarrow
\text{readout response}
\rightarrow
\text{observable covariance}.
\]

The morphology readout used a nonlinear Hessian-based filament score, which distorted the simple parent-kernel shape.

### 4.4 Verdict

\[
\boxed{
\text{v9 matched-filter anisotropy: REJECT}
}
\]

Reason:

- poor TauWorld recovery,
- increased NullWorld false-positive risk,
- over-specified observable covariance shape.

---

## 5. v10: Orientation diagnostic

### 5.1 Method

v10 tested whether the morphology signal contains local orientation information.

It used:

\[
Z_{\text{orient}}
\]

derived from orientation-weighted morphology correlations and orientation-randomized surrogates.

### 5.2 Result

v10 did not work as a primary detector:

\[
\text{TauWorld pass rate}=0\%.
\]

But it did show useful secondary structure:

\[
\text{TauWorld mean }Z_{\text{orient anisotropy}}\approx2.4,
\]

while:

\[
\text{NullWorld mean }Z_{\text{orient anisotropy}}\approx1.0.
\]

At stronger parent anisotropy:

\[
\ell_\parallel/\ell_\perp=5,
\]

TauWorld reached roughly:

\[
Z_{\text{orient}}\approx2.7\text{--}3.2.
\]

### 5.3 Verdict

\[
\boxed{
\text{v10 orientation diagnostic: KEEP AS SECONDARY}
}
\]

Reason:

- not sufficient as a primary detector,
- useful as a conditional morphology/orientation reinforcement,
- should only matter after shared-parent evidence is present.

---

## 6. v11: Two-axis classifier

### 6.1 Motivation

v9 and v10 showed that a single scalar Tau score is the wrong strategy.

The synthetic results support a two-axis diagnostic space:

\[
\boxed{
(Z_{\text{shared}},Z_{\text{orient}})
}
\]

where:

\[
Z_{\text{shared}}
\]

measures cross-readout shared-parent covariance, and:

\[
Z_{\text{orient}}
\]

measures morphology/orientation reinforcement.

### 6.2 Classes

The v11 classifier defines four classes.

#### Class A — shared parent + orientation

\[
Z_{\text{shared}}>3,
\quad
Z_{\text{orient}}>2.
\]

Interpretation:

\[
\boxed{
\text{strong Tau-like synthetic signature}
}
\]

#### Class B — shared parent only

\[
Z_{\text{shared}}>3,
\quad
Z_{\text{orient}}\leq2.
\]

Interpretation:

\[
\boxed{
\text{shared-parent evidence without robust orientation reinforcement}
}
\]

#### Class C — orientation-like only

\[
Z_{\text{shared}}\leq3,
\quad
Z_{\text{orient}}>2.
\]

Interpretation:

\[
\boxed{
\text{not sufficient for Tau Core claim}
}
\]

This may occur in NullWorld and must not be overinterpreted.

#### Class D — null

\[
Z_{\text{shared}}\leq3,
\quad
Z_{\text{orient}}\leq2.
\]

Interpretation:

\[
\boxed{
\text{no Tau-like evidence}
}
\]

### 6.3 Result

TauWorld:

\[
\text{shared-parent recovery}=100\%.
\]

Class split:

\[
48.9\% \rightarrow \text{Class A},
\]

\[
51.1\% \rightarrow \text{Class B}.
\]

NullWorld:

\[
\text{shared-parent false positive}=0\%.
\]

Class split:

\[
77.0\% \rightarrow \text{Class D},
\]

\[
23.0\% \rightarrow \text{Class C}.
\]

### 6.4 Key lesson

Orientation-like structure can appear in NullWorld:

\[
\text{Class C exists}.
\]

Therefore:

\[
\boxed{
Z_{\text{orient}}\text{ alone is not evidence for Tau Core.}
}
\]

The primary evidence must be:

\[
\boxed{
Z_{\text{shared}}>3.
}
\]

### 6.5 Verdict

\[
\boxed{
\text{v11 two-axis classifier: KEEP}
}
\]

---

## 7. Scientific meaning

The synthetic tests do not prove Tau Core physically.

They do show that the **methodological core** is coherent:

\[
\boxed{
\text{A shared parent can be detected through cross-readout covariance in controlled synthetic worlds.}
}
\]

They also show that Tau Core must avoid overclaiming morphology-only signals:

\[
\boxed{
\text{Morphology/orientation is conditional secondary evidence, not standalone evidence.}
}
\]

This is a major methodological constraint and strengthens the scientific discipline of the programme.

---

## 8. Updated Tau Core claim hierarchy

### Level 1 — weak indication

A single residual anomaly:

\[
\delta_i\neq0.
\]

Interpretation:

\[
\text{insufficient}.
\]

### Level 2 — shared-parent covariance

\[
Z_{\text{shared}}>3.
\]

Interpretation:

\[
\text{candidate Tau Core readout relation}.
\]

### Level 3 — shared parent + morphology/orientation

\[
Z_{\text{shared}}>3,
\quad
Z_{\text{orient}}>2.
\]

Interpretation:

\[
\text{stronger Tau-like morphology-shaped readout signature}.
\]

### Level 4 — out-of-sample multi-survey survival

\[
\Delta BIC_{test}>0
\]

across multiple datasets.

Interpretation:

\[
\text{serious empirical candidate}.
\]

### Level 5 — physical model closure

The parent, projectors, dynamics, and response operators are independently constrained:

\[
(\mathcal{P}_\tau,\eta_\tau,H_\tau,\mathcal{A}_\tau,\Pi_i,M_i)
\]

with minimal tuning.

Interpretation:

\[
\text{mature Tau Core physical theory}.
\]

Current status:

\[
\boxed{
\text{Level 2 synthetic validation achieved; Level 3 partially achieved in synthetic controls.}
}
\]

---

## 9. What was rejected

The synthetic programme rejected three unsafe strategies.

### 9.1 Single-score Tau detector

Rejected because shared-parent evidence and morphology/orientation evidence behave differently.

\[
\boxed{
\text{No single scalar Tau score at this stage.}
}
\]

### 9.2 Matched-filter anisotropy as primary evidence

Rejected because readout transformations distort parent kernels.

\[
\boxed{
K_\tau\not\approx C_{LF}\text{ directly.}
}
\]

### 9.3 Orientation-only Tau claims

Rejected because orientation-like signals can occur in NullWorld.

\[
\boxed{
Z_{\text{orient}}>2
\text{ without }
Z_{\text{shared}}>3
\text{ is not enough.}
}
\]

---

## 10. What was retained

### 10.1 Shared-parent cross-readout covariance

Retained as the primary synthetic detector.

\[
\boxed{
Z_{\text{shared}}
}
\]

### 10.2 Orientation/morphology diagnostic

Retained as secondary.

\[
\boxed{
Z_{\text{orient}}
}
\]

### 10.3 Multi-axis diagnostic space

Retained as the correct methodology.

\[
\boxed{
(Z_{\text{shared}},Z_{\text{orient}},\ldots)
}
\]

### 10.4 NullWorld discipline

Retained as mandatory.

\[
\boxed{
\text{No real-data claim without independent-parent/null controls.}
}
\]

---

## 11. Implications for real data

Before any real cosmological claim, the protocol must use:

1. baseline-subtracted lensing residuals,
2. baseline-subtracted morphology residuals,
3. phase/randomization controls,
4. orientation controls,
5. survey-mask controls,
6. independent mocks,
7. train/test split,
8. out-of-sample validation,
9. parameter-count penalty,
10. class-based reporting.

Real-data classes should follow v11:

\[
\text{A: shared + orientation}
\]

\[
\text{B: shared only}
\]

\[
\text{C: orientation only}
\]

\[
\text{D: null}.
\]

Only A and B are Tau Core candidate classes.

C is a warning class.

D is null.

---

## 12. Recommended v13 next step

The next methodological step is not real survey data yet.

The next step should be a **mock-cosmology intermediate test**.

### v13 target

Replace simple Gaussian parent fields with more realistic mock fields:

- clustered density field,
- filament skeleton extraction,
- lensing-like projection,
- galaxy bias,
- survey mask,
- photo-z noise,
- shape noise.

Then run the v11 classifier:

\[
(Z_{\text{shared}},Z_{\text{orient}})
\]

on:

1. shared-parent mock,
2. independent-parent mock,
3. isotropic-parent mock,
4. mask-only mock,
5. orientation-scrambled mock.

The v13 success condition:

\[
\text{shared-parent recovery high},
\]

\[
\text{false shared-parent rate low},
\]

\[
\text{orientation only not overinterpreted}.
\]

---

## 13. Final synthetic validation statement

The Tau Core synthetic validation programme supports the following methodological claim:

\[
\boxed{
\text{Tau Core should be tested as a multi-axis readout-covariance programme, not as a single anomaly detector.}
}
\]

The primary synthetic result is:

\[
\boxed{
\text{Shared-parent cross-readout covariance can be recovered with zero shared-parent false positives in the tested NullWorld controls.}
}
\]

The secondary result is:

\[
\boxed{
\text{Morphology/orientation diagnostics are useful only conditionally, after shared-parent evidence is present.}
}
\]

The current validated synthetic status is:

\[
\boxed{
\text{v11 two-axis classifier retained; v9 matched-filter rejected; v10 orientation retained as secondary diagnostic.}
}
\]

This does not prove Tau Core physically, but it turns the framework into a more disciplined, falsifiable research programme.
