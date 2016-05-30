from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import review
from .forms import reviewForm
from movies.models import movie, movie_artist
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext


# Create your views here.
def review_list(request):
    reviews_list = review.objects.filter(published=True).order_by('-published_date')
    paginator = Paginator(reviews_list, 5) # Show 25 contacts per page
    page_request_var = 'page'

    page = request.GET.get(page_request_var)
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    context = {'reviews' : reviews,
        'page_request_var' : page_request_var
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, slug):
    review_item = get_object_or_404(review, slug=slug)
    #review_movie = movie.objects.get(pk=review_item.movie_id)
    #review_details = movie_artist.objects.filter(movie_id=review_movie.id)
    context = {
        'review': review_item,
    #    'movie': review_movie,
    #    'details': review_details
    }
    return render(request, 'reviews/review_detail.html', context)

@login_required
def review_new(request):
    if request.method == 'POST':
        form = reviewForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.save()
            messages.success(request, "Review added successfully.")
            return redirect(review_item.get_absolute_url())
    else:
        form = reviewForm()
    context = {'form' : form}
    return render(request, 'reviews/review_edit.html', context)

@login_required
def review_edit(request, slug):
    review_item = get_object_or_404(review, slug=slug)
    if request.method == "POST":
        form = reviewForm(request.POST, request.FILES or None, instance=review_item)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.save()
            messages.success(request, "Changes saved.")
            return redirect(review_item.get_absolute_url())
    else:
        form = reviewForm(instance=review_item)
    context = {'form' : form}
    return render(request, 'reviews/review_edit.html', context)

@login_required
def review_draft_list(request):
    reviews = review.objects.filter(published=False,status=True).order_by('created_date')
    context = {'reviews' : reviews}
    return render(request, 'reviews/review_draft_list.html', context)

@login_required
def review_publish(request, slug):
    review_item = get_object_or_404(review, slug=slug)
    review_item.publish()
    messages.success(request, "Review published.", extra_tags='msg')
    return redirect(review_item.get_absolute_url())

@login_required
def review_unpublish(request, slug):
    review_item = get_object_or_404(review, slug=slug)
    review_item.unpublish()
    messages.success(request, "Review unpublished.")
    return redirect(review_item.get_absolute_url())

@login_required
def review_delete(request, slug):
    review_item = get_object_or_404(review, slug=slug)
    review_item.delete()
    messages.success(request, "Review deleted.")
    return redirect('/')

def page_not_found(request):
    response = render_to_response('reviews/404.html',
        context_instance = RequestContext(request)
    )
    response.status_code = 404
    return response

def server_error(request):
    response = render_to_response('reviews/500.html',
        context_instance = RequestContext(request)
    )
    response.status_code = 500
    return response
