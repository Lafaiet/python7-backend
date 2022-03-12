from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.name
