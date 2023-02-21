# -*- coding: utf-8 -*-
{
    "name": "Tutorial Member",
    "description": """
        Extending example
    """,
    "author": "vyngt",
    "website": "https://github.com/vyngt/odoo-sample-module",
    "category": "Services/Library",
    "version": "16.0.1.0.0",
    "depends": ["tutorial", "mail"],
    "data": [
        "security/tutorial_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "application": False,
}
