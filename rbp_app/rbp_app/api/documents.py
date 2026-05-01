import frappe

from rbp_app.services.documents import get_quick_links


@frappe.whitelist()
def get_documents_home():
	return {
		"quick_links": get_quick_links(),
	}
