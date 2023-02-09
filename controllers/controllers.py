# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.tutorial.controllers.main import Books  # type:ignore


class BooksExtend(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if (available := kwargs.get("available")) is not None:
            # Logic stuff: "available"
            all_books = response.qcontext["books"]
            available_books = all_books.filtered("is_available")
            response.qcontext["books"] = available_books

        return response
