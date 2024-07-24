from odoo import fields, models, api


class Compute(models.Model):
    _name = "compute.model"
    _description = "Calculating Price after discount"

    product_name = fields.Char(string="Product Name")
    product_price = fields.Float(string="Product Price")
    product_discount = fields.Float(string="Discount")
    product_final_price = fields.Float(string="Final Price", compute="_compute_discounted_price")

    @api.depends('product_price', 'product_discount')
    def _compute_discounted_price(self):
        for record in self:
            record.product_final_price = record.product_price * (1 - record.product_discount / 100)

    @api.model
    def find_products_with_discount(self, *args):
        if args:
            # If called with arguments, use the first one as discount
            discount = args[1]
        else:
            # If called without arguments, try to get discount from context
            discount = self._context.get("discount", 0.0)

        products = self.search([("product_discount", "=", discount)])
        return {
            "type": "ir.actions.act_window",
            "name": f"Products with {discount}% Discount",
            "res_model": "compute.model",
            "view_mode": "tree",
            "domain": [("id", "in", products.ids)],
        }