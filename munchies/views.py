"""Munchies views — snack list + HTMX roast endpoint."""
import random
from django.shortcuts import render
from .models import Snack


HALL_OF_FAME_ROASTS = [
    "Oh yeah, the button doesn't work yet. But have you listened to Marty Eyezlow?",
    "Aight calm down. The hall of fame is coming. Probably. Maybe. Don't push it.",
    "Whoa whoa whoa. We're not there yet. Have you tried just... rolling another joint?",
    "404: hall of fame not found. But you know what IS found? Marty Eyezlow's discography.",
    "Easy killer. The hall of fame opens when BSM drops his album or a single. So... never.",
    "Bro have you realised that the hall of fame is actually a state of mind? Just vibe and you'll be inducted in no time, what?",
    "The hall of fame is being built by stoners. ETA: whenever they remember.",
    "I admire the optimism but no. Try again next Tuesday. Or never.",
]


def snack_list(request):
    snacks = Snack.objects.filter(is_published=True)
    return render(request, "munchies/list.html", {"snacks": snacks})


def hall_of_fame_roast(request):
    """HTMX endpoint — returns a partial with a random Blazzze roast."""
    return render(
        request,
        "munchies/_roast.html",
        {"roast": random.choice(HALL_OF_FAME_ROASTS)},
    )