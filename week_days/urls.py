from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<weekday>/', views_week_days.weekday_choice)
]
