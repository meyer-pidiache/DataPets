from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', include('apps.main.urls')),
    path('places/', include('apps.places.urls')),
    path('', include('apps.user.urls')),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset/password_reset_complete.html'), name='password_reset_complete'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)