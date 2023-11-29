from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



def choice_zodiak(request, sign_zodiak):
    if sign_zodiak == 'aries':
        return HttpResponse('"[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."')
    elif sign_zodiak == 'taurus':
        return HttpResponse("['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
    elif sign_zodiak == 'gemini':
        return HttpResponse("['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
    elif sign_zodiak == 'cancer':
        return HttpResponse("['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")
    elif sign_zodiak == 'leo':
        return HttpResponse("['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")
    elif sign_zodiak == 'virgo':
        return HttpResponse("['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")
    elif sign_zodiak == 'libra':
        return HttpResponse("['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
    elif sign_zodiak == 'scorpio':
        return HttpResponse("['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")
    elif sign_zodiak == 'sagittarius':
        return HttpResponse(
            "[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")
    elif sign_zodiak == 'capricorn':
        return HttpResponse("['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")
    elif sign_zodiak == 'aquarius':
        return HttpResponse(
            "[ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")
    elif sign_zodiak == 'pisces':
        return HttpResponse("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")
    else:
        return HttpResponseNotFound(f'NotFound - {sign_zodiak}')