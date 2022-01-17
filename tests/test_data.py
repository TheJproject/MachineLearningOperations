from tests import _PROJECT_ROOT, _PATH_DATALOADER, _PATH_DATA
import sys
import torch
sys.path.append(f'{_PATH_DATALOADER}')
from mnist_loader import mnist



data_merged, test_merged = mnist(f'{_PATH_DATA}' + '/*')
assert len(data_merged['images']) == 25000 , "Dataset did not have the correct number of samples"
assert len(test_merged['labels']) == 5000  , "Testset did not have the correct number of samples"
for datapoints in data_merged['images']:
    assert datapoints.size() == (1,28,28) , "Datapoints in trainset do not have the right dimensions."
for datapoints in test_merged['images']:
    assert datapoints.size() == (1,28,28) , "Datapoints in testset do not have the right dimensions."


#assert that all labels are represented