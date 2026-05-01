import frappe


DEFAULT_ADMIN_ROLES = ("Administrator", "System Manager")


def get_admin_roles():
	"""Return roles that can access the RBP admin scaffold."""

	roles = list(DEFAULT_ADMIN_ROLES)

	for role in frappe.get_hooks("rbp_admin_roles") or []:
		if role not in roles:
			roles.append(role)

	configured = frappe.conf.get("rbp_admin_roles") if getattr(frappe, "conf", None) else None
	if isinstance(configured, str):
		configured = [role.strip() for role in configured.split(",")]

	for role in configured or []:
		if role and role not in roles:
			roles.append(role)

	return roles


def user_has_any_role(allowed_roles=None, user=None):
	"""Check whether the current or supplied user has one of the allowed roles."""

	allowed_roles = set(allowed_roles or [])
	if not allowed_roles:
		return False

	if user == "Administrator" and "Administrator" in allowed_roles:
		return True

	return bool(allowed_roles.intersection(frappe.get_roles(user)))


def is_admin_user(user=None):
	user = user or frappe.session.user
	return user_has_any_role(get_admin_roles(), user=user)
