from __future__ import unicode_literals
from frappe import _


def get_data(): 
	return [
		{
			"label": _("Reports"),
			"icon": "icon-star",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Daily Unapproved Timesheet Summary",
					"label": _("Daily Unapproved Timesheet Summary"),
					"description": _("Daily Unapproved Timesheet Summary"),
					"doctype": "Daily Unapproved Timesheet Summary",
				}
			]
		},
		{
			"label": _("Task Group"),
			"icon": "icon-star",
			"items": [
				{
					"type": "page",
					"name": "task-group",
					"label": _("Task Group"),
					"description": _("Task Group"),
				}
			]
		}
	]			