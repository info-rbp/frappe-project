import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const sidebarNav = [
  { label: "Dashboard", url: "/portal/dashboard" },
  { label: "Membership", url: "/portal/membership" },
  { label: "Library", url: "/portal/library" },
  { label: "Resources", url: "/portal/resources" },
  { label: "Finance", url: "/portal/finance" },
  { label: "Decision Desk", url: "/portal/decision-desk" },
  { label: "Billing", url: "/portal/billing" },
  { label: "Account", url: "/portal/account" },
  { label: "Notifications", url: "/portal/notifications" },
  { label: "Support", url: "/portal/support" },
];

export default function PortalShell({ children, pageTitle = "Portal" }) {
  const location = useLocation();
  const isActive = (url) => location.pathname === url || location.pathname.startsWith(url + "/");

  return (
    <div className="rbp-portal" data-testid="rbp-portal-shell">
      <aside className="rbp-portal-side" data-testid="rbp-portal-sidebar">
        <div className="rbp-portal-side-logo">
          <Link to="/">RBP</Link>
        </div>
        <nav data-testid="rbp-portal-nav">
          {sidebarNav.map(item => (
            <Link key={item.url} to={item.url} className={isActive(item.url) ? "active" : ""}>
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="rbp-portal-side-footer">
          <Link to="/" className="rbp-portal-side-link" data-testid="portal-to-public">Back to Website</Link>
          <Link to="/login" className="rbp-portal-side-link logout" data-testid="portal-logout">Sign Out</Link>
        </div>
      </aside>

      <div className="rbp-portal-body">
        <div className="rbp-portal-topbar" data-testid="rbp-portal-header">
          <span>Remote Business Partner</span>
          <div className="rbp-portal-topbar-links">
            <Link to="/" data-testid="portal-topbar-site">Website</Link>
            <Link to="/portal/account" data-testid="portal-topbar-account">Account</Link>
            <Link to="/login" className="rbp-portal-topbar-logout" data-testid="portal-topbar-logout">Sign Out</Link>
          </div>
        </div>
        <div className="rbp-portal-page-head">
          <h1>{pageTitle}</h1>
        </div>
        <div className="rbp-portal-content" data-testid="rbp-portal-content">
          {children}
        </div>
      </div>
    </div>
  );
}
