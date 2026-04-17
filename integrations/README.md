# Integrations

Use this directory for thin integration layers between Frappe apps and
non-Frappe OSS projects.

Examples:

- auth/session bridges
- API proxy services
- sync jobs
- webhook adapters
- configuration glue

Suggested pattern:

- upstream or third-party code lives in `external/`
- workspace-specific bridge code lives in `integrations/`

This keeps vendor code separate from local integration logic and makes upgrades
less painful.
