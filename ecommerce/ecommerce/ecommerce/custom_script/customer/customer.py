from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


def create_user(doc,method=None):
	print("=========validate called==========")
	user = frappe.new_doc("User") 
	user.email = doc.email
	full_name = doc.customer_name
	user.insert()
	user.save()
	frappe.db.commit()

	

