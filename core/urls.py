"""Core app URL configuration."""
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("age-gate/", views.age_gate, name="age_gate"),
    path("denied/", views.denied, name="denied"),
    path("preview-404/", views.preview_404, name="preview_404"),
]

