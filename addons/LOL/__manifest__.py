# -*- coding: utf-8 -*-
{
    'name': "LOL",

    'summary': """
        This application consists of a virtual NGO""",

    'description': """
        This app provides functionality for creating, 
        updating, and deleting locations (sede), events, and sponsors. 
        Users can seamlessly manage the information related to various venues, events, 
        and sponsors, facilitating the efficient organization and maintenance of data within the application.
    """,

    'author': "DAM Tartanga Grupo1",
    'website': "http://www.tartanga.eus",
    'icon': "/LOL/static/description/icono.png",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/patrocinador.xml',
        'views/sede.xml',
        'views/evento.xml',
        #'views/templates.xml',
    ],
    # Solo cargar en modo demostración si es necesario
    'demo': [
        'demo/demo.xml',
    ],
}
