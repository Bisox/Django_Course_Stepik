from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>/', views.number_zodiac),
    path('<str:sign_zodiac>/', views.choice_zodiac, name='horoscope-name'),

]
