// Copyright (c) 2024, pratikshak and contributors
// For license information, please see license.txt

frappe.ui.form.on("vehicle", {
	refresh(frm) {

	},

    get_summary(frm){
        frm.get_field("summary").$wrapper.append("<h5>Here is your summary</h5>")
    }
});
