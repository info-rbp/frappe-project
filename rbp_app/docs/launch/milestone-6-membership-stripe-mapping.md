# Milestone 6: Membership Plans and Stripe Mapping

## Implemented

- Membership plan schema now supports canonical `price`, `active`, and `included_entitlements` fields alongside legacy compatibility fields.
- Membership plan listing normalizes checkout data for portal/frontend consumers.
- Checkout validation now rejects missing, inactive, or placeholder Stripe price IDs before purchase can start.
- Added an idempotent seed patch for `Free Account` and `Premium Membership`.
- Added focused Milestone 6 tests for seeding and checkout validation.

## Seed and config notes

- `Free Account` remains non-checkout and has no Stripe price ID.
- `Premium Membership` reads Stripe test IDs from site config or environment variables.
- Placeholder values are intentionally blocked from checkout until replaced with real Stripe test-mode IDs.

## Outstanding runtime validation

- Run site migration so the new patch and DocType fields apply on the target bench.
- Confirm the QA Stripe product and recurring price IDs are set.
- Run the focused Milestone 6 unittest module inside the target bench site.
