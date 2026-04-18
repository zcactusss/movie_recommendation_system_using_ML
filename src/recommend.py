import pickle
import os

# -------- PATH FIX --------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

similarity_path = os.path.join(BASE_DIR, 'model', 'similarity.pkl')
matrix_path = os.path.join(BASE_DIR, 'model', 'movie_user_matrix.pkl')

# -------- LOAD FILES --------
similarity = pickle.load(open(similarity_path, 'rb'))
movie_user_matrix = pickle.load(open(matrix_path, 'rb'))

# -------- RECOMMEND FUNCTION --------
def recommend(movie):
    movie = movie.lower()

    # partial match search
    matches = [m for m in movie_user_matrix.index if movie in m.lower()]

    if not matches:
        return ["Movie not found"]

    # pick first match
    selected_movie = matches[0]
    index = movie_user_matrix.index.get_loc(selected_movie)

    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movie_user_matrix.index[i[0]])

    return recommended


# -------- TEST RUN --------
print("✅ Model loaded successfully!")

movie_name = input("Enter movie name: ")
print("Recommended movies:")
print(recommend(movie_name))
