# 04 — Installation manual (NL)
Handleiding om de notebook **`04_zero_shot_audio_CLIP.ipynb`** te draaien.
De notebook regelt zelf de **assets** (BPE vocab + checkpoint); jij hoeft **alleen de datasets** te downloaden en in de juiste map te zetten.

---

## 1 Benodigdheden
- **Python 3.8.10** (aanrader)
- **Virtuele omgeving** voor dit project (bijv. `.venv38`)
- **Git** (optioneel, maar handig)
- Schijfruimte: ca. **6–10 GB** (datasets + env)

### (Optioneel) Virtuele omgeving aanmaken
**Windows (PowerShell):**
```powershell
py -3.8 -m venv .venv38
.\.venv38\Scripts\Activate.ps1
python --version   # verwacht 3.8.x
```

**macOS/Linux (bash/zsh):**
```bash
python3.8 -m venv .venv38
source .venv38/bin/activate
python --version   # verwacht 3.8.x
```

---

## 2 Datasets downloaden (alleen dit handmatig doen)

| **ESC-50** | https://github.com/karolpiczak/ESC-50 | ZIP of repo → uitgepakt | `data/zero-shot-sound/ESC-50-master` |
| **UrbanSound8K** | https://zenodo.org/records/1203745 | `UrbanSound8K.zip` | `data/zero-shot-sound/UrbanSound8K` |

### Verwachte mappenstructuur
```
data/
└─ zero-shot-sound/
   ├─ ESC-50-master/
   │  ├─ audio/
   │  └─ meta/esc50.csv
   └─ UrbanSound8K/
      ├─ audio/fold1 ... fold10
      └─ metadata/UrbanSound8K.csv
```

> Let op hoofd-/kleine letters zoals hierboven.

---

## 3 Requirements installeren

Installeer vervolgens alle requirements met de requirements.txt die in deze folder staat.
```bash
pip install -r requirements.txt # Zorg dat je in de juiste map zit
```

> Op sommige systemen kan `librosa` een extra backend nodig hebben — `soundfile` is daarom expliciet toegevoegd.

---

## 4) Imports in de notebook

De notebook gebruikt o.a. deze imports (ter referentie of copy/paste in een cel):

```python
import os
import sys
import glob

import librosa
import librosa.display

import simplejpeg
import numpy as np

import torch
import torchvision as tv

import matplotlib.pyplot as plt

from PIL import Image
from IPython.display import Audio, display

sys.path.append(os.path.abspath(f'{os.getcwd()}/..'))

from model import AudioCLIP
from utils.transforms import ToTensor1D


torch.set_grad_enabled(False)

MODEL_FILENAME = 'AudioCLIP-Full-Training.pt'
# derived from ESResNeXt
SAMPLE_RATE = 44100
# derived from CLIP
IMAGE_SIZE = 224
IMAGE_MEAN = 0.48145466, 0.4578275, 0.40821073
IMAGE_STD = 0.26862954, 0.26130258, 0.27577711

LABELS = ['cat', 'thunderstorm', 'coughing', 'alarm clock', 'car horn']
```

> De notebook installeert/plaatst zelf de assets in de map `assets/` en gebruikt `MODEL_FILENAME` wanneer nodig.

---

## 5) Notebook starten

Start Jupyter (of open in VS Code):

```bash
jupyter notebook
# of
jupyter lab
```

Open **`04_zero_shot_audio_CLIP.ipynb`** en voer de cellen van boven naar beneden uit.

---

## 6) Snelle sanity check
- Bestaan de mappen `data/zero-shot-sound/ESC-50-master` en `data/zero-shot-sound/UrbanSound8K` met de **exacte** structuur hierboven?
- Is de venv actief en zijn de requirements zonder errors geïnstalleerd?
- Kun je in een notebookcel draaien:
  ```python
  import torch, torchvision, librosa
  print(torch.__version__, torchvision.__version__, librosa.__version__)
  ```

---

## 7) Veelvoorkomende issues
- **Dataset niet gevonden**: pad of mapnaam verschilt; check de structuur in §2.
- **Librosa/soundfile errors**: zorg dat `soundfile` is geïnstalleerd (zit in requirements).
- **GPU/Torch mismatch**: deze workflow vereist geen GPU; de standaard `torch`-wiel volstaat. Wil je GPU, installeer een CUDA-build die bij je systeem past.

credits naar https://github.com/AndreyGuzhov/AudioCLIP/tree/master?tab=readme-ov-file#audioclip toevoegen
