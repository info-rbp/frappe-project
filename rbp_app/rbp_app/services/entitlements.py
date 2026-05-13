"""Entitlement enforcement services for RBP apps and capabilities."""

import frappe
from frappe.utils import getdate, nowdate

from rbp_app.permissions import get_user_roles, is_admin_user
from rbp_app.services.tenancy import doctype_exists, get_current_tenant_name


ACTIVE_STATUSES = {"Active"}


def _parse_roles(value):
    if not value:
        return set()
    return {item.strip() for item in value.replace(",", "\n").splitlines() if item.strip()}


def _within_date_window(row):
    today = getdate(nowdate())
    starts_on = row.get("starts_on")
    ends_on = row.get("ends_on")

    if starts_on and getdate(starts_on) > today:
        return False

    if ends_on and getdate(ends_on) < today:
        return False

    return True


def _entitlement_rows(app_key=None, user=None):
    if not doctype_exists("RBP App Entitlement"):
        return []

    filters = {
        "enabled": 1,
        "status": ["in", list(ACTIVE_STATUSES)],
    }

    if app_key:
        filters["app_key"] = app_key.strip().lower()

    try:
        return frappe.get_all(
            "RBP App Entitlement",
            filters=filters,
            fields=[
                "name",
                "tenant",
                "user",
                "app_key",
                "app_label",
                "entitlement_type",
                "status",
                "enabled",
                "roles_allowed",
                "starts_on",
                "ends_on",
                "source_subscription",
            ],
        )
    except Exception:
        return []


def get_user_entitlements(user=None):
    user = user or frappe.session.user
    if not user or user == "Guest":
        return []

    if is_admin_user(user):
        return _entitlement_rows(user=user)

    tenant = get_current_tenant_name(user)
    roles = set(get_user_roles(user))
    rows = []

    for row in _entitlement_rows(user=user):
        if not _within_date_window(row):
            continue

        if row.get("user") and row.get("user") != user:
            continue

        if row.get("tenant") and tenant and row.get("tenant") != tenant:
            continue

        allowed_roles = _parse_roles(row.get("roles_allowed"))
        if allowed_roles and not roles.intersection(allowed_roles):
            continue

        rows.append(row)

    return rows


def user_has_entitlement(app_key, user=None):
    user = user or frappe.session.user
    app_key = (app_key or "").strip().lower()

    if not app_key or not user or user == "Guest":
        return False

    if is_admin_user(user):
        return True

    all_rows = _entitlement_rows(user=user)
    if not all_rows:
        # Scaffold-safe default: if no entitlement records exist yet, do not
        # block the portal. Once records exist, they become authoritative.
        return True

    return any(row.get("app_key") == app_key for row in get_user_entitlements(user))


def require_entitlement(app_key, user=None):
    if not user_has_entitlement(app_key, user):
        raise frappe.PermissionError

    return True

# --- Milestone 8: member benefit entitlement management ---

import json

from rbp_app.permissions import require_system_manager
from rbp_app.services.tenancy import doctype_exists, get_current_tenant_name


DISABLED_ENTITLEMENT_KEYS = {"applications_provisioning"}

MEMBERSHIP_ENTITLEMENT_KEYS = [
    "membership",
    "portal",
    "billing",
    "notifications",
    "offers",
    "resources",
    "documents",
    "decision_desk",
    "docushare",
    "marketplace",
    "connectivity",
    "risk_advisor",
    "fixer",
    "applications_interest",
]

