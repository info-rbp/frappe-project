from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RBP App Shell API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "rbp_app", "version": "0.1.0"}


@app.get("/api/navigation")
def get_navigation():
    return {
        "primary": [
            {"label": "Home", "url": "/", "section": "home"},
            {"label": "Services", "url": "/services", "section": "services"},
            {"label": "Membership", "url": "/membership", "section": "membership"},
            {"label": "Resources", "url": "/resources", "section": "resources"},
            {"label": "Finance", "url": "/finance", "section": "finance"},
            {"label": "Offers", "url": "/offers", "section": "offers"},
            {"label": "Decision Desk", "url": "/decision-desk", "section": "decision-desk"},
            {"label": "Documents", "url": "/documents", "section": "documents"},
            {"label": "Help", "url": "/help", "section": "help"},
        ],
        "utility": [
            {"label": "Search", "url": "/resources/search", "action": "search"},
            {"label": "My Portal", "url": "/portal/dashboard", "action": "portal"},
            {"label": "Login", "url": "/login", "action": "login"},
            {"label": "Join / Get Started", "url": "/join", "action": "join", "highlight": True},
        ],
    }


@app.get("/api/architecture")
def get_architecture():
    """Complete application shell architecture document."""
    return {
        "app_owner": "rbp_app",
        "description": "Remote Business Partner - Custom Frappe Application Shell",
        "framework": "Frappe v17",
        "shells": {
            "public": {
                "name": "Public Website",
                "template": "rbp_app/templates/shells/public_base.html",
                "description": "Guest-facing pages with full navigation, header, footer.",
                "access": "Unauthenticated",
                "transitions_to": ["auth", "portal"],
                "route_count": 38,
                "route_prefix": ["/", "/about", "/contact", "/services", "/membership",
                                 "/resources", "/finance", "/offers", "/decision-desk",
                                 "/documents", "/support", "/help", "/faq", "/privacy", "/terms"],
            },
            "auth": {
                "name": "Auth Layer",
                "template": "rbp_app/templates/shells/auth_base.html",
                "description": "Minimal chrome for identity: login, register, password flows.",
                "access": "Unauthenticated (redirects if already logged in)",
                "transitions_to": ["public", "portal"],
                "route_count": 6,
                "route_prefix": ["/login", "/register", "/join", "/forgot-password",
                                 "/reset-password", "/verify-account"],
            },
            "portal": {
                "name": "Member Portal",
                "template": "rbp_app/templates/shells/portal_base.html",
                "description": "Sidebar-driven dashboard for authenticated members.",
                "access": "Authenticated members only",
                "transitions_to": ["public", "auth", "admin"],
                "route_count": 13,
                "route_prefix": ["/portal"],
            },
            "admin": {
                "name": "Admin / Desk",
                "template": "rbp_app/templates/shells/admin_base.html",
                "description": "Scaffold pointing to Frappe Desk for content management.",
                "access": "Admin/staff roles via Frappe permissions",
                "transitions_to": ["portal", "public"],
                "production_surface": "/desk (Frappe Desk)",
                "route_count": 13,
                "route_prefix": ["/admin"],
            },
        },
        "boundaries": {
            "public_to_auth": "Login/Join buttons in header utility nav",
            "auth_to_portal": "Successful login redirects to /portal/dashboard",
            "portal_to_public": "Back to Website link in sidebar and topbar",
            "portal_to_admin": "Admin link in sidebar footer and topbar (role-gated)",
            "admin_to_portal": "Portal link in admin bar",
            "admin_to_desk": "In production, /admin routes map to /desk (Frappe Desk)",
        },
        "frappe_integration": {
            "hooks": "web_include_css, web_include_js, website_route_rules",
            "templates": "Shell templates extend frappe/templates/base.html",
            "www_pages": "Filesystem-driven routing via rbp_app/www/",
            "admin_strategy": "Frappe Desk (documented in ADMIN_APPROACH.md)",
            "core_modifications": "Zero",
        },
        "routes": {
            "public": [
                "/", "/about", "/contact", "/help", "/faq", "/privacy", "/terms",
                "/services", "/services/<category>", "/service/<slug>",
                "/membership", "/membership/plans", "/membership/pro",
                "/membership/ultimate", "/membership/compare",
                "/resources", "/resources/search", "/resources/<category>",
                "/resources/<category>/<slug>",
                "/finance", "/finance/funding", "/finance/insurance",
                "/finance/calculators", "/finance/learn", "/finance/resources",
                "/finance/enquiry", "/finance/thank-you",
                "/offers", "/offers/<slug>",
                "/decision-desk", "/decision-desk/how-it-works",
                "/decision-desk/request", "/decision-desk/thank-you",
                "/documents", "/templates", "/toolkits", "/documentation-suites",
                "/product/<slug>",
                "/support", "/support/contact", "/support/help-articles",
            ],
            "auth": [
                "/login", "/register", "/join", "/forgot-password",
                "/reset-password", "/verify-account",
            ],
            "portal": [
                "/portal", "/portal/dashboard", "/portal/membership",
                "/portal/library", "/portal/resources",
                "/portal/finance", "/portal/finance/enquiries",
                "/portal/decision-desk", "/portal/decision-desk/history",
                "/portal/billing", "/portal/account",
                "/portal/notifications", "/portal/support",
            ],
            "admin": [
                "/admin", "/admin/content", "/admin/services",
                "/admin/resources", "/admin/finance", "/admin/offers",
                "/admin/decision-desk", "/admin/documents",
                "/admin/memberships", "/admin/billing",
                "/admin/users", "/admin/navigation", "/admin/settings",
            ],
        },
    }
