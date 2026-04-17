import React from 'react';
import { Link } from 'react-router-dom';

const sectionCards = [
  { title: "Services", desc: "Explore our range of business services designed for growth and scale.", link: "/services", cta: "Browse Services" },
  { title: "Membership", desc: "Join and access exclusive member benefits, tools, and resources.", link: "/membership", cta: "View Plans" },
  { title: "Resources", desc: "Access guides, tools, templates, and a growing knowledge base.", link: "/resources", cta: "Explore" },
  { title: "Finance", desc: "Funding, insurance, calculators, and financial planning tools.", link: "/finance", cta: "Finance Hub" },
];

const secondaryCards = [
  { title: "Offers", desc: "Current deals, packages, and special opportunities for members.", link: "/offers", cta: "See Offers" },
  { title: "Decision Desk", desc: "Expert guidance and structured support for business decisions.", link: "/decision-desk", cta: "Learn More" },
  { title: "Documents", desc: "Templates, toolkits, documentation suites, and ready-to-use assets.", link: "/documents", cta: "Browse" },
  { title: "Support", desc: "Help centre, knowledge articles, and direct contact support.", link: "/support", cta: "Get Help" },
];

const stats = [
  { value: "50+", label: "Business services" },
  { value: "24/7", label: "Support access" },
  { value: "100%", label: "Digital-first" },
  { value: "1", label: "Partner for everything" },
];

export default function HomePage() {
  return (
    <div data-testid="rbp-home-page">
      <section className="rbp-hero" data-testid="rbp-hero">
        <div className="rbp-hero-inner">
          <h1>
            Your<br />
            <span className="accent">remote business</span><br />
            partner
          </h1>
          <p>
            Move forward with expert services, resources, and growth tools.
            Everything your business needs in one partner.
          </p>
          <div className="rbp-hero-actions">
            <Link to="/join" className="rbp-hero-cta" data-testid="hero-cta">
              Get Started Now
            </Link>
            <Link to="/services" className="rbp-hero-cta-secondary" data-testid="hero-services">
              Explore Services
            </Link>
          </div>
        </div>
      </section>

      <div className="rbp-main">
        {/* Stats strip */}
        <section className="rbp-stats" data-testid="rbp-stats">
          {stats.map(s => (
            <div className="rbp-stat" key={s.label}>
              <span className="rbp-stat-value">{s.value}</span>
              <span className="rbp-stat-label">{s.label}</span>
            </div>
          ))}
        </section>

        {/* Primary offering */}
        <section data-testid="rbp-sections">
          <h2>What we offer</h2>
          <p className="rbp-section-sub">Comprehensive business solutions under one roof.</p>
          <div className="rbp-cards">
            {sectionCards.map(c => (
              <div className="rbp-card" key={c.link}>
                <h3>{c.title}</h3>
                <p>{c.desc}</p>
                <Link to={c.link}>{c.cta} &#8594;</Link>
              </div>
            ))}
          </div>
        </section>

        {/* Why RBP */}
        <section className="rbp-why" data-testid="rbp-why">
          <div className="rbp-why-inner">
            <h2>Why <span className="accent">RBP</span>?</h2>
            <div className="rbp-why-grid">
              <div className="rbp-why-item">
                <h4>End-to-end solution</h4>
                <p>One partner for services, finance, documents, and decision support.</p>
              </div>
              <div className="rbp-why-item">
                <h4>Built for remote</h4>
                <p>Digital-first tools designed for distributed teams and businesses.</p>
              </div>
              <div className="rbp-why-item">
                <h4>Member benefits</h4>
                <p>Exclusive access, priority support, and tailored resources for members.</p>
              </div>
              <div className="rbp-why-item">
                <h4>Expert guidance</h4>
                <p>Decision Desk support to help you make confident business choices.</p>
              </div>
            </div>
          </div>
        </section>

        {/* More services */}
        <section data-testid="rbp-more-sections">
          <h2>More from RBP</h2>
          <div className="rbp-cards">
            {secondaryCards.map(c => (
              <div className="rbp-card" key={c.link}>
                <h3>{c.title}</h3>
                <p>{c.desc}</p>
                <Link to={c.link}>{c.cta} &#8594;</Link>
              </div>
            ))}
          </div>
        </section>

        {/* CTA banner */}
        <section className="rbp-cta-banner" data-testid="rbp-cta-banner">
          <h2>Ready to get started?</h2>
          <p>Join thousands of businesses already growing with RBP.</p>
          <Link to="/join" className="rbp-hero-cta">Get Started Now</Link>
        </section>
      </div>
    </div>
  );
}
