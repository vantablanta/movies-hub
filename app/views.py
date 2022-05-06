from flask import render_template
from app import app

from.request import get_movie, get_movies


@app.route('/')
def popular():
    popular_movies = get_movies('popular')
    return render_template('index.html', popular = popular_movies)

@app.route('/showing')
def showing():
    showing_movies = get_movies('now_playing')
    return render_template('showing.html', showing = showing_movies)

@app.route('/upcoming')
def upcoming():
    upcoming_movies = get_movies('upcoming')
    return render_template('upcoming.html', upcoming = upcoming_movies)

    

@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    return render_template('movie.html',movie = movie)