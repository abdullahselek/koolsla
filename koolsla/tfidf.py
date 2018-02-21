#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from numpy import argmax

# Initializing tf-idf vectorizer
tdidf = TfidfVectorizer(
            min_df=3,
            max_df=0.9,
            ngram_range=(1, 2),
            stop_words='english')

def train_engine(plots, min_df=3):
    tdidf.min_df = min_df
    # Fit and transform corpus
    tfidf_matrix = tdidf.fit_transform(plots)
    # Pack and return the results
    return tfidf_matrix

def find_similarities(dish_id, recommendation_count, tfidf_matrix):
    # Generate similarities
    cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix).flatten()
    # Find related dishes with recommendation count
    related_dish_indices = cosine_similarities.argsort()[:-recommendation_count:-1]
    return related_dish_indices
