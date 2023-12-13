from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
weekdays_dict = {
    "Monday": "Встать, пожрать, поспать",
    "Tuesday": "Что-нибудь",
    "Wednesday": "Кого-нибудь",
    "Thursday": "Чем-нибудь",
    "Friday": "Для чего-нибудь",
    "Saturday": "Кем-нибудь",
    "Sunday": "Заново"
}


def weekday_choice(request, weekday: str):
    description = weekdays_dict.get(weekday, None)
    if description:
        return HttpResponse(description)

    return HttpResponseNotFound('Not Found Day')


def weekday_number(request, weekday: int):
    weekday_list = list(weekdays_dict)

    if len(weekday_list) < weekday:
        return HttpResponseNotFound(f'Неверный номер дня - {weekday}')
    name_weekday = weekday_list[weekday-1]
    redirect_url = reverse('weekday-name', args=(name_weekday, ))
    return HttpResponseRedirect(redirect_url)
