import matplotlib.pyplot as plt


def set_default_style():
    """
    Shared matplotlib style for all EDA notebooks.
    """
    plt.rcParams.update(
        {
            "figure.figsize": (6, 4),
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "savefig.dpi": 200,
        }
    )


def save_and_close(fig, path=None):
    """
    Optional helper if you want consistent saving.
    """
    fig.tight_layout()
    if path is not None:
        fig.savefig(path)
    plt.close(fig)
