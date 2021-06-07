from django.contrib import admin
from .models import Shopy, Movie


class ShopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'daily_rate',
                    'number_in_stock', 'date_created', 'genre')


# Register your models here.
admin.site.register(Shopy, ShopyAdmin)
admin.site.register(Movie, MovieAdmin)
