from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from decouple import config

ADMIN_URL = config('ADMIN_URL', default='admin/')

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path("", include("site_dlo3.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")
