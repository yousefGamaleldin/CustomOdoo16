# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields


class hr_penalty(models.Model):
    _name = "hr.penalty"
    _description = "Hr Penalty "

    def action_penalty_mail_sent(self):
        template_pool = self.env['mail.template']    
        mail_template_id=self.env['ir.model.data']._xmlid_lookup('dev_hr_penalty.email_template_edi_employee_penalty')[2]
        if mail_template_id:
            mtp = template_pool.browse(mail_template_id)
            mtp.send_mail(self.id,force_send=True)
        return True

    name = fields.Char('Penalty reseon:', required=True)
    employee_id = fields.Many2one('hr.employee', 'Employee', required=True)
    department_id = fields.Many2one('hr.department', 'Department')
    job_id = fields.Many2one('hr.job', 'Job Title')
    declaration_date = fields.Date(string='Declaration Date')
    applied_date = fields.Date(string='Applied Date', required=True)
    penalty_target = fields.Selection(
        [('amount', 'Amount'), ('per', 'Percentage')], string="Penalty By")
    amount = fields.Integer(string="Penalty Amount")
    percentage_amt = fields.Integer(string="Percentage Amount")
    description = fields.Text(string="Description")
    company_id = fields.Many2one(related='employee_id.company_id',
                                 relation="res.company", string="company",
                                 readonly=True)
    state = fields.Selection([
        ('tentative', 'Draft'),
        ('cancelled', 'Cancelled'),
        ('confirmed', 'Confirmed'),
        ('mail_sent', 'Mails Sent'),
        ('done', 'Done'),
    ], 'Status', default='tentative')

    def do_confirm(self):
        return self.write({'state': 'confirmed'})

    def do_tentative(self):
        return self.write({'state': 'tentative'})

    def do_done(self):
        return self.write({'state': 'done'})

    def do_cancel(self):
        return self.write({'state': 'cancelled'})

    def set_to_draft(self):
        return self.write({'state': 'tentative'})

    def mail_send(self):
        res = False
        if self.employee_id.work_email:
            res = self.action_penalty_mail_sent()
        return self.write({'state': 'mail_sent'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
