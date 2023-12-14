# -*- coding: utf-8 -*-
from odoo import http

# class Grupo3c(http.Controller):
#     @http.route('/grupo3c/grupo3c/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grupo3c/grupo3c/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grupo3c.listing', {
#             'root': '/grupo3c/grupo3c',
#             'objects': http.request.env['grupo3c.grupo3c'].search([]),
#         })

#     @http.route('/grupo3c/grupo3c/objects/<model("grupo3c.grupo3c"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grupo3c.object', {
#             'object': obj
#         })