# -*- coding: utf-8 -*-
import argparse
import sys
from numpy.lib.type_check import imag
from model import MyAwesomeModel
import click
import numpy as np
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import torch
from torch import nn, optim



@click.command()
@click.argument('input1_filepath', type=click.Path(exists=True))
@click.argument('input2_filepath', type=click.Path())



def main(input1_filepath,input2_filepath):
    print("Evaluating until hitting the ceiling")
    state_dict = torch.load(input1_filepath)
    model = MyAwesomeModel()
    model.load_state_dict(state_dict)
    model.eval()
    print(model)

    #evaluate loop
    test_set = torch.load(input2_filepath)
    test_images = torch.tensor(test_set['images']).view(1000,1,28,28)
    test_labels = torch.tensor(test_set['labels'])
    # Get the class probabilities
    ps = torch.exp(model(test_images.float()))
    # Make sure the shape is appropriate, we should get 10 class probabilities for 64 examples
    top_p, top_class = ps.topk(1, dim=1)
    # Look at the most likely classes for the first 10 examples
    equals = top_class == test_labels.view(*top_class.shape)
    accuracy = torch.mean(equals.type(torch.FloatTensor))
    print(f'Accuracy: {accuracy.item()*100}%')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # not used in this stub but often useful for finding various files


    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()