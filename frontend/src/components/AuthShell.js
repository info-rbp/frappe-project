import React from 'react';
import { Link } from 'react-router-dom';

export default function AuthShell({ children }) {
  return (
    <div className="rbp-auth-wrap" data-testid="rbp-auth-shell">
      <div className="rbp-auth-head">
        <Link to="/" className="rbp-logo" data-testid="rbp-auth-logo">RBP</Link>
      </div>
      <div className="rbp-auth-body">
        <div className="rbp-auth-card">
          {children}
          <div className="rbp-auth-flow" data-testid="auth-flow-links">
            <div className="rbp-auth-flow-inner">
              <Link to="/" data-testid="auth-back-to-site">Back to site</Link>
            </div>
          </div>
        </div>
      </div>
      <div className="rbp-auth-help">
        <Link to="/support">Need help?</Link>
      </div>
      <div className="rbp-auth-foot" data-testid="rbp-auth-footer">
        &copy; {new Date().getFullYear()} Remote Business Partner
      </div>
    </div>
  );
}
