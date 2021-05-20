from __future__ import unicode_literals
import frappe
import json

from on_our_way_app.on_our_way_web.utils.response import webResponse
from ecommerce_app.ecommerce_web.api.server_info import get_server_info

@frappe.whitelist()
def getServer():
	try:
		return webResponse(200, data=get_server_info())
	except Exception as e:
		frappe.log_error(frappe.get_traceback())
		return webResponse(
			500,
			error="error_response",
			data={'message': 'error_response', 'err': str(e)},
			endpoint="get_page"
		)
