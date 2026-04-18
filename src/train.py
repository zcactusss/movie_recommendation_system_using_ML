import pandas as pd
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity

# --------- PATH FIX (important) ---------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

movies_path = os.path.join(BASE_DIR, 'data', 'movies.csv')
ratings_path = os.path.join(BASE_DIR, 'data', 'ratings.csv')

# --------- LOAD DATA ---------
print("Loading data...")
movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

print("Movies shape:", movies.shape)
print("Ratings shape:", ratings.shape)

# --------- MERGE ---------
data = pd.merge(ratings, movies, on='movieId')
print("Merged data shape:", data.shape)

# --------- MATRIX ---------
movie_user_matrix = data.pivot_table(index='title', columns='userId', values='rating').fillna(0)
print("Matrix created:", movie_user_matrix.shape)

# --------- SIMILARITY ---------
similarity = cosine_similarity(movie_user_matrix)
print("Similarity computed!")

# --------- SAVE MODEL ---------
model_path = os.path.join(BASE_DIR, 'model')
os.makedirs(model_path, exist_ok=True)

pickle.dump(similarity, open(os.path.join(model_path, 'similarity.pkl'), 'wb'))
pickle.dump(movie_user_matrix, open(os.path.join(model_path, 'movie_user_matrix.pkl'), 'wb'))

print("✅ Model trained and saved successfully!")
