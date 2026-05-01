import frappe
from frappe.tests.utils import FrappeTestCase


class TestRBPAuditLog(FrappeTestCase):
	def test_doctype_metadata_loads(self):
		self.assertEqual(frappe.get_meta("RBP Audit Log").name, "RBP Audit Log")
