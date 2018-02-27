#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas
import csv, os

from os.path import join, dirname
from .color_print import print_red

# Parent directory
parent_directory_path = dirname(__file__)
# Path to dish dataset
dish_dataset_path = join(parent_directory_path,
                          'dataset/dish.csv')

def import_data(dataset_path=dish_dataset_path):
    """Imports dataset.
    Args:
      dataset_path (str): Path of dataset file.
    Returns:
      dataset (dataset values): Datas loaded from csv file.
    """

    dish_dataset = pandas.read_csv(dataset_path)
    return dish_dataset

def split_data(dish_dataset):
    """Splits dataset.
    Args:
      dish_dataset (dataset values): Dataset.
    Returns:
      names (dictionary): Dish names in a dictionary.
    """

    # Get dish names
    dish_names = dish_dataset[['name']].values.flatten().tolist()
    # Pack and return the split data
    return {'names': dish_names}

def validate_dish_id(dish_id):
    """Validates dish id.
    Args:
      dish_id (int): Path of dataset file.
    Returns:
      is_valid (bool): True / False.
    """

    # Check whether the id is valid
    if not (isinstance(dish_id, int) and dish_id >= 0 and dish_id <= 424508):
        print_red('Input is not a valid integer between [0, 424508]')
        return False
    return True

def validate_max_recommendation(recommendation_count):
    """Validates dish id.
    Args:
      recommendation_count (int): Max recommendation count given by user.
    Returns:
      is_valid (bool): True / False.
    """

    # Check whether the recommendations count is valid
    if not (isinstance(recommendation_count, int)
            and recommendation_count >= 1 and recommendation_count <= 30):
        print_red('Invalid value for recommendations number: "' +
                 str(recommendation_count) + '"')
        print_red('Input is not a valid integer between [1, 30]')
        return False
    return True
