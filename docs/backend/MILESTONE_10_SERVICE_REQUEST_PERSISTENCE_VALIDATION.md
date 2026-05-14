# Milestone 10: Backend Service Request Persistence Validation

## Repository

`info-rbp/frappe-project`

## Completed scope

This milestone validates backend persistence for service request flows.

Expected persisted flows:

- Decision Desk
- DocuShare
- Connectivity and NBN
- Risk Advisor
- The Fixer
- Marketplace listing and enquiry

## Validation commands

    python3 -m compileall rbp_app/rbp_app
    bench --site hrms.localhost migrate
    bench --site hrms.localhost clear-cache
    bench --site hrms.localhost run-tests --app rbp_app
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_service_request_persistence
    bench --site hrms.localhost run-tests --app rbp_app --module rbp_app.tests.test_portal_service_activity

## Completion criteria

Milestone 10 is complete when service records persist, reference IDs are generated, portal activity can read them, admin can inspect them, and bench tests pass.
