# RBP Shell Implementation Handoff

---

## 1. Branch

**Branch:** `main`
**Latest commit:** `d4b36c6469` (Auto-generated changes)
**No PR link** — all work was committed directly to `main` via the Emergent platform auto-commit workflow. There is no separate feature branch or pull request.

---

## 2. Files Created and Modified

### Framework-Core Files Modified

**None.** Zero files inside `frappe/` were created, modified, or deleted.

### New: Frappe Custom App — `/app/rbp_app/` (93 source files)

#### App root
| File | Purpose |
|---|---|
| `pyproject.toml` | Python package config (flit, Frappe v17 compat) |
| `license.txt` | MIT license |
| `README.md` | App overview, structure, installation, route coverage |
| `ARCHITECTURE.md` | Shell architecture doc: flow diagram, boundaries, route ownership |
| `ADMIN_APPROACH.md` | Admin strategy: Frappe Desk mapping table, phase plan |

#### App module — `rbp_app/rbp_app/`
| File | Purpose |
|---|---|
| `__init__.py` | Package init, `__version__ = "0.1.0"` |
| `hooks.py` | `web_include_css`, `web_include_js`, `website_route_rules` (commented), `required_apps` |
| `modules.txt` | Frappe module declaration |
| `config/__init__.py` | Package init |
| `config/navigation.py` | `get_primary_nav()`, `get_utility_nav()`, `get_footer_nav()`, `get_portal_sidebar_nav()` |
| `utils/__init__.py` | Package init (empty, for future use) |

#### Shell templates — `rbp_app/rbp_app/templates/`
| File | Purpose |
|---|---|
| `__init__.py` | Package init |
| `shells/public_base.html` | Extends `templates/base.html`. Header + nav + content + footer. |
| `shells/auth_base.html` | Extends `templates/base.html`. Minimal header, centered card, cross-links to public + portal. |
| `shells/portal_base.html` | Extends `templates/base.html`. Sidebar nav, topbar with cross-links to public + admin. |
| `shells/admin_base.html` | Extends `templates/base.html`. Scaffold with Desk notice, cross-links to portal + public. |
| `includes/header.html` | Header bar: logo, 9 primary nav items, utility nav (Search, My Portal, Login, Join). |
| `includes/footer.html` | Footer: 5 column groups (Company, Services, Resources, Support, Account) + rbp_app badge. |
| `includes/mega_menu.html` | Placeholder for expanded nav (hidden, for future use). |
| `includes/portal_sidebar.html` | Portal sidebar: 10 nav items + cross-shell footer links. |
| `includes/admin_shell_elements.html` | Admin UI element concepts (reference only, HTML comments). |

#### Public assets — `rbp_app/rbp_app/public/`
| File | Purpose |
|---|---|
| `css/rbp.css` | Unlimit BaaS-inspired dark-first stylesheet (Outfit font, dark palette, green/purple accents). |
| `js/rbp.js` | Active nav highlighting based on current path. |
| `images/.gitkeep` | Placeholder for static images. |

#### WWW pages — `rbp_app/rbp_app/www/` (70 HTML + 2 Python)

**Public shell (38 pages):**
`index.html`, `index.py`, `about.html`, `contact.html`, `faq.html`, `privacy.html`, `terms.html`, `help/index.html`, `services/index.html`, `services/category.html`, `service/index.html`, `membership/index.html`, `membership/plans.html`, `membership/pro.html`, `membership/ultimate.html`, `membership/compare.html`, `resources/index.html`, `resources/search.html`, `finance/index.html`, `finance/funding.html`, `finance/insurance.html`, `finance/calculators.html`, `finance/learn.html`, `finance/resources.html`, `finance/enquiry.html`, `finance/thank-you.html`, `offers/index.html`, `decision-desk/index.html`, `decision-desk/how-it-works.html`, `decision-desk/request.html`, `decision-desk/thank-you.html`, `documents/index.html`, `templates.html`, `toolkits.html`, `documentation-suites.html`, `product/index.html`, `support/index.html`, `support/contact.html`, `support/help-articles.html`

**Auth shell (6 pages):**
`login.html`, `register.html`, `join.html`, `forgot-password.html`, `reset-password.html`, `verify-account.html`

