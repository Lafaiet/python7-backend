import random
from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Movie


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


def welcome(request):
    return render(request, 'welcome.html')

def movies(request):
    data_movies = Movie.objects.all()

    context = {
        'movies': data_movies
    }

    return render(request, 'movies.html', context=context)
