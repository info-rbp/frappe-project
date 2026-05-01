# RBP App - Remote Business Partner

Custom Frappe application and platform layer for the Remote Business Partner platform.

## Overview

This app provides the isolated shell architecture for the RBP business application and is evolving into the RBP platform layer on top of Frappe. It contains:

- **Public website shell** - Header, navigation, footer, and all public-facing page routes
- **Auth shell** - Minimal login/register/password-reset page templates
- **Portal shell** - Authenticated customer-facing portal with sidebar navigation
- **Admin scaffold** - Structural references pointing to Frappe Desk
- **Platform APIs** - Whitelisted API methods in `rbp_app.api`
- **Service layer** - Business logic and cross-app integrations in `rbp_app.services`

Installed Frappe apps such as HRMS, CRM, LMS, ERPNext, and Payments remain backend capability providers. RBP does not rebuild those apps, modify Frappe core, or replace Frappe Desk.

## Architecture

```
rbp_app/
├── rbp_app/
│   ├── hooks.py              # Frappe hooks (assets, routes)
│   ├── api/                   # Whitelisted platform API methods
│   ├── services/              # Business services and app integrations
│   ├── doctype/               # RBP platform DocTypes
│   ├── patches/               # RBP platform patches
│   ├── guards.py              # Website route guards
│   ├── permissions.py         # Shared role helpers
│   ├── www/                  # Website pages (filesystem-driven routes)
│   │   ├── index.html        # Home page (/)
│   │   ├── services/         # /services/*
│   │   ├── membership/       # /membership/*
│   │   ├── resources/        # /resources/*
│   │   ├── finance/          # /finance/*
│   │   ├── offers/           # /offers/*
│   │   ├── decision-desk/    # /decision-desk/*
│   │   ├── documents/        # /documents/*
│   │   ├── support/          # /support/*
│   │   ├── help/             # /help/*
│   │   ├── portal/           # /portal/* (authenticated)
│   │   ├── admin/            # /admin/* (scaffold → Desk)
│   │   ├── login.html        # Auth pages
│   │   ├── register.html
│   │   └── ...
│   ├── templates/
│   │   ├── shells/           # Base shell templates
│   │   │   ├── public_base.html
│   │   │   ├── auth_base.html
│   │   │   ├── portal_base.html
│   │   │   └── admin_base.html
│   │   ├── includes/         # Shared template fragments
│   │   │   ├── header.html
│   │   │   ├── footer.html
│   │   │   ├── mega_menu.html
│   │   │   ├── portal_sidebar.html
│   │   │   └── admin_shell_elements.html
│   │   └── pages/            # (future) full page templates
│   ├── public/
│   │   ├── css/rbp.css       # RBP stylesheet
│   │   ├── js/rbp.js         # RBP JavaScript
│   │   └── images/           # Static images
│   ├── config/
│   │   └── navigation.py     # Navigation configuration
│   └── utils/
├── tests/
├── pyproject.toml
├── ADMIN_APPROACH.md
└── README.md
```

## Shell Modes

### 1. Public Shell (`public_base.html`)
Full website layout: header with navigation, main content area, footer.

### 2. Auth Shell (`auth_base.html`)
Minimal layout: small header/logo, centered auth card, support link, small footer.

### 3. Portal Shell (`portal_base.html`)
Authenticated customer-facing layout: sidebar navigation, portal header, page content region. `/portal` and `/portal/*` require login.

### 4. Admin Shell (`admin_base.html`)
Scaffold only. Admin/backend work is served by Frappe Desk at `/desk`. `/admin` and `/admin/*` are restricted to Administrator, System Manager, or configured RBP admin roles. See `ADMIN_APPROACH.md`.

## Platform APIs

Phase 1 platform APIs live under `rbp_app.api`:

| API | Purpose |
|---|---|
| `rbp_app.api.me.get_current_user` | Current user, full name, roles, user type, guest state |
| `rbp_app.api.apps.get_available_apps` | Role-aware app cards based on installed apps and entitlement placeholders |
| `rbp_app.api.dashboard.get_home` | Portal dashboard payload |
| `rbp_app.api.hr.get_employee_summary` | HRMS-backed employee summary, safe empty response if HRMS is absent |
| `rbp_app.api.hr.get_leave_summary` | HRMS-backed leave summary, safe empty response if HRMS is absent |

Services live in `rbp_app.services` and own business logic. API modules should stay thin wrappers around those services.

## Installation

```bash
# From bench directory
bench get-app /path/to/rbp_app
bench install-app rbp_app
```

## Key Decisions

1. **All RBP business pages live in this custom app**, not in `frappe/` core.
2. **Shell templates extend `frappe/templates/base.html`** to inherit framework features.
3. **Admin uses Frappe Desk** - no duplicate admin UI.
4. **Dynamic routes** are commented out in `hooks.py` until business logic phase.
5. **Platform logic belongs in `rbp_app.api` and `rbp_app.services`**, not in Frappe core.
6. **Frappe apps remain backend capability providers** for HRMS, CRM, LMS, ERPNext, billing, and related workflows.

## Route Coverage

| Section | Routes | Shell |
|---|---|---|
| Public (home, about, etc.) | 7 | Public |
| Services | 3 | Public |
| Membership | 5 | Public |
| Resources | 2+ | Public |
| Finance | 8 | Public |
| Offers | 1+ | Public |
| Decision Desk | 4 | Public |
| Documents | 5 | Public |
| Support | 3 | Public |
| Help | 1 | Public |
| Auth | 6 | Auth |
| Portal | 13 | Portal |
| Admin | 13 | Admin (scaffold) |

## Framework-Core Changes

**None.** This app operates entirely within the custom app layer. Zero modifications to `frappe/` core files.
