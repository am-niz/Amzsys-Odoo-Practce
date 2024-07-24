# -*- coding: utf-8 -*-
# from odoo import http


# class Schools(http.Controller):
#     @http.route('/schools/schools', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schools/schools/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('schools.listing', {
#             'root': '/schools/schools',
#             'objects': http.request.env['schools.schools'].search([]),
#         })

#     @http.route('/schools/schools/objects/<model("schools.schools"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schools.object', {
#             'object': obj
#         })

