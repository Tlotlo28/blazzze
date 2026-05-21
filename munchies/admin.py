"""Munchies admin config."""
from django.contrib import admin
from .models import Snack


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ("name", "emoji", "vibe", "difficulty", "is_published", "created_at")
    list_filter = ("vibe", "is_published")
    search_fields = ("name", "description")
    list_editable = ("is_published", "difficulty")