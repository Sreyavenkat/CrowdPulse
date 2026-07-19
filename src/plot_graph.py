import matplotlib.pyplot as plt


def plot_excitement_graph(times, rms, peaks):

    fig, ax = plt.subplots(figsize=(14,5))

    # Main graph
    ax.plot(
        times,
        rms,
        color="royalblue",
        linewidth=2,
        label="Crowd Energy"
    )

    # Fill area
    ax.fill_between(
        times,
        rms,
        color="lightskyblue",
        alpha=0.35
    )

    # Peak markers
    ax.scatter(
        times[peaks],
        rms[peaks],
        color="red",
        s=70,
        zorder=5,
        label="Exciting Moment"
    )

    ax.set_title(
        "⚽ Match Excitement Timeline",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Audio Energy")

    ax.grid(alpha=0.3)

    ax.legend()

    plt.tight_layout()

    return fig