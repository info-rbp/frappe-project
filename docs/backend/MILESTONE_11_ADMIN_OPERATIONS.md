# Milestone 11: Admin Operations

## Repository

`info-rbp/frappe-project`

## Admin source of truth

Frappe Desk is the operational admin backend for QA.

React `/admin` is not authoritative unless a specific screen is connected to Frappe persistence.

## Required admin visibility

Admins should be able to inspect:

- Tenants
- Business Profiles
- Membership Plans
- Subscriptions
- Payment Events
- Entitlements
- Applications
- Application Interest
- Service Requests
- Notifications
- Notification Delivery
- Audit Logs

## Validation commands

    python3 -m compileall rbp_app/rbp_app
    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app

## Completion criteria

Milestone 11 is complete when Frappe Desk can operate the launch backend and React admin is clearly non-authoritative unless connected.
