# models/my_model.py
from odoo import models, fields


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model with Reference Field'

    name = fields.Char(string='Name', required=True)
    reference_field = fields.Reference(
        string='Reference Field',
        selection=[
            ('res.partner', 'Partner'),
            ('product.template', 'Product'),
            ('sale.order', 'Sale Order')
        ],
    )