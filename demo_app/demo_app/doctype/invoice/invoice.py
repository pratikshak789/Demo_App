# Copyright (c) 2024, pratikshak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Invoice(Document):
	def validate(self):
		
		
		total_price = 0
		for item in self.items:
			rate = item.quantity * item.price
			total_price += rate

		self.total_amount = total_price

		discount = (self.total_amount/100)*10
		self.payable_amount_after_discount = self.total_amount - discount




	



