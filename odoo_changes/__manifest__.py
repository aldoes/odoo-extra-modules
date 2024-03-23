# -*- coding: utf-8 -*-
{
    'name': "Odoo Changes",

    'summary': "Odoo Changes Default Configuration",

    'description': """
Module to change Default Configuration of initial Instalacion Parameters
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Cost',
    'version': '17.0.0.0.1',


    'depends': ['base','maintenance'],

    # always loaded
    "data": [
        "security/maintenance_sec.xml",
        "views/maintenance_views.xml",
    ],
    'license':"LGPL-3",
}

