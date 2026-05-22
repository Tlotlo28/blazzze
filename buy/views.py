"""Buy app views."""
from django.shortcuts import get_object_or_404, render
from .models import Product


def product_list(request):
    products = Product.objects.filter(is_published=True)
    return render(request, "buy/list.html", {"products": products})


def product_detail(request, pk):
    """HTMX endpoint — returns the modal partial for a product."""
    product = get_object_or_404(Product, pk=pk, is_published=True)
    return render(request, "buy/_product_detail.html", {"product": product})


def place_order(request, pk):
    """HTMX endpoint — returns the 'order placed' comedic confirmation."""
    product = get_object_or_404(Product, pk=pk, is_published=True)
    return render(request, "buy/_order_placed.html", {"product": product})