from django.urls import path
from . import views

urlpatterns = [
    path('<sign_zodiak>/', views.choice_zodiak)

]
