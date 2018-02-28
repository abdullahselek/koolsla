#!/usr/bin/env python

import unittest
from koolsla import recommender

class RecommenderTest(unittest.TestCase):

    def test_recommend(self):
        recommendatons = recommender.recommend(25, 3)
        self.assertIsNotNone(recommendatons)
        recommendatons = recommender.recommend(-1, 3)
        self.assertIsNone(recommendatons)
