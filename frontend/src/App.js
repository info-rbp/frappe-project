import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PublicShell from './components/PublicShell';
import AuthShell from './components/AuthShell';
import PortalShell from './components/PortalShell';
import AdminShell from './components/AdminShell';
import HomePage from './components/HomePage';
import PlaceholderPage from './components/PlaceholderPage';
import ArchitectureMap from './components/ArchitectureMap';
import './App.css';

const publicRoutes = [
  { path: "/about", title: "About", section: "Company" },
  { path: "/contact", title: "Contact", section: "Company" },
  { path: "/faq", title: "FAQ", section: "Support" },
  { path: "/privacy", title: "Privacy Policy", section: "Legal" },
  { path: "/terms", title: "Terms of Service", section: "Legal" },
  { path: "/help", title: "Help Centre", section: "Help" },
  { path: "/services", title: "Services", section: "Services" },
  { path: "/services/:category", title: "Service Category", section: "Services" },
  { path: "/service/:slug", title: "Service Detail", section: "Services" },
  { path: "/membership", title: "Membership", section: "Membership" },
  { path: "/membership/plans", title: "Membership Plans", section: "Membership" },
  { path: "/membership/pro", title: "Pro Membership", section: "Membership" },
  { path: "/membership/ultimate", title: "Ultimate Membership", section: "Membership" },
  { path: "/membership/compare", title: "Compare Plans", section: "Membership" },
  { path: "/resources", title: "Resources", section: "Resources" },
  { path: "/resources/search", title: "Search Resources", section: "Resources" },
  { path: "/finance", title: "Finance", section: "Finance" },
  { path: "/finance/funding", title: "Funding", section: "Finance" },
  { path: "/finance/insurance", title: "Insurance", section: "Finance" },
  { path: "/finance/calculators", title: "Calculators", section: "Finance" },
  { path: "/finance/learn", title: "Learn", section: "Finance" },
  { path: "/finance/resources", title: "Finance Resources", section: "Finance" },
  { path: "/finance/enquiry", title: "Finance Enquiry", section: "Finance" },
  { path: "/finance/thank-you", title: "Thank You", section: "Finance" },
  { path: "/offers", title: "Offers", section: "Offers" },
  { path: "/offers/:slug", title: "Offer Detail", section: "Offers" },
  { path: "/decision-desk", title: "Decision Desk", section: "Decision Desk" },
  { path: "/decision-desk/how-it-works", title: "How It Works", section: "Decision Desk" },
  { path: "/decision-desk/request", title: "Request", section: "Decision Desk" },
  { path: "/decision-desk/thank-you", title: "Thank You", section: "Decision Desk" },
  { path: "/documents", title: "Documents", section: "Documents" },
  { path: "/templates", title: "Templates", section: "Documents" },
  { path: "/toolkits", title: "Toolkits", section: "Documents" },
  { path: "/documentation-suites", title: "Documentation Suites", section: "Documents" },
  { path: "/product/:slug", title: "Product Detail", section: "Documents" },
  { path: "/support", title: "Support", section: "Support" },
  { path: "/support/contact", title: "Contact Support", section: "Support" },
  { path: "/support/help-articles", title: "Help Articles", section: "Support" },
];

const authRoutes = [
  { path: "/login", title: "Login", desc: "Sign in to your RBP account." },
  { path: "/register", title: "Register", desc: "Create a new RBP account." },
  { path: "/join", title: "Join / Get Started", desc: "Join Remote Business Partner today." },
  { path: "/forgot-password", title: "Forgot Password", desc: "Reset your password." },
  { path: "/reset-password", title: "Reset Password", desc: "Set a new password." },
  { path: "/verify-account", title: "Verify Account", desc: "Verify your email address." },
];

const portalRoutes = [
  { path: "/portal", title: "Portal Home", section: "Portal" },
  { path: "/portal/dashboard", title: "Dashboard", section: "Dashboard" },
  { path: "/portal/membership", title: "Membership", section: "Membership" },
  { path: "/portal/library", title: "Library", section: "Library" },
  { path: "/portal/resources", title: "Resources", section: "Resources" },
  { path: "/portal/finance", title: "Finance", section: "Finance" },
  { path: "/portal/finance/enquiries", title: "Finance Enquiries", section: "Finance" },
  { path: "/portal/decision-desk", title: "Decision Desk", section: "Decision Desk" },
  { path: "/portal/decision-desk/history", title: "Decision Desk History", section: "Decision Desk" },
  { path: "/portal/billing", title: "Billing", section: "Billing" },
  { path: "/portal/account", title: "Account", section: "Account" },
  { path: "/portal/notifications", title: "Notifications", section: "Notifications" },
  { path: "/portal/support", title: "Support", section: "Support" },
];

const adminRoutes = [
  { path: "/admin", title: "Admin Dashboard", section: "Dashboard" },
  { path: "/admin/content", title: "Content Management", section: "Content" },
  { path: "/admin/services", title: "Services Management", section: "Services" },
  { path: "/admin/resources", title: "Resources Management", section: "Resources" },
  { path: "/admin/finance", title: "Finance Management", section: "Finance" },
  { path: "/admin/offers", title: "Offers Management", section: "Offers" },
  { path: "/admin/decision-desk", title: "Decision Desk Admin", section: "Decision Desk" },
  { path: "/admin/documents", title: "Documents Admin", section: "Documents" },
  { path: "/admin/memberships", title: "Memberships Admin", section: "Memberships" },
  { path: "/admin/billing", title: "Billing Admin", section: "Billing" },
  { path: "/admin/users", title: "Users Admin", section: "Users" },
  { path: "/admin/navigation", title: "Navigation Admin", section: "Navigation" },
  { path: "/admin/settings", title: "Settings", section: "Settings" },
];

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Architecture Map - standalone shell-level page */}
        <Route path="/architecture" element={<ArchitectureMap />} />

        {/* Public Shell */}
        <Route path="/" element={<PublicShell><HomePage /></PublicShell>} />
        {publicRoutes.map(r => (
          <Route key={r.path} path={r.path} element={
            <PublicShell>
              <PlaceholderPage title={r.title} section={r.section} route={r.path} shell="public" />
            </PublicShell>
          } />
        ))}

        {/* Auth Shell */}
        {authRoutes.map(r => (
          <Route key={r.path} path={r.path} element={
            <AuthShell>
              <PlaceholderPage title={r.title} section="Auth" route={r.path} shell="auth" description={r.desc} />
            </AuthShell>
          } />
        ))}

        {/* Portal Shell */}
        {portalRoutes.map(r => (
          <Route key={r.path} path={r.path} element={
            <PortalShell pageTitle={r.title}>
              <PlaceholderPage title={r.title} section={r.section} route={r.path} shell="portal" />
            </PortalShell>
          } />
        ))}

        {/* Admin Shell */}
        {adminRoutes.map(r => (
          <Route key={r.path} path={r.path} element={
            <AdminShell>
              <PlaceholderPage title={r.title} section={r.section} route={r.path} shell="admin" />
            </AdminShell>
          } />
        ))}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
