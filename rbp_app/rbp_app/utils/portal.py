import frappe


def protect_portal_routes(context):
    """Require login for all RBP portal shell routes.

    This keeps portal gating aligned with Frappe's native website permission
    flow without introducing a custom auth system.
    """

    path = (getattr(context, "path", None) or getattr(frappe.local, "path", "") or "").strip("/")

    if path == "portal" or path.startswith("portal/"):
        context.no_cache = 1
        if frappe.session.user == "Guest":
            raise frappe.PermissionError

