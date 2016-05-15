from django.shortcuts import render, get_object_or_404, redirect
from .models import review
from .forms import reviewForm
from django.utils import timezone


# Create your views here.
def reviews_list(request):
    reviews = review.objects.filter(published=True)
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review_item = get_object_or_404(review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review_item})

def review_new(request):
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.published_date = timezone.now()
            review_item.save()
            return redirect('review_detail', pk=review_item.pk)
    else:
        form = reviewForm()
    return render(request, 'reviews/review_edit.html', {'form' : form})

def review_edit(request, pk):
    review_item = get_object_or_404(review, pk=pk)
    if request.method == "POST":
        form = reviewForm(request.POST, instance=review_item)
        if form.is_valid():
            review_item = form.save(commit=False)
            review_item.author = request.user
            review_item.published_date = timezone.now()
            review_item.save()
            return redirect('review_detail', pk=review_item.pk)
    else:
        form = reviewForm(instance=review_item)
    return render(request, 'reviews/review_edit.html', {'form' : form})
