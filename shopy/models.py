from django.db import models
from django.utils import timezone

# Create your models here.


class Shopy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    daily_rate = models.FloatField()
    number_in_stock = models.IntegerField()
    genre = models.ForeignKey(Shopy, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.title, self.release_year, self.date_created
