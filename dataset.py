import scipy
import torch.utils.data
import numpy as np
import random




def CreateDatasetSynthesis(phase, input_path):

    input_path = '/data/shew0029/MedSyn/DATA/clinical_lf/'
    phase = 'train'
    # Load data for contrast1
    target_file = input_path + phase + "/LF_T2.npy"
    data_fs_s1 = LoadDataSet(target_file)

    # Load data for contrast2
    target_file = input_path + phase + "/HF_T2.npy"
    data_fs_s2 = LoadDataSet(target_file)


    # Initialize lists to store concatenated slices
    concatenated_data1 = []


    num_images = data_fs_s1.shape[0] // 100


    # Iterate over each image
    for image_idx in range(num_images):
        start_idx = image_idx * 100
        end_idx = (image_idx + 1) * 100

        # Extract slices for contrast1
        image_slices1 = data_fs_s1[start_idx:end_idx]


        # Extract adjacent slices within the same image for contrast1
        image_slices1_prev = np.roll(image_slices1, 1, axis=0)  # Shift slices one position forward
        image_slices1_next = np.roll(image_slices1, -1, axis=0)  # Shift slices one position backward

        # Handle first and last slices within the image
        image_slices1_prev[0] = image_slices1[0]  # Repeat first slice for "previous" slice
        image_slices1_next[-1] = image_slices1[-1]  # Repeat last slice for "next" slice


        # Concatenate adjacent slices along the channel dimension
        concatenated_slices1 = np.concatenate((image_slices1_prev, image_slices1, image_slices1_next), axis=1)

        # Append concatenated slices to the list
        concatenated_data1.append(concatenated_slices1)


    input_data1 = np.concatenate(concatenated_data1,  axis=0)

    dataset = torch.utils.data.TensorDataset(  torch.from_numpy(input_data1), torch.from_numpy(data_fs_s2)  )

    return dataset


def LoadDataSet(load_dir, variable='slices', padding=True, Norm=True):

    # Load the Numpy array
    data=np.load(load_dir)

    # Transpose and expand dimensions if necessary
    if data.ndim == 3:
        data = np.expand_dims(np.transpose(data, (0, 2, 1)), axis=1)
    else:
        data = np.transpose(data, (1, 0, 3, 2))

    data = data.astype(np.float32)

    if padding:
        pad_x = int((256 - data.shape[2]) / 2)
        pad_y = int((256 - data.shape[3]) / 2)
        print('padding in x-y with:' + str(pad_x) + '-' + str(pad_y))
        data = np.pad(data, ((0, 0), (0, 0), (pad_x, pad_x), (pad_y, pad_y)))

    if Norm:
        data = (data - 0.5) / 0.5

    return data