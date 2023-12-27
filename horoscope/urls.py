from django.urls import path, register_converter
from . import views, converter

register_converter(converter.FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', views.index),
    path('type/', views.type_sign_zodiac),
    path('type/<str:sign_type>/', views.choice_type_sign, name='type_sign_name'),

    path('<yyyy:sign_zodiac>/', views.get_yyyy_converter),

    path('<int:sign_zodiac>/', views.number_zodiac),
    path('<str:sign_zodiac>/', views.choice_zodiac, name='horoscope-name'),


]