ENTITLEMENT_CATALOG = {
    "membership": {"label": "Membership", "category": "Platform", "route": "/portal/dashboard", "visible": 1},
    "portal": {"label": "Member Portal", "category": "Platform", "route": "/portal/dashboard", "visible": 1},
    "billing": {"label": "Billing", "category": "Finance", "route": "/portal/settings", "visible": 1},
    "notifications": {"label": "Notifications", "category": "Platform", "route": "/portal/dashboard", "visible": 1},
    "offers": {"label": "Member Offers", "category": "Commerce", "route": "/portal/offers", "visible": 1},
    "resources": {"label": "Member Resources", "category": "Knowledge", "route": "/portal/resources", "visible": 1},
    "documents": {"label": "Documents", "category": "Documents", "route": "/portal/documents", "visible": 1},
    "decision_desk": {"label": "Decision Desk", "category": "Operations", "route": "/portal/services/decision-desk/start", "visible": 1},
    "docushare": {"label": "DocuShare", "category": "Documents", "route": "/portal/services/docushare/start", "visible": 1},
    "marketplace": {"label": "Marketplace", "category": "Commerce", "route": "/portal/marketplace/listings/new", "visible": 1},
    "connectivity": {"label": "Connectivity", "category": "Operations", "route": "/portal/services/nbn/start", "visible": 1},
    "risk_advisor": {"label": "Risk Advisor", "category": "Operations", "route": "/portal/services/risk-advisor/start", "visible": 1},
    "fixer": {"label": "The Fixer", "category": "Operations", "route": "/portal/services/the-fixer/start", "visible": 1},
    "applications_interest": {"label": "Applications Interest", "category": "Platform", "route": "/portal/apps", "visible": 1},
    "applications_provisioning": {"label": "Applications Provisioning", "category": "Platform", "route": "/portal/apps", "visible": 0},
}


def _normalize_entitlement_key(app_key):
    return (app_key or "").strip().lower().replace("-", "_").replace(" ", "_")


def _coerce_payload(payload):
    if payload is None:
        return {}
    if isinstance(payload, str):
        return json.loads(payload or "{}")
    if isinstance(payload, dict):
        return payload
    return dict(payload)


def _catalog_entry(app_key):
    return ENTITLEMENT_CATALOG.get(_normalize_entitlement_key(app_key), {})


def _serialize_entitlement_doc(doc):
    row = doc.as_dict() if hasattr(doc, "as_dict") else dict(doc)
    app_key = _normalize_entitlement_key(row.get("app_key"))
    catalog = _catalog_entry(app_key)

    return {
        "name": row.get("name"),
        "tenant": row.get("tenant"),
        "user": row.get("user"),
        "app_key": app_key,
        "app_label": row.get("app_label") or catalog.get("label") or app_key,
        "app_category": row.get("app_category") or catalog.get("category"),
        "module_type": row.get("module_type") or "RBP Platform Module",
        "entitlement_type": row.get("entitlement_type"),
        "status": row.get("status"),
        "enabled": bool(row.get("enabled")),
        "visible_in_launcher": bool(row.get("visible_in_launcher")),
        "route": row.get("route") or catalog.get("route"),
        "roles_allowed": row.get("roles_allowed"),
        "plan_required": row.get("plan_required"),
        "source_subscription": row.get("source_subscription"),
        "starts_on": row.get("starts_on"),
        "ends_on": row.get("ends_on"),
        "notes": row.get("notes"),
    }


def _entitlement_exists(app_key, user=None, tenant=None, source_subscription=None):
    filters = {"app_key": _normalize_entitlement_key(app_key)}

    if user:
        filters["user"] = user
    if tenant:
        filters["tenant"] = tenant
    if source_subscription:
        filters["source_subscription"] = source_subscription

    return frappe.db.exists("RBP App Entitlement", filters)


