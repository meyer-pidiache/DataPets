from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('user/', views.user, name="user"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('logout_user', views.logout_user, name="logout_user"),
]
