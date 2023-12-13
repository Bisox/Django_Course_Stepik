from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {int(pi * radius ** 2)}')


def rectangle(request, width, height):
    rectangle_url = reverse('rectangle-name', args=(width, height, ))
    return HttpResponseRedirect(rectangle_url)


def square(request, width):
    square_url = reverse('square-name', args=(width, ))
    return HttpResponseRedirect(square_url)


def circle(request, radius):
    circle_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(circle_url)
