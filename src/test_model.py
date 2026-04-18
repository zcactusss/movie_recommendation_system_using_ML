import pickle
import os

# base directory (movie_recommender)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# correct path to model file
file_path = os.path.join(BASE_DIR, 'model', 'similarity.pkl')

# load model
similarity = pickle.load(open(file_path, 'rb'))

print("✅ Model loaded successfully!")
print("Shape:", similarity.shape)
