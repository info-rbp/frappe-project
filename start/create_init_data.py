import frappe

def create_initial_data():
    frappe.init(site="frappe.localhost", sites_path="sites")
    frappe.connect()
    frappe.set_user("Administrator")
    
    # 1. Create Features
    features = [
        {"feature_name": "Wiki", "app_name": "wiki", "route": "/wiki", "icon": "file-text"},
        {"feature_name": "Learning", "app_name": "lms", "route": "/lms", "icon": "book"},
        {"feature_name": "Support", "app_name": "helpdesk", "route": "/helpdesk", "icon": "help-circle"}
    ]
    
    for f in features:
        if not frappe.db.exists("Membership Feature", f["feature_name"]):
            frappe.get_doc({"doctype": "Membership Feature", **f}).insert()
            print(f"Created Feature: {f['feature_name']}")

    # 2. Create Tiers
    if not frappe.db.exists("Membership Tier", "Bronze"):
        bronze = frappe.get_doc({
            "doctype": "Membership Tier",
            "tier_name": "Bronze",
            "monthly_rate": 0,
            "features": [{"feature": "Wiki"}]
        })
        bronze.insert()
        print("Created Tier: Bronze")

    if not frappe.db.exists("Membership Tier", "Gold"):
        gold = frappe.get_doc({
            "doctype": "Membership Tier",
            "tier_name": "Gold",
            "monthly_rate": 100,
            "features": [{"feature": "Wiki"}, {"feature": "Learning"}, {"feature": "Support"}]
        })
        gold.insert()
        print("Created Tier: Gold")

    # 3. Create Subscription for Admin
    if not frappe.db.exists("Membership Subscription", {"user": "Administrator", "status": "Active"}):
        sub = frappe.get_doc({
            "doctype": "Membership Subscription",
            "user": "Administrator",
            "tier": "Gold",
            "status": "Active",
            "start_date": frappe.utils.today()
        })
        sub.insert()
        print("Created Subscription for Administrator")

    frappe.db.commit()

if __name__ == "__main__":
    create_initial_data()
