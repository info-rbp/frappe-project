import React from 'react';
import { Link } from 'react-router-dom';
import ShellNavigator from './ShellNavigator';

export default function AdminShell({ children }) {
  return (
    <div className="rbp-admin-wrap" data-testid="rbp-admin-shell-scaffold">
      <ShellNavigator />
      <div className="rbp-admin-bar">
        <div className="rbp-admin-bar-left">
          <span className="rbp-admin-bar-title">RBP Admin</span>
          <span className="rbp-admin-bar-badge">Scaffold</span>
        </div>
        <div className="rbp-admin-bar-links">
          <Link to="/" data-testid="admin-to-public">Public Site</Link>
          <Link to="/portal/dashboard" data-testid="admin-to-portal">Member Portal</Link>
          <Link to="/login" data-testid="admin-to-logout">Logout</Link>
        </div>
      </div>
      <div className="rbp-admin-body">
        <div className="rbp-admin-notice" data-testid="admin-desk-notice">
          <strong>Admin Shell Scaffold</strong><br />
          Admin functionality for RBP is delivered through <strong>Frappe Desk</strong> &mdash;
          workspaces, list views, and form views. These placeholder pages document the target
          admin structure. In production, <code>/desk</code> serves all admin surfaces.
          <div className="rbp-admin-notice-links">
            <Link to="/portal/dashboard">Go to Portal</Link>
            <Link to="/">Go to Public Site</Link>
            <Link to="/architecture">View Architecture Map</Link>
          </div>
        </div>
        {children}
      </div>
    </div>
  );
}
