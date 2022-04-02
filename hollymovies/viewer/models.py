from django.db import models


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


# name  year genre  duration       description
# Batman 2020 action  ?????        [asadad sasasas asa sasa saasa  ssa sa sas as asasasasasas sasas adad dad adfaf afafaf afagf ]
# Spider man 2022 action 1h 20mins null