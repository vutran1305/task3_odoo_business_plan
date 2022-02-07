from odoo import fields, models, api
from datetime import datetime


class BusinessPlan(models.Model):
    _name = 'plan.sale.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Text("Name")
    sale_order_id = fields.Many2one('sale.order')
    business_information = fields.Text("Business information")
    state = fields.Selection([('new', 'New'), ('sent', 'Plan sent'), ('accept', 'Accept'), ('callceled', "Callceled")],
                             string='Action Plan', default='new')
    approver_lines = fields.One2many('approval.line', 'plan_id', string='Approver Lines')
    sale_order_state = fields.Selection(related='sale_order_id.state', string="Order State")




    #send message to list user
    def send_mail_template(self):
        for record in self:
            record.state = 'sent'
            record.sale_order_id.business_plan = record.id
            partner_ids =[]
            for line in record.approver_lines:
                partner_ids.append(line.user_id.partner_id.id)
            body = "A business plan has been created that needs approval! " + datetime.now().strftime("%H:%M:%S  %d/%m/%Y")
            record.sale_order_id.message_post( message_type='notification', partner_ids=partner_ids, body=body)

        message_id = self.env['message.wizard'].create({'message': "Invitation is successfully sent"})
        return {
            'name': 'Successfull',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'message.wizard',
            'res_id': message_id.id,
            'target': 'new'
        }


    #action click button  "Confirm the order."
    def confirm_order(self):
        for record in self:
            record.sale_order_id.state = 'done'
