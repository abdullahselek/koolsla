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
        tfidf_matrix = tfidf.train_engine(split_data['names'])
        self.assertIsNotNone(tfidf_matrix)

    def test_find_similarities(self):
        dish_dataset = data.import_data(data.dish_dataset_path)
        split_data = data.split_data(dish_dataset)
        tfidf_matrix = tfidf.train_engine(split_data['names'])
        similar_dishes = tfidf.find_similarities(tfidf_matrix, 25, 5)
        self.assertIsNotNone(similar_dishes)
