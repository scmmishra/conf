# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ConferenceParticipant(Document):
	pass


@frappe.whitelist(allow_guest=True)
def register(name, email, organization, event="IndiaOS 2019"):
	part = frappe.new_doc("Conference Participant")
	part.full_name = name
	part.email = email
	part.organization = organization
	part.event = event
	part.save(ignore_permissions=True)
