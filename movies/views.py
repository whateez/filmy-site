from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import movie

# Create your views here.
def movie_list(request):
    movies_list = movie.objects.all()
    context = {'movies_list' : movies_list,
        #'page_request_var' : page_request_var,
        #'movies_list' : movies_list
    }
    return render(request, 'movies/movies_list.html', context)


def movie_detail(request, id):
    movie_item = get_object_or_404(movie, id=id)
    context = {'movie_item' : movie_item,
        #'page_request_var' : page_request_var,
        #'movies_list' : movies_list
    }
    return render(request, 'movies/movie_detail.html', context)

# def movie_list_by_lang(request):
#     movie_list = movie.objects.all(lang ='English')
