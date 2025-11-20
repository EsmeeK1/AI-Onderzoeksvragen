import numpy as np
import pandas as pd
import librosa
import matplotlib.pyplot as plt

from ipywidgets import Dropdown, Checkbox, FloatSlider, VBox, HBox, Layout, Output
from IPython.display import display
from scipy.signal import butter, sosfilt, sosfiltfilt

def make_patient_audio_widget(
    df: pd.DataFrame,
    n_fft: int = 1024,
    hop: int = 256,
    default_band=(50.0, 2000.0),
    dynamic_range_db: float = 60.0,
):
    """
    Interactive widget to:
    - select a patient_id
    - select a recording for that patient
    - show waveform + STFT spectrogram
    - optionally apply a bandpass filter
    - rescale spectrogram colors to the current visible band
    """

    # --- Patient and recording dropdowns ---
    patient_ids = sorted(df["patient_id"].unique())

    patient_dropdown = Dropdown(
        options=patient_ids,
        description="Patient:",
        layout=Layout(width="250px"),
    )

    recording_dropdown = Dropdown(
        options=[],
        description="Recording:",
        layout=Layout(width="600px"),
    )

    def _update_recording_dropdown(pid):
        """Update recording dropdown based on selected patient_id."""
        subset = df[df["patient_id"] == pid]

        options = []
        for idx, row in subset.iterrows():
            # Build a readable label for each recording
            label_parts = [str(row["file_name"])]
            if "chest_location" in df.columns:
                label_parts.append(str(row["chest_location"]))
            if "mode" in df.columns:
                label_parts.append(str(row["mode"]))
            label = " | ".join(label_parts)

            # value = index in df
            options.append((label, idx))

        if not options:
            options = [("No recordings found", None)]

        recording_dropdown.options = options
        recording_dropdown.value = options[0][1]

    # Initialize recordings for the first patient
    _update_recording_dropdown(patient_ids[0])

    # --- Filter controls ---
    nyq_global = float(df["samplerate"].max()) / 2.0
    low_default, high_default = default_band

    apply_filter_cb = Checkbox(
        value=True,
        description="Apply bandpass filter",
        indent=False,
        layout=Layout(width="250px"),
    )

    low_slider = FloatSlider(
        value=min(low_default, nyq_global * 0.4),
        min=10.0,
        max=max(low_default * 2, nyq_global - 20.0),
        step=10.0,
        description="Low cutoff (Hz)",
        continuous_update=False,
        readout_format=".0f",
        layout=Layout(width="400px"),
    )

    high_slider = FloatSlider(
        value=min(high_default, nyq_global - 50.0),
        min=low_slider.value + 10.0,
        max=nyq_global - 1.0,
        step=10.0,
        description="High cutoff (Hz)",
        continuous_update=False,
        readout_format=".0f",
        layout=Layout(width="400px"),
    )

    # Output widget to hold the plots
    plot_out = Output()

    def _plot():
        """Draw waveform and spectrogram for the current widget state."""
        row_idx = recording_dropdown.value
        if row_idx is None:
            with plot_out:
                plot_out.clear_output(wait=True)
                print("No recording selected.")
            return

        row = df.loc[row_idx]

        # 'path' already contains the full path to the .wav file
        full_path = str(row["path"])

        # Load audio file
        y, sr = librosa.load(full_path, sr=None, mono=True)
        nyq_local = sr / 2.0

        # Current filter settings
        apply_filter = apply_filter_cb.value
        low = float(low_slider.value)
        high = float(high_slider.value)

        # Validate and clamp cutoff frequencies according to the actual samplerate
        if low >= high:
            high = low + 1.0
        if high >= nyq_local:
            high = nyq_local - 1.0
        if low <= 0:
            low = 1.0

        # Optionally apply bandpass filter
        if apply_filter:
            y_proc = bandpass_filter(y, fs=sr, fc=(low, high))
            filter_suffix = f"(bandpass: {low:.0f}-{high:.0f} Hz)"
        else:
            y_proc = y
            filter_suffix = "(unfiltered)"

        # Metadata for plot titles
        pid = row["patient_id"]
        diagnosis = row["diagnosis"] if pd.notnull(row["diagnosis"]) else "unknown"
        age = row["age"] if pd.notnull(row["age"]) else "unknown"

        title_prefix = f"Patient ID: {pid}, Diagnosis: {diagnosis}, Age: {age}"

        # --- Compute STFT ---
        S = np.abs(librosa.stft(y_proc, n_fft=n_fft, hop_length=hop))
        S_db = librosa.amplitude_to_db(S, ref=np.max)

        # Frequency vector for STFT rows
        freqs = np.linspace(0.0, nyq_local, S_db.shape[0])

        # Determine visible frequency range (for both y-axis and color scaling)
        if apply_filter:
            f_min_vis, f_max_vis = low, high
        else:
            f_min_vis, f_max_vis = 0.0, nyq_local

        band_mask = (freqs >= f_min_vis) & (freqs <= f_max_vis)
        band_values = S_db[band_mask, :] if band_mask.any() else S_db

        # Dynamic range for better contrast in the visible band
        if np.isfinite(band_values).any():
            local_max = np.max(band_values)
            local_min = np.min(band_values)
            vmin = max(local_max - dynamic_range_db, local_min)
            vmax = local_max
        else:
            vmin, vmax = np.min(S_db), np.max(S_db)

        # --- Plot into the Output widget ---
        with plot_out:
            plot_out.clear_output(wait=True)
            plt.close("all")

            fig, (ax1, ax2) = plt.subplots(
                2, 1, figsize=(10, 6), sharex=True, constrained_layout=True
            )

            # Waveform
            t = np.arange(len(y_proc)) / sr
            ax1.plot(t, y_proc, linewidth=1)
            ax1.set_title(f"{title_prefix}\nWaveform {filter_suffix}")
            ax1.set_ylabel("Amplitude")
            ax1.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

            # STFT with adaptive color scaling
            img = ax2.imshow(
                S_db,
                aspect="auto",
                origin="lower",
                extent=[0, len(y_proc) / sr, 0, nyq_local],
                vmin=vmin,
                vmax=vmax,
            )
            ax2.set_xlabel("Time (s)")
            ax2.set_ylabel("Frequency (Hz)")

            # Sync y-axis with visible band
            if apply_filter:
                ax2.set_ylim(low, high)
                ax2.set_title(
                    f"{title_prefix}\nSTFT spectrogram (zoomed to {low:.0f}-{high:.0f} Hz)"
                )
            else:
                ax2.set_ylim(0, nyq_local)
                ax2.set_title(f"{title_prefix}\nSTFT spectrogram (full range)")

            cbar = fig.colorbar(img, ax=ax2)
            cbar.set_label("Amplitude (dB)")

            plt.show()

    # --- Observers to trigger replot ---
    def _on_patient_change(change):
        if change["name"] == "value" and change["new"] is not None:
            _update_recording_dropdown(change["new"])
            _plot()

    def _on_recording_change(change):
        if change["name"] == "value":
            _plot()

    patient_dropdown.observe(_on_patient_change, names="value")
    recording_dropdown.observe(_on_recording_change, names="value")

    for w in (apply_filter_cb, low_slider, high_slider):
        w.observe(lambda change: _plot(), names="value")

    # Initial plot
    _plot()

    controls_top = HBox([patient_dropdown, recording_dropdown])
    controls_filter = VBox([apply_filter_cb, low_slider, high_slider])

    display(VBox([controls_top, controls_filter, plot_out]))

