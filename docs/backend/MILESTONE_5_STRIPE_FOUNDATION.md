# Milestone 5: Stripe Foundation

## Repository

`info-rbp/frappe-project`

## Status

Milestone 5 aligns the backend Stripe foundation into `frappe-project`.

## Completed scope

This milestone adds or confirms:

- Stripe backend gateway service
- Payment event processing service
- Billing API
- Signed Stripe webhook API
- Stripe test/live mode guardrails
- Webhook signature verification
- Provider event idempotency
- Subscription/payment status handling
- Stripe-focused tests

## Required backend files

- `rbp_app/rbp_app/services/stripe_gateway.py`
- `rbp_app/rbp_app/services/payment_events.py`
- `rbp_app/rbp_app/api/billing.py`
- `rbp_app/rbp_app/api/stripe_webhooks.py`
- `rbp_app/rbp_app/tests/test_stripe_foundation.py`

## Launch boundary

Stripe is enabled only for test-mode QA validation until production credentials are intentionally configured.

Do not commit real Stripe keys.

## Required behaviour

- Missing Stripe secret key is rejected.
- Live key in test mode is rejected.
- Test key in live mode is rejected.
- Missing webhook secret is rejected.
- Stripe webhook signatures are verified before processing.
- Webhook events are idempotent by provider event ID.
- Successful payment/subscription events record payment events.
- Failed, cancelled, refunded, and disputed paths are either handled or explicitly documented in tests/code.

## Validation commands

    python3 -m compileall rbp_app/rbp_app

    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_stripe_foundation
    bench --site hrms.localhost run-tests --app rbp_app

## Completion criteria

Milestone 5 is complete when:

- Stripe gateway exists in `frappe-project`.
- Payment event service exists in `frappe-project`.
- Billing API exists in `frappe-project`.
- Stripe webhook API exists in `frappe-project`.
- Stripe dependency is declared.
- Stripe-focused tests pass.
- Bench migration passes.
- Full `rbp_app` test suite passes.
- No Stripe secrets are committed.
