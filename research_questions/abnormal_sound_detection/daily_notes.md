# 5-11-2025
Research the concept of unsupervised learning, read online papers:

1. https://arxiv.org/pdf/1810.09133
2. https://arxiv.org/pdf/2310.08950
3. https://arxiv.org/pdf/2011.02949
4. https://arxiv.org/pdf/2410.08919

Browsed through existing notebooks to learn the preprocessing and general pipeline to get more familiair with the technical side.

# 19-11-2025

Made two cnn-pipelines to preprocess the data and train a model to detect anomalies. One using log-mel spectrograms and one using stft spectrograms.

### conclusions
1. The `Log-mel based` autoencoder learns the general structure of the fan sounds but does not produce higher reconstruction errors for anomalous recordings. Because the difference in error is very small, the model cannot reliably distinguish normal sounds from anomalous ones using Mel-spectrogram patches alone.
2. The `STFT-based autoencoder` learns to reproduce normal sounds but does not produce noticeably higher errors for anomalous ones. The similarity between normal and anomaly errors shows that, in this setup, the STFT representation does not make the anomalies easier to detect. Just like the Mel experiment, this model cannot reliably separate normal and anomalous fan recordings based on reconstruction error alone.

# 24-11-2025
added the test plot to visualise original, reconstructed and error map. Tested with out of domain sounds and normal/ abnormal sounds.

Model does recognize abnormal sounds, but in a subtle way. Not as promiment as i'd like to. Going to test different models and preprocessing/ spectrogram inputs.

# 26-11-2025

Worked on the IDC-TransAE notebook. Added full documentation and markdown explanations for every major step, from dataset loading to training and evaluation. Tested the model on normal, anomalous, and out-of-domain sounds (e.g., elephant audio) using full reconstruction plots and audio playback. Analyzed reconstruction behavior, anomaly score curves, and error maps. Concluded that IDC-TransAE strongly detects out-of-domain audio but struggles to separate normal fan recordings from anomalous ones due to overlapping reconstruction errors. Prepared the notebook for multi–machine-type training and created a prompt for refactoring the code into a unified pipeline that trains all machine types in one run.