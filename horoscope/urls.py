from django.urls import path, register_converter
from . import views, converter

register_converter(converter.FourDigitYearConverter, 'yyyy')
register_converter(converter.MyFloatConverter, 'float')
register_converter(converter.MyDateConverter, 'date')

urlpatterns = [
    path('', views.index),
    path('type/', views.type_sign_zodiac),
    path('type/<str:sign_type>/', views.choice_type_sign, name='type_sign_name'),
    # converters-------------------------------------------------------
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converter),
    path('<float:sign_zodiac>/', views.get_float_converter),
    path('<date:sign_zodiac>/', views.get_date_converter),
    # -----------------------------------------------------------------
    path('<int:sign_zodiac>/', views.number_zodiac),
    path('<str:sign_zodiac>/', views.choice_zodiac, name='horoscope-name'),

]
