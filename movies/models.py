from django.db import models
from django.core.urlresolvers import reverse


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
    name = models.CharField(max_length = 200)
    storyline = models.TextField()
    tagline = models.CharField(max_length = 80, null=True, blank=True)
    cast_crew = models.ManyToManyField(
        artist,
        through='movie_artist',
        through_fields=('movie', 'artist'),
    )
    genres = models.ManyToManyField(
        genre,
        through='movie_genre',
        through_fields=('movie','genre'),
    )
    lang = models.ForeignKey(language, null=True)
    release_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"id":self.id})

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
