"""Chat views."""
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .blazzze_responses import get_intro, get_response


def chat_page(request):
    """Render the main chat page with a random intro."""
    return render(request, "chat/page.html", {"intro": get_intro()})


@require_http_methods(["POST"])
def send_message(request):
    """HTMX endpoint — returns the user bubble + Blazzze's response bubble."""
    user_message = (request.POST.get("message") or "").strip()

    if not user_message:
        return render(request, "chat/_message_exchange.html", {
            "user_message": "",
            "blazzze_response": "...You didn't say anything. Try words.",
        })

    return render(request, "chat/_message_exchange.html", {
        "user_message": user_message,
        "blazzze_response": get_response(user_message),
    })
