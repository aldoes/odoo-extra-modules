from datetime import date
from odoo import api, fields, models, _

class HrExpense(models.Model):
    _inherit = "hr.expense"

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        readonly=False,
        check_company=True,
        required=True,
        index=True,
        ondelete='restrict',
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        check_company=True,
        index=True,
        ondelete='restrict',
    )


    #TODO - Si es pago de combustible habilitar el [CHAPA] automovil
    #TODO - Si es combustible calcular precio unitario
