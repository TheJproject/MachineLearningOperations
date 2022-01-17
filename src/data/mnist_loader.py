import glob
from pathlib import Path

import numpy as np
import torch
from torchvision import transforms


def mnist(input_filepath):
    ''' Takes a given filepath and looks for file starting with train.'''
    file_list = glob.glob(input_filepath + 'train*')
    data_all = [np.load(fname) for fname in file_list]
    data_merged = {}
    for data in data_all:
        data_merged = dict_update_without_overwrite(data_merged,data)
    data_merged['images'] = torch.tensor(np.array(data_merged['images']))
    data_merged['images'] = data_merged['images'].view(25000,1,28,28)
    data_transforms = transforms.Normalize((0), (1))
    data_merged['images'] = data_transforms(data_merged['images'])
    data_merged['labels'] = torch.tensor(np.array(data_merged['labels'])).view(25000)

    test_file_list = glob.glob(input_filepath + 'test.npz')
    test_data_all = [np.load(fname) for fname in test_file_list]
    test_merged ={}
    for data in test_data_all:
        test_merged = dict_update_without_overwrite(test_merged,data)
    test_merged['images'] = torch.tensor(test_merged['images']).view(5000,1,28,28)
    test_merged['images'] = data_transforms(test_merged['images'])
    test_merged['labels'] = torch.tensor(test_merged['labels'])
    return data_merged, test_merged



def dict_update_without_overwrite(dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1:
            if isinstance(dict_1[key], list):
                dict_1[key].append(value)
            else:
                temp_list = [dict_1[key]]
                temp_list.append(value)
                dict_1[key] = temp_list
        else:
            dict_1[key] = value
    return dict_1
