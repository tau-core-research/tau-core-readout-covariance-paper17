"""
Tau Core v11 two-axis classifier.

Inputs:
- v8 audit CSV with z_strength.
- v10 orientation audit CSV with z_orient_anisotropy.

Classifier:
A: shared parent + orientation
B: shared parent only
C: orientation-like only
D: null
"""

from pathlib import Path
import pandas as pd
import numpy as np

def classify(z_shared, z_orient, shared_thr=3.0, orient_thr=2.0):
    shared = z_shared > shared_thr
    orient = z_orient > orient_thr
    if shared and orient:
        return "A_shared_plus_orientation"
    if shared and not orient:
        return "B_shared_only"
    if (not shared) and orient:
        return "C_orientation_only"
    return "D_null"

def run_classifier(v8_csv, v10_csv, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df8 = pd.read_csv(v8_csv)
    df10 = pd.read_csv(v10_csv)

    keys = [
        "shared_parent",
        "ell_parallel",
        "ell_perp",
        "anisotropy_ratio",
        "noise",
        "r_lensing",
        "r_morphology",
        "seed",
    ]

    merged = pd.merge(
        df8[keys + ["z_strength"]],
        df10[keys + ["z_orient_anisotropy"]],
        on=keys,
        how="inner",
    )

    merged = merged.rename(
        columns={
            "z_strength": "z_shared",
            "z_orient_anisotropy": "z_orient",
        }
    )

    merged["class"] = merged.apply(
        lambda r: classify(r["z_shared"], r["z_orient"]),
        axis=1,
    )

    merged["is_tau_world"] = merged["shared_parent"].astype(bool)
    merged["shared_recovered"] = merged["class"].isin(
        ["A_shared_plus_orientation", "B_shared_only"]
    )
    merged["orientation_detected"] = merged["class"].isin(
        ["A_shared_plus_orientation", "C_orientation_only"]
    )

    audit_path = output_dir / "taucore_v11_two_axis_classifier_audit.csv"
    merged.to_csv(audit_path, index=False)

    summary = merged.groupby("is_tau_world").agg(
        n=("class", "size"),
        shared_recovery_rate=("shared_recovered", "mean"),
        orientation_detection_rate=("orientation_detected", "mean"),
        class_A_rate=("class", lambda s: np.mean(s == "A_shared_plus_orientation")),
        class_B_rate=("class", lambda s: np.mean(s == "B_shared_only")),
        class_C_rate=("class", lambda s: np.mean(s == "C_orientation_only")),
        class_D_rate=("class", lambda s: np.mean(s == "D_null")),
        mean_z_shared=("z_shared", "mean"),
        mean_z_orient=("z_orient", "mean"),
    ).reset_index()

    summary_path = output_dir / "taucore_v11_overall_summary.csv"
    summary.to_csv(summary_path, index=False)

    return audit_path, summary_path

if __name__ == "__main__":
    run_classifier(
        v8_csv="../results/tables/taucore_v8_stability_audit.csv",
        v10_csv="../results/tables/taucore_v10_orientation_audit.csv",
        output_dir="../results/tables/",
    )
