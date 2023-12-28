from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_yyyy_converter(request, sign_zodiac):
    return HttpResponse(f'Принято 4-х значное число {sign_zodiac}')


def get_float_converter(request, sign_zodiac):
    return HttpResponse(f'Принято вещественное число {sign_zodiac}')


def get_date_converter(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату: {sign_zodiac}')


def type_sign_zodiac(request):
    type_list = list(zodiac_element)
    element = ''
    for type in type_list:
        redirect_path = reverse('type_sign_name', args=[type])
        element += f'<li><h3><a href="{redirect_path}">{type.title()}</a></h3></li>'
    response = f"""
    <ul>
        {element}
    </ul>                
    """
    return HttpResponse(response)


def choice_type_sign(request, sign_type):
    description = zodiac_element.get(sign_type, None)
    if description:
        sign_element = ''
        for element in description:
            redirect_url = reverse('horoscope-name', args=[element])
            sign_element += f'<li><h3><a href="{redirect_url}">{element.title()}</a></h3></li>'
        response = f"""
        <ul>
        {sign_element}
        </ul>                
        """
        return HttpResponse(response)


def index(request):
    zodiac_list = list(zodiac_dict)
    li_elements = ''
    for sign in zodiac_list:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f'<li> <a href={redirect_path}>{sign.title()} </a> </li>'
    response = f'''
    <ul>
        {li_elements}
    </ul>    
    '''
    return HttpResponse(response)


def choice_zodiac(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')

    return HttpResponseNotFound(f'NotFound - {sign_zodiac}')


def number_zodiac(request, sign_zodiac):
    zodiac_list = list(zodiac_dict)

    if sign_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'NotFound - {sign_zodiac}')
    name_zodiac = zodiac_list[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
