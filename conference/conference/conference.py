from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Conference"),
			"items": [
				{
					"type": "doctype",
					"name": "Homepage",
					"description": _("Settings for website homepage"),
				}
			]
		}
	]
