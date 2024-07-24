from odoo import models, fields


class CustomerTemplate(models.Model):
    _inherit = "res.partner"

    account_email = fields.Char(string="Account Email: ", help="Secondary email for accounting purposes")
