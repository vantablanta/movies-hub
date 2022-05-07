from flask import render_template,request,redirect,url_for
from app import app
from .forms import ReviewForm
from .models import reviews
from .request import get_movie, get_movies, search_movie

Review = reviews.Review

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
    reviews = Review.get_reviews(movie.id)
    if search_movie:
        return redirect(url_for('search',movie_name = search_movie))
    else:
        return render_template('movie.html',movie = movie, reviews = reviews)

@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    return render_template('search.html',movies = searched_movies)


@app.route('/reviews')
def reviews():
    form = ReviewForm()
    return render_template('review.html', form = form)


@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_reviews(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        print(new_review)
        return redirect(url_for('movie', id = movie.id ))
    title = f'{movie.title} review'
    return render_template('review.html',title = title, form=form, movie=movie)