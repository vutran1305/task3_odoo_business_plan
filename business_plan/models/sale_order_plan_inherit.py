
from odoo import models, fields, api
from odoo.exceptions import MissingError ,AccessError

class PlanSale(models.Model):
    _inherit = 'sale.order'
    business_plan = fields.Many2one('plan.sale.order')
    plan_state =   fields.Selection( related = 'business_plan.state', string ="Plan State" )

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

    def action_check_plan(self):
        for rec in self:
            if not rec.business_plan:
                raise MissingError("Plan doesn't exits")
            if rec.plan_state != 'accept':
                raise AccessError("Plan is not approval")
            else:
                message_id = self.env['message.wizard'].create({'message': "Plan approval"})
                return {
                    'name': 'Successfull',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'message.wizard',
                    'res_id': message_id.id,
                    'target': 'new'
                }



    # action click button  "Confirm the order."
    def confirm_order(self):
        for record in self:
            record.state = 'done'








