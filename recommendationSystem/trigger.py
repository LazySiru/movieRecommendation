import joblib
import pandas as pd

class trigger:
    def __init__(self):
        self.content_rec = joblib.load("./models/content_rec.pkl")
        self.content_based_model = joblib.load('./models/content_based_model.pkl')
        self.tfidf_matrix = joblib.load('./models/tfidf_matrix.pkl')
        self.movies = pd.read_csv(
            './datasets/movie_lens-1M/movies.dat', 
            delimiter='::', 
            encoding = 'latin1',
            header = None,
            engine = 'python',
            names = ['movie_id', 'title', 'genres']
        )
