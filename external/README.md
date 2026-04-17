# External Projects

Use this directory for non-Frappe OSS projects and standalone services that
live alongside the Frappe workspace.

Examples:

- standalone frontend apps
- API services
- workers
- CLIs
- vendored upstream repositories

Notes:

- Prefer adding one directory per project, for example `external/my-app`.
- If the project tracks an upstream repository, a git submodule or subtree is a
  good fit here.
- Do not place these projects in `start/apps/` unless they are actual
  bench-installable Frappe apps.
