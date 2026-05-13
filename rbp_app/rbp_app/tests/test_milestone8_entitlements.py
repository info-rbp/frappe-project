from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import MagicMock, patch

import frappe

from rbp_app.services import billing, entitlements


class TestMilestone8Entitlements(TestCase):
    def test_applications_provisioning_is_disabled(self):
        with patch.object(entitlements, "doctype_exists", return_value=True):
            with self.assertRaises(frappe.ValidationError):
                entitlements.grant_entitlement(
                    app_key="applications_provisioning",
                    user="member@example.com",
                    tenant="TENANT-1",
                )

    def test_membership_grant_excludes_applications_provisioning(self):
        subscription = SimpleNamespace(
            name="SUB-1",
            tenant="TENANT-1",
            member="member@example.com",
            plan="Premium Membership",
            current_period_start="2026-05-01",
            current_period_end="2026-06-01",
        )

        with patch.object(entitlements, "grant_entitlement", side_effect=lambda **kwargs: kwargs) as grant:
            result = entitlements.grant_membership_entitlements(subscription=subscription)

        granted_keys = [call.kwargs["app_key"] for call in grant.call_args_list]

        self.assertIn("membership", granted_keys)
        self.assertIn("portal", granted_keys)
        self.assertIn("offers", granted_keys)
        self.assertIn("resources", granted_keys)
        self.assertIn("applications_interest", granted_keys)
        self.assertNotIn("applications_provisioning", granted_keys)
        self.assertEqual(len(result), len(entitlements.MEMBERSHIP_ENTITLEMENT_KEYS))

    def test_has_entitlement_rejects_disabled_key(self):
        self.assertFalse(
            entitlements.has_entitlement(
                app_key="applications_provisioning",
                user="member@example.com",
            )
        )

    def test_has_entitlement_delegates_for_enabled_key(self):
        with patch.object(entitlements, "user_has_entitlement", return_value=True) as user_has:
            self.assertTrue(entitlements.has_entitlement("offers", user="member@example.com"))

        user_has.assert_called_once_with("offers", user="member@example.com")

    def test_billing_update_syncs_entitlements_after_paid_event(self):
        event = SimpleNamespace(
            related_name="SUB-1",
            status="Paid",
            provider_customer_id="cus_123",
            provider_payment_id="pi_123",
            name="PAY-1",
        )

        subscription = MagicMock()
        subscription.name = "SUB-1"
        subscription.status = "Draft"
        subscription.payment_status = "Pending"
        subscription.provider_customer_id = None
        subscription.provider_payment_id = None
        subscription.last_payment_event = None

        fake_frappe = SimpleNamespace(
            db=SimpleNamespace(exists=MagicMock(return_value=True)),
            get_doc=MagicMock(return_value=subscription),
            log_error=MagicMock(),
            get_traceback=MagicMock(return_value="traceback"),
        )

        with (
            patch.object(billing, "frappe", fake_frappe),
            patch.object(billing, "sync_subscription_entitlements") as sync,
        ):
            result = billing.update_subscription_from_payment_event(event)

        self.assertIs(result, subscription)
        self.assertEqual(subscription.status, "Active")
        self.assertEqual(subscription.payment_status, "Paid")
        subscription.save.assert_called_once_with(ignore_permissions=True)
        sync.assert_called_once_with(subscription)
