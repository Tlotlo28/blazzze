"""Munchies models."""
from django.db import models


class Snack(models.Model):
    """A sacred munchies entry. Curated, not user-submitted (yet)."""

    class Vibe(models.TextChoices):
        SALTY = "SALTY", "Salty"
        SWEET = "SWEET", "Sweet"
        CHAOTIC = "CHAOTIC", "Chaotic"
        BASIC = "BASIC", "Basic"

    name = models.CharField(max_length=80)
    emoji = models.CharField(max_length=12, default="🍿")
    description = models.TextField(help_text="Funny / vivid description")
    difficulty = models.PositiveSmallIntegerField(
        default=1,
        help_text="How hard to make while blazed (1=easy, 5=brain surgery)",
    )
    vibe = models.CharField(max_length=10, choices=Vibe.choices, default=Vibe.SALTY)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.emoji} {self.name}"

    @property
    def difficulty_leaves(self):
        """Return a string of leaf emojis for the difficulty level."""
        return "🍃" * self.difficulty
