from django.http import HttpResponse, HttpResponseRedirect
from math import pi


# Create your views here.

def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {int(pi * radius ** 2)}')


def rectangle(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
