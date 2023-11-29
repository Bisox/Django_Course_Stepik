from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.



def weekday_choice(request, weekday):
    if weekday == 'monday':
        return HttpResponse('<br> Встать <br>'
                            '<br> Пожрать <br>'
                            '<br> Поспать <br>')
    elif weekday == 'tuesday':
        return HttpResponse('Отдыхаем')
    else:
        return HttpResponseNotFound('Not Found Day')