def bandpass_filter(x: np.ndarray, fs: float, fc=(50.0, 2000.0), order=2, zero_phase=True, axis=-1) -> np.ndarray:
    """
    Apply a Butterworth band-pass filter to an input signal.

    Args:
        x (np.ndarray): Input signal to filter.
        fs (float): Sampling rate in Hz.
        fc (tuple of float): Low and high cutoff frequencies in Hz. Default is (50.0, 2000.0).
        order (int): Filter order. Default is 2.
        zero_phase (bool): If True, use zero-phase filtering (no phase shift). Default is True.
        axis (int): Axis to filter along. Default is -1.

    Returns:
        np.ndarray: The filtered signal, same shape as input.

    Notes:
        - Zero-phase filtering avoids phase distortion but cannot be used in real-time.
        - Frequencies are automatically limited to stay below the Nyquist frequency.
    """
    x = np.asarray(x)

    # Unpack cutoff frequencies
    low, high = float(fc[0]), float(fc[1])
    nyq = fs / 2.0  # Nyquist frequency (half the sample rate)

    # Clamp upper cutoff to stay below Nyquist
    high = min(high, nyq - 1e-6)
    if not (0.0 < low < high < nyq):
        raise ValueError(f"Invalid cutoffs: 0 < {low=} < {high=} < {nyq=}")

    # Normalize to Nyquist
    wn = (low / nyq, high / nyq)

    # Create Butterworth band-pass filter
    sos = butter(int(order), wn, btype='band', output='sos')

    # Apply the filter
    if zero_phase:
        # Use forward-backward filtering (no phase shift)
        return sosfiltfilt(sos, x, axis=axis)
    else:
        # Use one-way causal filtering (adds delay)
        return sosfilt(sos, x, axis=axis) # type: ignore