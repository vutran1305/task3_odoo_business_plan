from odoo import models,api,fields

class MessageWizard(models.TransientModel):
    _name = 'message.wizard'

    message = fields.Text('Message', required=True)


    def action_ok(self):
        """ close wizard"""
        return {'type': 'ir.actions.act_window_close'}