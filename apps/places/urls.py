from django.urls import path
from .views import *

app_name = "places"

urlpatterns = [
    path("", places, name="places"),
    path("add/", Add.as_view(), name="add"),
    path("<int:place_id>/", detail, name="detail"),
    path("<int:place_id>/edit/", edit, name="edit"),
    path("<int:place_id>/delete/", delete, name="delete"),
]
