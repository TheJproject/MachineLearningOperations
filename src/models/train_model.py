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
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    print("Training day and night")
    #parser = argparse.ArgumentParser(description='Training arguments')
    #parser.add_argument('--lr', default=0.1)
    # add any additional argument that you want
    #args = parser.parse_args(sys.argv[2:])
    #print(args)
    
    #path
    data_folder = str(Path().resolve())
    input_path = data_folder + '/' + input_filepath + '/processed'
    # TODO: Implement training loop here
    model = MyAwesomeModel()
    print(input_path)
    train_set = torch.load(input_path)
    train_images = train_set['images']
    train_labels = train_set['labels']
    print(train_images.size())
    print(train_labels.size())
    print(type(train_images))
    train_data = []
    for i in range(len(train_images)):
        train_data.append([train_images[i], train_labels[i]])
    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.003)


    epochs = 30

    for e in range(epochs):
        running_loss = 0
        for images, labels in trainloader:
            optimizer.zero_grad()
            
            log_ps = model(images.float())
            loss = criterion(log_ps, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()            
        else:
            ## TODO: Implement the validation pass and print out the validation accuracy
            print(f"Training loss: {running_loss/len(trainloader)}") 
    print(model)
    torch.save(model.state_dict(), output_filepath + '/my_trained_model.pth')  


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # not used in this stub but often useful for finding various files


    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
