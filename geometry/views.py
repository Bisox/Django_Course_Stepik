from django.http import HttpResponse
from math import pi


# Create your views here.

def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {int(pi * radius ** 2)}')
