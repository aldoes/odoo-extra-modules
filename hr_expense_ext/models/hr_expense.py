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
    
    def _compute_is_fuel(self):
        #TODO - Verificar si es fuel
        self.product_is_fuel= False


    #TODO - Si es pago de combustible habilitar el [CHAPA] automovil
    #TODO - Si es combustible calcular precio unitario
