from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

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
            {"label": "Login", "url": "/login", "action": "login"},
            {"label": "Join / Get Started", "url": "/join", "action": "join", "highlight": True},
        ],
    }


@app.get("/api/routes")
def get_routes():
    return {
        "public": [
            "/", "/about", "/contact", "/help", "/faq", "/privacy", "/terms",
            "/services", "/membership", "/membership/plans", "/membership/pro",
            "/membership/ultimate", "/membership/compare",
            "/resources", "/resources/search",
            "/finance", "/finance/funding", "/finance/insurance",
            "/finance/calculators", "/finance/learn", "/finance/resources",
            "/finance/enquiry", "/finance/thank-you",
            "/offers", "/decision-desk", "/decision-desk/how-it-works",
            "/decision-desk/request", "/decision-desk/thank-you",
            "/documents", "/templates", "/toolkits", "/documentation-suites",
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
    }
