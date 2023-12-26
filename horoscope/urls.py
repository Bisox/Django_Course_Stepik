from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.type_sign_zodiac),
    path('type/<str:sign_type>/', views.choice_type_sign, name='type_sign_name'),
    path('<int:sign_zodiac>/', views.number_zodiac),
    path('<str:sign_zodiac>/', views.choice_zodiac, name='horoscope-name'),


]
