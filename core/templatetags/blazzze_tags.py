"""Custom template tags so Blazzze can talk on any page."""
from django import template
from core.blazzze_quotes import get_random_quote

register = template.Library()


@register.simple_tag
def blazzze_says() -> str:
    """Drop a random Blazzze quote anywhere. Usage: {% blazzze_says %}"""
    return get_random_quote()