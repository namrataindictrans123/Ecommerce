# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ecommerce"
app_title = "Ecommerce"
app_publisher = "frape"
app_description = "Ecommerce"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "example@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ecommerce/css/ecommerce.css"
# app_include_js = "/assets/ecommerce/js/ecommerce.js"

# include js, css files in header of web template
# web_include_css = "/assets/ecommerce/css/ecommerce.css"
# web_include_js = "/assets/ecommerce/js/ecommerce.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
fixtures=['Custom Field','Property Setter','Role','Print Format']
# doctype_js = {
#     "Customer" : "ecommerce/custom_script/customer/customer.js",
# }
doctype_js = {
	"Customer" : "ecommerce/custom_script/customer/customer.js"
}
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ecommerce.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ecommerce.install.before_install"
# after_install = "ecommerce.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ecommerce.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and event

doc_events = {
	 "Customer": {
	  "validate":"ecommerce.ecommerce.custom_script.customer.customer.create_user"
        # "validate":"ecommerce.ecommerce.custom_script.customer.customer.create_user"
	}
}
#}
# doc_events = {
# 	"User" : {
# 	"validate":"ecommerce.ecommerce.custom_script.customer.customer.create_customer"
# 	"on_save":"ecommerce.ecommerce.custom_script.customer.customer.create_user"
# 	}
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ecommerce.tasks.all"
# 	],
# 	"daily": [
# 		"ecommerce.tasks.daily"
# 	],
# 	"hourly": [
# 		"ecommerce.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ecommerce.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ecommerce.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ecommerce.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ecommerce.event.get_events"
# }


