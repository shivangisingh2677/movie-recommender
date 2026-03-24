import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_name):
    # Load dataset
    df = pd.read_csv("movies.csv")

    # Convert text to numbers
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['genres'])

    # Compute similarity
    similarity = cosine_similarity(count_matrix)

    # Check if movie exists
    if movie_name not in df['title'].values:
        return ["Movie not found"]

    # Get index of movie
    idx = df[df['title'] == movie_name].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[idx]))

    # Sort movies based on similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    # Get movie names
    recommendations = [df.iloc[i[0]].title for i in scores]

    return recommendations
