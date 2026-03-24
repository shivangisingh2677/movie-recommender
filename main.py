#main.py code 
from recommender import recommend

print("🎬 Movie Recommendation System")

movie = input("Enter a movie name: ")

results = recommend(movie)

print("\nRecommended Movies:")
for r in results:
    print("-", r)

