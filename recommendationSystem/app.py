from flask import Flask, request, jsonify
from fuzzywuzzy import fuzz
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
content_rec = joblib.load("./models/content_rec.pkl")
content_based_model = joblib.load('./models/content_based_model.pkl')
tfidf_matrix = joblib.load('./models/tfidf_matrix.pkl')
movies = pd.read_csv('./cleaned_datasets/movies.dat', 
                 delimiter='::', 
                 encoding = 'latin1',
                 header = None,
                 engine = 'python',
                 names = ['movie_id', 'title', 'genres']
                 )

@app.route('/')
def home():
    return "Machine Learning Model API"

@app.route('/predict', methods=['GET'])
def predict():
    data = request.get_json(force=True)
    prediction = get_content_based_recs(data["input"][0], num_recommendations = 5)
    return jsonify({'prediction': prediction})

"""
calculate the Levenshtein distance to find closest title
if a and b are exactly same, score will be 100
"""
def matching_score(a, b):
    return fuzz.ratio(a, b) 
    
def find_closest_title(title):
    leven_scores = list(enumerate(content_rec['title'].apply(lambda x: fuzz.ratio(a, title))))
    sorted_lev_scores = sorted(leven_scores, key = lambda x: x[1], reverse = True)

    closest_idx = sorted_lev_scores[0][0]
    closest_movie = content_rec.loc[closest_idx]
    distance_score = sorted_lev_scores[0][1]

    closest_movie_id = closest_movie['movie_id']
    closest_movie_title = closest_movie['title']
        
    return (closest_movie_id, closest_movie_title, distance_score)

def get_movie_from_idx(idx):
    # get movie details from idx
    title = content_rec.loc[idx, 'title']
    year = content_rec.loc[idx, 'year']
    return title, year
    
def get_idx_from_title(title):
    # convert title to idx
    return content_rec[content_rec['title'] == title].index.values[0]
    
def get_content_based_recs(movie_name, num_recommendations = 5):
    _, closest_name, distance = find_closest_title(movie_name)
    movie_name = closest_name if distance != 100 else movie_name
    movie_idx = get_idx_from_title(movie_name)

    distances_cb, idx_cb = content_based_model.kneighbors(
        tfidf_matrix[movie_idx], 
        n_neighbors = num_recommendations + 1
    )

    cb_recommendations = []
    for i in range(1, len(distances_cb.flatten())):
        movie_id_cb = movies.iloc[idx_cb.flatten()[i]]['title']
        cb_recommendations.append(movie_id_cb)
    
    return cb_recommendations


if __name__ == '__main__':
    app.run(debug=True)