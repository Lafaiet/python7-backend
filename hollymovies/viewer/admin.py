from django.contrib import admin
from viewer.models import Movie, Director, Star, Profile, Rate


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Star)
admin.site.register(Profile)
admin.site.register(Rate)