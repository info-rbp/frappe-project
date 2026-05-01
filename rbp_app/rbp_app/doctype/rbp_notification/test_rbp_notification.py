import frappe
from frappe.tests.utils import FrappeTestCase


class TestRBPNotification(FrappeTestCase):
	def test_doctype_metadata_loads(self):
		self.assertEqual(frappe.get_meta("RBP Notification").name, "RBP Notification")
