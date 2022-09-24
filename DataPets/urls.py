from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.main.urls')),
    path('', include('apps.places.urls')),
    path('', include('apps.user.urls')),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)