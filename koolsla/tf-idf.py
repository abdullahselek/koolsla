#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

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

def find_similarities(name, recommendations, plots_tfidf):
    # Generate similarities
    similarities = linear_kernel(plots_tfidf, plots_tfidf)
    # Get similarity scores for the food
    scores = list(enumerate(similarities[name]))
    # Sort into descending order the scores
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    # Get the number of the recommendations asked
    food_recommendations = sorted_scores[1:recommendations + 1]
    # Get the indices of the recommendation food
    food_indices = [i[1] for i in food_recommendations]
    return food_indices
