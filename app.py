import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit_lottie import st_lottie

# Load data and similarity matrix
movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')



# Recommendation function
import random

def recommend(movie):
    selected_genre = movies[movies['title'] == movie]['genres'].values[0]
    
    # Find other movies with the same genre
    similar_movies = movies[movies['genres'] == selected_genre]
    
    # Exclude the selected movie itself
    similar_movies = similar_movies[similar_movies['title'] != movie]

    # Pick 5 random movies from the same genre (or fewer if not enough)
    recommendations = similar_movies['title'].sample(n=min(5, len(similar_movies)), random_state=42).tolist()
    
    return recommendations


# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Choose a movie you like:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write('Here are 5 movies you might like:')
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")


def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6;
            font-family: 'Segoe UI', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
set_background()

st.markdown(
    """
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

from streamlit_lottie import st_lottie

# Load lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# You can choose another animation from lottiefiles.com
#permanent_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
film_reel_url = "https://assets7.lottiefiles.com/packages/lf20_1pxqjqps.json"
permanent_animation = load_lottieurl(film_reel_url)
popcorn_url = "https://assets9.lottiefiles.com/packages/lf30_p8f9Tq.json"

# Show it permanently at the top or bottom
st_lottie(permanent_animation, height=300, key="looped_movie", loop=True, speed=1)








st.markdown("---")
st.markdown("<center>Developed by Sayma ❤️</center>", unsafe_allow_html=True)
