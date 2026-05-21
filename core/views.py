"""Core app views — homepage and shared stuff."""
from django.shortcuts import render


def home(request):
    """The Blazzze homepage."""
    return render(request, "core/home.html")
