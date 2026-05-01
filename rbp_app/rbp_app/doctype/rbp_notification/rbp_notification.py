import frappe
from frappe.model.document import Document


class RBPNotification(Document):
	"""Portal notification addressed to a user."""

	def validate(self):
		if self.is_read and not self.read_on:
			self.read_on = frappe.utils.now_datetime()
