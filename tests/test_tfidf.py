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
        dish_dataset = data.import_data(data.dish_dataset_path)
        split_data = data.split_data(dish_dataset)
        tfidf_matrix = tfidf.train_engine(split_data['dish_names'])
        self.assertIsNotNone(tfidf_matrix)

    def test_find_similarities(self):
        dish_dataset = data.import_data(data.dish_dataset_path)
        split_data = data.split_data(dish_dataset)
        tfidf_matrix = tfidf.train_engine(split_data['dish_names'])
        similar_dishes = tfidf.find_similarities(247, 5, tfidf_matrix)
        self.assertIsNotNone(similar_dishes)
