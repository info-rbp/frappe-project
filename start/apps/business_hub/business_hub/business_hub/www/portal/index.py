import frappe
from business_hub.api import get_member_context, get_dashboard_summary

def get_context(context):
    context.member_context = get_member_context()
    context.dashboard_summary = get_dashboard_summary()
    context.no_cache = 1
