
from odoo import models, fields, api


class PlanSale(models.Model):
    _inherit = 'sale.order'
    business_plan = fields.Many2one('plan.sale.order')



    #Show form create business plan
    def action_create_plan(self):
     course_form = self.env.ref('business_plan.view_plan_sale_order_form', False)
     sale_order_id = self.id
     return {

         'name': 'New Course',

         'type': 'ir.actions.act_window',

         'res_model': 'plan.sale.order',

         'view_type': 'form',

         'view_mode': 'tree,form',

         'target': 'new',

         'views': [(course_form.id, 'form')],

         'view_id': 'course_form.id',


         'flags': {'action_buttons': True},

         'context': {'default_sale_order_id': sale_order_id},

     }





