from django.contrib import admin
from .models import review
from django_summernote.admin import SummernoteModelAdmin


class reviewAdmin(SummernoteModelAdmin):
    list_display = ('__str__', 'author', 'created_date', 'published_date', 'published', 'status')
    class Meta:
        model=review

# class reviewAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'author', 'created_date', 'published_date', 'published')
#     class Meta:
#         model=review

admin.site.register(review, reviewAdmin)
