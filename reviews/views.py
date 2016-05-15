from django.shortcuts import render, get_object_or_404
from .models import review

# Create your views here.
def reviews_list(request):
    reviews = review.objects.filter(published=True)
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review_item = get_object_or_404(review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review_item})
