"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from viewer.views import (
    hello, calculator, MoviesListView,
    WelcomeView, MovieDetailView,
    CreateMovieView, UpdateMovie,
    DeleteMovie
)


urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('calculator', calculator),
    path('movies', MoviesListView.as_view(), name='movies'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/create', CreateMovieView.as_view(), name='create_movie'),
    path('movies/<int:pk>/update', UpdateMovie.as_view(), name='update_movie'),
    path('movies/<int:pk>/delete', DeleteMovie.as_view(), name='delete_movie'),
    path('accounts/', include('django.contrib.auth.urls')),
]
