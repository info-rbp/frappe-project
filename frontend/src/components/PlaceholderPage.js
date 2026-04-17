import React from 'react';

export default function PlaceholderPage({ title, section, route, shell, description }) {
  return (
    <div className="rbp-page" data-testid={`${route.replace(/\//g, '-').replace(/^-/, '')}-page`}>
      {shell !== 'portal' && <h1 data-testid="page-title">{title}</h1>}
      {description && (
        <p className="rbp-page-desc">{description}</p>
      )}
      <div className="rbp-page-content" data-testid="page-content">
        <p>Content for this page is being prepared.</p>
        <p className="rbp-page-sub">Check back soon for updates.</p>
      </div>
    </div>
  );
}
