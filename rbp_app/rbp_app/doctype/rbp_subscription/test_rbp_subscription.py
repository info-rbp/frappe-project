import frappe
from frappe.tests.utils import FrappeTestCase


class TestRBPSubscription(FrappeTestCase):
	def test_doctype_metadata_loads(self):
		self.assertEqual(frappe.get_meta("RBP Subscription").name, "RBP Subscription")
