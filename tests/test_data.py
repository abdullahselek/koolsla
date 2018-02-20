#!/usr/bin/env python

import unittest
from koolsla import data

class DataTest(unittest.TestCase):

    def test_import_data(self):
        food_dataset = data.import_data(data.food_dataset_path)
        self.assertEqual(len(food_dataset), 424509)

    def test_split_data(self):
        food_dataset = data.import_data(data.food_dataset_path)
        split_data = data.split_data(food_dataset)
        self.assertIsNotNone(split_data)
