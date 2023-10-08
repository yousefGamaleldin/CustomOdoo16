# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'HR Employee Penalty',
    'version': '15.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """
             Manage  Penalty Functioality for hr employee
            
 HR Employee Penalty
Odoo HR Employee Penalty
HR Employee Penalty odoo apps
HR Employee Penalty odoo app
Hr Penalty for employee
Odoo Hr Penalty for employee
Configure Penalty based on employee , by department wise
Odoo Configure Penalty based on employee , by department wise
Penalty Notification to employee in one click
Odoo Penalty Notification to employee in one click
Penalty Deduction in Employee Payslip
Odoo Penalty deduction in Employee Payslip
HR penalties
Odoo HR penalties
HR Employee Penalties
Odoo HR Employee Penalties
Penalty in Employee Payslip
Odoo Penalty in Employee Payslip
Penalty email
Odoo penalty email
HR Penalty Salary Rule
Odoo HR Penalty Salary Rule
Penalty in payslip
Odoo penalty in payslip
Payslip report
Odoo payslip report

    """,
    'summary': 'odoo Hr Penalty functioality for employee, HR Employee Penalty, Penalty management,Penalty for employee,Penalty based on employee , by department wise,Penalty Notification to employee,HR Employee Penalties,Penalty in Employee Payslip',
    'author': 'Devintelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['hr','hr_payroll'],
    'data': [
        'edi/hr_employee_penalty_email_data.xml',
        'security/hr_security_security.xml',
        'security/ir.model.access.csv',
        'views/hr_penalty_view.xml',
        'views/hr_payroll_data.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'qweb': [],    
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price':19.0,
    'currency':'EUR', 
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
