# RBP Platform Architecture

## Custom App Ownership

**All RBP business surfaces are owned by `rbp_app`**, a dedicated Frappe custom application located at `/rbp_app/`. The Frappe framework core (`/frappe/`) has zero modifications.

`rbp_app` is moving from a static shell into the RBP platform layer. It owns the public website, authenticated customer portal, RBP-specific APIs, service orchestration, route guards, and future RBP DocTypes.

Installed Frappe apps remain backend capability providers:

- HRMS provides employee and leave capabilities.
- CRM provides customer and sales capabilities.
- LMS provides learning capabilities.
- ERPNext provides operational and accounting capabilities.
- Payments and billing integrations remain backend services surfaced through RBP APIs.

RBP does not replace Frappe Desk. `/desk` remains the admin/backend workspace for staff and system administrators.

## Ecosystem Architecture

```text
Frappe Framework
    ↓
Installed Frappe Apps
    - ERPNext
    - HRMS
    - CRM
    - LMS
    - Helpdesk
    - Insights
    - Builder
    - Drive
    - Wiki
    - Payments
    - Webshop
    - Other installed apps
    ↓
rbp_app Platform Layer
    - APIs
    - Services
    - App launcher
    - Entitlements
    - Billing placeholders
    - Documents placeholders
    - Notifications
    ↓
Customer-facing Portal
    - /portal
    - /app
    - /portal/apps/<app_key>
```

`rbp_app` dynamically discovers installed apps with `frappe.get_installed_apps()`. Known apps receive first-class metadata, unknown apps receive generic metadata, and RBP platform modules are appended through the service layer. HRMS is one adapter in this ecosystem, not the whole architecture.

## Shell Architecture

The RBP application is organised into **four interconnected shell layers**:

```
 Public Website ──── Auth Layer ──── Customer Portal ──── Admin / Desk
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
5. **Route guards**: `/portal` requires login; `/admin` requires Administrator, System Manager, or configured admin roles
6. **Platform APIs**: Whitelisted methods in `rbp_app.api`
7. **Services**: Cross-app integration and business logic in `rbp_app.services`
8. **Core modifications**: Zero

## Platform Layer Structure

The backend platform structure gives future RBP APIs, services, data models, and migrations a clear home:

- `api/` contains whitelisted endpoints used by the portal/frontend.
- `services/` contains internal business logic and cross-app orchestration.
- `services/adapters/` contains app-specific integration adapters for HRMS, ERPNext, CRM, LMS and generic installed apps.
- `doctype/` contains RBP platform data models.
- `patches/` contains migration patches.
- `guards.py` contains route/API access protection.
- `permissions.py` contains shared permission helpers.

`rbp_app` is not HRMS-only. HRMS is one backend capability provider among many. The platform dynamically discovers installed Frappe apps, enriches known apps with first-class metadata, keeps unknown installed apps visible with generic metadata, and adds RBP platform modules such as Documents, Notifications and admin-only Billing.

## Dynamic Portal Launcher

Portal navigation and the portal dashboard now use dynamic app cards sourced from `rbp_app.services.apps`. The route guard/context layer attaches `portal_available_apps` and `portal_apps_by_category` for authenticated `/portal` and `/app` routes, so templates can render an ecosystem-wide launcher without calling Frappe Desk or assuming a specific backend app exists.

App cards are built from installed Frappe apps returned by `frappe.get_installed_apps()`, enriched with first-class metadata for known apps such as Frappe Core, ERPNext, HRMS, CRM, LMS, Helpdesk, Insights, Builder, Drive, Wiki, Payments and Webshop. Unknown installed apps remain visible with generic metadata. RBP platform modules such as Documents and Notifications are always included, while Billing is shown only to Administrator/System Manager users.

HRMS is only one capability module in this launcher. Static portal navigation remains as a fallback when dynamic app data is unavailable or empty.

## File Structure

```
rbp_app/
├── rbp_app/
│   ├── hooks.py                           # Frappe hooks
│   ├── api/                               # Whitelisted platform APIs
│   ├── services/                          # Platform services and app integrations
│   │   └── adapters/                      # App-specific integration adapters
│   ├── doctype/                           # Future RBP platform DocTypes
│   ├── patches/                           # Database patches
│   ├── guards.py                          # Portal/admin website guards
│   ├── permissions.py                     # Shared role checks
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
