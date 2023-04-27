from django.conf.urls.static import static
from django.urls import path, include
from . import settings

urlpatterns = [
    path('api/v1/auth/', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
