"""Document APIs for the RBP portal/frontend."""

import frappe

from rbp_app.permissions import require_login
from rbp_app.services.documents import get_documents as get_documents_service


@frappe.whitelist()
def get_documents():
	"""Return portal documents or a safe placeholder until DocTypes exist."""

	user = require_login()
	return get_documents_service(user)
