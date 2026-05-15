"""Seed a launch-safe QA application catalogue for Milestone 4.

This patch is intentionally idempotent. It creates or updates a small admin-managed
Applications catalogue while keeping customer provisioning disabled.
"""

from __future__ import annotations

import frappe


CATEGORY_SEEDS = [
    {
        "category_name": "Operations",
        "category_key": "operations",
        "description": "Operational tools and workflow support services.",
        "public_summary": "Operations applications and workflow support.",
        "sort_order": 10,
        "enabled": 1,
    },
    {
        "category_name": "Human Resources",
        "category_key": "human_resources",
        "description": "People operations, onboarding, and HR administration.",
        "public_summary": "HR-focused applications and support tooling.",
        "sort_order": 20,
        "enabled": 1,
    },
    {
        "category_name": "Admin and Finance",
        "category_key": "admin_finance",
        "description": "Administrative, finance, and back-office business tools.",
        "public_summary": "Admin and finance application options.",
        "sort_order": 30,
        "enabled": 1,
    },
]

APPLICATION_SEEDS = [
    {
        "application_name": "CRM",
        "application_key": "crm",
        "category": "operations",
        "description": "A launch-safe placeholder for customer relationship management support and setup.",
        "short_description": "CRM setup and support pathway.",
        "status": "register_interest",
        "visibility": "public",
        "provider": "frappe",
        "installed_app_key": "crm",
        "public_summary": "Register interest for CRM implementation and support.",
        "portal_summary": "Interest-only CRM setup path for members and clients.",
        "sort_order": 10,
        "requires_subscription": 0,
        "requires_manual_approval": 1,
        "provisioning_enabled": 0,
        "interest_enabled": 1,
        "archived": 0,
    },
    {
        "application_name": "HR Management",
        "application_key": "hr_management",
        "category": "human_resources",
        "description": "A launch-safe placeholder for HR workflows, employee administration, and onboarding support.",
        "short_description": "HR administration and onboarding support.",
        "status": "register_interest",
        "visibility": "public",
        "provider": "frappe",
        "installed_app_key": "hrms",
        "public_summary": "Register interest for HR management application setup.",
        "portal_summary": "Interest-only HR setup path for members and clients.",
        "sort_order": 20,
        "requires_subscription": 0,
        "requires_manual_approval": 1,
        "provisioning_enabled": 0,
        "interest_enabled": 1,
        "archived": 0,
    },
    {
        "application_name": "Finance Automation",
        "application_key": "finance_automation",
        "category": "admin_finance",
        "description": "A launch-safe placeholder for finance workflow and back-office automation support.",
        "short_description": "Finance workflow setup and advisory support.",
        "status": "available_later",
        "visibility": "public",
        "provider": "manual",
        "installed_app_key": "",
        "public_summary": "Available later. Register interest for finance workflow support.",
        "portal_summary": "Interest-only finance automation path for members and clients.",
        "sort_order": 30,
        "requires_subscription": 0,
        "requires_manual_approval": 1,
        "provisioning_enabled": 0,
        "interest_enabled": 1,
        "archived": 0,
    },
]


def _doctype_exists(doctype):
    try:
        return bool(frappe.db.exists("DocType", doctype))
    except Exception:
        return False


def _set_if_supported(doc, fieldname, value):
    if value is None:
        return
    if hasattr(doc, fieldname):
        setattr(doc, fieldname, value)


def _upsert_category(values):
    name = frappe.db.get_value(
        "RBP Application Category",
        {"category_key": values["category_key"]},
        "name",
    )

    if name:
        doc = frappe.get_doc("RBP Application Category", name)
    else:
        doc = frappe.new_doc("RBP Application Category")

    for fieldname, value in values.items():
        _set_if_supported(doc, fieldname, value)

    if doc.is_new():
        doc.insert(ignore_permissions=True)
    else:
        doc.save(ignore_permissions=True)

    return doc


def _upsert_application(values):
    name = frappe.db.get_value(
        "RBP Application",
        {"application_key": values["application_key"]},
        "name",
    )

    if name:
        doc = frappe.get_doc("RBP Application", name)
    else:
        doc = frappe.new_doc("RBP Application")

    for fieldname, value in values.items():
        _set_if_supported(doc, fieldname, value)

    doc.provisioning_enabled = 0
    doc.interest_enabled = 1
    doc.requires_manual_approval = 1

    if doc.is_new():
        doc.insert(ignore_permissions=True)
    else:
        doc.save(ignore_permissions=True)

    return doc


def execute():
    if not _doctype_exists("RBP Application Category") or not _doctype_exists("RBP Application"):
        return

    for category in CATEGORY_SEEDS:
        _upsert_category(category)

    for application in APPLICATION_SEEDS:
        _upsert_application(application)
