from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def monday(request):
    return HttpResponse('<br> Встать <br>'
                        '<br> Пожрать <br>'
                        '<br> Поспать <br>')

def tuesday(request):
    return HttpResponse('Отдыхаем')