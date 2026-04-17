import React from 'react';
import { Link } from 'react-router-dom';
import ShellNavigator from './ShellNavigator';

const publicRoutes = [
  { path: "/", label: "Home" },
  { path: "/about", label: "About" },
  { path: "/contact", label: "Contact" },
  { path: "/help", label: "Help Centre" },
  { path: "/faq", label: "FAQ" },
  { path: "/privacy", label: "Privacy" },
  { path: "/terms", label: "Terms" },
];

const serviceRoutes = [
  { path: "/services", label: "Services Index" },
  { path: "/services/:category", label: "Service Category", dynamic: true },
  { path: "/service/:slug", label: "Service Detail", dynamic: true },
];

const membershipRoutes = [
  { path: "/membership", label: "Membership Index" },
  { path: "/membership/plans", label: "Plans" },
  { path: "/membership/pro", label: "Pro" },
  { path: "/membership/ultimate", label: "Ultimate" },
  { path: "/membership/compare", label: "Compare" },
];

const resourceRoutes = [
  { path: "/resources", label: "Resources Index" },
  { path: "/resources/search", label: "Search" },
  { path: "/resources/:category", label: "Category", dynamic: true },
  { path: "/resources/:category/:slug", label: "Detail", dynamic: true },
];

const financeRoutes = [
  { path: "/finance", label: "Finance Index" },
  { path: "/finance/funding", label: "Funding" },
  { path: "/finance/insurance", label: "Insurance" },
  { path: "/finance/calculators", label: "Calculators" },
  { path: "/finance/learn", label: "Learn" },
  { path: "/finance/resources", label: "Resources" },
  { path: "/finance/enquiry", label: "Enquiry" },
  { path: "/finance/thank-you", label: "Thank You" },
];

const offersRoutes = [
  { path: "/offers", label: "Offers Index" },
  { path: "/offers/:slug", label: "Offer Detail", dynamic: true },
];

const decisionDeskRoutes = [
  { path: "/decision-desk", label: "Decision Desk Index" },
  { path: "/decision-desk/how-it-works", label: "How It Works" },
  { path: "/decision-desk/request", label: "Request" },
  { path: "/decision-desk/thank-you", label: "Thank You" },
];

const documentRoutes = [
  { path: "/documents", label: "Documents Index" },
  { path: "/templates", label: "Templates" },
  { path: "/toolkits", label: "Toolkits" },
  { path: "/documentation-suites", label: "Documentation Suites" },
  { path: "/product/:slug", label: "Product Detail", dynamic: true },
];

const supportRoutes = [
  { path: "/support", label: "Support Index" },
  { path: "/support/contact", label: "Contact Support" },
  { path: "/support/help-articles", label: "Help Articles" },
];

const authRoutes = [
  { path: "/login", label: "Login" },
  { path: "/register", label: "Register" },
  { path: "/join", label: "Join / Get Started" },
  { path: "/forgot-password", label: "Forgot Password" },
  { path: "/reset-password", label: "Reset Password" },
  { path: "/verify-account", label: "Verify Account" },
];

const portalRoutes = [
  { path: "/portal", label: "Portal Home" },
  { path: "/portal/dashboard", label: "Dashboard" },
  { path: "/portal/membership", label: "Membership" },
  { path: "/portal/library", label: "Library" },
  { path: "/portal/resources", label: "Resources" },
  { path: "/portal/finance", label: "Finance Overview" },
  { path: "/portal/finance/enquiries", label: "Finance Enquiries" },
  { path: "/portal/decision-desk", label: "Decision Desk" },
  { path: "/portal/decision-desk/history", label: "Decision Desk History" },
  { path: "/portal/billing", label: "Billing" },
  { path: "/portal/account", label: "Account" },
  { path: "/portal/notifications", label: "Notifications" },
  { path: "/portal/support", label: "Support" },
];

const adminRoutes = [
  { path: "/admin", label: "Admin Dashboard" },
  { path: "/admin/content", label: "Content" },
  { path: "/admin/services", label: "Services" },
  { path: "/admin/resources", label: "Resources" },
  { path: "/admin/finance", label: "Finance" },
  { path: "/admin/offers", label: "Offers" },
  { path: "/admin/decision-desk", label: "Decision Desk" },
  { path: "/admin/documents", label: "Documents" },
  { path: "/admin/memberships", label: "Memberships" },
  { path: "/admin/billing", label: "Billing" },
  { path: "/admin/users", label: "Users" },
  { path: "/admin/navigation", label: "Navigation" },
  { path: "/admin/settings", label: "Settings" },
];

