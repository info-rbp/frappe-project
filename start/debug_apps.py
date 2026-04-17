import importlib
import os
import frappe

# Mocking frappe context if needed, but get_all_apps should work if setup
frappe.init(".")
apps = frappe.get_all_apps(True)

for app_name in apps:
    try:
        mod = importlib.import_module(app_name)
        file_path = getattr(mod, "__file__", "MISSING")
        if file_path is None or file_path == "MISSING":
            print(f"!!! {app_name}: __file__ is {file_path} !!!")
        else:
            print(f"{app_name}: {file_path}")
    except Exception as e:
        print(f"{app_name}: FAILED - {e}")
