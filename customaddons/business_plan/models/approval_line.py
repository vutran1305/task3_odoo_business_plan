from odoo import fields ,models
from datetime import datetime
class ApprovalLine(models.Model):
    _name = 'approval.line'
    _description = 'ApprovalLine'
    plan_id = fields.Many2one('plan.sale.order', string = 'Business Plan' , ondelete="cascade")
    state = fields.Selection([('wait', 'Waiting for approval'), ('approved', 'Approved') , ('deny' , "Deny")],
                              string='Approval status', default='wait')
    user_id = fields.Many2one('res.users', string='Approver' )
    plan_state = fields.Selection( related = 'plan_id.state', string ="Plan State" )
    is_user = fields.Boolean(default = False , compute = 'identify')



    # If partner click button approve
    def action_button_approve(self):
        for record in self:
            record.state = 'approved'
            check_state = True         # check state of plan
            for line in record.plan_id.approver_lines:
                if line.state != 'approved':
                    check_state = False
                    break
            if check_state:
                record.plan_id.state = 'accept'
            # send message to user create plan
            body = "Approved plan! " + datetime.now().strftime("%H:%M:%S  %d/%m/%Y")
            user_create_plan = [record.plan_id.create_uid.partner_id.id]
            record.plan_id.message_post(message_type='notification', partner_ids= user_create_plan , body=body)

    #If partner click button Deny
    def action_button_deny(self):
        for record in self:
            record.state = 'deny'
            record.plan_id.state = 'callceled'
            # send message to user create plan
            body = "Refuse plan! " + datetime.now().strftime(
                "%H:%M:%S  %d/%m/%Y")
            user_create_plan= [record.plan_id.create_uid.partner_id.id]
            record.plan_id.message_post(message_type='notification', partner_ids=user_create_plan, body=body)

    #Check aprover vs curenet user
    def identify(self):
        for record in self:
            if record.user_id.id == self.env.user.id:
                record.is_user = True
            else:
                record.is_user = False



