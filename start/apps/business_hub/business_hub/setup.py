import frappe

def create_initial_data():
    # 1. Create Features
    features = [
        {"feature_name": "Wiki", "app_name": "wiki", "route": "/wiki", "icon": "file-text"},
        {"feature_name": "Learning", "app_name": "lms", "route": "/lms", "icon": "book"},
        {"feature_name": "Support", "app_name": "helpdesk", "route": "/helpdesk", "icon": "help-circle"}
    ]
    
    for f in features:
        if not frappe.db.exists("Membership Feature", f["feature_name"]):
            frappe.get_doc({"doctype": "Membership Feature", **f}).insert()

    # 2. Create Tiers
    if not frappe.db.exists("Membership Tier", "Bronze"):
        frappe.get_doc({
            "doctype": "Membership Tier",
            "tier_name": "Bronze",
            "monthly_rate": 0,
            "features": [{"feature": "Wiki"}]
        }).insert()

    if not frappe.db.exists("Membership Tier", "Gold"):
        frappe.get_doc({
            "doctype": "Membership Tier",
            "tier_name": "Gold",
            "monthly_rate": 100,
            "features": [{"feature": "Wiki"}, {"feature": "Learning"}, {"feature": "Support"}]
        }).insert()

    # 3. Create Subscription for Admin
    if not frappe.db.exists("Membership Subscription", {"user": "Administrator", "status": "Active"}):
        frappe.get_doc({
            "doctype": "Membership Subscription",
            "user": "Administrator",
            "tier": "Gold",
            "status": "Active",
            "start_date": frappe.utils.today()
        }).insert()

    frappe.db.commit()
