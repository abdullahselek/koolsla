#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas

from os.path import join, dirname

# Parent directory
parent_directory_path = dirname(__file__)
# Path to food dataset
food_dataset_path = join(parent_directory_path,
                          'dataset/food.csv')

def import_data(dataset_path):
    food_dataset = pandas.read_csv(dataset_path)
    return food_dataset

def split_data(food_dataset):
    # Get food names
    food_names = food_dataset[['name']].values.flatten().tolist()
    # Pack and return the split data
    return {'food_names': food_names}
