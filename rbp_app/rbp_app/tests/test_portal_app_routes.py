from unittest import TestCase

from rbp_app import hooks


class TestPortalAppRoutes(TestCase):
    def test_portal_app_routes_use_dedicated_pages(self):
        self.assertIn(
            {"from_route": "/portal/apps", "to_route": "portal/apps/index"},
            hooks.website_route_rules,
        )
        self.assertIn(
            {"from_route": "/portal/apps/<app_key>", "to_route": "portal/apps/app"},
            hooks.website_route_rules,
        )
        self.assertNotIn(
            {"from_route": "/portal/apps/<app_key>", "to_route": "portal/dashboard"},
            hooks.website_route_rules,
        )
