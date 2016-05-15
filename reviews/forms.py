from django import forms
from .models import review

class reviewForm(forms.ModelForm):

    class Meta:
        model = review
        fields = ('title', 'subtitle', 'tldr', 'desc', 'rating', )
