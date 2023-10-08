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
    'name': 'Employee Bonus Management',
    'version': '15.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """
                Apps will add bonus management functioality for employee
        
        Employee bonus, hr bonus, hr employee bonus, bonus management
Employee Bonus Management
Odoo Employee Bonus Management
Bonus management
Odoo bonus management
Hr Bonus for employee
Odoo Hr Bonus for employee
 employee bonus based on employee, by group, by department wise
odoo  employee bonus based on employee, by group, by department wise
Bonus Notification to many employee in one click
Odoo Bonus Notification to many employee in one click
Bonus Allowance in Employee Payslip
Odoo Bonus Allowance in Employee Payslip
Employee bonus
Odoo employee bonus
HR bonus
Odoo HR bonus
HR bonus management
Odoo HR Bonus management
HR Bonuses
Odoo HR BonusesHR Employee Bonuses
Odoo HR Employee Bonuses
HR Bonus Details
Odoo HR Bonus Details
Employee Bonus and Payroll Integration
Odoo Employee Bonus and Payroll Integration
Hr Employee Bonus
Odoo Hr Employee Bonus
Create Bonus for Employee
Odoo Create Bonus for Employee
Bonus E-Mail reminder to employee
Odoo Bonus E-Mail reminder to employee
Bonus in payslip
Odoo Bonus in payslip

    """,
    'summary': 'Apps will add bonus management functioality for employee,Bonus Allowance in Employee Payslip,Bonus Notification to many employee,Employee Bonus and Payroll Integration,Employee bonus,hr bonus, hr employee bonus, bonus management,Bonus for Employee',
    'author': 'Devintelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['hr', 'om_hr_payroll'],
    'data': ['security/ir.model.access.csv',
            'views/hr_employee_bonus.xml',
            'data/hr_employee_bonus_email_data.xml',
            'data/hr_payroll_data.xml',],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'qweb': [],    
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price':25.0,
    'currency':'EUR',  
    'live_test_url':'https://youtu.be/w_i1un5e7Hc',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
