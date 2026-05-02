# RBP Platform Validation Report

Validated against the local Frappe bench and a clean minimal Frappe site.

## Summary

`rbp_app` has been validated as the RBP platform layer on top of Frappe.

The platform now:

- Installs successfully on the existing local bench.
- Installs successfully on a clean minimal Frappe-only site.
- Runs migration successfully.
- Clears cache successfully.
- Passes the `rbp_app` test suite.
- Protects customer-facing portal and app routes.
- Leaves `/desk` as the Frappe backend/admin workspace.
- Treats installed Frappe apps as backend capability providers.
- Does not require ERPNext, HRMS, Payments, CRM, LMS, or other optional apps to install.

## Platform Scope

`rbp_app` is the RBP platform layer on top of Frappe.

The platform owns:

- `/portal`
- `/portal/*`
- `/portal/apps`
- `/portal/apps/<app_key>`
- `/app`
- `/app/*`
- RBP platform APIs
- RBP platform DocTypes
- RBP customer-facing route guards
- Dynamic app discovery and entitlement-aware app cards

Frappe still owns:

- `/desk`
- core administration
- backend workflows
- app installation and migration
- standard Frappe authentication internals

Installed Frappe apps are treated as backend capability providers. HRMS is one capability module among many, not the whole platform.

## Existing Local Bench Validation

### Bench

- Bench root: `/Users/gianpaulocoletti/frappe-1/start`
- Site: `frappe.localhost`
- Server: `http://127.0.0.1:8000` with `Host: frappe.localhost`

### Installed Apps

The existing local bench included:

```text
frappe, erpnext, hrms, insights, gameplan, frappe_whatsapp, payments, lms, crm, builder, drive, lending, telephony, helpdesk, meet, education, mail, slides, newsletter, webshop, blog, ecommerce_integrations, school_automations, ff_assignment_portal, fc_saas_helper, frappe_openai_integration, erpnext_australian_localisation, wiki, business_hub, rbp_app
```

### Migration Result

Command:

```sh
bench --site frappe.localhost migrate
```

Result: passed.

Migration emitted a non-fatal warning from another installed app:

```text
school_automations.utils.pull_recordings_for_yesterdays_live_classes is not a valid method: No module named 'offsite_backups'
```

The warning is outside `rbp_app`. Migration continued and completed.

### Cache Result

Command:

```sh
bench --site frappe.localhost clear-cache
```

Result: passed.

### Test Result

`allow_tests` was enabled for `frappe.localhost`.

Command:

```sh
bench --site frappe.localhost run-tests --app rbp_app
```

Result: passed.

Frappe output:

```text
Running 58 unspecified-category tests for rbp_app
Ran 58 rbp_app tests in 0.134s
OK
```

## Clean Minimal Site Validation

### Bench

- Bench root: `/Users/gianpaulocoletti/frappe-1/start`
- Site: `rbp-minimal.localhost`
- Installed apps: `frappe`, `rbp_app`

### Commands

```sh
bench new-site rbp-minimal.localhost --db-root-username root
bench --site rbp-minimal.localhost install-app rbp_app
bench --site rbp-minimal.localhost set-config allow_tests true
bench --site rbp-minimal.localhost migrate
bench --site rbp-minimal.localhost clear-cache
bench --site rbp-minimal.localhost run-tests --app rbp_app
```

### Result

Passed.

Test output:

```text
Running 58 unspecified-category tests for rbp_app
Ran 58 tests in 0.096s
OK
```

### Environment Note

MariaDB 12.2.2 emitted a warning because it is newer than the MariaDB version range currently tested by Frappe.

This is an environment warning, not an `rbp_app` failure.

### Conclusion

`rbp_app` installs, migrates, clears cache, and passes tests on a clean minimal Frappe site without ERPNext, HRMS, Payments, CRM, LMS, or other optional apps installed.

## API Validation Result

Authenticated validation used an Administrator API token and an Administrator session created for local validation.

The temporary session was deleted after route checks.

Validated endpoints:

- `/api/method/rbp_app.api.me.get_current_user`: passed. Returned Administrator user payload, roles, `is_system_manager: true`, and `is_admin: true`.
- `/api/method/rbp_app.api.apps.get_available_apps`: passed. Returned installed app cards plus RBP platform modules.
- `/api/method/rbp_app.api.dashboard.get_home`: passed. Returned current user, available apps, grouped categories, quick links, notifications placeholder, billing placeholder, and integrations status.
- `/api/method/rbp_app.api.integrations.get_integrations_status`: passed. Returned installed app summary data, known app counts, unknown app counts, and platform modules.

Guest API check:

- `/api/method/rbp_app.api.me.get_current_user`: rejected with HTTP 401.

