export const publicNavigation = [
  { name: 'Home', path: '/' },
  { name: 'Services', path: '/services' },
  { name: 'Membership', path: '/membership' },
  { name: 'Resources', path: '/resources' },
  { name: 'Finance', path: '/finance' },
  { name: 'Offers', path: '/offers' },
  { name: 'Decision Desk', path: '/decision-desk' },
  { name: 'Documents', path: '/documents' },
  { name: 'Help', path: '/help' },
]

export const routes = [
  // Public Core
  { path: '/', name: 'Home', layout: 'PublicShell' },
  { path: '/about', name: 'About', layout: 'PublicShell' },
  { path: '/contact', name: 'Contact', layout: 'PublicShell' },
  { path: '/help', name: 'Help', layout: 'PublicShell' },
  { path: '/faq', name: 'FAQ', layout: 'PublicShell' },
  { path: '/privacy', name: 'Privacy', layout: 'PublicShell' },
  { path: '/terms', name: 'Terms', layout: 'PublicShell' },
  
  // Services
  { path: '/services', name: 'Services', layout: 'PublicShell' },
  { path: '/services/:category', name: 'Service Category', layout: 'PublicShell' },
  { path: '/service/:slug', name: 'Service Detail', layout: 'PublicShell' },
  
  // Membership
  { path: '/membership', name: 'Membership', layout: 'PublicShell' },
  { path: '/membership/plans', name: 'Plans', layout: 'PublicShell' },
  { path: '/membership/compare', name: 'Compare', layout: 'PublicShell' },
  
  // Auth
  { path: '/login', name: 'Login', layout: 'AuthShell' },
  { path: '/register', name: 'Register', layout: 'AuthShell' },
  { path: '/join', name: 'Join', layout: 'AuthShell' },
  
  // Portal Scopes (Minimal Scaffolding)
  { path: '/portal', name: 'Portal Dashboard', layout: 'PortalShell' },
  { path: '/portal/dashboard', name: 'Dashboard', layout: 'PortalShell' },
  { path: '/portal/account', name: 'Account', layout: 'PortalShell' },

  // Admin Scopes (Minimal Scaffolding)
  { path: '/admin', name: 'Admin Dashboard', layout: 'AdminShell' },
  { path: '/admin/dashboard', name: 'Dashboard', layout: 'AdminShell' },
]
