"""Buy app models."""
from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        FLOWER = "FLOWER", "Flower"
        EDIBLE = "EDIBLE", "Edible"
        EXTRACT = "EXTRACT", "Extract"
        ACCESSORY = "ACCESSORY", "Accessory"
        MYSTERY = "MYSTERY", "Mystery"

    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=12, default="🌿", help_text="Fallback if no image")
    tagline = models.CharField(max_length=200, help_text="Short one-liner shown on the card")
    description = models.TextField(help_text="Long, comical, shown in the popup")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.FLOWER)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.emoji} {self.name}"
