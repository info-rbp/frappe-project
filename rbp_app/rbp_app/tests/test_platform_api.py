from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch

import frappe
from frappe.exceptions import Redirect

from rbp_app import guards
from rbp_app.api import apps as apps_api
from rbp_app.api import dashboard, hr, me


class TestPortalGuards(TestCase):
	def test_guest_cannot_access_portal_routes(self):
		context = SimpleNamespace(path="portal/dashboard")

		with (
			patch.object(guards.frappe, "session", SimpleNamespace(user="Guest"), create=True),
			patch.object(guards, "_redirect_to_login", side_effect=Redirect(302)) as redirect_to_login,
		):
			with self.assertRaises(Redirect):
				guards.protect_portal_routes(context)

		redirect_to_login.assert_called_once_with("portal/dashboard")


class TestCurrentUserApi(TestCase):
	def test_get_current_user_returns_session_payload(self):
		with (
			patch.object(me.frappe, "session", SimpleNamespace(user="member@example.com"), create=True),
			patch.object(me.frappe, "get_roles", return_value=["Website User"]),
			patch.object(
				me.frappe,
				"get_value",
				side_effect=lambda doctype, name, field: {
					"full_name": "Member Example",
					"user_type": "Website User",
				}[field],
			),
		):
			result = me.get_current_user()

		self.assertEqual(result["user"], "member@example.com")
		self.assertEqual(result["full_name"], "Member Example")
		self.assertEqual(result["roles"], ["Website User"])
		self.assertEqual(result["user_type"], "Website User")
		self.assertFalse(result["is_guest"])


class TestAvailableAppsApi(TestCase):
	def test_get_available_apps_returns_hrms_only_when_installed(self):
		with (
			patch.object(apps_api.frappe, "session", SimpleNamespace(user="member@example.com"), create=True),
			patch.object(apps_api.frappe, "get_installed_apps", return_value=["frappe", "rbp_app"]),
			patch.object(apps_api.frappe, "get_roles", return_value=["Website User"]),
			patch.object(apps_api.frappe, "conf", {"rbp_documents_enabled": False}, create=True),
		):
			without_hrms = apps_api.get_available_apps()

		self.assertNotIn("hrms", {app["key"] for app in without_hrms})

		with (
			patch.object(apps_api.frappe, "session", SimpleNamespace(user="member@example.com"), create=True),
			patch.object(apps_api.frappe, "get_installed_apps", return_value=["frappe", "rbp_app", "hrms"]),
			patch.object(apps_api.frappe, "get_roles", return_value=["Website User"]),
			patch.object(apps_api.frappe, "conf", {"rbp_documents_enabled": False}, create=True),
		):
			with_hrms = apps_api.get_available_apps()

		self.assertIn("hrms", {app["key"] for app in with_hrms})


class TestDashboardApi(TestCase):
	def test_get_home_returns_expected_payload(self):
		with (
			patch.object(dashboard, "get_current_user", return_value={"user": "member@example.com"}),
			patch.object(dashboard, "get_available_apps", return_value=[{"key": "documents"}]),
			patch.object(dashboard, "get_quick_links", return_value=[{"label": "Dashboard"}]),
			patch.object(dashboard, "get_notifications_placeholder", return_value={"items": []}),
			patch.object(dashboard, "get_billing_placeholder", return_value={"status": "placeholder"}),
		):
			result = dashboard.get_home()

		self.assertEqual(result["current_user"]["user"], "member@example.com")
		self.assertEqual(result["available_apps"], [{"key": "documents"}])
		self.assertEqual(result["quick_links"], [{"label": "Dashboard"}])
		self.assertEqual(result["notifications"], {"items": []})
		self.assertEqual(result["billing"], {"status": "placeholder"})


class TestHrApi(TestCase):
	def test_hrms_endpoints_fail_safely_when_hrms_is_absent(self):
		with patch.object(hr.frappe, "get_installed_apps", return_value=["frappe", "rbp_app"]):
			employee_summary = hr.get_employee_summary()
			leave_summary = hr.get_leave_summary()

		self.assertEqual(employee_summary["installed"], False)
		self.assertIsNone(employee_summary["employee"])
		self.assertEqual(leave_summary["installed"], False)
		self.assertEqual(leave_summary["allocations"], [])
