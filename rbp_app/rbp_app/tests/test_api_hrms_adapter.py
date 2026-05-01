from unittest import TestCase
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import frappe

from rbp_app.api import hr
from rbp_app.services.adapters import hrms


class TestApiHrmsAdapter(TestCase):
	def test_guest_is_rejected(self):
		with patch.object(hr, "require_login", side_effect=frappe.PermissionError):
			with self.assertRaises(frappe.PermissionError):
				hr.get_summary()

	def test_hrms_absent_returns_safe_payload(self):
		with (
			patch.object(hr, "require_login", return_value="member@example.com"),
			patch.object(hrms, "is_app_installed", return_value=False),
		):
			result = hr.get_summary()

		self.assertFalse(result["available"])
		self.assertEqual(result["app_key"], "hrms")

	def test_missing_hrms_doctypes_fail_safely(self):
		with (
			patch.object(hr, "require_login", return_value="member@example.com"),
			patch.object(hrms, "is_app_installed", return_value=True),
			patch.object(hrms, "_doctype_exists", return_value=False),
		):
			result = hr.get_employee_summary()

		self.assertFalse(result["available"])
		self.assertEqual(result["app_key"], "hrms")

	def test_hrms_summary_exposes_counts_not_employee_records(self):
		with (
			patch.object(hrms, "is_app_installed", return_value=True),
			patch.object(hrms, "_doctype_exists", return_value=True),
			patch.object(hrms.frappe, "db", SimpleNamespace(count=MagicMock(side_effect=[3, 2, 1])), create=True),
		):
			result = hrms.get_employee_summary("member@example.com")

		self.assertTrue(result["available"])
		self.assertEqual(result["summary"]["total_employees"], 3)
		self.assertNotIn("employees", result["summary"])
		self.assertNotIn("employee_name", result["summary"])
