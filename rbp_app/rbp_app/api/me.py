import frappe


@frappe.whitelist(allow_guest=True)
def get_current_user():
	user = frappe.session.user
	is_guest = user == "Guest"
	full_name = "Guest"
	user_type = "Guest"
	roles = frappe.get_roles(user)

	if not is_guest:
		full_name = frappe.get_value("User", user, "full_name") or user
		user_type = frappe.get_value("User", user, "user_type") or "Website User"

	return {
		"user": user,
		"full_name": full_name,
		"roles": roles,
		"user_type": user_type,
		"is_guest": is_guest,
	}
