frappe.ui.form.on('Customer', {
	refresh: function(frm) {
		frappe.msgprint("refresh")
		console.log("refresh called")
	 },
	onload:function(frm) {
		console.log("onload called")
	},
	before_save:function(frm) {
		console.log("before_save called")
	 }



	 /*,
	on_save:function(frm) {
		frappe.call({
			method:'ecommerce.ecommerce.custom_script.customer.customer.validate'
			callback : function(r) {
				if(r.message) {
					frape.msgprint("works well")
				}
			}
		})
	}*/
});