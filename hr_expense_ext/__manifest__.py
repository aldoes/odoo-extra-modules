# -*- coding: utf-8 -*-
{
    'name': "Hr Expense Extender",

    'summary': "Hr Expense Extender",

    'description': """
Module to extend Hr Expense Module
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Hr',
    'version': '17.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',"hr_expense"],

    # always loaded
    "data": [
        "views/hr_expense_menu.xml",
        "views/hr_expense_views.xml",
        "data/expenses_data.xml",
    ],
    'license':"LGPL-3",
}

