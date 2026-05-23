"""Blazzze URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("munchies/", include("munchies.urls")),
    path("buy/", include("buy.urls")),
    path("chat/", include("chat.urls")),
    path("", include("core.urls")),
]

# Serve uploaded media files (works in both dev and prod for this project)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar (dev only)
if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns