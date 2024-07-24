from odoo import fields, models


class Teachers(models.Model):
    _name = "teacher.model"
    _description = "Teachers Details"
    _rec_name = 'teacher_name'

    # teacher_id = fields.Integer(string="Id: ")
    teacher_name = fields.Char(string="Name: ")
    teacher_gender = fields.Selection([
        ("male","Male"),
        ("female", "Female")
    ])
    teacher_age = fields.Integer(string="Age: ")
    teacher_department = fields.Char(string="Department")
    teacher_salary = fields.Float(string="Salary: ")
    teacher_joining_date = fields.Date(string="Joining Date: ")
    teacher_address = fields.Char(string="Address: ", placeholder="Provide your home address here..")
    teacher_mobile_number = fields.Integer(string="Mobile: ")
    teacher_email = fields.Char(string="Email: ", placeholder="xyz@gmail.com")

    student_list = fields.One2many("student.model","teacher_id")

    teacher_profile_photo = fields.Binary(string="Upload Profile Photo: ", filename="profile")

    teacher_schedule_list = fields.One2many("teaching.schedules.model", "teacher_id", string="Teaching schedules")







