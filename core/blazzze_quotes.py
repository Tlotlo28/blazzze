"""Blazzze's catalogue of unsolicited wisdom."""
import random


DEFAULT_QUOTES = [
    "Yeah yeah I hear you, but did you know your browser history is actually wild?",
    "That's crazyyy, but did you know you've been breathing wrong this whole conversation?",
    "I'm not high, you're high.",
    "Hold up... did you really come here sober? Embarrassing.",
    "I'd give you advice, but you'd ignore it like everyone else does.",
    "Damn, you again? Get a hobby.",
    "Sit down, shut up, and let Blazzze cook.",
    "Plot twist: YOU are the joint.",
    "I would explain it to you, but I left my patience in 2003.",
    "Cousin, you are ZOOTED. Go drink some water before you evaporate.",
    "When is BSM going to release his music?? Asking for a friend.",
    "Brooo, have you listened to Marty Eyezlow?",
]


def get_random_quote() -> str:
    """Return a random Blazzze quote."""
    return random.choice(DEFAULT_QUOTES)