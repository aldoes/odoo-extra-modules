# -*- coding: utf-8 -*-
{
    'name': "Hr Expense Data",

    'summary': "Hr Expense Data",

    'description': """
Module for data to Hr Expense
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Hr',
    'version': '17.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr',"hr_expense"],

    # always loaded
    "data": [
         "data/expenses_data.xml",
         "data/hr_expense_menu.xml"
    ],
    'license':"LGPL-3",
}

