# -*- coding: utf-8 -*-
{
    'name': "academy",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/students_views.xml',
        'views/teachers_views.xml',
        'views/teaching_schedules_views.xml',
        'views/academy_menu.xml',
        'views/student_fee_wizard_views.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'images': ['static/description/academy.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
