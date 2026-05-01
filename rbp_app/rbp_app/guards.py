from urllib.parse import urlencode

import frappe
from frappe.exceptions import Redirect

from rbp_app.permissions import is_admin_user
from rbp_app.services.apps import get_available_apps


def _path_from_context(context):
	return (getattr(context, "path", None) or getattr(frappe.local, "path", "") or "").strip("/")


def _redirect_to_login(path):
	target = f"/{path.lstrip('/')}" if path else "/portal/dashboard"
	frappe.flags.redirect_location = f"/login?{urlencode({'redirect-to': target})}"
	raise Redirect(302)


def _is_portal_path(path):
	return path == "portal" or path.startswith("portal/")


def _is_admin_path(path):
	return path == "admin" or path.startswith("admin/")


def protect_portal_routes(context):
	path = _path_from_context(context)

	if not _is_portal_path(path):
		return context

	context.no_cache = 1
	if frappe.session.user == "Guest":
		_redirect_to_login(path)

	context.portal_available_apps = get_available_apps()
	return context


def protect_admin_routes(context):
	path = _path_from_context(context)

	if not _is_admin_path(path):
		return context

	context.no_cache = 1
	if frappe.session.user == "Guest":
		_redirect_to_login(path)

	if not is_admin_user():
		raise frappe.PermissionError

	return context
