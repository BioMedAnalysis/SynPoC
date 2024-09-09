# GenAI empowers point-of-care MRI: high-fidelity synthetic imaging with multi-site validation
This repo contains the official Pytorch implementation for SynPoC Model.
![alt text](figures/SynPoC_Framework.pdf)

**Environment**  <br />
Please prepare an environment with python>=3.8, and then run the command "pip install -r requirements.txt" for the dependencies.

**Data Preparation**  <br />
For experiments, extract 2D axial slices from 3D MR images, save them as a .npy file and prepare the dataset folder structure as follows.
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

