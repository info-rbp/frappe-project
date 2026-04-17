import React from 'react';

export default function PlaceholderPage({ title, section, route, shell, description }) {
  return (
    <div className="rbp-placeholder" data-testid={`${route.replace(/\//g, '-').replace(/^-/, '')}-page`}>
      {shell !== 'portal' && <h1>{title}</h1>}
      <div className="rbp-section-tag">
        Section: {section}
        <span className={`rbp-shell-badge ${shell}`}>{shell} shell</span>
      </div>
      {description && (
        <p style={{ color: 'var(--rbp-text-light)', marginBottom: '1.25rem' }}>{description}</p>
      )}
      <div className="rbp-placeholder-box">
        <p>This is a shell placeholder page for <strong>{route}</strong>.</p>
        <p>Business content will be added in a future phase.</p>
        <div className="rbp-route-badge">{route}</div>
      </div>
    </div>
  );
}
