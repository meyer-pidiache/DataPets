from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path('places/', views.places, name="places"),
]