from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<int:weekday>/', views_week_days.weekday_number),
    path('<str:weekday>/', views_week_days.weekday_choice),
]
