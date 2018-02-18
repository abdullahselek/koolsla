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
        self.assertEqual(len(food_dataset), 424509)
