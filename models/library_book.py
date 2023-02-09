from odoo import models, fields


class TutorialLibraryBook(models.Model):
    _inherit = "tutorial.library.book"

    is_available = fields.Boolean("Is Available?")

    isbn = fields.Char(help="A Valid ISBN-13 or ISBN-10")
    publisher_id = fields.Many2one(index=True)

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 10:
            # Logic stuff
            return True
        else:
            return super()._check_isbn()  # type:ignore
