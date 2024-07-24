from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_brand = fields.Char(string='Product Brand')