
import matplotlib.pyplot as plt
import numpy as np


def plot_mnm_distribution():
    counts = {
        "Red": 4,
        "Orange": 13,
        "Yellow": 18,
        "Blue": 17,
        "Green": 17,
        "Brown": 10,
    }
    total_count = 79

    if sum(counts.values()) != total_count:
        raise ValueError("Counts do not sum to the stated total of 79 M&Ms.")

    colors = list(counts.keys())
    values = np.array([counts[color] for color in colors], dtype=float)
    proportions = values / total_count

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        colors,
        values,
        color=["#C00000", "#FF7F00", "#FFD700", "#1F77B4", "#228B22", "#8B4513"],
    )

    for bar, percentage in zip(bars, proportions):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f"{percentage*100:.1f}%",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    ax.set_ylabel("Count")
    ax.set_title("Distribution of M&M Colors (n = 79)")
    ax.set_ylim(0, values.max() + 5)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

    print("Probability of drawing a non-brown M&M:", 1 - counts["Brown"] / total_count)


if __name__ == "__main__":
    plot_mnm_distribution()
