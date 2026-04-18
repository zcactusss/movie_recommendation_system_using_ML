import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, 'src'))

from recommend import recommend

print("🎬 Movie Recommender")

while True:
    movie = input("\nEnter movie name (or 'exit'): ")

    if movie.lower() == 'exit':
        break

    results = recommend(movie)

    print("\nRecommended Movies:")
    for r in results:
        print("-", r)
