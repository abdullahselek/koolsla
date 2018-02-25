#!/usr/bin/env python

import unittest
from koolsla import data

class DataTest(unittest.TestCase):

    def test_import_data(self):
        dish_dataset = data.import_data(data.dish_dataset_path)
        self.assertEqual(len(dish_dataset), 424509)

    def test_split_data(self):
        dish_dataset = data.import_data(data.dish_dataset_path)
        split_data = data.split_data(dish_dataset)
        self.assertIsNotNone(split_data)

    def test_validate_dish_id(self):
        self.assertFalse(data.validate_dish_id(-1))
        self.assertFalse(data.validate_dish_id(424509))
        self.assertTrue(data.validate_dish_id(100))

    def test_validate_max_recommendation(self):
        self.assertFalse(data.validate_max_recommendation(0))
        self.assertFalse(data.validate_max_recommendation(31))
        self.assertTrue(data.validate_max_recommendation(10))
