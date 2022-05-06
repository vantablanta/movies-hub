from app import app
import requests
from .models import movie

Movie = movie.Movie

api_key  = app.config['API_KEY']
base_url = app.config["BASE_URL"]

def get_movies(category):
    """API request"""
    movie_url = base_url.format(category, api_key)

    response = requests.get(movie_url).json()

    movie_list = []
    for item in response['results']:
        id = item['id']
        title = item['title']
        overview = item['overview']
        poster = item['poster_path']
        vote_average = item['vote_average']
        vote_count = item['vote_count']

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_list.append(movie_object)

    return movie_list

def get_movie(id):
    movie_detail_url = base_url.format(id, api_key)

    response = requests.get(movie_detail_url).json()

    movie_object = None

    if response: 
        id  = response['id']
        title  = response['title']
        overview  = response['overview']
        poster  = response['poster_path']
        vote_average = response['vote_average'] 
        vote_count = response['vote_count']

        movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object




