"""HRMS adapter for safe people-module summaries."""

import frappe

from rbp_app.services.apps import is_app_installed


def _doctype_exists(doctype):
	try:
		return bool(frappe.db.exists("DocType", doctype))
	except Exception:
		return False


def _unavailable(message):
	return {
		"available": False,
		"app_key": "hrms",
		"summary": {},
		"message": message,
	}


def is_available():
	"""Return whether HRMS and the minimum HRMS DocTypes are available."""

	return is_app_installed("hrms") and _doctype_exists("Employee")


def get_employee_summary(user=None):
	"""Return safe employee counts and statuses without exposing employee details."""

	if not is_app_installed("hrms"):
		return _unavailable("HRMS is not installed.")

	if not _doctype_exists("Employee"):
		return _unavailable("HRMS Employee DocType is not available.")

	try:
		total_employees = frappe.db.count("Employee")
		active_employees = frappe.db.count("Employee", {"status": "Active"})
		inactive_employees = frappe.db.count("Employee", {"status": "Inactive"})
	except Exception as exc:
		return _unavailable(f"Employee summary is unavailable: {exc}")

	return {
		"available": True,
		"app_key": "hrms",
		"summary": {
			"total_employees": total_employees,
			"active_employees": active_employees,
			"inactive_employees": inactive_employees,
		},
		"message": "Employee summary is available.",
	}


def get_leave_summary(user=None):
	"""Return safe leave allocation and application counts."""

	if not is_app_installed("hrms"):
		return _unavailable("HRMS is not installed.")

	required_doctypes = ("Leave Application", "Leave Allocation")
	missing_doctypes = [doctype for doctype in required_doctypes if not _doctype_exists(doctype)]
	if missing_doctypes:
		return _unavailable(f"HRMS leave DocTypes are not available: {', '.join(missing_doctypes)}.")

	try:
		open_leave_applications = frappe.db.count("Leave Application", {"status": "Open"})
		approved_leave_applications = frappe.db.count("Leave Application", {"status": "Approved"})
		active_leave_allocations = frappe.db.count("Leave Allocation", {"docstatus": 1})
	except Exception as exc:
		return _unavailable(f"Leave summary is unavailable: {exc}")

	return {
		"available": True,
		"app_key": "hrms",
		"summary": {
			"open_leave_applications": open_leave_applications,
			"approved_leave_applications": approved_leave_applications,
			"active_leave_allocations": active_leave_allocations,
		},
		"message": "Leave summary is available.",
	}


def get_summary(user=None):
	"""Return the combined safe HRMS adapter summary."""

	if not is_app_installed("hrms"):
		return _unavailable("HRMS is not installed.")

	employee_summary = get_employee_summary(user)
	leave_summary = get_leave_summary(user)

	return {
		"available": employee_summary["available"] or leave_summary["available"],
		"app_key": "hrms",
		"summary": {
			"employees": employee_summary,
			"leave": leave_summary,
		},
		"message": "HRMS summary is available."
		if employee_summary["available"] or leave_summary["available"]
		else "HRMS summary is not available.",
	}
