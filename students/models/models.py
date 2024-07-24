# -*- coding: utf-8 -*-
from odoo import fields, models


class Student(models.Model):
    _name = "student.model"
    _description = "Student"

    student_name = fields.Char(string="Name: ")
    student_class = fields.Char(string="Class: ")
    student_address = fields.Text(string="Address: ")
    student_age = fields.Integer(string="Age: ")
    student_fee_status = fields.Boolean(string="Paid: ")
    student_gender = fields.Selection([("male", "Male"),("female", "Female")], string="Gender: ")
    student_roll_number = fields.Integer("Roll No: ")
