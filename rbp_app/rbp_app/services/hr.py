import frappe

from rbp_app.services.apps import is_app_installed


EMPTY_EMPLOYEE_SUMMARY = {
	"installed": False,
	"employee": None,
	"employment_status": None,
	"department": None,
	"designation": None,
}

EMPTY_LEAVE_SUMMARY = {
	"installed": False,
	"employee": None,
	"allocations": [],
}


def is_hrms_available():
	return is_app_installed("hrms")


def _safe_empty(payload):
	return dict(payload)


def get_employee_for_user(user=None):
	user = user or frappe.session.user
	if not is_hrms_available() or user == "Guest":
		return None

	employee_name = frappe.db.exists("Employee", {"user_id": user})
	if not employee_name:
		return None

	employee = frappe.get_doc("Employee", employee_name)
	if not employee.has_permission("read"):
		return None

	return employee


def get_employee_summary(user=None):
	if not is_hrms_available():
		return _safe_empty(EMPTY_EMPLOYEE_SUMMARY)

	employee = get_employee_for_user(user)
	if not employee:
		payload = _safe_empty(EMPTY_EMPLOYEE_SUMMARY)
		payload["installed"] = True
		return payload

	return {
		"installed": True,
		"employee": employee.name,
		"employee_name": getattr(employee, "employee_name", None),
		"employment_status": getattr(employee, "status", None),
		"department": getattr(employee, "department", None),
		"designation": getattr(employee, "designation", None),
	}


def get_leave_summary(user=None):
	if not is_hrms_available():
		return _safe_empty(EMPTY_LEAVE_SUMMARY)

	employee = get_employee_for_user(user)
	if not employee:
		payload = _safe_empty(EMPTY_LEAVE_SUMMARY)
		payload["installed"] = True
		return payload

	allocations = frappe.get_list(
		"Leave Allocation",
		filters={"employee": employee.name, "docstatus": 1},
		fields=["name", "leave_type", "from_date", "to_date", "total_leaves_allocated"],
		order_by="from_date desc",
		limit_page_length=20,
	)

	return {
		"installed": True,
		"employee": employee.name,
		"allocations": allocations,
	}
