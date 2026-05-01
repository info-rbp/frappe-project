import frappe
from frappe.tests.utils import FrappeTestCase


class TestRBPTenant(FrappeTestCase):
	def test_doctype_metadata_loads(self):
		self.assertEqual(frappe.get_meta("RBP Tenant").name, "RBP Tenant")
