import frappe
from frappe import _

@frappe.whitelist()
def get_member_context():
    """
    Returns the membership context for the current user, 
    including their tier and allowed features.
    """
    user = frappe.session.user
    if user == "Guest":
        return {"status": "Guest", "features": []}

    subscription = frappe.get_all(
        "Membership Subscription",
        filters={"user": user, "status": "Active"},
        fields=["tier", "end_date"],
        order_by="creation desc",
        limit=1
    )

    if not subscription:
        return {"status": "No Active Membership", "features": []}

    tier = frappe.get_doc("Membership Tier", subscription[0].tier)
    
    features = []
    for f in tier.features:
        feature_doc = frappe.get_doc("Membership Feature", f.feature)
        features.append({
            "name": feature_doc.feature_name,
            "app": feature_doc.app_name,
            "route": feature_doc.route,
            "icon": feature_doc.icon
        })

    return {
        "status": "Active",
        "tier": tier.tier_name,
        "expiry": subscription[0].end_date,
        "features": features
    }

@frappe.whitelist()
def get_dashboard_summary():
    """
    Aggregates high-level summary from multiple apps for the portal dashboard.
    """
    context = get_member_context()
    if context.get("status") != "Active":
        return {"error": "Active membership required"}

    summary = {
        "apps": {}
    }

    # Example: Get Wiki updates if Wiki is enabled
    if any(f['name'] == 'Wiki' for f in context['features']):
        try:
            summary["apps"]["wiki"] = frappe.get_all(
                "Wiki Document", 
                limit=5, 
                order_by="modified desc",
                fields=["title", "name", "route"]
            )
        except Exception:
            pass

    # Example: Get LMS progress if LMS is enabled
    if any(f['name'] == 'Learning' for f in context['features']):
        try:
            # Placeholder for LMS logic
            summary["apps"]["lms"] = {"status": "Courses available"}
        except Exception:
            pass

    return summary

@frappe.whitelist()
def create_tier_upgrade_session(tier):
    """
    Creates a Stripe checkout session for upgrading to a selected tier.
    """
    context = get_member_context()
    user = frappe.session.user
    
    if context.get("status") == "Active" and context.get("tier") == tier:
        frappe.throw(_("You are already subscribed to the {0} tier").format(tier))

    tier_doc = frappe.get_doc("Membership Tier", tier)
    if tier_doc.monthly_rate <= 0:
        # For free tiers, just upgrade immediately
        return upgrade_membership(user, tier)

    # Stripe logic using payments app
    settings = frappe.get_single("Business Hub Settings")
    if not settings.stripe_settings:
        frappe.throw(_("Stripe integration is not configured in Business Hub Settings"))

    from payments.payment_gateways.stripe_integration import create_checkout_session
    
    # Mocking a simple payment object for the stripe_integration
    # In a full flow, you'd create a 'Payment Request' record.
    payload = {
        "amount": tier_doc.monthly_rate,
        "currency": "USD",
        "description": f"Subscription Upgrade to {tier}",
        "payer_email": frappe.db.get_value("User", user, "email"),
        "success_url": frappe.utils.get_url("/portal?status=success"),
        "cancel_url": frappe.utils.get_url("/portal?status=cancel"),
    }
    
    return create_checkout_session(settings.stripe_settings, payload)

def upgrade_membership(user, tier):
    # Deactivate existing
    frappe.db.set_value("Membership Subscription", {"user": user, "status": "Active"}, "status", "Expired")
    
    # Create new
    frappe.get_doc({
        "doctype": "Membership Subscription",
        "user": user,
        "tier": tier,
        "status": "Active",
        "start_date": frappe.utils.today()
    }).insert()
    
    frappe.db.commit()
    return {"status": "Success", "message": f"Upgraded to {tier}"}

def check_wiki_permission(doc, ptype, user):
    """
    Check if the user has permission to access Wiki based on their membership tier.
    """
    context = get_member_context()
    if context.get("status") != "Active":
        return False
    
    # Check if 'Wiki' is in enabled features
    return any(f['name'] == 'Wiki' for f in context['features'])
