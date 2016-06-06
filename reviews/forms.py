from django import forms
from .models import review
from django_summernote.widgets import SummernoteWidget,SummernoteInplaceWidget

class reviewForm(forms.ModelForm):
    desc = forms.CharField(widget=SummernoteInplaceWidget())
    class Meta:
        model = review
        fields = ('title', 'subtitle', 'tldr', 'cover_image', 'desc', 'movie', 'rating', )
