from django.db import models

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

class movie(models.Model):
    name = models.CharField(max_length = 200)
    cast_crew = models.ManyToManyField(
        artist,
        through='movie_artist',
        through_fields=('movie', 'artist'),
    )
    lang = models.ForeignKey(language, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class movie_artist(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.DO_NOTHING)
    artist = models.ForeignKey(artist, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(role, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s | %s | %s' %(self.movie, self.artist, self.role)
