# Milestone 7: Tenant and Account Provisioning

## Repository

`info-rbp/frappe-project`

## Completed scope

This milestone aligns customer signup and account provisioning into the backend source-of-truth repository.

Validated scope:

- Signup service exists.
- Signup provisions or links Frappe User.
- Signup provisions or links RBP Tenant.
- Signup provisions or links Business Profile.
- Signup provisions or links Subscription.
- Baseline entitlements are granted where applicable.
- Portal context can be returned.

## Validation commands

    python3 -m compileall rbp_app/rbp_app
    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_signup
    bench --site hrms.localhost run-tests --app rbp_app

## Completion criteria

Milestone 7 is complete when:

- `services/signup.py` exists in `frappe-project`.
- Signup or tenant/account provisioning tests pass where available.
- Full `rbp_app` suite passes.
- Signup remains backend-authoritative.
