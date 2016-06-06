from django.contrib import admin
from .models import movie, artist, movie_artist, role, language, genre, movie_genre
# Register your models here.

class movieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=movie

admin.site.register(movie, movieAdmin)

class artistAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=artist

admin.site.register(artist, artistAdmin)

class movie_artistAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=movie_artist

admin.site.register(movie_artist, movie_artistAdmin)

class roleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=role

admin.site.register(role, roleAdmin)

class languageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=language

admin.site.register(language, languageAdmin)
class genresAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=genre

admin.site.register(genre, genresAdmin)

class movie_genreAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'last_updated_date')
    class Meta:
        model=movie_genre

admin.site.register(movie_genre, movie_genreAdmin)
