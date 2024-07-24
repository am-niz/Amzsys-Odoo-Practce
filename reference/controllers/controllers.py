# -*- coding: utf-8 -*-
# from odoo import http


# class Reference(http.Controller):
#     @http.route('/reference/reference', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reference/reference/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reference.listing', {
#             'root': '/reference/reference',
#             'objects': http.request.env['reference.reference'].search([]),
#         })

#     @http.route('/reference/reference/objects/<model("reference.reference"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reference.object', {
#             'object': obj
#         })

