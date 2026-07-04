from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"


def main() -> None:
    overall = pd.read_csv(DERIVED / "taucore_v11_overall_summary.csv")
    class_rates = pd.read_csv(DERIVED / "taucore_v11_class_rates.csv")

    tau = overall[overall["is_tau_world"] == True].iloc[0]  # noqa: E712
    null = overall[overall["is_tau_world"] == False].iloc[0]  # noqa: E712
    null_rates = class_rates[class_rates["is_tau_world"] == False].iloc[0]  # noqa: E712

    rows = [
        ("tauworld_shared_parent_recovery", float(tau["shared_recovery_rate"])),
        ("nullworld_shared_parent_false_positive", float(null["shared_recovery_rate"])),
        ("tauworld_orientation_detection", float(tau["orientation_detection_rate"])),
        ("nullworld_orientation_only_rate", float(null_rates["C_orientation_only"])),
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
