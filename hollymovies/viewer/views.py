import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from viewer.models import Movie
from django.urls import reverse_lazy


def hello(request):
    lucky_number = random.randint(1, 100)
    return HttpResponse(f'Hello World! Your lucky number is {lucky_number}')


def calculator(request):
    x = request.GET.get('x')
    y = request.GET.get('y')

    if x is None or y is None:
        return HttpResponse('Error! Missing numbers!')

    try:
        x = int(x)
        y = int(y)
    except Exception:
        return HttpResponse('Error! Only numbers are accepted!')

    return HttpResponse(x+y)


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class MoviesListView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'movie_detail.html'
    model = Movie
    context_object_name = 'movie'
    permission_required = 'viewer.view_movie'


class CreateMovieView(PermissionRequiredMixin, CreateView):
    template_name = 'create_movie.html'
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'


class UpdateMovie(PermissionRequiredMixin, UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    success_url = reverse_lazy('movies')
    context_object_name = 'movie'
    fields = '__all__'
    permission_required = 'viewer.change_movie'


class DeleteMovie(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'

