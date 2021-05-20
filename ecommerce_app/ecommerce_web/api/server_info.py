import frappe
from ecommerce_app.ecommerce_web.utils.helper import get_server


def get_server_info():
    return get_server().__dict__