# -*- coding: utf-8 -*-
# from odoo import http


# class BusinessPlan(http.Controller):
#     @http.route('/business_plan/business_plan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/business_plan/business_plan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('business_plan.listing', {
#             'root': '/business_plan/business_plan',
#             'objects': http.request.env['business_plan.business_plan'].search([]),
#         })

#     @http.route('/business_plan/business_plan/objects/<model("business_plan.business_plan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('business_plan.object', {
#             'object': obj
#         })
