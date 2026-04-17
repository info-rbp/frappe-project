# RBP Application Shell Architecture

## Custom App Ownership

**All RBP business surfaces are owned by `rbp_app`**, a dedicated Frappe custom application located at `/rbp_app/`. The Frappe framework core (`/frappe/`) has zero modifications.

## Shell Architecture

The RBP application is organised into **four interconnected shell layers**:

```
 Public Website ──── Auth Layer ──── Member Portal ──── Admin / Desk
  (guest access)   (identity flow)   (authenticated)   (staff/admin)
```

### Application Flow

```
Visitor arrives
    │
    ▼
┌─────────────────┐
│  PUBLIC SHELL    │  Guest-facing pages, services, resources
│  /               │  Header + Nav + Content + Footer
│  /services       │
│  /membership     │──── Login/Join ────┐
│  /finance        │                    │
│  /documents      │                    ▼
│  ...             │         ┌─────────────────┐
└─────────────────┘         │  AUTH SHELL      │  Minimal chrome
                            │  /login          │  Identity flows
                            │  /register       │
                            │  /join           │──── Success ────┐
                            │  /forgot-password│                 │
                            └─────────────────┘                 │
                                     │                          ▼
                                     │              ┌─────────────────┐
                            Back to site            │  PORTAL SHELL   │
                                                    │  /portal        │  Sidebar + Content
                                                    │  /portal/dash   │  Member dashboard
                                                    │  /portal/billing│
                                                    │  /portal/account│──── Admin role ────┐
                                                    └─────────────────┘                    │
                                                             │                             ▼
                                                    Back to Website          ┌─────────────────┐
                                                                            │  ADMIN SHELL     │
                                                                            │  /admin (scaffold)│
                                                                            │  /desk (Frappe)   │
                                                                            └─────────────────┘
```

## Shell Boundaries

### 1. Public Shell → Auth Shell
- **Trigger**: Login/Join buttons in header utility nav
- **Header links**: `Login`, `Join / Get Started`
- **Footer links**: Account section with Login, Join, Portal, Admin

### 2. Auth Shell → Portal Shell
- **Trigger**: Successful authentication
- **Forward link**: "Go to Portal" in auth card
- **Reverse link**: "Back to site" returns to public shell

### 3. Portal Shell → Public Shell
- **Trigger**: "Back to Website" link in sidebar footer and topbar
- **Available in**: Sidebar bottom, topbar left

### 4. Portal Shell → Admin Shell
- **Trigger**: "Admin / Desk" link in sidebar footer and topbar
- **Access**: Role-gated (admin/staff roles only)

### 5. Admin Shell → Portal Shell / Public Shell
- **Links**: Admin bar has "Public Site", "Member Portal", "Logout"
- **Production**: Admin routes map to `/desk` (Frappe Desk)

## Route Ownership

| Shell | Template | Route Prefixes | Count |
|---|---|---|---|
| Public | `public_base.html` | `/`, `/services`, `/membership`, `/resources`, `/finance`, `/offers`, `/decision-desk`, `/documents`, `/support`, `/help`, `/about`, `/contact`, `/faq`, `/privacy`, `/terms` | 38 |
| Auth | `auth_base.html` | `/login`, `/register`, `/join`, `/forgot-password`, `/reset-password`, `/verify-account` | 6 |
| Portal | `portal_base.html` | `/portal/*` | 13 |
| Admin | `admin_base.html` | `/admin/*` (scaffold → `/desk`) | 13 |
| **Total** | | | **70** |

## Frappe Integration Points

1. **hooks.py**: Registers `web_include_css`, `web_include_js`, `website_route_rules`
2. **Template inheritance**: All shells extend `frappe/templates/base.html`
3. **www/ routing**: Filesystem-driven pages in `rbp_app/www/`
4. **Admin strategy**: Frappe Desk natively (see `ADMIN_APPROACH.md`)
5. **Core modifications**: Zero

## File Structure

```
rbp_app/
├── rbp_app/
│   ├── hooks.py                           # Frappe hooks
│   ├── www/                               # Website pages (routes)
│   │   ├── index.html                     # / (home)
│   │   ├── services/                      # /services/*
│   │   ├── membership/                    # /membership/*
│   │   ├── resources/                     # /resources/*
│   │   ├── finance/                       # /finance/*
│   │   ├── offers/                        # /offers/*
│   │   ├── decision-desk/                 # /decision-desk/*
│   │   ├── documents/                     # /documents/*
│   │   ├── support/                       # /support/*
│   │   ├── help/                          # /help/*
│   │   ├── login.html ... verify-account  # Auth routes
│   │   ├── portal/                        # /portal/*
│   │   └── admin/                         # /admin/* (scaffold)
│   ├── templates/
│   │   ├── shells/                        # 4 base shell templates
│   │   │   ├── public_base.html
│   │   │   ├── auth_base.html
│   │   │   ├── portal_base.html
│   │   │   └── admin_base.html
│   │   └── includes/                      # Shared fragments
│   │       ├── header.html                # With cross-shell links
│   │       ├── footer.html                # With cross-shell links
│   │       ├── mega_menu.html
│   │       ├── portal_sidebar.html        # With cross-shell links
│   │       └── admin_shell_elements.html
│   ├── public/                            # Static assets
│   │   ├── css/rbp.css
│   │   ├── js/rbp.js
│   │   └── images/
│   ├── config/navigation.py               # Nav config
│   └── utils/
├── ARCHITECTURE.md                        # This file
├── ADMIN_APPROACH.md                      # Admin strategy
└── README.md
```
