from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = "user"

urlpatterns = [
    path('user/', views.user, name="user"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('update_user', views.update_user, name="update_user"),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
]
