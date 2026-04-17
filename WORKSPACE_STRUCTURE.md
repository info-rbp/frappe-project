# Workspace Structure

This workspace contains both Frappe apps and supporting code that may not be
bench-installable.

## Top-Level Conventions

```text
frappe-1/
├── frappe/              # Core Frappe framework app
├── gameplan/            # Frappe app
├── frappe_whatsapp/     # Frappe app
├── start/               # Local bench workspace and runtime sandbox
├── external/            # Non-Frappe OSS projects and standalone services
└── integrations/        # Thin bridges between Frappe apps and external OSS
```

## Rules

- Put bench-installable Frappe apps in the existing Frappe app locations.
- Put non-Frappe OSS projects in `external/`.
- Put adapters, proxy layers, sync jobs, or auth bridges in `integrations/`.
- Do not place non-Frappe OSS directly in `start/apps/` unless it is a real
  Frappe app that Bench can install.
- Treat `start/` as a local runtime workspace, not the default home for new OSS.

## Recommended Patterns

### `external/`

Use for:

- standalone frontends
- standalone APIs
- workers
- CLIs
- vendored upstream projects tracked as submodules or subtrees

Suggested layout:

```text
external/
├── some-frontend/
├── some-api/
└── upstream-project/
```

### `integrations/`

Use for:

- Frappe-to-OSS auth bridges
- proxy services
- sync jobs
- webhook adapters
- shared configuration glue

Suggested layout:

```text
integrations/
├── some_oss_bridge/
└── another_service_sync/
```

## Integration Guidance

- Prefer HTTP APIs, webhooks, queues, or SSO over direct database coupling.
- Keep ownership boundaries clear: upstream code in `external/`, local glue in
  `integrations/`.
- If an external project needs to appear inside Frappe, wrap it with a thin
  Frappe-facing integration instead of reshaping the OSS into a Frappe app.
