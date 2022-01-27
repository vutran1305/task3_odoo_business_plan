from odoo import fields ,models

class ApprovalLine(models.Model):
    _name = 'approval.line'
    _description = 'ApprovalLine'
    _check_company_auto = True
    plan_id = fields.Many2one('plan.sale.order', string = 'Business Plan' , ondelete="cascade")
    state = fields.Selection([('wait', 'Waiting for approval'), ('approved', 'Approved') , ('deny' , "Deny")],
                              string='Approval status', default='wait', required=True)
    partner_id = fields.Many2one('res.users', string='Approver' )
    plan_state = fields.Selection( related = 'plan_id.state', string ="Plan State" )


    # If partner click button approve
    def action_button_approve(self):
        self.state = 'approved'
        check_state = 0         # check state of plan
        for line in self.plan_id.approver_line:
            if line.state == 'approved':
                check_state +=1
        if check_state == len(self.plan_id.approver_line):
            self.plan_id.state = 'accept'


    #If partner click button Deny
    def action_button_deny(self):
        self.state = 'deny'
        self.plan_id.state = 'callceled'
        notification_id = (0,0,{
       'res_partner_id':self.env.user.partner_id.id ,
            'notification_type':'inbox'})

        self.partner_id.message_post(body='This receipt has been validated!', message_type='notification',
                                     subtype_xmlid='mail.mt_comment', author_id=self.partner_id.id, notification_id=notification_id)


