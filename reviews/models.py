from django.db import models
from django.utils import timezone

class review(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(blank=True, null=True, max_length=200)
    tldr = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField()
    author = models.ForeignKey('auth.User')
    #tags =
    #cover_image =
    rating = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.published = True
        self.save()

    def __str__(self):
        return self.title
