from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
FIG = ROOT / "figures"
PAPER_FIG = ROOT / "paper17_submission_source" / "figures"


def save(fig: plt.Figure, name: str) -> None:
    for out_dir in (FIG, PAPER_FIG):
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / name, bbox_inches="tight")
    plt.close(fig)


def build_protocol_figure() -> None:
    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.set_axis_off()

    boxes = [
        (0.07, 0.64, 0.22, 0.18, "Hidden parent\nsynthetic field"),
        (0.39, 0.74, 0.22, 0.14, "Lensing-like\nreadout"),
        (0.39, 0.53, 0.22, 0.14, "Morphology /\nfilament readout"),
        (0.70, 0.74, 0.22, 0.14, "$Z_{shared}$\nco-variance axis"),
        (0.70, 0.53, 0.22, 0.14, "$Z_{orient}$\norientation axis"),
        (0.37, 0.20, 0.28, 0.16, "Two-axis classifier\nA/B/C/D"),
    ]

    for x, y, w, h, text in boxes:
        ax.add_patch(
            plt.Rectangle((x, y), w, h, fc="#eef3fb", ec="#345995", lw=1.4)
        )
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10)

    arrows = [
        ((0.29, 0.73), (0.39, 0.81)),
        ((0.29, 0.73), (0.39, 0.60)),
        ((0.61, 0.81), (0.70, 0.81)),
        ((0.61, 0.60), (0.70, 0.60)),
        ((0.81, 0.74), (0.55, 0.36)),
        ((0.81, 0.53), (0.55, 0.36)),
    ]
    for start, end in arrows:
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.2),
        )

    ax.text(
        0.50,
        0.07,
        "Evidence rule: shared-parent support is primary; orientation is secondary.",
        ha="center",
        fontsize=10,
        color="#222222",
    )
    save(fig, "fig_readout_covariance_protocol.pdf")


def build_class_rate_figure() -> None:
    rates = pd.read_csv(DERIVED / "taucore_v11_class_rates.csv")
    labels = ["A\nshared+orient", "B\nshared only", "C\norient only", "D\nnull"]
    cols = [
        "A_shared_plus_orientation",
        "B_shared_only",
        "C_orientation_only",
        "D_null",
    ]
    tau = rates[rates["is_tau_world"] == True][cols].iloc[0].to_numpy(float)  # noqa: E712
    null = rates[rates["is_tau_world"] == False][cols].iloc[0].to_numpy(float)  # noqa: E712

    x = np.arange(len(cols))
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.bar(x - 0.18, tau, width=0.36, label="TauWorld", color="#3b78b4")
    ax.bar(x + 0.18, null, width=0.36, label="NullWorld", color="#b45f5f")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("fraction")
    ax.set_ylim(0, 1.05)
    ax.set_title("v11 two-axis classifier class rates")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig_v11_class_rates.pdf")


def build_scatter_figure() -> None:
    audit = pd.read_csv(DERIVED / "taucore_v11_two_axis_classifier_audit.csv")
    fig, ax = plt.subplots(figsize=(8.2, 6.2))
    colors = {
        "A_shared_plus_orientation": "#2374ab",
        "B_shared_only": "#59a14f",
        "C_orientation_only": "#f28e2b",
        "D_null": "#777777",
    }
    for cls, group in audit.groupby("class"):
        ax.scatter(
            group["z_shared"],
            group["z_orient"],
            s=28,
            alpha=0.75,
            label=cls.replace("_", " "),
            color=colors.get(cls, "#444444"),
            edgecolor="none",
        )
    ax.axvline(3.0, color="black", lw=1.0, ls="--")
    ax.axhline(2.0, color="black", lw=1.0, ls="--")
    ax.text(3.05, ax.get_ylim()[0] + 0.3, "$Z_{shared}=3$", fontsize=9)
    ax.text(ax.get_xlim()[0] + 0.2, 2.08, "$Z_{orient}=2$", fontsize=9)
    ax.set_xlabel("$Z_{shared}$")
    ax.set_ylabel("$Z_{orient}$")
    ax.set_title("Shared-parent versus orientation diagnostic plane")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.grid(alpha=0.22)
    save(fig, "fig_v11_shared_orient_scatter.pdf")


def build_condition_heatmap() -> None:
    by_condition = pd.read_csv(DERIVED / "taucore_v11_summary_by_condition.csv")
    tau = by_condition[by_condition["is_tau_world"] == True].copy()  # noqa: E712
    pivot = tau.pivot(index="noise", columns="anisotropy_ratio", values="class_A_rate")
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    im = ax.imshow(pivot.to_numpy(float), origin="lower", cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([str(c) for c in pivot.columns])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels([str(i) for i in pivot.index])
    ax.set_xlabel("anisotropy ratio")
    ax.set_ylabel("noise")
    ax.set_title("TauWorld class-A rate by synthetic condition")
    for i, row in enumerate(pivot.to_numpy(float)):
        for j, val in enumerate(row):
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=9)
    fig.colorbar(im, ax=ax, label="class A fraction")
    save(fig, "fig_tauworld_condition_heatmap.pdf")


def build_threshold_sweep_figure() -> None:
    audit = pd.read_csv(DERIVED / "taucore_v11_two_axis_classifier_audit.csv")
    tau = audit[audit["is_tau_world"] == True]  # noqa: E712
    null = audit[audit["is_tau_world"] == False]  # noqa: E712

    shared_thresholds = np.linspace(
        min(audit["z_shared"].min(), 0.0),
        max(audit["z_shared"].max(), 8.0),
        120,
    )
    orient_thresholds = np.linspace(
        min(audit["z_orient"].min(), 0.0),
        max(audit["z_orient"].max(), 6.0),
        120,
    )

    shared_tau = [(tau["z_shared"] > t).mean() for t in shared_thresholds]
    shared_null = [(null["z_shared"] > t).mean() for t in shared_thresholds]
    orient_tau = [(tau["z_orient"] > t).mean() for t in orient_thresholds]
    orient_null = [(null["z_orient"] > t).mean() for t in orient_thresholds]

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.8))

    ax = axes[0]
    ax.plot(shared_thresholds, shared_tau, label="TauWorld recovery", color="#2374ab", lw=2)
    ax.plot(shared_thresholds, shared_null, label="NullWorld false positive", color="#b45f5f", lw=2)
    ax.axvline(3.0, color="black", lw=1.0, ls="--")
    ax.set_xlabel("$Z_{shared}$ threshold")
    ax.set_ylabel("fraction above threshold")
    ax.set_ylim(-0.03, 1.03)
    ax.set_title("Shared-parent threshold sweep")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(alpha=0.25)

    ax = axes[1]
    ax.plot(orient_thresholds, orient_tau, label="TauWorld orientation rate", color="#59a14f", lw=2)
    ax.plot(orient_thresholds, orient_null, label="NullWorld orientation-only trap", color="#f28e2b", lw=2)
    ax.axvline(2.0, color="black", lw=1.0, ls="--")
    ax.set_xlabel("$Z_{orient}$ threshold")
    ax.set_ylabel("fraction above threshold")
    ax.set_ylim(-0.03, 1.03)
    ax.set_title("Orientation threshold sweep")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(alpha=0.25)

    fig.suptitle("Threshold-sweep view of the v11 classifier", y=1.03)
    save(fig, "fig_v11_threshold_sweep.pdf")


def main() -> None:
    build_protocol_figure()
    build_class_rate_figure()
    build_scatter_figure()
    build_condition_heatmap()
    build_threshold_sweep_figure()
    print("PAPER17_FIGURES_BUILT")


if __name__ == "__main__":
    main()
