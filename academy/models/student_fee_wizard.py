from odoo import models, fields, api


class StudentFeeWizard(models.TransientModel):
    _name = 'student.fee.wizard'
    _description = 'Student Fee Wizard'

    student_id = fields.Many2one('student.model', string='Student', readonly=True)
    student_name = fields.Char(related='student_id.student_name', readonly=True)
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
    ], string="Class: ", readonly=True)
    student_roll_number = fields.Integer(related='student_id.student_roll_number', readonly=True)
    student_fee = fields.Float(related='student_id.student_fee', readonly=True)
    student_fee_status = fields.Boolean(related='student_id.student_fee_status', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super(StudentFeeWizard, self).default_get(fields)
        if self._context.get('default_student_id'):
            student = self.env['student.model'].browse(self._context['default_student_id'])
            res.update({
                'student_id': student.id,
                'student_name': student.student_name,
                'student_class': student.student_class,
                'student_roll_number': student.student_roll_number,
                'student_fee': student.student_fee,
                'student_fee_status': student.student_fee_status,
            })
        return res