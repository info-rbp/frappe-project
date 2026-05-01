"""Billing services for the RBP platform layer."""

import frappe

from rbp_app.permissions import is_admin_user


def _placeholder():
	return {
		"status": "not_configured",
		"plan": None,
		"message": "Billing is not configured for this portal yet.",
		"billing_enabled": False,
	}


def _doctype_exists(doctype):
	try:
		return bool(frappe.db.exists("DocType", doctype))
	except Exception:
		return False


def _get_user_tenant(user=None):
	if not user or user == "Guest" or not _doctype_exists("RBP Tenant"):
		return None

	try:
		return frappe.db.get_value("RBP Tenant", {"owner_user": user}, "name")
	except Exception:
		return None


def get_subscription_status(user=None):
	"""Return a safe subscription placeholder until billing DocTypes exist."""

	if not _doctype_exists("RBP Subscription"):
		return _placeholder()

	try:
		if frappe.db.count("RBP Subscription") <= 0:
			return _placeholder()
	except Exception:
		return _placeholder()

	filters = {}
	tenant = _get_user_tenant(user)
	if tenant:
		filters["tenant"] = tenant
	elif not is_admin_user(user):
		return _placeholder()

	try:
		subscriptions = frappe.get_all(
			"RBP Subscription",
			filters=filters,
			fields=[
				"name",
				"tenant",
				"status",
				"plan",
				"billing_provider",
				"current_period_start",
				"current_period_end",
			],
			order_by="modified desc",
			limit_page_length=1,
		)
	except Exception:
		return _placeholder()

	if not subscriptions:
		return _placeholder()

	subscription = subscriptions[0]
	return {
		"status": subscription.get("status"),
		"plan": subscription.get("plan"),
		"message": "Subscription status is available.",
		"billing_enabled": True,
		"subscription": {
			"name": subscription.get("name"),
			"tenant": subscription.get("tenant"),
			"billing_provider": subscription.get("billing_provider"),
			"current_period_start": subscription.get("current_period_start"),
			"current_period_end": subscription.get("current_period_end"),
		},
	}


def get_subscription_status_payload():
	"""Backward-compatible alias for the subscription placeholder payload."""

	return get_subscription_status()
