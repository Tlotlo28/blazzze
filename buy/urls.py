"""Buy URL configuration."""
from django.urls import path
from . import views

app_name = "buy"

urlpatterns = [
    path("", views.product_list, name="list"),
    path("p/<int:pk>/", views.product_detail, name="product_detail"),
    path("p/<int:pk>/order/", views.place_order, name="place_order"),
]