**Portal shell (13 pages):**
`portal/index.html`, `portal/dashboard.html`, `portal/membership.html`, `portal/library.html`, `portal/resources.html`, `portal/finance/index.html`, `portal/finance/enquiries.html`, `portal/decision-desk/index.html`, `portal/decision-desk/history.html`, `portal/billing.html`, `portal/account.html`, `portal/notifications.html`, `portal/support.html`

**Admin shell (13 pages):**
`admin/index.html`, `admin/content.html`, `admin/services.html`, `admin/resources.html`, `admin/finance.html`, `admin/offers.html`, `admin/decision-desk.html`, `admin/documents.html`, `admin/memberships.html`, `admin/billing.html`, `admin/users.html`, `admin/navigation.html`, `admin/settings.html`

#### Tests
| File | Purpose |
|---|---|
| `tests/__init__.py` | Package init |

### New: Preview Layer — `/app/frontend/` (12 source files)

These files exist **only** because the Emergent preview environment requires a React frontend on port 3000. They mirror the Frappe shell structure for visual preview. They are **not** part of the Frappe custom app.

| File | Purpose |
|---|---|
| `package.json` | React 18 + react-router-dom 6 + lucide-react |
| `public/index.html` | HTML entry point |
| `.env` | `REACT_APP_BACKEND_URL` |
| `src/index.js` | React entry point |
| `src/index.css` | Minimal reset (Outfit font in App.css) |
| `src/App.js` | Route config: all 70+ routes mapped to shell components |
| `src/App.css` | Full Unlimit-inspired dark design system |
| `src/components/ShellNavigator.js` | Shell nav bar: 4 shell links + rbp_app badge |
| `src/components/PublicShell.js` | Header (9 nav + utility) + footer (5 cols) |
| `src/components/AuthShell.js` | Centered card + cross-shell links |
| `src/components/PortalShell.js` | Sidebar (10 nav + cross-links) + topbar |
| `src/components/AdminShell.js` | Admin bar + Desk notice + cross-links |
| `src/components/HomePage.js` | Hero + layers section + cards |
| `src/components/PlaceholderPage.js` | Reusable placeholder with shell badge |
| `src/components/ArchitectureMap.js` | Flow diagram + boundaries + route tree |

### New: Preview Layer — `/app/backend/` (3 source files)

Same rationale — exists only for the Emergent preview (FastAPI on port 8001).

| File | Purpose |
|---|---|
| `.env` | `MONGO_URL`, `DB_NAME` |
| `requirements.txt` | fastapi, uvicorn, python-dotenv, pymongo |
| `server.py` | `/api/health`, `/api/navigation`, `/api/architecture` |
| `tests/test_rbp_api.py` | API tests (created by testing agent) |

### New: Documentation
| File | Purpose |
|---|---|
| `/app/memory/PRD.md` | Product requirements document with backlog |
| `/app/test_reports/iteration_1.json` | Structural validation (109/109 pass) |
| `/app/test_reports/iteration_2.json` | E2E shell testing (100% pass) |
| `/app/test_reports/iteration_3.json` | Cross-shell navigation testing (100% pass) |
| `/app/test_reports/iteration_4.json` | UI redesign visual verification (100% pass) |

---

## 3. Architecture Summary

### Custom app created?
**Yes.** `rbp_app` at `/app/rbp_app/`.

### Custom app name
`rbp_app` (app_name in hooks.py: `"rbp_app"`, app_title: `"Remote Business Partner"`)

### Where the public shell lives
- **Template:** `rbp_app/templates/shells/public_base.html` (extends `frappe/templates/base.html`)
- **Includes:** `rbp_app/templates/includes/header.html`, `footer.html`, `mega_menu.html`
- **Pages:** `rbp_app/www/` — 38 HTML files, each with `{% extends "rbp_app/templates/shells/public_base.html" %}`
- **Assets:** `rbp_app/public/css/rbp.css`, `rbp_app/public/js/rbp.js`
- **Config:** `rbp_app/config/navigation.py`

