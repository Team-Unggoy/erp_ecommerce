from __future__ import unicode_literals
import json

import frappe
from frappe.utils.response import build_response
from ecommerce_app.ecommerce_web.utils.helper import jsonify

STATUS_CODES = {
	200: "Success",
	201: "Created",
	204: "No Content",
	206: "Partial Content",
	400: "The server cannot or will not process the request due to an apparent client error.",
	401: "Unauthorized",
	403: "Unauthorized",
	404: "The requested resource could not be found",
	500: "Internal Server Error",
	503: "Service Unavailable",
	504: "Gateway Timeout"
}

def webResponse(status_code=200, data=[], error=None, endpoint=None):
	"""
		Custom API Json Responses: next-app usage.
	"""
	response = build_response("json")

	response.status_code = status_code
	res = {'status_message': STATUS_CODES[status_code]}
	res.update({'data': data})
	if error:
		res.update({'error': error})
	response.data = jsonify(res)

	if status_code != 200:
		response.headers['Access-Control-Allow-Origin'] = frappe.db.get_value("OnOurWay Settings", "OnOurWay Settings", 'url')
		
	return response
