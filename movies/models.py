from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

def upload_location(instance, filename):
    return "%s/%s" %(instance.slug, filename)

class language(models.Model):
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=3)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class role(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class artist(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class genre(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class movie(models.Model):
    slug = models.SlugField(unique=True,max_length=85)
    name = models.CharField(max_length = 200)
    storyline = models.TextField()
    tagline = models.CharField(max_length = 80, null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    lang = models.ForeignKey(language, null=True)
    release_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"slug":self.slug})

class movie_artist(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.DO_NOTHING)
    artist = models.ForeignKey(artist, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(role, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s | %s | %s' %(self.movie, self.artist, self.role)

class movie_genre(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(genre, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s | %s' %(self.movie, self.genre)

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


def pre_save_movie_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_movie_receiver, sender=movie)
