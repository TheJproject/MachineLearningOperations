# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
import numpy as np
import torch
from dotenv import find_dotenv, load_dotenv

from mnist_loader import mnist


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')  
    data_folder = str(Path().resolve())
    input_path = data_folder + '/' + input_filepath + '/*'
    data_cleaned, test_data_cleaned = mnist(input_path)
    output_path = data_folder + '/' + output_filepath + '/processed'
    output_path_test = data_folder + '/' + output_filepath + '/processed_test'
    torch.save(data_cleaned,output_path)
    torch.save(test_data_cleaned,output_path_test)

    #Generate 10 random picture for testing (OR 1000)
    output_path_example = data_folder + '/data/examples/example_images.npy'
    test_examples_10 ={}
    test_examples_10['images'] = test_data_cleaned['images'][:1000]
    #print(test_examples_10['images'].size())
    test_examples_10['labels'] = test_data_cleaned['labels'][:1000]
    torch.save(test_examples_10,output_path_example)

    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # not used in this stub but often useful for finding various files


    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
