# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Devintelle Software Solutions (<http://devintellecs.com>).
#
##############################################################################
from odoo import api, fields, models, _
from datetime import date


class Student(models.Model):
    _name = 'hr.bonus'

    @api.onchange('target', 'country_ids', 'state_ids', 'company_ids',
                  'department_ids', 'job_ids')
    def onchange_target(self):
        company_obj = self.env['res.company']
        emp_obj = self.env['hr.employee']
        bonus_employees = []
        if self.target and self.target == 'country':
            self.employee_ids = False
            employee_id = self.env['hr.employee'].search([('address_id.country_id','in',self.country_ids.ids)])
            for emp in employee_id:
                bonus_employees.append((0,0,{'employee_id': emp.id,
                                        'email': emp.work_email,
                                                }))
        elif self.target and self.target == 'state':
            self.employee_ids = False
            employee_id = self.env['hr.employee'].search([('address_id.state_id','in',self.state_ids.ids)])
            for emp in employee_id:
                bonus_employees.append((0,0,{'employee_id': emp.id,
                                        'email': emp.work_email,
                                                }))
        elif self.target and self.target == 'company':
            self.employee_ids = False
            employee_id = self.env['hr.employee'].search([('company_id','in',self.company_ids.ids)])
            for emp in employee_id:
                bonus_employees.append((0,0,{'employee_id': emp.id,
                                        'email': emp.work_email,
                                                }))
        elif self.target and self.target == 'department':
            self.employee_ids = False
            employee_id = self.env['hr.employee'].search([('department_id','in',self.department_ids.ids)])
            for emp in employee_id:
                bonus_employees.append((0,0,{'employee_id': emp.id,
                                        'email': emp.work_email,
                                                }))
        elif self.target and self.target == 'job':
            self.employee_ids = False
            employee_id = self.env['hr.employee'].search([('job_id','in',self.job_ids.ids)])
            for emp in employee_id:
                bonus_employees.append((0,0,{'employee_id': emp.id,
                                        'email': emp.work_email,
                                                }))
        self.employee_ids = False
        self.employee_ids = bonus_employees

    name = fields.Char(String='Bonus Summary', required=True)
    date = fields.Date('Declaration Date', required=True)
    applied_date = fields.Date('Applied Date')
    description = fields.Text('Bonus Description')
    amount = fields.Float(string="Bonus Amount", digits=(5, 2))
    percentage_amt = fields.Float(string="Salary Percentage", digits=(3, 2))
    bonus_target = fields.Selection(
        [('amount', 'Amount'), ('per', 'Percentage')], string="Bonus By")
    state = fields.Selection([
        ('tentative', 'Draft'),
        ('cancelled', 'Cancelled'),
        ('confirmed', 'Confirmed'),
        ('mail_sent', 'Mails Sent'),
        ('done', 'Done'),
    ], 'Status', default='tentative')
    employee_ids = fields.One2many('hr.bonus.employee', 'bonus_id',
                                   string='Employees')
    target = fields.Selection(
        [('country', 'Country Wise'), ('state', 'State Wise'),
         ('company', 'Company Wise'),
         ('department', 'Department Wise'), ('job', 'Job Profile Wise')],
        string="Target Group")
    country_ids = fields.Many2many('res.country', 'country_bonus_rel',
                                   'bonus_id', 'country_id', string="Countries")
    state_ids = fields.Many2many('res.country.state', 'state_bonus_rel',
                                 'bonus_id', 'state_id', string="States")
    company_ids = fields.Many2many('res.company', 'company_bonus_rel',
                                   'bonus_id', 'company_id', string="Companies")
    department_ids = fields.Many2many('hr.department', 'department_bonus_rel',
                                      'bonus_id', 'department_id',
                                      string="Departments")
    job_ids = fields.Many2many('hr.job', 'job_bonus_rel', 'bonus_id', 'job_id',
                               string="JOB Profiles")

    def mail_send(self):
        emp_obj = self.env['hr.bonus.employee']
        
        res = False
        for bonus in self:
            for emp in bonus.employee_ids:  
                if not emp.email:
                    continue
                if not emp.mail_sent:
                    res = emp_obj.action_bonus_mail_sent(self._cr,self._uid,self._ids,emp.id)
                    if res:
                        emp.write({'mail_sent': True})
            if not bonus.applied_date:
                bonus.write({'applied_date': date.today()})
        return self.write({'state': 'mail_sent'})

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


class hr_bonus_employee(models.Model):
    _name = "hr.bonus.employee"

    bonus_id = fields.Many2one('hr.bonus', 'Bonus')
    employee_id = fields.Many2one('hr.employee', 'Employee', required=True)
    mail_sent = fields.Boolean('Mail Sent', default=False)
    email = fields.Char('Email', size=124, help="Email of Invited Person")
    company_id = fields.Many2one(related='employee_id.company_id')

    @api.onchange('employee_id')
    def onchange_employee_id(self, employee_id=False):
        if self.employee_id:
            email = (self.employee_id and self.employee_id.work_email) or (self.employee_id and self.employee_id.user_id and self.employee_id.user_id.email) or ''
            return {
                'value': {'email': email}
            }

    def action_bonus_mail_sent(self, cr, uid, ids, context=None):
        '''
        This function opens a window to compose an email, with the edi holiday template message loaded by default
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        template_id = False
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data._xmlid_lookup('dev_hr_bonus.email_template_edi_employee_bonus')[2]
        except ValueError:
            template_id = False
        if template_id:
            template_pool = self.env['mail.template']
            mtp = template_pool.browse(template_id)
            mtp.send_mail(ids[0], force_send=True)
        return self.write({'mail_sent': True})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
