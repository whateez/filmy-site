from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import movie, movie_artist, genre
from reviews.models import review

# Create your views here.
def movie_list(request):
    movies_list = movie.objects.all()
    context = {'movies_list' : movies_list,
        #'page_request_var' : page_request_var,
        #'movies_list' : movies_list
    }
    return render(request, 'movies/movies_list.html', context)


def movie_detail(request, slug):
    movie_item = get_object_or_404(movie, slug=slug)
    cast = movie_item.movie_artist_set.all
    genres = movie_item.movie_genre_set.all
    reviews = movie_item.review_set.all
    context = {'movie_item' : movie_item,
        'cast': cast,
        'genres':genres,
        'reviews': reviews,
    }
    return render(request, 'movies/movie_detail.html', context)

# def movie_list_by_lang(request):
#     movie_list = movie.objects.all(lang ='English')
