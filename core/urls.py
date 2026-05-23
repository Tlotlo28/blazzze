"""Core app URL configuration."""
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("age-gate/", views.age_gate, name="age_gate"),
    path("denied/", views.denied, name="denied"),
    path("preview-404/", views.preview_404, name="preview_404"),
    path("why-cannabis/", views.why_cannabis, name="why_cannabis"),
    path("contact/", views.contact, name="contact"),
    path("legal-popup/", views.legal_modal, name="legal_modal"),
]

