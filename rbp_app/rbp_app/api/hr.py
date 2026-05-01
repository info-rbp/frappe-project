import frappe

from rbp_app.services.hr import get_employee_summary as get_employee_summary_service
from rbp_app.services.hr import get_leave_summary as get_leave_summary_service


@frappe.whitelist()
def get_employee_summary():
	return get_employee_summary_service()


@frappe.whitelist()
def get_leave_summary():
	return get_leave_summary_service()
