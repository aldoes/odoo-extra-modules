from datetime import date
from odoo import api, fields, models, _

class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    budget_expen = fields.Monetary(string="Budget", currency_field="budg_currency_id")
    budg_currency_id = fields.Many2one('res.currency',string='Budget Currency')

    def get_last_expense_line_to_date(self, product, date_limit= date.today()):      
                product.ensure_one()
                '''Get last expense line of active and done expense before or on limit date or return empty record  '''
                return self.env['hr.expense'].get_last_expense_line_to_date(product,date_limit)

