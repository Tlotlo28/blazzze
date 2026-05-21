"""Custom middleware for Blazzze."""
from django.shortcuts import redirect
from django.urls import reverse


class AgeVerificationMiddleware:
    """
    Blocks access to the site until the user confirms they're 18+.
    Adds an 'age_verified' flag to the session once confirmed.
    """

    # Paths the gate never blocks (admin, static, debug, the gate itself, denied page)
    EXEMPT_PREFIXES = (
        "/admin/",
        "/static/",
        "/media/",
        "/__debug__/",
        "/age-gate/",
        "/denied/",
    )

    def __init__(self, get_response):
        # Runs ONCE when the server starts
        self.get_response = get_response

    def __call__(self, request):
        # Runs on EVERY request

        # Already verified? Let them through.
        if request.session.get("age_verified"):
            return self.get_response(request)

        # Path is exempt? Let it through.
        if request.path.startswith(self.EXEMPT_PREFIXES):
            return self.get_response(request)

        # Otherwise, send them to the gate (preserving where they wanted to go)
        gate_url = reverse("core:age_gate")
        return redirect(f"{gate_url}?next={request.path}")