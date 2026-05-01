import frappe
from frappe.tests.utils import FrappeTestCase


class TestRBPAppEntitlement(FrappeTestCase):
	def test_doctype_metadata_loads(self):
		self.assertEqual(frappe.get_meta("RBP App Entitlement").name, "RBP App Entitlement")
