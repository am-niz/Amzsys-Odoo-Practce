from odoo import fields, models


class LibraryMember(models.Model):
    _name = "member.model"
    _description = "Library Member"

    member_image = fields.Image(max_width=128, max_height=128)
    member_name = fields.Char(required=True)
    member_address = fields.Char(required=True)
    member_city = fields.Char(required=True)
    member_state = fields.Char(required=True)
    member_pin_no = fields.Integer()
    is_library_member = fields.Boolean(string="Library Member")
    member_job = fields.Char(string="Job Position")
    member_phone = fields.Integer(string="Phone")
    member_email = fields.Char(string="Email")
    member_website = fields.Char(string="Website")
    member_language = fields.Char(string="Language")

