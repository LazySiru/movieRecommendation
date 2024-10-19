from flask import Flask, request, jsonify
import contentBasedModel as CBM

app = Flask(__name__)

import pickle
import pandas as pd

def get_movie_recommendations(user_id, data, k=5):
    # Get all movie IDs
    all_movie_ids = data['movie_id'].unique()
    
    # Get movie IDs that the user has already rated
    user_rated_movies = data[data['user_id'] == user_id]['movie_id'].tolist()
    
    # Predict ratings for all movies that the user hasn't rated
    movie_predictions = []
    with open('./models/svd_model.pkl', 'rb') as f:
        loaded_svd_model = pickle.load(f)

        for movie_id in all_movie_ids:
            if movie_id not in user_rated_movies:
                pred = loaded_svd_model.predict(user_id, movie_id)
                movie_predictions.append((movie_id, pred.est))
    
    # Sort by predicted rating and return top k recommendations
    movie_predictions.sort(key=lambda x: x[1], reverse=True)
    top_k_recommendations = movie_predictions[:k]
    
    return top_k_recommendations

def get_movie_recs_knn(user_id, data, k = 5):
    # Get all movie IDs
    all_movie_ids = data['movie_id'].unique()
    
    # Get movie IDs that the user has already rated
    user_rated_movies = data[data['user_id'] == user_id]['movie_id'].tolist()
    
    # Predict ratings for all movies that the user hasn't rated
    with open('./models/knn_clf.pkl', 'rb') as f:
        knn_clf = pickle.load(f)

        movie_predictions = []
        for movie_id in all_movie_ids:
            if movie_id not in user_rated_movies:
                pred = knn_clf.predict(user_id, movie_id)
                movie_predictions.append((movie_id, pred.est))
        
        # Sort by predicted rating and return top k recommendations
        movie_predictions.sort(key=lambda x: x[1], reverse=True)
        top_k_recommendations = movie_predictions[:k]
    
    return top_k_recommendations



@app.route('/')
def home():
    return "Machine Learning Model API"

@app.route('/recommend/cb_model', methods=['POST'])
def predict():
    req_data = request.get_json()
    movie_name = req_data['movie_name']

    model = CBM.contentBasedModel(movie_name)
    prediction = model.get_recommendation()

    return jsonify({'prediction': prediction})

@app.route('/recommend/knn_model', methods = ['POST'])
def recommend_knn():
    data = pd.read_csv('./datasets/merged.csv')

    req_data = request.get_json()
    user_id = req_data['user_id']

    res = get_movie_recs_knn(user_id, data)

    # extract list of movie_ids 
    movie_ids = [movie_id for movie_id, _ in res]
    filtered_movies = data[data['movie_id'].isin(movie_ids)]
    return_res = filtered_movies['title'].unique().tolist()

    return jsonify({'recommendations': return_res})

@app.route('/recommend/svd_model', methods = ['POST'])
def recommend_svd():
    data = pd.read_csv('./datasets/merged.csv')

    req_data = request.get_json()
    user_id = req_data['user_id']

    res = get_movie_recommendations(user_id, data)

    # extract list of movie_ids 
    movie_ids = [movie_id for movie_id, _ in res]
    filtered_movies = data[data['movie_id'].isin(movie_ids)]
    return_res = filtered_movies['title'].unique().tolist()
    return jsonify({'recommendations': return_res})


@app.route('/recommend/hybrid_model', methods = ['POST'])
def recommend_hybrid():
    pass


if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000, debug=True)



