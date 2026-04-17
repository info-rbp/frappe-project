import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import ShellNavigator from './ShellNavigator';

const navItems = [
  { label: "Home", url: "/" },
  { label: "Services", url: "/services" },
  { label: "Membership", url: "/membership" },
  { label: "Resources", url: "/resources" },
  { label: "Finance", url: "/finance" },
  { label: "Offers", url: "/offers" },
  { label: "Decision Desk", url: "/decision-desk" },
  { label: "Documents", url: "/documents" },
  { label: "Help", url: "/help" },
];

const footerGroups = {
  Company: [
    { label: "About", url: "/about" },
    { label: "Contact", url: "/contact" },
    { label: "Privacy Policy", url: "/privacy" },
    { label: "Terms of Service", url: "/terms" },
  ],
  Services: [
    { label: "All Services", url: "/services" },
    { label: "Membership", url: "/membership" },
    { label: "Finance", url: "/finance" },
    { label: "Offers", url: "/offers" },
  ],
  Resources: [
    { label: "Resource Library", url: "/resources" },
    { label: "Documents", url: "/documents" },
    { label: "Decision Desk", url: "/decision-desk" },
  ],
  Support: [
    { label: "Help Centre", url: "/help" },
    { label: "Support", url: "/support" },
    { label: "FAQ", url: "/faq" },
    { label: "Contact Support", url: "/support/contact" },
  ],
};

export default function PublicShell({ children }) {
  const location = useLocation();
  const isActive = (url) => {
    if (url === "/") return location.pathname === "/";
    return location.pathname.startsWith(url);
  };

  return (
    <div data-testid="rbp-public-shell">
      <ShellNavigator />
      <header className="rbp-header" data-testid="rbp-header">
        <div className="rbp-header-inner">
          <Link to="/" className="rbp-logo" data-testid="rbp-logo">RBP</Link>
          <nav className="rbp-nav" data-testid="rbp-primary-nav">
            {navItems.map(item => (
              <Link key={item.url} to={item.url} className={isActive(item.url) ? "active" : ""}>
                {item.label}
              </Link>
            ))}
          </nav>
          <div className="rbp-utility" data-testid="rbp-utility-nav">
            <Link to="/resources/search" data-testid="utility-search">Search</Link>
            <Link to="/portal/dashboard" className="rbp-utility-portal" data-testid="utility-portal">My Portal</Link>
            <Link to="/login" data-testid="utility-login">Login</Link>
            <Link to="/join" className="rbp-btn-cta" data-testid="join-cta">Join / Get Started</Link>
          </div>
        </div>
      </header>

      <main>{children}</main>

      <footer className="rbp-footer" data-testid="rbp-footer">
        <div className="rbp-footer-inner">
          <div className="rbp-footer-grid">
            {Object.entries(footerGroups).map(([group, links]) => (
              <div className="rbp-footer-group" key={group}>
                <h4>{group}</h4>
                {links.map(l => <Link key={l.url} to={l.url}>{l.label}</Link>)}
              </div>
            ))}
            <div className="rbp-footer-group">
              <h4>Account</h4>
              <Link to="/login">Login</Link>
              <Link to="/join">Join / Get Started</Link>
              <Link to="/portal/dashboard">Member Portal</Link>
              <Link to="/admin">Admin</Link>
            </div>
          </div>
          <div className="rbp-footer-bottom">
            &copy; {new Date().getFullYear()} Remote Business Partner. All rights reserved.
            <span className="rbp-footer-app-tag">Powered by <code>rbp_app</code> on Frappe</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
