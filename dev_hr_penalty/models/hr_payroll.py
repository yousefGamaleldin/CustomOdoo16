# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from datetime import datetime
from odoo import models, api


class hr_payslip(models.Model):
    _inherit = "hr.payslip"
    
    @api.onchange('contract_id')
    def onchange_contract(self):
        amount_input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', 'PENALTY_AMOUNT')], limit=1)
        percentage_input_type_id = self.env['hr.payslip.input.type'].search([('code', '=', 'PENALTY_PERCENTAGE')], limit=1)
        if amount_input_type_id and  percentage_input_type_id:
            penalty_obj = self.env['hr.penalty']
            penalty_amt = penalty_per = 0.0
            vals=[]
            if self.contract_id:
                penlaty_ids = penalty_obj.search([('state', 'in', ['done']), ('applied_date', '>=', datetime.strptime(str(self.date_from), '%Y-%m-%d')), ('applied_date', '<=', datetime.strptime(str(self.date_to), '%Y-%m-%d'))])
                for pan_id in penlaty_ids:
                    for penalty in penalty_obj.browse(pan_id.id):
                        employees_id =penalty.employee_id.id
                        if self.contract_id.employee_id.id == employees_id:
                            if penalty.penalty_target == 'amount':
                                penalty_amt += penalty.amount
                            if penalty.penalty_target == 'per':
                                penalty_per += penalty.percentage_amt
            if penalty_amt:
                vals.append((0,0,{
                    'input_type_id': amount_input_type_id.id,
                    'amount': penalty_amt,
                }))
            if penalty_per:
                vals.append((0,0,{
                    'input_type_id': percentage_input_type_id.id,
                    'amount': penalty_per,
                }))
            self.input_line_ids = vals
        

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
