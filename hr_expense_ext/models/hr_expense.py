from datetime import date
from odoo import api, fields, models, _


class HrExpense(models.Model):
    _inherit = "hr.expense"

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        readonly=False,
        required=True,
        index=True,
        ondelete='restrict',
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        index=True,
        ondelete='restrict',
    )
    odometer = fields.Float(string="Odometer")
    product_is_fuel = fields.Boolean(compute='_compute_is_fuel')
    
    @api.onchange('product_id')
    def _compute_is_fuel(self): 
        for expense in self:   
            fuel = self.env["cost.fleet.vehicle.fuel"].search([]).filtered(lambda r: r.product_id.id == self.product_id.id)
            expense.product_is_fuel= bool(fuel.product_id.id)


   #TODO - Si es combustible calcular precio unitario
