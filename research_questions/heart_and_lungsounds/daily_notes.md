## 13-11-2025
Performed sanity checks on the ICBHI, KA and HLS-CMDS datasets, links:

**ICBHI 2017 Respiratory Sound Database**
- Dataset: https://www.kaggle.com/datasets/vbookshelf/respiratory-sound-database
- Paper: https://pubmed.ncbi.nlm.nih.gov/30708353/

**King Abdullah Dataset (KA Dataset)**
- Dataset: https://data.mendeley.com/datasets/jwyy9np4gv/3
- aper: https://doi.org/10.1016/j.bbe.2020.11.003

**Pulmanory (Lungs) Sounds (ALDS-NET Dataset)**
- Dataset: [Pulmonary (Lungs) Sound - Mendeley Data](https://data.mendeley.com/datasets/jwyy9np4gv/3)
- Paper: https://doi.org/10.1007/s00521-021-06302-1

**Heart and Lung Sounds (HLS-CMDS Dataset)**
- Dataset: [HLS-CMDS: Heart and Lung Sounds Dataset Recorded from a Clinical Manikin using Digital Stethoscope - Mendeley Data](https://data.mendeley.com/datasets/8972jxbpmp/3)
- Paper: https://doi.org/10.1109/IEEEDATA.2025.3566012

Structure of the ALDS-NET dataset is messy, hence why i haven't touched it yet.

**Notes:** ICBHI and KA-Dataset are clean and no issues were found. `HLS-CMDS` had some labelling issues where there was a mismatch in the .csv and the audio-file name, resolved and saved. RC was mislabbeled as LC on row 25.

## 17-11-2025
Made an EDA-Report for the same 3 datasets. Looked into medical terms such as recording locations, soundtypes, missing values, waveform plots, playback etc.

## 3-12-2025
Validaded the counts in the ICBHI, KA and HLS-CMDS dataset.