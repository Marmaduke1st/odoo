from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_local_note = fields.Char(string="Local Note")
