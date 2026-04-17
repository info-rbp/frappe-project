import React from 'react';
import { Link } from 'react-router-dom';

export default function AdminShell({ children }) {
  return (
    <div className="rbp-admin-wrap" data-testid="rbp-admin-shell-scaffold">
      <div className="rbp-admin-bar">
        <span>RBP Admin (Scaffold)</span>
        <div>
          <Link to="/">Back to Site</Link>
        </div>
      </div>
      <div className="rbp-admin-body">
        <div className="rbp-admin-notice">
          <strong>Admin Shell Scaffold</strong><br />
          Admin functionality for RBP is delivered through Frappe Desk workspaces,
          list views, and form views. This is a structural reference only.
        </div>
        {children}
      </div>
    </div>
  );
}
