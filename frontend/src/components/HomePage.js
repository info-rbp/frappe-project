import React from 'react';
import { Link } from 'react-router-dom';

const sectionCards = [
  { title: "Services", desc: "Explore our range of business services.", link: "/services", cta: "Browse Services" },
  { title: "Membership", desc: "Join and access exclusive member benefits.", link: "/membership", cta: "View Plans" },
  { title: "Resources", desc: "Access guides, tools, and knowledge base.", link: "/resources", cta: "Explore Resources" },
  { title: "Finance", desc: "Funding, insurance, and financial tools.", link: "/finance", cta: "Finance Hub" },
  { title: "Offers", desc: "Current deals and special packages.", link: "/offers", cta: "See Offers" },
  { title: "Decision Desk", desc: "Expert guidance for business decisions.", link: "/decision-desk", cta: "Learn More" },
  { title: "Documents", desc: "Templates, toolkits, and documentation.", link: "/documents", cta: "Browse Documents" },
  { title: "Support", desc: "Help centre and contact support.", link: "/support", cta: "Get Help" },
];

export default function HomePage() {
  return (
    <div data-testid="rbp-home-page">
      <section className="rbp-hero" data-testid="rbp-hero">
        <h1>Remote Business Partner</h1>
        <p>Your partner for business services, resources, and growth.</p>
        <div className="rbp-hero-actions">
          <Link to="/join" className="rbp-hero-cta" data-testid="hero-cta">Get Started</Link>
          <Link to="/architecture" className="rbp-hero-cta-secondary" data-testid="hero-architecture">View Architecture</Link>
        </div>
      </section>

      <div className="rbp-main">
        {/* Application Layers */}
        <section className="rbp-app-layers" data-testid="rbp-app-layers">
          <h2>Application Shell Layers</h2>
          <p className="rbp-layers-desc">The RBP platform is organised into four interconnected application surfaces, all owned by the <code>rbp_app</code> custom Frappe application.</p>
          <div className="rbp-layers-grid">
            <Link to="/" className="rbp-layer-card public" data-testid="layer-public">
              <span className="rbp-layer-dot public" />
              <h3>Public Website</h3>
              <p>Guest-facing content: services, membership, resources, finance, documents.</p>
              <span className="rbp-layer-routes">38 routes</span>
            </Link>
            <Link to="/login" className="rbp-layer-card auth" data-testid="layer-auth">
              <span className="rbp-layer-dot auth" />
              <h3>Auth Layer</h3>
              <p>Login, registration, password reset, email verification.</p>
              <span className="rbp-layer-routes">6 routes</span>
            </Link>
            <Link to="/portal/dashboard" className="rbp-layer-card portal" data-testid="layer-portal">
              <span className="rbp-layer-dot portal" />
              <h3>Member Portal</h3>
              <p>Authenticated dashboard, membership, billing, account management.</p>
              <span className="rbp-layer-routes">13 routes</span>
            </Link>
            <Link to="/admin" className="rbp-layer-card admin" data-testid="layer-admin">
              <span className="rbp-layer-dot admin" />
              <h3>Admin / Desk</h3>
              <p>Content management via Frappe Desk. Scaffold placeholder.</p>
              <span className="rbp-layer-routes">13 routes</span>
            </Link>
          </div>
        </section>

        {/* Public Sections */}
        <section data-testid="rbp-sections">
          <h2>Public Website Sections</h2>
          <div className="rbp-cards">
            {sectionCards.map(c => (
              <div className="rbp-card" key={c.link}>
                <h3>{c.title}</h3>
                <p>{c.desc}</p>
                <Link to={c.link}>{c.cta} &rarr;</Link>
              </div>
            ))}
          </div>
        </section>

        <div className="rbp-placeholder-box" style={{ marginTop: '1.5rem' }}>
          <p>This is the RBP shell home page. Full content will be added in a future phase.</p>
          <div className="rbp-route-badge">/</div>
        </div>
      </div>
    </div>
  );
}
