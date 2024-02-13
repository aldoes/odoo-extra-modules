from datetime import date
from odoo import api, fields, models, _

class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    budget_expen = fields.Monetary(string="Budget", currency_field="budg_currency_id")
    budg_currency_id = fields.Many2one('res.currency',string='Budget Currency')
