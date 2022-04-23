from django.db import models
from django.contrib.auth.models import User


LANGUAGE_OPTIONS = [
    ('English', 'English'),
    ('Russian', 'Russian'),
    ('Estonian', 'Estonian'),
]



class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Star(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=20)
    duration = models.CharField(max_length=10, default='-')
    description = models.TextField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True, blank=True)
    stars = models.ManyToManyField(Star, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True, choices=LANGUAGE_OPTIONS)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')

    # imdb url
    # language
    # rating
    # budget
    # trailer url
    # content rating

    # movie cover ????

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    alergic = models.BooleanField(default=False)
    favorite_movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.user.username


STARS_OPTIONS = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]
class Rate(models.Model):

    num_starts = models.PositiveIntegerField(choices=STARS_OPTIONS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + ' - ' + self.profile.user.username
