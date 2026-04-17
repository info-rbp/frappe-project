import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const shells = [
  { id: "public", label: "Public Website", url: "/", prefix: ["/about", "/contact", "/faq", "/privacy", "/terms", "/help", "/services", "/membership", "/resources", "/finance", "/offers", "/decision-desk", "/documents", "/templates", "/toolkits", "/documentation-suites", "/product", "/support"] },
  { id: "auth", label: "Auth Layer", url: "/login", prefix: ["/login", "/register", "/join", "/forgot-password", "/reset-password", "/verify-account"] },
  { id: "portal", label: "Member Portal", url: "/portal/dashboard", prefix: ["/portal"] },
  { id: "admin", label: "Admin / Desk", url: "/admin", prefix: ["/admin"] },
];

export default function ShellNavigator() {
  const location = useLocation();
  const path = location.pathname;

  const current = (() => {
    if (path === "/architecture") return "map";
    for (const s of [...shells].reverse()) {
      if (s.prefix.some(p => path === p || path.startsWith(p + "/"))) return s.id;
    }
    return "public";
  })();

  return (
    <div className="shell-nav" data-testid="shell-navigator">
      <div className="shell-nav-inner">
        <div className="shell-nav-left">
          <Link to="/architecture" className={`shell-nav-map ${current === "map" ? "active" : ""}`} data-testid="shell-nav-architecture">
            Architecture Map
          </Link>
          <span className="shell-nav-sep">|</span>
          <span className="shell-nav-label">Shell:</span>
        </div>
        <div className="shell-nav-items">
          {shells.map(s => (
            <Link
              key={s.id}
              to={s.url}
              className={`shell-nav-item ${current === s.id ? "current" : ""}`}
              data-testid={`shell-nav-${s.id}`}
            >
              <span className={`shell-dot ${s.id}`} />
              {s.label}
            </Link>
          ))}
        </div>
        <div className="shell-nav-owner" data-testid="shell-nav-owner">
          <span className="shell-nav-app-badge">rbp_app</span>
        </div>
      </div>
    </div>
  );
}