## Route Validation Result

Guest route checks:

- `/portal`: HTTP 302 to `/login?redirect-to=%2Fportal`
- `/portal/dashboard`: HTTP 302 to `/login?redirect-to=%2Fportal%2Fdashboard`
- `/portal/apps/hrms`: HTTP 302 to `/login?redirect-to=%2Fportal%2Fapps%2Fhrms`
- `/app`: HTTP 302 to `/login?redirect-to=%2Fapp`
- `/admin`: HTTP 302 to `/login?redirect-to=%2Fadmin`

Authenticated Administrator session route checks:

- `/portal`: HTTP 200
- `/portal/dashboard`: HTTP 200
- `/portal/apps/hrms`: HTTP 200 through the portal app detail route
- `/app`: HTTP 302 to `/portal`
- `/admin`: HTTP 200

## Issues Found During Validation

The following issues were found and fixed during validation:

- `rbp_app.api.integrations.ADAPTERS` captured adapter function objects at import time. This prevented test patches on adapter modules from affecting the runtime call path.
- `RBP App Entitlement` was not found during test preload because newer platform DocTypes lived outside the synced `RBP App` module DocType path.
- DocType-local metadata-only test files triggered Frappe legacy test-record preloading and caused unrelated ERPNext fixture bootstrap issues.
- `/portal/apps/hrms` originally returned 404 before app routes were added.
- `/app` originally followed Frappe core's `/app -> /desk` redirect before RBP route protection could run.
- The first minimal-site validation attempt failed because an old `rbp-minimal.localhost` site existed with stale database credentials. The stale site was dropped and recreated.

## Fixes Applied

- Updated `rbp_app.api.integrations.ADAPTERS` to store adapter modules and call `adapter.get_summary(user)` at runtime.
- Kept integration exception handling and generic fallback behavior intact.
- Moved `RBP App Entitlement`, `RBP Tenant`, `RBP Subscription`, `RBP Audit Log`, and `RBP Notification` DocType source folders into the synced `rbp_app/rbp_app/rbp_app/doctype` module path.
- Removed DocType-local metadata-only test modules that triggered legacy test-record preloading.
- Verified the platform DocTypes through `bench migrate` and `frappe.get_meta(...)`.
- Added a `before_request` platform guard so protected RBP routes are checked before Frappe website redirects.
- Updated request path detection to work during early request hooks.
- Added dedicated portal app route rules:
  - `/portal/apps` resolves to `portal/apps/index`
  - `/portal/apps/<app_key>` resolves to `portal/apps/app`
- Added test coverage for dedicated portal app routes.
- Kept API protection inside API methods.
- Kept website route protection in both early request and website context layers.

## Current Validation Status

The current validated status is:

- Existing local bench validation: passed.
- Clean minimal Frappe-only site validation: passed.
- `rbp_app` migration: passed.
- `rbp_app` cache clearing: passed.
- `rbp_app` test suite: passed.
- Portal route protection: passed.
- Admin route protection: passed.
- Guest API rejection: passed.
- Authenticated API access: passed.
- Optional app absence handling: passed.
- HRMS absence handling: passed.
- Portal app detail routing: passed.

## Remaining Product Risks

The platform foundation is validated, but the following product work remains:

- `/portal/apps/<app_key>` now resolves to a dedicated app detail page, but richer per-app UX still needs to be built.
- Stripe/payment-provider synchronization is not fully wired.
- Tenant provisioning is not fully wired.
- Document repository behavior is still placeholder-backed.
- Some app-specific adapters are placeholders.
- The entitlement management UI is not complete.
- HRMS has the first safe summary adapter, but deeper HRMS workflows still need client-facing UX.
- ERPNext, CRM, LMS, Helpdesk, Drive, Wiki, and other app adapters need richer read-only summaries before write workflows are added.
- The migration warning from `school_automations` should be reviewed separately because it references a missing `offsite_backups` module outside `rbp_app`.
- An Administrator API secret was generated during validation; rotate or clear it if this local site is shared.
- MariaDB 12.2.2 is newer than the currently tested Frappe MariaDB range and should be treated as an environment warning.

## Release Readiness Conclusion

`rbp_app` is now validated as a Frappe-only installable platform layer.

It can be installed and tested without ERPNext, HRMS, Payments, CRM, LMS, or other optional apps installed.

The next phase should focus on product functionality, starting with:

1. Building the first richer `/portal/apps/hrms` detail experience.
2. Wiring tenant provisioning.
3. Wiring Stripe/payment subscription synchronization.
4. Building the document repository.
5. Expanding adapters for ERPNext, CRM, LMS, Helpdesk, Drive, Wiki, and other installed apps.
