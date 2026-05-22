"""Buy admin config."""
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "emoji", "category", "price", "is_published", "created_at")
    list_filter = ("category", "is_published")
    search_fields = ("name", "tagline", "description")
    list_editable = ("is_published", "price")
