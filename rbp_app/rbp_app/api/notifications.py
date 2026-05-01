"""Notification APIs for the RBP portal/frontend."""

import frappe

from rbp_app.permissions import require_login
from rbp_app.services.notifications import get_notifications as get_notifications_service


@frappe.whitelist()
def get_notifications():
	"""Return portal notifications for the current user."""

	user = require_login()
	return get_notifications_service(user)
