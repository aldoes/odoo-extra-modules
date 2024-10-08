# -*- coding: utf-8 -*-
{
    'name': "Fleet Cost",

    'summary': "Fleet Cost Module",

    'description': """
Module for Cost of Fleet
    """,

    'author': "Aldo Escobar",
    'website': "",
    'category': 'Cost',
    'version': '17.0.0.3.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_fiscal_year','purchase','fleet'],
    #'depends': ['base','purchase','fleet',"hr_expense",'account_fiscal_year'],
   

    # always loaded
    "data": [
        "data/cost_fleet_def_data.xml",
        "data/account.tax.group.csv",
        #"data/account.tax.csv",
        "security/ir.model.access.csv",
        "data/cost_fleet_spare_cat.xml",
        "data/product.category.csv",
        "data/cost_fleet_fuel_data.xml",
        "data/cost.fleet.vehicle.fuel.csv",
        "data/cost_fleet_vehicle_data.xml",
        "data/cost_fleet_spare_data.xml",
        "data/cost.fleet.vehicle.model.spare.csv",
        "data/cost_fleet_vehicle_model_budgets.xml",
        "views/account_fiscal_year_views.xml",
        "views/res_company_views.xml",
        "views/product_category_views.xml",
        "views/cost_fleet_vehicle_fuel_view.xml",
        "views/cost_fleet_vehicle_model_spare_view.xml",
        "views/fleet_views.xml",
        "views/cost_fleet_vehicle_model_budget_view.xml",
        "views/cost_fleet_menu.xml",
    ],
    'license':"LGPL-3",
}

