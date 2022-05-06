from flask import render_template,request,redirect,url_for
from app import app

from.request import get_movie, get_movies, search_movie


@app.route('/')
def popular():
    popular_movies = get_movies('popular')
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('index.html', popular = popular_movies)

@app.route('/showing')
def showing():
    showing_movies = get_movies('now_playing')
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('showing.html', showing = showing_movies)

@app.route('/upcoming')
def upcoming():
    upcoming_movies = get_movies('upcoming')
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('upcoming.html', upcoming = upcoming_movies)
  

@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('movie.html',movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)