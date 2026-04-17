import React from 'react';
import { Link } from 'react-router-dom';

const cards = [
  { title: "Services", desc: "Explore our range of business services.", link: "/services", cta: "Browse Services" },
  { title: "Membership", desc: "Join and access exclusive member benefits.", link: "/membership", cta: "View Plans" },
  { title: "Resources", desc: "Access guides, tools, and knowledge base.", link: "/resources", cta: "Explore Resources" },
  { title: "Finance", desc: "Funding, insurance, and financial tools.", link: "/finance", cta: "Finance Hub" },
  { title: "Offers", desc: "Current deals and special packages.", link: "/offers", cta: "See Offers" },
  { title: "Decision Desk", desc: "Expert guidance for business decisions.", link: "/decision-desk", cta: "Learn More" },
  { title: "Documents", desc: "Templates, toolkits, and documentation.", link: "/documents", cta: "Browse Documents" },
  { title: "Portal", desc: "Member dashboard and account management.", link: "/portal", cta: "Go to Portal" },
];

export default function HomePage() {
  return (
    <div data-testid="rbp-home-page">
      <section className="rbp-hero" data-testid="rbp-hero">
        <h1>Remote Business Partner</h1>
        <p>Your partner for business services, resources, and growth.</p>
        <Link to="/join" className="rbp-hero-cta" data-testid="hero-cta">Get Started</Link>
      </section>

      <div className="rbp-main">
        <div className="rbp-cards">
          {cards.map(c => (
            <div className="rbp-card" key={c.link}>
              <h3>{c.title}</h3>
              <p>{c.desc}</p>
              <Link to={c.link}>{c.cta} &rarr;</Link>
            </div>
          ))}
        </div>

        <div className="rbp-placeholder-box" style={{ marginTop: '1rem' }}>
          <p>This is the RBP shell home page. Full content will be added in a future phase.</p>
          <div className="rbp-route-badge">/</div>
        </div>
      </div>
    </div>
  );
}