function RouteGroup({ title, routes, shellId }) {
  return (
    <div className="arch-group">
      <h4>{title}</h4>
      <div className="arch-routes">
        {routes.map(r => (
          <Link
            key={r.path}
            to={r.dynamic ? "#" : r.path}
            className={`arch-route-link ${r.dynamic ? "dynamic" : ""}`}
            onClick={r.dynamic ? e => e.preventDefault() : undefined}
          >
            <code>{r.path}</code>
            <span>{r.label}</span>
            {r.dynamic && <span className="arch-dynamic-tag">dynamic</span>}
          </Link>
        ))}
      </div>
    </div>
  );
}

export default function ArchitectureMap() {
  return (
    <div data-testid="architecture-map-page">
      <ShellNavigator />
      <div className="arch-page">
        <div className="arch-header">
          <h1>RBP Application Shell Architecture</h1>
          <p>Complete route and shell ownership map for the Remote Business Partner application.</p>
          <div className="arch-owner-box" data-testid="arch-owner-box">
            <strong>Custom App Owner:</strong> <code>rbp_app</code>
            <span className="arch-owner-detail">
              All routes, templates, shells, and assets are owned by the <code>rbp_app</code> custom Frappe application.
              The Frappe framework core is untouched.
            </span>
          </div>
        </div>

        {/* Application Flow Diagram */}
        <section className="arch-section" data-testid="arch-flow-section">
          <h2>Application Flow</h2>
          <div className="arch-flow">
            <div className="arch-flow-node public">
              <div className="arch-flow-label">Public Website</div>
              <div className="arch-flow-desc">Guest-facing pages, services, resources</div>
              <Link to="/" className="arch-flow-enter">Enter Shell</Link>
            </div>
            <div className="arch-flow-arrow">
              <span>Login / Join</span>
            </div>
            <div className="arch-flow-node auth">
              <div className="arch-flow-label">Auth Layer</div>
              <div className="arch-flow-desc">Login, register, password reset, verification</div>
              <Link to="/login" className="arch-flow-enter">Enter Shell</Link>
            </div>
            <div className="arch-flow-arrow">
              <span>Authenticated</span>
            </div>
            <div className="arch-flow-node portal">
              <div className="arch-flow-label">Member Portal</div>
              <div className="arch-flow-desc">Dashboard, membership, billing, account</div>
              <Link to="/portal/dashboard" className="arch-flow-enter">Enter Shell</Link>
            </div>
            <div className="arch-flow-arrow">
              <span>Admin Role</span>
            </div>
            <div className="arch-flow-node admin">
              <div className="arch-flow-label">Admin / Desk</div>
              <div className="arch-flow-desc">Content management via Frappe Desk</div>
              <Link to="/admin" className="arch-flow-enter">Enter Shell</Link>
            </div>
          </div>
        </section>

        {/* Shell Boundaries */}
        <section className="arch-section" data-testid="arch-boundaries-section">
          <h2>Shell Boundaries</h2>
          <div className="arch-boundaries">
            <div className="arch-boundary public">
              <h3>Public Shell</h3>
              <p>Unauthenticated access. Full navigation, header, footer. Serves all guest-facing content.</p>
              <div className="arch-boundary-transitions">
                <span>Transitions to:</span>
                <Link to="/login">Auth (Login)</Link>
                <Link to="/join">Auth (Join)</Link>
                <Link to="/portal/dashboard">Portal (if authenticated)</Link>
              </div>
            </div>
            <div className="arch-boundary auth">
              <h3>Auth Shell</h3>
              <p>Minimal chrome. Handles identity: login, registration, password reset, email verification.</p>
              <div className="arch-boundary-transitions">
                <span>Transitions to:</span>
                <Link to="/">Public (back to site)</Link>
                <Link to="/portal/dashboard">Portal (on success)</Link>
              </div>
            </div>
            <div className="arch-boundary portal">
              <h3>Portal Shell</h3>
              <p>Authenticated members only. Sidebar navigation, personal dashboard, account management.</p>
              <div className="arch-boundary-transitions">
                <span>Transitions to:</span>
                <Link to="/">Public (back to site)</Link>
                <Link to="/login">Auth (logout)</Link>
                <Link to="/admin">Admin (if admin role)</Link>
              </div>
            </div>
            <div className="arch-boundary admin">
              <h3>Admin Shell</h3>
              <p>Admin/staff only. Served by Frappe Desk. Scaffold placeholders document the mapping.</p>
              <div className="arch-boundary-transitions">
                <span>Transitions to:</span>
                <Link to="/portal/dashboard">Portal</Link>
                <Link to="/">Public (back to site)</Link>
              </div>
            </div>
          </div>
        </section>

        {/* Complete Route Tree */}
        <section className="arch-section" data-testid="arch-routes-section">
          <h2>Complete Route Tree</h2>

          <div className="arch-shell-block public" data-testid="arch-public-routes">
            <div className="arch-shell-header">
              <span className="shell-dot public" />
              <h3>Public Shell</h3>
              <span className="arch-count">{7 + serviceRoutes.length + membershipRoutes.length + resourceRoutes.length + financeRoutes.length + offersRoutes.length + decisionDeskRoutes.length + documentRoutes.length + supportRoutes.length} routes</span>
            </div>
            <div className="arch-groups-grid">
              <RouteGroup title="General" routes={publicRoutes} shellId="public" />
              <RouteGroup title="Services" routes={serviceRoutes} shellId="public" />
              <RouteGroup title="Membership" routes={membershipRoutes} shellId="public" />
              <RouteGroup title="Resources" routes={resourceRoutes} shellId="public" />
              <RouteGroup title="Finance" routes={financeRoutes} shellId="public" />
              <RouteGroup title="Offers" routes={offersRoutes} shellId="public" />
              <RouteGroup title="Decision Desk" routes={decisionDeskRoutes} shellId="public" />
              <RouteGroup title="Documents" routes={documentRoutes} shellId="public" />
              <RouteGroup title="Support" routes={supportRoutes} shellId="public" />
            </div>
          </div>

          <div className="arch-shell-block auth" data-testid="arch-auth-routes">
            <div className="arch-shell-header">
              <span className="shell-dot auth" />
              <h3>Auth Shell</h3>
              <span className="arch-count">{authRoutes.length} routes</span>
            </div>
            <div className="arch-groups-grid">
              <RouteGroup title="Authentication" routes={authRoutes} shellId="auth" />
            </div>
          </div>

          <div className="arch-shell-block portal" data-testid="arch-portal-routes">
            <div className="arch-shell-header">
              <span className="shell-dot portal" />
              <h3>Portal Shell</h3>
              <span className="arch-count">{portalRoutes.length} routes</span>
            </div>
            <div className="arch-groups-grid">
              <RouteGroup title="Member Portal" routes={portalRoutes} shellId="portal" />
            </div>
          </div>

          <div className="arch-shell-block admin" data-testid="arch-admin-routes">
            <div className="arch-shell-header">
              <span className="shell-dot admin" />
              <h3>Admin Shell (Scaffold &rarr; Frappe Desk)</h3>
              <span className="arch-count">{adminRoutes.length} routes</span>
            </div>
            <div className="arch-groups-grid">
              <RouteGroup title="Admin Management" routes={adminRoutes} shellId="admin" />
            </div>
          </div>
        </section>

        {/* Frappe Integration Notes */}
        <section className="arch-section" data-testid="arch-integration-section">
          <h2>Frappe Integration</h2>
          <div className="arch-integration-grid">
            <div className="arch-integration-card">
              <h4>Custom App Ownership</h4>
              <p>
                All shell templates, www pages, public assets, and navigation config live inside
                <code>rbp_app/</code>. Zero framework-core modifications.
              </p>
            </div>
            <div className="arch-integration-card">
              <h4>Template Inheritance</h4>
              <p>
                Shell templates extend <code>frappe/templates/base.html</code>.
                Each www page extends its shell: <code>public_base.html</code>,
                <code>auth_base.html</code>, <code>portal_base.html</code>, or <code>admin_base.html</code>.
              </p>
            </div>
            <div className="arch-integration-card">
              <h4>Hooks Integration</h4>
              <p>
                <code>hooks.py</code> registers <code>web_include_css</code> and <code>web_include_js</code>
                for RBP assets. Dynamic <code>website_route_rules</code> are ready for activation.
              </p>
            </div>
            <div className="arch-integration-card">
              <h4>Admin Strategy</h4>
              <p>
                Admin uses Frappe Desk natively. Custom DocTypes will provide list/form views.
                No duplicate admin UI. See <code>ADMIN_APPROACH.md</code>.
              </p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
