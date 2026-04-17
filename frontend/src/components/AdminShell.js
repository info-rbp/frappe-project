import React from 'react';
import { Link } from 'react-router-dom';

export default function AdminShell({ children }) {
  return (
    <div className="rbp-admin-wrap" data-testid="rbp-admin-shell-scaffold">
      <div className="rbp-admin-bar">
        <div className="rbp-admin-bar-left">
          <Link to="/" className="rbp-logo" style={{fontSize:'1rem'}}>RBP</Link>
          <span className="rbp-admin-bar-title">Administration</span>
        </div>
        <div className="rbp-admin-bar-links">
          <Link to="/" data-testid="admin-to-public">Website</Link>
          <Link to="/portal/dashboard" data-testid="admin-to-portal">Portal</Link>
          <Link to="/login" data-testid="admin-to-logout">Sign Out</Link>
        </div>
      </div>
      <div className="rbp-admin-body">
        {children}
      </div>
    </div>
  );
}
