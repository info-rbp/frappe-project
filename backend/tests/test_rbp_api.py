"""
RBP App Shell API Tests
Tests for health, navigation, and architecture endpoints
"""
import pytest
import requests
import os

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')


class TestHealthEndpoint:
    """Health check endpoint tests"""
    
    def test_health_returns_ok(self):
        """Test /api/health returns status ok"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["app"] == "rbp_app"
        assert "version" in data


class TestNavigationEndpoint:
    """Navigation endpoint tests"""
    
    def test_navigation_returns_primary_items(self):
        """Test /api/navigation returns primary nav items"""
        response = requests.get(f"{BASE_URL}/api/navigation")
        assert response.status_code == 200
        data = response.json()
        
        # Check primary nav exists
        assert "primary" in data
        primary = data["primary"]
        assert len(primary) == 9  # 9 primary nav items
        
        # Verify expected nav items
        labels = [item["label"] for item in primary]
        expected = ["Home", "Services", "Membership", "Resources", "Finance", 
                   "Offers", "Decision Desk", "Documents", "Help"]
        assert labels == expected
    
    def test_navigation_returns_utility_items(self):
        """Test /api/navigation returns utility nav items with My Portal"""
        response = requests.get(f"{BASE_URL}/api/navigation")
        assert response.status_code == 200
        data = response.json()
        
        # Check utility nav exists
        assert "utility" in data
        utility = data["utility"]
        assert len(utility) == 4  # Search, My Portal, Login, Join
        
        # Verify utility items including My Portal
        labels = [item["label"] for item in utility]
        assert "Search" in labels
        assert "My Portal" in labels
        assert "Login" in labels
        assert "Join / Get Started" in labels
    
    def test_navigation_item_structure(self):
        """Test navigation items have correct structure"""
        response = requests.get(f"{BASE_URL}/api/navigation")
        data = response.json()
        
        # Check primary item structure
        for item in data["primary"]:
            assert "label" in item
            assert "url" in item
            assert "section" in item
        
        # Check utility item structure
        for item in data["utility"]:
            assert "label" in item
            assert "url" in item
            assert "action" in item


class TestArchitectureEndpoint:
    """Architecture endpoint tests - shell definitions, boundaries, and routes"""
    
    def test_architecture_returns_app_owner(self):
        """Test /api/architecture returns app owner info"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        assert response.status_code == 200
        data = response.json()
        
        assert data["app_owner"] == "rbp_app"
        assert "description" in data
        assert data["framework"] == "Frappe v17"
    
    def test_architecture_returns_all_shells(self):
        """Test /api/architecture returns all 4 shell definitions"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        assert response.status_code == 200
        data = response.json()
        
        # Check all 4 shells exist
        assert "shells" in data
        shells = data["shells"]
        assert "public" in shells
        assert "auth" in shells
        assert "portal" in shells
        assert "admin" in shells
    
    def test_architecture_shell_structure(self):
        """Test each shell has correct structure"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        for shell_id, shell in data["shells"].items():
            assert "name" in shell
            assert "template" in shell
            assert "description" in shell
            assert "access" in shell
            assert "transitions_to" in shell
            assert "route_count" in shell
            assert "route_prefix" in shell
    
    def test_architecture_shell_transitions(self):
        """Test shell transitions are correctly defined"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        shells = data["shells"]
        
        # Public transitions to auth and portal
        assert "auth" in shells["public"]["transitions_to"]
        assert "portal" in shells["public"]["transitions_to"]
        
        # Auth transitions to public and portal
        assert "public" in shells["auth"]["transitions_to"]
        assert "portal" in shells["auth"]["transitions_to"]
        
        # Portal transitions to public, auth, and admin
        assert "public" in shells["portal"]["transitions_to"]
        assert "auth" in shells["portal"]["transitions_to"]
        assert "admin" in shells["portal"]["transitions_to"]
        
        # Admin transitions to portal and public
        assert "portal" in shells["admin"]["transitions_to"]
        assert "public" in shells["admin"]["transitions_to"]
    
    def test_architecture_returns_boundaries(self):
        """Test /api/architecture returns shell boundaries"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        assert "boundaries" in data
        boundaries = data["boundaries"]
        
        # Check key boundary definitions
        assert "public_to_auth" in boundaries
        assert "auth_to_portal" in boundaries
        assert "portal_to_public" in boundaries
        assert "portal_to_admin" in boundaries
        assert "admin_to_portal" in boundaries
    
    def test_architecture_returns_routes(self):
        """Test /api/architecture returns complete route structure"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        assert "routes" in data
        routes = data["routes"]
        
        # Check all 4 route categories exist
        assert "public" in routes
        assert "auth" in routes
        assert "portal" in routes
        assert "admin" in routes
    
    def test_architecture_public_routes(self):
        """Test public routes are complete"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        public = data["routes"]["public"]
        assert len(public) >= 30  # At least 30 public routes
        
        # Verify key public routes exist
        assert "/" in public
        assert "/services" in public
        assert "/membership" in public
        assert "/membership/plans" in public
        assert "/finance" in public
        assert "/finance/funding" in public
        assert "/decision-desk" in public
        assert "/documents" in public
    
    def test_architecture_auth_routes(self):
        """Test auth routes are correct"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        auth = data["routes"]["auth"]
        assert len(auth) == 6
        
        expected = ["/login", "/register", "/join", "/forgot-password", 
                   "/reset-password", "/verify-account"]
        for route in expected:
            assert route in auth
    
    def test_architecture_portal_routes(self):
        """Test portal routes are correct"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        portal = data["routes"]["portal"]
        assert len(portal) >= 10  # At least 10 portal routes
        
        # Verify key portal routes
        assert "/portal" in portal
        assert "/portal/dashboard" in portal
        assert "/portal/membership" in portal
        assert "/portal/billing" in portal
        assert "/portal/account" in portal
    
    def test_architecture_admin_routes(self):
        """Test admin routes are correct"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        admin = data["routes"]["admin"]
        assert len(admin) >= 10  # At least 10 admin routes
        
        # Verify key admin routes
        assert "/admin" in admin
        assert "/admin/services" in admin
        assert "/admin/users" in admin
    
    def test_architecture_frappe_integration(self):
        """Test Frappe integration info is present"""
        response = requests.get(f"{BASE_URL}/api/architecture")
        data = response.json()
        
        assert "frappe_integration" in data
        integration = data["frappe_integration"]
        
        assert "hooks" in integration
        assert "templates" in integration
        assert "core_modifications" in integration
        assert integration["core_modifications"] == "Zero"
