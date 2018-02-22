#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas

from os.path import join, dirname

# Parent directory
parent_directory_path = dirname(__file__)
# Path to dish dataset
dish_dataset_path = join(parent_directory_path,
                          'dataset/dish.csv')

def import_data(dataset_path):
    dish_dataset = pandas.read_csv(dataset_path)
    return dish_dataset

def split_data(dish_dataset):
    # Get dish names
    dish_names = dish_dataset[['name']].values.flatten().tolist()
    # Pack and return the split data
    return {'dish_names': dish_names}
