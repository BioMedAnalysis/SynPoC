# GenAI empowers point-of-care MRI: high-fidelity synthetic imaging with multi-site validation
This repo contains the official Pytorch implementation for SynPoC Model.
![alt text](figures/SynPoC_Framework.pdf)

**Environment**
Please prepare an environment with python>=3.8, and then run the command "pip install -r requirements.txt" for the dependencies.

**Data Preparation**
For experiments, prepare the dataset folder as follows.
```
data/
├── dataset_1/
│   ├── train/
│   │   ├── lf_data.npy
│   │   └── hf_data.npy
│   ├── test/
│   │   ├── lf_data.mat
│   │   └── hf_data.mat
│   ├── val/
│   │   ├── lf_data.mat
│   │   └── hf_data.mat

```

Use [converter.py](converter.py) to convert 3D MRI data to 2D slices and save as .npy
