"""
RBP Navigation Configuration

Centralised navigation structure for the RBP public website.
Used by shell templates (header, mega_menu, footer) to render navigation.
"""


def get_primary_nav():
    """Primary navigation items shown in the main header bar."""
    return [
        {"label": "Home", "url": "/", "section": "home"},
        {"label": "Services", "url": "/services", "section": "services"},
        {"label": "Membership", "url": "/membership", "section": "membership"},
        {"label": "Resources", "url": "/resources", "section": "resources"},
        {"label": "Finance", "url": "/finance", "section": "finance"},
        {"label": "Offers", "url": "/offers", "section": "offers"},
        {"label": "Decision Desk", "url": "/decision-desk", "section": "decision-desk"},
        {"label": "Documents", "url": "/documents", "section": "documents"},
        {"label": "Help", "url": "/help", "section": "help"},
    ]


def get_utility_nav():
    """Utility actions shown in the header (login, join, search)."""
    return [
        {"label": "Search", "url": "/resources/search", "action": "search"},
        {"label": "Login", "url": "/login", "action": "login"},
        {"label": "Join / Get Started", "url": "/signup", "action": "join", "highlight": True},
    ]


def get_footer_nav():
    """Footer navigation groups."""
    return {
        "company": [
            {"label": "About", "url": "/about"},
            {"label": "Contact", "url": "/contact"},
            {"label": "Privacy", "url": "/privacy"},
            {"label": "Terms", "url": "/terms"},
        ],
        "services": [
            {"label": "All Services", "url": "/services"},
            {"label": "Membership", "url": "/membership"},
            {"label": "Finance", "url": "/finance"},
            {"label": "Offers", "url": "/offers"},
        ],
        "resources": [
            {"label": "Resource Library", "url": "/resources"},
            {"label": "Documents", "url": "/documents"},
            {"label": "Decision Desk", "url": "/decision-desk"},
        ],
        "support": [
            {"label": "Help Centre", "url": "/help"},
            {"label": "Support", "url": "/support"},
            {"label": "FAQ", "url": "/faq"},
            {"label": "Contact Support", "url": "/support/contact"},
        ],
    }


def get_portal_sidebar_nav():
    """Portal sidebar navigation for authenticated members."""
    return [
        {"label": "Dashboard", "url": "/portal/dashboard", "icon": "grid"},
        {"label": "Membership", "url": "/portal/membership", "icon": "users"},
        {"label": "Library", "url": "/portal/library", "icon": "book"},
        {"label": "Resources", "url": "/portal/resources", "icon": "folder"},
        {
            "label": "Finance",
            "url": "/portal/finance",
            "icon": "dollar-sign",
            "children": [
                {"label": "Overview", "url": "/portal/finance"},
                {"label": "Enquiries", "url": "/portal/finance/enquiries"},
            ],
        },
        {
            "label": "Decision Desk",
            "url": "/portal/decision-desk",
            "icon": "clipboard",
            "children": [
                {"label": "Overview", "url": "/portal/decision-desk"},
                {"label": "History", "url": "/portal/decision-desk/history"},
            ],
        },
        {"label": "Billing", "url": "/portal/billing", "icon": "credit-card"},
        {"label": "Account", "url": "/portal/account", "icon": "settings"},
        {"label": "Notifications", "url": "/portal/notifications", "icon": "bell"},
        {"label": "Support", "url": "/portal/support", "icon": "help-circle"},
    ]
