# Milestone 8: Entitlements and Member Benefits

## Repository

`info-rbp/frappe-project`

## Completed scope

This milestone validates entitlement and member benefit enforcement.

Confirmed:

- Entitlement service exists.
- Membership entitlements can be granted and synced.
- Admin grant and revoke is available.
- `applications_provisioning` remains disabled for this rollout.
- Focused entitlement tests exist in the backend repo.

## Validation commands

    python3 -m compileall rbp_app/rbp_app
    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_milestone8_entitlements
    bench --site hrms.localhost run-tests --app rbp_app

## Completion criteria

Milestone 8 is complete when:

- Entitlement focused tests pass.
- Full suite passes.
- Application provisioning entitlement remains disabled.
- Entitlement state can support portal and member benefits.
