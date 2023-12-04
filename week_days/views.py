from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def weekday_choice(request, weekday: str):
    if weekday == 'monday':
        return HttpResponse('<br> Встать <br>'
                            '<br> Пожрать <br>'
                            '<br> Поспать <br>')
    elif weekday == 'tuesday':
        return HttpResponse('Отдыхаем')
    else:
        return HttpResponseNotFound('Not Found Day')


def weekday_number(request, weekday: int):
    if 1 <= weekday <= 7:
        return HttpResponse(f'Сегодня {weekday} день недели')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {weekday}')

