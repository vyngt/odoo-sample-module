from odoo import fields, models


class Member(models.Model):
    _name = "tutorial.library.member"
    _description = "Tutorial Library Member"

    # Delegation inherit
    _inherits = {"res.partner": "partner_id"}

    # Mixin mail
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Member native
    card_number = fields.Char()

    # Delegation inherit
    partner_id = fields.Many2one(
        "res.partner", delegate=True, ondelete="cascade", required=True
    )
