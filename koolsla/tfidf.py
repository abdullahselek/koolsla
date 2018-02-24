#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def train_engine(plots):
    # Initializing tf-idf vectorizer
    vectorizer = TfidfVectorizer(
                    analyzer='word',
                    lowercase=True,
                    min_df=3,
                    max_df=0.9,
                    ngram_range=(1, 2),
                    stop_words='english')
    # Fit and transform corpus
    tfidf_matrix = vectorizer.fit_transform(plots)
    # Pack and return the results
    return tfidf_matrix

def find_similarities(tfidf_matrix, index, top_n=5):
    cosine_similarities = linear_kernel(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]
