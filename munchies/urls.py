"""Munchies URL configuration."""
from django.urls import path
from . import views

app_name = "munchies"

urlpatterns = [
    path("", views.snack_list, name="list"),
    path("hall-of-fame-roast/", views.hall_of_fame_roast, name="hall_of_fame_roast"),
]