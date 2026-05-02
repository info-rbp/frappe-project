"""Portal app detail context for /portal/apps/<app_key>."""

import frappe

from rbp_app.api.integrations import get_app_summary
from rbp_app.permissions import require_login
from rbp_app.services.apps import get_available_app_cards


def _get_app_key():
    """Return the app key from route params, form data, or request path."""

    route_options = getattr(frappe.local, "route_options", None) or {}
    form_dict = getattr(frappe.local, "form_dict", None) or {}

    app_key = route_options.get("app_key") or form_dict.get("app_key")
    if app_key:
        return str(app_key).strip().lower()

    request = getattr(frappe.local, "request", None)
    path = getattr(request, "path", "") or ""
    marker = "/portal/apps/"
    if marker in path:
        return path.split(marker, 1)[1].strip("/").split("/")[0].lower()

    return ""


def _find_app_card(app_key, user):
    """Find the app card visible to the current user."""

    for card in get_available_app_cards(user):
        if card.get("key") == app_key:
            return card
    return None


def get_context(context):
    """Build context for a dedicated portal app detail page."""

    user = require_login()
    app_key = _get_app_key()
    app_card = _find_app_card(app_key, user)

    if app_card:
        app_summary = get_app_summary(app_key)
    else:
        app_summary = {
            "available": False,
            "app_key": app_key,
            "summary": {},
            "message": "This app is not available for the current user.",
        }

    context.no_cache = 1
    context.app_key = app_key
    context.app_card = app_card
    context.app_summary = app_summary
    return context
