# RBP App - Product Requirements Document

## Original Problem Statement
Build an isolated RBP (Remote Business Partner) custom application shell on top of the Frappe v17 framework. The business application must be a coherent shell architecture with four interconnected surfaces: public website, auth layer, member portal, and admin scaffold — all owned by a dedicated custom Frappe app.

## Architecture
- **Framework**: Frappe v17 (17.0.0-dev)
- **Custom App Owner**: `rbp_app` at `/app/rbp_app/`
- **Pattern**: Frappe custom app with filesystem-driven www routing
- **Admin**: Frappe Desk (documented in ADMIN_APPROACH.md)
- **Template Inheritance**: Shell templates extend `frappe/templates/base.html`
- **Preview**: React frontend + FastAPI backend mirror the Frappe structure for Emergent preview

## User Personas
- **Public Visitor**: Browses services, membership, resources, documents
- **Authenticated Member**: Accesses portal dashboard, library, finance, billing
- **Admin/Manager**: Uses Frappe Desk for content and user management

## Core Requirements (Static)
1. Isolated custom app separate from Frappe core
2. 4 shell modes: Public, Auth, Portal, Admin scaffold
3. **Coherent cross-shell linking** between all 4 surfaces
4. Shell Navigator bar showing current position and all other shells
5. Architecture Map documenting complete structure
6. Auth routes with forward/backward shell transitions
7. Portal routes with links to public site, admin, and auth
8. Admin approach: Frappe Desk (documented in ADMIN_APPROACH.md)
9. Zero modifications to frappe/ core

## What's Been Implemented (Jan 2026)

### Iteration 1: Shell Structure
- Created `rbp_app` custom Frappe app with 96+ files
- 70 HTML www pages across 4 shell modes
- 4 shell templates, 5 shared includes
- hooks.py, navigation.py, CSS/JS assets

### Iteration 2: Coherent Shell Architecture (Current)
- **Shell Navigator Bar**: Appears on every page, shows all 4 shells with color-coded dots, current shell highlighted, rbp_app ownership badge
- **Architecture Map** (`/architecture`): App owner declaration, application flow diagram (Public → Auth → Portal → Admin), shell boundaries with transition links, complete route tree by shell
- **Cross-Shell Linking**:
  - Public → Auth: Login/Join in header + "My Portal" (green) link
  - Public → Portal: "My Portal" in header utility nav
  - Auth → Public: "Back to site" link in auth card
  - Auth → Portal: "Go to Portal" link in auth card
  - Portal → Public: "Back to Website" in sidebar footer + topbar
  - Portal → Admin: "Admin / Desk" in sidebar footer + topbar
  - Portal → Auth: "Logout" in sidebar + topbar
  - Admin → Public: "Public Site" in admin bar
  - Admin → Portal: "Member Portal" in admin bar
  - Admin → Auth: "Logout" in admin bar
- **Home Page**: "Application Shell Layers" section with 4 clickable cards showing each shell
- **Footer**: Account column with cross-shell links (Login, Join, Portal, Admin)
- **Backend**: `/api/architecture` endpoint documenting full structure programmatically
- **Testing**: 100% pass — Backend 15/15, Frontend all cross-shell navigation verified

### Route Coverage
| Section | Pages | Shell |
|---|---|---|
| Public (general + sections) | 38 | Public |
| Auth | 6 | Auth |
| Portal | 13 | Portal |
| Admin (scaffold) | 13 | Admin |
| Architecture Map | 1 | Standalone |
| **Total** | **71** | |

### Frappe Custom App Structure
```
rbp_app/
├── rbp_app/
│   ├── hooks.py, modules.txt, __init__.py
│   ├── www/ (70 HTML pages across all shells)
│   ├── templates/shells/ (public_base, auth_base, portal_base, admin_base)
│   ├── templates/includes/ (header, footer, mega_menu, portal_sidebar, admin_shell_elements)
│   ├── public/css/rbp.css, public/js/rbp.js, public/images/
│   ├── config/navigation.py
│   └── utils/
├── ARCHITECTURE.md, ADMIN_APPROACH.md, README.md
└── tests/
```

### Iteration 3: UI Redesign - Unlimit BaaS Style (Current)
- **Design language**: Inspired by Unlimit BaaS (https://www.baas.unlimit.com/)
- **Dark-first palette**: Navy-black backgrounds (#060714), deep card surfaces (#0d1028)
- **Accent colors**: Lime-green (#c8ff00) for CTAs and highlights, purple (#c4a8ff) for auth accents
- **Typography**: Outfit font, 800 weight for headlines, uppercase nav labels, generous letter-spacing
- **Hero**: 4rem headline with green accent word, pill-shaped green CTA, blue radial gradient glow
- **Cards**: Dark grid pattern with 1px separator borders (not individual card borders)
- **Nav**: Uppercase links, bordered Join button, green "My Portal" link
- **Portal**: Dark sidebar with green active border indicator, dark content area
- **Auth**: Dark card with subtle border, centered layout on dark background
- **Admin**: Amber accent badges and notice borders on dark background
- **Testing**: 100% pass — all visual elements verified, design tokens confirmed

## Prioritised Backlog

### P0 - Next Phase (Business Data Model)
- Create custom DocTypes for RBP business entities
- Configure Desk list/form views
- Create RBP Desk workspace

### P1 - Dynamic Routes
- Activate website_route_rules in hooks.py
- Implement context providers for dynamic pages

### P2 - Auth & Portal Logic
- Integrate auth shell with Frappe login
- Portal access control (role-based)
- Mega menu with section content

### P3 - Business Logic (Future)
- Calculators, referral logic, payment, CMS