### Where auth, portal, and admin scaffolds live
- **Auth:** `rbp_app/templates/shells/auth_base.html` → 6 pages in `rbp_app/www/` (login, register, join, forgot-password, reset-password, verify-account)
- **Portal:** `rbp_app/templates/shells/portal_base.html` + `rbp_app/templates/includes/portal_sidebar.html` → 13 pages in `rbp_app/www/portal/`
- **Admin:** `rbp_app/templates/shells/admin_base.html` + `rbp_app/templates/includes/admin_shell_elements.html` → 13 pages in `rbp_app/www/admin/`. Admin is documented as Frappe Desk in `ADMIN_APPROACH.md`. Scaffold pages point users to `/desk`.

### Framework-core files changed and why
**None.** Zero files in `frappe/` were modified. Verified by `git diff HEAD -- frappe/` returning empty. The custom app integrates via Frappe's standard hooks mechanism (`web_include_css`, `web_include_js`, `website_route_rules`).

---

## 4. Route Map

### Public Shell (38 routes) — `public_base.html`

| Route | File | Section |
|---|---|---|
| `/` | `www/index.html` + `index.py` | Home |
| `/about` | `www/about.html` | Company |
| `/contact` | `www/contact.html` | Company |
| `/faq` | `www/faq.html` | Support |
| `/privacy` | `www/privacy.html` | Legal |
| `/terms` | `www/terms.html` | Legal |
| `/help` | `www/help/index.html` | Help |
| `/services` | `www/services/index.html` | Services |
| `/services/<category>` | `www/services/category.html` | Services |
| `/service/<slug>` | `www/service/index.html` | Services |
| `/membership` | `www/membership/index.html` | Membership |
| `/membership/plans` | `www/membership/plans.html` | Membership |
| `/membership/pro` | `www/membership/pro.html` | Membership |
| `/membership/ultimate` | `www/membership/ultimate.html` | Membership |
| `/membership/compare` | `www/membership/compare.html` | Membership |
| `/resources` | `www/resources/index.html` | Resources |
| `/resources/search` | `www/resources/search.html` | Resources |
| `/finance` | `www/finance/index.html` | Finance |
| `/finance/funding` | `www/finance/funding.html` | Finance |
| `/finance/insurance` | `www/finance/insurance.html` | Finance |
| `/finance/calculators` | `www/finance/calculators.html` | Finance |
| `/finance/learn` | `www/finance/learn.html` | Finance |
| `/finance/resources` | `www/finance/resources.html` | Finance |
| `/finance/enquiry` | `www/finance/enquiry.html` | Finance |
| `/finance/thank-you` | `www/finance/thank-you.html` | Finance |
| `/offers` | `www/offers/index.html` | Offers |
| `/decision-desk` | `www/decision-desk/index.html` | Decision Desk |
| `/decision-desk/how-it-works` | `www/decision-desk/how-it-works.html` | Decision Desk |
| `/decision-desk/request` | `www/decision-desk/request.html` | Decision Desk |
| `/decision-desk/thank-you` | `www/decision-desk/thank-you.html` | Decision Desk |
| `/documents` | `www/documents/index.html` | Documents |
| `/templates` | `www/templates.html` | Documents |
| `/toolkits` | `www/toolkits.html` | Documents |
| `/documentation-suites` | `www/documentation-suites.html` | Documents |
| `/product/<slug>` | `www/product/index.html` | Documents |
| `/support` | `www/support/index.html` | Support |
| `/support/contact` | `www/support/contact.html` | Support |
| `/support/help-articles` | `www/support/help-articles.html` | Support |

### Auth Shell (6 routes) — `auth_base.html`

| Route | File |
|---|---|
| `/login` | `www/login.html` |
| `/register` | `www/register.html` |
| `/join` | `www/join.html` |
| `/forgot-password` | `www/forgot-password.html` |
| `/reset-password` | `www/reset-password.html` |
| `/verify-account` | `www/verify-account.html` |

### Portal Shell (13 routes) — `portal_base.html`

