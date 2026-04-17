# RBP App - Remote Business Partner

Custom Frappe application shell for the Remote Business Partner platform.

## Overview

This app provides the isolated shell architecture for the RBP business application, built as a dedicated Frappe custom app. It contains:

- **Public website shell** - Header, navigation, footer, and all public-facing page routes
- **Auth shell** - Minimal login/register/password-reset page templates
- **Portal shell** - Authenticated member portal with sidebar navigation
- **Admin scaffold** - Structural references pointing to Frappe Desk

## Architecture

```
rbp_app/
├── rbp_app/
│   ├── hooks.py              # Frappe hooks (assets, routes)
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
Authenticated layout: sidebar navigation, portal header, page content region.

### 4. Admin Shell (`admin_base.html`)
Scaffold only. Admin is served by Frappe Desk. See `ADMIN_APPROACH.md`.

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
5. **No business logic, payment, CMS, or calculator logic** in this shell phase.

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
