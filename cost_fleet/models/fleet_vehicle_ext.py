# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class FleetVehicleEx(models.Model):
    _inherit  = 'fleet.vehicle'
    _description = 'Vehicle Extender'

    fuel_enab_cat_ids = fields.One2many(
        comodel_name='cost.fleet.vehicle.model.fuels', 
        inverse_name="vehicle_id", 
        string="Fuel Category Enabled")