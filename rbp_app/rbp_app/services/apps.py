import frappe


def get_installed_app_names():
	return {app.lower() for app in frappe.get_installed_apps()}


def is_app_installed(app_name):
	return app_name.lower() in get_installed_app_names()


def is_documents_enabled():
	"""Placeholder for future document entitlement/module configuration."""

	enabled = frappe.conf.get("rbp_documents_enabled") if getattr(frappe, "conf", None) else None
	return enabled if enabled is not None else True


def get_future_entitlements(user=None):
	"""Future hook point for plan, tenant, and paid entitlement rules."""

	return {
		"user": user or frappe.session.user,
		"enabled_apps": [],
		"disabled_apps": [],
	}


def _has_any_role(roles, allowed):
	return bool(set(roles).intersection(allowed))


def _card(key, title, route, description, installed=True, enabled=True, source=None):
	return {
		"key": key,
		"title": title,
		"route": route,
		"description": description,
		"installed": installed,
		"enabled": enabled,
		"source": source or key,
	}


def get_available_apps(user=None):
	user = user or frappe.session.user
	installed_apps = get_installed_app_names()
	roles = frappe.get_roles(user)
	entitlements = get_future_entitlements(user)
	cards = []

	if "hrms" in installed_apps:
		cards.append(
			_card(
				"hrms",
				"HRMS",
				"/portal/hr",
				"People, leave, and employee services powered by HRMS.",
				source="hrms",
			)
		)

	if "crm" in installed_apps:
		cards.append(
			_card(
				"crm",
				"CRM",
				"/portal/crm",
				"Customer and sales workflows powered by CRM.",
				source="crm",
			)
		)

	if "lms" in installed_apps:
		cards.append(
			_card(
				"lms",
				"LMS",
				"/portal/lms",
				"Learning and course experiences powered by LMS.",
				source="lms",
			)
		)

	if is_documents_enabled():
		cards.append(
			_card(
				"documents",
				"Documents",
				"/portal/library",
				"Shared documents, templates, and resources from RBP.",
				installed=True,
				source="rbp_app",
			)
		)

	if user == "Administrator" or _has_any_role(roles, {"Administrator", "System Manager"}):
		cards.append(
			_card(
				"billing",
				"Billing",
				"/portal/billing",
				"Account billing, plans, and payment operations.",
				installed=True,
				source="rbp_app",
			)
		)

	disabled = set(entitlements.get("disabled_apps") or [])
	for card in cards:
		if card["key"] in disabled:
			card["enabled"] = False

	return cards
