from odoo import fields, models, api
from datetime import datetime


class BusinessPlan(models.Model):
    _name = 'plan.sale.order'
    name = fields.Text("Name", required=True)
    quotation_id = fields.Many2one('sale.order', required=True)
    business_information = fields.Text("Business information")
    state = fields.Selection([('new', 'New'), ('sent', 'Plan sent'), ('accept', 'Accept'), ('callceled', "Callceled")],
                             string='Action Plan', default='new', required=True)
    approver_line = fields.One2many('approval.line', 'plan_id', string='Approver Lines', required=True)
    sale_order_state = fields.Selection(related='quotation_id.state', string="Order State")

    # If click button send message
    def send_mail_template(self):
        for record in self:
            record.state = 'sent'
            record.quotation_id.business_plan = record
            user_ids = record.approver_line.partner_id
            print(user_ids)
            print(user_ids.ids)
            partner_ids =[]
            for user in user_ids:
                partner_ids.append(user.partner_id.id)
            print(partner_ids)

            body = "Bạn có 1 plan cần phê duyệt! " + datetime.now().strftime("%H:%M:%S  %d/%m/%Y")
            record.quotation_id.message_post( message_type='notification', partner_ids=partner_ids, body=body)

        message_id = self.env['message.wizard'].create({'message': "Invitation is successfully sent"})
        return {
            'name': 'Successfull',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'message.wizard',
            'res_id': message_id.id,
            'target': 'new'
        }

    def confirm_order(self):
        for record in self:
            record.quotation_id.state = 'done'
