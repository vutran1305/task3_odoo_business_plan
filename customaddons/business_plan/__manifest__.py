# -*- coding: utf-8 -*-
{
    'name': "Business_plan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vũ Trần",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/business_plan_view.xml',
        # 'views/aprroval_line_view.xml',
        'views/show_form_business_in_quotation.xml',
        'security/security.xml',
        'wizard/success_message.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,

}
