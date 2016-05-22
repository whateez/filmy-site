from django.shortcuts import render, get_object_or_404, redirect
from .models import review
from .forms import reviewForm
from movies.models import movie, movie_artist
from django.utils import timezone


# Create your views here.
def reviews_list(request):
    reviews = review.objects.filter(published=True)
    context = {'reviews': reviews}
    return render(request, 'reviews/reviews_list.html', context)

def review_detail(request, pk):
    review_item = get_object_or_404(review, pk=pk)
    #review_movie = movie.objects.get(pk=review_item.movie_id)
    #review_details = movie_artist.objects.filter(movie_id=review_movie.id)
    context = {
        'review': review_item,
    #    'movie': review_movie,
    #    'details': review_details
    }
    return render(request, 'reviews/review_detail.html', context)

def review_new(request):
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.published_date = timezone.now()
            review_item.save()
            return redirect(review_item.get_absolute_url())
    else:
        form = reviewForm()
    context = {'form' : form}
    return render(request, 'reviews/review_edit.html', context)

def review_edit(request, pk):
    review_item = get_object_or_404(review, pk=pk)
    if request.method == "POST":
        form = reviewForm(request.POST, instance=review_item)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.published_date = timezone.now()
            review_item.save()
            return redirect(review_item.get_absolute_url())
    else:
        form = reviewForm(instance=review_item)
    context = {'form' : form}
    return render(request, 'reviews/review_edit.html', context)
