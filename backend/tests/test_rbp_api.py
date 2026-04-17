"""
RBP App Shell API Tests
Tests for health, navigation, and routes endpoints
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
        """Test /api/navigation returns utility nav items"""
        response = requests.get(f"{BASE_URL}/api/navigation")
        assert response.status_code == 200
        data = response.json()
        
        # Check utility nav exists
        assert "utility" in data
        utility = data["utility"]
        assert len(utility) == 3  # Search, Login, Join
        
        # Verify utility items
        labels = [item["label"] for item in utility]
        assert "Search" in labels
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


class TestRoutesEndpoint:
    """Routes endpoint tests"""
    
    def test_routes_returns_all_categories(self):
        """Test /api/routes returns all route categories"""
        response = requests.get(f"{BASE_URL}/api/routes")
        assert response.status_code == 200
        data = response.json()
        
        # Check all 4 route categories exist
        assert "public" in data
        assert "auth" in data
        assert "portal" in data
        assert "admin" in data
    
    def test_public_routes_count(self):
        """Test public routes has expected count"""
        response = requests.get(f"{BASE_URL}/api/routes")
        data = response.json()
        
        public = data["public"]
        assert len(public) >= 30  # At least 30 public routes
        
        # Verify key public routes exist
        assert "/" in public
        assert "/services" in public
        assert "/membership" in public
        assert "/finance" in public
        assert "/about" in public
        assert "/contact" in public
    
    def test_auth_routes(self):
        """Test auth routes are correct"""
        response = requests.get(f"{BASE_URL}/api/routes")
        data = response.json()
        
        auth = data["auth"]
        assert len(auth) == 6
        
        expected = ["/login", "/register", "/join", "/forgot-password", 
                   "/reset-password", "/verify-account"]
        for route in expected:
            assert route in auth
    
    def test_portal_routes(self):
        """Test portal routes are correct"""
        response = requests.get(f"{BASE_URL}/api/routes")
        data = response.json()
        
        portal = data["portal"]
        assert len(portal) >= 10  # At least 10 portal routes
        
        # Verify key portal routes
        assert "/portal" in portal
        assert "/portal/dashboard" in portal
        assert "/portal/membership" in portal
        assert "/portal/billing" in portal
    
    def test_admin_routes(self):
        """Test admin routes are correct"""
        response = requests.get(f"{BASE_URL}/api/routes")
        data = response.json()
        
        admin = data["admin"]
        assert len(admin) >= 10  # At least 10 admin routes
        
        # Verify key admin routes
        assert "/admin" in admin
        assert "/admin/services" in admin
        assert "/admin/users" in admin
