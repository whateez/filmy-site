from django.db import models
from django.core.urlresolvers import reverse
from movies.models import movie
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify

def upload_location(instance, filename):
    return "%s/%s" %(instance.slug, filename)

class review(models.Model):
    slug = models.SlugField(unique=True,max_length=85)
    movie = models.ForeignKey(movie, blank=True, null=True)
    title = models.CharField(max_length=80)
    subtitle = models.CharField(blank=True, null=True, max_length=200)
    tldr = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField()
    author = models.ForeignKey('auth.User')
    #tags =
    cover_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    rating = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.published = True
        self.save()

    def unpublish(self):
        self.published_date = None
        self.published = False
        self.save()

    def delete(self):
        self.last_updated_date = timezone.now()
        self.status = False
        self.published = False
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("reviews:review_detail", kwargs={"slug":self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = review.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_review_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_review_receiver, sender=review)
