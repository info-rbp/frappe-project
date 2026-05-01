import frappe

from rbp_app.services.billing import get_billing_placeholder


@frappe.whitelist()
def get_summary():
	return get_billing_placeholder()
