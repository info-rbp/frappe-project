import frappe
from frappe.model.document import Document


class RBPTenant(Document):
	"""Tenant workspace record for the RBP platform layer."""

	def validate(self):
		if self.owner_user and not self.tenant_name:
			self.tenant_name = self.owner_user
