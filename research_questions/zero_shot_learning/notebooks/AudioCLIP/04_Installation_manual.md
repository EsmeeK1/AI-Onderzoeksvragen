# Installation Manual: Running AudioCLIP Zero-Shot Notebook

This guide explains how to set up and run the **AudioCLIP zero-shot learning demo** in this repository.

---

## 1. Prerequisites

- **Python 3.8** is required.
  Download and install Python 3.8.10 from the official website:
  [https://www.python.org/downloads/release/python-3810/](https://www.python.org/downloads/release/python-3810/)

- A working installation of **git** (optional, only needed if you want to explore the original AudioCLIP repo).

---

## 2. Create a Virtual Environment

Navigate to the root of your project and create a virtual environment using Python 3.8:

```bash
# Windows (PowerShell)
py -3.8 -m venv .venv38
.venv38\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip
```

## 3. Install Requirements

Install all required packages using the provided requirements.txt:

```bash
pip install -r research_questions\zero_shot_learning\notebooks\AudioCLIP\requirements.txt
```

This will install PyTorch 1.7.1 (CPU version by default) and all dependencies pinned for compatibility with AudioCLIP.

## Download Required Datasets
ESC-50 Dataset

Download the ESC-50 dataset from GitHub:
https://github.com/karolpiczak/ESC-50

UrbanSound8K Dataset

Download the UrbanSound8K dataset from the official website:
https://urbansounddataset.weebly.com/

After downloading, place both datasets in the following directory:

```bash
data/zero-shot-sound/
    ├── ESC-50-master/
    └── UrbanSound8K/
```

## 5. Notebook Location

The main notebook is located here:

```bash
notebooks/AudioCLIP/demo/04_zero_shot_audio_CLIP.ipynb
```

Open it in Jupyter Notebook or JupyterLab and run the cells step by step.

## 6. Assets (Pretrained Models & Tokenizer)

When running the notebook, make sure an assets/ folder exists under notebooks/AudioCLIP/.
It must contain at least the following two files:

**bpe_simple_vocab_16e6.txt.gz:** https://github.com/AndreyGuzhov/AudioCLIP/releases/download/v0.1/bpe_simple_vocab_16e6.txt.gz

**AudioCLIP-Full-Training.pt:** https://github.com/AndreyGuzhov/AudioCLIP/releases/download/v0.1/AudioCLIP-Full-Training.pt

You can download them manually or use Python to fetch them:

```python
import os, urllib.request

ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

files = [
    ("https://github.com/AndreyGuzhov/AudioCLIP/releases/download/v0.1/bpe_simple_vocab_16e6.txt.gz",
     "bpe_simple_vocab_16e6.txt.gz"),
    ("https://github.com/AndreyGuzhov/AudioCLIP/releases/download/v0.1/AudioCLIP-Full-Training.pt",
     "AudioCLIP-Full-Training.pt"),
]

for url, fname in files:
    path = os.path.join(ASSETS_DIR, fname)
    if not os.path.exists(path):
        print(f"Downloading {fname}...")
        urllib.request.urlretrieve(url, path)
    else:
        print(f"{fname} already exists.")
```

## 7. Folder Structure

After installation, your project should look like this (simplified):

```kotlin
research_questions/
└── zero_shot_learning/
    ├── data/
    │   └── zero-shot-sound/
    │       ├── ESC-50-master/
    │       └── UrbanSound8K/
    └── notebooks/
        └── AudioCLIP/
            ├── assets/
            │   ├── bpe_simple_vocab_16e6.txt.gz
            │   └── AudioCLIP-Full-Training.pt
            ├── demo/
            │   └── 04_zero_shot_audio_CLIP.ipynb
            ├── model/
            ├── utils/
            └── requirements.txt
```

## 8. Further Exploration

This notebook uses a fork of AudioCLIP. If you would like to explore or experiment further, check out the original repository here:
https://github.com/AndreyGuzhov/AudioCLIP

Additional context and usage examples are available in the repository’s own README.md.

