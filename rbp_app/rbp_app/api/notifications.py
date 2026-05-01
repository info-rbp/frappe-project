import frappe

from rbp_app.services.notifications import get_notifications_placeholder


@frappe.whitelist()
def get_notifications():
	return get_notifications_placeholder()
