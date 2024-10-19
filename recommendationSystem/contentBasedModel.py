from flask import Flask, request, jsonify
from fuzzywuzzy import fuzz
import joblib
import numpy as np
import pandas as pd
import trigger 

data = trigger.trigger()

movies = data.movies
content_rec = data.content_rec
tfidf_matrix = data.tfidf_matrix
content_based_model = data.content_based_model

class contentBasedModel():
    def __init__(self, movie_name, num_recommendations = 5):
        self.movie_name = movie_name
        self.num_recommendations = num_recommendations

    """
    calculate the Levenshtein distance to find closest title
    if a and b are exactly same, score will be 100
    """
    def find_closest_title(self, title):
        leven_scores = list(enumerate(content_rec['title'].apply(lambda x: fuzz.ratio(x, title))))
        sorted_lev_scores = sorted(leven_scores, key = lambda x: x[1], reverse = True)

        closest_idx = sorted_lev_scores[0][0]
        closest_movie = content_rec.loc[closest_idx]
        distance_score = sorted_lev_scores[0][1]

        closest_movie_id = closest_movie['movie_id']
        closest_movie_title = closest_movie['title']
            
        return (closest_movie_id, closest_movie_title, distance_score)

    def get_movie_from_idx(self, idx):
        # get movie details from idx
        title = content_rec.loc[idx, 'title']
        year = content_rec.loc[idx, 'year']
        return title, year
        
    def get_idx_from_title(self, title):
        # convert title to idx
        return content_rec[content_rec['title'] == title].index.values[0]
        
    def get_content_based_recs(self, movie_name, num_recommendations = 5):
        _, closest_name, distance = self.find_closest_title(movie_name)
        movie_name = closest_name if distance != 100 else movie_name
        movie_idx = self.get_idx_from_title(movie_name)

        distances_cb, idx_cb = content_based_model.kneighbors(
            tfidf_matrix[movie_idx], 
            n_neighbors = num_recommendations + 1
        )

        cb_recommendations = []
        for i in range(0, len(distances_cb.flatten())):
            movie_id_cb = movies.iloc[idx_cb.flatten()[i]]['title']
            cb_recommendations.append(movie_id_cb)
        
        return cb_recommendations
    
    def get_recommendation(self):
        return self.get_content_based_recs(self.movie_name, self.num_recommendations)
