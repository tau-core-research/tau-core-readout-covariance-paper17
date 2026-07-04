from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"


def wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total <= 0:
        raise ValueError("total must be positive")
    phat = successes / total
    denom = 1 + z**2 / total
    center = (phat + z**2 / (2 * total)) / denom
    half = z * ((phat * (1 - phat) / total + z**2 / (4 * total**2)) ** 0.5) / denom
    return max(0.0, center - half), min(1.0, center + half)


def main() -> None:
    overall = pd.read_csv(DERIVED / "taucore_v11_overall_summary.csv")
    class_rates = pd.read_csv(DERIVED / "taucore_v11_class_rates.csv")
    audit = pd.read_csv(DERIVED / "taucore_v11_two_axis_classifier_audit.csv")

    tau = overall[overall["is_tau_world"] == True].iloc[0]  # noqa: E712
    null = overall[overall["is_tau_world"] == False].iloc[0]  # noqa: E712
    null_rates = class_rates[class_rates["is_tau_world"] == False].iloc[0]  # noqa: E712
    tau_audit = audit[audit["is_tau_world"] == True]  # noqa: E712
    null_audit = audit[audit["is_tau_world"] == False]  # noqa: E712

    tau_n = len(tau_audit)
    null_n = len(null_audit)
    total_n = len(audit)
    tau_shared_success = int(tau_audit["shared_recovered"].sum())
    null_shared_success = int(null_audit["shared_recovered"].sum())
    null_orient_success = int(null_audit["orientation_detected"].sum())
    tau_shared_ci = wilson_interval(tau_shared_success, tau_n)
    null_shared_ci = wilson_interval(null_shared_success, null_n)
    null_orient_ci = wilson_interval(null_orient_success, null_n)

    rows = [
        ("total_runs", float(total_n)),
        ("tauworld_n", float(tau_n)),
        ("nullworld_n", float(null_n)),
        ("unique_seed_count", float(audit["seed"].nunique())),
        ("seed_min", float(audit["seed"].min())),
        ("seed_max", float(audit["seed"].max())),
        ("tauworld_shared_parent_recovery", float(tau["shared_recovery_rate"])),
        ("tauworld_shared_parent_recovery_ci95_low", tau_shared_ci[0]),
        ("tauworld_shared_parent_recovery_ci95_high", tau_shared_ci[1]),
        ("nullworld_shared_parent_false_positive", float(null["shared_recovery_rate"])),
        ("nullworld_shared_parent_false_positive_ci95_low", null_shared_ci[0]),
        ("nullworld_shared_parent_false_positive_ci95_high", null_shared_ci[1]),
        ("tauworld_orientation_detection", float(tau["orientation_detection_rate"])),
        ("nullworld_orientation_only_rate", float(null_rates["C_orientation_only"])),
        ("nullworld_orientation_only_rate_ci95_low", null_orient_ci[0]),
        ("nullworld_orientation_only_rate_ci95_high", null_orient_ci[1]),
        ("tauworld_mean_z_shared", float(tau["mean_z_shared"])),
        ("nullworld_mean_z_shared", float(null["mean_z_shared"])),
        ("tauworld_mean_z_orient", float(tau["mean_z_orient"])),
        ("nullworld_mean_z_orient", float(null["mean_z_orient"])),
    ]

    summary = pd.DataFrame(rows, columns=["metric", "value"])
    summary.to_csv(DERIVED / "paper17_readout_covariance_summary.csv", index=False)

    payload = {metric: value for metric, value in rows}
    payload["claim_boundary"] = "synthetic_methodology_not_empirical_validation"
    (DERIVED / "paper17_readout_covariance_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
