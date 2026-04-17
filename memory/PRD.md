# RBP App - Product Requirements Document

## Original Problem Statement
Build an isolated RBP (Remote Business Partner) custom application shell on top of the Frappe v17 framework. The business application must be moved into a dedicated custom app layer with its own website shell, templates, includes, public routes, portal shell, and admin-oriented structure.

## Architecture
- **Framework**: Frappe v17 (17.0.0-dev)
- **Custom App**: `rbp_app` at `/app/rbp_app/`
- **Pattern**: Frappe custom app with filesystem-driven www routing
- **Admin**: Frappe Desk (documented, not duplicated)
- **Template Inheritance**: Shell templates extend `frappe/templates/base.html`

## User Personas
- **Public Visitor**: Browses services, membership, resources, documents
- **Authenticated Member**: Accesses portal dashboard, library, finance, billing
- **Admin/Manager**: Uses Frappe Desk for content and user management

## Core Requirements (Static)
1. Isolated custom app separate from Frappe core
2. 4 shell modes: Public, Auth, Portal, Admin scaffold
3. Full public navigation: Home, Services, Membership, Resources, Finance, Offers, Decision Desk, Documents, Help
4. Auth routes: Login, Register, Join, Forgot/Reset Password, Verify Account
5. Portal routes: Dashboard, Membership, Library, Resources, Finance, Decision Desk, Billing, Account, Notifications, Support
6. Admin approach: Frappe Desk (documented in ADMIN_APPROACH.md)
7. Zero modifications to frappe/ core
8. No business logic, payment, CMS, or calculator logic in shell phase

## What's Been Implemented (Jan 2026)

### Shell Phase Complete
- Created `rbp_app` custom Frappe app at `/app/rbp_app/`
- **96 files** created across the custom app
- **70 HTML placeholder pages** with correct shell inheritance
- **4 shell templates**: public_base, auth_base, portal_base, admin_base
- **5 shared includes**: header, footer, mega_menu, portal_sidebar, admin_shell_elements
- **hooks.py**: web_include_css, web_include_js, website_route_rules (commented for future)
- **navigation.py**: Centralised nav config (primary, utility, footer, portal sidebar)
- **Public assets**: rbp.css (structural styles), rbp.js (active nav highlighting)
- **Admin approach documented**: ADMIN_APPROACH.md with Desk mapping table
- **109/109 structural validation tests passed**
- **Zero frappe/ core modifications**

### Route Coverage
| Section | Pages | Shell |
|---|---|---|
| Public (home, about, contact, faq, privacy, terms) | 7 | Public |
| Services | 3 | Public |
| Membership | 5 | Public |
| Resources | 2 | Public |
| Finance | 8 | Public |
| Offers | 1 | Public |
| Decision Desk | 4 | Public |
| Documents | 5 | Public |
| Support | 3 | Public |
| Help | 1 | Public |
| Auth | 6 | Auth |
| Portal | 13 | Portal |
| Admin | 13 | Admin scaffold |
| **Total** | **71** (+ index.py) | |

## Prioritised Backlog

### P0 - Next Phase (Business Data Model)
- Create custom DocTypes for RBP business entities (Services, Membership Plans, Resources, etc.)
- Configure Desk list views and form layouts
- Create RBP workspace in Frappe Desk

### P1 - Dynamic Routes
- Activate website_route_rules in hooks.py for parameterised URLs
- Implement context providers (.py files) for dynamic pages
- Services category/detail pages, resource search, offer detail

### P2 - Content & Auth Integration
- Replace placeholder pages with real content templates
- Integrate auth shell with Frappe's built-in login/registration
- Portal access control (role-based page access)
- Mega menu implementation with section-specific content

### P3 - Business Logic (Future)
- Calculators, referral logic, payment logic, CMS logic
- Finance enquiry workflow
- Decision Desk request workflow
- Membership billing integration

## Assumptions
1. Frappe Desk serves as the admin surface (no custom admin UI needed)
2. Shell templates are Jinja-based, extending Frappe's base.html
3. Dynamic routes will be activated when business logic is implemented
4. Portal pages will require authentication enforcement in a future phase
5. The app will be installed via `bench get-app` + `bench install-app rbp_app`
