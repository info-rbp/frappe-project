"""Document services for the RBP platform layer."""


def get_documents(user=None):
	"""Return a safe document placeholder until document DocTypes exist."""

	documents = []
	return {
		"documents": documents,
		"count": len(documents),
		"module_enabled": True,
	}


def get_documents_payload():
	"""Backward-compatible alias for the documents placeholder payload."""

	return get_documents()
