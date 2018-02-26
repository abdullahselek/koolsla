#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def train_engine(plots):
    """Train engine from dish names.
    Args:
      plots (array): List of dish names.
    Returns:
      tfidf_matrix (sparse matrix, [n_samples, n_features]): Tf-idf-weighted document-term matrix..
    """

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
    """Use to find similarities.
    Args:
      tfidf_matrix (sparse matrix, [n_samples, n_features]): Tf-idf-weighted document-term matrix..
      index (int): Dish id from dataset.
      top_n (int): Max recommendation count, max value 30.
    Returns:
      indice, similarity value (dictionary): Indice, similarity value.
    """

    # Find cosine similarities
    cosine_similarities = linear_kernel(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
    # Prepare related indices
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    # Return dish indices and similarity values
    return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]
