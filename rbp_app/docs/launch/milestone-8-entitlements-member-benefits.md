# Milestone 8: Entitlements and Member Benefits

## Implemented

- Explicit member entitlement service.
- Entitlement catalog for membership, portal, billing, notifications, offers, resources, documents, services, marketplace, and applications interest.
- Applications provisioning is disabled for this rollout.
- Portal/user entitlement listing API.
- Entitlement check API.
- Admin grant/revoke entitlement APIs.
- Admin sync from subscription state API.
- Membership entitlement grant helper.
- Membership entitlement suspension helper.
- Billing payment-event update now triggers entitlement sync.
- Unit tests for disabled Applications provisioning, membership grants, entitlement checks, and billing sync.

## Deliberately disabled

- `applications_provisioning`

Applications may be registered/managed separately, but customer-facing provisioning remains disabled until the next rollout.

## Acceptance criteria covered

- Stripe/payment success can grant membership entitlements through subscription sync.
- Portal can read entitlements through `list_my_entitlements`.
- Applications provisioning entitlement is not granted.
- Admin can manually grant/revoke entitlements.
- Expired/cancelled/failed subscription states can suspend entitlements.
