# -*- coding: utf-8 -*-
# from odoo import http


# class ComputeEx(http.Controller):
#     @http.route('/compute_ex/compute_ex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compute_ex/compute_ex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('compute_ex.listing', {
#             'root': '/compute_ex/compute_ex',
#             'objects': http.request.env['compute_ex.compute_ex'].search([]),
#         })

#     @http.route('/compute_ex/compute_ex/objects/<model("compute_ex.compute_ex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compute_ex.object', {
#             'object': obj
#         })

