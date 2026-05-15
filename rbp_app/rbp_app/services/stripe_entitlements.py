"""Stripe-specific subscription entitlement sync helpers."""

from __future__ import annotations

import frappe
from frappe.utils import getdate

from rbp_app.services.audit import record_audit_event
from rbp_app.services.tenancy import doctype_exists


def _parse_app_keys(value):
    if not value:
        return []
    return [item.strip().lower() for item in str(value).replace(",", "\n").splitlines() if item.strip()]


def _plan_for_subscription(subscription):
    plan_code = getattr(subscription, "plan", None)
    if not plan_code or not doctype_exists("RBP Membership Plan"):
        return None
    if frappe.db.exists("RBP Membership Plan", plan_code):
        return frappe.get_doc("RBP Membership Plan", plan_code)
    name = frappe.db.get_value("RBP Membership Plan", {"plan_code": plan_code}, "name")
    return frappe.get_doc("RBP Membership Plan", name) if name else None


def sync_entitlements_for_subscription(subscription, *, active=True, status=None):
    """Create or update app entitlements from a subscription's included apps."""

    if not doctype_exists("RBP App Entitlement"):
        return []

    plan = _plan_for_subscription(subscription)
    app_keys = _parse_app_keys(getattr(plan, "included_apps", None)) if plan else []
    if not app_keys:
        return []

    entitlement_status = status or ("Active" if active else "Suspended")
    enabled = 1 if active else 0
    synced = []

    for app_key in app_keys:
        filters = {
            "source_subscription": subscription.name,
            "app_key": app_key,
        }
        existing = frappe.db.get_value("RBP App Entitlement", filters, "name")
        if existing:
            doc = frappe.get_doc("RBP App Entitlement", existing)
        else:
            doc = frappe.get_doc(
                {
                    "doctype": "RBP App Entitlement",
                    "tenant": getattr(subscription, "tenant", None),
                    "user": getattr(subscription, "member", None),
                    "app_key": app_key,
                    "app_label": app_key.replace("_", " ").replace("-", " ").title(),
                    "source_app": app_key,
                    "app_category": "Platform",
                    "module_type": "RBP Platform Module",
                    "entitlement_type": "Tenant" if getattr(subscription, "tenant", None) else "User",
                    "source_subscription": subscription.name,
                }
            )

        doc.tenant = getattr(subscription, "tenant", None)
        doc.user = getattr(subscription, "member", None)
        doc.status = entitlement_status
        doc.enabled = enabled
        doc.visible_in_launcher = enabled
        doc.plan_required = getattr(subscription, "plan", None)
        doc.starts_on = (
            getdate(getattr(subscription, "current_period_start", None))
            if getattr(subscription, "current_period_start", None)
            else None
        )
        doc.ends_on = (
            getdate(getattr(subscription, "current_period_end", None))
            if getattr(subscription, "current_period_end", None)
            else None
        )
        doc.notes = f"Synced from subscription {subscription.name}."
        doc.save(ignore_permissions=True) if getattr(doc, "name", None) else doc.insert(ignore_permissions=True)
        synced.append(doc.name)

    record_audit_event(
        "subscription_entitlements_synced",
        actor="Stripe",
        tenant=getattr(subscription, "tenant", None),
        subject_doctype="RBP Subscription",
        subject_name=subscription.name,
        message="Subscription entitlements synced.",
        metadata={"entitlements": synced, "active": active, "status": entitlement_status},
    )
    return synced
