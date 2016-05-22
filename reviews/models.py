from django.db import models
from django.core.urlresolvers import reverse
from movies.models import movie

class review(models.Model):
    movie = models.ForeignKey(movie, blank=True, null=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(blank=True, null=True, max_length=200)
    tldr = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField()
    author = models.ForeignKey('auth.User')
    #tags =
    #cover_image =
    rating = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.published = True
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("reviews:review_detail", kwargs={"pk":self.id})
