import streamlit as st
import pickle
import pandas as pd
import requests


st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

with open("style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🎥 Movie Recommender System")
st.markdown("Get top 5 movie recommendations based on your favorite movie. Powered by NLP & ML! 💡")


# Load files
movies = pickle.load(open('movies.pkl', 'rb'))
import gzip

with gzip.open("similarity.pkl.gz", "rb") as f:
    similarity = pickle.load(f)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# UI
st.title("Movie Recommender System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Top 5 Recommendations:")
    for i in recommendations:
        st.write(i)

import requests

def fetch_poster(movie_title):
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=YOUR_API_KEY&query={movie_title}")
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_posters

if st.button("🎯 Recommend", key="recommend_button"):
    names, posters = recommend(selected_movie)
    st.write("### 🍿 Top 5 Movie Recommendations")
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        with [col1, col2, col3, col4, col5][i]:
            st.image(posters[i])
            st.caption(names[i])
selected_movie = st.selectbox("🎬 Choose a movie to begin:", sorted(movies['title'].values))

st.markdown("---")
st.markdown("Made with ❤️ by Sayma Siddiquie | Powered by Streamlit + Sklearn")






