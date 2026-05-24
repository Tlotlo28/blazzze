"""Blazzze URL Configuration."""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve as django_static_serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("munchies/", include("munchies.urls")),
    path("buy/", include("buy.urls")),
    path("chat/", include("chat.urls")),
    path("", include("core.urls")),
]

# Serve uploaded media files (dev + prod for this portfolio project).
# For higher-traffic production use, switch to Cloudinary or S3.
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", django_static_serve, {"document_root": settings.MEDIA_ROOT}),
]

# Debug toolbar (dev only)
if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns