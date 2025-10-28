# shared/utils/plots.py
from __future__ import annotations

import os
from typing import Tuple, Dict
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display


def generate_hls_spectrogram(
    audio_path: str,
    filter_mode: str,
    n_fft: int = 2048,
    hop_length: int = 512,
) -> None:
    """
    Genereer en visualiseer een spectrogram voor een HLS-CMDS .wav-bestand.

    Parameters
    ----------
    audio_path : str
        Pad naar het invoer .wav-bestand.
    filter_mode : str
        Stethoscoop-modus voor klinisch relevant frequentiebereik.
        Eén van: {"Bell", "Diaphragm", "Midrange"} (hoofdletter-onafhankelijk).
    n_fft : int, optional
        STFT-venstergrootte (default: 2048). Geschikt voor lage-frequentie signalen.
    hop_length : int, optional
        STFT-hop size (default: 512).

    Gedrag
    ------
    - Vaste sample rate (SR) = 22050 Hz (zoals gespecificeerd).
    - Y-as limiet = 0–600 Hz voor klinisch relevante banden (tot 500 Hz).
    - Omlijnde/shaded band ter accentuering van het klinische bereik per filter_mode.
    - Toont figuur via plt.show().
    """
    # ----------------------------
    # 1) Constantes & validatie
    # ----------------------------
    SR: int = 22050  # vaste sample rate
    FREQ_PLOT_MAX: float = 600.0  # y-as max

    # Klinisch relevante band per modus
    mode_map: Dict[str, Tuple[float, float]] = {
        "BELL": (20.0, 200.0),       # laagfrequent (hart)
        "DIAPHRAGM": (100.0, 500.0), # hoogfrequent (long)
        "MIDRANGE": (50.0, 500.0),   # gemengd
    }

    if not isinstance(filter_mode, str):
        raise TypeError("filter_mode moet een string zijn: 'Bell', 'Diaphragm' of 'Midrange'.")

    mode_key = filter_mode.strip().upper()
    if mode_key not in mode_map:
        raise ValueError("filter_mode ongeldig. Gebruik één van: 'Bell', 'Diaphragm', 'Midrange'.")

    f_min, f_max_mode = mode_map[mode_key]

    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Bestand niet gevonden: {audio_path}")

    if n_fft <= 0 or hop_length <= 0:
        raise ValueError("n_fft en hop_length moeten positieve integers zijn.")

    # ----------------------------
    # 2) Audio laden (mono, vaste SR)
    # ----------------------------
    # NB: HLS-CMDS wavs kunnen in verschillende SR's voorkomen; we resamplen naar 22050 Hz zoals geëist.
    y, sr = librosa.load(audio_path, sr=SR, mono=True)
    if y.size == 0:
        raise ValueError(f"Leeg audiobestand of niet-leesbaar: {audio_path}")

    # ----------------------------
    # 3) STFT + dB-conversie
    # ----------------------------
    # STFT -> magnitude -> dB
    S = librosa.stft(y, n_fft=n_fft, hop_length=hop_length, window="hann", center=True)
    S_mag = np.abs(S)
    S_db = librosa.amplitude_to_db(S_mag, ref=np.max)

    # ----------------------------
    # 4) Visualisatie
    # ----------------------------
    fig, ax = plt.subplots(figsize=(10, 5))

    # Gebruik librosa.display.specshow met frequentiële y-as in Hz
    img = librosa.display.specshow(
        S_db,
        sr=sr,
        hop_length=hop_length,
        x_axis="time",
        y_axis="hz",
        cmap="inferno",        # helder, klinisch prettig
        ax=ax,
    )

    # Beperk focus tot 0–600 Hz (relevant voor HLS-CMDS en paper)
    ax.set_ylim(0, FREQ_PLOT_MAX)

    # Accentueer klinische band van de gekozen modus met een halftransparante overlay
    # en dunne randen, zodat het spectrogram zichtbaar blijft.
    band_low = max(0.0, f_min)
    band_high = min(FREQ_PLOT_MAX, f_max_mode)
    ax.axhspan(band_low, band_high, facecolor="white", alpha=0.10, edgecolor="white", linewidth=0.8)

    # Labels en titel
    filename = os.path.basename(audio_path)
    ax.set_title(f"Spectrogram van {filename} — Modus: {filter_mode}")
    ax.set_xlabel("Tijd (seconden)")
    ax.set_ylabel("Frequentie (Hz)")

    # Kleurenschaal (dB: donker = lage energie, licht = hoge energie)
    cbar = plt.colorbar(img, ax=ax, format="%+0.0f dB")
    cbar.set_label("Energie (dB)")

    # Nuttige grid voor timing
    ax.grid(which="both", axis="x", linestyle=":", linewidth=0.5, alpha=0.4)

    plt.tight_layout()
    plt.show()
