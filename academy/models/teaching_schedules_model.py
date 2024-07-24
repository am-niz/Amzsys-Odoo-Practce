from odoo import fields, models


class TeachingSchedules(models.Model):
    _name = "teaching.schedules.model"
    _description = "Teaching Schedules"

    teacher_id = fields.Many2one("teacher.model", string="Teacher: ")

    day = fields.Selection([
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday")
    ], string="Day", required=True)

    start_time = fields.Datetime(string="Start Time: ", required=True)
    end_time = fields.Datetime(string="End Time: ", required=True)

