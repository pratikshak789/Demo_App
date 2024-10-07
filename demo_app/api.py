
import frappe

@frappe.whitelist(allow_guest= True)
def get_name():
    return "Hello I am Pratiksha"

def throw_emoji(doc, event):
    frappe.throw("🕵️‍♀️")

def send_payment_reminders():
    pass

def get_query_conditions_for_vehicle(user):
    return "name = 1"
    