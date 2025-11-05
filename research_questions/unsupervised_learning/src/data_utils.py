import librosa
import numpy as np
from pathlib import Path

def load_audio(filepath, sr=16000):
    y, sr = librosa.load(filepath, sr=sr)
    return y, sr

def audio_to_logmel(y, sr=16000, n_fft=1024, hop=512, n_mels=128):
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft,
                                       hop_length=hop, n_mels=n_mels)
    return librosa.power_to_db(S, ref=np.max)