def grant_entitlement(
    app_key,
    user=None,
    tenant=None,
    entitlement_type="Tenant",
    source_subscription=None,
    starts_on=None,
    ends_on=None,
    plan_required=None,
    roles_allowed=None,
    notes=None,
    visible_in_launcher=None,
    ignore_disabled=False,
):
    app_key = _normalize_entitlement_key(app_key)

    if not app_key:
        raise frappe.ValidationError("Entitlement key is required.")

    if app_key in DISABLED_ENTITLEMENT_KEYS and not ignore_disabled:
        raise frappe.ValidationError(f"Entitlement '{app_key}' is disabled for this rollout.")

    if not doctype_exists("RBP App Entitlement"):
        raise frappe.ValidationError("RBP App Entitlement is not installed.")

    if not tenant and user:
        tenant = get_current_tenant_name(user)

    catalog = _catalog_entry(app_key)

    existing_name = _entitlement_exists(
        app_key=app_key,
        user=user,
        tenant=tenant,
        source_subscription=source_subscription,
    )

    if existing_name:
        doc = frappe.get_doc("RBP App Entitlement", existing_name)
    else:
        doc = frappe.get_doc({"doctype": "RBP App Entitlement"})

    doc.tenant = tenant
    doc.user = user
    doc.app_key = app_key
    doc.app_label = catalog.get("label") or app_key.replace("_", " ").title()
    doc.app_category = catalog.get("category") or "Platform"
    doc.module_type = catalog.get("module_type") or "RBP Platform Module"
    doc.entitlement_type = entitlement_type or "Tenant"
    doc.status = "Active"
    doc.enabled = 1
    doc.visible_in_launcher = visible_in_launcher if visible_in_launcher is not None else catalog.get("visible", 1)
    doc.route = catalog.get("route")
    doc.roles_allowed = roles_allowed
    doc.plan_required = plan_required
    doc.source_subscription = source_subscription
    doc.starts_on = starts_on
    doc.ends_on = ends_on
    doc.notes = notes

    if existing_name:
        doc.save(ignore_permissions=True)
    else:
        doc.insert(ignore_permissions=True)

    return _serialize_entitlement_doc(doc)


def revoke_entitlement(
    app_key,
    user=None,
    tenant=None,
    source_subscription=None,
    status="Suspended",
    notes=None,
):
    app_key = _normalize_entitlement_key(app_key)

    if not app_key:
        raise frappe.ValidationError("Entitlement key is required.")

    if not doctype_exists("RBP App Entitlement"):
        return []

    filters = {"app_key": app_key}

    if user:
        filters["user"] = user
    if tenant:
        filters["tenant"] = tenant
    if source_subscription:
        filters["source_subscription"] = source_subscription

    names = frappe.get_all("RBP App Entitlement", filters=filters, pluck="name")
    revoked = []

    for name in names:
        doc = frappe.get_doc("RBP App Entitlement", name)
        doc.status = status
        doc.enabled = 0
        if notes:
            doc.notes = notes
        doc.save(ignore_permissions=True)
        revoked.append(_serialize_entitlement_doc(doc))

    return revoked


def grant_membership_entitlements(
    subscription=None,
    user=None,
    tenant=None,
    plan=None,
    starts_on=None,
    ends_on=None,
):
    if isinstance(subscription, str):
        subscription = frappe.get_doc("RBP Subscription", subscription)

    if subscription:
        user = user or getattr(subscription, "user", None) or getattr(subscription, "member", None)
        tenant = tenant or getattr(subscription, "tenant", None)
        plan = plan or getattr(subscription, "plan", None)
        starts_on = starts_on or getattr(subscription, "current_period_start", None)
        ends_on = ends_on or getattr(subscription, "current_period_end", None)
        source_subscription = getattr(subscription, "name", None)
    else:
        source_subscription = None

    granted = []

    for key in MEMBERSHIP_ENTITLEMENT_KEYS:
        granted.append(
            grant_entitlement(
                app_key=key,
                user=user,
                tenant=tenant,
                entitlement_type="Plan",
                source_subscription=source_subscription,
                starts_on=starts_on,
                ends_on=ends_on,
                plan_required=plan,
                notes="Granted from active membership subscription.",
            )
        )

    return granted


