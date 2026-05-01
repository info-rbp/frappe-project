import frappe

from rbp_app.api.me import get_current_user
from rbp_app.services.apps import get_available_apps
from rbp_app.services.billing import get_billing_placeholder
from rbp_app.services.documents import get_quick_links
from rbp_app.services.notifications import get_notifications_placeholder


@frappe.whitelist()
def get_home():
	return {
		"current_user": get_current_user(),
		"available_apps": get_available_apps(),
		"quick_links": get_quick_links(),
		"notifications": get_notifications_placeholder(),
		"billing": get_billing_placeholder(),
	}
