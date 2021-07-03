from django.shortcuts import render

from mainapp.models import City
import random


def index(request):
    city = City.objects.all()

    context = {
        'title': 'Главная',
        'random': random.choice(city),
    }
    return render(request, 'mainapp/index.html', context)


def about_us(request):
    context = {
        'title': 'О нас',
    }
    return render(request, 'mainapp/about_us.html', context)