| Route | File |
|---|---|
| `/portal` | `www/portal/index.html` |
| `/portal/dashboard` | `www/portal/dashboard.html` |
| `/portal/membership` | `www/portal/membership.html` |
| `/portal/library` | `www/portal/library.html` |
| `/portal/resources` | `www/portal/resources.html` |
| `/portal/finance` | `www/portal/finance/index.html` |
| `/portal/finance/enquiries` | `www/portal/finance/enquiries.html` |
| `/portal/decision-desk` | `www/portal/decision-desk/index.html` |
| `/portal/decision-desk/history` | `www/portal/decision-desk/history.html` |
| `/portal/billing` | `www/portal/billing.html` |
| `/portal/account` | `www/portal/account.html` |
| `/portal/notifications` | `www/portal/notifications.html` |
| `/portal/support` | `www/portal/support.html` |

### Admin Shell (13 routes) — `admin_base.html` (scaffold → Frappe Desk)

| Route | File | Desk Equivalent |
|---|---|---|
| `/admin` | `www/admin/index.html` | `/desk` |
| `/admin/content` | `www/admin/content.html` | Web Page list |
| `/admin/services` | `www/admin/services.html` | RBP Service DocType |
| `/admin/resources` | `www/admin/resources.html` | RBP Resource DocType |
| `/admin/finance` | `www/admin/finance.html` | RBP Finance Enquiry DocType |
| `/admin/offers` | `www/admin/offers.html` | RBP Offer DocType |
| `/admin/decision-desk` | `www/admin/decision-desk.html` | RBP Decision Request DocType |
| `/admin/documents` | `www/admin/documents.html` | RBP Document DocType |
| `/admin/memberships` | `www/admin/memberships.html` | RBP Membership DocType |
| `/admin/billing` | `www/admin/billing.html` | RBP Invoice DocType |
| `/admin/users` | `www/admin/users.html` | `/desk/user` |
| `/admin/navigation` | `www/admin/navigation.html` | Website Settings |
| `/admin/settings` | `www/admin/settings.html` | RBP Settings DocType |

---

## 5. Known Gaps and Incomplete Parts

### Not implemented (by design — explicitly excluded in requirements)
- No business logic, payment logic, referral logic, CMS logic, or calculators
- No custom DocTypes (Services, Membership, Resources, etc.)
- No Frappe Desk workspace for RBP
- No data models or database schema
- No real authentication enforcement on portal routes
- No real admin functionality

### Structural gaps
1. **Dynamic routes are commented out** in `hooks.py`. The `website_route_rules` for `/services/<category>`, `/offers/<slug>`, `/resources/<category>/<slug>`, and `/product/<slug>` exist as comments but are not activated. The corresponding www pages exist as static placeholders.

2. **No `.py` context files** for most www pages. Only `www/index.py` provides a context function. All other pages are HTML-only with no server-side context. Context files are needed when business data is introduced.

3. **`/login` override risk.** `rbp_app/www/login.html` will override `frappe/www/login.html` when the app is installed. This is intentional but the RBP login page is a placeholder — it does not integrate with Frappe's authentication backend. Before going live, this page must either integrate with Frappe's login flow or be removed to let the framework handle it.

4. **`/portal` routes have no authentication gate.** Portal pages are publicly accessible in the shell phase. Frappe's `is_guest` context or login-required checks must be added before production.

5. **The `rbp_app` is not installed into any Frappe bench site.** It exists as a directory structure at `/app/rbp_app/`. To activate it in Frappe, it must be installed via `bench get-app /path/to/rbp_app && bench install-app rbp_app`. Until then, the www pages and hooks are not active in Frappe — they are only visible through the React preview layer.

6. **The preview layer (`/app/frontend/`, `/app/backend/`) is not part of the Frappe app.** It exists solely for the Emergent platform's preview environment. It should not be deployed alongside the Frappe app. It duplicates the shell structure in React for visual review purposes only.

7. **No `setup.py`** in `rbp_app/`. Only `pyproject.toml` is present. Frappe v17 should support pyproject.toml, but if bench requires setup.py, one must be added.

8. **Mega menu is a hidden placeholder.** `includes/mega_menu.html` contains no functional content.

9. **No test coverage for Frappe-specific behavior.** The test reports validate structure and the React preview, but there are no Frappe-native tests (e.g., `bench run-tests --app rbp_app`).
