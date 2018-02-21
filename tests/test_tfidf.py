#!/usr/bin/env python

import unittest
from os.path import (
    join, dirname
)
from koolsla import (
    tfidf,
    data
)

class TfIdfTest(unittest.TestCase):

    def test_train_engine(self):
        food_dataset = data.import_data(data.food_dataset_path)
        split_data = data.split_data(food_dataset)
        tfidf_matrix = tfidf.train_engine(split_data['food_names'])
        self.assertIsNotNone(tfidf_matrix)

    def test_find_similarities(self):
        food_dataset = data.import_data(data.food_dataset_path)
        split_data = data.split_data(food_dataset)
        tfidf_matrix = tfidf.train_engine(split_data['food_names'])
        similar_dishes = tfidf.find_similarities(247, 5, tfidf_matrix)
        self.assertIsNotNone(similar_dishes)
