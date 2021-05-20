import frappe
import json

def jsonify(data):
    """
        Serialize data to JSON
    """
    return json.dumps(data, default=default)

def get_server():
    return frappe.get_single("Server Info")