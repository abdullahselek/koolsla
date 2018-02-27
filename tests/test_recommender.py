#!/usr/bin/env python

import unittest
from koolsla import recommender

class RecommenderTest(unittest.TestCase):

    def test_recommend(self):
        result = recommender.recommend(25, 3)
        self.assertEqual(result, 0)
        result = recommender.recommend(-1, 3)
        self.assertEqual(result, -1)