def suspend_membership_entitlements(subscription=None, user=None, tenant=None, status="Suspended"):
    if isinstance(subscription, str):
        subscription = frappe.get_doc("RBP Subscription", subscription)

    source_subscription = None

    if subscription:
        user = user or getattr(subscription, "user", None) or getattr(subscription, "member", None)
        tenant = tenant or getattr(subscription, "tenant", None)
        source_subscription = getattr(subscription, "name", None)

    revoked = []

    for key in MEMBERSHIP_ENTITLEMENT_KEYS:
        revoked.extend(
            revoke_entitlement(
                app_key=key,
                user=user,
                tenant=tenant,
                source_subscription=source_subscription,
                status=status,
                notes=f"Membership entitlement {status.lower()} due to subscription state.",
            )
        )

    return revoked


def sync_subscription_entitlements(subscription):
    status = getattr(subscription, "status", None)
    payment_status = getattr(subscription, "payment_status", None)

    should_grant = status in {"Active", "Trial"} and payment_status in {
        None,
        "",
        "Not Required",
        "Authorised",
        "Paid",
    }

    if should_grant:
        granted = grant_membership_entitlements(subscription=subscription)
        return {"action": "granted", "entitlements": granted}

    inactive_status = "Suspended"

    if status == "Expired":
        inactive_status = "Expired"
    if status == "Cancelled":
        inactive_status = "Cancelled"

    suspended = suspend_membership_entitlements(subscription=subscription, status=inactive_status)

    return {"action": "suspended", "entitlements": suspended}


def has_entitlement(app_key, user=None):
    app_key = _normalize_entitlement_key(app_key)

    if app_key in DISABLED_ENTITLEMENT_KEYS:
        return False

    return user_has_entitlement(app_key, user=user)


def list_my_entitlements(user=None, include_inactive=False):
    rows = get_user_entitlements(user=user, include_inactive=include_inactive)
    active_keys = sorted(
        row.get("app_key")
        for row in rows
        if row.get("enabled") and row.get("status") == "Active" and row.get("app_key") not in DISABLED_ENTITLEMENT_KEYS
    )

    return {
        "entitlements": rows,
        "active_keys": active_keys,
        "disabled_keys": sorted(DISABLED_ENTITLEMENT_KEYS),
    }


def admin_grant_entitlement(payload=None, **kwargs):
    require_system_manager()
    data = _coerce_payload(payload)
    data.update({key: value for key, value in kwargs.items() if value is not None})

    return {
        "ok": True,
        "entitlement": grant_entitlement(
            app_key=data.get("app_key"),
            user=data.get("user"),
            tenant=data.get("tenant"),
            entitlement_type=data.get("entitlement_type") or "Tenant",
            source_subscription=data.get("source_subscription"),
            starts_on=data.get("starts_on"),
            ends_on=data.get("ends_on"),
            plan_required=data.get("plan_required"),
            roles_allowed=data.get("roles_allowed"),
            notes=data.get("notes") or "Granted manually by admin.",
            visible_in_launcher=data.get("visible_in_launcher"),
        ),
    }


def admin_revoke_entitlement(payload=None, **kwargs):
    require_system_manager()
    data = _coerce_payload(payload)
    data.update({key: value for key, value in kwargs.items() if value is not None})

    return {
        "ok": True,
        "revoked": revoke_entitlement(
            app_key=data.get("app_key"),
            user=data.get("user"),
            tenant=data.get("tenant"),
            source_subscription=data.get("source_subscription"),
            status=data.get("status") or "Suspended",
            notes=data.get("notes") or "Revoked manually by admin.",
        ),
    }


def entitlement_catalog():
    return {
        "keys": sorted(ENTITLEMENT_CATALOG.keys()),
        "membership_keys": list(MEMBERSHIP_ENTITLEMENT_KEYS),
        "disabled_keys": sorted(DISABLED_ENTITLEMENT_KEYS),
        "catalog": ENTITLEMENT_CATALOG,
    }
