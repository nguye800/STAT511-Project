import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def make_qq_plots(df: pd.DataFrame, columns: list[str]) -> list[tuple[str, float]]:
    """
    Build normal QQ-plots for each column in `columns` and return the r^2
    diagnostic from scipy.stats.probplot (1.0 == perfect normal fit).
    """
    fig, axes = plt.subplots(len(columns), 1, figsize=(6, 10), sharex=False)
    if len(columns) == 1:
        axes = [axes]

    diagnostics: list[tuple[str, float]] = []
    for ax, col in zip(axes, columns):
        clean = df[col].dropna()
        (theoretical_q, sample_q), (slope, intercept, r) = stats.probplot(
            clean, dist="norm"
        )
        ax.scatter(
            theoretical_q,
            sample_q,
            s=32,
            facecolor="tab:blue",
            edgecolor="black",
            alpha=0.9,
            label="Sample quantiles",
        )
        line_x = np.array([theoretical_q.min(), theoretical_q.max()])
        line_y = slope * line_x + intercept
        ax.plot(
            line_x,
            line_y,
            color="tab:red",
            linestyle="--",
            linewidth=2,
            label="Reference line",
        )
        ax.set_title(f"{col} normal QQ-plot")
        ax.set_xlabel("Theoretical quantiles")
        ax.set_ylabel("Sample quantiles")
        ax.legend(loc="lower right")
        diagnostics.append((col, r**2))

    plt.tight_layout()
    plt.show()
    return diagnostics


def summarize_normality(
    df: pd.DataFrame, diagnostics: list[tuple[str, float]], cutoff: float = 0.99
):
    print("QQ-plot r^2 diagnostics (closer to 1 => closer to normal):")
    for name, r_squared in diagnostics:
        print(f"  {name}: r^2 = {r_squared:.4f}")

    normal_like = [name for name, r_squared in diagnostics if r_squared >= cutoff]
    if normal_like:
        joined = ", ".join(normal_like)
        print(
            f"Samples that closely follow the normal reference (r^2 >= {cutoff:.2f}): {joined}"
        )
        print("Estimated mean and standard deviation from those samples:")
        for name in normal_like:
            clean = df[name].dropna()
            mean = clean.mean()
            std = clean.std(ddof=1)
            print(f"  {name}: mean = {mean:.4f}, std = {std:.4f}")
    else:
        print(
            f"No sample achieved r^2 >= {cutoff:.2f}; visual inspection of the QQ-plots is recommended."
        )
        print(
            "Without identifying a normal-looking sample, we cannot reliably report its mean and standard deviation."
        )


if __name__ == "__main__":
    df_data = pd.read_excel("data.xlsx")
    sample_columns = [col for col in df_data.columns if col.lower().startswith("sample")]
    if not sample_columns:
        raise ValueError("No columns that start with 'Sample' were found in data.xlsx")

    qq_diagnostics = make_qq_plots(df_data, sample_columns)
    summarize_normality(df_data, qq_diagnostics)
