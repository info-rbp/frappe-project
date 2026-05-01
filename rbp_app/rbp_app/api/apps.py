import frappe

from rbp_app.services.apps import get_available_apps as get_available_apps_service


@frappe.whitelist()
def get_available_apps():
	return get_available_apps_service()
