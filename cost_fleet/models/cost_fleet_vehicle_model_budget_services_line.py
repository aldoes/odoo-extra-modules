# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CostFleetVehicleModelBudgetServicesline(models.Model):
   _name = 'cost.fleet.vehicle.model.budget.services.line'
   _inherit = ['abstract.kmcost.fields'] 
   _description = 'Line Links the model Budget with services'
   _sql_constraints = [('service_uniq', 'unique(budget_id,service_type_id)', "Duplicate service line"), ]

   budget_id = fields.Many2one('cost.fleet.vehicle.model.budget',string='Budget', required=True,ondelete="cascade")
   service_type_id = fields.Many2one('fleet.service.type',string='Services', required=True,ondelete="restrict")
   obs = fields.Text(string="Details")
   
   # @api.depends('km_use')
   # def _compute_cost_by_km(self):
   #    for line in self:
   #       line.cost_km = 0.0
   #       #line.currency_id = self.env['res.currency']
   #       # if line.km_use == 0.0:
   #       #    line.cost_km = 0.0
   #       # else:
   #       #    line.cost_km = line.price / (line.taxes_id.amount/100) / line.km_use #formula provisoria
   #    TODO usar calculo de impuesto incluido o no


