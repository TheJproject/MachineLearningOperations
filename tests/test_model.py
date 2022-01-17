from tests import _PATH_MODEL, _PATH_DATALOADER,_PATH_DATA
import sys
import pytest
sys.path.append(f'{_PATH_MODEL}')
from model import MyAwesomeModel
sys.path.append(f'{_PATH_DATALOADER}')
from mnist_loader import mnist
import torch
from torch import nn, optim

model = MyAwesomeModel()

data_merged, test_merged = mnist(f'{_PATH_DATA}' + '/*')
train_images = data_merged['images']
train_labels = data_merged['labels']
x, y = train_images[0], train_labels[0]
predict = model(x.float())

assert predict.size() == (1,10) , "The model does not return the right dimension (should be (1,10))"
