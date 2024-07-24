from odoo import fields, models


class Students(models.Model):
    _name = "student.model"
    _description = "Students Details"

    # student_id = fields.Integer(string="Id: ")
    student_name = fields.Char(string="Name: ")
    student_class = fields.Selection([
        ("first", "1st"),
        ("second", "2nd"),
        ("third", "3rd"),
        ("fourth", "4th"),
        ("fifth", "5th"),
        ("sixth", "6th"),
        ("seventh", "7th"),
        ("eighth", "8th"),
        ("ninth", "9th"),
        ("tenth", "10th")
    ], string="Class: ")
    student_roll_number = fields.Integer(string="Roll No: ", required=True)
    student_age = fields.Integer(string="Age: ")
    student_dob = fields.Date(string="DOB: ")
    student_address = fields.Text(string="Address: ")
    student_mobile_number = fields.Char(string="Mobile: ")
    student_email = fields.Char(string="Email: ")
    student_gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female")
    ], string="Gender")
    student_fee = fields.Float(string="Fee: ", default="2000", readonly=True)
    student_fee_status = fields.Boolean(string="Paid: ", help="Annual school fee paid or not?")

    teacher_id = fields.Many2one("teacher.model", string="Teacher: ")

    student_certificate_file = fields.Binary(string="Upload Profile Photo: ", filename="profile")

    if_paid = fields.Char(string="If Paid ?", readonly=True)
    currency_id = fields.Many2one("res.currency", string="Select Currency: ")
    Amount = fields.Monetary(string="Amount: ")

    student_profile_photo = fields.Image(string="Upload Picture", max_width=100, max_height=128, help="upload student "
                                                                                                      "profile photo")

    def action_view_fee_details(self):
        return {
            'name': 'Student Fee Details',
            'type': 'ir.actions.act_window',
            'res_model': 'student.fee.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_student_id': self.id},
        }
