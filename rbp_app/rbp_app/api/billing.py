"""Billing APIs for the RBP portal/frontend."""

import frappe

from rbp_app.permissions import require_login
from rbp_app.services.billing import get_subscription_status as get_subscription_status_service


@frappe.whitelist()
def get_subscription_status():
	"""Return the current user's subscription status or a safe placeholder."""

	user = require_login()
	return get_subscription_status_service(user)
