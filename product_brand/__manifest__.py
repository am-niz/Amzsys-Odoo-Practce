# -*- coding: utf-8 -*-
{
    'name': "Product Brand",
    'summary': "Add brand field to products",
    'description': """
    Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
}
