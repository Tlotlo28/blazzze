"""Core app views."""
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods


def home(request):
    """The Blazzze homepage."""
    return render(request, "core/home.html")


@require_http_methods(["GET", "POST"])
def age_gate(request):
    """The age verification interstitial."""
    if request.method == "POST":
        choice = request.POST.get("choice")
        if choice == "yes":
            request.session["age_verified"] = True
            next_url = request.POST.get("next") or reverse("core:home")
            return redirect(next_url)
        return redirect("core:denied")

    return render(
        request,
        "core/age_gate.html",
        {"next_url": request.GET.get("next", "")},
    )


def denied(request):
    """For the users who said no. Blazzze roasts them gently."""
    return render(request, "core/denied.html")