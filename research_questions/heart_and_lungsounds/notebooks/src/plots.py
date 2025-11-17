import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import librosa

def histplot(df, column, bins=30, ax=None, title=None):
    ax = ax or plt.gca()
    ax.hist(df[column].dropna(), bins=bins)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    if title:
        ax.set_title(title)
    return ax


def countplot(df, column, ax=None, title=None, order=None, rotate_xticks=True):
    ax = ax or plt.gca()
    vc = df[column].value_counts(dropna=False)
    if order is not None:
        vc = vc.reindex(order)
    vc.plot(kind="bar", ax=ax)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    if title:
        ax.set_title(title)
    if rotate_xticks:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    return ax

def show_waveform(y: np.ndarray, sr: int, title: str = "Waveform"):
    """
    Standalone waveform plot (single figure).
    """
    plt.figure(figsize=(10, 3))
    t = np.arange(len(y)) / sr
    plt.plot(t, y, color="#1f77b4", linewidth=1)
    plt.title(title, fontsize=14, pad=15)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Amplitude", fontsize=12)
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout(pad=2)
    plt.box(False)
    plt.show()


def plot_stft(
    y: np.ndarray,
    sr: int,
    n_fft: int = 1024,
    hop: int = 256,
    title: str = "STFT Spectrogram",
    fmax: float | None = None,
):
    """
    Plot an STFT spectrogram of an audio signal (librosa-based).

    Parameters
    ----------
    y : np.ndarray
        Audio signal (1D).
    sr : int
        Sample rate.
    n_fft : int
        FFT window size.
    hop : int
        Hop length.
    title : str
        Plot title.
    fmax : float or None
        Maximum frequency shown on the y-axis. If None, sr/2 is used.
    """
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop))
    S_db = librosa.amplitude_to_db(S, ref=np.max)

    if fmax is None:
        fmax = sr / 2.0

    plt.figure(figsize=(10, 4))
    img = plt.imshow(
        S_db,
        aspect="auto",
        origin="lower",
        cmap="magma",
        extent=[0, len(y) / sr, 0, sr / 2],  # type: ignore
    )
    plt.colorbar(img, format="%+2.0f dB", label="Amplitude (dB)")
    plt.title(title, fontsize=12)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Frequency (Hz)", fontsize=12)

    # Limit visible frequency range according to fmax
    plt.ylim(0, min(fmax, sr / 2.0))

    plt.tight_layout()
    plt.show()

