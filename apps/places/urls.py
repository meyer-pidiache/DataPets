from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path('', views.places, name="places"),
    path('<int:place_id>/', views.detail, name="detail"),
    path('<int:place_id>/edit/', views.edit, name="edit"),
]