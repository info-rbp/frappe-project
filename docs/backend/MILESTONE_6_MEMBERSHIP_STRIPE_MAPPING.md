# Milestone 6: Membership Plans and Stripe Mapping

## Repository

`info-rbp/frappe-project`

## Completed scope

This milestone validates Membership Plan to Stripe product and price mapping.

Confirmed:

- `RBP Membership Plan` has Stripe product and price fields.
- Membership seed patch is registered.
- Focused Stripe mapping tests exist in the backend repo.
- Real QA Stripe product and price IDs remain external configuration.

## Stripe QA requirement

Real Stripe test product and price IDs must be configured in QA before live QA checkout testing.

No live Stripe keys are committed.

## Validation commands

    python3 -m compileall rbp_app/rbp_app
    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_milestone6_membership_stripe_mapping
    bench --site hrms.localhost run-tests --app rbp_app

## Completion criteria

Milestone 6 is complete when:

- Membership Plan schema supports Stripe mapping.
- Seed patch is registered.
- Focused tests pass.
- Full suite passes.
- Real QA Stripe test price remains external configuration.
