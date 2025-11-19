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
