from django.contrib import admin

from applications.movie.models import Movie, Relation, Like

# Register your models here.
admin.site.register(Movie)
admin.site.register(Relation)
admin.site.register(Like)
