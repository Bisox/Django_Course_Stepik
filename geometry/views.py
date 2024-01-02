from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from math import pi


# Create your views here.

def get_rectangle_area(request, width, height):
    S = width * height
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {S}')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width):
    S = width * width
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {S}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius):
    D = pi * radius ** 2
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {D}')
    return render(request, 'geometry/circle.html')


def rectangle(request, width, height):
    rectangle_url = reverse('rectangle-name', args=(width, height,))
    return HttpResponseRedirect(rectangle_url)


def square(request, width):
    square_url = reverse('square-name', args=(width,))
    return HttpResponseRedirect(square_url)


def circle(request, radius):
    circle_url = reverse('circle-name', args=(radius,))
    return HttpResponseRedirect(circle_url)
