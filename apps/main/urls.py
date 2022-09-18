from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('que_es_datapets/', views.about_1, name="about_1"),
    path('donde_encontrarnos/', views.about_2, name="about_2"),
    path('contactenos/', views.about_3, name="about_3"),
]
