#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from sklearn.feature_extraction.text import TfidfVectorizer

def train_engine(plots, min_df=3):
    # Initializing tf-idf vectorizer
    vectorizer = TfidfVectorizer(
        min_df=min_df,
        max_df=0.9,
        ngram_range=(1, 2),
        stop_words='english')
    # Fit and transform corpus
    plots_tfidf = vectorizer.fit_transform(plots)
    # Pack and return the results
    return plots_tfidf
