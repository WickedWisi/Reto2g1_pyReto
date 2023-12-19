# -*- coding: utf-8 -*-
{
    'name': "LOL",

    'summary': """
        This application consists in a virtual ong""",

    'description': """
        This app provides functionality for creating, 
        updating, and deleting locations (sede), events, and sponsors. 
        Users can seamlessly manage the information related to various venues, events, 
        and sponsors, facilitating the efficient organization and maintenance of data within the application.
    """,

    'author': "DAM Tartanga Grupo1",
    'website': "http://www.tartanga.eus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}