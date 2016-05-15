from django.shortcuts import render
from .models import review

# Create your views here.
def reviews_list(request):
    reviews = review.objects.filter(published=True)
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})
