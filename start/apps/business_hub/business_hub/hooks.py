app_name = "business_hub"
app_title = "Business Hub"
app_publisher = "Gian Paulo Coletti"
app_description = "Unified Business Portal"
app_email = "gian@example.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "business_hub",
# 		"logo": "/assets/business_hub/logo.png",
# 		"title": "Business Hub",
# 		"route": "/business_hub",
# 		"has_permission": "business_hub.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/business_hub/css/business_hub.css"
# app_include_js = "/assets/business_hub/js/business_hub.js"

# include js, css files in header of web template
# web_include_css = "/assets/business_hub/css/business_hub.css"
# web_include_js = "/assets/business_hub/js/business_hub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "business_hub/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "business_hub/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
role_home_page = {
	"System Manager": "hub",
	"All": "hub"
}

website_route_rules = [
	{"from_route": "/hub/<path:app_path>", "to_route": "hub"},
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "business_hub.utils.jinja_methods",
# 	"filters": "business_hub.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "business_hub.install.before_install"
# after_install = "business_hub.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "business_hub.uninstall.before_uninstall"
# after_uninstall = "business_hub.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "business_hub.utils.before_app_install"
# after_app_install = "business_hub.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "business_hub.utils.before_app_uninstall"
# after_app_uninstall = "business_hub.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "business_hub.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "business_hub.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

has_permission = {
	"Wiki Document": "business_hub.api.check_wiki_permission",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"business_hub.tasks.all"
# 	],
# 	"daily": [
# 		"business_hub.tasks.daily"
# 	],
# 	"hourly": [
# 		"business_hub.tasks.hourly"
# 	],
# 	"weekly": [
# 		"business_hub.tasks.weekly"
# 	],
# 	"monthly": [
# 		"business_hub.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "business_hub.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "business_hub.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "business_hub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "business_hub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["business_hub.utils.before_request"]
# after_request = ["business_hub.utils.after_request"]

# Job Events
# ----------
# before_job = ["business_hub.utils.before_job"]
# after_job = ["business_hub.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"business_hub.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

