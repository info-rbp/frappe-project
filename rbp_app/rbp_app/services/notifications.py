"""Notification services for the RBP platform layer."""

import frappe


def _doctype_exists(doctype):
	try:
		return bool(frappe.db.exists("DocType", doctype))
	except Exception:
		return False


def get_notifications(user=None):
	"""Return a safe notification placeholder."""

	if not user or user == "Guest" or not _doctype_exists("RBP Notification"):
		notifications = []
		return {
			"notifications": notifications,
			"unread_count": 0,
		}

	try:
		notifications = frappe.get_all(
			"RBP Notification",
			filters={"user": user},
			fields=["name", "title", "message", "notification_type", "route", "is_read", "read_on", "modified"],
			order_by="is_read asc, modified desc",
			limit_page_length=20,
		)
		unread_count = frappe.db.count("RBP Notification", {"user": user, "is_read": 0})
	except Exception:
		notifications = []
		unread_count = 0

	return {
		"notifications": notifications,
		"unread_count": unread_count,
	}


def get_notifications_payload():
	"""Backward-compatible alias for the notification placeholder payload."""

	return get_notifications()
